"""Direct, finite vertex-subset verifier for matching-deleted biclique visibility."""
from collections import Counter, deque
from itertools import combinations


def graph(n, t):
    N = 2*n
    nb = [set() for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i == j and i < t:
                continue
            nb[i].add(n+j)
            nb[n+j].add(i)
    return nb


def distance(nb, start, allowed):
    todo = deque([start]); dis = {start: 0}
    while todo:
        u = todo.popleft()
        for v in nb[u]:
            if v in allowed and v not in dis:
                dis[v] = dis[u] + 1
                todo.append(v)
    return dis


def connected_visible(nb, sel, ambient_dist=None):
    if not sel:
        return False
    todo = [next(iter(sel))]; seen = set(todo)
    for u in todo:
        for v in nb[u] & sel:
            if v not in seen:
                seen.add(v); todo.append(v)
    if seen != sel:
        return False
    ambient_dist = ambient_dist or [distance(nb, v, set(range(len(nb)))) for v in range(len(nb))]
    for u, v in combinations(sorted(sel), 2):
        if ambient_dist[u][v] == 1:
            continue
        allowed = set(range(len(nb))) - sel | {u, v}
        if distance(nb, u, allowed).get(v, 100000) != ambient_dist[u][v]:
            return False
    return True


def predicted(n, t):
    assert n >= 4 and 0 <= t <= n
    if t == n:
        expected = []
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                expected.append(set(range(2*n)) - {i, n+i, n+j})
                expected.append(set(range(2*n)) - {n+i, i, j})
        return 2*n-3, {frozenset(x) for x in expected}
    expected = [set(range(2*n)) - {i, n+j} for i in range(t, n) for j in range(t, n)]
    if t == 1:
        expected.append(set(range(2*n)) - {0, n})
    return 2*n-2, {frozenset(x) for x in expected}


def exhaustive(n, t):
    nb = graph(n, t)
    ad = [distance(nb, v, set(range(2*n))) for v in range(2*n)]
    best = 0; maxima = set()
    for mask in range(1, 1 << (2*n)):
        k = mask.bit_count()
        if k < best:
            continue
        S = {v for v in range(2*n) if mask >> v & 1}
        if connected_visible(nb, S, ad):
            if k > best:
                best = k; maxima = set()
            maxima.add(frozenset(S))
    want_n, want = predicted(n,t)
    assert best == want_n, (n,t,best,want_n)
    assert maxima == want, (n,t,len(maxima),len(want),maxima^want)
    return best, len(maxima)


def top_levels(n,t):
    nb=graph(n,t)
    ad=[distance(nb,v,set(range(2*n))) for v in range(2*n)]
    want_n,want=predicted(n,t)
    nmax=set()
    for omit_count in range(0, 2*n-want_n+1):
        for omitted in combinations(range(2*n),omit_count):
            S=set(range(2*n))-set(omitted)
            if connected_visible(nb,S,ad):
                if len(S)>want_n:raise AssertionError((n,t,S))
                nmax.add(frozenset(S))
    assert nmax==want, (n,t,len(nmax),len(want))
    return want_n, len(nmax)

if __name__ == '__main__':
    for n in range(4,8):
        print('EXHAUSTIVE_ORDER',n,[(t,exhaustive(n,t)) for t in range(n+1)],flush=True)
    for t in range(9):
        print('TOP_LEVEL_ORDER8',t,top_levels(8,t),flush=True)
    print('VERIFY_OK')
