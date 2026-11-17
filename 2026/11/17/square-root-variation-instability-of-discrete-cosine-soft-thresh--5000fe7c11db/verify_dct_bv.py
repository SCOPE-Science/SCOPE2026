#!/usr/bin/env python3
"""Standalone numerical tests for the finite DCT variation result.
No external Python packages are required.
"""
import math
import random
from itertools import product


def sine(n, a, k):
    return math.sin(math.pi * k * a / n)


def kernel(n, mask):
    return [[2.0 / n * sum(sine(n,a,k)*sine(n,b,k) for k in range(1,n) if mask[k-1])
             for a in range(1,n)] for b in range(1,n)]


def projection_gain(mat):
    return max(sum(abs(mat[b][a]) for b in range(len(mat))) for a in range(len(mat)))


def dct(n, x):
    return [sum((math.sqrt(1/n) if k==0 else math.sqrt(2/n))
                *math.cos(math.pi*k*(i+.5)/n)*x[i] for i in range(n))
            for k in range(n)]


def idct(n, c):
    return [sum((math.sqrt(1/n) if k==0 else math.sqrt(2/n))
                *math.cos(math.pi*k*(i+.5)/n)*c[k] for k in range(n))
            for i in range(n)]


def soft(n,x,lam):
    c=dct(n,x)
    for k in range(1,n):c[k]=math.copysign(max(abs(c[k])-lam,0.),c[k])
    return idct(n,c)


def variation(x):return sum(abs(x[i+1]-x[i]) for i in range(len(x)-1))


def masks(n):
    return product((0,1),repeat=n-1)


def main():
    random.seed(42341)
    for n in range(2,10):
        best=0.
        for mask in masks(n):
            K=kernel(n,mask)
            gain=projection_gain(K)
            best=max(best,gain)
            for a in range(1,n):
                # Directly project a single step by DCT and compare first differences.
                step=[float(i>=a) for i in range(n)]
                cc=dct(n,step)
                projected=idct(n,[cc[k] if (k==0 or mask[k-1]) else 0. for k in range(n)])
                differences=[projected[j+1]-projected[j] for j in range(n-1)]
                assert max(abs(differences[j]-K[j][a-1]) for j in range(n-1))<1e-11
        lower=.5+(n-2)/(2*math.sqrt(3*n))
        assert best+1e-12>=lower and best<=math.sqrt(n-1)+1e-12
        print('EXACT_MASK_AND_DCT_STEP_IDENTITY_PASS',n,round(best,10))
    for n in (11,20,35,64,100):
        K=kernel(n,[random.randrange(2) for _ in range(n-1)])
        assert projection_gain(K)<=math.sqrt(n-1)+1e-10
        print('RANDOM_SINE_PROJECTION_UNIFORM_UPPER_PASS',n)
    for n in (4,6,9,15):
        for _ in range(40):
            mask=[random.randrange(2) for _ in range(n-1)]
            c=[random.uniform(-2,2)] + [2. if v else 0. for v in mask]
            x=idct(n,c)
            h=[random.uniform(-.01,.01) for _ in range(n)]
            u=soft(n,x,1.)
            v=soft(n,[x[i]+h[i] for i in range(n)],1.)
            assert variation([v[i]-u[i] for i in range(n)]) <= projection_gain(kernel(n,mask))*variation(h)+1e-9
        print('NONLINEAR_ACTIVE_SET_LOCAL_VARIATION_PASS',n)
    print('ALL_DCT_VARIATION_CHECKS_PASS')

if __name__=='__main__':main()
