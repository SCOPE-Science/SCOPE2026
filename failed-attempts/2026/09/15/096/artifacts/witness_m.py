"""Witness analysis for exact m-sets over Fq (q=p^a), supersingular K3, fixed sigma0.

For each Galois-stable root-of-unity multiset (union of full cyclotomic orbits,
total 22): m = trace, r = #{1's}, B = prod_{d>1} Phi_d(1)^{mult} (=|Q(1/q)|).
Artin-Tate (K3, alpha=1): |Br| * |D_Fq| = q * B, |Br| a square.
- r=22 (all ones): D_Fq = p^{2 s0} forced => |Br| = q/p^{2 s0} must be square int
  => m=22 occurs over Fq iff a even and a >= 2*s0 (necessity; sufficiency cond.).
- r=0: D_Fq = 1 forced (rank 0) => |Br| = q*B must be a perfect square.
  => m with an r=0 witness with q*B square is (conditionally) realizable over Fq.
Prints per-m witness tables for sample (p,a) and endpoint theorems.
"""
import json, math

def phi(n):
    r = n
    nn = n
    ps = set()
    d = 2
    while d * d <= nn:
        if nn % d == 0:
            ps.add(d)
            while nn % d == 0:
                nn //= d
        d += 1 if d == 2 else 2
    if nn > 1:
        ps.add(nn)
    for p in ps:
        r -= r // p
    return r

def mobius(n):
    if n == 1:
        return 1
    nn = n
    d = 2
    c = 0
    while d * d <= nn:
        if nn % d == 0:
            nn //= d
            if nn % d == 0:
                return 0
            c += 1
        d += 1 if d == 2 else 2
    if nn > 1:
        c += 1
    return -1 if c % 2 else 1

def Phi_at_1(d):
    if d <= 1:
        return None
    tmp = d
    pb = None
    p = 2
    while p * p <= tmp:
        if tmp % p == 0:
            pb = p
            while tmp % p == 0:
                tmp //= p
            break
        p += 1 if p == 2 else 2
    if pb is None:
        return d
    return pb if tmp == 1 else 1

def is_square(n):
    assert n >= 1
    r = math.isqrt(n)
    return r * r == n

DMAX = 200
dorbits = [d for d in range(1, DMAX + 1) if phi(d) <= 22]
info = {d: {"phi": phi(d), "sum": 1 if d == 1 else mobius(d),
            "Phi1": Phi_at_1(d)} for d in dorbits}
uniq = sorted(set(dorbits), key=lambda d: (info[d]["phi"], d))
res = []
cur = {}

def rec(i, rem):
    if rem == 0:
        res.append(dict(cur))
        return
    if i >= len(uniq):
        return
    d = uniq[i]
    s = info[d]["phi"]
    for k in range(rem // s + 1):
        if k:
            cur[d] = k
        rec(i + 1, rem - k * s)
        if k:
            del cur[d]

rec(0, 22)
data = []
for k in res:
    m = sum(k[d] * info[d]["sum"] for d in k)
    r = k.get(1, 0)
    B = 1
    for d in k:
        if d > 1:
            B *= info[d]["Phi1"] ** k[d]
    data.append({"k": k, "m": m, "r": r, "B": B})

def fmt(k):
    return "{" + ",".join(f"{d}:{k[d]}" for d in sorted(k)) + "}"

# Endpoint theorems
print("=== Endpoint necessity (exact, all p, all sigma0) ===")
print("m=22 (all-ones, r=22, B=1): Fq-admissible iff a even and a>=2*sigma0.")
print("m=-22 (all-minus-one, r=0, B=2^22 square): Fq-admissible iff a even.")
print("  check: q*B = p^a * 2^22 square iff a even. True.")

# r=0 witnesses per m with q*B square, for sample (p,a)
def witnesses(p, a):
    q = p ** a
    out = {}
    for x in data:
        if x["r"] == 0 and is_square(q * x["B"]):
            m = x["m"]
            if m not in out:
                out[m] = (x["k"], x["B"])
    return out

for (p, a) in [(5, 1), (5, 2), (2, 1), (2, 2), (3, 3)]:
    w = witnesses(p, a)
    ms = sorted(w)
    print(f"--- p={p}, a={a}: r=0 square-witness m values ({len(ms)} of 45):")
    print("   ", ms)
    for m in ms:
        k, B = w[m]
        print(f"    m={m}: orbits {fmt(k)} B={B} q*B={p**a*B} square={is_square(p**a*B)}")

# all m admitting any r=0 multiset (ignoring square)
r0m = sorted(set(x["m"] for x in data if x["r"] == 0))
print("m admitting some r=0 multiset:", r0m)
# all m admitting any multiset (full): already known [-22,22] all integers
allm = sorted(set(x["m"] for x in data))
print("all Gal-stable m:", allm)

with open("output/artifacts/witnesses.json", "w") as f:
    json.dump({f"witness_r0_p{p}_a{a}": {str(m): {"orbits": {str(d): v for d, v in k.items()}, "B": B}
                                         for m, (k, B) in sorted(witnesses(p, a).items())}
               for (p, a) in [(5, 1), (5, 2), (2, 1), (2, 2), (3, 3)]}, f, indent=1)
print("wrote output/artifacts/witnesses.json")
