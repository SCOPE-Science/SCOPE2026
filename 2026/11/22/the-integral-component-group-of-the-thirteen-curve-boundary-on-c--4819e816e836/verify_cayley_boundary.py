#!/usr/bin/env python3
"""Exact integer verification of a thirteen-component Cayley-cubic boundary.

No external packages are required. The proof of the general identities is in RESULT.md;
this script independently reconstructs the plane configuration, intersections,
Laplacian, characteristic polynomial, determinant, and local Smith ranks.
"""
from itertools import combinations
from math import prod

PAIRS = list(combinations(range(4), 2))
MATCHINGS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]

def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

def normalize(a):
    from math import gcd
    d = gcd(gcd(abs(a[0]), abs(a[1])), abs(a[2]))
    assert d
    t = tuple(v//d for v in a)
    return tuple(-v for v in t) if next(v for v in t if v) < 0 else t

def dot(a, b):
    return sum(x*y for x,y in zip(a,b))

def det_bareiss(A):
    a = [list(map(int, row)) for row in A]
    n = len(a)
    sign, prev = 1, 1
    for k in range(n-1):
        if a[k][k] == 0:
            j = next((j for j in range(k+1,n) if a[j][k]), None)
            if j is None: return 0
            a[k], a[j] = a[j], a[k]
            sign *= -1
        d = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                q = a[i][j]*d-a[i][k]*a[k][j]
                assert q%prev == 0
                a[i][j] = q//prev
            a[i][k] = 0
        prev = d
    return sign*a[-1][-1]

def rank_mod(A,p):
    B = [[x%p for x in row] for row in A]
    nr, nc = len(B),len(B[0]); r=0; pivots=[]
    for j in range(nc):
        k = next((i for i in range(r,nr) if B[i][j]),None)
        if k is None: continue
        B[r],B[k]=B[k],B[r]
        inv=pow(B[r][j],-1,p)
        B[r] = [(inv*x)%p for x in B[r]]
        for i in range(nr):
            if i !=r and B[i][j]:
                t=B[i][j]; B[i]=[(u-t*v)%p for u,v in zip(B[i],B[r])]
        pivots.append(j)
        r+=1
        if r==nr:break
    return r,pivots

def product_poly(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def charpoly(M):
    n=len(M)
    P=[[int(i==j) for j in range(n)] for i in range(n)]
    power=[]
    for _ in range(n):
        P = [[sum(P[i][k]*M[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        power.append(sum(P[i][i] for i in range(n)))
    c=[1]
    for k in range(1,n+1):
        v=-sum(c[k-i]*power[i-1] for i in range(1,k+1))
        assert v%k==0
        c.append(v//k)
    return c

# Four general lines and six nodes of the complete quadrangle.
planes=[(1,0,0),(0,1,0),(0,0,1),(1,1,1)]
points={ij:normalize(cross(planes[ij[0]], planes[ij[1]])) for ij in PAIRS}
assert len(set(points.values())) == 6
assert all(sum(dot(planes[i],points[jk])==0 for i in range(4)) == 2 for jk in PAIRS)
collinear_triples=[p for p in combinations(PAIRS,3) if dot(cross(points[p[0]],points[p[1]]),points[p[2]]) == 0]
assert len(collinear_triples)==4  # only the original four lines

# Three diagonal lines; their pairwise points are distinct and not base points.
diagonals=[]
for matching in MATCHINGS:
    p,q=matching
    diagonals.append(normalize(cross(points[p],points[q])))
triangle=[normalize(cross(diagonals[i],diagonals[j])) for i,j in combinations(range(3),2)]
assert len(set(triangle))==3
assert set(triangle).isdisjoint(points.values())
assert all(dot(diagonals[i],triangle[j]) == 0 for j,(i,k) in enumerate(combinations(range(3),2)))

# Divisor classes in Picard(X) with intersection diag(1,-1,...,-1).
cls={}
for i in range(4):
    cls[('R',i)]=(1,)+tuple(-int(i in ij) for ij in PAIRS)
for ij in PAIRS:
    cls[('E',)+ij]=(0,)+tuple(int(ij==e) for e in PAIRS)
for j,matching in enumerate(MATCHINGS):
    cls[('T',j)]=(1,)+tuple(-int(e in matching) for e in PAIRS)
V=list(cls)
def intersection(a,b):
    u,w=cls[a],cls[b]
    return u[0]*w[0]-sum(x*y for x,y in zip(u[1:],w[1:]))
assert len(V)==13
assert [intersection(v,v) for v in V] == [-2]*4+[-1]*9
edges=[]
for a,b in combinations(V,2):
    t=intersection(a,b)
    assert t in (0,1)
    if t:edges.append((a,b))
assert len(edges)==21
assert all(sum(int(v in e) for e in edges)>=3 for v in V)
assert len(edges)-len(V)+1 == 9

# Independent combinatorial edge specification from the K4 matchings.
expected=set()
for ij in PAIRS:
    for i in ij:
        expected.add(frozenset([('R',i),('E',)+ij]))
for k,matching in enumerate(MATCHINGS):
    for ij in matching:
        expected.add(frozenset([('T',k),('E',)+ij]))
for i,j in combinations(range(3),2):
    expected.add(frozenset([('T',i),('T',j)]))
assert expected == {frozenset(e) for e in edges}

L=[[0]*13 for _ in range(13)]
index={v:i for i,v in enumerate(V)}
for a,b in edges:
    i,j=index[a],index[b]
    L[i][i]+=1;L[j][j]+=1;L[i][j]-=1;L[j][i]-=1
assert sorted(L[i][i] for i in range(13))==[3]*10+[4]*3
assert all(sum(row)==0 for row in L)

# The characteristic polynomial is t(t^2-8t+13)^3(t^2-6t+7)^3.
coef=[1]
for factor in ((1,-8,13),)*3+((1,-6,7),)*3:
    coef=product_poly(coef,factor)
coef=product_poly(coef,(1,0))
assert charpoly(L)==coef

# Rooted critical group: integral order and finite-field ranks.
M=[row[:-1] for row in L[:-1]]
det=det_bareiss(M)
assert det==7**3*13**2==57967
assert det==13**2*7**3
ranks={p:rank_mod(M,p) for p in (7,13)}
assert ranks[7][0]==9 and ranks[13][0]==10
for removed in (0,4,12):
    minor=[[L[i][j] for j in range(13) if j!=removed] for i in range(13) if i!=removed]
    assert det_bareiss(minor)==57967
    assert rank_mod(minor,7)[0]==9
    assert rank_mod(minor,13)[0]==10
# Rank deficiencies 3 and 2 equal the respective valuations of the order.
# Therefore all p-primary cyclic factors have exponent p.
assert prod([7,91,91])==det
print('CAYLEY_13_CURVE_BOUNDARY_INTEGRAL_COMPONENT_GROUP_OK')
print('components=13 nodes=21 genus=9')
print('charpoly=t*(t^2-8t+13)^3*(t^2-6t+7)^3')
print('tree_count=57967')
print('reduced_mod7_rank=9 reduced_mod13_rank=10')
print('critical_group=Z/7 + Z/91 + Z/91')
