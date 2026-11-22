#!/usr/bin/env python3
"""Numerical checks of the exact analytic three-step coefficients at several fractional orders."""
import math

def j(s, a):
    return ((2*s-1)*(s**(1-a)-(s-1)**(1-a))/(1-a)
            -2*(s**(2-a)-(s-1)**(2-a))/(2-a))

def energy(a, eps):
    sig=1-a/2
    A=a/((1-a)*(2-a))
    B=j(1+sig,a)
    q=-B/(2*A)
    s2=1+sig*eps
    s3=1+eps+sig
    x=s3-1
    y=s3-(1+eps)
    I0=(x**(1-a)-y**(1-a))/(1-a)
    I1=(2*x-eps)*I0-2*(x**(2-a)-y**(2-a))/(2-a)
    W22=sig**(1-a)*eps**(-a)/(1-a)+j(s2,a)/(eps*(1+eps))
    W32=j(s3,a)/(eps*(1+eps))+I0/eps-I1/(eps*(1+eps))
    W33=sig**(1-a)/(1-a)+I1/(1+eps)
    return (q*q*W22+q*W32+W33), -B*B/(4*A)

def main():
    for a in [.2,.5,.8]:
        previous=None
        for eps in [1e-4,1e-5,1e-6]:
            E,C=energy(a,eps)
            err=abs(eps*E-C)
            print('alpha=',a,'epsilon=',eps,'scaled=',eps*E,
                  'limit=',C,'absolute_error=',err)
            assert C<0
            if previous is not None: assert err<previous
            previous=err
    print('ALL GENERAL-ORDER CHECKS PASSED')

if __name__=='__main__':
    main()
