"""Exact finite certificate for the resolved icosahedral line boundary.
Python 3.9+ standard library; no external packages.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
from math import prod

# Elements a+b*w of Q(w), with w^2=w+1, represented by rational pairs.
def el(a=0,b=0): return (Q(a),Q(b))
ZERO=el(); ONE=el(1); W=el(0,1)
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    u,v=a; x,y=b
    return (u*x+v*y, u*y+v*x+v*y)
def inv(a):
    u,v=a
    norm=u*u+u*v-v*v
    assert norm != 0
    return ((u+v)/norm,-v/norm)
def scale(a,b): return mul(a,b)
def cross(x,y):
    return (sub(mul(x[1],y[2]),mul(x[2],y[1])),
            sub(mul(x[2],y[0]),mul(x[0],y[2])),
            sub(mul(x[0],y[1]),mul(x[1],y[0])))
def proj(v):
    f=next(x for x in v if x!=ZERO)
    return tuple(scale(a,inv(f)) for a in v)

# Six antipodal pairs of vertices of a standard real icosahedron.
poles=[(ZERO,ONE,W),(ZERO,ONE,neg(W)),(ONE,W,ZERO),
       (ONE,neg(W),ZERO),(W,ZERO,ONE),(neg(W),ZERO,ONE)]
line_labels=list(combinations(range(6),2))
lines={ij:proj(cross(poles[ij[0]],poles[ij[1]])) for ij in line_labels}
assert len(set(lines.values()))==15
# Cross-check against the conventional H3 root normals, up to Y/Z swap.
# They are the axes and all cyclic permutations of (1,w,w-1) with
# independent sign changes in the last two coordinates.
std={proj((ONE,ZERO,ZERO)),proj((ZERO,ONE,ZERO)),proj((ZERO,ZERO,ONE))}
root=(ONE,W,sub(W,ONE))
for shift in range(3):
    t=root[shift:]+root[:shift]
    for a in (-1,1):
        for b in (-1,1):
            std.add(proj((t[0],scale(el(a),t[1]),scale(el(b),t[2]))))
assert len(std)==15
assert set(lines.values())=={proj((v[0],v[2],v[1])) for v in std}
incidences={}
for e,f in combinations(line_labels,2):
    point=proj(cross(lines[e],lines[f]))
    incidences.setdefault(point,set()).update((e,f))
assert Counter(map(len,incidences.values()))=={2:15,3:10,5:6}
assert sum(len(g)*(len(g)-1)//2 for g in incidences.values()) == 105

# Blow up all points of multiplicity >=3, not the 15 ordinary nodes.
multiple=[frozenset(g) for g in incidences.values() if len(g)>2]
multiple.sort(key=lambda s:(-len(s),tuple(sorted(s))))
assert len(multiple)==16
n=31
edges=[]
for j,group in enumerate(multiple):
    edges.extend((line_labels.index(e),15+j) for e in group)
for group in incidences.values():
    if len(group)==2:
        a,b=sorted(group)
        edges.append((line_labels.index(a),line_labels.index(b)))
assert len(edges)==75
L=[[0]*n for _ in range(n)]
for a,b in edges:
    L[a][a]+=1;L[b][b]+=1;L[a][b]-=1;L[b][a]-=1
assert Counter(L[i][i] for i in range(n))=={6:15,3:10,5:6}
assert all(sum(row)==0 for row in L)
assert 75-31+1==45

def det_bareiss(M):
    A=[row[:] for row in M]; n=len(A);denom=1;sign=1
    for k in range(n-1):
        if not A[k][k]:
            t=next((t for t in range(k+1,n) if A[t][k]),None)
            if t is None: return 0
            A[t],A[k]=A[k],A[t];sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=A[i][j]*pivot-A[i][k]*A[k][j]
                assert num%denom==0
                A[i][j]=num//denom
            A[i][k]=0
        denom=pivot
    return sign*A[-1][-1]

def rank_mod(M,p):
    A=[[x%p for x in row] for row in M]
    rank=0;nr=len(A);nc=len(A[0])
    for c in range(nc):
        pivot=next((i for i in range(rank,nr) if A[i][c]),None)
        if pivot is None:continue
        A[rank],A[pivot]=A[pivot],A[rank]
        t=pow(A[rank][c],-1,p)
        for j in range(c,nc):A[rank][j]=A[rank][j]*t%p
        for i in range(rank+1,nr):
            t=A[i][c]
            if t:
                for j in range(c,nc):A[i][j]=(A[i][j]-t*A[rank][j])%p
        rank+=1
    return rank

def matrix_product(A,B):
    n=len(A)
    BT=list(zip(*B))
    return [[sum(a*b for a,b in zip(row,col)) for col in BT] for row in A]

def charpoly_coefficients(A):
    # Faddeev--LeVerrier over Z. Output descending coefficients.
    n=len(A)
    B=[[int(i==j) for j in range(n)] for i in range(n)]
    coeffs=[1]
    for k in range(1,n+1):
        B=matrix_product(A,B)
        t=sum(B[i][i] for i in range(n))
        assert t%k==0
        c=-(t//k)
        coeffs.append(c)
        for i in range(n):B[i][i]+=c
    assert all(not any(row) for row in B)
    return coeffs

def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

# Reconstruct the complete characteristic polynomial independently of the cofactor.
expect=[0,1]
for q,m in [([31,-12,1],6),([17,-10,1],5),([11,-7,1],4)]:
    for _ in range(m):expect=poly_mul(expect,q)
assert charpoly_coefficients(L)==list(reversed(expect))
# The coefficient of t is (-1)^30 times 31 times the spanning-tree count.
assert expect[1] == 31*(11**4)*(17**5)*(31**5)

A=[r[1:] for r in L[1:]]
spanning=595146407909049887
assert det_bareiss(A)==spanning
assert det_bareiss([r[:-1] for r in L[:-1]])==spanning
assert spanning == 11**4 * 17**5 * 31**5
for p,nullity in ((11,4),(17,5),(31,5)):
    assert 30-rank_mod(A,p)==nullity
# v_p(det) equals nullity, so all nonzero p-primary Smith valuations equal one.
# Hence K = (Z/11)^4 x (Z/17)^5 x (Z/31)^5
# and invariant factors are [527,5797,5797,5797,5797].
assert 527==17*31 and 5797==11*17*31
assert prod([527]+[5797]*4)==spanning
print('ICOSAHEDRAL_15_LINE_STABLE_BOUNDARY_INTEGRAL_GROUP_OK')
print('NODES/COMPONENTS/GENUS',75,31,45)
print('DET',spanning,'SMITH',[527]+[5797]*4)
