# https://www.desmos.com/calculator/vackyxsond

T = 7
K = 2.5
x = 0
dt = 1e-3
t = 0

while (abs(T-x) > 1e-5):
    
    m = K * (T - x)
    x += m * dt
    print(round(x, 5), round(t, 5))
    t += dt

print(t)