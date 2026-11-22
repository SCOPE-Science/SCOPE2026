"""Standalone checks for the generalized Cesaro two-rate kernel-limit algebra.

Only finite exact identities and numerical normalization checks are performed;
infinite-dimensional assertions require the proof in RESULT.md.
"""
from fractions import Fraction
from math import exp, log, pi
from random import Random


def finite_hs_difference(t, s, N):
    return sum((t**j-s**j)**2 / (n+1)**2 for n in range(N)
               for j in range(n+1))


def finite_gram(t, s, N):
    return sum(sum((t*s)**j for j in range(n+1))/(n+1)**2
               for n in range(N))


def gram_infinite(q, N=140000):
    # Direct partial sum plus a controlled tail bound handled separately.
    return sum((1-q**(n+1))/((n+1)**2*(1-q)) for n in range(N))


def kernel_sq_integral(a, b, n=200000, max_u=50.0):
    # midpoint quadrature of the Frullani integrand; tail is exponentially tiny.
    h=max_u/n
    return sum((exp(-a*(k+.5)*h)-exp(-b*(k+.5)*h))**2/((k+.5)*h)
               for k in range(n))*h


def run():
    rng=Random(23)
    exact=0
    for N in range(1, 17):
        for _ in range(18):
            t=Fraction(rng.randint(1, 7), 9)
            s=Fraction(rng.randint(1, 7), 9)
            lhs=finite_hs_difference(t,s,N)
            rhs=finite_gram(t,t,N)+finite_gram(s,s,N)-2*finite_gram(t,s,N)
            assert lhs == rhs, (N,t,s,lhs,rhs)
            exact+=1
    for a,b in [(1.,3.),(.3,4.),(2.,2.5)]:
        goal=log((a+b)**2/(4*a*b))
        val=kernel_sq_integral(a,b)
        assert abs(val-goal)<3e-7, (a,b,val,goal)
        for eps in (.02,.005,.001):
            t,s=1-a*eps,1-b*eps
            # Cross Gram formula evaluated efficiently via 1D partial series.
            val=(gram_infinite(t*t)+gram_infinite(s*s)-2*gram_infinite(t*s))
            # Each tail <= (1/(1-q))*(1/N). Cancellation may improve it.
            bound=(1/(1-t*t)+1/(1-s*s)+2/(1-t*s))/140000
            assert abs(val-goal) < .08+bound, (a,b,eps,val,goal,bound)
    print(f'PASS {exact} exact-rational Gram identities; 3 kernel integrals; 9 boundary metric comparisons')

if __name__=='__main__':
    run()
