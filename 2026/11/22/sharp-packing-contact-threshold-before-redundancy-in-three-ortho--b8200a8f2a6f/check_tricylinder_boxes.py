#!/usr/bin/env python3
"""Reproducible finite diagnostics for a three-cylinder inscribed-box classification.
The analytic proof is in RESULT.md; numerical tests are not a proof of universality.
Only standard-library modules are required.
"""
import math, random


def solve(alpha, beta, gamma):
    assert 0 < alpha <= beta <= gamma
    disc = math.sqrt(alpha*alpha - alpha*beta + beta*beta)
    critical = (alpha + beta + 2*disc)/3
    if gamma <= critical:
        U = (alpha+gamma-beta)/2
        V = (alpha+beta-gamma)/2
        W = (beta+gamma-alpha)/2
        branch = 'all-three'
    else:
        V = (alpha+beta-disc)/3
        U, W = alpha - V, beta - V
        branch = 'first-two'
    return U,V,W,critical,branch


def check_one(alpha,beta,gamma):
    U,V,W,crit,branch = solve(alpha,beta,gamma)
    assert min(U,V,W)>0
    sc = max(alpha,beta,gamma)
    tol = 2e-10*sc
    assert U+V <= alpha+tol and V+W<=beta+tol and U+W<=gamma+tol
    assert abs(U+V-alpha)<tol and abs(V+W-beta)<tol
    if branch=='all-three':
        assert abs(U+W-gamma)<tol
        l1 = (1/U + 1/V - 1/W)/2
        l2 = (1/V + 1/W - 1/U)/2
        l3 = (1/U + 1/W - 1/V)/2
        assert min(l1,l2,l3)>-2e-9/sc
    else:
        l1,l2,l3 = 1/U,1/W,0.0
        assert U+W < gamma+tol
        assert abs(1/V-l1-l2) < 2e-9/sc
    assert abs((l1+l3)*U-1)<2e-9
    assert abs((l1+l2)*V-1)<2e-9
    assert abs((l2+l3)*W-1)<2e-9
    assert crit>=beta-2e-12*sc and crit<alpha+beta
    # KKT dual certificate: concavity yields the global upper bound.
    # Logarithm tangent plus complementary slackness implies
    # sum(log trial squares) <= sum(log optimal squares).
    opt = math.log(U)+math.log(V)+math.log(W)
    rr=random.Random(int((alpha+beta+gamma)*1e7) % (2**32))
    for _ in range(80):
        # Feasible squares from scaling positive random radii.
        p,q,r = [rr.random()+1e-8 for j in range(3)]
        t=min(math.sqrt(alpha/(p+q)),math.sqrt(beta/(q+r)),math.sqrt(gamma/(p+r)))
        # Alternative strictly feasible boxes, including random scaling.
        t *= rr.uniform(.15,1)
        x,y,z=p*t*t,q*t*t,r*t*t
        assert math.log(x)+math.log(y)+math.log(z) <= opt+1e-9
    return (U,V,W,crit,branch)


def main():
    n=0
    for a,b,c in [(1.,1.,1.),(1.,1.,4/3),(1.,1.,1.5),(1.,1.,2.),
                  (1.,4.,4.),(1.,4.,5.),(1.,100.,100.1)]:
        check_one(a,b,c); n+=1
    rr=random.Random(20261117)
    for _ in range(2500):
        a,b,c=sorted(math.exp(rr.uniform(-2.5,2.5)) for j in range(3))
        check_one(a,b,c);n+=1
    # Check C1/not-C2 benchmark at equal smallest radii:
    a=b=1.;c0=4/3
    U0,V0,W0,_,_=solve(a,b,c0)
    assert max(abs(U0-2/3),abs(V0-1/3),abs(W0-2/3))<1e-14
    f0=math.log(8)+0.5*(math.log(U0)+math.log(V0)+math.log(W0))
    assert abs(8*math.sqrt(U0*V0*W0)-16/(3*math.sqrt(3)))<1e-13
    for h in [1e-2,1e-3,1e-4]:
        U,V,W,_,_=solve(1,1,c0-h)
        f=math.log(8)+.5*(math.log(U)+math.log(V)+math.log(W))
        assert abs((f-f0)/(h*h)+27/32)<0.02
        Up,Vp,Wp,_,_=solve(1,1,c0+h)
        assert abs(math.log(8)+.5*(math.log(Up)+math.log(Vp)+math.log(Wp))-f0)<1e-13
    print('PASS',n,'parameter cases, 80 independent feasible competitors per case, and exact benchmark/transition checks')

if __name__=='__main__':main()
