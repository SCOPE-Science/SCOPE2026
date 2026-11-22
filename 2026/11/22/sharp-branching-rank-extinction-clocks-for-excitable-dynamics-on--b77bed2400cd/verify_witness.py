#!/usr/bin/env python3
"""Independent constructive tests of sharp worst-case clocks on trees.
No third-party dependencies: integer-indexed parent arrays and explicit phase updates.
"""
import random


def height(adjacency, theta, root, forbid=-1):
    values = sorted((height(adjacency, theta, u, root) for u in adjacency[root] if u != forbid), reverse=True)
    return 1 + values[theta - 1] if len(values) >= theta else 0


def rooted_witness(adjacency, theta, root, target_h, forbid=-1):
    if target_h == 0:
        return [root]
    choices = []
    for u in adjacency[root]:
        if u == forbid:
            continue
        hu = height(adjacency, theta, u, root)
        if hu >= target_h - 1:
            choices.append((u, hu))
    assert len(choices) >= theta
    choices.sort(key=lambda q: (-q[1], q[0]))
    return sum((rooted_witness(adjacency, theta, v, target_h - 1, root)
                for v, _ in choices[:theta]), [])


def update(adjacency, theta, kappa, state):
    result = []
    for v, z in enumerate(state):
        result.append((z + 1) % kappa if z else int(sum(state[u] == 1 for u in adjacency[v]) >= theta))
    return result


def probe(adj, theta, kappa):
    hvals = [height(adj, theta, v) for v in range(len(adj))]
    h = max(hvals)
    root = hvals.index(h)
    leaves = rooted_witness(adj, theta, root, h)
    assert len(leaves) == theta ** h
    state = [0] * len(adj)
    for u in leaves:
        state[u] = 1
    clock = kappa - 1 + h
    for t in range(clock):
        assert any(state), ('early all-zero',t,clock)
        if t == h:
            assert state[root] == 1
        state = update(adj, theta, kappa, state)
    assert all(z == 0 for z in state)
    return clock


def random_tree(n, rng):
    a = [[] for _ in range(n)]
    for j in range(1, n):
        p = rng.randrange(j)
        a[p].append(j)
        a[j].append(p)
    return a


def full_tree(theta, h):
    a = [[]]
    frontier = [0]
    for _ in range(h):
        new = []
        for v in frontier:
            for _ in range(theta):
                u = len(a); a.append([v]); a[v].append(u); new.append(u)
        frontier = new
    return a


def main():
    rng = random.Random(42137)
    cases = 0
    for theta in range(2, 6):
        for kappa in range(3, 7):
            for h in range(4):
                adj = full_tree(theta, h)
                probe(adj, theta, kappa)
                cases += 1
            for n in range(1, 70):
                for _ in range(8):
                    adj = random_tree(n, rng)
                    exact = probe(adj, theta, kappa)
                    bound = kappa - 2
                    count = len(adj)
                    power = theta
                    while power <= (theta-1)*count+1:
                        bound += 1
                        power *= theta
                    assert exact <= bound
                    cases += 1
    print('PASS witness_cases=%d maximal_full_tree_depth=3 parameters_theta=2..5_kappa=3..6' % cases)

if __name__ == '__main__':
    main()
