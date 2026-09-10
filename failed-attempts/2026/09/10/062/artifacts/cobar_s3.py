# Cobar s=3 kernel computation for Ext_{A(2)_*}(F2,F2) in stems 52-56.
# Gamma = F2[x,y,z]/(x^8,y^4,z^2), |x|=1,|y|=3,|z|=7. Coproduct:
# px = x@1+1@x; py = y@1 + x^2@x + 1@y; pz = z@1 + y^2@x + x^4@y + 1@z.
# Reduced coproduct gives cobar d. Compute H^{3,t} = ker(d: C^3_t -> C^4_t) since C^2_t=0.
import itertools
from collections import defaultdict

# monomial basis: (i,j,k), 0<=i<8,0<=j<4,0<=k<2
mons=[]; idx={}
for i in range(8):
    for j in range(4):
        for k in range(2):
            idx[(i,j,k)]=len(mons); mons.append((i,j,k))
N=len(mons)
def deg(m): return m[0]*1+m[1]*3+m[2]*7
def add(m1,m2):
    i=m1[0]+m2[0]; j=m1[1]+m2[1]; k=m1[2]+m2[2]
    if i>=8 or j>=4 or k>=2: return None
    return (i,j,k)
# full coproduct psi(m) as dict {(a,b):1} over F2 (use bilinearity from generators)
# psi(x^iy^jz^k) = psi(x)^i psi(y)^j psi(z)^k in (G x G) with truncated mult.
# Represent elements of GxG as dict {(a,b):coef}.
from functools import lru_cache
GxG_basis_N = N*N
def gmult(a,b):
    return add(a,b)
# generator coproducts as list of pairs
def psi_gen(g):
    if g==(1,0,0): return [((1,0,0),(0,0,0)),((0,0,0),(1,0,0))]
    if g==(0,1,0): return [((0,1,0),(0,0,0)),((2,0,0),(1,0,0)),((0,0,0),(0,1,0))]
    if g==(0,0,1): return [((0,0,1),(0,0,0)),((0,2,0),(1,0,0)),((4,0,0),(0,1,0)),((0,0,0),(0,0,1))]
    raise ValueError(g)
def mul_GxG(P,Q):
    R=defaultdict(int)
    for (a1,b1),c1 in P.items():
        for (a2,b2),c2 in Q.items():
            na=add(a1,a2); nb=add(b1,b2)
            if na is None or nb is None: continue
            R[(na,nb)]^= (c1&c2)
    return {k:v for k,v in R.items() if v}
def psi_mon(m):
    # product over i copies of psi(x), j of psi(y), k of psi(z)
    R={( (0,0,0),(0,0,0) ):1}
    for g,n in [((1,0,0),m[0]),((0,1,0),m[1]),((0,0,1),m[2])]:
        Pg={k:1 for k in psi_gen(g)} if n>0 else None
        # exponentiate: P^n under GxG mult
        Pn={( (0,0,0),(0,0,0) ):1}
        for _ in range(n):
            Pn=mul_GxG(Pn,Pg)
        R=mul_GxG(R,Pn)
    return R
# precompute reduced coproduct: bars = terms with both factors != 1
red={}
for m in mons:
    if m==(0,0,0): continue
    P=psi_mon(m)
    terms=[(a,b) for (a,b) in P if a!=(0,0,0) and b!=(0,0,0)]
    red[m]=terms
# sanity: coassociativity spot check + counit
print("red coproduct examples:")
for m in [(1,0,0),(0,1,0),(0,0,1),(2,0,0),(4,0,0),(0,2,0)]:
    print(m, "deg", deg(m), "->", red[m])
# Build C^3_t basis: triples (a,b,c) non-1 monomials with deg sum = t
def basis_C3(t):
    res=[]
    cottage=[m for m in mons if m!=(0,0,0)]
    for a in cottage:
        da=deg(a)
        for b in cottage:
            db=deg(b)
            for c in cottage:
                if da+db+deg(c)==t: res.append((a,b,c))
    return res
def basis_C4(t):
    # quadruples; count only (need column count for matrix width? actually rows)
    # Instead of enumerating all (~300k), enumerate lazily for matrix rows.
    cottage=[m for m in mons if m!=(0,0,0)]
    res=[]
    for a in cottage:
        for b in cottage:
            for c in cottage:
                for d in cottage:
                    if deg(a)+deg(b)+deg(c)+deg(d)==t: res.append((a,b,c,d))
    return res
for stem in [52,53,54,55,56]:
    for s,t in [(3,stem+3)]:
        print(f"stem {stem} C^3 dim:", len(basis_C3(t)))
