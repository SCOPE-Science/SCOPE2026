"""descent2.py: sound full-2-descent upper bound for E_d: y^2=x(x-9d)(x-729d).
x = b1 u^2, x-9d = b2 v^2, x-729d = b3 w^2; b1b2b3 square; b1|3d, b2|30d, b3|30d (sqf kernels).
Filters (all NECESSARY => drops preserve soundness, inconclusive=>keep):
 R: real sign intervals; M: exhaustive mod p^k on bad primes; L: Legendre filter at good primes.
"""
import json, math, sys
import sympy as sp

def sfdiv_signed(n):
    f = sp.factorint(abs(n))
    divs = [1]
    for p in f:
        divs = divs + [d*p for d in divs]
    out = set()
    for b in divs:
        out.add(b); out.add(-b)
    return sorted(out)

def sqf_kernel(n):
    if n == 0:
        return 0
    f = sp.factorint(abs(n))
    k = 1
    for p, e in f.items():
        if e % 2 == 1:
            k *= p
    return k if n > 0 else -k

def candidates(d):
    D1 = set(sfdiv_signed(3*d))
    D2 = set(sfdiv_signed(30*d))
    trips = set()
    for b1 in D1:
        for b2 in D2:
            b3 = sqf_kernel(b1*b2)
            if b3 in D2:
                trips.add((b1, b2, b3))
    return sorted(trips)

def real_ok(b1, b2, b3, d):
    pts = sorted([0.0, 9*d, 729*d])
    tests = [pts[0]-1.0, (pts[0]+pts[1])/2, (pts[1]+pts[2])/2, (pts[2]+1.0)]
    for x in tests:
        if (x > 0) == (b1 > 0) and ((x-9*d) > 0) == (b2 > 0) and ((x-729*d) > 0) == (b3 > 0):
            return True
    return False

def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p-1)//2, p) == 1 else -1

def mod_pow_ok(A, B, c, p, k, cap=1500000):
    m = p**k
    if m*m > cap:
        return True
    A %= m; B %= m; c %= m
    # index squares of B*v^2
    seen = set()
    for v in range(m):
        seen.add((B*v*v) % m)
    for u in range(m):
        if (A*u*u - c) % m in seen:
            return True
    return False

SMALL_PRIMES = list(sp.primerange(2, 200))

def legendre_ok(A, B, c, bad, ntry=8):
    # for good odd p not dividing A,B,c: need (-AB|p)=1 or (cA|p)=1
    n = 0
    for p in SMALL_PRIMES:
        if p == 2 or p in bad:
            continue
        if (A % p) == 0 or (B % p) == 0 or (c % p) == 0:
            continue
        if legendre(-A*B, p) < 0 and legendre(c*A, p) < 0:
            return False
        n += 1
        if n >= ntry:
            break
    return True

def sel2_upper(d):
    trips = candidates(d)
    badprimes = {2, 3, 5} | set(sp.factorint(abs(d)))
    kept = []
    why = {'R': 0, 'M': 0, 'L': 0}
    for (b1, b2, b3) in trips:
        if not real_ok(b1, b2, b3, d):
            why['R'] += 1
            continue
        c1, c2 = 9*d, 729*d
        ok = True
        for p in sorted(badprimes):
            k = 3 if p == 2 else 2
            if not mod_pow_ok(b1, b2, c1, p, k) or not mod_pow_ok(b1, b3, c2, p, k):
                ok = False
                break
        if not ok:
            why['M'] += 1
            continue
        if not legendre_ok(b1, b2, c1, badprimes) or not legendre_ok(b1, b3, c2, badprimes):
            why['L'] += 1
            continue
        kept.append([b1, b2, b3])
    n = len(kept)
    dim = math.log2(n) if n > 0 and (n & (n-1)) == 0 else None
    return {'d': d, 'ncand': len(trips), 'nkept': n, 'dim': dim, 'kept': kept, 'why': why}

if __name__ == '__main__':
    for a in sys.argv[1:]:
        r = sel2_upper(int(a))
        print(json.dumps({k: r[k] for k in ('d', 'ncand', 'nkept', 'dim', 'why')}))
