#!/usr/bin/env python3
"""Exact-rational and floating-point checks of bipartite thermal factorization.

Dependencies: Python 3 standard library only.  Does not replace the theorem proof.
"""
from fractions import Fraction as F
from random import Random


def transpose(a):
    return [list(row) for row in zip(*a)]


def mul(a, b):
    bt = transpose(b)
    return [[sum(x*y for x,y in zip(row, col)) for col in bt] for row in a]


def plus(a, b):
    return [[x+y for x,y in zip(ra,rb)] for ra,rb in zip(a,b)]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def inverse(a):
    n = len(a)
    z = [list(row)+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for i in range(n):
        p = next(k for k in range(i,n) if z[k][i])
        z[i],z[p] = z[p],z[i]
        t=z[i][i]
        z[i] = [v/t for v in z[i]]
        for k in range(n):
            if k != i:
                t=z[k][i]
                z[k]=[v-t*w for v,w in zip(z[k],z[i])]
    return [row[n:] for row in z]


def cov(m, d):
    n=len(m)
    mt=transpose(m)
    lhs=[]
    rhs=[]
    for i in range(n):
        for j in range(n):
            lhs.append([m[i][k]*F(k2==j)+F(i==k)*mt[k2][j]
                        for k in range(n) for k2 in range(n)])
            rhs.append(-2*d[i][j])
    li=inverse(lhs)
    v=[sum(x*y for x,y in zip(row,rhs)) for row in li]
    return [v[i*n:(i+1)*n] for i in range(n)]


def epr(m,d):
    s=cov(m,d)
    q=plus(mul(m,s),d)
    di=inverse(d)
    return trace(mul(mul(inverse(s), transpose(q)),mul(di,q))),s,q


def instance(p,q,rng):
    n=p+q
    # Gershgorin SPD symmetric blocks with nontrivial internal couplings.
    a=[[F(0) for j in range(p)] for i in range(p)]
    c=[[F(0) for j in range(q)] for i in range(q)]
    for mat in [a,c]:
        k=len(mat)
        for i in range(k):
            for j in range(i+1,k):
                mat[i][j]=mat[j][i]=F(rng.randint(-2,2),4)
        for i in range(k):
            mat[i][i]=F(2+rng.randrange(3)) + sum(abs(mat[i][j]) for j in range(k) if j!=i)
    b=[[F(rng.randint(-4,4),3) for j in range(q)] for i in range(p)]
    if all(v==0 for row in b for v in row):
        b[0][0]=F(1)
    m=[[F(0) for j in range(n)] for i in range(n)]
    for i in range(p):
        for j in range(p):m[i][j]=-a[i][j]
        for j in range(q):m[i][p+j]=-b[i][j]
    for i in range(q):
        for j in range(p):m[p+i][j]=b[j][i]
        for j in range(q):m[p+i][p+j]=-c[i][j]
    return m


def diagonal(t):
    return [[F(t[i]) if i==j else F(0) for j in range(len(t))] for i in range(len(t))]


def check():
    rng=Random(261037030)
    count=0
    for p,q in [(1,1),(1,2),(2,1),(2,2),(1,3),(3,1),(2,3),(3,2)]:
        for rep in range(4):
            m=instance(p,q,rng)
            n=p+q
            e0,s0,q0=epr(m,diagonal([1]*n))
            assert e0>0
            for u,v in [(F(1),F(2)),(F(2),F(5)),(F(13,7),F(1,3))]:
                e,s,c=epr(m,diagonal([u]*p+[v]*q))
                alpha=(u+v)/2
                beta=(u-v)/2
                assert e==alpha*alpha/(u*v)*e0, (p,q,rep,u,v,'epr')
                assert c==[[alpha*z for z in row] for row in q0], (p,q,'current')
                j=diagonal([1]*p+[-1]*q)
                r=mul(inverse(m),j)
                r=[[-z for z in row] for row in r]
                assert r==transpose(r)
                assert s==plus([[alpha*z for z in row] for row in s0],
                               [[beta*z for z in row] for row in r])
                count+=1
    # Reversible uncoupled system, all positive bath choices.
    m=[[F(-2),F(0)],[F(0),F(-3)]]
    for u,v in [(F(1),F(8)),(F(5),F(2))]:
        e,_,q=epr(m,diagonal([u,v]));assert e==0 and q==[[F(0)]*2]*2
        count+=1
    # Violate within-group symmetry: the universal multiplier must fail.
    broken=[[F(-2),F(-1),F(-1)],[F(1),F(-2),F(0)],[F(1),F(0),F(-2)]]
    b0,_,_=epr(broken,diagonal([1,1,1]))
    b1,_,_=epr(broken,diagonal([1,1,2]))
    assert b0==2 and b1==F(307,144) and b1!=F(9,8)*b0
    count+=1
    print(f'PASS: {count} independent exact-rational temperature / drift cases; '
          'each nontrivial case verified the EPR, irreversible current and covariance identities.')


if __name__=='__main__':check()
