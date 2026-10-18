#!/usr/bin/env python3
import math

r = 1.0
K = 1.0
alpha = 5.0
s = 0.02
Y = 0.6
beta = 0.1

tau_star = math.log(alpha * Y * (1.0 - math.exp(-beta * K)) / s) / s
tau_real = math.log(alpha * Y / s) / s
assert abs(tau_star - 132.9233416526083) < 1e-12
assert abs(tau_real - 250.5317647048128) < 1e-12
assert round(tau_star, 4) == 132.9233

def equilibrium(tau):
    z = s * math.exp(s * tau) / (alpha * Y)
    assert 0.0 < z < 1.0
    x = -math.log(1.0 - z) / beta
    y = (r * Y * x / (s * math.exp(s * tau))) * (1.0 - x / K)
    return x, y

x250, y250 = equilibrium(250.0)
assert x250 > K
assert y250 < 0.0
assert abs(x250 - 45.48890111249169) < 1e-10
assert abs(y250 + 409.07785445982495) < 1e-9

# Positivity switches exactly when x*=K.
z_star = s * math.exp(s * tau_star) / (alpha * Y)
x_star = -math.log(1.0 - z_star) / beta
assert abs(x_star - K) < 1e-12

for tau in (0.0, 50.0, 100.0, 132.0):
    x, y = equilibrium(tau)
    assert 0.0 < x < K and y > 0.0
for tau in (140.0, 200.0, 250.0):
    x, y = equilibrium(tau)
    assert x > K and y < 0.0

print('VERIFY_OK')
print(f'tau_positive_endpoint={tau_star:.15f}')
print(f'tau_real_log_endpoint={tau_real:.15f}')
print(f'x_at_250={x250:.15f}')
print(f'y_at_250={y250:.15f}')
