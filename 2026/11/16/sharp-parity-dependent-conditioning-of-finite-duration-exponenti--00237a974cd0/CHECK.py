"""Reproducibility checks for finite-duration exponentially tapered Gabor windows.

Only finite-frequency and numerical comparisons; the published asymptotics
and optimality for all frequencies rest on the accompanying analytic proof.
Run: python3 CHECK.py (Python 3 standard library only).
"""
import math


def numer_minmax(m, lam, n=6001):
    r = math.exp(-lam)
    minimum, maximum = float("inf"), 0.0
    for k in range(n):
        theta = math.pi * k / (n-1)
        z = complex(r*math.cos(theta), r*math.sin(theta))
        # Direct repeated multiplication, independent of the rational formula.
        power, summation = 1.0 + 0.0j, 0.0 + 0.0j
        for j in range(m):
            summation += power
            power *= z
        val = summation.real**2 + summation.imag**2
        minimum = min(minimum, val)
        maximum = max(maximum, val)
    return minimum, maximum

def analytic_even(m, lam):
    assert m % 2 == 0
    r = math.exp(-lam)
    return ((1-r**m)/(1+r))**2, ((1-r**m)/(1-r))**2

def analytic_three(lam):
    r = math.exp(-lam)
    threshold = 2-math.sqrt(3)
    lo = (1-r+r*r)**2 if r <= threshold else 0.75*(1-r*r)**2
    hi = (1+r+r*r)**2
    return lo,hi

def run():
    count = 0
    for m in range(2, 29, 2):
        for lam in (0.025,0.1,0.25,0.5,1.0,2.,4.):
            lo,hi = numer_minmax(m,lam)
            a,b = analytic_even(m,lam)
            assert abs(lo-a)<2e-9*max(1,a), (m,lam,lo,a)
            assert abs(hi-b)<2e-9*max(1,b)
            count += 2
    for lam in (.03,.1,.3,.8,1.,1.3169578969,1.9,2.5,4.):
        lo,hi = numer_minmax(3,lam,n=60001)
        a,b = analytic_three(lam)
        assert abs(lo-a)<1e-8*max(1,a),(lam,lo,a)
        assert abs(hi-b)<1e-8*max(1,b)
        count+=2
    for m in (2,3,4,5,6,7,9,13):
        target = 4*(1 if m%2==0 else math.cos(math.pi/(2*m))**2)
        ratios=[]
        for lam in (.1,.05,.025,.0125):
            lo,hi=numer_minmax(m,lam,n=16001)
            kappa=math.exp(2*lam)*hi/lo
            ratios.append(lam**2*kappa)
            count+=1
        assert abs(ratios[-1]-target)<0.2,(m,target,ratios)
        assert abs(ratios[-1]-target)<abs(ratios[0]-target) + 1e-6
        count+=2
    print(f'PASS: {count} numerical cross-checks; finite checks do not prove universal bounds.')
if __name__=='__main__': run()
