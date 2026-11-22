#!/usr/bin/env python3
"""Independent exhaustive trace and boundary-obstruction verifier."""
from itertools import combinations
from math import comb

def words(a,b):
    out=[]
    for A_positions in combinations(range(a+b),a):
        A=set(A_positions)
        w=''.join('A' if z in A else 'B' for z in range(a+b))
        apos=[k for k,x in enumerate(w) if x=='A']
        bpos=[k for k,x in enumerate(w) if x=='B']
        trans=sum(w[i]=='B' and w[j]=='A' for i in range(a+b) for j in range(i+1,a+b))
        trace=sum(1<<(i*b+j) for i in range(a) for j in range(b) if apos[i]<bpos[j])
        boundaries=set()
        ai=bi=0
        for h,c in enumerate(w):
            if c=='A':ai+=1
            else:bi+=1
            if h and c!=w[h-1]: boundaries.add((ai-1,bi-1))
        out.append((trace, trans%2, frozenset(boundaries), w))
    return out

def check(a,b):
    W=words(a,b)
    even=[w[0] for w in W if w[1]==0]
    odd=[w[2] for w in W if w[1]==1]
    counts=[];bad=[]
    for k in range(min(a,b)+1):
        good=0
        for ii in combinations(range(a),k):
            for jj in combinations(range(b),k):
                S=frozenset(zip(ii,jj))
                positions=[i*b+j for i,j in sorted(S)]
                seen={sum(((m>>p)&1)<<r for r,p in enumerate(positions)) for m in even}
                actual=len(seen)==1<<k
                prediction=not any(boundary.issubset(S) for boundary in odd)
                assert actual==prediction,(a,b,S,actual,prediction)
                good+=int(actual)
        counts.append(good)
    vc=max(k for k,n in enumerate(counts) if n)
    expected=(min(a,b)-1 if a==b and a%2 else min(a,b))
    assert vc==expected,(a,b,vc,expected)
    return counts

if __name__=='__main__':
    tested=0
    for total in range(2,13):
        for a in range(1,total):
            b=total-a
            counts=check(a,b)
            print('PASS',a,b,'coefs',','.join(map(str,counts)))
            tested+=1
    print('PARITY_TWO_CHAIN_PY_PASS',tested,'profiles')
