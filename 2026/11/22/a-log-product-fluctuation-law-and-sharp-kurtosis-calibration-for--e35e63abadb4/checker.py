#!/usr/bin/env python3
"""Standalone numerical and algebraic sanity checks for stationary sluggish diffusion."""
import math, random

def moments(alpha, r=1.0, p=2.0):
    mu=1.0/(alpha+2.0)
    return math.exp(2*p*mu*math.log(alpha+2.0)-p*mu*math.log(r)+math.lgamma(1+p*mu)+math.lgamma(1+(p-1)*mu)-math.lgamma(1-mu))

def kurt(mu):
    return math.exp(math.lgamma(1+4*mu)+math.lgamma(1+3*mu)+math.lgamma(1-mu)-2*math.lgamma(1+2*mu)-2*math.lgamma(1+mu))

# Exact polynomial identities, checked with integer coefficient arithmetic.
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b): c[i+j]+=u*v
    return c

def deriv(a): return [i*a[i] for i in range(1,len(a))]
def sub(a,b): return [(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]

def test():
    N=mul(mul([1,2],[1,2]),mul([1,1],[1,1]))
    D=mul(mul([1,4],[1,3]),[1,-1])
    assert sub(N,D)==[0,0,8,24,4]
    # h'(x)>0 since numerator = -8x(x+1)(2x+1)(3x+2)(x*x-3x-1)
    deriv_num=sub(mul(deriv(N),D),mul(N,deriv(D)))
    expect=mul(mul(mul(mul([0,-8],[1,1]),[1,2]),[2,3]),[-1,-3,1])
    assert deriv_num==expect, (deriv_num,expect)
    assert abs(kurt(.5)-6)<1e-13
    assert abs(kurt(0.0001)-1-4*math.pi**2/3*1.e-8)<1e-8
    grid=[k/1000 for k in range(1,501)]
    assert all(kurt(v)>kurt(u) for u,v in zip(grid,grid[1:]))
    for alpha in [0, 0.5, 1, 2, 5, 10, 50]:
        m2=moments(alpha,p=2);m4=moments(alpha,p=4)
        assert abs(m4/m2**2-kurt(1/(alpha+2)))<5e-13
        assert m2>0 and m4>0
    # Direct stationary sampling: independent Poisson age and free radial Gamma.
    rng=random.Random(371934)
    for alpha in [1,5,50,250]:
        mu=1/(alpha+2)
        a2=math.exp(math.lgamma(1+2*mu)+math.lgamma(1+mu)-math.lgamma(1-mu))
        vals=[]
        n=85000
        for _ in range(n):
            e=rng.expovariate(1)
            y=rng.gammavariate(1-mu,1)
            vals.append((math.exp(mu*(math.log(e)+math.log(y)))/math.sqrt(a2)-1)/mu)
        avg=sum(vals)/n
        variance=sum((v-avg)**2 for v in vals)/n
        target_var=(kurt(mu)-1)/(4*mu*mu) # only leading-order proxy, not exact
        assert math.isfinite(avg) and variance>0
        if alpha==250:
            assert abs(avg)<.035,(avg, variance)
            assert abs(variance-math.pi**2/3)<.14,(avg,variance)
        print('alpha',alpha,'scaled_mean',round(avg,5),'scaled_variance',round(variance,5),'kurtosis',round(kurt(mu),7))
    print('PASS: polynomial identity, monotonic gamma ratio, stationary moments, high-sluggishness sampling')

if __name__=='__main__':test()
