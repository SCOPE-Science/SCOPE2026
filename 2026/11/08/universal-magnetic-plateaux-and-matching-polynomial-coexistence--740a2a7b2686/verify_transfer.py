"""Exact local-factor contraction for the 3-state Potts model on L(Q_3)."""
from collections import Counter
from functools import lru_cache

CUBE_EDGES = tuple((u, v) for u in range(8) for v in range(u + 1, 8)
                   if (u ^ v).bit_count() == 1)
INCIDENT = tuple(tuple(i for i, (a, b) in enumerate(CUBE_EDGES) if u in (a, b))
                 for u in range(8))
LAST = tuple(max(i) for i in INCIDENT)

def mono(a):
    return int(a[0] == a[1]) + int(a[1] == a[2]) + int(a[0] == a[2])

@lru_cache(None)
def recur(i, front):
    if i == len(CUBE_EDGES):
        assert not front
        return {(0, 0): 1}
    u, v = CUBE_EDGES[i]
    out = Counter()
    for c in range(3):
        state = {w: list(s) for w, s in front}
        cost = 0
        for w in (u, v):
            state.setdefault(w, []).append(c)
            if LAST[w] == i:
                assert len(state[w]) == 3
                cost += mono(state.pop(w))
        nxt = tuple((w, tuple(cs)) for w, cs in sorted(state.items()))
        for (k, b), val in recur(i + 1, nxt).items():
            out[(k + (c == 0), b + cost)] += val
    return dict(out)

def main():
    hist = recur(0, ())
    assert sum(hist.values()) == 3**12
    sectors = {k: (min(b for (kk, b) in hist if kk == k),
                   sum(n for (kk, b), n in hist.items() if kk == k and b == min(bb for (k2, bb) in hist if k2 == k)))
               for k in range(13)}
    expected = {0:(8,450),1:(6,1248),2:(4,1044),3:(2,288),4:(0,24),5:(2,288),6:(4,912),7:(6,864),8:(8,144),9:(12,352),10:(16,168),11:(20,24),12:(24,1)}
    assert sectors == expected, (sectors, expected)
    for x, deg in [(-2,3054),(2,2232),(4,689)]:
        energy = min(b-x*k for k,(b,n) in sectors.items())
        got = sum(n for k,(b,n) in sectors.items() if b-x*k==energy)
        assert got==deg,(x,got)
    print('TRANSFER_OK states=',sum(hist.values()),'states=',len(hist),'memo=',recur.cache_info().currsize)
    for k in range(13):print(k,*sectors[k])

if __name__=='__main__':main()
