"""Finite independent checks for rooted singular transformation semigroup theorem.

Composition is right action: first f, then g. This is finite
corroboration, not a proof of the theorem for all n.
"""
import itertools
import math


def arc(n, source, target):
    return tuple(target if x == source else x for x in range(n))


def compose(a, b):
    return tuple(b[x] for x in a)


def singular_pointed(n):
    return {
        (0,) + t
        for t in itertools.product(range(n), repeat=n-1)
        if len({0, *t}) < n
    }


def closure(generators):
    seen = set(generators)
    pending = list(seen)
    while pending:
        f = pending.pop()
        for e in generators:
            h = compose(f, e)
            if h not in seen:
                seen.add(h)
                pending.append(h)
    return seen


def tournaments(m):
    pairs = list(itertools.combinations(range(1, m+1), 2))
    for mask in range(1 << len(pairs)):
        arcs = [
            (a, b) if (mask >> i) & 1 else (b, a)
            for i, (a, b) in enumerate(pairs)
        ]
        yield arcs


def strong(m, arcs):
    adj = {v: [] for v in range(1, m+1)}
    for a, b in arcs:
        adj[a].append(b)
    for root in adj:
        visited = {root}
        todo = [root]
        while todo:
            for v in adj[todo.pop()]:
                if v not in visited:
                    visited.add(v)
                    todo.append(v)
        if len(visited) != m:
            return False
    return True


def full_generators(n, arcs):
    return [arc(n, i, 0) for i in range(1, n)] + [
        arc(n, i, j) for i, j in arcs
    ]


def recurrence(m):
    s = [0] * (m+1)
    s[1] = 1
    for n in range(2, m+1):
        s[n] = 2 ** (n*(n-1)//2) - sum(
            math.comb(n, k) * s[k] * 2 ** ((n-k)*(n-k-1)//2)
            for k in range(1, n)
        )
    return s


def main():
    assert len(closure([arc(2, 1, 0)])) == 1
    assert closure(full_generators(3, [(1, 2), (2, 1)])) == singular_pointed(3)
    for n in (4, 5):
        target = singular_pointed(n)
        positives = 0
        for arcs in tournaments(n-1):
            hit = closure(full_generators(n, arcs)) == target
            assert hit == strong(n-1, arcs), (n, arcs, hit)
            positives += hit
        assert positives == recurrence(n-1)[-1]
        print(f'n={n}: {len(target)} singular maps; {positives} minimal generating tournaments')
    # All arc sets of the cyclic tournament on five movable points.
    n = 6
    m = n-1
    cyc = [
        (i, j) for i in range(1, n) for j in range(1, n)
        if (j-i) % m in {1, 2}
    ]
    assert len(cyc) == math.comb(m, 2)
    assert strong(m, cyc)
    target = singular_pointed(n)
    assert closure(full_generators(n, cyc)) == target
    print(f'n={n}: {len(target)} singular maps; cyclic tournament generates all')
    assert recurrence(6)[1:] == [1, 0, 2, 24, 544, 22320]
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
