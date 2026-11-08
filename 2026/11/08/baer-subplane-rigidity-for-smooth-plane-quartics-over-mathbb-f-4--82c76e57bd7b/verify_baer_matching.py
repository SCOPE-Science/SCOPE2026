#!/usr/bin/env python3
"""Exact Fano-incidence certificate for quartics over GF(4).
Requires Python 3.9+ and SymPy for the geometric-smoothness ideal check.
Run: python3 verify_baer_matching.py
"""
import itertools
from sympy import symbols, groebner, diff, expand

B = sorted(p for p in itertools.product((0,1), repeat=3) if any(p))
LINES = B[:]
MONS = [(i,j,4-i-j) for i in range(5) for j in range(5-i)]
assert len(B)==7 and len(MONS)==15

def dot(p,q):return sum(a*b for a,b in zip(p,q))%2

def derivative_q_at_p(m,q,p):
    s=0
    for t in range(3):
        if m[t]%2 and q[t]:
            s ^= int(all((p[u] or m[u]-(u==t)==0) for u in range(3)))
    return s

def eliminate_mod2(rows, n=15):
    R=list(rows); piv=[]; r=0
    for c in range(n):
        k=next((i for i in range(r,len(R)) if (R[i]>>c)&1), None)
        if k is None:continue
        R[r],R[k]=R[k],R[r]
        for i in range(len(R)):
            if i!=r and ((R[i]>>c)&1):R[i]^=R[r]
        piv.append(c);r+=1
    free=[c for c in range(n) if c not in piv]
    v=0
    if len(free)==1:
        v=1<<free[0]
        for k,p in enumerate(piv):
            if (R[k]>>free[0])&1:v|=1<<p
    return r,v

def monval(m,p):
    return int(all((not e) or p[i] for i,e in enumerate(m)))

matchings=[]
for perm in itertools.permutations(range(7)):
    if all(dot(B[i],LINES[perm[i]])==0 for i in range(7)):
        matchings.append(perm)
assert len(matchings)==24

solutions=[]
for matching in matchings:
    rows=[]
    for i,p in enumerate(B):
        rows.append(sum(monval(m,p)<<j for j,m in enumerate(MONS)))
        l=LINES[matching[i]]
        q=next(t for t in B if t!=p and dot(t,l)==0)
        rows.append(sum(derivative_q_at_p(m,q,p)<<j for j,m in enumerate(MONS)))
    rank,vec=eliminate_mod2(rows)
    assert rank==14 and vec!=0
    assert all((row&vec).bit_count()%2==0 for row in rows)
    solutions.append(vec)
assert len(set(solutions))==24

# Exact projective symmetry action on matchings.
def det2(a):
    acc=0
    for perm in itertools.permutations(range(3)):
        bit=1
        for i,j in enumerate(perm):bit &= a[3*i+j]
        acc ^= bit
    return acc
G=[a for a in itertools.product((0,1),repeat=9) if det2(a)]
assert len(G)==168
line_sets={frozenset(p for p in B if dot(p,l)==0):i for i,l in enumerate(LINES)}
images=set()
for a in G:
    pmap=[]
    for p in B:
        out=tuple((a[3*i]*p[0])^(a[3*i+1]*p[1])^(a[3*i+2]*p[2]) for i in range(3))
        pmap.append(B.index(out))
    lmap=[]
    for l in LINES:
        support=frozenset(B[pmap[i]] for i,p in enumerate(B) if dot(p,l)==0)
        lmap.append(line_sets[support])
    match=[-1]*7
    for i,lidx in enumerate(matchings[0]):match[pmap[i]]=lmap[lidx]
    images.add(tuple(match))
assert images==set(matchings) and len(images)==24
assert len(G)//len(images)==7

# The chosen quartic is smooth over algebraic closure: affine Jacobian ideals
# contain 1 over GF(2), on each projective chart.
vec=solutions[0]
X,Y,Z=symbols('X Y Z'); xyz=(X,Y,Z)
F=expand(sum(xyz[0]**i*xyz[1]**j*xyz[2]**k for n,(i,j,k) in enumerate(MONS) if (vec>>n)&1))
for chart in xyz:
    u,v=[q for q in xyz if q!=chart]
    f=F.subs(chart,1)
    basis=groebner([f,diff(f,u),diff(f,v)],u,v,order='grevlex',modulus=2)
    assert len(basis.polys)==1 and basis.polys[0].as_expr()==1, (chart,basis)

# Its complete GF(4) rational point locus is precisely the Fano subplane.
MUL=((0,0,0,0),(0,1,2,3),(0,2,3,1),(0,3,1,2))
INV=(0,1,3,2)
def product(a,b):return MUL[a][b]
def pow4(a,n):
    v=1
    for _ in range(n):v=product(v,a)
    return v
points=set()
for p in itertools.product(range(4),repeat=3):
    if not any(p):continue
    inv=INV[next(t for t in p if t)]
    points.add(tuple(product(inv,t) for t in p))
assert len(points)==21
roots=[]
for p in points:
    val=0
    for n,m in enumerate(MONS):
        if (vec>>n)&1:
            w=1
            for a,e in zip(p,m):w=product(w,pow4(a,e))
            val^=w
    if val==0:roots.append(p)
assert set(roots)==set(B), (set(roots)-set(B))

print('BAER_MATCHING_PASS',len(B),len(matchings),len(set(solutions)),len(G),len(images),len(roots))
print('REPRESENTATIVE',str(F))
print('GLOBAL_CURVES',360*len(solutions),'STABILIZER',len(G)//len(images))
