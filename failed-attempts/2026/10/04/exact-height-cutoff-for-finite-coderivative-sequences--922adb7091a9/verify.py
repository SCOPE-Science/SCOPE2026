#!/usr/bin/env python3
import itertools

def is_poset(n, rel):
    for i in range(n):
        if (i, i) not in rel:
            return False
    for i in range(n):
        for j in range(n):
            if i != j and (i, j) in rel and (j, i) in rel:
                return False
    for i in range(n):
        for j in range(n):
            if (i, j) in rel:
                for k in range(n):
                    if (j, k) in rel and (i, k) not in rel:
                        return False
    return True

def strict_succ(n, rel, w):
    return [v for v in range(n) if v != w and (w, v) in rel]

def upsets(n, rel):
    ans = []
    for mask in range(1 << n):
        X = {i for i in range(n) if (mask >> i) & 1}
        if all(v in X for u in X for v in range(n) if (u, v) in rel):
            ans.append(X)
    return ans

def nabla(n, rel, X):
    return {w for w in range(n) if all(v in X for v in strict_succ(n, rel, w))}

def iterate(n, rel, X, k):
    Y = set(X)
    for _ in range(k):
        Y = nabla(n, rel, Y)
    return Y

def height(n, rel, Q):
    if not Q:
        return 0
    memo = {}
    def h(w):
        if w not in memo:
            memo[w] = 1 + max([h(v) for v in strict_succ(n, rel, w) if v in Q] or [0])
        return memo[w]
    return max(h(w) for w in Q)

def has_chain(n, rel, Q, w, length):
    if w not in Q:
        return False
    if length == 1:
        return True
    return any(has_chain(n, rel, Q, v, length - 1)
               for v in strict_succ(n, rel, w) if v in Q)

posets_by_n = {}
for n in range(1, 5):
    pairs = [(i, j) for i in range(n) for j in range(n)]
    posets = []
    for mask in range(1 << len(pairs)):
        rel = {pairs[k] for k in range(len(pairs)) if (mask >> k) & 1}
        if is_poset(n, rel):
            posets.append(rel)
    posets_by_n[n] = posets

    for rel in posets:
        U = upsets(n, rel)
        top = set(range(n))
        fixed = [X for X in U if nabla(n, rel, X) == X]
        assert fixed == [top]

        for X in U:
            Q = top - X
            hq = height(n, rel, Q)
            for k in range(n + 2):
                Y = iterate(n, rel, X, k)
                for w in range(n):
                    assert (w not in Y) == has_chain(n, rel, Q, w, k + 1)
                assert (Y == top) == (k >= hq)

# Independent exhaustive semantic check for small posets.
for n in range(1, 4):
    for rel in posets_by_n[n]:
        U = upsets(n, rel)
        top = set(range(n))
        h = height(n, rel, top)
        for N in range(0, 4):
            valuations = itertools.product(U, repeat=N + 1)
            models = []
            for vals in valuations:
                if all(nabla(n, rel, vals[j + 1]) <= vals[j] for j in range(N)):
                    models.append(vals)
            assert models
            for i in range(N + 1):
                forced = all(vals[i] == top for vals in models)
                assert forced == (N - i >= h), (n, N, i, h)

print("VERIFY_OK")
