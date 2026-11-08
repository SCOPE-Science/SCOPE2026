"""Exact integer-ring certificate for 65 nodal sections of the Barth sextic.

All computations take place in Z[t]/(t*t-t-1). The proof works in any
residue field of odd characteristic, including the ramified prime over 5.
No extension-field enumeration or symbolic algebra package is required.
"""
from itertools import product, combinations
from math import gcd

Z = (0, 0)
ONE = (1, 0)
T = (0, 1)
T2 = (1, 1)

def add(a, b): return (a[0]+b[0], a[1]+b[1])
def neg(a): return (-a[0], -a[1])
def sub(a, b): return add(a, neg(b))
def scale(a, n): return (a[0]*n, a[1]*n)
def mul(a, b):
    return (a[0]*b[0] + a[1]*b[1],
            a[0]*b[1] + a[1]*b[0] + a[1]*b[1])
def power(a, n):
    out = ONE
    while n:
        if n & 1: out = mul(out, a)
        a = mul(a, a)
        n //= 2
    return out

def norm(a): return a[0]**2+a[0]*a[1]-a[1]**2

def term(exps, coeff):
    return {} if coeff == Z else {tuple(exps):coeff}

def polyadd(A, B):
    C=A.copy()
    for e,c in B.items():
        d=add(C.get(e,Z), c)
        if d==Z: C.pop(e,None)
        else: C[e]=d
    return C

def polyn(a,n): return {e:scale(c,n) for e,c in a.items() if scale(c,n)!=Z}

def polyp(A,B):
    C={}
    for a,ca in A.items():
        for b,cb in B.items():
            e=tuple(a[i]+b[i] for i in range(4))
            C[e]=add(C.get(e,Z),mul(ca,cb))
    return {e:c for e,c in C.items() if c!=Z}

def cpoly(c): return term((0,0,0,0),c)

def diff(A,i):
    return {tuple(e[j]-(j==i) for j in range(4)):scale(c,e[i])
            for e,c in A.items() if e[i]}

def evaluate(A, point):
    out=Z
    for e,c in A.items():
        v=c
        for j in range(4):v=mul(v,power(point[j],e[j]))
        out=add(out,v)
    return out

def det3(a):
    return add(sub(mul(a[0][0],sub(mul(a[1][1],a[2][2]),mul(a[1][2],a[2][1]))),
                   mul(a[0][1],sub(mul(a[1][0],a[2][2]),mul(a[1][2],a[2][0])))),
               mul(a[0][2],sub(mul(a[1][0],a[2][1]),mul(a[1][1],a[2][0]))))

X = [term(tuple(1 if j==i else 0 for j in range(4)),ONE) for i in range(4)]
xs=[polyp(v,v) for v in X]
A=polyadd(polyp(cpoly(T2),xs[0]),polyn(xs[1],-1))
B=polyadd(polyp(cpoly(T2),xs[1]),polyn(xs[2],-1))
C=polyadd(polyp(cpoly(T2),xs[2]),polyn(xs[0],-1))
R=polyadd(polyadd(xs[0],xs[1]),polyadd(xs[2],polyn(xs[3],-1)))
# F = 4 ABC - (1+2t) R^2 w^2.
F=polyadd(polyn(polyp(polyp(A,B),C),4),
          polyn(polyp(cpoly((1,2)),polyp(polyp(R,R),xs[3])),-1))
first=[diff(F,i) for i in range(4)]
second=[[diff(first[i],j) for j in range(4)] for i in range(4)]

nodes=[]
for v in [(ONE,Z,Z),(Z,ONE,Z),(Z,Z,ONE)]:nodes.append(('infty_axis',v+(Z,)))
for family in range(3):
    for e,d in product((-1,1),repeat=2):
        v=(ONE,scale(T,e),scale(T2,e*d)); v=v[family:]+v[:family]
        nodes.append(('infty_cross',v+(Z,)))
for name,pt in nodes[:15]:
    for sg in (-1,1):
        w=scale(ONE if name=='infty_axis' else scale(T,2),sg)
        nodes.append(('sphere_axis' if name=='infty_axis' else 'sphere_cross',pt[:3]+(w,)))
for signs in product((-1,1),repeat=3):
    nodes.append(('outer_diagonal',tuple(scale(ONE,s) for s in signs)+(ONE,)))
for family in range(3):
    for e,d in product((-1,1),repeat=2):
        v=(Z,scale(sub(T,ONE),e),scale(T,d));v=v[family:]+v[:family]
        nodes.append(('outer_cycle',v+(ONE,)))
assert len(nodes)==65
assert len(F)>0

# All node coordinates are units when nonzero, apart from entries 2t on
# the spherical cross family; the other coordinates are units there.
for label,pt in nodes:
    assert evaluate(F,pt)==Z,(label,'not on surface',pt)
    assert all(evaluate(g,pt)==Z for g in first),(label,'not critical',pt)
    patch=next(i for i,c in enumerate(pt) if abs(norm(c))==1)
    other=[j for j in range(4) if j!=patch]
    mat=[[evaluate(second[i][j],pt) for j in other] for i in other]
    Hessian_norm=abs(norm(det3(mat)))
    assert Hessian_norm>0 and (Hessian_norm&(Hessian_norm-1))==0,(label,'bad Hessian',Hessian_norm)

# Pairwise projective distinctness: each possible common-residue zero of
# the six minors forces its characteristic to divide the gcd of their norms.
# Only powers of 2 occur in these gcds.
nonunit_pairs=0
for (_,a),(_,b) in combinations(nodes,2):
    minors=[sub(mul(a[i],b[j]),mul(a[j],b[i])) for i,j in combinations(range(4),2)]
    norms=[abs(norm(m)) for m in minors]
    g=gcd(*norms)
    assert g>0, 'identical projective points in characteristic zero'
    assert (g&(g-1))==0,('possible odd collision prime',a,b,g)
    if g>1:nonunit_pairs+=1

from collections import Counter
print('BARTH_ODD_NODE_CERTIFICATE_OK',
      'nodes='+str(len(nodes)),
      'types='+str(dict(Counter(tag for tag,_ in nodes))),
      'possible_bad_primes={2}',
      'pairs_with_nontrivial_norm_gcd='+str(nonunit_pairs))
