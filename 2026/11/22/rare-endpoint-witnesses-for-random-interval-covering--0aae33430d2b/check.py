"""Exact and numerical checks for endpoint-dominated interval covering."""
from fractions import Fraction
from math import comb, factorial, gamma, sqrt, pi, exp, erfc, log
from random import Random


def exact_probability(n):
    assert n >= 1
    return Fraction(4**n * factorial(n) * factorial(n-1), factorial(2*n)) - Fraction(1,n)


def inclusion_exclusion(n):
    out = Fraction(0)
    for j in range(n):
        out += 2*(-1)**j*comb(n-1,j)*(Fraction(1,2*j+1)-Fraction(1,2*j+2))
    return out


def simpson(f,a,b,N=16000):
    assert N%2 == 0
    h=(b-a)/N
    return h/3*(f(a)+f(b)+4*sum(f(a+(2*j-1)*h) for j in range(1,N//2+1))
                +2*sum(f(a+2*j*h) for j in range(1,N//2)))


def joint_t_density(n,t):
    if t<=0 or t>=n:
        return 0.0
    return (n*t)**(-.5)*(1-sqrt(t/n))*(1-t/n)**(n-1)


def main():
    exact=0; numerical=0; stochastic=0
    for n in range(1,41):
        assert exact_probability(n) == inclusion_exclusion(n)
        assert Fraction(0)<exact_probability(n)<=1
        exact+=2
    assert exact_probability(1) == 1
    assert exact_probability(2) == Fraction(5,6)
    assert exact_probability(3) == Fraction(11,15)
    exact+=3
    for n in (1,2,3,5,9,20,40):
        actual=simpson(lambda u: 2*(1-u)*(1-u*u)**(n-1),0.,1.)
        assert abs(actual-float(exact_probability(n)))<1e-9
        numerical+=1
    for n in (2,5,20,100):
        for t in (0.1,0.3,1.,2.):
            if t<n:
                assert joint_t_density(n,t)>0
                numerical+=1
    for n in (20,100,1000):
        from math import lgamma
        p=exp(lgamma(.5)+lgamma(n)-lgamma(n+.5))-1/n
        assert abs(sqrt(n)*p-sqrt(pi))<1.5/sqrt(n)
        numerical+=1
    # Independently integrate the finite law of the scaled endpoint numerator.
    for n in (100,500,5000):
        p=float(exact_probability(n))
        scale=sqrt(n)
        def witness_v_density(v):
            if v<0 or v>=scale:
                return 0.0
            return (2/scale)*(1-v/scale)*(1-v*v/n)**(n-1)/p
        assert abs(simpson(witness_v_density,0,min(scale,10),8000)-1)<1e-7
        numerical+=1
        for y in (-2.,0.,2.):
            cdf=simpson(witness_v_density,exp(-y/2),min(scale,10),8000)
            limit=erfc(exp(-y/2))
            assert abs(cdf-limit)<.2/sqrt(n)
            numerical+=1
    rng=Random(330331)
    for n in (3,8,21):
        trials=30000
        count=0
        for k in range(trials):
            a=[rng.expovariate(1.0) for _ in range(n+1)]
            z=max(a[0],a[-1])
            count += (2*z > max(a[1:-1]))
        p=float(exact_probability(n))
        assert abs(count/trials-p) < 6*sqrt(p*(1-p)/trials)
        stochastic+=1
    print(f'PASS: {exact} exact Fraction assertions; {numerical} numerical checks; {stochastic} seeded Monte Carlo confirmations')

if __name__=='__main__':
    main()
