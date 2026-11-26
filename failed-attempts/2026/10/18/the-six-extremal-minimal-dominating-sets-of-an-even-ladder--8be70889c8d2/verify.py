#!/usr/bin/env python3
"""Exact, standalone certificate for the maximal minimal dominating sets of ladders.

Run: python3 verify.py. No third-party dependencies.
"""
from collections import deque, defaultdict
from itertools import product

OUT = 4
PATTERNS = ((1,), (2,), (1, 2), (2, 1), (3, 0, 0, 3), (0, 3, 3, 0))


def selected(symbol, row):
    return symbol != OUT and bool(symbol & (1 << row))


def locally_valid(a, b, c, d, e):
    """Domination and private neighbors at center of five columns."""
    if c == OUT:
        return True
    columns = (a, b, c, d, e)

    def neighborhood(j, row):
        vertices = [(j, row), (j, 1 - row)]
        for k in (j - 1, j + 1):
            if 0 <= k < 5 and columns[k] != OUT:
                vertices.append((k, row))
        return vertices

    for row in (0, 1):
        near = neighborhood(2, row)
        if not any(selected(columns[j], r) for j, r in near):
            return False
        if selected(c, row):
            private = False
            for j, r in near:
                # A private vertex w of a selected vertex v has N[w] cap D={v}.
                if sum(selected(columns[k], s) for k, s in neighborhood(j, r)) == 1:
                    private = True
                    break
            if not private:
                return False
    return True


def build_automaton():
    # State=(last four symbols, phase, has_real); phase 0=body,1/2=closing.
    start = ((OUT,) * 4, 0, False)
    seen = {start}
    queue = deque([start])
    edges = defaultdict(list)
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        memory, phase, has_real = u
        if phase == 2:
            continue
        additions = range(4) if phase == 0 else (OUT,)
        if phase == 0 and has_real:
            additions = (0, 1, 2, 3, OUT)
        for sym in additions:
            if not locally_valid(*memory, sym):
                continue
            next_phase = 1 if phase == 0 and sym == OUT else 2 if phase == 1 else 0
            v = (memory[1:] + (sym,), next_phase, has_real or sym != OUT)
            # The central column is inspected exactly once; weight = |D|-n.
            weight = 0 if memory[2] == OUT else memory[2].bit_count() - 1
            edges[u].append((v, sym, weight))
            if v not in seen:
                seen.add(v)
                queue.append(v)
    return start, order, edges


def automaton_certificate():
    start, order, edges = build_automaton()
    terminals = {u for u in order if u[1] == 2}
    assert len(order) == 229 and sum(map(len, edges.values())) == 471
    assert len(terminals) == 10
    minus_inf = -10**9
    potential = {u: minus_inf for u in order}
    potential[start] = 0
    # Longest-path Bellman--Ford, with no positive-weight cycle reachable.
    for _ in range(len(order)):
        changed = False
        for u in order:
            for v, _, weight in edges[u]:
                if potential[u] != minus_inf and potential[v] < potential[u] + weight:
                    potential[v] = potential[u] + weight
                    changed = True
        if not changed:
            break
    else:
        raise AssertionError("potential did not stabilize (positive cycle)")
    assert all(potential[u] != minus_inf for u in order)
    assert all(potential[v] >= potential[u] + w
               for u in order for v, _, w in edges[u])
    assert max(potential[u] for u in terminals) == 0
    assert sorted(potential[u] for u in terminals) == [-1, -1] + [0] * 8

    # Only paths using equality (tight) arcs and ending at best terminal can
    # attain weight zero. Compute which states can reach such a terminal.
    predecessors = defaultdict(list)
    for u in order:
        for v, symbol, weight in edges[u]:
            if potential[v] == potential[u] + weight:
                predecessors[v].append(u)
    coreach = {u for u in terminals if potential[u] == 0}
    queue = deque(coreach)
    while queue:
        v = queue.popleft()
        for u in predecessors[v]:
            if u not in coreach:
                coreach.add(u)
                queue.append(u)
    assert start in coreach

    # Exact language-containment test for six periodic word families.
    # Bit j means candidate pattern j still matches the emitted real prefix.
    initial = (start, 0, (1 << len(PATTERNS)) - 1)
    seen = {initial}
    queue = deque([initial])
    bad_terminals = 0
    good_terminals = 0
    while queue:
        u, position_mod_4, candidate_mask = queue.popleft()
        if u in terminals:
            if candidate_mask == 0:
                bad_terminals += 1
            else:
                good_terminals += 1
            continue
        for v, symbol, weight in edges[u]:
            if v not in coreach or potential[v] != potential[u] + weight:
                continue
            new_mask = candidate_mask
            if symbol != OUT:
                new_mask = sum(
                    1 << j for j, pattern in enumerate(PATTERNS)
                    if (candidate_mask & (1 << j)) and
                    pattern[position_mod_4 % len(pattern)] == symbol
                )
            next_pos = (position_mod_4 + (symbol != OUT)) % 4
            state = (v, next_pos, new_mask)
            if state not in seen:
                seen.add(state)
                queue.append(state)
    assert bad_terminals == 0
    assert len(seen) == 91
    # These are full finite-state tests, not numerical extrapolation.
    print(f"certificate states={len(order)} transitions={sum(map(len, edges.values()))} terminals={len(terminals)}")
    print(f"longest terminal weight={max(potential[u] for u in terminals)} potential inequalities=PASS")
    print(f"tight pattern-product states={len(seen)} counterexamples={bad_terminals} accepted_product_terminal_states={good_terminals}")


def predicted(n):
    words = {
        tuple(pattern[j % len(pattern)] for j in range(n))
        for pattern in PATTERNS[:4]
    }
    if n % 2 == 0:
        words |= {
            tuple(pattern[j % len(pattern)] for j in range(n))
            for pattern in PATTERNS[4:]
        }
    return words


def exhaustive_checks():
    checked = 0
    total_minimal = 0
    for n in range(1, 10):
        N = 2 * n
        neighbors = []
        for col in range(n):
            for row in (0, 1):
                vertex = 2 * col + row
                adj = {vertex, 2 * col + 1 - row}
                if col > 0:
                    adj.add(2 * (col - 1) + row)
                if col + 1 < n:
                    adj.add(2 * (col + 1) + row)
                neighbors.append(sum(1 << w for w in adj))
        found = set()
        minimum_count = 0
        for subset in range(1 << N):
            checked += 1
            if any(subset & closed == 0 for closed in neighbors):
                continue
            if not all(
                any((subset & neighbors[w]) == (1 << v)
                    for w in range(N) if neighbors[v] & (1 << w))
                for v in range(N) if subset & (1 << v)
            ):
                continue
            minimum_count += 1
            if subset.bit_count() == n:
                found.add(tuple(sum((1 << row) for row in range(2)
                                    if subset & (1 << (2 * col + row)))
                                for col in range(n)))
            assert subset.bit_count() <= n
        assert found == predicted(n), (n, found ^ predicted(n))
        assert len(found) == (2 if n == 1 else 6 if n % 2 == 0 else 4)
        total_minimal += minimum_count
        print(f"bruteforce n={n} minimal={minimum_count} maxsize_count={len(found)}")
    print(f"bruteforce vertex subsets={checked} minimal_total={total_minimal} all=PASS")


if __name__ == '__main__':
    automaton_certificate()
    exhaustive_checks()
    print('VERIFY_OK')
