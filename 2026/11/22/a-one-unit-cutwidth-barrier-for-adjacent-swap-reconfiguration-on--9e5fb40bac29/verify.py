#!/usr/bin/env python3
"""Direct-edge small-case and constructive checks for cutwidth-constrained
adjacent-order swaps on balanced double stars. Standard-library only.
"""
from itertools import permutations
from collections import Counter, deque
from functools import lru_cache
from math import factorial
import random


def edges(t):
    return [("U", "V")] + [("U", f"A{i}") for i in range(t)] + [("V", f"B{i}") for i in range(t)]


def width(perm, t):
    # Edge-crossing definition, deliberately independent of the prefix formula.
    pos = {v: i for i, v in enumerate(perm)}
    return max(sum(min(pos[u], pos[v]) <= i < max(pos[u], pos[v])
                   for u, v in edges(t)) for i in range(len(perm)-1))


def symbolic_count(t, k):
    @lru_cache(None)
    def count(a, b, h):
        if (a, b, h) == (t, t, 2):
            return 1
        result = 0
        for symbol in ('A', 'B', 'H'):
            if (symbol == 'A' and a == t or symbol == 'B' and b == t
                    or symbol == 'H' and h == 2):
                continue
            aa = a + (symbol == 'A')
            bb = b + (symbol == 'B')
            hh = h + (symbol == 'H')
            crossing = (aa + bb if hh == 0 else
                        t - aa + bb + 1 if hh == 1 else
                        2*t - aa - bb)
            if crossing <= k:
                result += count(aa, bb, hh)
        return result
    return count(0, 0, 0)


def normalize(perm, t, k):
    """Construct a valid route to the canonical state without exchanging hubs.
    Requires k>=t and U before V. Returns every intermediate ordering.
    """
    seq = list(perm)
    route = [tuple(seq)]
    assert seq.index('U') < seq.index('V') and width(seq, t) <= k

    def swap(i):
        seq[i], seq[i+1] = seq[i+1], seq[i]
        assert width(seq, t) <= k, (t, k, route[-1], tuple(seq))
        route.append(tuple(seq))

    def isA(x): return x.startswith('A')
    def isB(x): return x.startswith('B')

    def sort_BA():
        changed = True
        while changed:
            changed = False
            for i in range(len(seq)-1):
                if isB(seq[i]) and isA(seq[i+1]):
                    swap(i)
                    changed = True

    sort_BA()
    # Pass all B leaves preceding U through U to its right.
    while seq.index('U') and isB(seq[seq.index('U')-1]):
        swap(seq.index('U')-1)
    # Pass all A leaves following V through V to its left.
    while seq.index('V')+1 < len(seq) and isA(seq[seq.index('V')+1]):
        swap(seq.index('V'))
    sort_BA()
    while seq.index('U')+1 < len(seq) and isA(seq[seq.index('U')+1]):
        swap(seq.index('U'))
    while seq.index('V') and isB(seq[seq.index('V')-1]):
        swap(seq.index('V')-1)
    # All A leaves now precede U; all B leaves follow V.
    assert all(isA(x) for x in seq[:t]), seq
    assert seq[t:t+2] == ['U', 'V'], seq
    assert all(isB(x) for x in seq[t+2:]), seq
    # Reorder labels inside each twin class; these swaps preserve every cut.
    for start,end in [(0,t), (t+2,2*t+2)]:
        for i in range(start,end):
            for j in range(end-1,i,-1):
                if int(seq[j][1:]) < int(seq[j-1][1:]):
                    swap(j-1)
    assert tuple(seq) == tuple([f'A{i}' for i in range(t)] + ['U','V'] + [f'B{i}' for i in range(t)])
    return route


def check_bridge(t):
    h = t//2
    state = tuple([f'A{i}' for i in range(h)] + [f'B{i}' for i in range(h)]
                  + ['U','V'] + [f'A{i}' for i in range(h,t)]
                  + [f'B{i}' for i in range(h,t)])
    j = state.index('U')
    other = state[:j] + ('V','U') + state[j+2:]
    assert width(state, t) == t+1 and width(other, t) == t+1


def full(t,k):
    vs = [p for p in permutations(['U','V'] + [f'A{i}' for i in range(t)]
                                     + [f'B{i}' for i in range(t)])
          if width(p,t) <= k]
    keys = {p: i for i,p in enumerate(vs)}
    g = [[] for _ in vs]
    for j,p in enumerate(vs):
        for i in range(len(p)-1):
            q=p[:i]+(p[i+1],p[i])+p[i+2:]
            if q in keys: g[j].append(keys[q])
    seen = set(); sizes=[]; orientations=[]
    for i in range(len(vs)):
        if i in seen: continue
        queue=deque([i]);seen.add(i);component=[]
        while queue:
            v=queue.popleft();component.append(v)
            for w in g[v]:
                if w not in seen:
                    seen.add(w);queue.append(w)
        sizes.append(len(component))
        orientations.append({vs[v].index('U') < vs[v].index('V') for v in component})
    return vs, sorted(sizes),orientations


def main():
    for t in range(1,4):
        for k in [t,t+1]:
            vs,sizes,orients=full(t,k)
            per_side=symbolic_count(t,k)*factorial(t)**2
            assert len(vs)==2*per_side, (t,k,len(vs),per_side)
            assert sizes==([per_side,per_side] if k==t else [2*per_side]), (t,k,sizes)
            if k==t: assert all(len(o)==1 for o in orients)
            for state in vs:
                if state.index('U') < state.index('V'):
                    normalize(state,t,k)
            print('exhaustive',t,k,len(vs),sizes,flush=True)
        check_bridge(t)
    # Independent edge-counting formula for all symbolic placements,
    # and random-state route checks across arbitrarily chosen labels.
    rng = random.Random(1425)
    for t in range(4,15):
        check_bridge(t)
        for k in [t,t+1,t+2]:
            good=0
            for trial in range(350):
                q = ['U','V'] + [f'A{i}' for i in range(t)] + [f'B{i}' for i in range(t)]
                rng.shuffle(q)
                if q.index('U') < q.index('V') and width(q,t) <= k:
                    normalize(q,t,k);good += 1
            if good:print('sample',t,k,good,flush=True)
    print('symbolic component orders',[(t, factorial(t)**2*symbolic_count(t,t)) for t in range(1,9)])
    print('ALL CHECKS PASS')

if __name__ == '__main__': main()
