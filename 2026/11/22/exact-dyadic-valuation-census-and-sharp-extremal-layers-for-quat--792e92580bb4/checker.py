#!/usr/bin/env python3
"""Exact finite cross-checks for the valuation census of 4-ary Fuss-Catalan numbers."""
from collections import Counter
from math import comb
from fractions import Fraction


def valuation(k):
    assert k > 0
    return (k & -k).bit_length() - 1


def v_at(n):
    return (3*n).bit_count() - valuation(3*n+1)


def polynomial_add(*terms):
    z = Counter()
    for a, sign, shift in terms:
        for k, v in a.items():
            z[k+shift] += sign*v
    return Counter({k:v for k,v in z.items() if v})


def recurrence(last):
    a,b,c=last[-1],last[-2],last[-3]
    return polynomial_add((a,1,0),(a,1,1),(b,1,0),(b,-1,1),(b,1,2),
                          (c,-1,0),(c,-1,3))


def transducer_poly(L):
    # state (carry 0,1,2; has any zero been emitted yet)
    d={(0,False,0):1}
    for _ in range(L):
        nd=Counter()
        for (c,seen,e),count in d.items():
            for bit in (0,1):
                y=(3*bit+c)%2
                cc=(3*bit+c)//2
                nd[(cc,seen or y==0,e+int(seen and y==1))]+=count
        d=nd
    out=Counter()
    for (c,seen,e),count in d.items():
        # flush the remaining carry, then remove trailing initial ones
        if seen:
            tail=c.bit_count()
        elif c==2:
            tail=1 # binary 10 creates a zero and then a counted one
        else:
            tail=0
        out[e+tail]+=count
    return out


def run():
    # G(z,t)=(1+(1-t)z-z^2)/((1-(1+t)z)(1-(1-t+t^2)z^2)).
    P=[Counter({0:1}),Counter({0:2}),Counter({0:2,1:1,2:1})]
    assertions=0
    for L in range(14):
        if L>=3:P.append(recurrence(P))
        assert sum(P[L].values())==2**L; assertions+=1
        T=transducer_poly(L)
        assert P[L]==T,(L,P[L],T); assertions+=1
        enum=Counter(v_at(n) for n in range(2**L))
        assert P[L]==enum,(L,P[L],enum); assertions+=1
        assert P[L][0]==L//2+1+(L%2); assertions+=1
        top=2*(L//2)
        assert max(P[L])==top; assertions+=1
        assert P[L][top]==(1 if L%2==0 else L+1);assertions+=1
        mean=Fraction(sum(e*c for e,c in P[L].items()),2**L)
        var=Fraction(sum(e*e*c for e,c in P[L].items()),2**L)-mean**2
        formula_mean=Fraction(L,2)-Fraction(1,3)+Fraction((-1)**L,3*2**L)
        formula_var=Fraction(L,4)+Fraction(2,9)+Fraction(7*(-1)**L,18*2**L)-Fraction(1,2**(L+1))-Fraction(1,9*4**L)
        assert mean==formula_mean; assertions+=1
        assert var==formula_var; assertions+=1
        if L<=8:
            for n in range(2**L):
                exact=comb(4*n,n)//(3*n+1)
                assert valuation(exact)==v_at(n) if n>0 else v_at(n)==0
                assertions+=1
    print('CHECK_OK',assertions,'exact assertions', 'levels=0..13')

if __name__=='__main__':run()
