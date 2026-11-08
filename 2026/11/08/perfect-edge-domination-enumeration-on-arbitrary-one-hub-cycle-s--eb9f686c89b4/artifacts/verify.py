#!/usr/bin/env python3
"""Reproducible checks for perfect edge domination of cycle spiders.

Only the standard library is needed. Finite tests do not prove the theorem.
"""
from itertools import product


def graph(c, lengths):
    edges = [(j, (j+1)%c) for j in range(c)]
    arms=[]
    nxt=c
    for ell in lengths:
        arm=list(range(nxt,nxt+ell))
        edges.append((0,arm[0]))
        edges.extend((arm[j],arm[j+1]) for j in range(ell-1))
        arms.append(arm)
        nxt += ell
    return nxt,edges,arms


def spaced(bits):
    return all(not (bits[i] and bits[j]) for i in range(len(bits))
               for j in range(i+1,min(i+3,len(bits))))


def classified(mask,c,lengths):
    n,edges,arms=graph(c,lengths)
    C=[bool(mask>>i&1) for i in range(c)]
    A=[[bool(mask>>j&1) for j in arm] for arm in arms]
    if not spaced(C[1:]) or any(not spaced(v) for v in A):return False
    if any(len(v)>=2 and v[-2] for v in A):return False
    if C[0]:
        return (all(len(v)>=2 for v in A)
                and not any(C[1:3]+C[-2:])
                and all(not any(v[:2]) for v in A))
    return sum([C[1],C[-1]]+[v[0] for v in A]) in (0,len(A)+1)


def direct_white_sets(c,lengths):
    n,edges,arms=graph(c,lengths)
    adj=[]
    for i,(a,b) in enumerate(edges):
        adj.append(sum(1<<j for j,(u,v) in enumerate(edges)
                       if i!=j and (a in (u,v) or b in (u,v))))
    seen=set()
    for F in range(1<<len(edges)):
        if any(not (F>>j&1) and (F&adj[j]).bit_count()!=1 for j in range(len(edges))):
            continue
        occupied=0
        for j,(u,v) in enumerate(edges):
            if F>>j&1:occupied |= (1<<u)|(1<<v)
        W=((1<<n)-1)^occupied
        reformed=sum(1<<j for j,(u,v) in enumerate(edges)
                     if occupied>>u&1 and occupied>>v&1)
        assert F==reformed
        assert W not in seen
        seen.add(W)
    return seen


def word_sequences(max_size):
    I={-7:0,-6:0,-5:0,-4:0,-3:0,-2:1,-1:1,0:1}
    for j in range(1,max_size+5):I[j]=I[j-1]+I[j-3]
    b0={1:1,2:2,3:2};b1={1:1,2:0,3:1};h={1:0,2:1,3:2}
    for t in range(4,max_size+5):
        for B in (b0,b1,h):B[t]=B[t-1]+B[t-3]
    return I,b0,b1,h


def formula(c,lengths,seq):
    I,b0,b1,h=seq
    p=I[c-3]
    q=I[c-7] if c>=5 else 0
    s=I[c-5]
    a=p
    for ell in lengths:a*=b0[ell]
    B=2*s
    for ell in lengths:B*=b1[ell]
    Q=0
    for j,ell in enumerate(lengths):
        term=q*b0[ell]
        for k,ell2 in enumerate(lengths):
            if j!=k:term*=b1[ell2]
        Q+=term
    H=s
    for ell in lengths:H*=h[ell]
    return a+B+Q+H


def cycle_reference(n):
    C={3:4,4:5,5:6}
    for j in range(6,n+1):C[j]=C[j-1]+C[j-3]
    return C[n]


def run():
    seq=word_sequences(180)
    cases=0;largest=0
    for r in (2,3,4):
        for c in range(3,9):
            for arms in product(range(1,5),repeat=r):
                n=c+sum(arms)
                if n>12:continue
                actual=direct_white_sets(c,arms)
                expected={W for W in range(1<<n) if classified(W,c,arms)}
                assert actual==expected,(c,arms,sorted(actual^expected))
                assert len(actual)==formula(c,arms,seq),(c,arms,len(actual),formula(c,arms,seq))
                cases+=1;largest=max(largest,n)
    print('DIRECT_EDGE_SUBSET_AND_WHITE_CLASSIFICATION_OK',cases,'max_order',largest)
    for c in range(3,40):
        for r in range(2,11):
            arms=(2,)*r
            I,_,_,_=seq
            predicted=2**r*I[c-3]+I[c-5]
            assert formula(c,arms,seq)==predicted
    print('EQUAL_LENGTH_TWO_ARMS_CLOSED_FORM_OK c=3..39,r=2..10')
    for c in range(3,17):
        for r in (2,3,4):
            for arms in product(range(1,6),repeat=r):
                n=c+sum(arms)
                if n>20:continue
                assert formula(c,arms,seq)<cycle_reference(n),(c,arms)
    print('CYCLE_COMPARISONS_FINITE_OK order<=20 (nonproof)')
    print('VERIFY_OK')

if __name__=='__main__':run()
