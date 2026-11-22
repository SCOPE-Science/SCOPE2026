"""Numerical consistency tests for burst-fed competing absorbing walls.

Run with: python checks/spectral_two_wall.py
Requirements: numpy, scipy.
These finite tests do not replace the analytic high-frequency proof.
"""
import numpy as np
from scipy.optimize import brentq


def transfers(s, diffusivity, width, source, mortality):
    z = np.sqrt(complex(mortality + s) / diffusivity)
    if abs(z) < 1e-13:
        return complex((width-source)/width), complex(source/width)
    denom = np.sinh(width*z)
    return np.sinh((width-source)*z)/denom, np.sinh(source*z)/denom


def cross_spectrum(omega, diffusivity, width, source, mortality):
    left, right = transfers(1j*omega, diffusivity, width, source, mortality)
    return left * np.conj(right)  # normalized by birth rate and E[K(K-1)]


def omega_from_imag_root(y, diffusivity, mortality):
    return 2*diffusivity*y*np.sqrt(y*y+mortality/diffusivity)


def independent_flux_laplace(s, diffusivity, width, source, mortality, n_modes=20000):
    # Absorbing-interval heat-kernel eigenfunction series.
    k = np.arange(1, n_modes+1, dtype=float)
    summand = (2*diffusivity*np.pi / width**2)*k*np.sin(np.pi*k*source/width)
    summand = summand / (s+mortality+diffusivity*(np.pi*k/width)**2)
    return summand.sum(), (((-1.)**(k+1))*summand).sum()


def test():
    cases = [(1.,3.,.9,.7),(.7,2.,.4,0.),(3.,10.,8.1,3.5)]
    count=0
    for D,L,x,mu in cases:
        sep=abs(L-2*x)
        for n in range(2,9):
            center=(n+.5)*np.pi/sep
            low=omega_from_imag_root((n+.25)*np.pi/sep,D,mu)
            high=omega_from_imag_root((n+.75)*np.pi/sep,D,mu)
            f=lambda w:cross_spectrum(w,D,L,x,mu).real
            assert f(low)*f(high)<0
            root=brentq(f,low,high,xtol=1e-12)
            approx=omega_from_imag_root(center,D,mu)
            assert abs(root-approx)/approx<0.002
            assert abs(f(root))<1e-9
            count+=3
        for w in [0.,.3,1.,10.,100.]:
            left,right=transfers(1j*w,D,L,L/2,mu)
            assert abs(left-right)<1e-10
            assert (left*np.conj(right)).real>0
            count+=2
    for mu in [0.,.5,4.]:
        D,L,x=1.3,4.,1.1
        left,right=transfers(0,D,L,x,mu)
        assert (left*right).real>0
        if mu==0:
            assert abs(left-(L-x)/L)<1e-12
            assert abs(right-x/L)<1e-12
        count+=1
    for s in [0j,1j,5j]:
        D,L,x,mu=1.3,4.,1.1,.5
        exact=transfers(s,D,L,x,mu)
        approx=independent_flux_laplace(s,D,L,x,mu)
        for a,b in zip(exact,approx):
            assert abs(a-b)<6e-5, (s,a,b)
            count+=1
    # Complex cross-spectrum obeys Hermitian symmetry under lag reversal.
    for w in [.1,1.,4.,13.]:
        S=cross_spectrum(w,1.5,3.2,.9,.5)
        assert abs(np.conj(S)-cross_spectrum(-w,1.5,3.2,.9,.5))<1e-12
        count+=1
    print('PASS:',count,'spectral, zero-ladder and independent heat-flux checks')


if __name__=='__main__':
    test()
