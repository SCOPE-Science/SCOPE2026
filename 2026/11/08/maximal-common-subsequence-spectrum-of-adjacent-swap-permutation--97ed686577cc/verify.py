#!/usr/bin/env python3
"""Exact finite checks for the adjacent-swap permutation-power MCS law."""
from collections import Counter
from itertools import product
from math import comb, factorial

def subsequences(word):
    ans={''}
    for ch in word:
        ans.update({x+ch for x in tuple(ans)})
    return ans

def brute_maximal(x,y,alphabet):
    common=subsequences(x)&subsequences(y)
    return {w for w in common if not any(w[:i]+a+w[i:] in common
                for a in alphabet for i in range(len(w)+1))},len(common)

def is_subsequence(w,X):
    it=iter(X)
    return all(any(y==c for y in it) for c in w)

def predicted(q,p,k):
    P=''.join(map(str,range(q)))
    A=P[:p]; B=P[p+2:]; x=P[p];y=P[p+1]
    answer=set()
    # each segment has positive alternating middle; total core length <=2*k-1
    blocks=[]
    for n in range(1,2*k):
        for start in (x,y):
            s=''.join((start if j%2==0 else (y if start==x else x)) for j in range(n))
            blocks.append((s,sum(a==x and b==y for a,b in zip(s,s[1:])),
                          sum(a==y and b==x for a,b in zip(s,s[1:]))))
    def rec(parts,h,v):
        r=len(parts)
        if r>=1 and h==v==k-r:
            answer.add(''.join(A+s+B for s in parts))
        if r>=k or h>k-r-1 or v>k-r-1:return
        for s,a,b in blocks:
            if h+a<=k-(r+1) and v+b<=k-(r+1):
                rec(parts+[s],h+a,v+b)
    rec([],0,0)
    return answer

def class_count(k,r):
    d=k-r
    return sum(factorial(r)//(factorial(t)**2*factorial(r-2*t))
               *2**(r-2*t)*comb(k-t-1,r-1)
               for t in range(min(d,r//2)+1))

def run():
    tested=0; words=0; mcs=0
    for q in range(4,8):
        for p in range(q-1):
            for k in range(1,5):
                if q*k>17:continue
                P=''.join(map(str,range(q)))
                Q=list(P); Q[p],Q[p+1]=Q[p+1],Q[p]; Q=''.join(Q)
                actual,c=brute_maximal(P*k,Q*k,P)
                predicted_set=predicted(q,p,k)
                assert actual==predicted_set, (q,p,k,'set mismatch',actual^predicted_set)
                hist=Counter(map(len,actual))
                exp={2*k+(q-3)*r:class_count(k,r) for r in range(1,k+1)}
                assert hist==exp,(q,p,k,hist,exp)
                assert len(actual)==comb(2*k,k)
                tested+=1;words+=c;mcs+=len(actual)
    # Independent greedy budget equivalence on all small words.
    budget_tests=0
    for q in range(4,7):
        for p in range(q-1):
            P=''.join(map(str,range(q)))
            Q=list(P);Q[p],Q[p+1]=Q[p+1],Q[p];Q=''.join(Q)
            for k in (1,2):
                for W in map(''.join,product(P,repeat=min(5,q*k))):
                    dP=(int(bool(W))+sum(P.index(a)>=P.index(b) for a,b in zip(W,W[1:])))
                    dQ=(int(bool(W))+sum(Q.index(a)>=Q.index(b) for a,b in zip(W,W[1:])))
                    assert is_subsequence(W,P*k)==(dP<=k)
                    assert is_subsequence(W,Q*k)==(dQ<=k)
                    budget_tests+=1
    for k in range(1,26):
        assert sum(class_count(k,r) for r in range(1,k+1))==comb(2*k,k)
    print('VERIFY_OK', 'host_cases',tested,'common_words',words,'maximal_words',mcs,'budget_tests',budget_tests,'symbolic_count_levels',25)
if __name__=='__main__':run()
