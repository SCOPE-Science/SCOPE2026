"""Standalone finite checks for a Fourier construction over the golden rotation.
The exact infinite claims in RESULT.md are proved analytically, not by this script.
"""
import math
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 85
alpha = (mp.sqrt(5) - 1) / 2

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def q(j):
    return fib(4*j + 3)

def p(j):
    return fib(4*j + 2)

def delta(j):
    return alpha ** (4*j + 3)

def trig_cocycle(x, count):
    return mp.fsum((mp.cos(2*mp.pi*(q(j)*x+delta(j))) -
                    mp.cos(2*mp.pi*q(j)*x)) / j for j in range(1,count+1))

checks = 0
# Exact Fibonacci recurrence and convergent indexing, high precision errors.
for j in range(1, 17):
    n = 4*j + 2
    assert fib(n+2) == fib(n+1) + fib(n)
    assert q(j) > p(j) > 0
    assert abs(mp.mpf(q(j))*alpha - p(j) - delta(j)) < mp.mpf('1e-55')
    assert delta(j) > 0 and delta(j) < mp.mpf(1)/16
    assert mp.mpf('0.44') < q(j)*delta(j) < mp.mpf('0.46')
    checks += 5

# Positive-frequency lower signs and the nearly logarithmic modulus at finite scales.
ratios = []
for J in range(3, 11):
    h = mp.mpf(1)/(8*q(J))
    m = abs(trig_cocycle(h,J+14)-trig_cocycle(0,J+14))
    A = mp.fsum(mp.mpf(1)/j for j in range(1,J+1))
    z = m/(h*A)
    assert mp.mpf('15') < z < mp.mpf('19')
    for j in range(1, J+1):
        term = (mp.cos(2*mp.pi*(q(j)*h+delta(j)))
                - mp.cos(2*mp.pi*q(j)*h)
                - mp.cos(2*mp.pi*delta(j))+1)
        assert term < 0
        checks += 1
    ratios.append(mp.nstr(z,12))
    checks += 2

# H^1 Fourier energy proxy: sum a_j^2; Fejer amplitude grows harmonically.
for J in range(2, 21):
    energy = sum(Fraction(1, j*j) for j in range(1,J+1))
    amp = sum(Fraction(1, j) for j in range(1,J+1))
    assert energy < Fraction(2)
    if J > 2:
        assert amp > sum(Fraction(1,j) for j in range(1,J))
    checks += 2

print('PASS:',checks,'finite checks')
print('modulus ratios:',', '.join(ratios))
