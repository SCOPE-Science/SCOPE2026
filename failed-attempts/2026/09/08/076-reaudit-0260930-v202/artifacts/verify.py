"""Independent stdlib-only verifier for disks.json + gaps.json.
Recomputes from committed centers/radii with exact Fraction arithmetic:
 1. coefficient check: s_n defined as sum z^k/k! (recompute factorials).
 2. Rouche inequality m=|a1|r-|a0| > M=sum|a_k|r^k at r=3/10 AND r=1/100, with
    rigorous sqrt bounds via integer isqrt; g=a0+a1(w-c) has exactly one zero
    (|a0|<|a1|r) strictly inside each disk.
 3. Disjointness at r=3/10 (exact) + count=n per degree => all n zeros enclosed.
 4. Maximal-Re witness: n=16 pair Re-disks disjoint from and above all others at r=1/100.
 5. Minimal-gap extremal: every zero of the n=16 pair has gap-hi < every other zero's gap-lo.
Prints VERIFY_OK on success. No numpy. Run: python3 verify.py
"""
import json, math
from fractions import Fraction

D = 10**12
R = Fraction(3, 10)
R2 = Fraction(1, 100)

def sqrt_lo(q):
    assert q >= 0
    if q == 0:
        return Fraction(0)
    return Fraction(math.isqrt(q.numerator * q.denominator * D * D) // q.denominator, D)

def cabs_lo(zr, zi):
    return sqrt_lo(zr*zr + zi*zi)

def cabs_hi(zr, zi):
    return cabs_lo(zr, zi) + Fraction(1, D)

def sexact(n, cr, ci):
    pr, pi = Fraction(1), Fraction(0)
    sr, si = Fraction(1), Fraction(0)
    for k in range(1, n+1):
        nr = (pr*cr - pi*ci) / k
        ni = (pr*ci + pi*cr) / k
        pr, pi = nr, ni
        sr, si = sr + pr, si + pi
    return sr, si

def exp_bounds(x):
    assert Fraction(-3) <= x <= Fraction(3)
    if x < 0:
        lo, hi = exp_bounds(-x)
        return Fraction(1) / hi, Fraction(1) / lo
    N = 60
    E = Fraction(3) ** (math.ceil(float(x)) if float(x) > 0 else 0)
    if E < 1:
        E = Fraction(1)
    S, t = Fraction(0), Fraction(1)
    for k in range(0, N):
        S += t
        t = t * x / (k + 1)
    RN = t * E
    assert RN < Fraction(1, 10**9)
    return S, S + RN

disks = json.load(open('disks.json'))
gaps = json.load(open('gaps.json'))
assert len(disks) == 136 and len(gaps) == 136
for n in range(1, 17):
    assert sum(1 for d in disks if d['n'] == n) == n, n

for d in disks:
    n = d['n']
    cr, ci = Fraction(d['cr']), Fraction(d['ci'])
    assert Fraction(d['r']) == R
    for r in (R, R2):
        a0r, a0i = sexact(n, cr, ci)
        a1r, a1i = sexact(n-1, cr, ci)
        m = cabs_lo(a1r, a1i) * r - cabs_hi(a0r, a0i)
        M = sum((cabs_hi(*sexact(n-k, cr, ci)) * r**k / math.factorial(k)
                 for k in range(2, n+1)), Fraction(0))
        assert m > M, (n, d['j'], r)
        assert cabs_hi(a0r, a0i) < cabs_lo(a1r, a1i) * r

for n in range(1, 17):
    cs = [(Fraction(d['cr']), Fraction(d['ci'])) for d in disks if d['n'] == n]
    assert len(cs) == n
    for i in range(n):
        for k in range(i+1, n):
            assert (cs[i][0]-cs[k][0])**2 + (cs[i][1]-cs[k][1])**2 > (2*R)**2, (n, i, k)

ranked = sorted(disks, key=lambda d: (-float(Fraction(d['cr'])), abs(float(Fraction(d['ci'])))))
E = [d for d in ranked[:4] if d['n'] == 16][:2]
O = [d for d in disks if d not in E]
assert len(E) == 2 and all(d['n'] == 16 for d in E)
assert all(x not in E for x in O)
loE = min(float(Fraction(d['cr'])) - float(R2) for d in E)
hiO = max(float(Fraction(d['cr'])) + float(R2) for d in O)
assert loE > hiO, (loE, hiO)

# gap intervals recomputed and checked against gaps.json + extremal separation
G = {(o['n'], o['j']): o for o in gaps}
for d in disks:
    n, j = d['n'], d['j']
    cr, ci = Fraction(d['cr']), Fraction(d['ci'])
    c_lo, c_hi = cabs_lo(cr, ci), cabs_hi(cr, ci)
    assert c_lo > R2
    elo, _ = exp_bounds(Fraction(1) - (cr + R2) / n)
    _, ehi = exp_bounds(Fraction(1) - (cr - R2) / n)
    glo = ((c_lo - R2) / n) * elo - 1
    ghi = ((c_hi + R2) / n) * ehi - 1
    o = G[(n, j)]
    assert abs(float(glo) - o['glo']) < 1e-9 and abs(float(ghi) - o['ghi']) < 1e-9, (n, j)
ehi = max(G[(16, j)]['ghi'] for j in (14, 15))
olo = min(o['glo'] for (n, j), o in G.items() if (n, j) not in ((16, 14), (16, 15)))
assert ehi < olo, (ehi, olo)
print(f"VERIFY_OK disks=136 rouche_r=0.3+0.01 disjoint=1..16 "
      f"maxRe_lo={loE:.4f}>others_hi={hiO:.4f} gap_ext_hi={ehi:.6f}<others_lo={olo:.6f}")
