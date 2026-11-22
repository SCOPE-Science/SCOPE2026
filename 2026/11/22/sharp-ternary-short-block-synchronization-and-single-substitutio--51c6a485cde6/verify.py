#!/usr/bin/env python3
"""Exact ternary error-correcting non-overlapping code census, lengths 2..6.

Only the Python standard library is required.  Bron-Kerbosch enumerates every
maximal compatibility clique, so the absence of cliques of size >=9 is exact.
"""
from itertools import permutations, product
from collections import Counter
from pathlib import Path

SIGMA='012'
def is_bifix_free(s):
    return all(s[:k]!=s[-k:] for k in range(1,len(s)))
def allowed_pair(a,b):
    return sum(x!=y for x,y in zip(a,b))>=3 and all(
        a[:k]!=b[-k:] and b[:k]!=a[-k:] for k in range(1,len(a)))
def build(n):
    W=[''.join(a) for a in product(SIGMA,repeat=n) if is_bifix_free(''.join(a))]
    A=[0]*len(W); edges=0
    for i in range(len(W)):
        for j in range(i):
            if allowed_pair(W[i],W[j]):
                A[i] |= 1<<j
                A[j] |= 1<<i
                edges += 1
    return W,A,edges

def bits(mask):
    while mask:
        z=mask&-mask
        yield z.bit_length()-1
        mask-=z

def maximal_cliques(A):
    N=len(A)
    histogram=Counter()
    largest=[]
    maxsize=[-1]
    def bk(R,P,X):
        if not (P or X):
            histogram[len(R)]+=1
            if len(R)>maxsize[0]:
                maxsize[0]=len(R);largest[:]=[R]
            elif len(R)==maxsize[0]:largest.append(R)
            return
        U=P|X
        pivot=max(bits(U),key=lambda u:(P&A[u]).bit_count())
        choices=P&~A[pivot]
        while choices:
            x=choices&-choices;v=x.bit_length()-1
            bk(R+(v,),P&A[v],X&A[v])
            P &=~x
            X |= x
            choices &=~x
    bk((),(1<<N)-1,0)
    return histogram,largest

def orbit_table(codes):
    transforms=[]
    for p in permutations(SIGMA):
        d=dict(zip(SIGMA,p))
        for rev in (False,True):
            transforms.append(lambda s,d=d,rev=rev:
                 ''.join(d[t] for t in (s[::-1] if rev else s)))
    left=set(codes); rows=[]
    while left:
        seed=min(left)
        orb={tuple(sorted(t(s) for s in seed)) for t in transforms}
        assert orb<=left
        rows.append((len(orb),min(orb)))
        left-=orb
    return sorted(rows)

def verify_table(path,header,expected):
    if not path.is_file():raise AssertionError('missing certificate table: '+str(path))
    lines=path.read_text(encoding='utf-8').splitlines()
    assert lines[0]==header
    assert len(lines)==len(expected)+1
    assert {tuple(s.split('\t')) for s in lines[1:]}==set(expected)

def main():
    s=[]
    expectation={2:(6,0,1,6),3:(18,0,1,18),4:(48,108,2,108),
                 5:(144,2070,4,300),6:(414,24156,8,528)}
    for n in range(2,7):
        W,A,edges=build(n)
        hist,R=maximal_cliques(A)
        maxc=max(hist)
        codes=sorted(tuple(sorted(W[i] for i in c)) for c in R)
        assert (len(W),edges,maxc,len(codes))==expectation[n]
        assert len(set(codes))==len(codes)
        if n in (5,6):
            assert dict(hist)==({2:48,3:1752,4:300} if n==5 else {3:48,4:4752,5:289464,6:507546,7:56568,8:528}),hist
            folder=Path(__file__).parent
            table=folder/('OPTIMA_%d.tsv'%n)
            verify_table(table,'\t'.join('codeword_%d'%j for j in range(1,maxc+1)),codes)
            orbits=orbit_table(codes)
            expect_count={5:29,6:49}[n]
            expect_sizes={5:{6:8,12:21},6:{6:10,12:39}}[n]
            assert len(orbits)==expect_count and dict(Counter(z for z,_ in orbits))==expect_sizes
            ot=folder/('ORBIT_REPRESENTATIVES_%d.tsv'%n)
            verify_table(ot,'orbit_size\t'+'\t'.join('codeword_%d'%j for j in range(1,maxc+1)),
                         [tuple([str(t)]+list(rep)) for t,rep in orbits])
            if n==5:
                assert all(sum(a!=b for a,b in zip(x,y))==3 for c in codes
                           for i,x in enumerate(c) for y in c[i+1:])
        s.append((n,len(W),edges,maxc,len(codes),sorted(hist.items())))
    print('VERIFY_OK',s)
if __name__=='__main__':main()
