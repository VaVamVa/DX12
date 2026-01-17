#include "framework.h"

void EngineManager::InitializeInstance()
{
    keyInputManager = new KeyInput();
    
    dictMsgHandler[WM_DESTROY];
    dictMsgHandler[WM_PAINT];
    dictMsgHandler[WM_KEYDOWN];
    dictMsgHandler[WM_KEYUP];
}

void EngineManager::DestroyInstance()
{
}

void EngineManager::Update()
{
}

void EngineManager::Render()
{
}


