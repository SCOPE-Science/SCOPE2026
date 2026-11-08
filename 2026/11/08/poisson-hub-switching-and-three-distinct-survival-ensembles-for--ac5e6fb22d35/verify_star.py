"""Finite-state checks for star-graph collision-free walk identities.

Run: python star_hub_checker.py
Uses only the standard library. Tests supplement the analytic theorem.
"""
from itertools import permutations
from math import comb, factorial, isclose, sqrt, exp, cosh, sinh
from fractions import Fraction

checks = 0

def eq(a,b,eps=2e-12):
    global checks
    checks += 1
    assert isclose(float(a),float(b),rel_tol=eps,abs_tol=eps),(a,b)

for n in range(3,8):
    for k in range(2,n):
        r=Fraction(n-k,n-1)
        s=sqrt(float(k*r))
        lam=k-s
        hA=sqrt(k)
        hB=sqrt(float(r))
        eq(lam,k-s)
        eq(-k*hA + k*hB,-lam*hA)
        eq(r*hA-k*hB,-lam*hB)
        eq(k*hB/hA,s)
        eq(float(r)*hA/hB,s)
        # Injective labeled configurations on the star: 0 is the hub.
        states=list(permutations(range(n),k))
        for st in states:
            hubs=sum(x==0 for x in st)
            assert hubs in (0,1)
            h=hB if hubs else hA
            outgoing=[]
            killing=0.0
            for i,x in enumerate(st):
                if x==0:
                    for y in range(1,n):
                        rate=1/(n-1)
                        if y in st: killing+=rate
                        else:
                            dst=list(st);dst[i]=y
                            outgoing.append((tuple(dst),rate))
                else:
                    if 0 in st: killing+=1
                    else:
                        dst=list(st);dst[i]=0
                        outgoing.append((tuple(dst),1.0))
            eq(sum(v for _,v in outgoing)+killing,k)
            eq(killing, (k-1)*(1+1/(n-1)) if hubs else 0)
            Qh=-k*h+sum(v*(hB if 0 in dst else hA) for dst,v in outgoing)
            eq(Qh,-lam*h)
            eq(sum(v*(hB if 0 in dst else hA)/h for dst,v in outgoing),s)
            eq(sum(v for _,v in outgoing),float(r) if hubs else k)
        # Counts, equilibrium hub fractions, and exact Yaglom limit.
        countA=factorial(n-1)//factorial(n-1-k)
        countB=k*factorial(n-1)//factorial(n-k)
        eq(countB/countA,k/(n-k))
        eq(countB/countA*(n-1)*hB*hB/(hA*hA),1)
        eq((k/(k+float(r))) + (float(r)/(k+float(r))),1)
        for t in (0.0,.1,.4,1.0,3.0):
            sa=exp(-k*t)*(cosh(s*t)+(k/s)*sinh(s*t))
            sb=exp(-k*t)*(cosh(s*t)+(float(r)/s)*sinh(s*t))
            eq(sa,exp(-(k-s)*t)*(.5*(1+k/s)) + exp(-(k+s)*t)*(.5*(1-k/s)))
            eq(sb,exp(-(k-s)*t)*(.5*(1+float(r)/s)) + exp(-(k+s)*t)*(.5*(1-float(r)/s)))
            eq((1-exp(-2*s*t))/2, .5-.5*exp(-2*s*t))
print('PASS:',checks,'finite-state and numerical identities; n=3,...,7; 2<=k<n')
