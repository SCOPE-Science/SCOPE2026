"""Standalone exact cross-check for the q-ary two-deletion descendant law.

Requires Python 3.9+ standard library only. Every descendant is materialized
independently of the transition-pattern formula.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb


def actual_ball(x):
    n = len(x)
    return len({x[:i]+x[i+1:j]+x[j+1:] for i in range(n) for j in range(i+1,n)})


def run_formula(x):
    runs = []
    for a in x:
        if not runs or runs[-1][0] != a:
            runs.append([a,1])
        else:
            runs[-1][1] += 1
    r = len(runs)
    long_runs = sum(t>=2 for _,t in runs)
    returns = sum(x[i-1]==x[i+1]!=x[i] for i in range(1,len(x)-1))
    return comb(r,2)+long_runs-returns


def predicted_counts(q,n):
    """Integer coefficient enumeration, without constructing source words."""
    out=Counter()
    for a in product((0,1),repeat=n-1):
        k=sum(a)
        s=(1-a[0])+sum(a[i-1]*(1-a[i]) for i in range(1,len(a)))
        h=sum(a[i-1]*a[i] for i in range(1,len(a)))
        for t in range(h+1):
            ways=q*(q-1)**(k-h)*comb(h,t)*(q-2)**(h-t)
            out[comb(k+1,2)+s-t]+=ways
    return +out



def matrix_counts(q,n):
    """Independent sparse transfer implementation of the two-state polynomial."""
    # State: previous edge, transition count, long-run count, return count.
    d={(0,0,1,0):q,(1,1,0,0):q*(q-1)}
    for _ in range(2,n):
        nxt=Counter()
        for (prev,k,s,t),c in d.items():
            nxt[(0,k,s+prev,t)]+=c
            if prev==0:
                nxt[(1,k+1,s,t)]+=c*(q-1)
            else:
                nxt[(1,k+1,s,t)]+=c*(q-2)
                nxt[(1,k+1,s,t+1)]+=c
        d=nxt
    out=Counter()
    for (_,k,s,t),c in d.items():
        if c: out[comb(k+1,2)+s-t]+=c
    return +out


def actual_counts(q,n):
    out=Counter()
    for x in product(range(q),repeat=n):
        b=actual_ball(x)
        assert b == run_formula(x), (q,n,x,b,run_formula(x))
        out[b]+=1
    return out


def predicted_variance(q,n):
    m=n-1
    return Fraction((m-1)*(q-1)*(2*m*m*(q-1)**2-m*(q-1)*(2*q-3)+2*q*(q-2)),2*q**4)


def predicted_mean(q,n):
    return Fraction(1+n*(q-1)+comb(n,2)*(q-1)**2,q**2)


def test_distribution(h,q,n):
    assert sum(h.values()) == q**n
    e=Fraction(sum(b*c for b,c in h.items()),q**n)
    v=Fraction(sum(b*b*c for b,c in h.items()),q**n)-e**2
    assert e == predicted_mean(q,n),(q,n,e,predicted_mean(q,n))
    assert v == predicted_variance(q,n),(q,n,v,predicted_variance(q,n))


def main():
    checked=0
    for q,max_n in ((2,12),(3,8),(4,7),(5,6),(7,5)):
        for n in range(2,max_n+1):
            p=predicted_counts(q,n)
            actual=actual_counts(q,n)
            assert p==actual,(q,n,p,actual)
            assert p==matrix_counts(q,n),(q,n,p,matrix_counts(q,n))
            test_distribution(p,q,n)
            checked+=1
        print(f'q={q}, all lengths 2..{max_n}: complete histograms and moments match')
    for q in (2,3,4,5,8):
        for n in range(2,14):
            test_distribution(predicted_counts(q,n),q,n)
            assert matrix_counts(q,n)==predicted_counts(q,n)
    print(f'PASS: {checked} independent word-enumeration cases; 60 edge-law and transfer moment tests')
    for q,n in ((3,5),(4,6)):
        print(f'q={q}, n={n}:',sorted(predicted_counts(q,n).items()))


if __name__=='__main__':
    main()
