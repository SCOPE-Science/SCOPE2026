#!/usr/bin/env python3
"""Supplementary exact Fourier-factor checks for two-speed mobile response inversion.

This is a reproducibility aid, not a proof of the infinite-dimensional theorem.
Uses only the Python 3 standard library.
"""
import cmath
import random


def response(w, alpha, beta, mix):
    # Normalized mixture of two one-sided exponential response densities.
    return mix * alpha / (alpha + 1j * w) + (1-mix) * beta / (beta + 1j * w)


def field(w, width):
    # Characteristic transform of a centered Laplace spatial source density.
    return 1/(1+(width*w)**2)


def reading(w, speed, width, alpha, beta, mix):
    return field(w,width)*response(speed*w, alpha,beta,mix)


def recovered_H(w, vfast, vslow, width, alpha, beta, mix, n):
    a=vslow/vfast
    p=1.+0j
    for j in range(n):
        x=(a**j)*w/vfast
        p*=reading(x,vfast,width,alpha,beta,mix)/reading(x,vslow,width,alpha,beta,mix)
    return p


def assert_close(a,b,tol=1e-10):
    assert abs(a-b) < tol*(1+abs(b)), (a,b)


def check():
    rng=random.Random(20241117)
    checks=0
    for _ in range(1200):
        vfast=rng.uniform(1.5,7.0)
        vslow=rng.uniform(.3,.75*vfast)
        width=rng.uniform(.1,1.8)
        alpha=rng.uniform(.2,2.0)
        beta=rng.uniform(2.2,4.5)
        mix=rng.uniform(.15,.9)
        w=rng.uniform(-6,6)
        a=vslow/vfast
        n=160
        htrue=response(w,alpha,beta,mix)
        hrec=recovered_H(w,vfast,vslow,width,alpha,beta,mix,n)
        assert_close(hrec, htrue/response((a**n)*w,alpha,beta,mix))
        assert_close(hrec,htrue,tol=2e-10)
        crec=reading(w/vfast,vfast,width,alpha,beta,mix)/hrec
        assert_close(crec,field(w/vfast,width),tol=2e-10)
        checks+=3
        # Means and variances of the normalized measured spatial profiles.
        mean_t=mix/alpha+(1-mix)/beta
        second_t=2*mix/(alpha**2)+2*(1-mix)/(beta**2)
        var_t=second_t-mean_t**2
        mean1=vfast*mean_t
        mean2=vslow*mean_t
        var1=2*width**2+vfast**2*var_t
        var2=2*width**2+vslow**2*var_t
        assert_close((mean1-mean2)/(vfast-vslow),mean_t)
        assert_close((var1-var2)/(vfast**2-vslow**2),var_t)
        assert_close((vfast*mean2-vslow*mean1)/(vfast-vslow),0)
        assert_close((vfast**2*var2-vslow**2*var1)/(vfast**2-vslow**2),2*width**2)
        checks+=4
    # Sharp one-speed counterexample: two distinct causal kernels / spatial fields
    # give precisely identical observations by commutativity of convolution.
    for _ in range(2600):
        v=rng.uniform(.2,5)
        w=rng.uniform(-11,11)
        width=rng.uniform(.1,2)
        h1=response(v*w,1.0,3.0,.7)
        h2=response(v*w,.6,4.0,.45)
        y1=field(w,width)*h2*h1
        y2=field(w,width)*h1*h2
        assert_close(y1,y2)
        checks+=1
    # Confirm the frequency normalization and the common mass of two scans.
    for _ in range(1800):
        v=rng.uniform(.1,9)
        width=rng.uniform(.1,3)
        assert_close(reading(0,v,width,1.2,4,.4),1)
        checks+=1
    return checks

if __name__=='__main__':
    print('SUPPLEMENTARY_CHECKS_PASSED',check())
