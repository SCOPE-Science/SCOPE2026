#!/usr/bin/env python3
"""Exact finite certificate for period-two binary, four-site number-conserving maps.

All computations use integer arithmetic / exact rational Gaussian elimination.
This file needs only the Python standard library and collision_witnesses.json.
"""
import itertools
import json
from fractions import Fraction
from collections import Counter
from pathlib import Path

BITS = (0, 1)

def rule_bit(rule, bits):
    a, b, c, d = bits
    return (rule >> (8*a + 4*b + 2*c + d)) & 1

def apply_ring(f, g, x):
    n = len(x)
    return tuple(rule_bit(f if i % 2 == 0 else g,
                          (x[(i-1)%n], x[i], x[(i+1)%n], x[(i+2)%n]))
                 for i in range(n))

def conservation_matrix(n):
    rows = []
    for x in itertools.product(BITS, repeat=n):
        row = [0] * 33
        for i in range(n):
            t = 8*x[(i-1)%n]+4*x[i]+2*x[(i+1)%n]+x[(i+2)%n]
            row[16*(i%2)+t] += 1
        row[-1] = sum(x)
        rows.append(row)
    return rows

def flip_matrix():
    rows=[]
    for parity in BITS:
        for x,y,z,u,w,t in itertools.product(BITS,repeat=6):
            row=[0]*33
            for phase,high,low in (
                (parity,(x,y,z,1),(x,y,z,0)),
                (1-parity,(y,z,1,u),(y,z,0,u)),
                (parity,(z,1,u,w),(z,0,u,w)),
                (1-parity,(1,u,w,t),(0,u,w,t))):
                row[16*phase+8*high[0]+4*high[1]+2*high[2]+high[3]]+=1
                row[16*phase+8*low[0]+4*low[1]+2*low[2]+low[3]]-=1
            row[32]=1
            rows.append(row)
    # Double quiescence is enough for the zero reference configuration.
    # More simply enforce both constant outputs: f(0000)=g(0000)=0,
    # f(1111)=g(1111)=1, in this exact binary problem.
    for j,v in ((0,0),(16,0),(15,1),(31,1)):
        row=[0]*33;row[j]=1;row[32]=v;rows.append(row)
    return rows

def rref_int(rows):
    a=[[Fraction(x) for x in row] for row in rows]
    piv=[];h=0
    for c in range(32):
        chosen=next((i for i in range(h,len(a)) if a[i][c]),None)
        if chosen is None: continue
        a[h],a[chosen]=a[chosen],a[h]
        d=a[h][c];a[h]=[v/d for v in a[h]]
        for i in range(len(a)):
            if i!=h and a[i][c]:
                mul=a[i][c]
                a[i]=[v-mul*w for v,w in zip(a[i],a[h])]
        piv.append(c);h+=1
    assert all(not any(row[:32]) or not row[32] for row in a[h:]),'inconsistent'
    return a[:h],piv

def boolean_solutions(rows):
    red,piv=rref_int(rows)
    free=[i for i in range(32) if i not in piv]
    output=set()
    for mask in range(1<<len(free)):
        vec=[0]*32
        for k,j in enumerate(free):vec[j]=(mask>>k)&1
        good=True
        for line,j in zip(red,piv):
            t=line[32]-sum(line[k]*vec[k] for k in free)
            if t!=0 and t!=1:
                good=False;break
            vec[j]=int(t)
        if good:
            f=sum(vec[j]<<j for j in range(16))
            g=sum(vec[16+j]<<j for j in range(16))
            output.add((f,g))
    return output,len(piv),len(free)

def main():
    # Two independent finite formulations: all 256 length-eight binary rings,
    # and all 128 local single-site flip equations plus constant states.
    S,r,free=boolean_solutions(conservation_matrix(8))
    assert (r,free,len(S))==(17,15,174),(r,free,len(S))
    T,r2,free2=boolean_solutions(flip_matrix())
    assert S==T and len(S)==174,(len(S),len(T),len(S^T))
    assert all(all(sum(apply_ring(f,g,x))==sum(x) for x in itertools.product(BITS,repeat=n))
               for f,g in S for n in (2,4,6,8)), 'failed small-ring conservation'
    witnesses=json.loads((Path(__file__).parent/'collision_witnesses.json').read_text())
    keys=set()
    hist=Counter()
    for w in witnesses:
        f,g,n=w['f'],w['g'],w['n']
        a=tuple(int(c) for c in w['a']);b=tuple(int(c) for c in w['b'])
        assert (f,g) in S and (f,g) not in keys
        assert n in (2,4,6) and len(a)==len(b)==n and a!=b
        assert apply_ring(f,g,a)==apply_ring(f,g,b)
        keys.add((f,g));hist[n]+=1
    expected={(0xAAAA,0xAAAA),(0xAAAA,0xF0F0),(0xCCCC,0xCCCC),(0xCCCC,0xFF00),
              (0xF0F0,0xAAAA),(0xF0F0,0xF0F0),(0xFF00,0xCCCC),(0xFF00,0xFF00)}
    assert S-keys==expected and len(keys)==166,(len(S-keys),len(keys))
    # Each surviving map is a parity-preserving or parity-swapping
    # permutation of the spatial sites, hence invertible on any even ring
    # and on the bilateral lattice.
    offs={0xFF00:-1,0xF0F0:0,0xCCCC:1,0xAAAA:2}
    for f,g in expected:
        o1,o2=offs[f],offs[g]
        assert o1%2 == o2%2
        for n in (2,4,6,8,10):
            images=[(i+(o1 if i%2==0 else o2))%n for i in range(n)]
            assert len(set(images))==n
    print('exact-rational rank 17, free 15; 174 ordered conserving pairs')
    print('independent flip-system enumeration agrees exactly')
    print('166 explicit nonreversible collision certificates',dict(sorted(hist.items())))
    print('8 surviving pairs are reversible spatial site permutations')
    print('all required checks PASS')
if __name__=='__main__':main()
