"""Exact finite-horizon Fourier-visibility checks for an isotropic Poisson-turning swimmer.
Pure Python standard library; execute python3 checker.py.
"""
from fractions import Fraction
from math import factorial, comb
from itertools import product


def compositions(n, length):
    if length == 1:
        yield (n,)
        return
    for a in range(n+1):
        for b in compositions(n-a, length-1):
            yield (a,)+b


def mode(m, law, order):
    """Exact Fourier coefficients for Haar or order-fold discrete turn law."""
    if law == 'haar':
        return int(m == 0)
    if law == 'comb':
        return int(m % order == 0)
    raise ValueError(law)


def conditional_scaled_moment(n, k, law, order):
    """E|sum_{j=0}^k S_j exp(i(Psi_1+...+Psi_j))|^(2n).

    S ~ Dirichlet(1,...,1); exact rational by multinomial expansion.
    """
    nf = factorial(n)
    ans = Fraction(0)
    vectors = list(compositions(n, k+1))
    for a in vectors:
        for b in vectors:
            cur = Fraction(factorial(k)*nf*nf, factorial(2*n+k))
            for ai, bi in zip(a,b):
                cur *= Fraction(factorial(ai+bi), factorial(ai)*factorial(bi))
            for h in range(1,k+1):
                m = sum(a[j]-b[j] for j in range(h,k+1))
                cur *= mode(m,law,order)
                if not cur:
                    break
            ans += cur
    return ans


def main():
    checks=0
    for n in range(1,8):
        # Top angular Fourier coefficient of a *single* turn is Beta(n+1,n+1).
        beta = Fraction(factorial(n)**2, factorial(2*n+1))
        # Haar and n-Dirac comb differ precisely in nth harmonic among 1...n.
        # For n=1, 1-comb is a deterministic turn of angle 0.
        one = conditional_scaled_moment(n,1,'comb',n)-conditional_scaled_moment(n,1,'haar',n)
        assert one == 2*beta, (n,one,2*beta)
        checks+=1
        for m in range(1,n):
            for k in range(0,4):
                left=conditional_scaled_moment(m,k,'comb',n)
                right=conditional_scaled_moment(m,k,'haar',n)
                assert left==right, (n,m,k,left,right)
                checks+=1
        for k in range(0,3):
            left=conditional_scaled_moment(n,k,'comb',n)
            right=conditional_scaled_moment(n,k,'haar',n)
            assert 0<=left<=1 and 0<=right<=1
            checks+=1
    # Nonasymptotic finite-time bound, computed via exactly summed k<=5
    # and a rigorous common probability tail for k>5.
    from math import exp
    for n in range(1,5):
        coeff = Fraction(2*factorial(n)**2, factorial(2*n+1))
        for lam in (Fraction(1,100),Fraction(1,20),Fraction(1,5),Fraction(1,2)):
            # Approximate Poisson-weighted difference through k=5.
            sm=0.0
            for k in range(0,6):
                df=conditional_scaled_moment(n,k,'comb',n)-conditional_scaled_moment(n,k,'haar',n)
                sm += float(df)*float(lam)**k / factorial(k)
            trunc=exp(-float(lam))*sm
            # True value lies within tail with coefficient at most 2.
            tail=1-exp(-float(lam))*sum(float(lam)**k/factorial(k) for k in range(6))
            # compare against first term and uniform upper bound, accounting tail.
            assert abs(trunc-float(lam*coeff)) <= 3*float(lam)**2+2*abs(tail)+1e-12
            checks+=1
    print('PASS:',checks,'deterministic exact and finite-rate checks')


if __name__=='__main__':
    main()
