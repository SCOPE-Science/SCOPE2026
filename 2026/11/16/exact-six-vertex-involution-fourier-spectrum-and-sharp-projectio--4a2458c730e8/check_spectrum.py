#!/usr/bin/env python3
"""Exact independent recurrence for signed involution Walsh coefficients.
All computations are integer arithmetic. No third-party dependencies.
"""
from itertools import combinations
from collections import Counter
from hashlib import sha256
from struct import pack
from fractions import Fraction

EXPECTED_HIST6 = {-24:6,-20:75,-16:465,-12:1740,-8:4105,-4:6348,0:6825,4:5540,8:3570,12:1815,16:963,20:660,24:240,28:100,32:195,36:60,44:45,56:15,76:1}

def fwht(a):
    a=list(a)
    step=1
    while step<len(a):
        for i in range(0,len(a),2*step):
            for j in range(i,i+step):
                x,y=a[j],a[j+step]
                a[j],a[j+step]=x+y,x-y
        step *= 2
    return a

def weights(n):
    edges=list(combinations(range(n),2))
    # For each complete signing, solve the exact monomer--dimer recurrence.
    all_values=[]
    for bits in range(1<<len(edges)):
        signs=[[1]*n for _ in range(n)]
        for j,(u,v) in enumerate(edges):
            signs[u][v]=signs[v][u]=(-1 if (bits>>j)&1 else 1)
        mem={0:1}
        def evaluate(vertices):
            if vertices in mem:
                return mem[vertices]
            bit=vertices & -vertices
            v=bit.bit_length()-1
            rem=vertices^bit
            s=evaluate(rem)
            t=rem
            while t:
                jbit=t&-t; j=jbit.bit_length()-1
                s+=signs[v][j]*evaluate(rem^jbit)
                t^=jbit
            mem[vertices]=s
            return s
        all_values.append(evaluate((1<<n)-1))
    return edges,all_values

def main():
    for n,z,d in [(3,3,2),(4,0,2),(5,0,2),(6,6825,4)]:
        edges,w=weights(n)
        hist=Counter(w)
        assert hist[0]==z
        assert min(abs(v) for v in hist if v)!=0
        assert min(abs(v) for v in hist if v)==d
        assert sum(v*v*c for v,c in hist.items()) == (1<<len(edges))*sum(1 for _ in matchings_count(n))
        # Last identity is Parseval for signed matching-character transform.
        if n==6:
            assert dict(hist)==EXPECTED_HIST6, (hist,EXPECTED_HIST6)
            assert Counter(i.bit_count() for i,v in enumerate(w) if v==0)=={5:480,7:2880,9:2280,11:1185}
            proj=fwht([int(v!=0) for v in w])
            total=sum(abs(v) for v in proj)
            assert Fraction(total,len(w))==Fraction(762169,16384)
            assert sum(p*p for p in proj)==len(w)*25943
            assert len([p for p in w if p!=0])==25943
            digest=sha256(b''.join(pack('<i',v) for v in w)).hexdigest()
            print('W6_SHA256',digest)
            print('projection',total,'/',len(w),'=',Fraction(total,len(w)))
        print('n',n,'hist',sorted(hist.items()))
    print('INVO_FOURIER_PYTHON_PASS')

def matchings_count(n):
    # Matching masks counted independently of their sign; used for Parseval.
    e=list(combinations(range(n),2))
    def rec(v):
        if not v:
            yield ();return
        i=v[0]
        for m in rec(v[1:]):yield m
        for j in v[1:]:
            for m in rec([x for x in v if x not in [i,j]]):yield ((i,j),)+m
    return rec(list(range(n)))

if __name__=='__main__':main()
