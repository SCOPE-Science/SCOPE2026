#!/usr/bin/env python3
"""Exact checks for two-round zero-forcing completion on K_{2,b}.

Requires only the Python standard library. Its finite tests complement,
not replace, the analytic all-b and spectral-radius arguments.
"""
from fractions import Fraction as F
from math import comb


def two_round_small(b):
    return sum((F(comb(b,j),b**j)*F(b-1,b)**(b-j)*F(j+1,b)**(b-j)
                for j in range(1,b+1)), F(0))


def two_round_large(b):
    return F(1,2)*F(2,b)**(b-1)+F(1,4)*F(4*(b-1),b*b)**(b-1)


def exact_integer_difference(b):
    a=sum(comb(b,j)*((b-1)*(j+1))**(b-j)*b**(j-1)
          for j in range(1,b+1))
    z=2**(b-2)*b**b+4**(b-2)*(b-1)**(b-1)*b
    assert F(a-z,b**(2*b-1)) == two_round_small(b)-two_round_large(b)
    return a-z


def all_states_step(n_b, state):
    """Direct labeled-vertex transitions, independent of the two-count reduction."""
    n=n_b+2
    neighbors=[tuple(range(2,n)),tuple(range(2,n))]+[(0,1)]*n_b
    blues=[i for i in range(n) if (state>>i)&1]
    white=[i for i in range(n) if not ((state>>i)&1)]
    qs=[]
    for v in white:
        fail=F(1)
        for u in blues:
            if v in neighbors[u]:
                active=1+sum(1 for w in neighbors[u] if (state>>w)&1)
                fail *= 1-F(active,len(neighbors[u]))
        qs.append(1-fail)
    for m in range(1<<len(white)):
        dest=state
        p=F(1)
        for k,v in enumerate(white):
            if (m>>k)&1:
                dest |= 1<<v
                p *= qs[k]
            else:
                p *= 1-qs[k]
        if p: yield dest,p


def labeled_two_round(b,start):
    d={1<<start:F(1)}
    for _ in range(2):
        nxt={}
        for mask,p in d.items():
            for dest,q in all_states_step(b,mask):
                nxt[dest]=nxt.get(dest,F(0))+p*q
        d=nxt
        assert sum(d.values())==1
    return d.get((1<<(b+2))-1,F(0))


def main():
    for b in range(3,16):
        d=exact_integer_difference(b)
        assert d>0,(b,d)
    print('13 exact positive two-round differences (b=3,...,15)')
    for b in range(3,8):
        assert labeled_two_round(b,0)==two_round_small(b)
        assert labeled_two_round(b,2)==two_round_large(b)
    print('10 independent labeled-state/two-count identities (b=3,...,7)')
    for b in range(3,101):
        la=F(b-1,b)**b
        assert la>F(1,4)
        for y in range(1,b):
            w=b-y
            stay=F(w-1,b)**(2*w)
            assert stay<F(1,4)
    print('98 exact spectral comparisons plus all descendants (b=3,...,100)')
    for m in range(7,41):
        even_lower=F(m**(m-1),3*(2*m+1)*2**(2*m-3))
        assert even_lower>1
    for m in range(8,41):
        odd_lower=F(4*(2*m+1)**(m-1),3*(m+1)*2**(3*m))
        assert odd_lower>1
    print('central-binomial inequality bounds checked at starts and through m=40')
    print('b=3 exact CDFs',two_round_small(3),two_round_large(3))
    print('All tests passed.')

if __name__=='__main__':
    main()
