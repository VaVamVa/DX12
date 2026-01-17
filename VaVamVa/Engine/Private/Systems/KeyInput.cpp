#include "framework.h"

KeyInput::KeyInput()
{
    keys = new bool[256] {};
}

KeyInput::~KeyInput()
{
    delete[] keys;
}

void KeyInput::OnKeyDown(const WPARAM& wParam)
{
    keys[wParam] = true;
}

void KeyInput::OnKeyUp(const WPARAM& wParam)
{
    keys[wParam] = false;
}

bool KeyInput::IsKeyDown(UINT key)
{
    if (BETWEEN_COM(0, key, 255))
    {
        return keys[key];
    }
    
#ifdef _DEBUG
    std::cout << "Out Of Range _Param: " << key << std::endl;
#endif
    
    return false;
}
