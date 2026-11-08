"""Numerical cross-checks for a boundary-loss quantum walk.
Run: python3 CHECK.py. Requires scipy and numpy.
These finite checks supplement the analytic arguments and do not prove the
asymptotic theorems.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
from scipy.sparse import diags
from scipy.sparse.linalg import expm_multiply

pi = math.pi

def band(eta):
    return 2*eta/pi*quad(lambda k: math.sin(k)/(1+eta*eta+2*eta*math.sin(k)),0,pi,epsabs=1e-12)[0]

def outer(n,eta):
    return 2*eta/pi*quad(lambda q:q**(2*n-2)*(1-q*q)/(1+eta*eta*q*q),0,1,epsabs=1e-12)[0]

def P(n,eta):
    return band(eta)+outer(n,eta)

def first_derivative_at_one(n):
    return 2/pi*quad(lambda q:q**(2*n-2)*(1-q*q)**2/(1+q*q)**2,0,1,epsabs=1e-13)[0]

def check():
    checks=0
    # Positive and strictly decreasing spatial correction over multiple strengths.
    for eta in (.15,.5,1,2.5,10):
        values=[P(n,eta) for n in range(1,26)]
        assert all(values[i]>values[i+1] for i in range(len(values)-1))
        assert all(v>band(eta) for v in values)
        checks+=51
    # Reciprocal symmetry holds for the continuum, not at each finite site.
    for eta in (.2,.5,1,2,5):
        assert abs(band(eta)-band(1/eta))<1e-11
        checks+=1
    assert abs(band(1)-(1-2/pi))<1e-12
    checks+=1
    # Boundary source exhibits no finite positive large-coupling cut-off.
    assert P(1,1000)>.99999
    assert P(2,1000)<.002
    checks+=2
    # Exact derivative at unit coupling is positive for all finite n.
    for n in (1,2,3,4,6,10,25,50):
        assert first_derivative_at_one(n)>0
        checks+=1
    # Maximal absorption is attained beyond unit coupling for n >= 2.
    for n in (2,3,4,6,10,20):
        fit=minimize_scalar(lambda t:-P(n,math.exp(t)),bounds=(0,1.0),method='bounded',options={'xatol':1e-12})
        assert fit.x>0 and P(n,math.exp(fit.x))>P(n,1)
        if n>=10:
            assert abs(n**3*fit.x-0.75)<.15
        checks+=1
    # Check asymptotic constants at n=100, 300 with high precision integration.
    for n in (100,300):
        c=outer(n,1)
        assert abs(n*n*c-1/(2*pi))<.003
        d=first_derivative_at_one(n)
        assert abs(n**3*d-1/(2*pi))<.005
        checks+=2
    # Independent finite-chain evolution: direct survival norm approaches integral.
    N=380
    for eta,n in ((.4,1),(1,1),(1,2),(2,2)):
        A=diags([.5j*np.ones(N-1), np.zeros(N), .5j*np.ones(N-1)],[-1,0,1],format='lil')
        A[0,0]=-eta/2
        initial=np.zeros(N,dtype=complex)
        initial[n-1]=1
        final=expm_multiply(A.tocsr()*140.,initial)
        integrated=1-np.vdot(final,final).real
        assert 0<=P(n,eta)-integrated<.004, (eta,n,integrated,P(n,eta))
        checks+=1
    print(f'PASS {checks} deterministic numerical assertions (not an infinite proof)')

if __name__=='__main__':
    check()
