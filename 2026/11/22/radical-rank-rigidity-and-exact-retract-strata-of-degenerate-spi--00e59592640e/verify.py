#!/usr/bin/env python3
"""Exact checks of finite-field Jordan endomorphism and retraction formulas.
Standard Python 3 only; all arithmetic is in prime finite fields.
"""
from itertools import product
from math import prod


def jordan_product(x, y, q):
    # Coordinates (scalar,w0,w1,r) for B=diag(1,1,0).
    a, v0, v1, vr = x
    b, w0, w1, wr = y
    return ((a*b + v0*w0+v1*w1)%q,
            (a*w0+b*v0)%q, (a*w1+b*v1)%q, (a*wr+b*vr)%q)


def exhaustive_unital(q=3):
    # Images of the 3 nonidentity basis elements must have the same squares.
    # This is a logically necessary filter, and therefore still exhausts ALL
    # q^(4*3) unital linear maps, not merely a random sample.
    vectors = list(product(range(q), repeat=4))
    zero=(0,0,0,0); one=(1,0,0,0)
    square_one=[x for x in vectors if jordan_product(x,x,q)==one]
    square_zero=[x for x in vectors if jordan_product(x,x,q)==zero]
    assert q**12 == len(vectors)**3
    counts={3:0,4:0}
    for x,y,z in product(square_one,square_one,square_zero):
        if jordan_product(x,y,q)!=zero: continue
        if jordan_product(x,z,q)!=zero: continue
        if jordan_product(y,z,q)!=zero: continue
        # The classification predicts no scalar parts; W columns form an isometry,
        # and the radical maps only into the radical.
        assert x[0]==y[0]==z[0]==0
        assert z[1]==z[2]==0
        assert (x[1]*x[1]+x[2]*x[2])%q==1
        assert (y[1]*y[1]+y[2]*y[2])%q==1
        assert (x[1]*y[1]+x[2]*y[2])%q==0
        counts[3+(z[3]!=0)]+=1
    assert counts=={3:72,4:144},counts
    # A map with primitive-idempotent image would be a Jordan character;
    # test every linear character on the 3-vector pure component.
    chars=sum(all((f[i]*f[j]-(i==j and i<2))%q==0
                  for i in range(3) for j in range(3))
              for f in product(range(q),repeat=3))
    assert chars==0
    print('unital endomorphism ranks over F3:',counts,
          '; primitive-image characters:',chars)


def rank(M,q):
    A=[row[:] for row in M]; n=len(A); pivot=0
    for c in range(n):
        k=next((i for i in range(pivot,n) if A[i][c]%q),None)
        if k is None:continue
        A[pivot],A[k]=A[k],A[pivot]
        v=pow(A[pivot][c],-1,q)
        A[pivot]=[(x*v)%q for x in A[pivot]]
        for i in range(n):
            if i==pivot:continue
            b=A[i][c]
            A[i]=[(x-b*y)%q for x,y in zip(A[i],A[pivot])]
        pivot+=1
    return pivot


def gaussian(n,j,q):
    return prod(q**(n-i)-1 for i in range(j))//prod(q**(j-i)-1 for i in range(j))


def check_retractions(q,r,m):
    counts=[0]*(r+1)
    for data in product(range(q),repeat=r*r):
        U=[list(data[i*r:(i+1)*r]) for i in range(r)]
        if any(sum(U[i][k]*U[k][j] for k in range(r))%q!=U[i][j]
               for i in range(r) for j in range(r)):
            continue
        j=rank(U,q)
        counts[j]+=q**(m*(r-j))
    formula=[gaussian(r,j,q)*q**((r-j)*(m+j)) for j in range(r+1)]
    assert counts==formula,(counts,formula)
    print(f'F{q}, W dimension {m}, radical dimension {r}:',counts)


if __name__=='__main__':
    exhaustive_unital()
    check_retractions(3,1,2)
    check_retractions(3,2,2)
    print('DEGENERATE_SPIN_RETRACTIONS_VERIFIED')
