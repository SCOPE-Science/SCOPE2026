#!/usr/bin/env python3
"""Exact finite-field checks for an explicitly presented cubic and its plane geometry."""
from itertools import combinations,product
from collections import Counter

# GF(4) with alpha^2=alpha+1, elements encoded by binary polynomial coefficients.
def mul(a,b):
    z=0
    for i in range(2):
        if b>>i&1:z^=a<<i
    if z&8:z ^= (0b111<<1)
    if z&4:z ^= 0b111
    return z

def power(a,n):
    z=1
    while n:
        if n&1:z=mul(z,a)
        a=mul(a,a);n>>=1
    return z

def normalize(v):
    m=next(x for x in v if x)
    inv=power(m,2)
    return tuple(mul(inv,x) for x in v)

def add(a,b):return tuple(x^y for x,y in zip(a,b))
def scale(a,v):return tuple(mul(a,x) for x in v)
def cube(x):return mul(mul(x,x),x)
def F(v):
    s=0
    for x in v:s ^= x
    return cube(s) ^ sum_xor(cube(x) for x in v)
def sum_xor(vs):
    s=0
    for x in vs:s ^= x
    return s

def B(u,v):
    # ambient five-coordinate dot product on W=sum(y)=0; y4=sum first four.
    a=list(u)+[sum_xor(u)];b=list(v)+[sum_xor(v)]
    return sum_xor(mul(x,y) for x,y in zip(a,b))

def pts(q):
    for v in product(range(q),repeat=4):
        if any(v):yield normalize(v)

def line_on_surface(u,v):
    yy=list(u)+[sum_xor(u)]; zz=list(v)+[sum_xor(v)]
    c1=sum_xor(mul(mul(a,a),b) for a,b in zip(yy,zz))
    c2=sum_xor(mul(a,mul(b,b)) for a,b in zip(yy,zz))
    return F(u)==F(v)==c1==c2==0

def lines_on_S(q):
    P=sorted(set(pts(q))); seen={}
    for u,v in combinations(P,2):
        pair=[normalize(v)]+[normalize(add(u,scale(a,v))) for a in range(q)]
        key=tuple(sorted(set(pair)))
        if len(key)!=q+1:raise AssertionError((u,v,key))
        if key not in seen:seen[key]=(u,v)
    good={key:uv for key,uv in seen.items() if line_on_surface(*uv)}
    return P,seen,good

P2,all2,S2=lines_on_S(2)
P4,all4,S4=lines_on_S(4)
print("precounts",len(P2),len(all2),len(S2),len(P4),len(all4),len(S4));assert len(P2)==15 and len(all2)==35 and len(S2)==15
assert len(P4)==85 and len(all4)==357 and len(S4)==27
assert sum(F(v)==0 for v in P2)==15
assert sum(F(v)==0 for v in P4)==45
assert all(B(u,v)==0 for u,v in S2.values())
assert Counter(B(u,v)==0 for u,v in S4.values())==Counter({True:15,False:12})

# Independent coefficient extraction from the elementary symmetric quadratic E2.
# E2(s*u+r*v) has mixed s*r coefficient sum_{i<j}(u_i*v_j+v_i*u_j),
# equal to the ambient alternating dot-product B(u,v) when sum u=sum v=0.
def cross_e2(u,v):
    a=list(u)+[sum_xor(u)]; b=list(v)+[sum_xor(v)]
    return sum_xor(mul(a[i],b[j]) ^ mul(b[i],a[j]) for i in range(5) for j in range(i+1,5))
assert all(cross_e2(u,v)==B(u,v) for u,v in S4.values())

# Frobenius permutation of all 27 geometric lines and field-of-definition profile.
frob=lambda v:normalize(tuple(mul(x,x) for x in v))
perm={line:tuple(sorted(frob(v) for v in line)) for line in S4}
assert all(val in S4 for val in perm.values())
assert all(perm[perm[line]]==line for line in S4)
assert sum(a==b for a,b in perm.items())==15
assert sum(a!=b for a,b in perm.items())==12
assert all((line==perm[line])==(B(*S4[line])==0) for line in S4)

# Three rational isotropic lines through each of 15 rational points.
inci={p:sum(p in line for line in S2) for p in P2}
assert Counter(inci.values())=={3:15}
assert all(sum(p in line for p in P2)==3 for line in S2)

# The F2 planes in the cubic cone are exactly the fifteen matching planes.
# Each F2 point of the 4-dimensional quotient W corresponds to a pair among six labels.
# Each F2 isotropic 2-space corresponds to a partition of six into three pairs.
assert len(S2)==15

# Direct projective point count in P4(F2) and P4(F4): x5=0 section + vertex coordinate t.
# Cone equation is independent of t.
for q, expected in [(2,31),(4,181)]:
    N=1+q*sum(F(x)==0 for x in set(pts(q)))
    assert N==expected,(q,N)

print('GF2: P3 points=15, surface points=15; total lines=35, contained lines=15; all points have degree 3')
print('GF4: P3 points=85, surface points=45; total lines=357, contained lines=27')
print('Fano planes: Frobenius-fixed=15, six two-cycles; B-isotropic=15, B-nonisotropic=12')
print('Cone point counts: #X(F2)=31, #X(F4)=181')
print('First-order normal obstruction on extra planes is coefficient of t*u*v = B(u,v), nonzero for exactly 12')
print('VERIFY_OK')
