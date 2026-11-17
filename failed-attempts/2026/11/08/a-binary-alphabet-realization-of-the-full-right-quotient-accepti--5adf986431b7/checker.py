"""Finite checks for the binary right-quotient permutation-automaton construction.

Run with Python 3.9 or newer. All checks are exact integer computations.
"""
from collections import deque
from itertools import combinations
from math import factorial, gcd


def compose(p, q):
    """First act by p, then act by q."""
    return tuple(q[p[x]] for x in range(len(p)))


def transformations(k, r):
    identity = tuple(range(k))
    cycle = tuple((x + 1) % k for x in range(k))
    trans = tuple((1 if x == 0 else (0 if x == 1 else x)) for x in range(k))
    return (identity, cycle, trans), (((cycle, 1), (trans, 0)))


def full_group(k, r):
    (identity, cycle, trans), letters = transformations(k, r)
    seen = {(identity, 0)}
    q = deque(seen)
    while q:
        perm, residue = q.popleft()
        for gen, increment in letters:
            nxt = (compose(perm, gen), (residue + increment) % r)
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
    assert len(seen) == factorial(k) * r, (k, r, len(seen))
    return seen


def min_classes(states, start, transition, final):
    reached = {start}
    queue = deque([start])
    while queue:
        s = queue.popleft()
        for letter in range(2):
            t = transition(s, letter)
            if t not in reached:
                reached.add(t)
                queue.append(t)
    assert reached == set(states), (len(reached), len(states))
    blocks = [frozenset(reached & set(final)), frozenset(reached - set(final))]
    blocks = [b for b in blocks if b]
    while True:
        which = {s:i for i,b in enumerate(blocks) for s in b}
        next_blocks = []
        for b in blocks:
            buckets = {}
            for s in b:
                signature = tuple(which[transition(s,l)] for l in range(2))
                buckets.setdefault(signature, set()).add(s)
            next_blocks.extend(frozenset(x) for x in buckets.values())
        if len(next_blocks) == len(blocks):
            return len(blocks)
        blocks = next_blocks


def check(k, r, m):
    (identity, cycle, trans), letters = transformations(k, r)
    assert 1 <= m <= k-1 and r >= 2
    group = full_group(k, r)
    # First component of accepted words from B: exactly permutations fixing k-1.
    projected = {p for p, z in group if p[k-1] == k-1 and z != r-1}
    stabilizer = {p for p,z in group if p[k-1] == k-1}
    assert projected == stabilizer
    assert len(projected) == factorial(k-1)
    # Exact quotient final set, computed from all accepted group elements.
    quotient_final = {s for s in range(k)
                      if any(p[s] < m for p in projected)}
    assert quotient_final == set(range(k-1)), (k, r, m, quotient_final)
    alpha_transition = lambda s, letter: letters[letter][0][s]
    beta_transition = lambda st, letter: (
        letters[letter][0][st[0]], (st[1] + letters[letter][1]) % r)
    A_states = tuple(range(k))
    B_states = tuple((p,z) for p in range(k) for z in range(r))
    A_final = set(range(m))
    B_final = {(k-1,z) for z in range(r-1)}
    assert min_classes(A_states, 0, alpha_transition, A_final) == k
    assert min_classes(B_states, (k-1,0), beta_transition, B_final) == k*r
    assert min_classes(A_states, 0, alpha_transition, quotient_final) == k
    # The key relation: sigma*tau has order k-1, and gcd(k,k-1)=1.
    sigmatau = compose(cycle, trans)
    cur = identity
    for _ in range(k-1):
        cur = compose(cur, sigmatau)
    assert cur == identity and gcd(k,k-1) == 1
    return len(group)


def main():
    cases, total_group, total_quotients = 0, 0, 0
    for k in range(2, 7):
        for r in range(2, 5):
            for m in range(1, k):
                total_group += check(k, r, m)
                cases += 1
                total_quotients += k-1
    print(f'PASS: {cases} complete (k,r,m) parameter cases; '
          f'{total_group} exact group-state checks (including repeats); '
          f'{total_quotients} quotient accepting-state checks; '
          'each A, B, and quotient DFA reachable and pairwise distinguishable')


if __name__ == '__main__':
    main()
