"""Independent verifier for lane-116 claimed witness (stdlib only).

Witness: n=6 weighted game w=[6,5,4,3,2,1], absolute quota Q=12 (q=12/21=4/7),
weighted instant-runoff (majority quota: >1/2 first round, else eliminate unique-lowest, pairwise runoff).
Profile P, no-show event (voter 4 abstains), upward-monotonicity event (voter 4 raises B).
Exact Banzhaf/Shapley (Fractions) before/after; Penrose sqrt-share gap via certified isqrt intervals.

Run: python3 verify_witness.py  -> prints PASS lines and ALL-OK.
"""
from fractions import Fraction
from math import factorial, isqrt

W = [6, 5, 4, 3, 2, 1]
Q = 12
CANDS = ('A', 'B', 'C')
P = [('A', 'B', 'C'), ('B', 'A', 'C'), ('C', 'A', 'B'),
     ('B', 'A', 'C'), ('C', 'A', 'B'), ('C', 'A', 'B')]
ABSTAINER = 4          # weight 2, ranking ('C','A','B')
UP_BALLOT = ('B', 'C', 'A')

def irv(w, ballots):
    total = sum(w)
    fp = {c: 0 for c in CANDS}
    for i in range(len(w)):
        fp[ballots[i][0]] += w[i]
    for c in CANDS:
        if fp[c] * 2 > total:
            return c, dict(fp), None
    m = min(fp.values())
    elim = [c for c in CANDS if fp[c] == m][0]
    rem = [c for c in CANDS if c != elim]
    t2 = {c: 0 for c in rem}
    for i in range(len(w)):
        for c in ballots[i]:
            if c in t2:
                t2[c] += w[i]
                break
    win = rem[0] if t2[rem[0]] > t2[rem[1]] else rem[1]
    return win, dict(fp), (elim, dict(t2))

def swings(w, quota):
    n = len(w)
    sw = [0] * n
    for mask in range(1 << n):
        s = sum(w[i] for i in range(n) if (mask >> i) & 1)
        for i in range(n):
            if not ((mask >> i) & 1) and s < quota <= s + w[i]:
                sw[i] += 1
    return sw

def shapley(w, quota):
    n = len(w)
    out = []
    for i in range(n):
        t = Fraction(0)
        others = [j for j in range(n) if j != i]
        for mask in range(1 << (n - 1)):
            S = [others[k] for k in range(n - 1) if (mask >> k) & 1]
            s = sum(w[j] for j in S)
            if s < quota <= s + w[i]:
                t += Fraction(factorial(len(S)) * factorial(n - len(S) - 1), factorial(n))
        out.append(t)
    return out

def sqrt_interval(m):
    N = m * 100**16
    r = isqrt(N)
    return (Fraction(r, 10**8), Fraction(r + 1, 10**8))

ok = True
def check(name, cond, info=""):
    global ok
    print(("PASS " if cond else "FAIL ") + name, info)
    if not cond:
        ok = False

# (0) quota window
check("quota in Penrose window [1/2,0.65]", Fraction(Q, sum(W)) >= Fraction(1, 2) and Fraction(Q, sum(W)) <= Fraction(65, 100),
      "q=%s" % Fraction(Q, sum(W)))
# (1) exact power indices, full game
sw = swings(W, Q)
check("Banzhaf swing counts", sw == [17, 13, 11, 7, 5, 3], str(sw))
beta = [Fraction(x, sum(sw)) for x in sw]
check("normalized Banzhaf", beta == [Fraction(17, 56), Fraction(13, 56), Fraction(11, 56), Fraction(1, 8), Fraction(5, 56), Fraction(3, 56)], str(beta))
phi = shapley(W, Q)
check("Shapley-Shubik", phi == [Fraction(19, 60), Fraction(7, 30), Fraction(1, 5), Fraction(7, 60), Fraction(1, 12), Fraction(1, 20)], str(phi))
check("Shapley sums to 1", sum(phi) == 1)
# (2) certified Penrose gap >= 1/25 for BOTH indices at voter 0
SIs = [sqrt_interval(x) for x in W]
Slo = sum(a for a, b in SIs); Shi = sum(b for a, b in SIs)
lo, hi = sqrt_interval(W[0])
plo, phi_ = lo / Shi, hi / Slo
gb = min(abs(beta[0] - plo), abs(beta[0] - phi_))
gs = min(abs(phi[0] - plo), abs(phi[0] - phi_))
check("voter0 Banzhaf gap >= 1/25", gb >= Fraction(1, 25), "gap=%.4f penrose=[%.6f,%.6f]" % (float(gb), float(plo), float(phi_)))
check("voter0 Shapley gap >= 1/25", gs >= Fraction(1, 25), "gap=%.4f" % float(gs))
# (3) IRV full outcome, tie-break-free
full, fpA, rA = irv(W, P)
check("full winner is B", full == 'B', str((full, fpA, rA)))
check("full rounds tie-break-free (distinct FP, strict R2)", rA is not None and len(set(fpA.values())) == 3 and list(rA[1].values())[0] != list(rA[1].values())[1], str((fpA, rA)))
# (4) no-show: voter 4 abstains -> A, strictly preferred (C>A>B ranking: A(2nd) beats B(3rd))
W2 = W[:ABSTAINER] + W[ABSTAINER + 1:]
P2 = P[:ABSTAINER] + P[ABSTAINER + 1:]
alt, fb, rb = irv(W2, P2)
check("post-abstention winner is A", alt == 'A', str((alt, fb, rb)))
check("abstention strictly beneficial", P[ABSTAINER].index(alt) < P[ABSTAINER].index(full), "%s %s->%s" % (P[ABSTAINER], full, alt))
check("post rounds tie-break-free", rb is not None and len(set(fb.values())) == 3 and list(rb[1].values())[0] != list(rb[1].values())[1], str((fb, rb)))
# (5) upward monotonicity: voter 4 moves B above C (C,A,B -> B,C,A), B still above... winner B -> A
Q2 = list(P); Q2[ABSTAINER] = UP_BALLOT
a3, f3, r3 = irv(W, Q2)
check("raised-ballot winner is A (monotonicity fails)", a3 == 'A', str((a3, f3, r3)))
check("ballot raised winner B, order otherwise kept", UP_BALLOT.index('B') < P[ABSTAINER].index('B') and UP_BALLOT.index('C') < UP_BALLOT.index('A'), str(UP_BALLOT))
check("raised rounds tie-break-free", r3 is not None and len(set(f3.values())) == 3 and list(r3[1].values())[0] != list(r3[1].values())[1], str((f3, r3)))
# (6) exact post-abstention indices (same absolute quota Q=12)
sw5 = swings(W2, Q)
check("post swing counts", sw5 == [7, 7, 5, 5, 1], str(sw5))
b5 = [Fraction(x, sum(sw5)) for x in sw5]
check("post Banzhaf", b5 == [Fraction(7, 25), Fraction(7, 25), Fraction(1, 5), Fraction(1, 5), Fraction(1, 25)], str(b5))
p5 = shapley(W2, Q)
check("post Shapley", p5 == [Fraction(17, 60), Fraction(17, 60), Fraction(1, 5), Fraction(1, 5), Fraction(1, 30)], str(p5))
print("ALL-OK" if ok else "SOME-FAILED")
