#!/usr/bin/env python3
"""Standalone exact verifier for hierarchical temporal delegation optimization.

Tests an interval-envelope dynamic program against independent exhaustive search.
All costs are integers and the only dependencies are from Python's standard library.
"""
from heapq import heappush, heappop
from itertools import product
from random import Random


def solve(parent, availability, horizons, scores):
    """Return optimum utility and one feasible choice of times, or (None, None).

    Vertices numbered with parent[v] < v; vertices can always be topologically
    renumbered before applying this routine. Root is vertex 0 and has no horizon.
    """
    n = len(parent)
    assert parent[0] == -1 and all(0 <= parent[v] < v for v in range(1, n))
    children = [[] for _ in range(n)]
    for v in range(1, n):
        children[parent[v]].append(v)
    dp = [{} for _ in range(n)]
    intervals = [None] * n
    for v in range(n-1, -1, -1):
        a, b = availability[v]
        low, high = a, b
        # Difference array over the parent's explicit available times.
        change = [0] * (b - a + 2)
        for c in children[v]:
            if intervals[c] is None:
                return None, None
            cl, cu = intervals[c]
            low = max(low, min(t-horizons[c][t] for t in range(cl,cu+1)))
            high = min(high, cu)
            # Each child choice generates a closed interval of parent times
            # with a constant subtree-optimal contribution. Calculate the
            # upper envelope of these weighted intervals using a heap sweep.
            events = {}
            for s in range(cl,cu+1):
                left = s-horizons[c][s]
                events.setdefault(left, []).append((dp[c][s],s))
                events.setdefault(s+1, [])
            heap=[]
            ev=sorted(events)
            for j, t in enumerate(ev):
                while heap and heap[0][2] < t:
                    heappop(heap)
                for weight, end in events[t]:
                    heappush(heap, (-weight,-end,end))
                # Remove events with expired end after new inserts as well.
                while heap and heap[0][2] < t:
                    heappop(heap)
                finish = (ev[j+1]-1 if j+1 < len(ev) else t)
                if not heap:
                    continue
                start=max(a,t)
                stop=min(b,finish)
                if start<=stop:
                    w=-heap[0][0]
                    change[start-a]+=w
                    change[stop+1-a]-=w
        if low>high:
            return None, None
        intervals[v]=(low,high)
        run=0
        for t in range(a,b+1):
            run+=change[t-a]
            if low <=t <= high:
                dp[v][t]=scores[v][t]+run
    root_time=max(dp[0],key=lambda t:dp[0][t])
    best=dp[0][root_time]
    chosen=[None]*n
    chosen[0]=root_time
    for v in range(1,n):
        pt=chosen[parent[v]]
        available=[t for t in dp[v] if t-horizons[v][t]<=pt<=t]
        assert available
        chosen[v]=max(available,key=lambda t:dp[v][t])
    assert sum(scores[v][chosen[v]] for v in range(n)) == best
    return best,tuple(chosen)


def brute(parent, availability, horizons, scores):
    domains=[range(a,b+1) for a,b in availability]
    good=[]
    for times in product(*domains):
        if all(times[v]-horizons[v][times[v]] <= times[parent[v]] <= times[v]
               for v in range(1,len(parent))):
            good.append((sum(scores[v][times[v]] for v in range(len(parent))),times))
    return (max(good) if good else (None,None))


def run_checks():
    rng=Random(440311)
    count=0
    for n in range(2,7):
        for _ in range(1150):
            L=rng.choice((2,3,4))
            parent=[-1]+[rng.randrange(v) for v in range(1,n)]
            av=[]; h=[{}]; w=[]
            for v in range(n):
                a=rng.randint(1,L);b=rng.randint(a,L)
                av.append((a,b))
                w.append({t:rng.randint(0,12) for t in range(1,L+1)})
                if v: h.append({t:rng.randrange(t) for t in range(1,L+1)})
            x,path=solve(parent,av,h,w)
            z,example=brute(parent,av,h,w)
            assert x==z, (parent,av,h,w,x,z,path,example)
            if path is not None:
                assert all(av[v][0]<=path[v]<=av[v][1] for v in range(n))
                assert all(path[v]-h[v][path[v]]<=path[parent[v]]<=path[v] for v in range(1,n))
            count+=1
    # Four-voter obstruction: both leaves individually reach the ballot,
    # but their parent needs incompatible action times.
    pa=[-1,0,1,1]
    av=[(1,6),(1,6),(2,2),(5,5)]
    h=[{}, {t:t-1 for t in range(1,7)}]+[{t:min(1,t-1) for t in range(1,7)} for _ in (2,3)]
    w=[{t:0 for t in range(1,7)} for _ in range(4)]
    assert solve(pa,av,h,w)[0] is None
    for leaf in (2,3):
        assert any(tleaf-h[leaf][tleaf] <= tp <= tleaf and tp-h[1][tp]<=tr<=tp
                   for tr in range(1,7) for tp in range(1,7) for tleaf in range(av[leaf][0],av[leaf][1]+1))
    print(f'PASS: {count} random exact brute-force welfare comparisons; four-vertex confluence obstruction checked')

if __name__=='__main__':
    run_checks()
