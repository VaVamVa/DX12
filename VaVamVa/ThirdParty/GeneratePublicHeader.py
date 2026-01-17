import os

def update_inner_dependencies(project_dir: str) -> None:
    """
    Updates Public/InnerDependencies.h ONLY if changed.
    """
    public_dir = os.path.join(project_dir, "Public")
    inner_h_path = os.path.join(public_dir, "InnerDependencies.h")

    if not os.path.exists(inner_h_path):
        print(f"Warning: {inner_h_path} not found.")
        return

    # Read existing content
    with open(inner_h_path, 'r', encoding='utf-8') as f:
        old_content = f.read()

    # Compute expected sections
    expected_sections = {}
    for item in os.listdir(public_dir):
        subdir_path = os.path.join(public_dir, item)
        if os.path.isdir(subdir_path):
            headers = [f for f in os.listdir(subdir_path)
                       if f.endswith('.h') and f != 'InnerDependencies.h']
            if headers:
                headers.sort()
                expected_sections[item] = [f"{item}/{h}" for h in headers]

    # Parse existing sections
    existing_sections = []
    lines = old_content.splitlines(keepends=True)
    i = 0
    pragma_lines = []
    while i < len(lines):
        line = lines[i].rstrip('\n')
        if line.strip().startswith('#pragma once'):
            pragma_lines.append(line + '\n')
            i += 1
            continue
        stripped = line.strip()
        if stripped.startswith('//') and len(stripped) > 2 and '/' not in stripped[2:].strip():
            section_name = stripped[2:].strip()
            includes = set()
            i += 1
            while i < len(lines):
                inc_line = lines[i].rstrip('\n').strip()
                if inc_line.startswith('#include "') and inc_line.endswith('"'):
                    path = inc_line[10:-1].strip()
                    if path:
                        includes.add(path)
                if inc_line.startswith('//') and len(inc_line) > 2 and '/' not in inc_line[2:].strip():
                    break
                i += 1
            existing_sections.append((section_name, includes))
        else:
            i += 1

    # Build new content
    new_content = ''.join(pragma_lines)
    if not new_content.endswith('\n\n'):
        new_content += '\n\n'

    added_subdirs = 0
    # Existing sections (union includes)
    for section_name, existing_includes in existing_sections:
        expected_includes = expected_sections.get(section_name, [])
        all_includes = sorted(set(existing_includes) | set(expected_includes))
        new_content += f"// {section_name}\n"
        for inc_path in all_includes:
            new_content += f'#include "{inc_path}"\n'
        new_content += "\n"

    # New sections (sorted) - count added
    new_sections_at_end = sorted([name for name in expected_sections if name not in dict(existing_sections)])
    added_subdirs = len(new_sections_at_end)
    for section_name in new_sections_at_end:
        expected_includes = expected_sections[section_name]
        new_content += f"// {section_name}\n"
        for inc_path in sorted(expected_includes):
            new_content += f'#include "{inc_path}"\n'
        new_content += "\n"

    new_content = new_content.rstrip() + '\n'

    # Write ONLY if changed
    if new_content == old_content:
        print(f"No changes in {inner_h_path}.")
        return

    with open(inner_h_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    if added_subdirs > 0:
        print(f"Updated {inner_h_path}: Added {added_subdirs} new subdirs.")
    else:
        print(f"Updated {inner_h_path}: Fixed includes.")
        

def create_missing_cpp_files(project_dir: str) -> None:
    """
    Scans Public/ subdirectories for .h files and creates corresponding .cpp files
    in Private/ with the same directory structure if they don't exist.
    Uses only #include "framework.h" as per project PCH pattern.
    Returns list of newly created .cpp paths (relative to project_dir).
    """
    public_dir = os.path.join(project_dir, "Public")
    private_dir = os.path.join(project_dir, "Private")
    new_cpp_paths = []
    
    if not os.path.exists(public_dir):
        print(f"Warning: {public_dir} not found.")
        return
    
    for subdir in os.listdir(public_dir):
        public_subdir = os.path.join(public_dir, subdir)
        if not os.path.isdir(public_subdir):
            continue
        
        private_subdir = os.path.join(private_dir, subdir)
        os.makedirs(private_subdir, exist_ok=True)  
        
        headers = [f for f in os.listdir(public_subdir) if f.endswith('.h')]
        for header in headers:
            filename = header[:-2]
            cpp_filename = filename + '.cpp'
            cpp_path = os.path.join(private_subdir, cpp_filename)
            
            if not os.path.exists(cpp_path):
                cpp_content = f'#include "framework.h"\n\n {filename}::{filename}() {{}}'
                with open(cpp_path, 'w', encoding='utf-8') as f:
                    f.write(cpp_content)
                rel_path = os.path.relpath(cpp_path, project_dir).replace('\\', '/')
                new_cpp_paths.append(rel_path)
                print(f"Created: {cpp_path}")
                
    print(f"Created {len(new_cpp_paths)} new definition files.")
    if len(new_cpp_paths) > 0:
        add_generated_cpp_to_vcxproj(project_dir, new_cpp_paths)
        
    return


from xml.dom import minidom
def add_generated_cpp_to_vcxproj(project_dir: str, new_cpp_paths: list[str]) -> None:
    """
    Adds new .cpp to <ItemGroup Label="Definitions"> ONLY.
    """
    vcxproj_path = os.path.join(project_dir, "Engine.vcxproj")
    
    doc = minidom.parse(vcxproj_path)
    root = doc.documentElement
    
    # Find EXACT ItemGroup Label="Definitions"
    target_group = None
    for ig in root.getElementsByTagName('ItemGroup'):
        if ig.getAttribute('Label') == 'Definitions':
            target_group = ig
            break

    if not target_group:
        print("No ItemGroup Label='Definitions' found.")
        return
    
    # Existing Includes in this group
    existing_in_group = set()
    for cl in target_group.getElementsByTagName('ClCompile'):
        inc = cl.getAttribute('Include')
        if inc:
            existing_in_group.add(os.path.normpath(inc).replace('\\', '/'))

    added = 0
    for rel_path in new_cpp_paths:
        norm_path = os.path.normpath(rel_path).replace('/', '\\')
        if norm_path.replace('\\', '/') not in existing_in_group:
            # Create clean ClCompile (NO prefix)
            cl_node = doc.createElement('ClCompile')
            cl_node.setAttribute('Include', norm_path)
            target_group.appendChild(cl_node)
            added += 1
            print(f"Added to Definitions: {norm_path}")
            
    if added > 0:
        # Pretty XML with VS indent (removes extra newlines)
        pretty_xml = doc.toprettyxml(indent='  ')
        clean_xml = pretty_xml.replace('<?xml version="1.0" ?>', '<?xml version="1.0" encoding="utf-8"?>')
        # Remove extra empty lines from toprettyxml
        lines = [line for line in clean_xml.splitlines() if line.strip() or line.startswith('<?')]
        final_xml = '\n'.join(lines) + '\n'

        with open(vcxproj_path, 'w', encoding='utf-8') as f:
            f.write(final_xml)
        print(f"{vcxproj_path} updated (+{added}).")
    else:
        print("No adds.")
