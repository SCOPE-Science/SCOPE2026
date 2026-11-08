"""Direct finite checks of outer mutual-visibility partitions on cycles.

Run with: python3 verify.py
Only Python's standard library is used.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import comb


def shortest_paths(n, x, y):
    if x == y:
        return [tuple([x])]
    forward = tuple((x+i) % n for i in range((y-x)%n+1))
    backward = tuple((x-i) % n for i in range((x-y)%n+1))
    length = min(len(forward),len(backward))
    return [p for p in (forward,backward) if len(p) == length]


def outer_visible(n, subset):
    S = set(subset)
    return all(any(S.isdisjoint(path[1:-1]) for path in shortest_paths(n,x,y))
               for x in S for y in range(n) if x != y)


def allowed_pair_graph(n):
    return {(a,b) for a in range(n) for b in range(a+1,n)
            if (n % 2 and min(b-a,n-(b-a)) == n//2)
            or (n % 2 == 0 and min(b-a,n-(b-a)) >= n//2-1)}


def enumerate_matchings(n, edges):
    links = [set() for _ in range(n)]
    for a,b in edges:
        links[a].add(b);links[b].add(a)
    @lru_cache(None)
    def recurse(mask):
        if not mask:
            return (1,)
        v = (mask&-mask).bit_length()-1
        rest = mask & ~(1<<v)
        res = list(recurse(rest))
        for u in links[v]:
            if rest & (1<<u):
                z = recurse(rest & ~(1<<u))
                while len(res) < len(z)+1:res.append(0)
                for j, c in enumerate(z):res[j+1] += c
        return tuple(res)
    return recurse((1<<n)-1)


def make_matrix():
    # Coefficient tuples indexed by degree, in the four occupancy states.
    T = [[[0] for _ in range(4)] for __ in range(4)]
    for a in range(4):
        for b in range(4):
            if a & b:continue
            deg = (b&1)+((b>>1)&1)
            p = [0]*(deg+1);p[deg]=1
            if a==0 and b==0:p.append(1)
            T[a][b] = p
    return T


def mul_p(a,b):
    r = [0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):r[i+j] += ai*bj
    return r


def mul_m(A,B):
    n=len(A);C=[[[0] for _ in range(n)] for __ in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                p=mul_p(A[i][k],B[k][j]);s=C[i][j]
                if len(s)<len(p):s.extend([0]*(len(p)-len(s)))
                for t,c in enumerate(p):s[t]+=c
    return C


def matrix_counts(n):
    assert n % 2==0 and n>=4
    m=n//2;T=make_matrix()
    X=[[[int(i==j)] for j in range(4)] for i in range(4)]
    for _ in range(m):X=mul_m(X,T)
    p=[0]*(2*m+1)
    for a in range(4):
        b= a if m%2 else (a&~3)|((a&1)<<1)|((a&2)>>1)
        for k,c in enumerate(X[a][b]):p[k]+=c
    return tuple(p[:m+1])


def lucas(m):
    a,b=2,1
    for _ in range(m):a,b=b,a+b
    return a


def all_partitions(n):
    # Genuine set partitions, not partitions pre-restricted to 1- and 2-blocks.
    def recurse(v, blocks):
        if v == n:
            yield tuple(tuple(block) for block in blocks)
            return
        for i in range(len(blocks)):
            blocks[i].append(v)
            yield from recurse(v+1,blocks)
            blocks[i].pop()
        blocks.append([v])
        yield from recurse(v+1,blocks)
        blocks.pop()
    yield from recurse(0,[])


def check():
    for n in range(4,19):
        edges=allowed_pair_graph(n)
        for a,b in combinations(range(n),2):
            assert outer_visible(n,(a,b)) == ((a,b) in edges),(n,a,b)
        if n<=12:
            for k in range(3,n+1):
                for S in combinations(range(n),k):
                    assert not outer_visible(n,S),(n,S)
        matching=enumerate_matchings(n,edges)
        if n%2==0:
            assert matching==matrix_counts(n),(n,matching,matrix_counts(n))
            assert matching[-1]==lucas(n//2),(n,matching[-1])
        else:
            formula=tuple(n*comb(n-k,k)//(n-k) for k in range(n//2+1))
            assert matching==formula,(n,matching,formula)
    print('ORIGINAL_GEODESIC_PAIR_AND_TRIPLE_CLASSIFICATION_OK n=4..18; sets through n=12')
    print('INDEPENDENT_MATCHING_AND_MATRIX_COEFFICIENTS_OK n=4..18')
    for n in range(3,11):
        counts=Counter()
        cache={mask:outer_visible(n,[j for j in range(n) if mask & (1<<j)]) for mask in range(1,1<<n)}
        for blocks in all_partitions(n):
            valid=True
            for block in blocks:
                mask=sum(1<<j for j in block)
                if not cache[mask]:valid=False;break
            if valid:counts[len(blocks)]+=1
        if n==3:expected={1:1,2:3,3:1}
        else:
            expected={n-k:c for k,c in enumerate(enumerate_matchings(n,allowed_pair_graph(n)))}
        assert dict(counts)==expected,(n,counts,expected)
        print('DIRECT_SET_PARTITIONS_OK',n,dict(sorted(counts.items())))
    print('VERIFY_OK')

if __name__=='__main__':check()
