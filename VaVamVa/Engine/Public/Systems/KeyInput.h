#pragma once

class KeyInput
{
public:
    KeyInput();
    ~KeyInput();

    void OnKeyDown(const WPARAM& wParam);
    void OnKeyUp(const WPARAM& wParam);
    bool IsKeyDown(UINT key);

private:
    bool* keys;
};