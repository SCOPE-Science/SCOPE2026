#!/usr/bin/env python3
"""Exact checks for ternary length-three-palindrome-avoiding deletion spectra.

Requires Python 3 and SymPy for the symbolic identity; no external data.
"""
from collections import Counter
from itertools import product
import sympy as sp

STATES = ((0,0,1,1),(0,0,1,2),(0,1,1,0),
          (0,1,1,2),(0,1,2,0),(0,1,2,2))

def canonical(t):
    lookup = {}
    return tuple(lookup.setdefault(a, len(lookup)) for a in t)

def spectrum_direct(n):
    counts = Counter()
    for x in product(range(3), repeat=n):
        if any(x[i] == x[i+2] for i in range(n-2)):
            continue
        shadow = set()
        for i in range(n):
            y = x[:i] + x[i+1:]
            if not any(y[j] == y[j+2] for j in range(n-3)):
                shadow.add(y)
        counts[len(shadow)] += 1
    return counts

def polynomial_spectrum(n):
    # Orbit-reduced transfer; each length-four equality class has six labelings.
    if n <= 3:
        return {1:Counter({1:3}), 2:Counter({1:3,2:6}),
                3:Counter({2:12,3:6})}[n]
    row = [Counter() for _ in STATES]
    for j,t in enumerate(STATES):
        row[j][1+int(t[1] != t[0] and t[0] != t[3])] = 6
    for length in range(4,n):
        nex = [Counter() for _ in STATES]
        for j,t in enumerate(STATES):
            p = len(set(t))
            for a in range(p+1):
                multiplicity = 1 if a < p else 3-p
                if not multiplicity or a == t[2]:
                    continue
                k=STATES.index(canonical(t[1:]+(a,)))
                inc = int(t[2]!=t[1] and t[0]!=t[3] and t[1]!=a)
                for deg,count in row[j].items():
                    nex[k][deg+inc] += count*multiplicity
        row = nex
    final = Counter()
    for t,polynomial in zip(STATES,row):
        tail = int(t[2]!=t[1] and t[0]!=t[3])+int(t[3]!=t[2])
        for deg,count in polynomial.items():
            final[deg+tail]+=count
    return final

def target_max(n):
    return (2*n+3)//3  # ceiling((2n+1)/3)

def target_count(n):
    if n == 1: return 3
    h,r=divmod(n,3)
    return (6,3*h*(h+1)+12,6*(h+1))[r]

def main():
    z,u = sp.symbols('z u')
    M=sp.zeros(6)
    V=sp.zeros(1,6)
    T=sp.zeros(6,1)
    for j,t in enumerate(STATES):
        V[0,j]=6*u**(1+int(t[1]!=t[0] and t[0]!=t[3]))
        T[j,0]=u**(int(t[2]!=t[1] and t[0]!=t[3])+int(t[3]!=t[2]))
        p=len(set(t))
        for a in range(p+1):
            mult=1 if a<p else 3-p
            if not mult or a==t[2]:continue
            k=STATES.index(canonical(t[1:]+(a,)))
            inc=int(t[2]!=t[1] and t[0]!=t[3] and t[1]!=a)
            M[j,k] += mult*u**inc
    Q=1-z-(1+u)*z**2+(1-u**2)*z**3+(u**2-1)*z**4
    R=(1-z-z**2+z**3-z**4
        +u*(2*z-z**2+2*z**4)
        +u**2*(2*z**2-z**3-z**4))
    claimed=3*u*z*(1+z)*R/Q
    obtained=(3*u*z+(3*u+6*u**2)*z**2
              +(12*u**2+6*u**3)*z**3
              +z**4*(V*(sp.eye(6)-z*M).inv()*T)[0])
    assert sp.cancel(obtained-claimed)==0, 'rational-function identity'
    assert sp.factor(claimed.subs(u,1)-(3*z+9*z*z/(1-2*z)))==0
    for n in range(1,17):
        transfer=polynomial_spectrum(n)
        assert sum(transfer.values())==(3 if n==1 else 9*2**(n-2))
        assert max(transfer)==target_max(n)
        assert transfer[max(transfer)]==target_count(n)
        if n<=13:
            direct=spectrum_direct(n)
            assert direct==transfer, (n,direct,transfer)
    # Check the rational recurrence beyond the independently enumerated sizes.
    p = [None] + [sp.Poly.from_dict({(d,):v for d,v in polynomial_spectrum(n).items()},u).as_expr()
                  for n in range(1,27)]
    N=sp.Poly(sp.expand(3*u*z*(1+z)*R),z)
    for n in range(7,27):
        residue=sp.expand(p[n]-p[n-1]-(1+u)*p[n-2]
                          -(u**2-1)*p[n-3]-(1-u**2)*p[n-4])
        assert residue==0, (n,residue)
    print('PASS: exact symbolic six-state resolvent / rational identity')
    print('PASS: independent direct deletion spectrum through length 13')
    print('PASS: six-state spectra / maximum / optimizer count through length 16')
    print('PASS: polynomial recurrence through length 26')

if __name__=='__main__':main()
