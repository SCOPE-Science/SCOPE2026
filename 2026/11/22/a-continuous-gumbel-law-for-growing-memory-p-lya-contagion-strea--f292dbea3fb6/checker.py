#!/usr/bin/env python3
"""Exact rational cross-checks for finite-memory reinforced Bernoulli streaks.
This finite checker is supplemental to, not a substitute for, the analytical theorem.
"""
from fractions import Fraction
from itertools import product
from math import prod

def poch(x,k):
    return prod((x+i for i in range(k)), start=1)

def exact_word_probability(word, a, b, M):
    c=a+b
    s=0
    ones=0
    for i,bit in enumerate(word):
        if i<M:
            p=Fraction(a+ones,c+i)
        else:
            p=Fraction(a+sum(word[i-M:i]),c+M)
        s += bit
        ones += bit
        if i==0: val=Fraction(1)
        val *= p if bit else (1-p)
    return val

def run():
    tests=0
    for M in range(1,5):
      for a in (1,2,3):
       for b in (1,2,3):
        c=a+b
        q=Fraction(a+M,c+M)
        U=Fraction(poch(a,M),poch(c,M))
        for length in range(M,M+5):
            # all-one word probability and one preceding zero under stationary initialization
            one_word=(1,)*length
            p1=exact_word_probability(one_word,a,b,M)
            assert p1==U*q**(length-M),(M,a,b,length,p1)
            tests+=1
            p01=exact_word_probability((0,)+one_word,a,b,M)
            assert p01==U*(1-q)*q**(length-M),(M,a,b,length,p01)
            tests+=1
        # Every M-block has the beta mixture law; verify block shift invariance
        for state in product((0,1),repeat=M):
            expected=Fraction(poch(a,sum(state))*poch(b,M-sum(state)),poch(c,M))
            got=exact_word_probability(state,a,b,M)
            assert got==expected,(state,M,a,b,got,expected)
            incoming=Fraction(0)
            for first in (0,1):
                incoming+=exact_word_probability((first,)+state,a,b,M)
            assert incoming==expected,(M,a,b,state,incoming,expected)
            tests+=2
        # Sum of all length-M+2 probabilities equals one
        total=sum((exact_word_probability(s,a,b,M) for s in product((0,1),repeat=M+2)),Fraction())
        assert total==1
        tests+=1
    print('PASS:',tests,'exact-rational assertions; finite enumeration is not an infinite proof')

if __name__=='__main__':run()
