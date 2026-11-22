#!/usr/bin/env python3
"""Exact arithmetic certificate for the upper brightness law of an edge-2 icosahedron.

No external packages. A pair (a,b) represents a+b*phi with phi=(1+sqrt(5))/2.
Finite face and sign-spectrum searches are exhaustive; a Fibonacci-sphere check is
separately labelled numerical and is not used in the proof.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
from math import sqrt, pi, cos, sin

Z = (0, 0)
O = (1, 0)
P = (0, 1)

def add(x,y): return (x[0]+y[0], x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+x[1]*y[1],x[0]*y[1]+x[1]*y[0]+x[1]*y[1])
def times(n,x): return (n*x[0],n*x[1])
def sgn(x):
    """Exact sign, since 2(a+b*phi)=(2a+b)+b*sqrt(5)."""
    m,n=2*x[0]+x[1],x[1]
    if m==0: return (n>0)-(n<0)
    if n==0: return (m>0)-(m<0)
    if (m>0)==(n>0): return (m>0)-(m<0)
    dif=m*m-5*n*n
    assert dif!=0
    return ((m>0)-(m<0))*((dif>0)-(dif<0))
def absq(x): return x if sgn(x)>=0 else neg(x)
def vadd(x,y): return tuple(add(a,b) for a,b in zip(x,y))
def vneg(x): return tuple(neg(a) for a in x)
def vsub(x,y): return vadd(x,vneg(y))
def vcross(x,y): return (sub(mul(x[1],y[2]),mul(x[2],y[1])),
                     sub(mul(x[2],y[0]),mul(x[0],y[2])),
                     sub(mul(x[0],y[1]),mul(x[1],y[0])))
def vdot(x,y):
    r=Z
    for a,b in zip(x,y):r=add(r,mul(a,b))
    return r
def canon(x): return max(x,vneg(x))
def num(x):return x[0]+(1+sqrt(5))/2*x[1]

V=[]
for s,t in product((-1,1),repeat=2):
    V.extend([ (Z,(s,0),(0,t)), ((s,0),(0,t),Z), ((0,t),Z,(s,0)) ])
assert len(V)==12 and len(set(V))==12
faces=[]
for i,j,k in combinations(range(12),3):
    normal=vcross(vsub(V[j],V[i]),vsub(V[k],V[i]))
    assert normal!=(Z,Z,Z)
    tests=[sgn(vdot(normal,vsub(V[m],V[i]))) for m in range(12) if m not in (i,j,k)]
    if all(s>=0 for s in tests) or all(s<=0 for s in tests):
        assert all(s!=0 for s in tests)
        faces.append((i,j,k))
assert len(faces)==20
centroids=[vadd(vadd(V[i],V[j]),V[k]) for i,j,k in faces]
C=sorted({canon(c) for c in centroids})
assert len(C)==10 and set(centroids)=={v for c in C for v in (c,vneg(c))}
Nc=vdot(C[0],C[0]); assert Nc==(6,9)
assert all(vdot(c,c)==Nc for c in C)

# Exhaustively classify the 2^10 zonotope sign sums.
hist=Counter(); level_vectors=defaultdict(list)
for signs in product((-1,1), repeat=10):
    v=(Z,Z,Z)
    for c,s in zip(C,signs):v=vadd(v,c if s>0 else vneg(c))
    q=vdot(v,v)
    hist[q]+=1
    level_vectors[q].append(v)
expect={
(156,252):20,(140,224):60,(140,220):12,(108,172):60,
(92,144):60,(92,140):60,(76,112):60,(60,96):60,
(60,92):120,(60,80):12,(44,64):120,(44,60):60,
(28,44):60,(28,32):60,(28,28):60,(12,16):60,
(12,12):60,(12,0):20}
assert hist==expect and sum(hist.values())==1024
TOP=(156,252); SECOND=(140,224)
assert all(sgn(sub(TOP,q))>0 for q in hist if q!=TOP)
assert all(sgn(sub(SECOND,q))>0 for q in hist if q not in (TOP,SECOND))
maxima=set(level_vectors[TOP]); assert len(maxima)==20
normals={c for c in centroids}
assert all(any(vcross(v,c)==(Z,Z,Z) and sgn(vdot(v,c))>0 for c in normals) for v in maxima)

# Exact squared physical brightness and lower endpoint of certified upper band.
B2=(24,36)               # 42+18*sqrt(5)
T2=(28,28)               # 42+14*sqrt(5)
assert mul(B2,Nc)==times(3,TOP)
assert mul(T2,Nc)==times(3,SECOND)
assert sgn(sub(times(3,T2),mul(B2,(1,1))))>0 # disjoint caps
assert sgn(sub(times(9,T2),times(8,B2)))>0  # all caps in face-sign chambers

# Min angle between the 20 face-normal maxima and face-fan boundary.
for x in normals:
    off=[vdot(x,y) for y in normals if y!=x]
    assert all(sgn(sub(times(3,v),mul(Nc,(-1,2))))<=0 for v in off)
    # cos(min separation)=sqrt(5)/3=(2*phi-1)/3
    assert any(times(3,v)==mul(Nc,(-1,2)) for v in off)
    assert all(sgn(sub(times(3,absq(vdot(x,y))),Nc))>=0 for y in normals)
    assert any(times(3,absq(vdot(x,y)))==Nc for y in normals)

# Six silhouette edges: opposite facing statuses across the two triangles
# adjacent to an edge of the icosahedron.
edge_faces=defaultdict(list)
for idx,tri in enumerate(faces):
    for a,b in combinations(tri,2):edge_faces[tuple(sorted((a,b)))].append(idx)
assert len(edge_faces)==30 and all(len(owners)==2 for owners in edge_faces.values())
for x in normals:
    ss=[sgn(vdot(x,c)) for c in centroids]
    assert 0 not in ss
    assert sum(ss[i]!=ss[j] for i,j in edge_faces.values())==6

# Auxiliary, independent approximate quadrature; never part of the exact proof.
def approx_area(U):
    return sqrt(3/num(Nc))*sum(abs(sum(num(a)*z for a,z in zip(c,U))) for c in C)
N=65536
bmax=sqrt(num(B2)); t0=sqrt(num(T2))
for t in (t0, (t0+bmax)/2, 0.99*bmax):
    count=0
    for i in range(N):
        z=1-2*(i+0.5)/N
        a=2*pi*i*((sqrt(5)-1)/2)
        U=(sqrt(1-z*z)*cos(a),sqrt(1-z*z)*sin(a),z)
        count+=approx_area(U)>=t
    empirical=count/N
    expected=10*(1-t/bmax)
    assert abs(empirical-expected)<0.001
    print('quadrature',round(t,9),round(empirical,8),round(expected,8))
print('PASS exact faces=20 generators=10 sign patterns=1024 spectrum=18')
print('PASS max vectors=20 maximum-area-square', B2, 'threshold-square',T2)
print('PASS separated cap law, six-sided silhouettes, exact field inequalities')
