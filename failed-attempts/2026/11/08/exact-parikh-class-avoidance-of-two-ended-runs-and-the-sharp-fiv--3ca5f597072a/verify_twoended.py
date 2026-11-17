#!/usr/bin/env python3
"""Reproduce exact two-ended-run subsequence avoidance counts over binary Parikh classes."""
from collections import defaultdict
from itertools import combinations
from math import comb

def has_subsequence(word, pat):
    j=0
    for c in word:
        if j < len(pat) and c == pat[j]:
            j += 1
    return j == len(pat)

def t_count(word):
    a = t = 0
    for c in word:
        if c == 'a': a += 1
        else: t += a
    return t

def gaussian(N, K):
    if K<0 or K>N: return [0]
    rows=[[1]]
    for n in range(1,N+1):
        new=[]
        for k in range(n+1):
            if k==0 or k==n:
                new.append([1]); continue
            left, right=rows[k],rows[k-1]
            out=[0]*max(len(left),len(right)+n-k)
            for i,x in enumerate(left): out[i]+=x
            for i,x in enumerate(right): out[i+n-k]+=x
            new.append(out)
        rows=new
    return rows[K]

def formula(A,B,r):
    if A<2: return gaussian(A+B,A)
    out=[0]*(A*B+1)
    for p in range(min(r-1,B)+1):
        inner=gaussian(A+p-2,p)
        for j,value in enumerate(inner):
            for v in range(B-p+1):
                out[p+j+A*v]+=value
    return out

def h(A,s):
    if not(2<=s<=2*A-2): return 0
    return min(s,2*A-s)//2

def triple_closed(A,B,t):
    if A<2: return 1
    return 1+sum(h(A,s) for s in range(2,2*A-1)
        if (t-s)%A==0 and 0 <= (t-s)//A <= B-2)

def test():
    tested=0
    for A in range(0,9):
        for B in range(0,9):
            if A+B>14: continue
            groups=defaultdict(list)
            for pos in combinations(range(A+B),A):
                mask=set(pos)
                w=''.join('a' if i in mask else 'b' for i in range(A+B))
                groups[t_count(w)].append(w)
            assert len(groups)==A*B+1
            assert [len(groups[t]) for t in range(A*B+1)]==gaussian(A+B,A)
            for r in range(1,min(B+2,7)):
                poly=formula(A,B,r)
                brute=[sum(not has_subsequence(w,'a'+'b'*r+'a')
                         for w in groups[t]) for t in range(A*B+1)]
                assert poly==brute,(A,B,r,poly,brute)
                tested+=1
            coeff=formula(A,B,3)
            assert all(coeff[t]==triple_closed(A,B,t) for t in range(A*B+1))
            bound=(A//2+1 if A>=2 and B>=2 else 1)
            assert max(coeff)==bound,(A,B,bound,coeff)
            if A>=2 and B>=2: assert coeff[A]==bound
    # Test arithmetic closed-form bound without any exponential enumeration.
    for A in range(2,160):
        for B in (0,1,2,3,6,12,100):
            values=[triple_closed(A,B,t) for t in range(A*B+1)]
            target=A//2+1 if B>=2 else 1
            assert max(values)==target
            if B>=2: assert values[A]==target
    print('TWO_ENDED_PARIKH_VERIFY_OK',tested)

if __name__=='__main__': test()
