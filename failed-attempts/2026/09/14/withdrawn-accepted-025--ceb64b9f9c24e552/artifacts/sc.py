# Exact structure constant via Murnaghan-Nakayama for S12 at classes (4,2,1^6),(5,4,3),(7,3,2).
import math, itertools, time
from functools import lru_cache

def partitions(n, maxp=None):
    if maxp is None: maxp=n
    if n==0: yield ();
    else:
        for f in range(min(maxp,n),0,-1):
            for rest in partitions(n-f,f):
                yield (f,)+rest
PARTS=list(partitions(12))

def rim_hook_removals(lam, k):
    lam=list(lam)
    cells={(r,c) for r in range(len(lam)) for c in range(lam[r])}
    if k>len(cells): return []
    # NOTE: hooks may contain interior cells (e.g. hook of (0,0)); search ALL subsets.
    seen=set(); results=[]
    for H in itertools.combinations(sorted(cells),k):
        H=set(H)
        q=[next(iter(H))]; vis={next(iter(H))}
        while q:
            (r,c)=q.pop()
            for (rr,cc) in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
                if (rr,cc) in H and (rr,cc) not in vis:
                    vis.add((rr,cc)); q.append((rr,cc))
        if len(vis)!=k: continue
        bad=False
        for (r,c) in H:
            if (r+1,c) in H and (r,c+1) in H and (r+1,c+1) in H: bad=True; break
        if bad: continue
        rest=cells-H
        if not rest:
            mu=()
        else:
            maxr=max(r for r,c in rest)
            rows=[]; ok=True
            for r in range(maxr+1):
                row=sorted(c for (rr,c) in rest if rr==r)
                if row!=list(range(len(row))): ok=False; break
                rows.append(len(row))
            if not ok: continue
            if any(rows[i]<rows[i+1] for i in range(len(rows)-1)): continue
            while rows and rows[-1]==0: rows.pop()
            mu=tuple(rows)
        leg=len({r for r,c in H})-1
        if (mu,leg) in seen: continue
        seen.add((mu,leg)); results.append((mu,leg))
    return results

MN={}
def mn_get(lam,k):
    key=(tuple(lam),k)
    if key not in MN:
        MN[key]=rim_hook_removals(list(lam),k)
    return MN[key]

def make_chi(lam):
    @lru_cache(maxsize=None)
    def chi(lam2, alpha):
        if not alpha: return 1 if not lam2 else 0
        if not lam2: return 0
        k=alpha[-1]; rest=alpha[:-1]
        tot=0
        for (nu,leg) in mn_get(lam2,k):
            tot += ((-1)**leg)*chi(nu,rest)
        return tot
    return lambda alpha: chi(tuple(lam),tuple(alpha))

A0=(4,2,1,1,1,1,1,1); A1=(5,4,3); A2=(7,3,2)
t0=time.time()
S=0; terms=[]
totsq=0
for lam in PARTS:
    chi=make_chi(lam)
    deg=chi((1,)*12)
    a=chi(A0); b=chi(A1); c=chi(A2)
    totsq+=0
    if a and b and c:
        terms.append((lam,deg,a,b,c))
print("nonzero-at-all-three:",len(terms),"time:",round(time.time()-t0,1))
# structure constant N = |C0||C1|/|G| * sum chi(a)chi(b)chi(c)/chi(1); c^{-1} in same class (all cycle lengths: check inverse class: 7->7,3->3,2->2 yes)
import math
n=12; nf=math.factorial(n)
from collections import Counter
def centsz(ct):
    c=Counter(ct); z=1
    for m,k in c.items(): z*=(m**k)*math.factorial(k)
    return z
C0sz=nf//centsz(A0); C1sz=nf//centsz(A1)
from fractions import Fraction
tot=Fraction(0,1)
for (lam,deg,a,b,c) in terms:
    tot+=Fraction(a*b*c,deg)
N=Fraction(C0sz*C1sz,nf)*tot
print("sum =",tot," N =",N, "=",float(N))
# also conjugacy: number of triples with x*y*z=1 equals |G|^{-1}|C0||C1||C2| * sum... ; our N fixes z so divide by |C2|? verify: standard formula N(z fixed) = |C0||C1|/|G| sum ...
# print terms table
for (lam,deg,a,b,c) in sorted(terms,key=lambda t:-abs(t[2]*t[3]*t[4]/t[1])):
    print(lam,"deg",deg,"a",a,"b",b,"c",c,"term",Fraction(a*b*c,deg))
