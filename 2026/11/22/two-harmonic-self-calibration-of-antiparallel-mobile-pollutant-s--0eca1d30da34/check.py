#!/usr/bin/env python3
"""Numerical checks for two-harmonic bidirectional first-order scan calibration.

No field data are used. Synthetic periodic concentration profiles are used only to
check analytic reconstruction; numerical experiments are not proofs.
"""
import math
import numpy as np
from scipy.optimize import brentq

TWOPI = 2*math.pi

def wrap(a):
    return (a+math.pi) % (2*math.pi)-math.pi

def solve(R1, R2):
    r1 = R1/abs(R1)
    r2 = R2/abs(R2)
    z = r2/(r1*r1)
    theta = math.atan2(z.imag,z.real)
    if not (-math.pi < theta < 0):
        raise ValueError('Not a positive finite first-order response')
    if abs(abs(R1)-abs(R2)) > 1e-9*max(abs(R1),abs(R2)):
        raise ValueError('Inconsistent gain magnitudes')
    q = -math.tan(theta/2)
    ell = brentq(lambda s: 2*s**3/(1+3*s*s)-q,1e-12, max(5,4*q+5), xtol=1e-12)
    delta = (2*math.atan(ell)-math.atan2(r1.imag,r1.real)) % TWOPI
    return ell, delta, abs(R1), z

def test():
    rng=np.random.default_rng(20261121)
    N=256
    x=TWOPI*np.arange(N)/N
    worst_ell=0.0
    worst_shift=0.0
    worst_gain=0.0
    for j in range(2000):
        ell=10**rng.uniform(-1.5,1.5)
        delta=rng.uniform(0,TWOPI)
        gain1=10**rng.uniform(-1,1)
        gain2=10**rng.uniform(-1,1)
        offset1=rng.uniform(-10,10)
        offset2=rng.uniform(-10,10)
        amplitudes=rng.uniform(.1,1.5,6)
        phases=rng.uniform(-math.pi,math.pi,6)
        c=15+sum(a*np.cos(k*x+t) for k,(a,t) in enumerate(zip(amplitudes,phases),start=1))
        C=np.fft.rfft(c)/N
        omega=np.arange(len(C))
        plus=np.fft.irfft((C/(1+1j*omega*ell))*N,n=N)
        minus=np.fft.irfft((C/(1-1j*omega*ell))*N *np.exp(-1j*omega*delta),n=N)
        Yp=np.fft.rfft(offset1+gain1*plus)/N
        Ym=np.fft.rfft(offset2+gain2*minus)/N
        R1=Ym[1]/Yp[1]
        R2=Ym[2]/Yp[2]
        recovered_ell,recovered_delta,rho,z=solve(R1,R2)
        worst_ell=max(worst_ell,abs(ell-recovered_ell)/ell)
        worst_shift=max(worst_shift,abs(wrap(delta-recovered_delta)))
        worst_gain=max(worst_gain,abs(rho-gain2/gain1)/(gain2/gain1))
        assert abs(ell-recovered_ell)/ell<1e-8,(j,ell,recovered_ell)
        assert abs(wrap(delta-recovered_delta))<1e-8,(j,delta,recovered_delta)
        assert abs(rho-gain2/gain1)/(gain2/gain1)<1e-8
        # All available higher harmonics obey the independently reconstructed transfer law.
        for n in range(3,7):
            actual=Ym[n]/Yp[n]
            pred=rho*np.exp(-1j*n*recovered_delta)*(1+1j*n*recovered_ell)/(1-1j*n*recovered_ell)
            assert abs(actual-pred)/abs(pred)<1e-8
    # Exact algebraic witness ell=1/2, independent of position and gain.
    ell=.5; delta=.37; rho=1.7
    R=lambda n:rho*np.exp(-1j*n*delta)*(1+1j*n*ell)/(1-1j*n*ell)
    ell0,delta0,rho0,z=solve(R(1),R(2))
    assert abs(z-(24-7j)/25)<1e-13
    assert abs(ell0-.5)<1e-12
    assert abs(wrap(delta0-delta))<1e-12
    assert abs(rho0-rho)<1e-12
    # Mathematical inequalities and asymptotic signs (not substitutes for proofs).
    xx=np.geomspace(1e-4,1e4,3000)
    theta=2*np.arctan(2*xx)-4*np.arctan(xx)
    assert np.all(np.diff(theta)<0)
    assert np.all((theta<0)&(theta>-math.pi))
    deriv=4/(1+4*xx**2)-4/(1+xx**2)
    factor=-12*xx**2/((1+xx**2)*(1+4*xx**2))
    assert np.max(np.abs(deriv-factor))<1e-12
    assert abs((2*math.atan(.001*2)-4*math.atan(.001))/(-4*1e-9)-1)<3e-6
    print('PASS: 2,000 distinct profiles with relative gains, offsets, phase shifts and 2,000 x 4 higher-harmonic tests; exact witness and asymptotics')
    print('max rel ell err:',worst_ell,'max wrapped delta err:',worst_shift,'max gain error:',worst_gain)
    print('exact invariant ell=1/2:',z)

if __name__=='__main__':
    test()
