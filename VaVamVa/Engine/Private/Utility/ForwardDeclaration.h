#pragma once

/*extern struct ID3D11Device* device;
extern struct ID3D11DeviceContext* deviceContext;

extern struct IDXGISwapChain* swapChain;
extern struct ID3D11RenderTargetView* rtv;*/

constexpr int MAX_LOADSTRING = 100;

constexpr int WIN_START_X = 10;
constexpr int WIN_START_Y = 50;

constexpr int SCREEN_WIDTH = 1280;
constexpr int SCREEN_HEIGHT = 720;
constexpr int CENTER_X = SCREEN_WIDTH / 2;
constexpr int CENTER_Y = SCREEN_HEIGHT / 2;

extern HINSTANCE hInst;
extern WCHAR szTitle[MAX_LOADSTRING];
extern WCHAR szWindowClass[MAX_LOADSTRING];

using MsgHandler = LRESULT(CALLBACK*)(HWND, UINT, WPARAM, LPARAM);