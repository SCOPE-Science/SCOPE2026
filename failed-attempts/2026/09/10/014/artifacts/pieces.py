#!/usr/bin/env python3
"""Lane-526 target deepening: decide ALL mu>=0, p>0 graded pieces for m<=15.

For each risky piece S^p Omega_X(q) of E_{2,m} tensor O(-1) twist cell:
  enumerate diagonal-mu5-invariant S4-orbit monomial basis (exact),
  evaluate on random X_F 1-jets over F_11 (dF=0 enforced),
  rank = dim H^0(X, S^p Omega(q))^G (orbit sums span invariants; kernel =
  tangency ideal). Rank 0 => piece contributes no G-invariant sections.
Also: fit chi(E_{2,m}(-1)) to quartic, verify leading coeff -215/324.
"""
import itertools, json, random
from fractions import Fraction
P = 11
rng = random.Random(20260910)
PERMS = list(itertools.permutations(range(4)))

def tuples_sum(n, k):
    if k == 1:
        yield (n,); return
    for i in range(n+1):
        for t in tuples_sum(n-i, k-1):
            yield (i,)+t

def sym_p_tuples(p):
    # symmetric exponent patterns in the 4 jet directions summing to p
    out = []
    for e in tuples_sum(p, 4):
        out.append(e)
    return out

def enum_piece_orbits(p, q):
    """Monomials (e, b): x-deg q, Sym^p in x'. diag-invariant, S4-orbits."""
    seen = {}
    for e in tuples_sum(q, 4):
        for b in sym_p_tuples(p):
            w = tuple((e[i]-b[i]) % 5 for i in range(4))
            if len(set(w)) != 1:
                continue
            best = None
            for s in PERMS:
                kk = (tuple(e[i] for i in s), tuple(sorted(tuple(b[i] for i in s))))
                if best is None or kk < best:
                    best = kk
            seen.setdefault(best, 0)
            seen[best] += 1
    reps = sorted(seen)
    # orbit images (as (e,b) with b ordered tuple -> expand)
    imgs = []
    for (e, bs) in reps:
        s = set()
        for t in PERMS:
            s.add((tuple(e[i] for i in t), tuple(bs)))
        # note: b as multiset pattern; evaluation uses one representative fiber exponents
        imgs.append(sorted(s))
    return reps, imgs

def orb_val_piece(images, jet):
    x, xp = jet
    t = 0
    for (e, bs) in images:
        # bs is sorted pattern; actual fiber monomial = prod_i (xp_i)^{b_i} with b the pattern vector
        v = 1
        for i in range(4):
            if e[i]:
                v = v*pow(x[i], e[i], P) % P
            if bs[i]:
                v = v*pow(xp[i], bs[i], P) % P
        t = (t+v) % P
    return t

def add_mod(vec, tgt, piv):
    inv = pow(pow(vec[piv], 4, P), P-2, P)
    s = sum(pow(vec[k], 4, P)*tgt[k] for k in range(4) if k != piv) % P
    tgt[piv] = ((-s)*inv) % P
    return tgt

def rand_X_1jet():
    while True:
        x = [rng.randrange(P) for _ in range(4)]
        if any(x) and sum(pow(v, 5, P) for v in x) % P == 0:
            break
    piv = rng.choice([i for i in range(4) if x[i] % P != 0])
    xp = [rng.randrange(P) for _ in range(4)]
    add_mod(x, xp, piv)
    return (x, xp)

def rank_modp(rows, ncols):
    M = [list(r) for r in rows]
    nr = len(M); rk = 0
    for c in range(ncols):
        piv = None
        for i in range(rk, nr):
            if M[i][c] % P != 0:
                piv = i; break
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        inv = pow(M[rk][c] % P, P-2, P)
        M[rk] = [(v*inv) % P for v in M[rk]]
        for i in range(nr):
            if i != rk and M[i][c] % P != 0:
                f = M[i][c] % P
                M[i] = [(M[i][j]-f*M[rk][j]) % P for j in range(ncols)]
        rk += 1
    return rk

RISKY = [(1,1,7),(2,1,8),(1,2,10),(2,2,11),(3,2,12),(4,2,13),(1,3,13),(2,3,14),(3,3,15)]
jets = [rand_X_1jet() for _ in range(600)]
res = {}
for (p, q, m) in RISKY:
    reps, imgs = enum_piece_orbits(p, q)
    n = len(reps)
    if n == 0:
        res[f"m{m}_S{p}O{q}"] = {"orbits": 0, "rank": 0, "h0G": 0}
        print(f"m={m} S^{p}O({q}): orbits=0 rank=0 h0G=0")
        continue
    rows = [[orb_val_piece(im, jt) for im in imgs] for jt in jets]
    rk = rank_modp(rows, n)
    res[f"m{m}_S{p}O{q}"] = {"orbits": n, "rank": rk, "h0G": rk}
    print(f"m={m} S^{p}O({q}): orbits={n} rank={rk} h0G={rk}")
    if rk > 0:
        print("   reps:", reps)

# chi quartic fit check
def chi_piece(p, q):
    r = p+1; s1 = p*(p+1)//2; s2 = p*(p+1)*(2*p+1)//6
    A2, B = 5, 55
    c2Sp = Fraction(A2*(s1*s1-s2), 2) + B*(2*s2-p*s1)
    t = s1+r*q
    c2E = c2Sp+(r-1)*5*s1*q+Fraction(r*(r-1), 2)*5*q*q
    return r*5-Fraction(5*t, 2)+Fraction(5*t*t, 2)-c2E

def chi_E(m):
    return sum((chi_piece(m-3*j, j-1) for j in range(m//3+1)), Fraction(0))

xs = list(range(1, 16))
ys = [chi_E(m) for m in xs]
# 4th finite difference must be constant = 24*lead
d1 = [ys[i+1]-ys[i] for i in range(14)]
d2 = [d1[i+1]-d1[i] for i in range(13)]
d3 = [d2[i+1]-d2[i] for i in range(12)]
d4 = [d3[i+1]-d3[i] for i in range(11)]
print("4th differences:", set(d4))
print("lead check:", set(d4) == {Fraction(-215, 324)*24}, Fraction(-215, 324)*24)
with open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-526/output/artifacts/pieces_log.json", "w") as f:
    json.dump({"pieces": res, "fourth_diff": str(set(d4))}, f, indent=1)
print("PIECES_OK")
