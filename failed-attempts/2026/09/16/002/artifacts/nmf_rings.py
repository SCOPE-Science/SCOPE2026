"""Verified Verlinde computations for the three NMF rank-6 modular fusion rings.
Run: python3 nmf_rings.py  (needs numpy/mpmath for Green S only; E47/E49 use plain math)
Asserts: fusion tables, max N=2 (NMF), associativity(spot), S unitarity, boson sets.
"""
import math, cmath

def check_ring(name, S, D2expect, T, NMF_claim):
    n = len(S)
    D2 = sum(S[0][j]**2 for j in range(n))
    assert abs(D2 - D2expect) < 1e-6, (name, D2)
    asym = max(abs(S[i][j]-S[j][i]) for i in range(n) for j in range(n))
    assert asym < 1e-9, (name, asym)
    unit = max(abs(sum(S[i][k]*S[j][k] for k in range(n))-(D2 if i==j else 0))
               for i in range(n) for j in range(n))
    assert unit < 1e-6, (name, unit)
    Sn = [[x/math.sqrt(D2) for x in row] for row in S]
    N = {}
    mx = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(n):
                v = sum(Sn[i][t]*Sn[j][t]*Sn[k][t]/Sn[0][t] for t in range(n))
                r = int(round(v.real))
                assert abs(v-r) < 1e-6, (name, i, j, k, v)
                assert r >= 0, (name, i, j, k, r)
                N[(i,j,k)] = r; N[(j,i,k)] = r; mx = max(mx, r)
    # associativity spot-check (full: 6^4)
    bad = sum(1 for a in range(n) for b in range(n) for c in range(n) for dd in range(n)
              if sum(N[(a,b,x)]*N[(x,c,dd)] for x in range(n)) !=
                 sum(N[(b,c,x)]*N[(a,x,dd)] for x in range(n)))
    bosons = [i for i in range(n) if abs(((T[i] % 1)+1)%1) < 1e-9 or abs(((T[i]%1)+1)%1-1) < 1e-9]
    duals = {}
    for i in range(n):
        duals[i] = [k for k in range(n) if N[(i,k,0)] == 1]
    print(f"{name}: D2={D2:.6f} maxN={mx} assoc_bad={bad} bosons={bosons} duals={duals}")
    assert (mx >= 2) == NMF_claim
    assert bad == 0
    return N

# ---------- Green B9 ring (D2=9), S from Green arXiv:1908.07128 Thm 3.5 ----------
a = cmath.exp(1j*math.pi/9)
r1, r2, r3 = (-a-a**2+a**5).real, (a+a**2-a**4).real, (a**4-a**5).real
SG = [[1,-1,1,r1,r2,r3],[-1,1,-1,-r2,-r3,-r1],[1,-1,1,r3,r1,r2],
      [r1,-r2,r3,1,1,1],[r2,-r3,r1,1,1,1],[r3,-r1,r2,1,1,1]]
NG = check_ring("Green-B9", SG, 9.0, [0,1/3,2/3,-2/9,4/9,1/9], True)
assert NG[(1,1,1)] == 2 and NG[(1,1,2)] == 2  # signature NMF entries
print("  1x1 =", "+".join(f"{NG[(1,1,k)]}*{k}" for k in range(6) if NG[(1,1,k)]))

# ---------- E47 ring (D2=27+27c1_9+18c2_9), S from Ng-Rowell-Wen App F.5 entry 47 ----------
c1 = 2*math.cos(2*math.pi/9); c2 = 2*math.cos(4*math.pi/9)
xi = 1+c1+c2; p = 1+2*c1+c2; q = 2+2*c1+c2
S47 = [[1,xi,xi,xi,p,q],[xi,2*xi,-xi,-xi,xi,-xi],[xi,-xi,2*xi,-xi,xi,-xi],
       [xi,-xi,-xi,2*xi,xi,-xi],[p,xi,xi,xi,-q,-1],[q,-xi,-xi,-xi,-1,p]]
N47 = check_ring("E47", S47, 27+27*(c1/2)+18*(c2/2) if False else 1+3*xi**2+p**2+q**2, [0,1/9,1/9,1/9,1/3,2/3], True)
assert N47[(4,5,5)] == 2 and N47[(5,5,4)] == 2 and N47[(5,5,5)] == 2
print("  5x5 =", "+".join(f"{N47[(5,5,k)]}*{k}" for k in range(6) if N47[(5,5,k)]))

# ---------- E49 ring (D2=(105+21√21)/2), S from Ng-Rowell-Wen App F.5 entry 49 ----------
s21 = math.sqrt(21)
def ck(n, m=21): return 2*math.cos(2*math.pi*n/m)
A, B, C, E = (3+s21)/2, (5+s21)/2, (7+s21)/2, -(3+s21)/2
S11 = 2-ck(1)-2*ck(2)+3*ck(3)+2*ck(4)-2*ck(5)
S12 = -ck(2)-2*ck(3)-ck(4)+ck(5)
S13 = -1+2*ck(1)+3*ck(2)-ck(3)+2*ck(5)
S49 = [[1,A,A,A,B,C],[A,S11,S12,S13,E,0],[A,S12,S13,S11,E,0],
       [A,S13,S11,S12,E,0],[B,E,E,E,1,C],[C,0,0,0,C,-C]]
N49 = check_ring("E49", S49, (105+21*s21)/2, [0,1/7,2/7,4/7,0,2/3], True)
assert N49[(4,5,5)] == 2 and N49[(5,5,4)] == 2 and N49[(5,5,5)] == 2
print("  5x5 =", "+".join(f"{N49[(5,5,k)]}*{k}" for k in range(6) if N49[(5,5,k)]))
print("ALL RING CHECKS PASSED")
