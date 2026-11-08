"""Exact and independent numerical checks for the balanced exponential EFX law."""
from fractions import Fraction as F
from math import comb, factorial, log, exp
from random import Random
from scipy.integrate import quad


def poly_mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def tail_coefficients(r):
    """Return Q and c with P(T>t)=exp(-t) Q(t)-c exp(-r*t/(r-1))."""
    k=r-1
    q=[F(1,factorial(l)) for l in range(k)]
    for j in range(k):q[k-1-j]+=F((-1)**j*k**(j+1),factorial(k-1-j))
    c=(-1)**(k-1)*k**k
    return q,c


def exact_row_probability(n,r):
    assert n>=2 and r>=2
    q,c=tail_coefficients(r)
    k=r-1; rate=F(r,k); N=n-1
    powers=[[F(1)]]
    for _ in range(N):powers.append(poly_mul(powers[-1],q))
    total=F(0)
    for i in range(N+1):
        for j in range(N+1-i):
            mult=F(factorial(N),factorial(i)*factorial(j)*factorial(N-i-j))*(-1)**i * c**j
            den=1+i+rate*j
            for l,coef in enumerate(powers[i]):
                if coef:total+=mult*coef*F(factorial(r+l-1),factorial(r-1))*den**(-(r+l))
    return total


def row_mc(n,r,trials=30000,seed=1234):
    rng=Random(seed);wins=0
    for _ in range(trials):
        own=sum(rng.expovariate(1) for _ in range(r))
        competitors=[[rng.expovariate(1) for _ in range(r)] for _ in range(n-1)]
        wins+=all(own>=sum(a)-min(a) for a in competitors)
    return wins/trials


def row_quad(n,r):
    from math import lgamma
    q,c=tail_coefficients(r)
    def integrand(t):
        qt=sum(float(x)*t**i for i,x in enumerate(q))
        surv=exp(-t)*qt-c*exp(-r*t/(r-1))
        cdf=max(0.,min(1.,1-surv))
        return t**(r-1)*exp(-t)/factorial(r-1)*cdf**(n-1)
    return quad(integrand,0,max(50,8*log(n)),epsabs=1.e-11,epsrel=1.e-11)[0]


def main():
    checked=0
    for r in range(2,6):
        q,c=tail_coefficients(r)
        assert q[0]-c==1
        assert q[-1]==F(r,factorial(r-2))
        for n in range(2,7):
            p=exact_row_probability(n,r)
            assert 0<p<1,(n,r,p)
            numeric=row_quad(n,r)
            assert abs(float(p)-numeric)<2e-9,(n,r,p,numeric)
            checked+=1
            if r==2:
                h=sum((F(1,j) for j in range(1,2*n)))
                assert p==h/F(2*n-1)
    print('exact-versus-quadrature comparisons:',checked)
    for n,r in [(2,2),(3,2),(4,3),(3,4),(6,2)]:
        true=float(exact_row_probability(n,r))
        sim=row_mc(n,r)
        assert abs(true-sim)<0.013,(n,r,true,sim)
        print('MC',n,r,'theory',round(true,6),'estimate',round(sim,6))
    print('P_2,2',exact_row_probability(2,2)**2)
    print('P_3,2',exact_row_probability(3,2)**3)
    print('all checks passed')

if __name__=='__main__':main()
