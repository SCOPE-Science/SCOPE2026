#!/usr/bin/env python3
"""Independent exact and randomized checks for parallelogram moment reconstruction."""
from fractions import Fraction as F
from math import comb, sqrt
import random

def dmoment(k):
    # Difference of two independent uniforms on [0,1].
    return F(0) if k%2 else F(2,(k+1)*(k+2))

def moments_expansion(u,v,z,n):
    # d^2 = u U^2 + v V^2 + z UV; exact polynomial integration
    value=F(0)
    for i in range(n+1):
        for j in range(n-i+1):
            h=n-i-j
            coefficient=F(comb(n,i)*comb(n-i,j))*u**i*v**j*z**h
            value += coefficient*dmoment(2*i+h)*dmoment(2*j+h)
    return value

def inverse(m2,m4,m6):
    S=6*m2
    X=90*(m4-S*S/F(15))
    Y=420/S*(m6-S*S*S/F(28))
    p=(5*Y-28*X)/41
    cos2=(X/F(p)+7)/10
    return S,p,cos2

def check(u,v,cos2):
    z2=4*u*v*cos2
    # For 2nd and 3rd powers, odd z terms vanish; evaluating at sqrt(z2)
    # is avoided by factoring the even terms independently.
    n2=(u*u+v*v)/15+u*v/F(18)+z2/F(36)
    n3=(u**3+v**3)/28+u*v*(u+v)/30+(u+v)*z2/F(30)
    m2=(u+v)/6
    S,p,c=inverse(m2,n2,n3)
    assert S==u+v,(S,u+v)
    assert p==u*v,(p,u*v)
    assert c==cos2,(c,cos2)
    assert moments_expansion(u,v,F(0),1)==m2
    assert moments_expansion(u,v,F(0),2)==(u*u+v*v)/15+u*v/F(18)
    return (m2,n2,n3)

if __name__=='__main__':
    rr=random.Random(20261102)
    for _ in range(1200):
        u=F(rr.randint(1,100),rr.randint(1,20))
        v=F(rr.randint(1,100),rr.randint(1,20))
        cos2=F(rr.randint(0,99),100)
        check(u,v,cos2)
    # Integrate the full two-variable polynomial with nonzero cross terms,
    # independently of the closed moment formulas.
    for aa,bb,ct in [(3,4,F(3,5)),(5,7,F(4,5)),(2,9,F(5,13)),(11,13,F(0))]:
        u,v=F(aa*aa),F(bb*bb)
        c2=ct*ct
        z=2*aa*bb*ct
        analytical=check(u,v,c2)
        for j in range(1,4):
            assert moments_expansion(u,v,z,j)==analytical[j-1]
    P=check(F(1),F(4),F(1,2))
    Q=check(F(5,2),F(5,2),F(143,250))
    assert P[:2]==Q[:2]
    assert P[2]!=Q[2]
    print('exact_ambiguous_pair',P,Q)
    # Numerically compare polynomial formulas to geometric simulations
    N=150000
    for u,v,cc in [(1.,4.,0.5),(2.5,2.5,143/250),(2.,3.,0.2),(0.3,0.9,0.)]:
        cost=sqrt(cc)
        z=2*sqrt(u*v)*cost
        ms=[0.,0.,0.]
        for k in range(N):
            U=rr.random()-rr.random()
            V=rr.random()-rr.random()
            D2=u*U*U+v*V*V+z*U*V
            ms[0]+=D2;ms[1]+=D2**2;ms[2]+=D2**3
        ms=[x/N for x in ms]
        exact=check(F(str(u)),F(str(v)),F(str(cc)))
        # generous 6-sigma scale sample error tolerances
        for observed,claimed in zip(ms,exact):
            if claimed>0:
                assert abs(observed-float(claimed))<0.065*float(claimed),(ms,exact)
        print('random_moments',u,v,cc,'empirical',list(map(lambda x:round(x,7),ms)), 'exact',list(map(float,exact)))
    # Convex-order inequality for fixed side lengths: check fifth power on shared abs coords
    U=[abs(rr.random()-rr.random()) for _ in range(35000)]
    V=[abs(rr.random()-rr.random()) for _ in range(35000)]
    prev=-1.
    for c in [0.,0.1,0.2,0.5,0.9,0.99]:
        val=sum((((x*x+4*y*y+4*c*x*y)**5 + (x*x+4*y*y-4*c*x*y)**5)/2) for x,y in zip(U,V))/len(U)
        assert val>prev
        prev=val
    print('VERIFY_OK exact_parameter_reconstructions=1200 random_configurations=',4*N,'convex_order_test_points=',len(U))
