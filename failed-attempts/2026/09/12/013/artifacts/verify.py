#!/usr/bin/env python3
"""Lane-1082 verifier (stdlib only).

Target: least K0=Q(sqrt(pq)), p<q both 3 mod 4, pq<2500, with ordinary 4-rank 1,
claimed to have Cl_2 = C4 with explicit unramified generator.

Result proved here: NO such field exists. For every pair in the window the
narrow 4-rank is 0 (Redei matrix identically rank 1 via the opposite-sign lemma),
hence the ordinary 4-rank is 0 as well. Independently, exact class numbers via
the reduced-indefinite-form rho-cycle count satisfy v2(h) <= 1 for all 161
fields, confirming 4-rank 0 (and ruling out both C4 and V4).

Steps:
  1. Enumerate all pairs, check discriminant shape D=pq, prime discriminants -p,-q.
  2. Per pair: A=(-p/q), B=(-q/p); assert A == -B; Redei matrix [[x,x],[y,y]]
     has rank exactly 1 -> narrow 4-rank = (t-1)-rank = 0.
  3. Per D: enumerate ALL reduced indefinite forms (completeness from the
     coefficient bounds |a|<sqrt(D) and the b-window), check rho is a
     permutation, count cycles = narrow class number hn; continued-fraction
     period parity gives h_ord; assert 4 does not divide h_ord.
  4. Write output/artifacts/table.json; print VERIFY_OK.
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------- primes / pairs ----------
def primes_upto(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            step = i
            start = i * i
            sieve[start:n + 1:step] = [False] * (((n - start) // step) + 1)
    return [i for i, p in enumerate(sieve) if p]

def kron_pm(a, p):
    """Kronecker/Legendre (a/p) = +/-1 for odd prime p not dividing a."""
    assert a % p != 0
    return 1 if pow(a % p, (p - 1) // 2, p) == 1 else -1

PRIMES = [p for p in primes_upto(2500) if p % 4 == 3]
PAIRS = [(p, q) for i, p in enumerate(PRIMES) for q in PRIMES[i + 1:] if p * q < 2500]
assert len(PAIRS) == 161, len(PAIRS)
assert PAIRS[0] == (3, 7)
DS = [p * q for p, q in PAIRS]
assert len(set(DS)) == len(DS)
assert all(D % 4 == 1 for D in DS)  # discriminant shape: disc = pq

# ---------- Redei 2x2 check ----------
def redei_rank(A, B):
    x = 0 if A == 1 else 1
    y = 0 if B == 1 else 1
    rows = {(x, x), (y, y)}
    rows.discard((0, 0))
    return len(rows)  # distinct nonzero rows of [[x,x],[y,y]]

# ---------- reduced indefinite forms ----------
def reduced_forms(D):
    """Complete enumeration: reduced iff |sqrt(D)-2|a|| < b < sqrt(D).
    Completeness: any reduced form has |a| < sqrt(D) (else 2|a|-sqrt(D) >=
    sqrt(D) > b, contradiction), and b is an integer in the stated window
    with b^2 = D mod 4a. The loop covers exactly this finite box."""
    assert int(math.isqrt(D)) ** 2 != D
    sq = math.sqrt(D)
    out = []
    amax = int(sq) + 2
    for a in range(-amax, amax + 1):
        if a == 0:
            continue
        if abs(a) >= sq:
            continue
        blo = abs(sq - 2 * abs(a))
        b = int(math.floor(blo)) + 1
        while b < sq:
            if (b * b - D) % (4 * a) == 0:
                c = (b * b - D) // (4 * a)
                assert b * b - 4 * a * c == D
                assert abs(sq - 2 * abs(a)) < b < sq
                out.append((a, b, c))
            b += 1
    assert len(out) > 0
    return out

def rho_next(f, D):
    """Unique reduced rho-successor: b1 = -b + 2*c*k in the window.
    Any solution satisfies |k| <= sqrt(D)/|c| + 1 < sqrt(D) + 1, so the
    search box provably contains every candidate; uniqueness is asserted."""
    a, b, c = f
    sq = math.sqrt(D)
    a1 = c
    blo = abs(sq - 2 * abs(a1))
    K = int(sq) + 2
    sols = []
    for k in range(-K, K + 1):
        b1 = -b + k * 2 * a1
        if blo < b1 < sq and (b1 * b1 - D) % (4 * a1) == 0:
            sols.append((a1, b1, (b1 * b1 - D) // (4 * a1)))
    assert len(sols) == 1, (D, f, sols)
    return sols[0]

def narrow_class_number(D):
    S = reduced_forms(D)
    T = set(S)
    img = {}
    for f in S:
        g = rho_next(f, D)
        assert g in T, (D, f, g)  # closure => enumeration complete
        img[f] = g
    assert len(set(img.values())) == len(S)  # bijective: permutation
    seen = set()
    cycles = 0
    for f in S:
        if f in seen:
            continue
        cycles += 1
        x = f
        while x not in seen:
            seen.add(x)
            x = img[x]
    return cycles

def cf_period(D):
    a0 = math.isqrt(D)
    assert a0 * a0 != D
    m, d, a = 0, 1, a0
    per = 0
    while True:
        m = d * a - m
        assert (D - m * m) % d == 0, (D, m, d)
        d = (D - m * m) // d
        a = (a0 + m) // d
        per += 1
        if a == 2 * a0:
            return per

def v2(n):
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    return e

# ---------- main certificate ----------
rows = []
for p, q in PAIRS:
    D = p * q
    A = kron_pm(-p, q)
    B = kron_pm(-q, p)
    assert A == -B, (p, q, A, B)  # opposite-sign lemma, verified per pair
    assert A * B == -1
    r = redei_rank(A, B)
    assert r == 1, (p, q, A, B)
    narrow4 = (2 - 1) - r
    assert narrow4 == 0
    hn = narrow_class_number(D)
    ell = cf_period(D)
    if ell % 2 == 1:
        h = hn  # N(eps) = -1: narrow = ordinary
    else:
        assert hn % 2 == 0, (D, hn)
        h = hn // 2  # N(eps) = +1
    assert h % 4 != 0, (D, h)
    rows.append({"p": p, "q": q, "D": D, "A": A, "B": B,
                 "redei_rank": r, "narrow_4rank": narrow4,
                 "narrow_class_number": hn, "cf_period": ell,
                 "class_number": h, "v2_class_number": v2(h),
                 "ordinary_4rank": 0})

# calibration spot-checks against standard literature values
cal = {(3, 7): 1, (3, 11): 1, (3, 23): 1, (3, 31): 1, (7, 11): 1}
for row in rows:
    key = (row["p"], row["q"])
    if key in cal:
        assert row["class_number"] == cal[key], (key, row["class_number"])

assert all(row["ordinary_4rank"] == 0 for row in rows)
assert all(row["class_number"] % 4 != 0 for row in rows)

with open(os.path.join(HERE, "table.json"), "w") as f:
    json.dump({"n_fields": len(rows), "least_pair": list(PAIRS[0]), "rows": rows},
              f, indent=1)

print("fields:", len(rows))
print("least pair:", PAIRS[0], "h =", rows[0]["class_number"])
print("max class number:", max(r["class_number"] for r in rows))
print("all narrow 4-ranks zero:", all(r["narrow_4rank"] == 0 for r in rows))
print("4 | h anywhere:", any(r["class_number"] % 4 == 0 for r in rows))
print("VERIFY_OK")
