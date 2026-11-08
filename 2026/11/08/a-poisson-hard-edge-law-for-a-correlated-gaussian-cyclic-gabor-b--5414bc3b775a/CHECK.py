"""Reproducibility checks for cyclic Gaussian Gabor lower-frame law.

Python 3 standard library only. The proof of the distributional limit is
analytical; these are finite numerical consistency tests, not certification.
"""
import cmath
import math
import random

R = random.Random(20261106)
checks = 0

def cn(scale=1.0):
    # E |cn(scale)|^2 = scale^2.
    return scale * complex(R.gauss(0, 1), R.gauss(0, 1)) / math.sqrt(2)

def lam_min(a, b):
    # Smallest eigenvalue of [a,b][a,b]^* for columns in C^2.
    t = sum(abs(v)**2 for v in a) + sum(abs(v)**2 for v in b)
    det = abs(a[0]*b[1]-a[1]*b[0])**2
    return (t - math.sqrt(max(t*t-4*det, 0.0)))/2

def blocks(g, p):
    a = [(math.sqrt(p)*g[j],math.sqrt(p)*g[j+p]) for j in range(p)]
    return [(a[j],a[j-1][::-1] if j == 0 else a[j-1]) for j in range(p)]

# Reconstruct each entry of the original 2p x 2p frame operator
# and compare with the asserted p blocks of order 2.
for p in (3,4,5,7,9):
    n=2*p
    for rep in range(15):
        g=[cn(1/math.sqrt(n)) for _ in range(n)]
        S=[[0j]*n for _ in range(n)]
        for k in (0,1):
            for ell in range(p):
                col=[cmath.exp(2j*math.pi*(2*ell)*i/n)*g[(i-k)%n] for i in range(n)]
                for i in range(n):
                    for j in range(n):
                        S[i][j] += col[i]*col[j].conjugate()
        B=blocks(g,p)
        for i in range(n):
            a=i%p
            ia=0 if i<p else 1
            for j in range(n):
                b=j%p
                jb=0 if j<p else 1
                expect=sum(x[ia]*x[jb].conjugate() for x in B[a]) if a==b else 0j
                if abs(S[i][j]-expect)>4e-11:
                    raise AssertionError(('block identity',p,rep,i,j,S[i][j],expect))
                checks+=1
        for b in B:
            lam=lam_min(*b)
            if lam<-1e-11:
                raise AssertionError('negative block eigenvalue')
            checks+=1

# Independent Monte Carlo check of E|g|^2 normalization, the one-block
# survival e^{-4x}, and p-minimum survival e^{-4t}.
for p in (60,120,240):
    samples=4000
    one=[0,0,0]
    all_=[0,0,0]
    points=(0.10,0.25,0.50)
    total=0.0
    for rep in range(samples):
        a=[(cn(1/math.sqrt(2)),cn(1/math.sqrt(2))) for _ in range(p)]
        vals=[lam_min(a[j],a[j-1][::-1] if j==0 else a[j-1]) for j in range(p)]
        x= p*min(vals)
        total += x
        for h,t in enumerate(points):
            all_[h]+= x>t
            one[h]+= vals[1]>t/p
    for h,t in enumerate(points):
        observed=all_[h]/samples
        expected=math.exp(-4*t)
        if abs(observed-expected) > 0.075:
            raise AssertionError(('Poisson limit diagnostic',p,t,observed,expected))
        checks+=1
        expected_single=math.exp(-4*t/p)
        if abs(one[h]/samples-expected_single)>0.055:
            raise AssertionError('single-block diagnostic')
        checks+=1
    if abs(total/samples-0.25)>0.065:
        raise AssertionError(('first moment diagnostic',p,total/samples))
    checks+=1

print('GAUSSIAN_GABOR_HARD_EDGE_CHECKS_PASSED', checks)
