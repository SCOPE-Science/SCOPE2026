"""Exact algebra and numerical checks for alternating Laplace-kernel sampling.

Needs Python 3, sympy and numpy. Run: python verify_spectrum.py
"""
import numpy as np
import sympy as sp

r, X, m, p = sp.symbols('r X m p', positive=True, real=True)
u = 1+r*r
D = u*u-4*r*r*X
T = (1-r*r)**2 / D**2 * ((p*p+m*m)*(u*u+4*r*r*X)+4*(p*p-m*m)*u*r*X)
Delta = (m*p)**2*(1-r*r)**4/D**2
k = (1-r*r)/u
H = r**6+3*r**5+3*r**4+(6-4*X)*r**3+3*r*r+3*r+1
q = p*p-m*m
expected = [
 -4*m*m*r*X*(q*u*u*(1+r+r*r)+4*m*m*r*(u*u-r*r*X)),
 -4*p*p*r*X*(q*H+4*m*m*r*(u*u-r*r*X)),
]
for z, rhs in zip((m*m*k*k, p*p*k*k), expected):
    actual = (z*z-T*z+Delta)*D*D*u**4/(1-r*r)**4
    assert sp.factor(actual-rhs) == 0
print('EXACT_IDENTITIES_OK')

for alpha in (.2,.8,1.7,3.):
    rr = np.exp(-alpha)
    for delta in (0.,.03,.19,.43,.49):
        a = np.sinh(alpha*(1-delta))/np.sinh(alpha)
        b = np.sinh(alpha*delta)/np.sinh(alpha)
        pp = a+b
        mm = a-b
        M = np.array([[a,b],[b,a]])
        values = []
        for theta in np.linspace(0,np.pi,301):
            denominator = 1-2*rr*rr*np.cos(theta)+rr**4
            C = (1-rr*rr)/denominator * np.array([
                [1+rr*rr, rr*(1+np.exp(-1j*theta))],
                [rr*(1+np.exp(1j*theta)), 1+rr*rr]])
            values.append(np.linalg.svd(M@C,compute_uv=False)**2)
        values = np.array(values)
        expected_edges = [
            mm**2*np.tanh(alpha/2)**2,
            mm**2*np.tanh(alpha)**2,
            pp**2*np.tanh(alpha)**2,
            pp**2/np.tanh(alpha/2)**2,
        ]
        observed_edges = [
            values[:,1].min(), values[:,1].max(),
            values[:,0].min(), values[:,0].max(),
        ]
        assert np.allclose(expected_edges, observed_edges, rtol=1e-9, atol=1e-10)
print('BLOCH_BAND_EDGES_OK parameter_pairs=20 frequencies_per_pair=301')
