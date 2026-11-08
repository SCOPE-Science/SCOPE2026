#!/usr/bin/env python3
"""Reproducibility checks for a flat-bulk recycled spectral scaling theorem.
Checks numerical spectral formulas, sharp global scaling, and finite-step CG.
These checks corroborate but do not replace the analytic proof.
"""
import math
import random
from fractions import Fraction
import numpy as np

def predicted(a,b,c,t):
    g2=t*t/a
    threshold=(b-c)**2/b
    if g2 <= threshold:
        opt=c*(b-c)/(b-c-g2)
        cond=b/c + g2/(b-c-g2)
        branch='collision'
    else:
        opt=b
        z=math.sqrt(b*g2)
        cond=(b+z)/(b-z)
        branch='balance'
    two=(g2 < b-c)
    theta_collision=(c*(b-c)/(b-c-g2)) if two else None
    return opt,cond,branch,two,theta_collision

def matrix(a,b,c,t,theta,m):
    out=np.diag([theta,b]+[c]*m)
    off=t*math.sqrt(theta/a)
    out[0,1]=out[1,0]=off
    return out

def cond(x):
    e=np.linalg.eigvalsh(x)
    return e[-1]/e[0]

def cg_steps(B,r,steps=3):
    # RHS chosen in B coordinates, x0=0
    x=np.zeros(B.shape[0]); res=r.copy(); d=res.copy(); rr=res@res
    for k in range(1,steps+1):
        alp=rr/(d@(B@d)); x+=alp*d; res-=alp*(B@d)
        rnew=res@res
        if np.linalg.norm(res)<1e-8*max(1,np.linalg.norm(r)):
            return k
        d=res+(rnew/rr)*d; rr=rnew
    return steps+1

def run():
    count=0
    rng=random.Random(290517)
    # Exact-rational crossing and threshold checks (no floats in identities)
    for b in range(2,30):
        for c in range(1,b):
            B=Fraction(b); C=Fraction(c)
            s=(B-C)**2/B
            # Three rational coupling regimes
            for factor in (Fraction(1,4),Fraction(1),Fraction(5,4)):
                u=s*factor
                if u>=B: continue
                if u<B-C:
                    theta=C*(B-C)/(B-C-u)
                    assert (theta-C)*(B-C)==theta*u
                    assert (theta<=B)==(u<=s)
                    count+=2
                else:
                    assert u>=B-C
                    count+=1
    # Random continuous parameter tests, many dimensions / both branches
    for i in range(4000):
        c=10**rng.uniform(-2,1)
        b=c*(1+10**rng.uniform(-2,1.7))
        a=b*(1+10**rng.uniform(-2,1.7))
        u=b*rng.uniform(.0002,.9998)
        t=math.sqrt(a*u)
        m=rng.randint(1,10)
        opt,ko,branch,two,tc=predicted(a,b,c,t)
        B=matrix(a,b,c,t,opt,m)
        observed=cond(B)
        assert math.isclose(observed,ko,rel_tol=2e-8,abs_tol=1e-8),(a,b,c,t,observed,ko)
        count+=1
        if two:
            evals=np.linalg.eigvalsh(matrix(a,b,c,t,tc,m))
            assert abs(evals[0]-c)<1e-7*max(1,c), (a,b,c,t,tc,evals)
            count+=1
        for delta in (.02,.05,.1,.25,.5,1,2,4,10):
            theta=opt*delta
            assert cond(matrix(a,b,c,t,theta,m))>=ko-1e-7*max(1,ko), (a,b,c,t,theta,ko)
            count+=1
    # Explicit exact examples and generic CG iteration-count verification
    a,b,c=9.,4.,1.
    for u in (1., 2.5, 3., 3.5):
        t=math.sqrt(a*u)
        opt,k,branch,two,tc=predicted(a,b,c,t)
        print('example',{'g2':u,'optimal_scale':opt,'optimal_kappa':k,'branch':branch,
                         'two_step_possible':two,'collision_scale':tc})
        rhs=np.ones(6);rhs[1]=2.;rhs[2:]=np.linspace(.1,1.0,4)
        if two:
            B=matrix(a,b,c,t,tc,4)
            assert cg_steps(B,rhs)==2
        else:
            assert cg_steps(matrix(a,b,c,t,opt,4),rhs)==3
        count+=1
    print('PASS',count,'checks')

if __name__=='__main__':run()
