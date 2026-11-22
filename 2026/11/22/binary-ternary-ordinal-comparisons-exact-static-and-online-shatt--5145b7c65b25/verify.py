"""Standalone finite checks for the stated binary/ternary threshold theorem.
Run: python verify.py (standard library only).  The infinite proof is in RESULT.md.
"""
from itertools import product, combinations
from functools import lru_cache
from math import floor, log2


def matching(s):
    assert s >= 3
    whole=(1<<s)-1
    # Pair sets that differ by inclusion of the first label.
    pairs=[]
    for v in range(1,whole):
        if v & 1: continue
        if v==whole^1: continue
        if v==(1<<1):
            # repair: {1}--{1,2} and {2}--{2,...,s}
            pairs.extend([(1,3),(2,whole^1)])
        else:
            pairs.append((v,v|1))
    assert len(pairs)==(2**s-2)//2
    assert {v for e in pairs for v in e} == set(range(1,whole))
    assert all((x & y)==x and x!=y for x,y in pairs)
    return pairs


def shattered_sample(a,b,s):
    # a ternary and b binary coordinates; constructions for s >= 3.
    N=2**s-2
    assert s>=3 and 2*a+b>=N
    pairs=matching(s)
    r=min(a,len(pairs))
    cols=[]
    for x,y in pairs[:r]:
        cols.append(tuple(0 if (x>>j)&1 else 1 if (y>>j)&1 else 2 for j in range(s)))
    leftovers=[v for pair in pairs[r:] for v in pair]
    for v in leftovers[:a-r]:
        cols.append(tuple(0 if (v>>j)&1 else 2 for j in range(s)))
    rest=leftovers[a-r:]
    assert len(rest)<=b
    for v in rest:
        cols.append(tuple(0 if (v>>j)&1 else 1 for j in range(s)))
    while len(cols)<a: cols.append((2,)*s)
    while len(cols)<a+b: cols.append((1,)*s)
    pts=list(zip(*cols))
    assert len(pts)==s and len(set(pts))==s
    Q=[3]*a+[2]*b
    traces={0,(1<<s)-1}
    for i,q in enumerate(Q):
        for t in range(q-1):
            traces.add(sum(1<<j for j,p in enumerate(pts) if p[i]<=t))
    assert len(traces)==2**s
    return pts


def online_dim(qs):
    X=list(product(*(range(q) for q in qs)))
    H=[tuple(0 for _ in X),tuple(1 for _ in X)]
    H += [tuple(int(x[i]<=t) for x in X)
          for i,q in enumerate(qs) for t in range(q-1)]
    masks=[]
    for x in range(len(X)):
        masks.append(sum(1<<j for j,h in enumerate(H) if h[x]))
    masks=set(masks)
    @lru_cache(None)
    def rank(S):
        if S.bit_count()<=1: return 0
        best=0
        for m in masks:
            A=S&m; B=S&~m
            if A and B:
                best=max(best,1+min(rank(A),rank(B)))
        return best
    return len(H),rank((1<<len(H))-1)


def vc_dim_bruteforce(qs, max_s=4):
    X=list(product(*(range(q) for q in qs)))
    H=[lambda x: False,lambda x: True]
    for i,q in enumerate(qs):
        for t in range(q-1):
            H.append(lambda x,i=i,t=t:x[i]<=t)
    vc=0
    for s in range(1,min(max_s,len(X))+1):
        if any(len({sum(int(h(X[j]))<<i for i,j in enumerate(idx)) for h in H})==2**s
               for idx in combinations(range(len(X)),s)):
            vc=s
        else:
            break
    return vc


def main():
    checks=0
    for s in range(3,11):
        M=matching(s)
        assert len(M)==2**(s-1)-1
        checks+=1
        if s<=6:
            n=2**s-2
            for a in range((n+1)//2,n//2+2):
                for b in range(0,3):
                    if 2*a+b>=n:
                        shattered_sample(a,b,s);checks+=1
            for a,b in [(1,n-2),(0,n),(n//2,0),(n//2-1,2)]:
                if 2*a+b>=n:
                    shattered_sample(a,b,s);checks+=1
    for qs in ([2],[3],[4],[2,2],[2,3],[3,3],[2,2,2],[2,3,3],[4,4],[2,4]):
        size,d=online_dim(qs)
        assert d==floor(log2(size)),(qs,size,d)
        checks+=1
    for qs,expected in [([2],1),([3],1),([4],1),([2,2],2),([2,3],2),
                        ([3,3],2),([2,2,2],2),([3,3,3],3),([4,4],2)]:
        v=vc_dim_bruteforce(qs,4)
        assert v==expected,(qs,v,expected)
        checks+=1
    print('VERIFY_OK',checks)

if __name__=='__main__':main()
