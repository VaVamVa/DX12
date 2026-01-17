#pragma once

#define WIN32_LEAN_AND_MEAN

#pragma region WindowAPI
#include <windows.h>
#include <assert.h>
#include <cstdlib>
#include <memory>
#include <malloc.h>
#include <tchar.h>

// (ProjectDir)Engine\Engine.vcxproj 수정하는 법 -> 프로젝트 우클릭/ [Edit] / [Edit `Engine.vcxproj`]
#include "targetver.h"
#include "resource.h"
#pragma endregion


// STL
#pragma region STL
#include <thread>
#include <mutex>
#include <functional>
#include <iostream>

#include <string>
#include <iterator>
#include <vector>
#include <list>
#include <map>
#include <unordered_map>
#pragma endregion

#pragma region DirectX
//https://learn.microsoft.com/ko-kr/windows/win32/direct3d12/directx-12-programming-environment-set-up
#include <dxgi1_6.h>
#pragma comment(lib, "dxgi.lib")
#pragma comment(lib, "dxguid.lib")

#include <d3dcommon.h>
#include <d3d12shader.h>
#include <d3d12.h>
#pragma comment(lib, "d3d12.lib")
#include <d3d11.h>
#pragma comment(lib, "d3d11.lib")
#include <d3d11on12.h>

#include <d3dcompiler.h>
#pragma comment(lib, "d3dcompiler.lib")

/*
 * DirectX Utilies
 * https://learn.microsoft.com/ko-kr/windows/win32/direct3d12/directx-12-programming-environment-set-up?source=recommendations
 * https://learn.microsoft.com/ko-kr/windows/win32/dxmath/ovw-xnamath-progguide
 */
#include <DirectXMath.h>
#pragma endregion

#pragma region ImGui
#pragma endregion

#pragma region Framework
#include "InnerDependencies.h"
#pragma endregion