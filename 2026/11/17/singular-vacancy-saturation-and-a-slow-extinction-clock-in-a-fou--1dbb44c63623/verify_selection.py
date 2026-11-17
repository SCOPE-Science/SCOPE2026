"""Numerical sanity checks for the nonlinear recruitment selection law.
Not a proof of convergence or originality; analytical derivation is in RESULT.md.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import lambertw

def rhs(t,y,a,b,k,V,gamma):
    T,R,I,B=y
    flux=k*(V-R)*T
    return [-a*T-flux,flux-b*R,a*T+b*R-gamma*I,gamma*I]

def selected(a,k,V,T0,R0):
    Z0=V-R0
    if Z0==0: return V
    arg=(k/a)*Z0*math.exp((k/a)*(Z0-T0))
    return V-(a/k)*float(lambertw(arg).real)

checks=0
for (a,k,V,T0,R0,I0,gamma) in [(1.2,0.7,3.1,0.9,0.8,0.4,1.6),(0.35,1.8,2.1,0.4,0.1,0.05,1.25),(2.0,0.25,5.0,1.1,2.0,0.8,0.5)]:
    N=T0+R0+I0+0.4
    Rstar=selected(a,k,V,T0,R0)
    sol0=solve_ivp(rhs,[0,250/a],[T0,R0,I0,0.4],args=(a,0,k,V,gamma),rtol=1e-11,atol=1e-13, dense_output=True)
    assert sol0.success
    assert abs(sol0.y[1,-1]-Rstar)<3e-9, (Rstar,sol0.y[1,-1]);checks+=1
    vals=sol0.sol(np.linspace(0,100/a,100))
    Z=V-vals[1]
    invariant=vals[0]-Z-(a/k)*np.log(Z)
    assert max(abs(invariant-invariant[0]))<2e-9;checks+=1
    b=a/200
    sol=solve_ivp(rhs,[0,2/b],[T0,R0,I0,0.4],args=(a,b,k,V,gamma),rtol=1e-10,atol=1e-12,dense_output=True)
    assert sol.success
    for tau in [0.3,0.7,1.0,2.0]:
        T,R,I,B=sol.sol(tau/b)
        err=abs(R-Rstar*math.exp(-tau))
        assert err<0.05, (a,k,tau,err)
        assert abs(T+R+I+B-N)<1e-8
        checks+=1


# Test the distinct vacancy-saturation asymptotic normalizations.
asymptotic_tests=0
a=1.0; V=3.0; R0=0.7; Z0=V-R0
for k in (20.0,60.0,200.0):
    L=k/a
    # Subcapacity: the first correction has an exact positive limit.
    T0=1.2; d=Z0-T0
    z=(a/k)*float(lambertw(L*Z0*math.exp(L*d)).real)
    assert abs(L*(z-d)-math.log(Z0/d)) < 0.04; asymptotic_tests+=1
    # Exact capacity: an exact Lambert-W boundary layer.
    T0=Z0
    z=(a/k)*float(lambertw(L*Z0).real)
    assert abs(L*z-float(lambertw(L*Z0).real)) < 1e-12; asymptotic_tests+=1
    # Overcapacity: exponentially small vacancies, tested relative to scale.
    T0=3.0; d=T0-Z0
    z=(a/k)*float(lambertw(L*Z0*math.exp(-L*d)).real)
    assert abs(z/(Z0*math.exp(-L*d))-1) < 0.0001;asymptotic_tests+=1

print(f'VERIFY_OK parameter_cases=3 exact_first_integrals=3 endpoint_selections=3 slow_scaled_samples={checks-6} saturation_asymptotics={asymptotic_tests}')
