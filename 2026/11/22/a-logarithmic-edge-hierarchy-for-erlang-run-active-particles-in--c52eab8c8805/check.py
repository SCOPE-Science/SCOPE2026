"""Finite consistency checks of the renewal-tail formulas; not a proof.

Requires Python 3 and NumPy. Run: python check.py
"""
from math import factorial, exp, log, isclose
from fractions import Fraction
import numpy as np


def gamma_age_survival(t, m, beta):
    z = beta * t
    poly = sum((m-j)*z**j/factorial(j) for j in range(m))/m
    return np.exp(-z)*poly


def gamma_run_survival(t, m, beta):
    z = beta*t
    return np.exp(-z)*sum(z**j/factorial(j) for j in range(m))


def equilibrium_start_gap(rng, m, beta, n=350000):
    z = np.ones(n)
    for _ in range(45):
        s_minus = rng.gamma(m, 1.0/beta, size=n)
        s_plus = rng.gamma(m, 1.0/beta, size=n)
        b, c = np.exp(-s_minus), np.exp(-s_plus)
        z = 2.0*(1.0-b) + b*c*z
    return z


def phase_moment_second(m, beta):
    # Generator of the 2*m-state phase representation. Relaxation rate is one.
    n = 2*m
    generator = np.zeros((n,n))
    sign = np.array([1.0]*m + [-1.0]*m)
    for i in range(n):
        j = (i+1)%n
        generator[i,j] = beta
        generator[i,i] = -beta
    pi = np.ones(n)/n
    first = np.linalg.solve(np.eye(n)-generator.T, sign*pi)
    second = np.linalg.solve(2*np.eye(n)-generator.T, 2*sign*first)
    return second.sum()


def main():
    checks = 0
    # The age survivor is the exact integrated Erlang survival, not the ordinary survival.
    for m in range(1,7):
        for beta in (0.4, 1.0, 2.6):
            for t in (0.0, 0.25, 1.2, 4.3):
                s = gamma_age_survival(t,m,beta)
                assert 0 <= s <= 1+1e-14
                assert isclose(gamma_age_survival(0,m,beta),1,abs_tol=1e-14)
                h = 1e-5
                if t>h:
                    deriv=(gamma_age_survival(t+h,m,beta)-gamma_age_survival(t-h,m,beta))/(2*h)
                    assert abs(deriv+beta/m*gamma_run_survival(t,m,beta))<1e-8
                checks+=1
    assert Fraction(2,1)/(1+Fraction(1,4))==Fraction(8,5)
    checks+=1
    rng=np.random.default_rng(187371)
    for m,beta in ((2,1.),(3,1.5),(2,3.)):
        z=equilibrium_start_gap(rng,m,beta)
        assert np.all(z>0) and np.all(z<2)
        checks+=1
        a1=(beta/(beta+1))**m
        assert abs(z.mean()-2/(1+a1))<0.012
        checks+=1
        negative=float(np.mean(z**(-beta)))
        assert np.isfinite(negative) and negative>0
        c=beta**(m-1)*negative/(2*m*factorial(m-1))
        scaled=[]
        for delta in (1e-2,1e-4,1e-6,1e-8):
            t=np.maximum(0,np.log(z/delta))
            plus=0.5*gamma_age_survival(t,m,beta).mean()
            scaled.append(plus/(delta**beta*log(1/delta)**(m-1)))
            checks+=1
        assert scaled[0]>scaled[-1]>c*0.98
        assert abs(scaled[-1]/c-1)<0.23
        checks+=2
        if m==2 and beta==1:
            # Stationary position from size-biased run length plus uniform age.
            length=rng.gamma(m+1,1/beta,size=len(z))
            age=length*rng.random(len(z))
            positive_x=1-z*np.exp(-age)
            sign=np.where(rng.random(len(z))<0.5,1,-1)
            x=sign*positive_x
            independent=phase_moment_second(m,beta)
            assert abs(np.mean(x**2)-independent)<0.012
            checks+=1
            print('Independent phase-generator E[X^2]:',format(independent,'.9f'))
        print('shape',m,'rate/trap',beta,'entrance inverse moment',format(negative,'.8f'),
              'prefactor',format(c,'.8f'),'scaled ratio at 1e-8',format(scaled[-1]/c,'.6f'))
    print('PASS',checks,'finite symbolic/numeric consistency checks; the infinite asymptotic is proved analytically in RESULT.md.')

if __name__=='__main__': main()
