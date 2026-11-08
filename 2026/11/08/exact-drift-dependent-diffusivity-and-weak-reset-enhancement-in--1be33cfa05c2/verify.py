#!/usr/bin/env python3
"""Check formulas for drift and dispersion of instantaneously rectified Brownian ratchet.
No data files or nonstandard resources are required; uses Python standard library.
"""
import math, random


def formula(ell, delta):
    u = math.exp(-delta*ell)
    w = math.exp(-(1-delta)*ell)
    q = math.exp(-ell)
    h = -math.expm1(-ell)
    m = (u-w)/(2*h)
    m_prime = ((-delta*u+(1-delta)*w)*h - (u-w)*q)/(2*h*h)
    e2 = (u+w)*(1+q)/(2*h*h)
    return m, e2, (ell*ell*e2 + ell**3*m*m_prime)/2


def direct_sums(ell, delta, cutoff=1800):
    # Independently sum the bilateral-Laplace tails of the cycle displacement.
    ppos = pneg = e2 = ltime = 0.0
    for k in range(cutoff):
        zpos = k + delta
        zneg = k + 1-delta
        rpos = math.exp(-ell*zpos)/2
        rneg = math.exp(-ell*zneg)/2
        ppos += rpos
        pneg += rneg
        e2 += (2*k+1)*(rpos+rneg)
        # E[(r E) 1_{B_E > a}] = tail*(1+lambda*a/2).
        ltime += rpos*(1+ell*zpos/2)-rneg*(1+ell*zneg/2)
        if k > 50 and max(rpos,rneg) < 1e-18:
            break
    m = ppos-pneg
    # E[J rE]/L = ltime, E[(J/L - ell^2*m*(rE)/ell^2 )^2]
    # rE has second moment 2, and vE/L = m*(rE).
    varreward = e2-2*m*ltime+2*m*m
    return m,e2,ell*ell*varreward/2


def approx(ell, delta):
    return 1+ell*ell*(1/24+0.5*(delta-0.5)**2)


def main():
    c=0
    for ell in [0.02,0.15,0.5,1.0,2.5,4.0,8.0,15.0]:
        for delta in [0.03,0.2,0.375,0.5,0.65,0.97]:
            m,e2,diff = formula(ell,delta)
            md,e2d,diffd = direct_sums(ell,delta)
            assert abs(m-md) < 2e-12, (ell,delta,m,md)
            assert abs(e2-e2d)<2e-10*max(e2,1.0), (ell,delta,e2,e2d)
            assert abs(diff-diffd) < 2e-10*max(diff,1), (ell,delta,diff,diffd)
            assert diff>0
            assert abs(formula(ell,1-delta)[2]-diff)<1e-11
            c+=5
    for delta in [0.03,0.2,0.5,0.75,0.97]:
        # Convergence to the analytic weak-resetting coefficient.
        ell=.004
        coeff=(formula(ell,delta)[2]-1)/ell**2
        target=1/24+0.5*(delta-0.5)**2
        assert abs(coeff-target)<1e-5,(delta, coeff,target)
        c+=1
    for delta in [0.05,0.2,0.375,0.5,0.8,0.95]:
        assert formula(0.035,delta)[2]>1
        assert formula(1000.0,delta)[2]<1e-5
        c+=2
    for ell in [0.2,2,5,10]:
        _,_,v=formula(ell,.5)
        y=ell/2
        d_sym=y*y*(math.cosh(y)/math.sinh(y))/math.sinh(y)
        assert abs(v-d_sym)<1e-11
        c+=1
    # Cross-check at an asymmetric point without using the derivative formula.
    assert abs(formula(3,.25)[2]-direct_sums(3,.25)[2])<1e-12
    c+=1
    print(f'{c} assertions passed; independent cycle-tail sums, covariance/time correction, symmetry, weak-rate expansion and high-rate limits')
    for ell,delta in [(1,.25),(3,.25),(8,.25),(3,.5)]:
        print('ell=%g delta=%.2f: E[J]/L=%.12f, D_eff/D=%.12f'%((ell,delta)+ (formula(ell,delta)[0],formula(ell,delta)[2])))

if __name__=='__main__':
    main()
