"""Exact finite checks of oriented root-polytope vertex covariance identities.

Requires only Python 3's standard library. All identities are tested using
integers, not floating point or stochastic numerical approximations.
"""
from itertools import combinations
from math import comb
from random import Random


def determinant(a):
    a = [list(row) for row in a]
    n = len(a)
    if not n:
        return 1
    d = 1
    sign = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((j for j in range(k+1, n) if a[j][k]), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign *= -1
        p = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j]*p - a[i][k]*a[k][j]
                assert num % d == 0
                a[i][j] = num // d
            a[i][k] = 0
        d = p
    return sign * a[-1][-1]


def score_and_laplacian(n, edges):
    s = [0]*n
    L = [[0]*n for _ in range(n)]
    for u,v in edges:
        s[u] += 1
        s[v] -= 1
        L[u][u] += 1
        L[v][v] += 1
        L[u][v] -= 1
        L[v][u] -= 1
    return s,L


def covariance_cofactor(n, edges):
    m = len(edges)
    s,L = score_and_laplacian(n, edges)
    return determinant([[m*L[i][j]-s[i]*s[j] for j in range(n-1)] for i in range(n-1)])


def unicycle_imbalance_squared(n, subset):
    # A connected n-edge graph has one cycle. Peel leaves, count the signs
    # of directed cycle edges along either chosen cyclic traversal.
    und = [[] for _ in range(n)]
    orientation = set(subset)
    for u,v in subset:
        und[u].append(v)
        und[v].append(u)
    seen={0}; queue=[0]
    for u in queue:
        for v in und[u]:
            if v not in seen:
                seen.add(v); queue.append(v)
    if len(seen)!=n:
        return 0
    active=[True]*n
    degrees=[len(x) for x in und]
    leaves=[i for i in range(n) if degrees[i]<=1]
    for v in leaves:
        active[v]=False
        for u in und[v]:
            if active[u]:
                degrees[u]-=1
                if degrees[u]==1:
                    leaves.append(u)
    cyc=[i for i in range(n) if active[i]]
    assert len(cyc)>=3
    start=cyc[0]
    prev=-1; cur=start; signed=0; steps=0
    while True:
        neighbor=next(v for v in und[cur] if active[v] and v!=prev)
        signed += 1 if (cur,neighbor) in orientation else -1
        steps += 1
        if neighbor==start:
            break
        prev,cur=cur,neighbor
        assert steps<=n
    assert steps==len(cyc)
    return signed*signed


def sum_unicycles(n, edges):
    return sum(unicycle_imbalance_squared(n, c) for c in combinations(edges,n))


def graph_check(n, edges):
    m=len(edges)
    LHS=covariance_cofactor(n,edges)
    RHS= m**(n-2)*sum_unicycles(n,edges) if m>=n else 0
    assert LHS==RHS, (n,edges,LHS,RHS)


def tournament(n, mask):
    return [(u,v) if mask & (1<<k) else (v,u)
            for k,(u,v) in enumerate(combinations(range(n),2))]


def tournament_check(n, mask, full_unicycles=False):
    edges=tournament(n,mask)
    m=len(edges)
    s,_=score_and_laplacian(n,edges)
    score=sum(x*x for x in s)
    # Use integer numerator for the fraction.
    U_num=n**(n-2)*(n*m-score)
    assert U_num>=0
    assert covariance_cofactor(n,edges)*n == (m**(n-2))*U_num
    if full_unicycles:
        assert sum_unicycles(n,edges)*n==U_num
    return score


def main():
    R=Random(20261017)
    checks_graph=checks_tourney=0
    for n in range(3,7):
        und=list(combinations(range(n),2))
        # Random graphs, many with bridges and some orientation-graded.
        for _ in range(50 if n<=5 else 22):
            k=R.randrange(n-1,len(und)+1)
            chosen=R.sample(und,k)
            oriented=[(u,v) if R.randrange(2) else (v,u) for u,v in chosen]
            graph_check(n,oriented)
            checks_graph+=1
    for n in range(3,6):
        bits=comb(n,2)
        masks=range(1<<bits)
        seen_min=set(); seen_max=set()
        scores=[]
        for mask in masks:
            score=tournament_check(n,mask,full_unicycles=(n<=4 or (n==5 and mask%67==0)))
            scores.append(score)
            checks_tourney+=1
        lo=n if n%2==0 else 0
        hi=n*(n*n-1)//3
        assert min(scores)==lo
        assert max(scores)==hi
        if n<=5:
            for mask, score in enumerate(scores):
                s,_=score_and_laplacian(n,tournament(n,mask))
                if score==hi:
                    assert sorted(s)==list(range(-(n-1),n,2))
                if score==lo:
                    assert all(abs(x)==(1-n%2) for x in s)
    # For order 6, enumerate every score vector without determinant expansion.
    n=6
    scores=[]
    for mask in range(1<<comb(n,2)):
        s,_=score_and_laplacian(n,tournament(n,mask))
        scores.append(sum(x*x for x in s))
    assert min(scores)==n and max(scores)==n*(n*n-1)//3
    checks_tourney+=len(scores)
    # Orientation reversal does not affect a squared imbalance.
    for n in range(3,7):
        for _ in range(8):
            und=R.sample(list(combinations(range(n),2)),R.randint(n-1,comb(n,2)))
            edges=[(u,v) if R.randrange(2) else (v,u) for u,v in und]
            assert sum_unicycles(n,edges)==sum_unicycles(n,[(v,u) for u,v in edges])
    print(f"PASS exact determinant/unicycle identity: {checks_graph} oriented graphs")
    print(f"PASS tournament determinant, sharp square-score extrema: {checks_tourney} orientations")
    print("PASS independent cycle-sign enumeration and reversal symmetry")


if __name__=='__main__':
    main()
