"""Exhaustive exact finite reduction for four-color successor-contact dynamics on complete bicliques.
The 225 initial support signatures are represented by tagged initially distinct colors;
tags are retained through mergers, so transient and least period are microscopic.
"""
from collections import Counter,defaultdict
from itertools import combinations
from math import comb

def step(tag):
    L,R=tag
    return (tuple((v+((v+1)%4 in R))%4 for v in L),
            tuple((v+((v+1)%4 in L))%4 for v in R))

def classify(tag):
    visited={};q=tag;t=0
    while q not in visited:
        if t>=50:raise AssertionError('unexpected long orbit')
        visited[q]=t;q=step(q);t+=1
    return visited[q],t-visited[q]

def coeffs():
    supports=[c for j in range(1,5) for c in combinations(range(4),j)]
    C=Counter();witness={};signature={}
    for L in supports:
        for R in supports:
            label=classify((L,R))
            C[(label[0],label[1],len(L),len(R))]+=1
            witness.setdefault(label,(L,R))
            signature[(L,R)]=label
    assert sum(C.values())==225
    assert set((t,p) for t,p,_,_ in C)=={(0,1),(1,1),(2,1),(3,1),(4,1),(0,4),(1,4),(2,4),(3,4),(0,6)}
    assert all(k==3 and h==3 for (t,p,k,h) in C if p==6)
    assert C[(0,6,3,3)]==4
    assert all(t<=4 and p in (1,4,6) for t,p,_,_ in C)
    return C,signature,witness

def onto(n,k):
    return sum((-1)**j*comb(k,j)*(k-j)**n for j in range(k+1))

def predicted(m,n,C):
    result=Counter()
    for (t,p,k,h),c in C.items():
        result[t,p]+=c*onto(m,k)*onto(n,h)
    return result

if __name__=='__main__':
    C,_,ex=coeffs()
    for t,p in sorted(set((t,p) for t,p,k,h in C)):
        table=[[C[t,p,k,h] for h in range(1,5)] for k in range(1,5)]
        print('ENTRY',t,'PERIOD',p,'MATRIX',table,'SUPPORT_COUNT',sum(map(sum,table)),'EXAMPLE',ex[t,p])
    for m,n in [(1,1),(1,4),(2,2),(2,3),(3,3),(4,4),(5,6),(9,9)]:
        result=predicted(m,n,C)
        assert sum(result.values())==4**(m+n)
        assert result[0,6]==4*onto(m,3)*onto(n,3)
        assert sum(v for (t,p),v in result.items() if p==6)==result[0,6]
        assert result[4,1]>0 if (m>=2 and n>=3) or (m>=3 and n>=2) else result[4,1]==0
        print('SIZE',m,n,'TOTAL',4**(m+n),'CLASSES',dict(sorted(result.items())))
    print('PASS 225 tagged support pairs; exact surjection-weighted counts')
