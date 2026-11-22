"""Exhaustive power-domination and sensor-relocation verification on the McGee graph.

The 24 labelled vertices use the published LCF representation [12,7,-7]^8.
Run with Python 3: python verify_direct.py. No external dependencies.
"""
from itertools import combinations
from collections import Counter, deque

V = frozenset(range(24))
N = {v:set() for v in V}
def edge(x,y):
    N[x].add(y)
    N[y].add(x)
for i in range(24):
    edge(i,(i+1)%24)
    edge(i,(i+(12,7,-7)[i%3])%24)
assert all(len(N[v])==3 for v in V)
assert sum(map(len,N.values()))//2 == 36


def monitor(seed):
    blue = set(seed)
    for x in seed: blue.update(N[x])
    waves = 0
    while True:
        fresh = set()
        for v in blue:
            white = N[v] - blue
            if len(white) == 1: fresh.update(white)
        if not fresh: return blue == V, waves
        blue.update(fresh)
        waves += 1


def graph(optima, local):
    eligible = frozenset(optima)
    out = {}
    for s in eligible:
        nbr = set()
        for old in s:
            targets = N[old] if local else V
            for new in targets - s:
                nxt = frozenset((s-{old})|{new})
                if nxt in eligible: nbr.add(nxt)
        out[s]=frozenset(nbr)
    assert all(s in out[t] for t in out for s in out[t])
    return out


def shortest(net,start):
    dist={start:0}
    q=deque((start,))
    while q:
        u=q.popleft()
        for v in net[u]:
            if v not in dist:
                dist[v]=dist[u]+1
                q.append(v)
    return dist


def verify():
    assert all(not monitor(t)[0] for k in (1,2) for t in combinations(range(24),k))
    chosen=frozenset(frozenset(t) for t in combinations(range(24),3) if monitor(t)[0])
    assert len(chosen)==576
    assert Counter(monitor(t)[1] for t in chosen)==Counter({2:144,3:272,4:160})
    tj=graph(chosen,False)
    ts=graph(chosen,True)
    assert sum(map(len,tj.values()))//2 == 6184
    assert sum(map(len,ts.values()))//2 == 1328
    assert Counter(map(len,ts.values()))==Counter({4:320,5:176,6:64,7:16})
    assert Counter(map(len,tj.values()))==Counter({23:112,17:96,22:80,18:64,21:64,25:64,16:32,27:32,29:32})
    dist_hist_j=Counter()
    dist_hist_s=Counter()
    delta_hist=Counter()
    hard=set()
    ecc_j=Counter()
    ecc_s=Counter()
    for s in chosen:
        d0=shortest(tj,s)
        d1=shortest(ts,s)
        assert len(d0)==len(d1)==576
        ecc_j[max(d0.values())]+=1
        ecc_s[max(d1.values())]+=1
        for t in chosen:
            if t==s: continue
            a,b=d0[t],d1[t]
            dist_hist_j[a]+=1
            dist_hist_s[b]+=1
            delta_hist[b-a]+=1
            if b-a==7:
                hard.add(frozenset((s,t)))
                assert (a,b)==(1,8)
    assert ecc_j==Counter({4:576})
    assert ecc_s==Counter({8:432,9:144})
    assert tuple(dist_hist_j[i]//2 for i in range(1,5)) == (6184,44944,109672,4800)
    assert tuple(dist_hist_s[i]//2 for i in range(1,10)) == (1328,4048,10816,24744,42752,48752,27624,5400,136)
    assert {k:v//2 for k,v in delta_hist.items()} == {0:8856,1:21048,2:41056,3:50216,4:35568,5:8600,6:248,7:8}
    assert len(hard)==8
    assert len(set().union(*(set(pair) for pair in hard))) == 16
    assert sum(delta_hist.values())//2==576*575//2
    print('VERIFY_DIRECT_OK')
    print('minimum sensors=3, placements=576; waves after neighborhood stage: (2:144,3:272,4:160)')
    print('jump edges=6184, radius=diameter=4; slide edges=1328, radius=8, diameter=9')
    print('max slide distance excess=7 on exactly 8 unordered pairs, all direct jumps of slide distance eight')

if __name__=='__main__':verify()
