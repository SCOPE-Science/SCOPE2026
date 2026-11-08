#!/usr/bin/env python3
"""Standard-library diagnostic checker for Gaussian rank-one Krylov memory law.
The analytic proof is separate; this checks numerical instances and source-equivalent updates.
"""
import math
import random


def dot(u, v):
    return sum(a*b for a,b in zip(u,v))


def norm2(u):
    return dot(u,u)


def sub(u, v, scale=1.0):
    return [a-scale*b for a,b in zip(u,v)]


def project(g, basis):
    v = list(g)
    for p in basis:
        v=sub(v,p,dot(v,p)/norm2(p))
    return v


def run(d, ell, steps, rng, raw=False):
    e = [1.0]+[0.0]*(d-1)
    history=[]
    initial=norm2(e)
    ratios=[]
    for k in range(steps):
        g=[rng.gauss(0,1) for _ in range(d)]
        window=history[-(ell-1):] if ell>1 else []
        if raw:
            z=dot(g,e)
            grad=[z*t for t in g]
            p=project(grad,window)
            # Actual sketch scalar used by source.
            step=z*z/norm2(p)
            new=sub(e,p,step)
            # Verify exact line-search equivalence.
            vp=project(g,window)
            model=sub(e,vp,dot(e,vp)/norm2(vp))
            assert math.dist(new,model)<3e-9
        else:
            p=project(g,window)
            new=sub(e,p,dot(e,p)/norm2(p))
        r=norm2(new)/norm2(e)
        ratios.append(r)
        history.append(p)
        e=new
        if ell==d and k==d-1:
            assert norm2(e)<5e-24
            break
    return ratios, norm2(e)/initial


def main():
    rng=random.Random(47931)
    trials=5000
    checks=0
    for d,ell in [(2,1),(2,2),(3,1),(3,2),(3,3),(5,1),(5,2),(5,3),(5,4),(5,5),(8,4)]:
        K=min(5,d) if ell==d else 6
        observed=[[0.0,0.0] for _ in range(K)]
        finals=0.0
        for _ in range(trials):
            rs,energy=run(d,ell,K,rng)
            finals+=energy
            for j,r in enumerate(rs):
                observed[j][0]+=r
                observed[j][1]+=r*r
            checks+=1
        predicted=1.0
        for k,(a,b) in enumerate(observed):
            m=d-min(k,ell-1)
            expected=0.0 if m==1 else (m-1)/m
            expected2=0.0 if m==1 else (m*m-1)/(m*(m+2))
            assert abs(a/trials-expected)<0.03,(d,ell,k,a/trials,expected)
            assert abs(b/trials-expected2)<0.03,(d,ell,k,b/trials,expected2)
            predicted*=expected
            checks+=2
        assert abs(finals/trials-predicted)<0.025,(d,ell,finals/trials,predicted)
        checks+=1
    for d,ell in [(3,2),(5,3),(6,2)]:
        for _ in range(140):
            run(d,ell,4,rng,raw=True)
            checks+=1
    print('PASS; deterministic seed; checks=',checks,
          '; independent beta means and second moments, total mean, raw-algorithm equivalence')

if __name__=='__main__':
    main()
