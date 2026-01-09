#pragma once

//https://learn.microsoft.com/ko-kr/windows/win32/direct3d12/directx-12-programming-environment-set-up

#include <Windows.h>
#include <assert.h>

#include <cstdlib>
#include <memory>

// STL
#include <string>

#include <iterator>
#include <vector>
#include <list>
#include <map>
#include <unordered_map>

#include <functional>

#include <thread>
#include <mutex>

// DX3D_12
#include <dxgi1_6.h>
#pragma comment(lib, "dxgi.lib")
#include <d3dcommon.h>
#include <d3dcompiler.h>
#pragma comment(lib, "d3dcompiler.lib")
#include <d3d12shader.h>
#include <d3d12.h>
#pragma comment(lib, "d3d12.lib")

#pragma comment(lib, "dxguid.lib")
#pragma comment(lib, "d3dx10.lib")
#pragma comment(lib, "d3dx11.lib")

/*
 * https://learn.microsoft.com/ko-kr/windows/win32/direct3d12/directx-12-programming-environment-set-up?source=recommendations
 https://learn.microsoft.com/ko-kr/windows/win32/dxmath/ovw-xnamath-progguide
 */
#include <DirectXMath.h>

// Framework
#include "Systems/Window.h"

#include "Utility/Macro.h"