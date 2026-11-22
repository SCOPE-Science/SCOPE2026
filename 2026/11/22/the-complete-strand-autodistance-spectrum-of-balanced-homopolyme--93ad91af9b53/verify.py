#!/usr/bin/env python3
"""Exact finite checks of the strand-orientation distance spectrum.
Pure Python 3, no third-party modules required.
"""
from collections import defaultdict
from itertools import product
from fractions import Fraction

ALPHABET = 'ACGT'
COMP = dict(A='T', T='A', C='G', G='C')
GC = {'C', 'G'}
STATES = [(a,b) for a in ALPHABET for b in ALPHABET]

def transfer(m):
    """Return [u^m] of the exact 16-state transfer in powers of v."""
    dp = {(a,b,int(a in GC)+int(b in GC),int(a!=b)):1
          for a,b in STATES}
    for _ in range(1,m):
        nxt=defaultdict(int)
        for (a,b,w,r),mult in dp.items():
            for c,d in STATES:
                if c != a and d != b:
                    nxt[(c,d,w+int(c in GC)+int(d in GC),r+int(c!=d))]+=mult
        dp=nxt
    ans=[0]*(m+1)
    for (a,b,w,r),mult in dp.items():
        if w==m and a!=COMP[b]:
            ans[r]+=mult
    return ans

def direct(m):
    """Independent enumeration of original length-2m DNA words."""
    n=2*m
    out=[0]*(m+1)
    def dfs(word,wt):
        if len(word)==n:
            if wt==m:
                rc=''.join(COMP[a] for a in reversed(word))
                dist=sum(a!=b for a,b in zip(word,rc))
                assert dist%2==0
                out[dist//2]+=1
            return
        for a in ALPHABET:
            if word and word[-1]==a:continue
            w=wt+int(a in GC)
            if w>m or w+(n-len(word)-1)<m:continue
            dfs(word+a,w)
    dfs('',0)
    return out

def moments(m):
    """Check exact first and second moments through an independent low-memory recurrence."""
    dp={(a,b,int(a in GC)+int(b in GC)):(1,int(a!=b),int(a!=b))
        for a,b in STATES}
    for _ in range(1,m):
        nd=defaultdict(lambda:[0,0,0])
        for (a,b,w),(count,s1,s2) in dp.items():
            for c,d in STATES:
                ww=w+int(c in GC)+int(d in GC)
                if c==a or d==b or ww>m:continue
                inc=int(c!=d)
                e=nd[(c,d,ww)]
                e[0]+=count
                e[1]+=s1+inc*count
                e[2]+=s2+2*inc*s1+inc*count
        dp=nd
    C=S1=S2=0
    for (a,b,w),v in dp.items():
        if w==m and a!=COMP[b]:
            C+=v[0]; S1+=v[1]; S2+=v[2]
    return C,Fraction(S1,C),Fraction(S2,C)-Fraction(S1,C)**2

def main():
    known={1:[0,8],2:[8,8,40],3:[0,80,112,232],
           4:[56,112,776,1056,1352],
           5:[0,848,2016,7168,8976,8200],
           6:[424,1232,11360,26120,63248,71520,50856]}
    for m in range(1,7):
        x=transfer(m)
        assert x==known[m],(m,x)
        if m<=5:
            y=direct(m)
            assert x==y,(m,x,y)
        assert all(v>0 for v in x[m%2:]), (m,x)
        assert all(v==0 for v in x[:m%2]), (m,x)
        C,mu,var=moments(m)
        assert C==sum(x)
        assert mu==Fraction(sum(i*c for i,c in enumerate(x)),C)
        assert var==Fraction(sum(i*i*c for i,c in enumerate(x)),C)-mu*mu
        print('n=',2*m,'spectrum=',x,'total=',C,'self_rc=',x[0])
    for m in [10,20,40]:
        C,mu,var=moments(m)
        print('half_length=',m,'mean/half_length=',float(mu/m),
              'variance/half_length=',float(var/m))
    print('PASS: transfer, direct source enumeration, moments, support')
if __name__=='__main__':main()
