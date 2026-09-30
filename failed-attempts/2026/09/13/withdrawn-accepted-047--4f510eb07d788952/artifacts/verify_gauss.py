"""Verify Re(quartic Gauss period) = sqrt(p) for p = 5 mod 24.

For p == 1 mod 4, T_1 = sum_{x in F_p} exp(2*pi*i*x^4/p)
decomposes as g(chi)+g(phi)+g(chibar). For p == 5 mod 8,
chi(-1) = -1 so g(chi)+g(chibar) is purely imaginary and
Re(T_1) = g(phi) = sqrt(p). This script checks it directly.
"""
import cmath
import math

def T1(p):
    return sum(cmath.exp(2j * math.pi * (pow(x, 4, p) / p)) for x in range(p))

primes = [5, 29, 53, 101, 149, 173, 197, 269, 293, 317, 509, 557]
ok = True
for p in primes:
    assert p % 24 == 5, p
    t = T1(p)
    err = abs(t.real - math.sqrt(p))
    print(f"p={p} Re(T)={t.real:.9f} sqrt(p)={math.sqrt(p):.9f} err={err:.2e} |T|/sqrt(p)={abs(t)/math.sqrt(p):.4f}")
    ok = ok and (err < 1e-9) and (abs(t) >= math.sqrt(p) - 1e-9)
print("ALL_OK" if ok else "MISMATCH")
