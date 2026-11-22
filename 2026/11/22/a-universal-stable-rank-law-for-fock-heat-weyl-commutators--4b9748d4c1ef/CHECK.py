"""Finite-dimensional checks of Fock dilation/Weyl displacement commutator identities.
Pure Python, no external packages.  Finite tests are not proofs of limit laws.
"""
from math import exp, factorial, sqrt, e


def weyl_entry(m, n, a):
    pref = exp(-a*a/2)*sqrt(factorial(m)*factorial(n))
    return pref*sum(a**(m-k)*(-a)**(n-k)/(
        factorial(m-k)*factorial(n-k)*factorial(k))
                    for k in range(min(m,n)+1))


def hs_square_finite(r, a, N):
    return sum((r**m-r**n)**2*weyl_entry(m,n,a)**2
               for m in range(N) for n in range(N))


def hs_square_exact(r,a,d=1):
    return 2*(1-exp(-a*a*(1-r)/(1+r)))/(1-r*r)**d


def test():
    cases=[(0.3,0.25,20),(0.5,0.4,30),(0.65,0.3,40)]
    for r,a,N in cases:
        numeric=hs_square_finite(r,a,N)
        exact=hs_square_exact(r,a)
        assert abs(numeric-exact) < 2e-8, (r,a,numeric,exact)
    for r in (0.25,0.5,0.8):
        for a in (0.0,0.1,0.7):
            assert hs_square_exact(r,a,2) == 0 if a==0 else hs_square_exact(r,a,2)>0
            assert abs(hs_square_exact(r,a,3) - hs_square_exact(r,a,1)/(1-r*r)**2)<1e-10
    # The coherent-state lower and Jacobi upper bounds sandwich the sharp limit.
    for r in (0.98,0.995,0.999):
        a=0.7
        R=1/sqrt(2*(1-r))
        lower=abs(exp(-(1-r)*R*R)-exp(-(1-r)*(R-a)**2))
        upper=2*a*(1-r)*max(sqrt(n+1)*r**n for n in range(int(6/(1-r))))
        target=a*sqrt(2*(1-r)/e)
        assert lower <= upper*(1+1e-12)
        assert lower/target > 0.97, (r,lower/target)
        assert upper/target < 1.02, (r,upper/target)
    print('PASS: 3 finite matrix comparisons, 9 dimension/positivity identities, 3 norm sandwiches.')

if __name__ == '__main__':
    test()
