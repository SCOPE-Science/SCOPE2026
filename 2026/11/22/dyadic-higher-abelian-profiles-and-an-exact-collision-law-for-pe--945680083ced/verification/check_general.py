#!/usr/bin/env python3
"""Tests the complete all-order bridge principle against overlapping counts."""
from itertools import product
from collections import defaultdict


def morph(k):
    w0,w1='0','1'
    for _ in range(k):
        w0,w1=(''.join(('01' if c=='0' else '00') for c in w) for w in (w0,w1))
    return w0,w1


def signature(s,ell):
    counts=[]
    for t in range(1,ell+1):
        for v in map(''.join, product('01',repeat=t)):
            counts.append(sum(s[j:j+t]==v for j in range(len(s)-t+1)))
    return tuple(counts)


def main():
    for ell in range(2,7):
        m=2*ell-2
        j=(m-1).bit_length()
        for k in range(j+3,min(j+5,9)):
            words=morph(k)
            p=morph(k+2)[0]
            F={p[t:t+m] for t in range(len(p)-m+1)}
            for a,w in enumerate(words):
                L=len(w)
                cycfactors={(w+w)[r:r+m] for r in range(L)}
                assert cycfactors==F,(ell,k,a,len(cycfactors),len(F))
                C=defaultdict(set);D=defaultdict(set)
                for r in range(L):
                    rot=w[r:]+w[:r]
                    local=(w+w+w)[L+r-(ell-1):L+r+ell-1]
                    C[local].add(signature(rot,ell))
                    D[signature(rot,ell)].add(local)
                assert len(C)==len(F)
                assert len(D)==len(F)
                assert all(len(z)==1 for z in C.values())
                assert all(len(z)==1 for z in D.values())
            # Different block images carry different one counts.
            assert words[0].count('1')!=words[1].count('1')
            print('ell=',ell,'k=',k,'classes=',2*len(F))
    print('GENERAL_OK')

if __name__=='__main__':main()
