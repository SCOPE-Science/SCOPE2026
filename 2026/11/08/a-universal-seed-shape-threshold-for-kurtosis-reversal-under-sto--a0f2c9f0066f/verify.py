#!/usr/bin/env python3
"""Reproduce exact fourth-moment identities and independent renewal quadrature.

Requires only Python's standard library. This is a finite diagnostic, not an
independent proof of the analytic sign classification.
"""
from fractions import Fraction as F
from math import exp, expm1, sqrt, isclose


def moment_generator(beta, w, chi):
    rho2 = F(2)*w/beta
    rho4 = chi*rho2*rho2
    M = {(0, 0): F(1)}
    for n in (2, 4):
        for i in range(n+1):
            j = n-i
            if j == 0:
                M[i,j] = beta*M[i-1,1]
            else:
                reset = {2: rho2, 4: rho4}.get(j, F(0))
                M[i,j] = (i*beta*M.get((i-1,j+1),F(0))+
                    j*(j-1)*M.get((i,j-2),F(0)) + beta*reset*M.get((i,0),F(0)))/(i+beta)
    return M[2,0], M[4,0]


def formula(beta, w, chi):
    return F(6)*(((beta+1)*chi-(2*beta+3))*w*w + 5*beta*w + 7*beta+3)/((beta+2)*(beta+3)*(1+w)**2)


def integrate(f, beta, n=12000):
    # Independent Poisson-waiting-time integration using composite Simpson.
    tmax = 60.0/beta
    h = tmax/n
    acc = f(0.0)+f(tmax)
    for i in range(1,n):
        t = i*h
        acc += (4 if i%2 else 2)*f(t)
    return h*acc/3


def renewal(beta,w,chi):
    z=2*w/beta; q=chi*z*z
    def kern(t):
        u=exp(-t); h=-expm1(-t)
        vg=2*beta*beta*(t-2*h+(-expm1(-2*t))/2)
        a2=beta*beta*z*h*h+vg
        a4=beta**4*q*h**4+6*beta*beta*z*h*h*vg+3*vg*vg
        return u,a2,a4
    def expectation(which):
        return integrate(lambda t:beta*exp(-beta*t)*which(*kern(t)),beta)
    e2=expectation(lambda u,a2,a4:a2)
    m2=e2/(1-beta/(beta+2))
    term=expectation(lambda u,a2,a4:u*u*a2)
    a4=expectation(lambda u,a2,a4:a4)
    m4=(6*m2*term+a4)/(1-beta/(beta+4))
    return m2,m4


def main():
    assertions=0
    for beta in [F(1,3),F(1,2),F(1),F(3,2),F(2),F(5),F(10)]:
        for w in [F(1,10),F(1),F(2),F(4),F(10)]:
            for chi in [F(1),F(3,2),F(2),F(5,2),F(3),F(4)]:
                m2,m4=moment_generator(beta,w,chi)
                assert m2 == 2*beta*(w+1)/(beta+1)
                assertions += 1
                assert m4/m2**2-3 == formula(beta,w,chi)
                assertions += 1
    for beta,w,chi in [(0.5,0.5,1),(1,1,1),(1,3,1),(2,4,3),(3,2,2.2),(5,8,1.8)]:
        x,y=renewal(beta,w,chi)
        m2,m4=moment_generator(F(str(beta)),F(str(w)),F(str(chi)))
        assert isclose(x,float(m2),rel_tol=4e-7,abs_tol=1e-8),(beta,w,chi,'m2',x,float(m2))
        assert isclose(y,float(m4),rel_tol=6e-7,abs_tol=1e-8),(beta,w,chi,'m4',y,float(m4))
        assertions += 2
    for beta in [0.1,0.5,1,2,5,20]:
        critical=(2*beta+3)/(beta+1)
        for chi in [1,1.5,2,2.2,2.7,3,4]:
            if chi>=critical:
                for w in [0.01,1,5,1000]:
                    assert formula(beta,w,chi)>0
                    assertions+=1
            else:
                B=(2*beta+3)-(beta+1)*chi
                wc=(5*beta+sqrt(25*beta*beta+4*B*(7*beta+3)))/(2*B)
                assert formula(beta,wc*0.5,chi)>0
                assert formula(beta,wc*2,chi)<0
                assert abs(formula(beta,wc,chi))<1e-10
                assertions+=3
    print(f'PASS: {assertions} finite deterministic checks (exact rational moments; independent renewal quadrature; phase boundaries).')
    print('Analytical stationarity and infinite-parameter phase classification require the written proof.')
if __name__=='__main__':main()
