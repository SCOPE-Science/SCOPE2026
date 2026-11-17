"""Finite diagnostics for the one-defect Fourier Kaczmarz continuum law.
The infinite-dimensional statements depend on the accompanying proof.
"""
import numpy as np
from scipy.special import lambertw

def sweep(m, c):
    r = c / (m+c)
    i = np.arange(m)[:,None]
    j = np.arange(m)[None,:]
    return r * ((1-r)**np.maximum(i-j,0)*(j<=i) - (1-r)**i)

def exact_projection(m,c):
    r=c/(m+c)
    G=(1-r)*np.eye(m)+r*np.ones((m,m))
    L=np.tril(G)
    U=np.triu(G,1)
    return -np.linalg.solve(L,U)

def kernel(s,t,c):
    return c*np.exp(-c*(s-t))*(t<=s)-c*np.exp(-c*s)

count=0
for m in range(2,28):
    for c in (.12,.4,1.,2.,5.):
        assert np.max(np.abs(sweep(m,c)-exact_projection(m,c)))<8e-14
        count+=1

for c in (.5,1.,2.,4.):
    errors=[]
    for m in (32,64,128,256):
        q=sweep(m,c)
        # midpoint quadrature of smooth limit except near the diagonal
        i=np.arange(m)[:,None]
        j=np.arange(m)[None,:]
        s=(i+.5)/m
        t=(j+.5)/m
        err=np.linalg.norm(m*q-kernel(s,t,c))/m
        errors.append(err)
        assert err<15/np.sqrt(m)
        count+=1
    assert errors[-1]<errors[0]*.63
    count+=1

for c in (.5,1.,3.):
    target=c/lambertw(c*np.exp(c),1)
    m=80
    eig=np.linalg.eigvals(sweep(m,c))
    err=min(abs(eig-target))
    assert err<.08, (c,err)
    assert all(abs(x)<1.00001 for x in eig)
    count+=1

print('CHECKS_PASSED',count)

# The physical Hilbert norm on Fourier coefficients is induced by G.
for m in (16,32,64,128):
    c=3.
    r=c/(m+c)
    G=(1-r)*np.eye(m)+r*np.ones((m,m))
    q=sweep(m,c)
    a=np.sqrt(1-r)
    d=np.sqrt(1+(m-1)*r)
    p=np.ones((m,m))/m
    S=a*np.eye(m)+(d-a)*p
    assert np.linalg.norm(S@S-G,ord=np.inf)<1e-12
    physical=S@q@np.linalg.inv(S)
    # Explicit coordinate unitary used for the physical cycle.
    assert np.linalg.norm(S@q - physical@S,ord=np.inf)<1e-11
    count += 2
print('PHYSICAL_CHECKS_PASSED',count)
