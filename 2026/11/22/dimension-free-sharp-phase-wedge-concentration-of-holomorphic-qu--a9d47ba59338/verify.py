"""Independent finite checks for phase-wedge compression of holomorphic quadratics.
Uses direct angular/radial quadrature and a separate symbolic matrix construction.
No numerical check substitutes for the proof for all dimensions and all apertures.
"""
import math
from functools import lru_cache
import numpy as np
from scipy.integrate import quad
from scipy.special import gammaln
import sympy as sp

@lru_cache(None)
def radial_integral(k,a,b):
    power=(a+b)/2
    return quad(lambda t:t**power*(1-t)**(k-power),0,1,epsabs=1e-12,epsrel=1e-12)[0]

def direct_quadrature(k,theta):
    ans=np.zeros((k+1,k+1))
    for a in range(k+1):
        for b in range(k+1):
            ca=math.sqrt(math.factorial(k+1)/(math.factorial(a)*math.factorial(k-a)))
            cb=math.sqrt(math.factorial(k+1)/(math.factorial(b)*math.factorial(k-b)))
            ang=quad(lambda phi:math.cos((a-b)*phi),-theta,theta,epsabs=1e-12)[0]/(2*math.pi)
            ans[a,b]=ca*cb*radial_integral(k,a,b)*ang
    return ans

def formula(k,theta):
    out=np.zeros((k+1,k+1))
    for a in range(k+1):
        for b in range(k+1):
            p=(a+b)/2
            radial=math.gamma(1+p)*math.gamma(1+k-p)/math.sqrt(math.factorial(a)*math.factorial(b)*math.factorial(k-a)*math.factorial(k-b))
            ang=theta/math.pi if a==b else math.sin((a-b)*theta)/(math.pi*(a-b))
            out[a,b]=radial*ang
    return out

def explicit_m2(theta):
    t=theta/math.pi
    s=math.sin(theta)
    c=math.sin(2*theta)/(4*math.pi)
    r=math.sqrt(c*c/4+9*s*s/64)
    return np.array([t+c/2-r,t-c,t+c/2+r])

def multiindices(d,m):
    if d==1:
        yield (m,)
        return
    for j in range(m+1):
        for rest in multiindices(d-1,m-j):
            yield (j,)+rest

def full_dimension_matrix(d,m,theta):
    I=list(multiindices(d,m))
    out=np.zeros((len(I),len(I)))
    for i,a in enumerate(I):
        for j,b in enumerate(I):
            if a[2:]==b[2:]:
                k=a[0]+a[1]
                assert k==b[0]+b[1]
                out[i,j]=formula(k,theta)[a[0],b[0]]
    return out

def verify():
    errs=[]
    for theta in [0.23,0.73,math.pi/3,math.pi/2,2.21,2.91]:
        for k in range(7):
            A=direct_quadrature(k,theta)
            B=formula(k,theta)
            errs.append(np.max(np.abs(A-B)))
            assert np.max(np.abs(A-B))<3e-11
        e=np.linalg.eigvalsh(formula(2,theta))
        assert np.max(np.abs(e-np.sort(explicit_m2(theta))))<1e-13
        ek1=np.linalg.eigvalsh(formula(1,theta))
        assert np.max(np.abs(ek1-[theta/math.pi-math.sin(theta)/4,theta/math.pi+math.sin(theta)/4]))<1e-13
        for k in range(6):
            a=np.linalg.eigvalsh(formula(k,theta))
            b=np.linalg.eigvalsh(formula(k+1,theta))
            assert b[0] <= a[0]+1e-12 and b[-1] >= a[-1]-1e-12
    for d in range(2,9):
        for theta in (0.71,math.pi/2,2.12):
            got=np.linalg.eigvalsh(full_dimension_matrix(d,2,theta))
            predicted=list(explicit_m2(theta))
            predicted += [theta/math.pi-math.sin(theta)/4]*(d-2)
            predicted += [theta/math.pi+math.sin(theta)/4]*(d-2)
            predicted += [theta/math.pi]*((d-2)*(d-1)//2)
            assert len(got)==d*(d+1)//2
            assert np.max(np.abs(got-np.sort(predicted)))<2e-13
    t=sp.symbols('t',positive=True)
    s,c=sp.symbols('s c',real=True)
    M=sp.Matrix([[t,c, s],[c,t,c],[s,c,t]])
    # Here c=3 sin(theta)/(8 sqrt(2)), s=sin(2theta)/(4pi).
    eig=sp.factor(M.charpoly().as_expr())
    expect=sp.expand((sp.Symbol('lambda')-t+s)*((sp.Symbol('lambda')-t)*(sp.Symbol('lambda')-t-s)-2*c*c))
    assert sp.expand(eig-expect)==0
    print('PASS: 42 exact-structure vs independent quadrature checks, max error',max(errs))
    print('PASS: all 6 quadratic spectra match; finite monotone spectral-edge tests k=0..6')
    print('PASS: symbolic cubic characteristic polynomial')
    print('PASS: all-dimensional quadratic multiplicities d=2..8, three apertures')
    print('half-phase spectrum d>=3:', [1/8,1/4,1/2,3/4,7/8])
    print('squared restriction condition number:',7)

if __name__=='__main__': verify()
