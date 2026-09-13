"""Numerics: K(1,1;p), normalized value t=K/2sqrt(p), discrepancy D_p for p=3 mod 4.
Checks Koksma lower bound D_p >= |K|/(2*pi*(p-1)) and upper-bound shape."""
import math, cmath

def primes(limit):
    sieve = [True] * (limit + 1)
    out = []
    for i in range(2, limit + 1):
        if sieve[i]:
            out.append(i)
            if i * i <= limit:
                for j in range(i * i, limit + 1, i):
                    sieve[j] = False
    return out

def K11(p):
    s = 0j
    for x in range(1, p):
        xi = pow(x, -1, p)
        s += cmath.exp(2j * math.pi * (x + xi) / p)
    return s.real

def discrep(p):
    xs = sorted(((h + pow(h, -1, p)) % p) / p for h in range(1, p))
    N = len(xs)
    D = 0.0
    for i, x in enumerate(xs):
        D = max(D, abs((i + 1) / N - x), abs(i / N - x))
    return D

print(f'{"p":>5} {"K(1,1;p)":>10} {"|t|":>6} {"D_p":>8} {"Koksma-lb":>9} {"D*sqp/logp":>10}')
big = []
for p in primes(200):
    if p % 4 != 3 or p < 7:
        continue
    K = K11(p)
    t = abs(K) / (2 * math.sqrt(p))
    D = discrep(p)
    lb = abs(K) / (2 * math.pi * (p - 1))
    assert D + 1e-9 >= lb, p
    if t >= 0.5:
        big.append(p)
    print(f'{p:>5} {K:>+10.4f} {t:>6.3f} {D:>8.5f} {lb:>9.5f} {D*math.sqrt(p)/math.log(p):>10.3f}')
print('primes p=3mod4 <=200 with |t|>=1/2 (=>|K|>=sqrt(p)):', big)
