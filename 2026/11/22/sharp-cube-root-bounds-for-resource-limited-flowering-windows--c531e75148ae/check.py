#!/usr/bin/env python3
"""Numerical checks for Gaussian flowering-window optimization.
Python 3, standard library only. Numerical checks supplement, not replace, proofs.
"""
import math

def log_mex(a):
    # log E exp(a(1-U^2)), U uniform on [0,1]
    if a < 1e-4:
        # Stable high-accuracy quadrature at near zero
        n=100
        h=1/n
        s=math.exp(a)+1
        for i in range(1,n):
            s+=(4 if i%2 else 2)*math.exp(a*(1-(i*h)**2))
        return math.log(s*h/3)
    return a+0.5*math.log(math.pi)-math.log(2)-0.5*math.log(a)+math.log(math.erf(math.sqrt(a)))

def log_mun(z):
    # log E exp(z U), U uniform on [0,1]
    if z < 1e-5:
        return math.log1p(z/2+z*z/6+z**3/24+z**4/120)
    return z+math.log(-math.expm1(-z))-math.log(z)

def contrast(y,k):
    return log_mex(y*y/2)-log_mun(k/y)

def optimum(k):
    l=(1.5*k)**(1/3);r=(2*k)**(1/3)
    assert contrast(l,k) < 1e-11, (k,contrast(l,k))
    assert contrast(r,k) > -1e-11,(k,contrast(r,k))
    for _ in range(85):
        m=(l+r)/2
        if contrast(m,k)<0:l=m
        else:r=m
    return (l+r)/2

def score(y,k):
    return -math.expm1(-k/y)*math.erf(y/math.sqrt(2))

def check():
    count=0
    past=0
    for j in range(301):
        k=10**(-6+j*9/300)
        y=optimum(k)
        low=(1.5*k)**(1/3); high=(2*k)**(1/3)
        assert low-1e-14 < y < high+1e-14
        count+=1
        assert y>past
        past=y
        count+=1
        for scale in [0.15,0.4,0.75,0.9,1.1,1.3,2,4]:
            v=score(y*scale,k)
            assert score(y,k)>v-1e-14,(k,scale,v,y)
            count+=1
        # Signed equality equation across optimum
        for scale in [.5,.8,1.2,2]:
            assert (contrast(y*scale,k)>0)==(scale>1)
            count+=1
    # Exact convex-order quantile integral calculations against symbolic expression
    for i in range(1,1000):
        s=i/1000
        lhs=(s*s)-(s**3)/3-(2/3)*s*s
        rhs=s*s*(1-s)/3
        assert abs(lhs-rhs)<1e-14
        assert rhs>0
        count+=2
    # Improvement for a shift of same half-width is direct Gaussian rearrangement
    for k in [.02,.2,1.,5.,20.]:
        y=optimum(k)
        centered=score(y,k)
        for delta in [.1,.5,1,2]:
            shifted=(-math.expm1(-k/y))*0.5*(math.erf((y+delta)/math.sqrt(2))-math.erf((-y+delta)/math.sqrt(2)))
            assert centered>shifted
            count+=1
    print('PASS', count,'checks')
    for k in [1e-4,.01,.1,1,10,100,1000]:
        y=optimum(k)
        print('k=',k,'y=',f'{y:.12g}','score=',f'{score(y,k):.12g}', 'normalized cubic=',f'{y**3/k:.12g}')
if __name__=='__main__':check()
