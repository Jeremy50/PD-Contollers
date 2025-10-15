# https://www.desmos.com/calculator/auzctdwrhc

import math

T = lambda x: math.e ** x
F0 = lambda x: math.e ** x + x * math.sin(x ** 2)
dF0 = lambda x: math.e ** x + 2 * x ** 2 * math.cos(x ** 2) + math.sin(x ** 2)

t = 0
y = F0(t)

e = 0
e_acc = 0
e_prev = 0
K = 1
dt = 0.00001

while t <= 5:
    
    e = T(t) - y
    e_acc += abs(e) * dt
    print(round(T(t), 5), round(y, 5), round(e, 5), round(e_acc, 5))

    y += ((dF0(t-dt/2) + dF0(t+dt/2)) / 2) * dt + K * (e - e_prev)
    
    e_prev = e
    t += dt

print()
print(e_acc)