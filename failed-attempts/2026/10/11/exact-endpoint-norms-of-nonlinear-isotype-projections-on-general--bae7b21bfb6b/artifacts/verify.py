#!/usr/bin/env python3
import math


def closed(L):
    if L % 2:
        return (2.0 / L) / math.sin(math.pi / (2.0 * L))
    if L % 4 == 0:
        return (4.0 / L) / math.tan(math.pi / L)
    return (4.0 / L) / math.sin(math.pi / L)


def char_order_mod(m, a):
    if m == 1:
        return 1
    return m // math.gcd(m, a)


def lcm(a, b):
    return a // math.gcd(a, b) * b


def product_average(m, n, a, b):
    # lambda(x,y)=exp(2 pi i (a*x/m+b*y/n)) on Z_m x Z_n.
    total = 0.0
    for x in range(m):
        for y in range(n):
            angle = 2.0 * math.pi * ((a * x / m if m > 1 else 0.0) + (b * y / n if n > 1 else 0.0))
            total += abs(math.cos(angle))
    return 2.0 * total / (m * n)

cases = 0
max_err = 0.0
# Noncyclic checks: all characters on Z_m x Z_n for modest factors.
for m in range(1, 17):
    for n in range(1, 17):
        for a in range(m):
            for b in range(n):
                L = lcm(char_order_mod(m, a), char_order_mod(n, b))
                if L <= 2:
                    continue
                direct = product_average(m, n, a, b)
                target = closed(L)
                err = abs(direct - target)
                max_err = max(max_err, err)
                assert err < 3e-12, (m, n, a, b, L, direct, target)
                cases += 1

contractive=[]
for L in range(3,401):
    value=closed(L)
    if abs(value-1.0)<5e-13:
        contractive.append(L)
    if L==4:
        assert abs(value-1.0)<5e-13
    else:
        assert value>1.0+1e-12,(L,value)

assert contractive==[4]
print(f"VERIFY_OK abelian_character_cases={cases} max_formula_err={max_err:.3e} contractive_orders={contractive}")
