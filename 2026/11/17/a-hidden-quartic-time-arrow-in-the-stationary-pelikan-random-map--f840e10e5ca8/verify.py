#!/usr/bin/env python3
"""Independent exact checks for mixed-moment directionality of the Pelikan map.
Python standard library only. All checks use rational arithmetic.
"""
from fractions import Fraction as F
from itertools import product

def dint_poly(coeff):
    return sum((c/F(i+1) for i,c in enumerate(coeff)), F(0))

def jmoment(a,b,m):
    # Integrate x^a (2^m*x mod 1)^b on each of the 2^m equal cells.
    N=2**m
    total=F(0)
    for j in range(N):
        # x=(j+v)/N, D^m x=v; binomial a expansion
        from math import comb
        total += sum(F(comb(a,k))*j**(a-k)*F(1,b+k+1) for k in range(a+1))/N**(a+1)
    return total

def depth_arrow(p,n):
    q=1-p
    r=q/p
    total=F(0)
    for k0 in range(n):
        mass=(1-r)*r**k0
        for choices in product((0,1),repeat=n):
            k=k0; l=0; w=mass
            for choice in choices:
                if choice==1:
                    w*=p
                    if k==0: l+=1
                    else: k-=1
                else:
                    w*=q
                    k+=1
            total+=w*F(1,2**(3*k0+k))* (F(1,2**l)-F(1,2**(3*l)))/120
    return total

def directly_integrated_one_step(p):
    # Use the invariant cell density a_j and integrate the exact map.
    # Since x<1/2 has D(x)=2*x, x>=1/2 has D(x)=2*x-1.
    # Delta integrand x^3 Dx - x (Dx)^3 = -6x^4+12x^3-6x^2+x
    # on upper half; on lower half = -6x^4.
    # Stationary fourth moment m4 = 16*(2p-1)/(5*(17*p-1)).
    a0=(2*p-1)/p
    m4=16*(2*p-1)/(5*(17*p-1))
    # Upper-half polynomial correction from (-6 x^4+12x^3-6x^2+x) - (-6 x^4).
    # integrate 12 x^3-6 x^2+x on x=1/2..1 ->  ?  12*15/64 - 2*7/8 + 3/8 = 45/16 - 7/4 + 3/8 = 23/16.
    # Actually derived direct full doubling difference: on lower half 2x^4-8x^4=-6x^4;
    # upper: x^3(2x-1)-x(2x-1)^3 = -6x^4+11x^3-6x^2+x
    # correction =11x^3-6x^2+x => 11*15/64/4? see integral below.
    from math import comb
    # compute exact correction integral upper branch algebraically
    poly=[F(0),F(1),F(-6),F(11)]
    correction=sum(c*(F(1)-F(1,2)**(i+1))/(i+1) for i,c in enumerate(poly))
    doubling=-6*m4+a0*correction
    halving=F(1,2)*m4-F(1,8)*m4
    return p*doubling+(1-p)*halving

def main():
    for m in range(8):
        h21=jmoment(2,1,m); h12=jmoment(1,2,m)
        h31=jmoment(3,1,m); h13=jmoment(1,3,m)
        assert h21==h12==F(1,6)+F(1,12*2**m)
        assert h31==F(1,8)+F(1,12*2**m)-F(1,120*2**(3*m))
        assert h13==F(1,8)+F(3,40*2**m)
        assert h31-h13==(F(1,2**m)-F(1,2**(3*m)))/120
    for p in [F(3,5),F(2,3),F(4,5),F(1)]:
        d1=depth_arrow(p,1)
        assert d1==(2*p-1)/320,(p,d1)
        print('lag1',str(p),str(d1),'direct',str(directly_integrated_one_step(p)))
        assert d1==directly_integrated_one_step(p)
        for n in range(1,8):
            d=depth_arrow(p,n)
            assert d>0,(p,n,d)
            if p==1:
                assert d==(F(1,2**n)-F(1,2**(3*n)))/120
            if n in (3,7):print('lag',n,'p',str(p),'delta',str(d))
    print('VERIFY_OK: 32 exact uniform-shift moments; 4 independent direct-map lag-one integrals; 28 finite path evaluations with strict positivity')
if __name__=='__main__':main()
