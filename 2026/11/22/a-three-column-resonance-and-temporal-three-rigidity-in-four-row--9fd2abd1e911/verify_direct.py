#!/usr/bin/env python3
"""Independent direct brute-force check (not an all-length proof)."""

def update(x, n):
    # Packed as four consecutive row bits per column.
    y = 0
    for i in range(n):
        for r in range(4):
            a = (x >> (4*i + r)) & 1
            b = (x >> (4*i + (r+1)%4)) & 1
            c = (x >> (4*((i+1)%n) + r)) & 1
            if a+b+c >= 2:
                y |= 1 << (4*i+r)
    return y

for n in range(3, 6):
    fixed, fixed3 = 0, 0
    for x in range(1 << (4*n)):
        a = update(x, n)
        b = update(a, n)
        c = update(b, n)
        fixed += a == x
        fixed3 += c == x
    p3_states = fixed3-fixed
    assert p3_states == (6 if n%3 == 0 else 0)
    print(f'n={n}, fixed={fixed}, third_return={fixed3}, primitive_three_states={p3_states}, orbits={p3_states//3}')
print('INDEPENDENT DIRECT CHECKS PASSED')
