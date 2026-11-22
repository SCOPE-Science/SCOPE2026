"""Independent binary symplectic GQ(2,2) model; standard-library exact check.
Run: python3 verify_symplectic.py
"""
from collections import Counter,deque
from fractions import Fraction
from itertools import combinations

P=list(range(1,16))
def omega(a,b):
    # alternating form on F_2^4, with coordinates a0,a1,a2,a3
    return (((a>>0)&1)*((b>>2)&1) + ((a>>2)&1)*((b>>0)&1)
        + ((a>>1)&1)*((b>>3)&1) + ((a>>3)&1)*((b>>1)&1))%2
L=sorted({tuple(sorted((a,b,a^b))) for a,b in combinations(P,2) if omega(a,b)==0})
assert len(L)==15
A=[set() for _ in range(30)]
for j,l in enumerate(L):
    for p in l:
        i=P.index(p)
        A[i].add(j+15);A[j+15].add(i)
assert all(len(v)==3 for v in A)

def dist(source,removed=()):
    removed=set(removed)
    q=deque([source]);D={source:0}
    while q:
        u=q.popleft()
        for v in A[u]:
            if v not in D and v not in removed:
                D[v]=D[u]+1;q.append(v)
    return D
D=[dist(x) for x in range(30)]
assert max(max(t.values()) for t in D)==4

def porous(S):
    mask=set(S)
    for v in range(30):
        if v in mask:continue
        wt=sum(Fraction(2,2**D[v][p]) for p in S)
        if wt<1:return False
    return True

C=[0]*5;sol=[]
for k in range(5):
    for S in combinations(range(30),k):
        if porous(S):
            C[k]+=1
            if k==4:sol.append(frozenset(S))
assert C==[0,0,0,0,45],C
# Independent flag construction directly from incidence matrix.
F=set()
for p in range(15):
    for l in A[p]:
        F.add(frozenset((A[l]-{p})|(A[p]-{l})))
assert len(F)==45 and set(sol)==F

# Check the ORIGINAL, obstacle-aware definition on every candidate.
for S in sol:
    vals=[]
    for v in range(30):
        if v in S:continue
        val=Fraction(0)
        for source in S:
            d=dist(v,S-{source}).get(source)
            if d is not None:val+=Fraction(2,2**d)
        vals.append(val)
    assert Counter(vals)==Counter({Fraction(9,8):16,Fraction(21,16):8,Fraction(3):2})

# Construct the three-exchange graph independently from Hamming distances.
D3={i:set() for i in range(45)}
for i,j in combinations(range(45),2):
    common=len(sol[i]&sol[j])
    assert common<=1
    if common==1:D3[i].add(j);D3[j].add(i)
assert sum(len(z) for z in D3.values())==900
assert set(len(z) for z in D3.values())=={20}
for s in range(45):
    R={s};front={s}
    for _ in range(2):
        front=set().union(*(D3[u] for u in front))-R
        R.update(front)
    assert len(R)==45
print('PASS: independent symplectic GQ(2,2); C(30,k) for k=0..4 gives',C)
print('PASS: exact nonporous influence histogram, flags, and 3-exchange regularity/diameter')
