#!/usr/bin/env python3
"""Independent exact checks of the order-ideal learning-rank theorem.
Run: python3 verify.py ; requires Python 3 standard library only.
"""
from functools import lru_cache
from itertools import product,combinations

@lru_cache(None)
def two_row_rank(al, ah, bl, bh):
    # Coordinates are row-length parameters 0 <= b <= a <= n.
    al = max(al,bl)
    bh = min(bh,ah)
    if al > ah or bl > bh:
        return -1
    if al == ah and bl == bh:
        return 0
    best = 0
    for pivot in range(al + 1, ah + 1):
        z, o = two_row_rank(al,pivot - 1,bl,bh), two_row_rank(pivot,ah,bl,bh)
        if z >= 0 and o >= 0:
            best = max(best, 1 + min(z,o))
    for pivot in range(bl + 1,bh + 1):
        z, o = two_row_rank(al,ah,bl,pivot - 1),two_row_rank(al,ah,pivot,bh)
        if z >= 0 and o >= 0:
            best = max(best, 1 + min(z,o))
    return best


def direct_rank(masks, size):
    masks = frozenset(masks)
    @lru_cache(None)
    def go(sub):
        if len(sub) <= 1:
            return 0
        best = 0
        for x in range(size):
            on = frozenset(s for s in sub if s & (1 << x))
            if not on or on == sub:
                continue
            best = max(best, 1 + min(go(on), go(sub - on)))
        return best
    return go(masks)


def ideal_family(leq):
    n = len(leq)
    out = []
    for m in range(1<<n):
        if all(not(m>>x&1) or all(m>>y&1 for y in range(n) if leq[y][x]) for x in range(n)):
            out.append(m)
    return out


def ideal_interval_rank(leq):
    n = len(leq)
    down = [sum(1<<y for y in range(n) if leq[y][x]) for x in range(n)]
    up = [sum(1<<y for y in range(n) if leq[x][y]) for x in range(n)]
    @lru_cache(None)
    def go(low,high):
        free = high & ~low
        if free == 0:
            return 0
        ans = 0
        while free:
            z = free & -free
            free -= z
            i = z.bit_length()-1
            yes = go(low | down[i], high)
            no = go(low,high & ~up[i])
            ans = max(ans,1+min(yes,no))
        return ans
    return go(0,(1<<n)-1)


def all_small_posets():
    checks = 0
    for n in range(1,5):
        pairs=list(combinations(range(n),2))
        for choice in product((-1,0,1),repeat=len(pairs)):
            L = [[i == j for j in range(n)] for i in range(n)]
            for (a,b),c in zip(pairs,choice):
                if c==1: L[a][b]=True
                elif c==-1: L[b][a]=True
            if any(L[i][j] and L[j][k] and not L[i][k] for i in range(n) for j in range(n) for k in range(n)):
                continue
            d=direct_rank(ideal_family(L),n)
            r=ideal_interval_rank(L)
            assert d==r, (n,L,d,r)
            checks+=1
    return checks


def main():
    count=all_small_posets()
    for n in range(1,7):
        masks=[]
        for a in range(n+1):
            for b in range(a+1):
                m=sum(1<<j for j in range(a)) + sum(1<<(n+j) for j in range(b))
                masks.append(m)
        r=two_row_rank(0,n,0,n)
        assert r == direct_rank(masks,2*n),n
    seq=[two_row_rank(0,n,0,n) for n in range(1,31)]
    assert seq == [1,2,3,3,4,4,4,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7,7,7,8,8,8,8,8,8],seq
    for k in range(1,5):
        n=2**(k+1)-2
        assert two_row_rank(0,n,0,n)==2*k,(n,k)
    print('ORDER_IDEAL_ONLINE_PASS',count,'posets','6 direct grid crosschecks','30 grid ranks','4 dyadic equalities')

if __name__=='__main__':main()
