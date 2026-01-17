#pragma once
#include "Private/SelectionDependencies.h"

class EngineManager : public Singleton<EngineManager>
{
    friend class Singleton<EngineManager>;

protected:
    virtual void InitializeInstance() override;
    virtual void DestroyInstance() override;
    
public:
    void Update();
    void Render();

private:
    std::unordered_map<UINT, MsgHandler> dictMsgHandler;

    KeyInput* keyInputManager = nullptr;
};
