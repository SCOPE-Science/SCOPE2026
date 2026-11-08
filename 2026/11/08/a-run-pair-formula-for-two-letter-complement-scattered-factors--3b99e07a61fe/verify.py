"""Independent finite tests for ordered two-letter complement factors."""
from itertools import product
from collections import defaultdict
from random import Random
from fractions import Fraction

def run_signature(w):
    ans=[]
    i=0
    while i<len(w):
        j=i+1
        while j<len(w) and w[j]==w[i]:j+=1
        ans.append((w[i],i,j))
        i=j
    return ans

def formula(w,a,b):
    rr=run_signature(w)
    m=sum(1 for i,(x,_,_) in enumerate(rr) if x==a for j in range(i+1,len(rr)) if rr[j][0]==b)
    e=sum(1 for i in range(len(rr)-3) if rr[i][0]==a and rr[i+1][0]==b and rr[i+2][0]==a and rr[i+3][0]==b and rr[i+1][2]-rr[i+1][1]==1 and rr[i+2][2]-rr[i+2][1]==1)
    return m-e

def linear_formula(w,a,b):
    count_a=0
    pairs=0
    prev=None
    for c in w:
        if c!=prev:
            if c==a:count_a+=1
            if c==b:pairs+=count_a
        prev=c
    return pairs-sum(w[i:i+4]==a+b+a+b for i in range(len(w)-3))

def expected(n,q):
    if n<2:return Fraction(0)
    return (Fraction(1,q*q)+Fraction(2*(n-2)*(q-1),q**3)+
            Fraction((n-2)*(n-3)*(q-1)**2,2*q**4)-
            Fraction(max(0,n-3),q**4))

def brute(w,a,b):
    s=set()
    for i in range(len(w)):
        if w[i]!=a:continue
        for j in range(i+1,len(w)):
            if w[j]==b:
                s.add(w[:i]+w[i+1:j]+w[j+1:])
    return len(s)

def graph_equivalence(w,a,b):
    rr=run_signature(w)
    pairs=[(i,j) for i,run in enumerate(rr) if run[0]==a for j in range(i+1,len(rr)) if rr[j][0]==b]
    obs=defaultdict(set)
    for i,j in pairs:
        p=rr[i][1];q=rr[j][1]
        v=w[:p]+w[p+1:q]+w[q+1:]
        obs[v].add((i,j))
    for members in obs.values():
        if len(members)==1: continue
        a0=min(i for i,j in members)
        a1=max(i for i,j in members)
        expected={(i,i+1) for i in range(a0,a1+1,2)}
        if members!=expected:
            raise AssertionError(('nonchain class',w,a,b,members,expected))
        for i in range(a0,a1,2):
            if not (rr[i+1][2]-rr[i+1][1]==rr[i+2][2]-rr[i+2][1]==1):
                raise AssertionError(('bad link',w,members,i))
    return len(obs)

def main():
    checks=0
    for n in range(12):
        for chars in product('abc',repeat=n):
            w=''.join(chars)
            f=formula(w,'a','b')
            v=brute(w,'a','b')
            g=graph_equivalence(w,'a','b')
            assert f==v==g==linear_formula(w,'a','b'),(w,f,v,g)
            checks+=1
    rng=Random(20261102)
    for q in (2,3,4,5):
        A='abcde'[:q]
        for n in range(12,61,4):
            for _ in range(80):
                w=''.join(rng.choice(A) for _ in range(n))
                assert formula(w,'a','b')==brute(w,'a','b')==linear_formula(w,'a','b')
                graph_equivalence(w,'a','b')
                checks+=1
    for q in (2,3):
        for n in range(2,8):
            A='abc'[:q]
            count=sum(linear_formula(''.join(t),'a','b') for t in product(A,repeat=n))
            assert Fraction(count,q**n)==expected(n,q)
    print('PASS',checks,'words: exhaustive ternary lengths 0..11, random length 12..60 over q=2..5; full collision classes verified')
if __name__=='__main__':main()
