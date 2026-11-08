"""Independent numerical checks of the detuning-weighted Kuramoto triad formulas.

Finite tests corroborate; the exact statements require the analytic proof.
Requires Python 3, numpy and scipy.
"""
import math
import numpy as np
from scipy.optimize import brentq


def weights(K, p):
    z = 2.0 ** p
    a = 3.0 * K / (2.0 * (2.0 + z))
    b = z * a
    assert abs((4*a + 2*b)/3 - K) < 1e-11
    return a, b


def fold_phase(z):
    # Stable quadratic root of 4*z*c*c+c-2*z=0.
    c = 4*z / (math.sqrt(1+32*z*z) + 1)
    # rationalized formula? Algebra: (sqrt(1+32z^2)-1)/(8z) = (4z)/(sqrt+1)
    return math.acos(c)


def critical_budget(omega, p):
    z = 2**p
    phi = fold_phase(z)
    Kcrit = 2*omega*(z+2)/(3*(math.sin(phi)+z*math.sin(2*phi)))
    return Kcrit


def stable_phase(omega, K, p):
    kc = critical_budget(omega, p)
    if not K > kc:
        raise ValueError("no hyperbolic locked state")
    a, b = weights(K,p)
    phi_max=fold_phase(2**p)
    return brentq(lambda phi: a*math.sin(phi)+b*math.sin(2*phi)-omega,
                  0,phi_max,xtol=1e-14)


def jacobian(theta, a, b):
    pair = ((0,1,a),(1,2,a),(0,2,b))
    J = np.zeros((3,3))
    for i,j,w in pair:
        c=w*math.cos(theta[j]-theta[i])
        J[i,j]+=c; J[j,i]+=c
        J[i,i]-=c; J[j,j]-=c
    return J


def rhs(theta, omega, a,b):
    R=np.array([-omega,0.,omega]);
    for i,j,w in ((0,1,a),(1,2,a),(0,2,b)):
        term=w*math.sin(theta[j]-theta[i]);R[i]+=term;R[j]-=term
    return R


def check():
    tests=0
    for p in (0,0.1,0.5,1,1.7,2,3,4,5,7,10,15,20):
        z=2.0**p; phi=fold_phase(z)
        assert math.pi/4 < phi < math.pi/2
        assert abs(4*z*math.cos(phi)**2+math.cos(phi)-2*z)<2e-14*z
        assert math.cos(phi) >= (math.sqrt(33)-1)/8 - 1e-13
        tests+=3
        for ratio in (0.7,0.88,1.,1.15,1.4,2.,4.):
            K=ratio*critical_budget(1,p)
            if ratio<=1:continue
            a,b=weights(K,p)
            x=stable_phase(1,K,p)
            theta=np.array([-x,0.,x]);
            assert np.linalg.norm(rhs(theta,1,a,b),ord=np.inf)<2e-12
            J=jacobian(theta,a,b)
            w=np.linalg.eigvalsh(J)
            predicted=np.sort([-3*a*math.cos(x),-(a*math.cos(x)+2*b*math.cos(2*x)),0.])
            assert np.max(np.abs(w-predicted))<1e-10
            assert max(w[:2])<-1e-12
            tests+=4
    for p in (0,0.2,0.7,1,2,3,5,8,12,20):
        if p>0: assert critical_budget(1,p)<critical_budget(1,p-0.00001)
        tests+=1
    for K in (0.72,1.,1.5,2.,3.,5.):
        present=[]
        for p in (0,0.2,0.6,1,1.5,2,3,4,5,7,9,12,16,20):
            if K>critical_budget(1,p):
                x=stable_phase(1,K,p)
                present.append((p,x,(1+2*math.cos(x))/3))
        for (_,x1,r1),(_,x2,r2) in zip(present,present[1:]):
            assert x2<x1 and r2>r1
            tests+=2
    # Compare asymptotic spectral-gap and coherence-error coefficients.
    for K in (0.75,1.0,1.5,2.,5.):
        s=2/(3*K)
        xinf=math.asin(s)/2
        delta=(2*s-math.sin(xinf))/(2*math.cos(2*xinf))
        A=(2/3)*math.sin(xinf)*delta
        B=(9*K/2)*math.cos(xinf)
        for p in (14.,18.,22.):
            x=stable_phase(1,K,p)
            a,b=weights(K,p)
            spectral=min(3*a*math.cos(x),a*math.cos(x)+2*b*math.cos(2*x))
            error=((1+2*math.cos(xinf))/3-(1+2*math.cos(x))/3)
            assert abs(error*2**p/A-1)<0.01
            assert abs(spectral*2**p/B-1)<0.01
            tests+=2
    print(f"VERIFY_OK checks={tests} asymptotic_cases=15 full_jacobian_and_phase=52")

if __name__=='__main__':check()
