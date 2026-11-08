"""Independent numerical and symbolic spot checks for the stated finite-cycle identities.
These tests support but do not replace the analytic global proof.
"""
import math
import numpy as np
import sympy as sp

x = sp.symbols('x')
f = x - 2*sp.sin(x)
assert sp.series(f, x, 0, 7).removeO() == -x + x**3/3 - x**5/60
assert sp.series((x/f)**2, x, 0, 5).removeO().expand().coeff(x,2) == sp.Rational(2,3)

rng=np.random.default_rng(8701)
checks=0
for n in [3,5,6,7,10,11]:
    lam=4.0 if n%2==0 else 2+2*math.cos(math.pi/n)
    h=2/lam
    ev=2-2*np.cos(2*np.pi*np.arange(n)/n)
    assert abs(max(ev)-lam)<1e-12
    for k in range(250):
        theta=rng.uniform(-math.pi,math.pi,n)
        z=np.roll(theta,-1)-theta
        q=np.sin(z)
        Kq=2*q-np.roll(q,1)-np.roll(q,-1)
        d=h*Kq
        v0=np.cos(z).sum()
        v1=np.cos(z+d).sum()
        if np.linalg.norm(Kq)>1e-7:
            assert v1 < v0 - 1e-12 or v1 < v0
        checks+=1

for n in [6,10,14]:
    signs=np.array([(-1.)**j for j in range(n)])
    u=.19
    for k in range(12000):
        z=np.pi+u*signs
        s=np.sin(z)
        Ks=2*s-np.roll(s,1)-np.roll(s,-1)
        dz=.5*Ks
        assert np.max(np.abs(dz-(-2*math.sin(u))*signs))<2e-13
        u=u-2*math.sin(u)
    assert abs(12000*u*u-1.5)<.02, (n,12000*u*u)

for n in [3,5,6,7,10,11]:
    lam=4.0 if n%2==0 else 2+2*math.cos(math.pi/n)
    h=2/lam
    for q in range(n):
        cos=math.cos(2*math.pi*q/n)
        if cos<-1e-12:
            mu=1+h*cos*(2-2*np.cos(2*np.pi*np.arange(1,n)/n))
            assert max(abs(mu)) < 1+1e-12
            if cos>-1+1e-12: assert max(abs(mu))<1-1e-10

print(f'VERIFY_OK exact_scalar_cubic=1 exact_reciprocal_coefficient=1 strict_descent_samples={checks} alternating_invariant_lines=3 critical_amplitude_limits=3 sink_spectra=6')
