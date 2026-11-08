"""Independent Green-kernel checks for stopped logarithmic-potential diffusion.

Run: python checker.py
Only uses local Python, SciPy, and ordinary algebra.
"""
from math import sqrt, isclose
from scipy.integrate import quad


def green(x, y, beta, d):
    return min(x, y)**beta*y**(1-beta)/(d*beta)


def first(p, beta, d, x):
    return x**p/(d*p*(beta-p))


def first_quad(p, beta, d, x):
    f = lambda y: green(x, y, beta, d)*y**(p-2)
    return quad(f, 0, x, epsabs=1e-12)[0] + quad(f, x, float('inf'), epsabs=1e-12)[0]


def second(p, q, beta, d, x):
    return (first(p, beta, d, 1)+first(q, beta, d, 1))*first(p+q, beta, d, x)


def second_quad(p, q, beta, d, x):
    f=lambda y:green(x,y,beta,d)*(y**(p-2)*first(q,beta,d,y)+y**(q-2)*first(p,beta,d,y))
    return quad(f, 0, x, epsabs=1e-12)[0]+quad(f,x,float('inf'),epsabs=1e-12)[0]


def covariance(p, q, beta, d, x):
    return 2*x**(p+q)/(d*d*(beta-p)*(beta-q)*(p+q)*(beta-p-q))


def variance(p, beta, d, x):
    return x**(2*p)/(d*d*p*(beta-p)**2*(beta-2*p))


def correlation(p, q, beta):
    return 2*sqrt(p*q)*sqrt((beta-2*p)*(beta-2*q))/((p+q)*(beta-p-q))


def check():
    n=0
    for p,q in [(0.7,1.2),(1,2),(2,3),(0.5,3.4),(2.2,2.2)]:
        for beta in [2*max(p,q)+0.3,2*max(p,q)+2,2*max(p,q)+25]:
            for d,x in [(1,1),(0.8,1.3)]:
                for z in [p,q,p+q]:
                    assert isclose(first_quad(z,beta,d,x),first(z,beta,d,x),rel_tol=2e-8,abs_tol=1e-9)
                    n+=1
                a,b=second_quad(p,q,beta,d,x),second(p,q,beta,d,x)
                assert isclose(a,b,rel_tol=2e-8,abs_tol=1e-9), (p,q,beta,a,b)
                n+=1
                c=b-first(p,beta,d,x)*first(q,beta,d,x)
                assert isclose(c,covariance(p,q,beta,d,x),rel_tol=2e-8,abs_tol=1e-9)
                n+=1
                v1=second(p,p,beta,d,x)-first(p,beta,d,x)**2
                v2=second(q,q,beta,d,x)-first(q,beta,d,x)**2
                assert isclose(v1,variance(p,beta,d,x),rel_tol=2e-8,abs_tol=1e-9)
                assert isclose(v2,variance(q,beta,d,x),rel_tol=2e-8,abs_tol=1e-9)
                assert isclose(c/sqrt(v1*v2),correlation(p,q,beta),rel_tol=2e-8,abs_tol=1e-9)
                n+=3
    for p,q in [(0.7,1.2),(1,2),(2,3),(0.5,3.4)]:
        vals=[correlation(p,q,2*max(p,q)+x) for x in (0.0001, 0.1,1,10,1000)]
        assert all(a<b for a,b in zip(vals,vals[1:]))
        assert abs(vals[-1]-2*sqrt(p*q)/(p+q))<0.01
        n+=2
    print(f'PASS: {n} kernel-integral, mixed-moment, variance, and sharp-correlation checks')

if __name__=='__main__':
    check()
