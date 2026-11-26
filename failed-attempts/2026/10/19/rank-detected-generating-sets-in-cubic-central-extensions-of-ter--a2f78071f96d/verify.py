#!/usr/bin/env python3
"""Finite verification for cubic central extensions of ternary midpoint quandles."""
from itertools import product
from random import Random

P = 3

def core(u, v):
    return tuple((-x-y) % P for x, y in zip(u, v))

def make_operations(d, seed=0):
    rng=Random(seed)
    M=[[0]*d for _ in range(d)]
    for i in range(d):
        for j in range(i+1,d):
            t=rng.randrange(3); M[i][j]=t; M[j][i]=-t
    L=[rng.randrange(3) for _ in range(d)]
    def B(x,y):
        return sum(M[i][j]*x[i]*y[j] for i in range(d) for j in range(d))%3
    def l(x):
        return sum(L[i]*x[i] for i in range(d))%3
    def phi(x,y):
        return B(x,y)*(l(x)-l(y))%3
    def T(x,y,z):
        return (B(x,y)*l(z)+B(y,z)*l(x)+B(z,x)*l(y))%3
    return phi,T

def canonical(x,y):
    u,a=x[:-1],x[-1]
    v,b=y[:-1],y[-1]
    return core(u,v)+((-a-b + (u[0]*v[1]-u[1]*v[0])*(u[2]-v[2]))%3,)

def closure(xs):
    A=set(xs)
    while True:
        U = A | {canonical(x,y) for x in A for y in A}
        if U == A: return A
        A = U

def det(a,b,c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0])) % 3

def subtract(x,y):
    return tuple((a-b)%3 for a,b in zip(x,y))

def rank(vectors):
    if not vectors: return 0
    mat=[list(row) for row in vectors]
    m=len(mat); n=len(mat[0]); row=0
    for col in range(n):
        pivot=next((t for t in range(row,m) if mat[t][col]%3),None)
        if pivot is None:continue
        mat[row],mat[pivot]=mat[pivot],mat[row]
        inv=pow(mat[row][col],-1,3)
        mat[row]=[(a*inv)%3 for a in mat[row]]
        for i in range(m):
            if i!=row:
                t=mat[i][col]
                mat[i]=[(v-t*w)%3 for v,w in zip(mat[i],mat[row])]
        row+=1
        if row==m:break
    return row

Q=list(product(range(3),repeat=4))
assert len(Q)==81
for x in Q:
    assert canonical(x,x)==x
    assert len({canonical(y,x) for y in Q})==81
    for y in Q:
        assert canonical(x,y)==canonical(y,x)
        assert canonical(canonical(x,y),y)==x
for x in Q:
    for y in Q:
        for z in Q:
            assert canonical(canonical(x,y),z)==canonical(canonical(x,z),canonical(y,z))
o=(0,0,0,0);a=(1,0,0,0);b=(0,1,0,0);c=(0,0,1,0)
assert canonical(canonical(o,a),canonical(b,c))==(1,1,1,1)
assert canonical(canonical(o,b),canonical(a,c))==(1,1,1,2)
assert len(closure([o,a,b,c]))==81
# All 4-tuples of projected points: rank-3 tuples have the predicted count.
V=list(product(range(3),repeat=3))
count=0
for u in V:
    for v in V:
        for w in V:
            for z in V:
                if det(subtract(v,u),subtract(w,u),subtract(z,u)):
                    count+=1
assert count==27*26*24*18==303264
# For every tuple of rank <3 the generated subset cannot project surjectively.
for x,y,z in [(o,a,b),(o,b,c),(o,a,c),(a,b,c)]:
    assert len(closure([x,y,z])) < 81
# Cubic cocycle and defect identity for general alternating B and linear L.
rng=Random(470119)
for d in (3,4,5):
    for trial in range(10):
        phi,T=make_operations(d,seed=trial*13+d)
        vectors=list(product(range(3),repeat=d)) if d==3 else [tuple(rng.randrange(3) for _ in range(d)) for _ in range(250)]
        for _ in range(2000):
            u,v,w,z=[vectors[rng.randrange(len(vectors))] for _ in range(4)]
            sd=lambda x,y:core(x,y)
            ident=(phi(sd(u,v),w)-phi(u,v)-phi(sd(u,w),sd(v,w))+phi(u,w)+phi(v,w))%3
            assert ident==0
            defect=(-phi(u,v)-phi(w,z)+phi(sd(u,v),sd(w,z))
                    +phi(u,w)+phi(v,z)-phi(sd(u,w),sd(v,z)))%3
            dd=[subtract(t,u) for t in (v,w,z)]
            assert defect==(-T(*dd))%3
# Random higher-arity generating tuples in the canonical family, checked by closure.
for k in (4,5,6):
    for j in range(20):
        xs=[Q[rng.randrange(81)] for _ in range(k)]
        projected=[x[:3] for x in xs]
        r=rank([subtract(v,projected[0]) for v in projected[1:]])
        assert (len(closure(xs))==81)==(r==3)
print('VERIFY_OK: 81-point quandle; 531441 distributivity tests; 531441 projected quadruples; cubic cocycle and defect; generating tuples')
