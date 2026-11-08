#!/usr/bin/env python3
"""Exact near-endpoint trinomial coefficients and Poisson-window convergence.
Reports exact integer identities and analytical binomial event probabilities;
finite computations are illustrative, not proofs of infinite asymptotics.
"""
from math import comb, factorial, exp, log1p

def endpoint(n,d):
    return sum(comb(n,a)*comb(n-a,d-2*a) for a in range(d//2+1))

def main():
    for s in range(3):
        for n in range(12+s,30,3):
            assert n%3==s
            m=n-s
            pnum=2*endpoint(n,s)
            qnum=2*endpoint(n,s+3)
            den=3**(n-1)
            r=(3**n)//(n**s)
            if r:
                p=pnum/den;q=qnum/den
                assert p>0 and q>0
                pt= -__import__('math').expm1(r*log1p(-p))
                p2=exp(r*log1p(-p)) - exp(r*log1p(-p-q))
                print('CHECK',n,'residue',s,'r',r,'max_prob',round(pt,9),
                      'second_prob',round(p2,9),'limit_max',round(1-exp(-6/factorial(s)),9),
                      'coefficient_rescaled',round(pnum*3**n/(den*n**s),8))
    print('CRITICAL_FINITE_FORMULAS_PASS')

if __name__=='__main__':main()
