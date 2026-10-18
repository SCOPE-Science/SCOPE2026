#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 100
assertions = 0

def check(cond):
    global assertions
    assertions += 1
    if not cond:
        raise AssertionError(f"assertion {assertions} failed")

# Represent a+b*alpha by the pair (a,b), using alpha^2 = 1-alpha.
def mul(x, y):
    a,b = x
    c,d = y
    # (a+bA)(c+dA) = ac + (ad+bc)A + bd(1-A)
    return (a*c + b*d, a*d + b*c - b*d)

alpha_pair = (0,1)
p = (1,0)
F0, F1 = 0, 1
for r in range(1, 101):
    p = mul(p, alpha_pair)
    if r == 1:
        Fr, Frm1 = 1, 0
    else:
        F0, F1 = F1, F0 + F1
        Fr, Frm1 = F1, F0
    sign = 1 if r % 2 == 1 else -1
    expected = (-sign * Frm1, sign * Fr)
    check(p == expected)

# High-precision sanity check of the constructive density step.
five = Decimal(5)
alpha = (five.sqrt() - Decimal(1)) / Decimal(2)
for j in range(1000):
    a = Decimal(j) / Decimal(1000)
    b = Decimal(j+1) / Decimal(1000)
    delta = alpha
    r = 1
    while not delta < b-a:
        delta *= alpha
        r += 1
    k = int(a // delta) + 1
    x = Decimal(k) * delta
    check(a < x < b)
    check(Decimal(0) < x < Decimal(1))

print(f"VERIFY_OK {assertions} assertions")
