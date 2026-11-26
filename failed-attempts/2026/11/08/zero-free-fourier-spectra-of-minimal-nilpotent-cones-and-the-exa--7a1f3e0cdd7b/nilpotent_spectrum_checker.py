"""Exact additive Fourier checks for the rank-at-most-one square-zero 3x3 matrix cone.
Usage: python nilpotent_spectrum_checker.py
Only Python and numpy are required. Frequency vectors are in row-major order.
"""
import itertools
from collections import Counter
import numpy as np


def run(q, full):
    if q not in (2, 3, 4, 5):
        raise ValueError('Supported test fields: 2, 3, 4, 5')
    elems = list(range(q))
    if q == 4:
        add = lambda a,b: a ^ b
        def mul(a,b):
            r=0
            for k in range(2):
                if (b >> k) & 1: r ^= a << k
            for k in (2,):
                if (r >> k) & 1: r ^= 0b111 << (k-2)
            return r
        trace = lambda a: a ^ mul(a,a)  # always 0 or 1
        sign = lambda a: 1 if trace(a)==0 else -1
    else:
        add = lambda a,b: (a+b)%q
        mul = lambda a,b: (a*b)%q
        sign = lambda a: None
    def dot(x,y):
        r=0
        for a,b in zip(x,y):r=add(r,mul(a,b))
        return r
    v3=list(itertools.product(elems,repeat=3))
    zero=(0,0,0)
    vectors=[v for v in v3 if v !=zero]
    def line(v):
        return tuple(tuple(mul(c,z) for z in v) for c in elems[1:])
    visited=set()
    lines=[]
    for v in vectors:
        if v not in visited:
            lines.append(v)
            visited.update(line(v))
    assert len(lines)==q*q+q+1
    S={tuple([0]*9)}
    for u in vectors:
        for v in v3:
            if dot(u,v)==0:
                S.add(tuple(mul(u[i],v[j]) for i in range(3) for j in range(3)))
    assert len(S)==q**4+q**3-q
    S=sorted(S)
    freq = list(itertools.product(elems,repeat=9)) if full else None
    if not full:
        rng=np.random.default_rng(213051)
        freq=[(0,)*9]+[tuple(int(i) for i in x) for x in rng.integers(0,q,size=(700,9))]
    observed=Counter()
    for a in freq:
        E=0
        for u in lines:
            Au=tuple(dot(a[3*i:3*i+3],u) for i in range(3))
            if any(Au==tuple(mul(c,z) for z in u) for c in elems):E+=1
        expected=q*q*E-q*(q+1)
        counts=[0]*q
        for s in S:
            t=dot(a,s)
            counts[t]+=1
        if q==2:
            actual=counts[0]-counts[1]
        elif q==3:
            assert counts[1]==counts[2], (q,a,counts)
            actual=counts[0]-counts[1]
        elif q==4:
            actual=sum(counts[t]*sign(t) for t in elems)
        else:
            # Integral Fourier coefficients force equal counts at all nonzero residues.
            assert len(set(counts[1:]))==1, (q,a,counts)
            actual=counts[0]-counts[1]
        assert actual==expected,(q,a,E,counts,expected,actual)
        assert actual!=0
        observed[E]+=1
    if full:
        G=(q**3-1)*(q**3-q)*(q**3-q**2)
        table={
            0:(q**3-q)*G//(3*(q**3-1)),
            1:G//(q*(q-1))+q*q*G//(2*(q*q-1)),
            2:G//(q-1),
            3:q*(q-1)*(q-2)*G//(6*(q-1)**3),
            q+1:q*(q**3-1)*(q+1),
            q+2:q**3*(q**3-1),
            q*q+q+1:q
        }
        # For q=2, the label '3' overlaps q+1, and use additive multiplicities.
        if q==2:
            table[3]=q*(q**3-1)*(q+1)
        assert sum(table.values())==q**9,table
        assert Counter({k:v for k,v in table.items() if v})==observed,(q,table,observed)
    print('PASS', 'exhaustive' if full else 'sampled','field',q,'frequencies',len(freq),'orbit_size',len(S),'E_counts',dict(sorted(observed.items())))

if __name__=='__main__':
    for q,full in [(2,True),(3,True),(4,False),(5,False)]:run(q,full)
    print('ALL_MINIMAL_NILPOTENT_SPECTRUM_CHECKS_OK')
