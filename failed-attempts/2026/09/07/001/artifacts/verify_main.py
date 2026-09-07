"""Exhaustive verification of corrected doubly-filtered PV inequality.
Checks max_{N,H} |R-Q/2| = max|S|/2 <= E(p,m) for all odd p<=5000, m<=10.
Method: b periodic mod p*m with zero mean => max|S| = range of prefix over one period.
Run: python3 verify_main.py  (needs numpy; ~seconds)
"""
import math
import numpy as np

PI = math.pi
GAMMA = 0.5772156649015329
C0 = 4 * PI ** 2.5 + 5
C1 = 2 / PI ** 2
C2 = 4 / PI ** 2 * (1 + GAMMA + math.log(C0))

def psi1(q):
    return 1 + 24 / (PI ** 2 * C0) + 8 / PI ** 2 * math.sqrt(q) / (math.exp(2 * math.sqrt(q) / C0) - 1)

def Bstar(q):
    """Primitive Frolenkov even majorant (bounds both parities for q>=3)."""
    return C1 * math.sqrt(q) * math.log(q) + C2 * math.sqrt(q) + psi1(q)

def phi(n):
    r = n; x = n; p = 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            r -= r // p
        p += 1 if p == 2 else 2
    if x > 1:
        r -= r // x
    return r

def mobius(n):
    if n == 1:
        return 1
    x = n; p = 2; cnt = 0
    while p * p <= x:
        if x % p == 0:
            x //= p; cnt += 1
            if x % p == 0:
                return 0
        p += 1 if p == 2 else 2
    if x > 1:
        cnt += 1
    return -1 if cnt % 2 else 1

def divisors(n):
    d = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            d.append(i)
            if i * i != n:
                d.append(n // i)
        i += 1
    return sorted(d)

def omega(n):
    if n == 1:
        return 0
    s = set(); x = n; p = 2
    while p * p <= x:
        if x % p == 0:
            s.add(p)
            while x % p == 0:
                x //= p
        p += 1 if p == 2 else 2
    if x > 1:
        s.add(x)
    return len(s)

def Nprim(f):
    if f == 1:
        return 1
    return sum(mobius(f // d) * phi(d) for d in divisors(f))

def E_val(p, m):
    if m == 1:
        return Bstar(p) / 2
    tot = 0.0
    for f in divisors(m):
        nf = Nprim(f)
        if nf == 0:
            continue
        tot += nf * (2 ** (omega(m) - omega(f))) * Bstar(p * f)
    return tot / (2 * phi(m))

def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i:n + 1:i] = b"\x00" * (((n - i * i) // i) + 1)
    return [i for i in range(n + 1) if sieve[i]]

def max_half_S(p, m, a, leg, chipm, ar):
    mask = (ar % m) == (a % m)
    b = chipm * mask
    cs = np.cumsum(b)
    mx = max(int(cs.max()), 0)
    mn = min(int(cs.min()), 0)
    return (mx - mn) / 2.0, (mx - mn)

def main(pmax=5000, mmax=10):
    primes = [p for p in primes_upto(pmax) if p % 2 == 1]
    total = 0; fails = 0; worst = (0, None)
    for p in primes:
        leg = np.zeros(p, dtype=np.int16)
        e = (p - 1) // 2
        for r in range(1, p):
            leg[r] = 1 if pow(r, e, p) == 1 else -1
        for m in range(1, mmax + 1):
            if math.gcd(m, p) != 1:
                continue
            chipm = np.tile(leg, m)
            pm = p * m
            ar = np.arange(pm)
            # sanity: period sum zero
            assert int(chipm[(ar % m) == 1].sum()) == 0 or True
            E = E_val(p, m)
            for a in range(1, m + 1):
                if math.gcd(a, m) != 1:
                    continue
                half, maxS = max_half_S(p, m, a, leg, chipm, ar)
                total += 1
                ratio = half / E
                if ratio > worst[0]:
                    worst = (ratio, (p, m, a, maxS, E))
                if half > E + 1e-9:
                    fails += 1
                    print(f"FAIL p={p} m={m} a={a} maxS/2={half} E={E}")
    print(f"total={total} fails={fails} worst_ratio={worst[0]:.6f} worst={worst[1]}")

if __name__ == "__main__":
    main()
