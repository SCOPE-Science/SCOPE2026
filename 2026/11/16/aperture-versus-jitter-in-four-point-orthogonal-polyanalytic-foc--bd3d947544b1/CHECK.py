"""Exact four-point distance-graph certificate and numerical sensitivity checks.

Python 3.10+, standard library only. All enumerated graph claims use
integer arithmetic in Q(sqrt(3)); numerical checks are illustrative only.
"""
from itertools import product, combinations
from math import sqrt, exp, isclose, hypot

# Represent p+q sqrt(3) as an integer pair.
def add(u, v): return (u[0]+v[0], u[1]+v[1])
def neg(u): return (-u[0], -u[1])
def sub(u,v): return add(u,neg(v))
def mul(u, v): return (u[0]*v[0]+3*u[1]*v[1], u[0]*v[1]+u[1]*v[0])
def det3(A):
    p = (0,0)
    for perm, sgn in [((0,1,2),1),((1,2,0),1),((2,0,1),1),((0,2,1),-1),((2,1,0),-1),((1,0,2),-1)]:
        term=mul(mul(A[0][perm[0]],A[1][perm[1]]),A[2][perm[2]])
        p=add(p,term if sgn==1 else neg(term))
    return p

S=(1,0); L=(2,1)
E4=list(combinations(range(4),2))
allowed=[]
for mask in product((0,1),repeat=6):
    edge=dict(zip(E4,mask))
    def d(i,j):
        if i==j:return (0,0)
        return L if edge[tuple(sorted((i,j)))] else S
    H=[[sub(add(d(0,i),d(0,j)),d(i,j)) for j in range(1,4)] for i in range(1,4)]
    zero = det3(H)==(0,0)
    deg=sorted(sum(mask[k] for k,e in enumerate(E4) if i in e) for i in range(4))
    expected=deg in ([0,1,1,2],[1,2,2,3])
    assert zero == expected, (mask,deg,det3(H))
    if zero:allowed.append(mask)
assert len(allowed)==24

E5=list(combinations(range(5),2))
count_five=0
for mask in product((0,1),repeat=10):
    edge=dict(zip(E5,mask))
    four_ok=True
    for vs in combinations(range(5),4):
        degrees=sorted(sum(edge[e] for e in combinations(vs,2) if v in e) for v in vs)
        if degrees not in ([0,1,1,2],[1,2,2,3]):
            four_ok=False
            break
    if four_ok: count_five+=1
assert count_five==0

a=3-sqrt(3); b=3+sqrt(3)
u=sqrt(a);v=sqrt(b)
A=[complex(-u/2,0),complex(u/2,0),complex(0,sqrt(3)*u/2),complex(0,(1+sqrt(3)/2)*u)]
B=[complex(-v/2,0),complex(v/2,0),complex(0,sqrt(3)*v/2),complex(0,(a-b/2)/(sqrt(3)*v))]

def delta2(z,w):return abs(z-w)**2

def classify(P):
    ds=sorted(delta2(z,w) for z,w in combinations(P,2))
    assert all(min(abs(t-a),abs(t-b))<1e-12 for t in ds)
    return [sum(abs(t-a)<1e-12 for t in ds),sum(abs(t-b)<1e-12 for t in ds)]
assert classify(A)==[4,2]
assert classify(B)==[2,4]

def small_big_eigen(P,i):
    pairs=[(P[i].real-P[j].real,P[i].imag-P[j].imag) for j in range(4) if j!=i]
    xx=sum(exp(-x*x-y*y)*x*x for x,y in pairs)
    yy=sum(exp(-x*x-y*y)*y*y for x,y in pairs)
    xy=sum(exp(-x*x-y*y)*x*y for x,y in pairs)
    return ((xx+yy)-sqrt((xx-yy)**2+4*xy*xy))/2, ((xx+yy)+sqrt((xx-yy)**2+4*xy*xy))/2

def jitter(P):
    vals=[2/sqrt(3)*sqrt(small_big_eigen(P,i)[1]) for i in range(4)]
    return max(vals),vals
JA, av=jitter(A)
JB, bv=jitter(B)
assert isclose(JA,sqrt(10*a/3*exp(-a)),rel_tol=1e-13)
assert isclose(JB,sqrt(2*b/3*exp(-a)),rel_tol=1e-13)
assert av.index(max(av))==2
assert bv.index(max(bv))==3
assert JB<JA
assert sqrt(a)<sqrt(b/3)

# Small-displacement finite difference of the normalized reproducing kernel
# at an actual orthogonal four-node configuration, with fixed alpha=1.
def norm_overlap(z,w):
    d=delta2(z,w)
    l=3-3*d+d*d/2
    return complex(exp(-d/2),0) * l/3 * complex(__import__('cmath').exp(1j*(z*w.conjugate()).imag))

def fdiff(P,i,theta,eps):
    v=complex(__import__('math').cos(theta),__import__('math').sin(theta))
    q=P[i]+eps*v
    return sqrt(sum(abs(norm_overlap(q,P[j]))**2 for j in range(4) if j!=i))/eps
for P in (A,B):
    for i in range(4):
        for theta in (0,0.3,1.1,2.0):
            e=1e-6
            grad=fdiff(P,i,theta,e)
            assert grad <= jitter(P)[0] + 1e-5

print('PASS: 64 exactly classified four-point edge colorings; 24 admissible determinant patterns')
print('PASS: all 1024 five-point colorings violate a four-point necessary condition')
print('PASS: two explicit configurations and normalized-Gram first-order sensitivity')
print('type-A radius and jitter:',sqrt(a),JA)
print('type-B radius and jitter:',sqrt(b/3),JB)
