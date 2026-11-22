#!/usr/bin/env python3
"""Independent truth-table and bias-sensitive checks of q-ary NOR tree laws."""
from fractions import Fraction
from itertools import product


def tree_value(bits, q):
    length = len(bits)
    assert length >= 1
    a = list(bits)
    while len(a) > 1:
        assert len(a) % q == 0
        a = [int(not any(a[j:j+q])) for j in range(0, len(a), q)]
    return a[0]


def count_trees(q, t):
    n = q ** t
    assert n <= 9
    a = sum(tree_value(x, q) for x in product((0,1), repeat=n))
    return a, (2**n-a)


def verify():
    for q,tmax in [(2,3),(3,2),(4,1)]:
        a,b=1,1
        for t in range(tmax+1):
            assert (a,b) == count_trees(q,t)
            if t<tmax:
                a, b = b**q, 2**(q**(t+1))-b**q
        print(f'q={q}: tree truth tables through depth {tmax}: PASS')
    # For a q=2,d=3 de Bruijn graph, disjoint word-prefix blocks of length 2**t
    # give the exact Bernoulli(1/3) first-entry CDF. Weighted enumeration is exact.
    q,d,p=2,3,Fraction(1,3)
    for t in range(d+1):
        probs=[]
        for bits in product((0,1), repeat=q**d):
            outcomes=[]
            block_size=q**t
            for i in range(0,len(bits),block_size):
                outcomes.append(tree_value(bits[i:i+block_size],q))
            probs.append((int(all(x==0 for x in outcomes) or all(x==1 for x in outcomes)),p**sum(bits)*(1-p)**(len(bits)-sum(bits))))
        observed=sum((indicator*weight for indicator,weight in probs),Fraction())
        pp=p
        for j in range(t): pp=(1-pp)**q
        expected=pp**(q**(d-t))+(1-pp)**(q**(d-t))
        assert observed==expected,(t,observed,expected)
        print(f'biased q=2 d=3 t={t} CDF={observed} PASS')
    print('independent_truth_tables: PASS')

if __name__=='__main__': verify()
