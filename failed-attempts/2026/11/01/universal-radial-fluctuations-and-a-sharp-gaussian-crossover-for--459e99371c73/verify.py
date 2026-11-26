#!/usr/bin/env python3
"""Reproducibility checks for radial-universal zonogon deficit and area crossover.
Standalone: Python 3 standard library only. Analytical proofs are in RESULT.md.
"""
import math, random, statistics
PI=math.pi
MU=2/PI

def zonogon_stats(pairs):
    # Unoriented generators (theta mod pi). Sorting makes all pairwise sines positive.
    pairs=sorted(pairs, key=lambda x:x[0])
    a=0.; c=0.; s=0.; length=0.
    for t,r in pairs:
        a+=r*(math.sin(t)*c-math.cos(t)*s)
        c+=r*math.cos(t); s+=r*math.sin(t); length+=r
    p=2*length
    deficit=(length*length/PI-a)/len(pairs)
    return a,p,deficit

def brute_area(pairs):
    return sum(r*s*abs(math.sin(t-u)) for j,(t,r) in enumerate(pairs)
               for u,s in pairs[j+1:])

def exact_deficit_variance(n,q,m4):
    return (m4-q*q)/(PI*PI*n) + (1-1/n)*q*q*(PI*PI-8)/(4*PI*PI)

def laplace_limit(t):
    # For S_1=(2/pi)*sum E_k/(4k^2-1).
    x=2*t/PI-1
    if abs(x)<1e-12:
        return 2/PI
    if x>0:
        z=math.sqrt(x); return z/math.sinh(PI*z/2)
    z=math.sqrt(-x); return z/math.sin(PI*z/2)

def check():
    rng=random.Random(27182818)
    # Geometric area formula independent of Fourier probabilistic derivation.
    for n in (2,3,4,9):
        for _ in range(30):
            pairs=[(PI*rng.random(), .2+1.8*rng.random()) for i in range(n)]
            a,p,d=zonogon_stats(pairs)
            assert abs(a-brute_area(pairs)) <1e-12*(1+a)
            assert d>-1e-12
            # Deterministic Fourier identity, with rigorous tail bound.
            kmax=1000
            fs=sum((2/PI)/(4*k*k-1)*abs(sum(r*complex(math.cos(2*k*t),math.sin(2*k*t)) for t,r in pairs))**2/n for k in range(1,kmax+1))
            err=d-fs
            tail_bound=sum(r for _,r in pairs)**2/(PI*n*(2*kmax+1))
            assert -1e-8 <= err <= tail_bound+1e-8, (n,err,tail_bound)
    # Exact infinite sums and Euler hyperbolic-sine transform.
    for t in (0., .25, 1., PI/2, 2.5, 5.):
        prod=1.
        for k in range(1,3000): prod*=1/(1+(2*t/PI)/(4*k*k-1))
        assert abs(prod-laplace_limit(t))<3e-4, (t,prod,laplace_limit(t))
    assert abs(sum(1/(4*k*k-1) for k in range(1,30000))-.5)<1e-5
    assert abs(sum(1/(4*k*k-1)**2 for k in range(1,30000))-(PI*PI-8)/16)<1e-9
    # Empirical finite-n mean/variance with a nontrivial two-point length law.
    for n,sigma,rep in ((3,.3,9000),(8,.4,9000),(30,.25,9000)):
        vals=[]; areas=[]; perimeters=[]
        for _ in range(rep):
            pairs=[(PI*rng.random(), 1+sigma*(1 if rng.getrandbits(1) else -1)) for i in range(n)]
            a,p,d=zonogon_stats(pairs)
            areas.append(a); perimeters.append(p); vals.append(d)
        mean=sum(vals)/rep; var=statistics.variance(vals)
        q=1+sigma*sigma
        m4=1+6*sigma*sigma+sigma**4
        e_mean=q/PI; e_var=exact_deficit_variance(n,q,m4)
        # conservative Monte Carlo 8-sigma margins (bounded model)
        assert abs(mean-e_mean)<.065, (n,mean,e_mean)
        assert abs(var-e_var)<.085, (n,var,e_var)
        expected_area_var=(n*(n-1)/2)*(q*q/2-4/PI**2) + n*(n-1)*(n-2)*(4/PI**2)*sigma*sigma
        measured_area_var=statistics.variance(areas)
        assert abs(measured_area_var-expected_area_var)<max(3.,.12*expected_area_var), (n,measured_area_var,expected_area_var)
        measured_cov=statistics.covariance(vals,perimeters)
        expected_cov=4*sigma*sigma/PI
        assert abs(measured_cov-expected_cov)<.09, (n,measured_cov,expected_cov)
    # Critical scaling: both area and perimeter have fluctuation of order n.
    for tau in (0., .8, 2.):
        n=700; rep=5000; sigma=tau/math.sqrt(n)
        Bs=[]; Ds=[]; Gs=[]
        for _ in range(rep):
            xis=[1 if rng.getrandbits(1) else -1 for _ in range(n)]
            pairs=[(PI*rng.random(),1+sigma*x) for x in xis]
            a,p,d=zonogon_stats(pairs)
            Bs.append((a-n*(n-1)/PI)/n)
            Ds.append(d)
            Gs.append(sum(xis)/math.sqrt(n))
            # Exact relation (not an asymptotic approximation).
            rhs=1/PI-d+2*tau/PI*Gs[-1]+sigma*sigma*Gs[-1]**2/PI
            assert abs(Bs[-1]-rhs)<5e-9
        vB=statistics.variance(Bs)
        expected=(PI*PI-8)/(4*PI*PI)+4*tau*tau/(PI*PI)
        assert abs(vB-expected)<.13, (tau,vB,expected)
        assert abs(statistics.mean(Ds)-1/PI)<.04
        print('critical_tau=',tau,'measured_area_var=',round(vB,5),'limit_var=',round(expected,5))
    print('ALL_RADIAL_UNIVERSALITY_AND_CROSSOVER_CHECKS_PASSED')
if __name__=='__main__': check()
