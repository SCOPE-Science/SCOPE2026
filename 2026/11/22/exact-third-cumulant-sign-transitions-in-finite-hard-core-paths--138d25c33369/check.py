"""Exact finite-instance checks for open-chain hard-core triple correlations.
Run with Python 3 standard library: python check.py
These checks supplement (and do not replace) the all-length argument.
"""
from fractions import Fraction
from itertools import combinations


def independent_masks(n):
    return [s for s in range(1 << n) if not (s & (s << 1))]


def exact_moments(n, lam):
    masks = independent_masks(n)
    weights = [lam ** s.bit_count() for s in masks]
    z = sum(weights)
    def mean(*sites):
        bit = sum(1 << (i-1) for i in sites)
        return sum(w for s, w in zip(masks, weights) if s & bit == bit) / z
    return mean


def polynomials(n, lam):
    p = [Fraction(1), 1+lam]
    for i in range(2,n+1):
        p.append(p[-1] + lam*p[-2])
    return p


def run():
    triple_count = 0
    ratio_count = 0
    for n in range(3,11):
        for lam in (Fraction(1,3), Fraction(1), Fraction(3), Fraction(10), Fraction(100)):
            mean = exact_moments(n,lam)
            p = [None]+[mean(i) for i in range(1,n+1)]
            p_pol = polynomials(n,lam)
            for j in range(1,n+1):
                expected = lam*(p_pol[j-2] if j>=2 else Fraction(1)) * \
                    (p_pol[n-j-1] if n-j>=1 else Fraction(1))/p_pol[n]
                assert p[j] == expected, ('one-site formula',n,j,lam)
            for i,j,k in combinations(range(1,n+1),3):
                pi,pj,pk=p[i],p[j],p[k]
                cov_ij=mean(i,j)-pi*pj
                cov_jk=mean(j,k)-pj*pk
                kappa=(mean(i,j,k)-mean(i,j)*pk-mean(i,k)*pj-
                       mean(j,k)*pi+2*pi*pj*pk)
                predicted = cov_ij*cov_jk*(1-2*pj)/(pj*(1-pj))
                assert kappa == predicted, ('triple factor',n,i,j,k,lam)
                assert (cov_ij >0)-(cov_ij<0) == (-1)**(j-i)
                assert (cov_jk >0)-(cov_jk<0) == (-1)**(k-j)
                triple_count += 1
    for n in range(3,15):
        for x in (Fraction(1,5), Fraction(1,2), Fraction(3,4)):
            lam=x/(1-x)**2
            p_pol=polynomials(n,lam)
            for j in range(1,n+1):
                num=lam*(p_pol[j-2] if j>=2 else Fraction(1))* \
                     (p_pol[n-j-1] if n-j>=1 else Fraction(1))
                p=num/p_pol[n]
                b=n-j+1
                odds=x*(1-(-x)**j)*(1-(-x)**b)/((1-(-x)**(j+1))*(1-(-x)**(b+1)))
                assert odds==p/(1-p), ('odds identity',n,j,x)
                ratio_count+=1
    n,j=5,3
    def root_polynomial(z):
        pp=polynomials(n,Fraction(z))
        return 2*z*pp[j-2]*pp[n-j-1]-pp[n]
    assert root_polynomial(3)<0 and root_polynomial(4)>0
    print('EXACT_CHECKS_PASSED', triple_count, ratio_count, 'five-site threshold bracket (3,4)')

if __name__=='__main__': run()
