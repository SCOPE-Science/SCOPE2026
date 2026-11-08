"""Reproducible finite-volume and continuum checks for cubic-score law."""
import math
from fractions import Fraction


def gaussian_moment_even(k):
    z=1
    for j in range(1, k+1, 2):
        z*=j
    return z


def v_periodic(length, a, gamma, kc, modes=1500, sigma=1.0):
    return sigma*sigma/(2*length)*sum(
        1/(a+gamma*((2*math.pi*j/length)**2-kc*kc)**2)
        for j in range(-modes, modes+1)
    )


def phi(eta):
    return math.pi/math.sqrt(2)*math.sqrt(math.sqrt(1+eta**4)+eta*eta)/math.sqrt(1+eta**4)


def v_inf(a, gamma, kc, sigma=1.0):
    eta=kc*(gamma/a)**.25
    return sigma*sigma/(4*math.pi*gamma**.25*a**.75)*phi(eta)


def per_length_time_information(v, sigma=1.0):
    return 6*v**3/(sigma*sigma)


def test():
    # Gaussian Wick orthogonality and squared residual norm for several rational variances.
    checks=0
    for den in range(1, 10):
        for num in range(1, 10):
            v=Fraction(num,den)
            m2=v
            m4=gaussian_moment_even(3)*v*v  # E[X^4]=3v^2
            m6=gaussian_moment_even(5)*v*v*v  # E[X^6]=15v^3
            assert m4-3*v*m2==0
            assert m6-6*v*m4+9*v*v*m2==6*v*v*v
            checks+=2
    for a,gamma,kc in [(0.2,1.0,0.),(.5,2.,1.),(.03,.4,.6),(1.,3.,2.)]:
        t=v_inf(a,gamma,kc)
        for length in [100.,250.]:
            r=v_periodic(length,a,gamma,kc)
            assert abs(r/t-1)<1e-5,(a,gamma,kc,length,t,r)
            checks+=1
    for e in [1e-3,1e-4,1e-5]:
        # Exact finite-volume resonant mode count: k*=2pi/L and k*=0.
        L=10.0
        for kc, r in [(0.,1),(2*math.pi/L,2)]:
            v=v_periodic(L,e,1.,kc)
            assert abs(e*v/(r/(2*L))-1)<.02,(e,kc,v,r)
            checks+=1
    # Infinite-volume asymptotics and the explicit, uniform crossover function.
    for eta in [0.,.2,1.,3.,10.,30.]:
        # Simpson quadrature of integrand over a finite window.
        R=max(200.,3*eta)
        n=160000
        dx=2*R/n
        def f(q): return 1/(1+(q*q-eta*eta)**2)
        S=f(-R)+f(R)
        for j in range(1,n):
            S+=(4 if j%2 else 2)*f(-R+j*dx)
        val=dx*S/3
        assert abs(val/phi(eta)-1)<1e-5,(eta,val,phi(eta))
        checks+=1
    print('VERIFY_OK checks=%d finite_lengths=2 resonance_cases=2 continuum_eta=6'%checks)

if __name__=='__main__':test()
