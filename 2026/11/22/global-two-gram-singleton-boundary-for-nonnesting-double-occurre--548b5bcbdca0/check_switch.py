#!/usr/bin/env python3
"""Independently check every canonical non-mountain Dyck matching through order 9."""
from check import dyck_paths, fifo_word, bigrams, mountain

def find_switch(w):
    # Search every interlaced pair of letters a,b, in that order.
    n=len(w)//2
    pos=[[i for i,c in enumerate(w) if c==j] for j in range(n)]
    for a in range(n):
        for b in range(n):
            if a==b: continue
            a1,a2=pos[a];b1,b2=pos[b]
            if not (a1<b1<a2<b2): continue
            B=w[a1+1:b1]; D=w[a2+1:b2]
            if B==D: continue
            alt=w[:a1+1]+D+(b,)+w[b1+1:a2+1]+B+(b,)+w[b2+1:]
            assert len(w)==len(alt)
            assert sorted(w)==sorted(alt)
            assert bigrams(w,n)==bigrams(alt,n)
            assert w!=alt
            return alt
    return None

if __name__=='__main__':
    for n in range(1,10):
        seen=0; count=0
        for path in dyck_paths(n):
            w=fifo_word(path,tuple(range(n)))
            alt=find_switch(w)
            assert (alt is None)==mountain(path), (n,path,w,alt)
            seen+=1
            if alt is not None: count+=1
        print('n=%d Dyck=%d ambiguous=%d expected=%d'%(n,seen,count,seen-2**(n-1)))
    print('PASS')
