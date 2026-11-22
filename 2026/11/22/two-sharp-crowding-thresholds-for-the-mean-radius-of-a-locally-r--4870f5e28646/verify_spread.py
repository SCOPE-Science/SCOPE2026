#!/usr/bin/env python3
"""Independent numerical quadrature and exact consistency tests for a two-phase stationary active-gas profile."""
from math import sqrt, log, exp, isclose

def q_of_mu(mu):
    return 2.0/(1.0+sqrt(1.0-4.0/mu))

def moment_closed(c, chi, mu):
    q=q_of_mu(mu)
    return ((c-1.0)*(q-1.0)/(q*q)+(1.0+q+4.0/q)/6.0)/(c*chi)

def simpson(func,a,b,n=2000):
    assert n%2==0
    delta=(b-a)/n
    return delta/3.0*(func(a)+func(b)+4.0*sum(func(a+i*delta) for i in range(1,n,2)) +2.0*sum(func(a+i*delta) for i in range(2,n,2)))

def moment_integrated(c,chi,mu):
    # Compute first moments directly in spatial coordinates, using inverse flux on the gas side.
    q=q_of_mu(mu)
    b=log(c)/(mu*chi)
    dense=simpson(lambda x:x*mu*c*exp(-mu*chi*x),0.0,b)
    # Transform gas-side spatial integral with exact x(rho), Jacobian -dx/drho.
    def gas(t):
        rho=q*exp(-t)
        x=b+(t-2.0*(q-rho)/mu)/chi
        return x*(1.0-2.0*rho/mu)*rho/chi
    gas_one=simpson(gas,0.0,45.0,4000)
    return (dense+gas_one)*chi/c

def test():
    checked=0
    for c in (1.05,1.2,1.5,1.7,2.,7./3.,2.5,4.):
        for chi in (.4,1.0,2.0):
            for mu in (4.001,4.2,5.,8.,15.,1000.):
                a=moment_closed(c,chi,mu)
                b=moment_integrated(c,chi,mu)
                assert abs(a-b)<6.e-5*(1+abs(a)),(c,chi,mu,a,b)
                checked+=1
            lo=moment_closed(c,chi,4.0000001)
            hi=moment_closed(c,chi,1.e12)
            assert isclose(lo,((3*c+7.)/12.)/(c*chi),rel_tol=1e-4)
            assert isclose(hi,1./(c*chi),rel_tol=1e-5)
            checked+=2
    for c in (1.1,1.5,1.7,2.0,2.2,7./3.,3.0):
        vals=[moment_closed(c,1.,4.0000001+0.002*i) for i in range(1,100)]
        if c<=1.5: assert all(vals[i+1]>vals[i] for i in range(len(vals)-1))
        elif c>=7./3.: assert all(vals[i+1]<vals[i] for i in range(len(vals)-1))
        else:
            q=sqrt(6*c-5)-1
            opt=q*q/(q-1)
            objective=moment_closed(c,1.,opt)
            assert opt>4
            assert all(objective>z for z in vals if abs(z-objective)>1e-12)
        checked+=1
    print(f'PASS: {checked} quadrature, boundary, and optimizer checks')

if __name__=='__main__': test()
