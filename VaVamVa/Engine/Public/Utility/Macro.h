#pragma once

#define Super __super

#define SAFE_RELEASE(ptr) if (ptr) { (ptr)->Release(); (ptr) = nullptr; }

#define REPEAT(n) for(int i = 0; i < (n); ++i)
#define FOR_INDEX(i, min, max) for((i) = (min); (i) < (max); ++(i))
#define FOR_EACH(iter, container) for ((iter) : (container))

#define BETWEEN_WITH(min, num, max) ((num) >= (min) && (num) <= (max)) 
#define BETWEEN_THAN(min, num, max) ((num) > (min) && (num) < (max))
#define BETWEEN_COM(min, num, max) ((num) >= (min) && (num) < (max))

#define DEVICE Device::Get()->GetDevice()
#define DEVICE_CONTEXT Device::Get()->GetDeviceContext()

