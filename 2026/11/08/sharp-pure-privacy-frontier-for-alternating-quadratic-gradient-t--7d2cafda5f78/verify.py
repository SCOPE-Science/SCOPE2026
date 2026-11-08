#!/usr/bin/env python3
"""Exact-rational reproducibility checks for the quadratic privacy theorem.

Only standard-library fractions are used. These checks supplement the proof.
"""
from fractions import Fraction as F


def sensitivity_next(t, x, z):
    # x=Delta-x/(alpha*a); z=-Delta-y/a for 0<t<1.
    return t*x+(1-t)*z, t*(1-t)*(x-z)


def generating_sums(t, r):
    den=r*r-r*t*t+t*t-t
    assert den>0
    return r*(r+1-t)/den, r*r*(1-t)/den


def check_symbolic_by_rational_grid():
    count=0
    for d in range(2,21):
        for j in range(1,d):
            t=F(j,d)
            x,z=F(1),1-t
            for k in range(18):
                assert x>=z>=0
                x,z=sensitivity_next(t,x,z)
                count+=1
            for rr in range(1,21):
                r=F(rr,21)
                den=r*r-r*t*t+t*t-t
                if den<=0: continue
                sx,sz=generating_sums(t,r)
                x2,z2=sensitivity_next(t,sx,sz)
                assert sx-x2/r==1
                assert sz-z2/r==1-t
                assert sx>0 and sz>0
                count+=1
    return count


def transcript_shifts():
    # Three agents, independent arbitrary local intercepts, exact common messages.
    # W is symmetric, strictly positive, doubly stochastic.
    W=[[F(1,2),F(1,4),F(1,4)],
       [F(1,4),F(1,2),F(1,4)],
       [F(1,4),F(1,4),F(1,2)]]
    h=F(5,4); alpha=F(2,5); t=alpha*h
    hvec=[F(3,5), h, F(7,3)] # genuinely heterogeneous local curvatures
    b=[F(-3,4),F(7,5),F(2,3)]
    a=F(3,7); changed=1
    x=[[F(0)]*3 for _ in range(2)]
    y=[[b[i]+(a if c==1 and i==changed else 0) for i in range(3)] for c in range(2)]
    expected_x,expected_z=F(1),1-t
    checks=0
    for k in range(14):
        if k%2==1:
            assert x[0][changed]-x[1][changed]==alpha*a*expected_x
            assert y[0][changed]-y[1][changed]==-a*expected_z
            for i in [0,2]:
                assert x[0][i]==x[1][i] and y[0][i]==y[1][i]
            checks+=4
            # The same realized public messages are conditioned on in both runs.
            msgx=[F((k+1)*i+1,11) for i in range(3)]
            msgy=[F((k+2)*(3-i),13) for i in range(3)]
            nextx=[[sum(W[i][j]*msgx[j] for j in range(3))-alpha*y[c][i] for i in range(3)] for c in range(2)]
            nexty=[[sum(W[i][j]*msgy[j] for j in range(3))+
                   hvec[i]*(nextx[c][i]-x[c][i]) for i in range(3)] for c in range(2)]
            expected_x,expected_z=sensitivity_next(t,expected_x,expected_z)
        else:
            nextx=[[x[c][i]-alpha*y[c][i] for i in range(3)] for c in range(2)]
            nexty=[[y[c][i]+hvec[i]*(nextx[c][i]-x[c][i]) for i in range(3)] for c in range(2)]
        x,y=nextx,nexty
    return checks



def likelihood_ratio_certificate():
    # Exact finite-prefix worst-case log likelihood ratio for adaptive messages.
    h=F(1); hvec=[h,F(3,2)]; alpha=F(1,2); q=F(2,1)/F(5,2) # 4/5, so r=16/25
    # Use q=2/sqrt(5) only in theory; for rational tests choose q=9/10.
    q=F(9,10); r=q*q
    W=[[F(3,4),F(1,4)],[F(1,4),F(3,4)]]
    b=[F(2,3),F(-1,4)]; a=F(2,3)
    x=[[F(0)]*2 for _ in range(2)]
    y=[[b[i]+(a if c==1 and i==0 else 0) for i in range(2)] for c in range(2)]
    eps=F(0); predicted=F(0); count=0
    X,Z=F(1),F(1,2)
    for k in range(20):
        if k%2==1:
            assert x[0][0]-x[1][0]==alpha*a*X
            assert y[0][0]-y[1][0]==-a*Z
            scale=q**(k-1)
            msgx=[max(x[0][0],x[1][0])+3,F(1,7)]
            msgy=[min(y[0][0],y[1][0])-3,F(2,7)]
            # log p(dataset=0)/p(dataset=1) under conditional Laplace densities
            eps+= (abs(msgx[0]-x[1][0])-abs(msgx[0]-x[0][0]))/scale
            eps+= (abs(msgy[0]-y[1][0])-abs(msgy[0]-y[0][0]))/scale
            predicted+=(alpha*a*X+a*Z)/scale
            assert eps==predicted
            X,Z=sensitivity_next(F(1,2),X,Z)
            nextx=[[sum(W[i][j]*msgx[j] for j in range(2))-alpha*y[c][i] for i in range(2)] for c in range(2)]
            nexty=[[sum(W[i][j]*msgy[j] for j in range(2))+hvec[i]*(nextx[c][i]-x[c][i]) for i in range(2)] for c in range(2)]
            count+=1
        else:
            nextx=[[x[c][i]-alpha*y[c][i] for i in range(2)] for c in range(2)]
            nexty=[[y[c][i]+hvec[i]*(nextx[c][i]-x[c][i]) for i in range(2)] for c in range(2)]
        x,y=nextx,nexty
    return count


def explicit_certificate():
    t=F(1,2); r=F(4,5)
    sx,sz=generating_sums(t,r)
    assert (sx,sz)==(F(104,19),F(32,19))
    # h=1, alpha=1/2, dx=dy=delta=1:
    assert F(1,2)*sx+sz==F(84,19)
    # Quadratic at r evaluated with rational arithmetic is positive.
    assert r*r-r*t*t+t*t-t==F(19,100)
    # The earlier comparison matrix cannot have rho below 1 at t=1/2,
    # since its characteristic polynomial at 1 is 1-3t-2t^2 < 0.
    assert 1-3*t-2*t*t<0
    return F(84,19)


if __name__=='__main__':
    count=check_symbolic_by_rational_grid()
    count+=transcript_shifts()
    count+=likelihood_ratio_certificate()
    explicit_certificate()
    print('PASS:',count,'exact rational assertions/checkgroups; epsilon=84/19')
