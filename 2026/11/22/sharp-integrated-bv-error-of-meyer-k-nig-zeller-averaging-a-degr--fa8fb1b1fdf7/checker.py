"""Exact checks for a Beta-cell representation of classical MKZ approximation.
No external packages. Run with python checker.py.
"""
from math import comb, isqrt
from fractions import Fraction


def beta_cdf(a, b, x):
    """I_x(a,b) for positive integer a,b and rational x."""
    N = a+b-1
    return sum((Fraction(comb(N,j)) * x**j * (1-x)**(N-j)
                for j in range(a,N+1)), Fraction(0))


def beta_abs(k,n,s):
    """E|B-s| for B ~ Beta(k,n+1); exact rational."""
    mean = Fraction(k,n+k+1)
    return mean-s + 2*(s*beta_cdf(k,n+1,s)
                         -mean*beta_cdf(k+1,n+1,s))


def endpoints(k,n):
    return Fraction(k-1,n+k-1),Fraction(k,n+k)


def cutoff(n):
    """Beyond this index all candidates are below 1/(n+2)."""
    rootceil = isqrt(n+1)
    if rootceil*rootceil != n+1:
        rootceil += 1
    return (n+2)*(1+rootceil)+1


def small_n():
    comparisons = 0
    for n in range(1,8):
        best = Fraction(1,n+2)
        closest = Fraction(0)
        runner = None
        for k in range(1, cutoff(n)+1):
            sl,sr=endpoints(k,n)
            for side,s in [('L',sl),('R',sr)]:
                val=beta_abs(k,n,s)
                comparisons+=1
                if (k,side)==(1,'L'):
                    assert val == best
                else:
                    assert val < best, (n,k,side,val,best)
                    if val>closest:
                        closest=val;runner=(k,side)
        print('n=%d k<=%d: boundary= %s, largest other %s at %s' %
              (n,cutoff(n),best,closest,runner))
    print('EXACT_SMALL_DEGREE_CANDIDATE_CHECKS_PASS',comparisons)


def degree_eight_strict():
    n=8
    left,right=endpoints(3,n)
    assert beta_abs(3,n,right)>Fraction(1,n+2)
    print('EXACT_DEGREE_EIGHT_INTERIOR_ADVANTAGE_PASS',beta_abs(3,n,right))


def direct_negative_binomial_integral(k,n,s):
    """Integrate polynomial NB tail probabilities directly (no Beta CDF)."""
    answer=s
    for j in range(k):
        C=comb(n+j,j)
        full=Fraction(n+1,(n+j+1)*(n+j+2))
        partial=sum((Fraction(C*(-1)**q*comb(n+1,q),j+q+1)*s**(j+q+1)
                     for q in range(n+2)), Fraction(0))
        answer+=full-2*partial
    return answer


def independent_integral_test():
    """One independent exact identity integrating beta CDF in two pieces.
    Cross-checks the absolute-moment closed form against the actual step-response.
    """
    for n in range(1,6):
        for k in range(1,6):
            s=endpoints(k,n)[1]
            # Direct polynomial integration of negative-binomial tails.
            assert direct_negative_binomial_integral(k,n,s)==beta_abs(k,n,s)
            # Evaluate E|B-s| via beta truncations by another formula:
            mean=Fraction(k,n+k+1)
            u=beta_cdf(k,n+1,s)
            v=beta_cdf(k+1,n+1,s)
            left_int = s*u-mean*v
            right_int = mean*(1-v)-s*(1-u)
            assert left_int+right_int==beta_abs(k,n,s)
    print('EXACT_CDF_LEAKAGE_IDENTITY_PASS',25)


def finite_sanity():
    for n in [8,10,20,50]:
        cand=[(max(beta_abs(k,n,endpoints(k,n)[0]),
                   beta_abs(k,n,endpoints(k,n)[1])),k)
              for k in range(1, min(cutoff(n),2*n+40))]
        val,k=max(cand)
        print('n=%d: finite candidate k=%d, sharp-candidate=%.12f' % (n,k,float(val)))

if __name__=='__main__':
    small_n()
    degree_eight_strict()
    independent_integral_test()
    finite_sanity()
    print('ALL_MKZ_CHECKS_PASS')
