"""Enumerate supersingular K3 Weil data via cyclotomic orbits.

Model: P(T) = prod_{i=1}^{22} (1 - q*zeta_i T), zeta_i roots of unity,
Gal-stable multiset <=> union of full primitive-d orbits.
Orbit d: size phi(d), trace sum mu(d) (d>1) or 1 (d=1),
B-factor Phi_d(1) (d>1): p0 if d = p0^k else 1.
Weak admissibility for (q=p^a, sigma0): N=lcm of d's; a*N >= 2*sigma0 and a*N even.
m = sum zeta_i. r = mult of 1.
"""
import json, math
from functools import reduce

def phi(n):
    r = n
    p = 2
    nn = n
    primes = set()
    d = 2
    while d * d <= nn:
        if nn % d == 0:
            primes.add(d)
            while nn % d == 0:
                nn //= d
        d += 1 if d == 2 else 2
    if nn > 1:
        primes.add(nn)
    for p in primes:
        r -= r // p
    return r

def mobius(n):
    if n == 1:
        return 1
    d = 2
    nn = n
    cnt = 0
    while d * d <= nn:
        if nn % d == 0:
            nn //= d
            if nn % d == 0:
                return 0
            cnt += 1
        d += 1 if d == 2 else 2
    if nn > 1:
        cnt += 1
    return -1 if cnt % 2 else 1

def Phi_at_1(d):
    # Phi_d(1) for d>1: p if d = p^k else 1
    if d <= 1:
        return None
    # check prime power
    # find prime base
    tmp = d
    pbase = None
    p = 2
    while p * p <= tmp:
        if tmp % p == 0:
            pbase = p
            while tmp % p == 0:
                tmp //= p
            break
        p += 1 if p == 2 else 2
    if pbase is None:
        # d is prime
        return d
    if tmp == 1:
        return pbase
    return 1

DMAX = 200
dorbits = []
for d in range(1, DMAX + 1):
    if phi(d) <= 22:
        dorbits.append(d)
dorbits.sort(key=lambda d: (phi(d), d))
print("num orbit types:", len(dorbits))
print(dorbits)
# orbit info
info = {}
for d in dorbits:
    info[d] = {"phi": phi(d), "mu": mobius(d) if d > 1 else 1,
               "Phi1": Phi_at_1(d), "sum": 1 if d == 1 else mobius(d)}

# enumerate multisets sum phi = 22 via recursion over orbit types
uniq = sorted(set(dorbits), key=lambda d: (info[d]["phi"], d))
res = []
cur = {}
order = uniq

def rec(i, rem):
    if rem == 0:
        res.append(dict(cur))
        return
    if i >= len(order):
        return
    d = order[i]
    s = info[d]["phi"]
    kmax = rem // s
    for k in range(kmax + 1):
        if k:
            cur[d] = k
        rec(i + 1, rem - k * s)
        if k:
            del cur[d]

rec(0, 22)
print("num multisets:", len(res))

def lcm(a, b):
    return a // math.gcd(a, b) * b

data = []
for k in res:
    m = sum(k[d] * info[d]["sum"] for d in k)
    r = k.get(1, 0)
    N = 1
    for d in k:
        N = lcm(N, d)
    B = 1
    for d in k:
        if d > 1:
            B *= info[d]["Phi1"] ** k[d]
    # prime factorization of B (small)
    data.append({"k": {str(d): k[d] for d in k}, "m": m, "r": r, "N": N, "B": B})

# all m (unconstrained Galois) :
allm = sorted(set(x["m"] for x in data))
print("all Gal-stable m values:", allm)

def weak_mset(a, sigma0):
    s = set()
    for x in data:
        N = x["N"]
        if a * N >= 2 * sigma0 and (a * N) % 2 == 0:
            s.add(x["m"])
    return sorted(s)

# tables
tables = {}
for a in [1, 2, 3, 4]:
    for s0 in [1, 5, 10]:
        tables[f"a={a},s0={s0}"] = weak_mset(a, s0)
for k, v in tables.items():
    print(k, v)

# m=22 / m=-22 conditions illustration
# all-plus-one: k={1:22}: N=1,B=1,m=22 ; all-minus-one: need phi(2)=1 x22: k={2:22}, m=-22, N=2, B=2^22
for x in data:
    if x["m"] == 22:
        print("m=22 example:", x["k"], "N=", x["N"], "B=", x["B"])
        break
for x in data:
    if x["m"] == -22:
        print("m=-22 example:", x["k"], "N=", x["N"], "B=", x["B"])
        break

# count multisets per m (weak) for a sample (a=1,s0=1)
sample = [x for x in data if 1 * x["N"] >= 2 and (1 * x["N"]) % 2 == 0]
from collections import Counter
c = Counter(x["m"] for x in sample)
print("a=1,s0=1 weak counts per m:", sorted(c.items()))

with open("output/artifacts/enumeration.json", "w") as f:
    json.dump({"orbit_info": {str(d): info[d] for d in dorbits},
               "num_multisets": len(res),
               "all_m": allm,
               "weak_tables": tables}, f, indent=1)
print("wrote output/artifacts/enumeration.json")
