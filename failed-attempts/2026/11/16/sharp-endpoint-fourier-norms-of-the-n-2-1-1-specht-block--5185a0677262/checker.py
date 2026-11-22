#!/usr/bin/env python3
"""Exact checks for the hook Specht-block Fourier endpoint norm.

Standard-library-only Python 3 program. The independent exhaustive permutation
path is separate from the rational two-short-cycle count path.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial


def no_one_two_cycles(m):
    """Number of permutations of m points with no 1- or 2-cycles."""
    value = sum((Fraction((-1)**(a+b)*factorial(m),
                          factorial(a)*2**b*factorial(b))
                 for a in range(m+1)
                 for b in range((m-a)//2+1)), Fraction(0))
    assert value.denominator == 1 and value >= 0
    return int(value)


def count_cycles_one_two(p):
    seen=[False]*len(p); j=k=0
    for i in range(len(p)):
        if seen[i]:
            continue
        t=i; length=0
        while not seen[t]:
            seen[t]=True; length+=1; t=p[t]
        if length==1:
            j+=1
        elif length==2:
            k+=1
    return j,k


def char_hook(j,k):
    return ((j-1)*(j-2))//2-k


def cycle_stat_weights(n):
    """Exact probabilities of (number of 1-cycles, number of 2-cycles)."""
    for j in range(n+1):
        for k in range((n-j)//2+1):
            m=n-j-2*k
            yield (j,k,Fraction(no_one_two_cycles(m),
                                factorial(j)*2**k*factorial(k)*factorial(m)))


def norm_formula(n):
    d=(n-1)*(n-2)//2
    return 2*d*sum((Fraction(max(0,-char_hook(j,k)))*weight
                    for j,k,weight in cycle_stat_weights(n)), Fraction(0))


def norm_bruteforce(n):
    s=0
    for p in permutations(range(n)):
        j,k=count_cycles_one_two(p)
        s+=abs(char_hook(j,k))
    return Fraction((n-1)*(n-2),2)*Fraction(s,factorial(n))


def h_coefficient(m):
    """Coefficient [z^m] exp(-z-z^2/2) F(z), computed independently."""
    total=Fraction(0)
    for j in range(m+1):
        a=(j-1)*(j-2)//2
        for k in range((m-j)//2+1):
            if k<=a:
                continue
            r=m-j-2*k
            for v in range(r//2+1):
                u=r-2*v
                total+=Fraction((k-a)*(-1)**(u+v),
                       factorial(j)*factorial(k)*2**k*factorial(u)*factorial(v)*2**v)
    return total


def run():
    for n in range(4,9):
        assert norm_formula(n)==norm_bruteforce(n), n
        print('n', n, 'norm', norm_formula(n))
    coeff_sum=Fraction(0)
    for n in range(0,16):
        coeff_sum+=h_coefficient(n)
        if n>=4:
            d=(n-1)*(n-2)//2
            assert coeff_sum==norm_formula(n)/(2*d), n
            total_weight=sum((w for _,_,w in cycle_stat_weights(n)),Fraction(0))
            mean=sum((w*char_hook(j,k) for j,k,w in cycle_stat_weights(n)),Fraction(0))
            second=sum((w*char_hook(j,k)**2 for j,k,w in cycle_stat_weights(n)),Fraction(0))
            assert total_weight==1 and mean==0 and second==1, (n,total_weight,mean,second)
    print('HOOK_SPECHT_EXACT_FOURIER_PROJECTION_CHECKS_PASS')

if __name__=='__main__':
    run()
