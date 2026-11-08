#!/usr/bin/env python3
"""Independent finite numerical checks of a weighted odd-cycle phase energy theorem.
Requires Python 3 and scipy for multistart unconstrained minimization.
All analytic/all-size claims are proved separately, not by this script.
"""
import math
import random
from scipy.optimize import brentq, minimize
PI=math.pi

def predicted(n,w):
    k=n-1
    if w<=1/k: return -k+w,0.0
    def force(d): return math.sin(d)-w*math.sin(k*d)
    # force negative near zero and positive near pi/k
    d=brentq(force,1e-9,PI/k-1e-9,xtol=1e-14)
    return -k*math.cos(d)+w*math.cos(k*d),d

def energy(theta,n,w):
    seq=[0.0]+list(theta)
    return sum(math.cos(seq[i+1]-seq[i]) for i in range(n-1))+w*math.cos(seq[0]-seq[-1])

rng=random.Random(63711)
checks=0
worst_err=0.0
for n in (3,5,7,9):
    for ratio in (0.27,0.7,0.999,1,1.001,1.4,3,8,20):
        w=ratio/(n-1)
        target,d=predicted(n,w)
        # Construct a phase vector using a common positive preferred-antiphase error.
        theta=[(i*(PI+d)) for i in range(1,n)]
        actual=energy(theta,n,w)
        if w>1/(n-1):
            assert abs(actual-target)<2e-8,(n,w,actual,target)
        else:
            theta=[i*PI for i in range(1,n)]
            actual=energy(theta,n,w)
            assert abs(actual-target)<2e-8,(n,w,actual,target)
        for _ in range(30):
            guess=[rng.uniform(-PI,PI) for i in range(1,n)]
            fit=minimize(energy,guess,args=(n,w),method='L-BFGS-B',
                         options={'maxiter':2000,'ftol':1e-12})
            # Every competing configuration must have energy >= known minimizer.
            err=target-fit.fun
            worst_err=max(worst_err,err)
            assert err<3e-7,(n,w,target,fit.fun,fit.message)
            checks+=1
print(f'VERIFY_OK odd_sizes=4 weight_cases=36 multistart_cases={checks} worst_negative_gap={worst_err:.3g}')
