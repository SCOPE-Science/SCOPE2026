"""Supplementary numerical checks for one-particle transport on friendship graphs.

Usage: python check_transport.py
Requirements: Python 3, numpy, scipy. Analytic proof is in RESULT.md.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize_scalar, brentq

def matrix(m):
    a = np.zeros((2*m+1, 2*m+1))
    for j in range(m):
        u,v = 2*j+1,2*j+2
        a[u,v]=a[v,u]=1.
        a[0,u]=a[u,0]=1.
        a[0,v]=a[v,0]=1.
    return a

def amplitude(m, t):
    s = math.sqrt(8*m+1)
    f = np.exp(-0.5j*t)*(np.cos(0.5*s*t)-1j*np.sin(0.5*s*t)/s)
    return ((m-1)*np.exp(-1j*t)+f-m*np.exp(1j*t))/(2*m)

def constant(alpha):
    f = lambda u: math.cos(alpha+u/2)/math.sqrt(2)-u*u/8
    root = brentq(lambda u: u + math.sqrt(2)*math.sin(alpha+u/2), -math.sqrt(2),math.sqrt(2))
    return 1-f(root)

checks=0
for m in range(2,13):
    a=matrix(m)
    for t in np.linspace(0,5,13):
        actual=expm(-1j*t*a)[1,2]
        assert abs(actual-amplitude(m,t))<3e-13,(m,t,actual,amplitude(m,t))
        checks+=1

cgen=1-1/math.sqrt(2)
good=constant(math.pi/4)
bad=constant(3*math.pi/4)
assert 0.29<cgen<0.30 and 0.41<good<0.43 and 1.30<bad<1.32
checks+=3

# On triangular m, all graph eigenvalues are integral and the walk is 2*pi-periodic.
# Compare finite-m supremum with the theoretical three subsequential constants.
for k in [9,10,11,12,21,22,23,24,61,62,63,64]:
    m=k*(k+1)//2
    s=2*k+1
    ts=np.linspace(0,2*math.pi,20000)
    ps=np.abs(amplitude(m,ts))**2
    center=ts[np.argmax(ps)]
    opt=minimize_scalar(lambda t:-abs(amplitude(m,t))**2,
        bounds=(center-0.002,center+0.002),method='bounded',
        options={'xatol':1e-12})
    coeff=m*(1+opt.fun)
    target=good if s%8 in (1,7) else bad
    # error tends to zero; modest safety margin across this finite sequence
    assert abs(coeff-target)<0.09,(k,coeff,target)
    checks+=1

# For nonsquare frequency, the two independent circle phases have dense orbits;
# evaluate their limiting optimized-envelope witness at t=pi/2 and phase 0.
for m in [2,4,5,7,8,9,11,100,101,1001]:
    if math.isqrt(8*m+1)**2==8*m+1: continue
    w=(2*m-1)*np.exp(-.25j*math.pi)
    p=abs(w+1)**2/(4*m*m)
    formula=1-cgen/m+(2-math.sqrt(2))/(4*m*m)
    assert abs(p-formula)<1e-13
    checks+=1

print('ALL_NEW_TRANSPORT_CHECKS_PASSED', checks)
print('nonresonant',format(cgen,'.12f'))
print('triangular favorable',format(good,'.12f'))
print('triangular unfavorable',format(bad,'.12f'))
