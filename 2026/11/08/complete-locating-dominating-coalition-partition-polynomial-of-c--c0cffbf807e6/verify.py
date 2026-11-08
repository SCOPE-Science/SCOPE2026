"""Independent finite checks for locating-dominating coalition partitions of K_{m,n}.

Run: python3 verify.py
The program uses direct graph-neighbourhood tests, rather than the transversal
characterization in the proof. It is a finite corroboration, not an infinite proof.
"""
from collections import Counter
from itertools import combinations
from math import comb


def partitions(n):
    """Each unordered set partition occurs once, via restricted growth labels."""
    labels = [0] * n
    def rec(i, k):
        if i == n:
            blocks = [0] * k
            for v, j in enumerate(labels):
                blocks[j] |= 1 << v
            yield blocks
            return
        for j in range(k + 1):
            labels[i] = j
            yield from rec(i + 1, max(k, j + 1))
    labels[0] = 0
    yield from rec(1, 1)


def all_ld_masks(m, n):
    N = m + n
    adj = []
    for v in range(N):
        adj.append(sum(1 << w for w in range(N) if (v < m) != (w < m)))
    ok = bytearray(1 << N)
    for mask in range(1 << N):
        signatures = set()
        valid = True
        for v in range(N):
            if not (mask & (1 << v)):
                signature = adj[v] & mask
                if not signature or signature in signatures:
                    valid = False
                    break
                signatures.add(signature)
        ok[mask] = valid
    return ok


def predicted(m, n):
    N = m+n
    if N == 4:
        return {2: 1, 3: 2, 4: 1}
    if N == 5:
        return {2: 4, 3: 16}
    if N == 6:
        return {2: 17, 3: 51} if sorted((m,n)) == [2,4] else {2: 16, 3: 48}
    return {
        2: 2 ** (N - 1) - (m+1)*(n+1),
        3: comb(m,2)+comb(n,2)+m*n*(N-2)+2*comb(m,2)*comb(n,2)
    }


def check(m,n):
    ld = all_ld_masks(m,n)
    observed=Counter()
    triangles=0
    for blocks in partitions(m+n):
        if any(ld[b] for b in blocks):
            continue
        edges = []
        for i,j in combinations(range(len(blocks)),2):
            if ld[blocks[i]|blocks[j]]:
                edges.append((i,j))
        if all(any(i in edge for edge in edges) for i in range(len(blocks))):
            observed[len(blocks)] += 1
            if len(blocks)==3 and len(edges)==3:
                triangles += 1
    expect = predicted(m,n)
    assert dict(observed) == expect, (m,n,observed,expect)
    expected_triangles = 6 if (m,n) in ((2,3),(3,2),(3,3)) else 0
    assert triangles==expected_triangles,(m,n,triangles,expected_triangles)
    print('EXHAUSTIVE_OK',m,n,dict(observed),'triangles',triangles)


def sampled_larger(m,n):
    # Independently test every proposed three-block configuration (finite samples).
    N=m+n
    ld=all_ld_masks(m,n) if N<=16 else None
    def direct_ld(mask):
        if ld is not None:return ld[mask]
        ad=[sum(1<<w for w in range(N) if (v<m)!=(w<m)) for v in range(N)]
        signatures=set()
        for v in range(N):
            if not mask>>v&1:
                sig=ad[v]&mask
                if not sig or sig in signatures:return False
                signatures.add(sig)
        return True
    full=(1<<N)-1
    three=set()
    for i,j in combinations(range(m),2):three.add(tuple(sorted((1<<i,1<<j,full^(1<<i)^(1<<j)))))
    for i,j in combinations(range(m,N),2):three.add(tuple(sorted((1<<i,1<<j,full^(1<<i)^(1<<j)))))
    pairs=[(1<<a)|(1<<b) for a in range(m) for b in range(m,N)]
    for p in pairs:
        for v in range(N):
            if not p>>v&1:
                q=1<<v
                three.add(tuple(sorted((p,q,full^p^q))))
    for p,q in combinations(pairs,2):
        if not p&q:three.add(tuple(sorted((p,q,full^p^q))))
    assert len(three)==predicted(m,n)[3]
    for blocks in three:
        assert not any(direct_ld(b) for b in blocks)
        assert all(any(i!=j and direct_ld(blocks[i]|blocks[j]) for j in range(3)) for i in range(3))
    print('CONSTRUCTED_FAMILIES_OK',m,n,len(three))


def main():
    for N in range(4,11):
        for m in range(2,N//2+1):
            n=N-m
            check(m,n)
    for m,n in ((2,9),(3,8),(5,6),(6,7),(7,8)):
        sampled_larger(m,n)
    print('VERIFY_OK')

if __name__=='__main__':main()
