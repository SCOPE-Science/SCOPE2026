#!/usr/bin/env python3
"""Exact reproducibility checks for two-ballot committee construction.
No third-party packages. Run: python check.py
"""
from itertools import combinations, product
from fractions import Fraction
from math import floor, ceil

def build(na, nb, a_count, b_count, c_count, k):
    assert na >= 1 and nb >= 1 and 1 <= k <= a_count+b_count+c_count
    z = min(c_count, k)
    if z == k: return (0,0,k)
    t = k-z
    low, high = max(0,t-b_count), min(a_count,t)
    assert low <= high
    Q = Fraction(k*na,na+nb)
    target = (Q.numerator//Q.denominator) if z else ((2*Q.numerator+Q.denominator)//(2*Q.denominator))
    a = min(high,max(low,target))
    return (a,t-a,z)

def literal(na,nb, A,B,C,k,w):
    # Verify EXACT axioms, with every possible witness subset, not a simplified rule.
    goods = tuple(range(A+B+C))
    ballots = [frozenset(range(A))|frozenset(range(A+B,A+B+C))]*na + [frozenset(range(A,A+B+C))]*nb
    assert all(any(g in ballot for ballot in ballots) for g in goods)
    W = frozenset((*range(w[0]),*range(A,A+w[1]),*range(A+B,A+B+w[2])))
    n=na+nb
    sat=[len(v&W) for v in ballots]
    supp={g:tuple(i for i,v in enumerate(ballots) if g in v) for g in goods}
    def subs(ids):
        for j in range(1,len(ids)+1):
            yield from combinations(ids,j)
    # EJR+: unselected candidate and nonempty subset all below floor quota.
    for d in goods:
        if d in W: continue
        for S in subs(supp[d]):
            threshold=k*len(S)//n
            if all(sat[i]<threshold for i in S):return False,'EJR+',d,S
    # JUQ: selected c over ceil of supporter quota; swap with outside d
    # grants some nonempty subset of d-approvers at most its upper quota.
    for c in W:
        qc=(k*len(supp[c])+n-1)//n
        if not all(sat[i]>qc for i in supp[c]):continue
        for d in goods:
            if d in W:continue
            for S in subs(supp[d]):
                qs=(k*len(S)+n-1)//n
                if all(sat[i]+int(d in ballots[i])-int(c in ballots[i])<=qs for i in S):
                    return False,'JUQ',c,d,S
    # JNQ: both strict half-unit inequalities as defined in the primary work.
    for c in W:
        qc=Fraction(k*len(supp[c]),n)
        for d in goods:
            if d in W:continue
            if not all(sat[i]-qc > Fraction(int(d not in ballots[i]),2) for i in supp[c]):continue
            for S in subs(supp[d]):
                qs=Fraction(k*len(S),n)
                if all(qs-sat[i]>Fraction(int(c not in ballots[i]),2) for i in S):
                    return False,'JNQ',c,d,S
    return True,None

def reduced(na,nb,A,B,C,k,w):
    # Faster independent type-wise implementation including all nonempty type supports.
    a,b,c=w; sa=a+c;sb=b+c
    n=na+nb
    types={0:(1,),1:(2,),2:(1,2)}
    avail=(A,B,C)
    W=(a,b,c)
    s={1:sa,2:sb}
    q=lambda T:Fraction(k*(na*(1 in T)+nb*(2 in T)),n)
    groups=lambda t:tuple((i,) for i in types[t])+(((1,2),) if t==2 else ())
    for d in range(3):
        if W[d]>=avail[d]:continue
        for S in groups(d):
            if all(s[i] < floor(q(S)) for i in S):return False,'EJR+'
    for ctyp in range(3):
        if W[ctyp]==0:continue
        if all(s[i]>ceil(q(types[ctyp])) for i in types[ctyp]):
            for d in range(3):
                if W[d]>=avail[d]:continue
                for S in groups(d):
                    if all(s[i]+int(i in types[d])-int(i in types[ctyp])<=ceil(q(S)) for i in S):return False,'JUQ'
        for d in range(3):
            if W[d]>=avail[d]:continue
            if not all(s[i]-q(types[ctyp])>Fraction(int(i not in types[d]),2) for i in types[ctyp]):continue
            for S in groups(d):
                if all(q(S)-s[i]>Fraction(int(i not in types[ctyp]),2) for i in S):return False,'JNQ'
    return True,None

def main():
    exhaustive=0; fast=0
    # Full voter-subset quantification checks for small domains.
    for na,nb in product(range(1,4),repeat=2):
      for A,B,C in product(range(0,4),repeat=3):
        for k in range(1,min(A+B+C,6)+1):
            w=build(na,nb,A,B,C,k)
            assert literal(na,nb,A,B,C,k,w)[0],(na,nb,A,B,C,k,w,literal(na,nb,A,B,C,k,w))
            assert reduced(na,nb,A,B,C,k,w)[0]
            exhaustive+=1
    # Long-range rational boundaries, nontrivial inventory clipping.
    caps=(0,1,2,3,5,8,15)
    ks=(1,2,3,4,5,6,7,8,12,20)
    for na in range(1,21):
      for nb in range(1,21):
        for A,B,C in product(caps,repeat=3):
          for k in ks:
            if k>A+B+C:continue
            w=build(na,nb,A,B,C,k)
            assert reduced(na,nb,A,B,C,k,w)[0],(na,nb,A,B,C,k,w)
            fast+=1
    # JUQ strictly weaker than UQ even in this domain: voters {common}, {common,private}, k=2.
    assert build(1,1,0,1,1,2)==(0,1,1)
    print('PASS: literal voter-subset cases',exhaustive)
    print('PASS: extended type-aggregate cases',fast)
    print('PASS: boundary example')

if __name__=='__main__':main()
