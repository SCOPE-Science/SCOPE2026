#!/usr/bin/env python3
"""Exact rational zetas for period-one and period-dividing-two cyclic ECA words.
Dependencies: Python 3, SymPy. Prints a reproducible 256-row summary.
"""
import sympy as sp
import csv
from pathlib import Path
from collections import Counter

def bit(r,a,b,c):return (r>>(4*a+2*b+c))&1

def matrix(r,k):
    m=sp.zeros(1<<k)
    for v in range(1<<k):
        for e in (0,1):
            bits=[(v>>(k-1-j))&1 for j in range(k)]+[e]
            if k==2:
                valid=bit(r,*bits)==bits[1]
            else:
                next_bits=[bit(r,*bits[j:j+3]) for j in range(3)]
                valid=bit(r,*next_bits)==bits[2]
            if valid:m[v,((v<<1)&((1<<k)-1))|e]+=1
    return m

def det_coeffs(mat):
    x=sp.Symbol('x')
    # det(I-zA), computed exactly from the characteristic polynomial.
    a=list(map(int,mat.charpoly(x).all_coeffs()))
    while len(a)>1 and a[-1]==0:a.pop()
    return tuple(a)

def trace_from_det(coeffs,nmax):
    # Newton identities: t_n + a_1 t_{n-1}+...+a_{n-1}t_1+n*a_n=0.
    t=[0]*(nmax+1)
    for n in range(1,nmax+1):
        t[n]=-sum(coeffs[j]*t[n-j] for j in range(1,min(n,len(coeffs)-1)+1))
        if n<len(coeffs):t[n]-=n*coeffs[n]
    return t

def brute(rule,n):
    counts=[0,0]
    for integer in range(1<<n):
        a=tuple((integer>>j)&1 for j in range(n))
        def step(w):
            return tuple(bit(rule,w[(i-1)%n],w[i],w[(i+1)%n]) for i in range(n))
        b=step(a)
        if a==b:counts[0]+=1
        if a==step(b):counts[1]+=1
    return counts

def first_two(rule):
    for n in range(1,7):
        fixed,periodtwo=brute(rule,n)
        if periodtwo>fixed:return n
    return None

def main():
    data={}
    for r in range(256):
        p=det_coeffs(matrix(r,2));q=det_coeffs(matrix(r,4))
        c=trace_from_det(p,9);d=trace_from_det(q,9)
        for n in range(1,10):
            assert [c[n],d[n]]==brute(r,n),('trace mismatch',r,n)
            assert (d[n]-c[n])%2==0 and d[n]>=c[n]
        data[r]=(p,q,first_two(r))
    assert len({p for p,q,n in data.values()})==23
    assert len({q for p,q,n in data.values()})==40
    assert len({(p,q) for p,q,n in data.values()})==51
    with (Path(__file__).parent/'rule_table.csv').open(newline='',encoding='utf-8') as handle:
        rows=list(csv.DictReader(handle))
    assert len(rows)==256
    for row in rows:
        rule=int(row['rule']);p,q,n=data[rule]
        assert row['first_primitive_two_ring']==('none' if n is None else str(n))
        assert row['det_I_minus_zA_coefficients']==';'.join(map(str,p))
        assert row['det_I_minus_zB_coefficients']==';'.join(map(str,q))
        witness=row['witness_bits']
        if n is None:
            assert not witness
        else:
            assert len(witness)==n and set(witness)<={'0','1'}
            word=tuple(map(int,witness))
            def once(x):return tuple(bit(rule,x[(j-1)%n],x[j],x[(j+1)%n]) for j in range(n))
            assert once(word)!=word and once(once(word))==word
    assert sum(p==q for p,q,n in data.values())==107
    c=Counter('none' if n is None else n for p,q,n in data.values())
    assert c==Counter({'none':107,1:64,2:48,3:6,4:17,5:2,6:12})
    print('rules=256; exact trace vs direct bitwise dynamics: 256*9=2304 cases')
    print('distinct zeta polynomials: one-step=23, two-step=40, joint=51')
    print('full 256-row polynomial table and temporal-two witnesses checked')
    print('rules with no primitive two-cycle=107; first periods: 1=64, 2=48, 3=6, 4=17, 5=2, 6=12')
    print('PASS')

if __name__=='__main__':main()
