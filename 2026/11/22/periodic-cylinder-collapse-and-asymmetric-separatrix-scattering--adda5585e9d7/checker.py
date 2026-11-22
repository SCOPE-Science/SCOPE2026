"""Numerical reproducibility for the explicit Duffing separatrix displacement.
Uses only the Python standard library; all infinite claims require the proof.
"""
from math import pi, sqrt, exp, cosh, tanh

def simpson(f, a, b, n=12000):
    assert n % 2 == 0
    h = (b-a)/n
    return h/3 * (f(a)+f(b)+sum((4 if i % 2 else 2)*f(a+h*i) for i in range(1,n)))

def J(s):
    # substitute v=sin(theta) into the integrable endpoint singularity
    from math import sin
    return 2*simpson(lambda theta:exp(s*sin(theta)),0,pi/2)

def main():
    zeta=2.; b=3.; alpha=1.; A=sqrt(2*zeta/b); k=sqrt(zeta)
    for t in [-3.2,-1.3,0.,1.2,3.9]:
        h=1/cosh(k*t); q=tanh(k*t)
        x=A*h; y=-A*k*h*q
        accel=A*k*k*h*(2*q*q-1)
        assert abs(accel-(zeta*x-b*x**3))<3e-14
        assert abs(.5*y*y-.5*zeta*x*x+.25*b*x**4)<5e-14
    for beta in [-2.,-.2,0.,.2,2.]:
        for sign in [-1,1]:
            s=sign*beta*A
            direct=simpson(lambda t:sign*alpha*A/cosh(k*t)*exp(s/cosh(k*t)), -20./k,20./k, 20000)
            analytic=sign*alpha*A/k*J(s)
            assert abs(direct-analytic)<2e-8*(1+abs(analytic)),(beta,sign,direct,analytic)
    assert abs(A/k*J(0)-pi*sqrt(2/b))<1e-11
    for beta in [.2,1.,2.]:
        plus=alpha*A/k*J(beta*A)
        minus=-alpha*A/k*J(-beta*A)
        assert plus>0 and minus<0 and plus+minus>0
    from math import log
    s=32.
    jp=J(s)
    jm=J(-s)
    assert abs(jp/(exp(s)*sqrt(2*pi/s))-1)<.02
    assert abs(jm/(2/s)-1)<.02
    print('PASS: separatrix, Hamiltonian, two drift integral forms, signs, threshold and asymptotic samples')
if __name__=='__main__': main()
