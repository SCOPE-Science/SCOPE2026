"""Exact small-DAG census and independent directed-reachability checks.

Requires only Python 3 standard library. Run: python verify.py
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations

N = 6
EDGES = tuple(combinations(range(N), 2))
INTERNAL = (1, 2, 3, 4)


def dynamic_reach(adj, alive):
    # Reachability in the displayed topological order, terminals protected.
    reached = 1
    for u in range(N):
        if reached & (1 << u):
            for v in adj[u]:
                if v == N-1 or (alive & (1 << v)):
                    reached |= 1 << v
    return int(bool(reached & (1 << (N-1))))


def breadth_first_reach(edges, alive):
    # Independent search: no dependence on acyclic order.
    seen = {0}
    todo = [0]
    while todo:
        u = todo.pop()
        for x, y in edges:
            if x != u or y in seen or (y != N-1 and not(alive & (1 << y))):
                continue
            seen.add(y)
            todo.append(y)
    return int(N-1 in seen)


def sign_changes(triple):
    # The exact quadratic is a(1-p)^2+b p(1-p)+c p^2.
    a, b, c = map(Fraction, triple)
    linear = -2*a+b
    quadratic = a-b+c
    xs = [Fraction(0), Fraction(1)]
    if quadratic:
        vertex = -linear/(2*quadratic)
        if 0 < vertex < 1:
            xs.append(vertex)
    vals = [a+linear*x+quadratic*x*x for x in xs]
    return min(vals) < 0 < max(vals)


def full_census():
    patterns = Counter()
    for graph_bits in range(1 << len(EDGES)):
        adj = [[] for _ in range(N)]
        for idx, (u, v) in enumerate(EDGES):
            if graph_bits & (1 << idx):
                adj[u].append(v)
        values = [dynamic_reach(adj, state) for state in range(1 << N)]
        for u, v in combinations(INTERNAL, 2):
            w, z = [x for x in INTERNAL if x not in (u, v)]
            d = []
            for aw, az in ((0, 0), (1, 0), (0, 1), (1, 1)):
                r = aw << w | az << z
                def g(a, b):
                    return values[r | (a << u) | (b << v)]
                d.append(g(1, 1)-g(1, 0)-g(0, 1)+g(0, 0))
            patterns[(d[0], d[1]+d[2], d[3])] += 1
    assert sum(patterns.values()) == 196608
    assert len(patterns) == 18
    switching = {k: v for k, v in patterns.items() if sign_changes(k)}
    assert switching == {(1, 0, -1): 24}, switching
    return patterns


WITNESS = ((0, 1), (0, 3), (1, 2), (1, 4), (2, 5), (3, 4), (4, 5))
# Protected pair u=1, v=4. Other intermediate taxa w=2 and z=3.

def witness_check():
    adj = [[] for _ in range(N)]
    for u, v in WITNESS:
        adj[u].append(v)
    for state in range(1 << N):
        assert dynamic_reach(adj, state) == breadth_first_reach(WITNESS, state)
    for state in range(1 << N):
        # All directed source-to-target paths use (1,2), (1,4), or (3,4).
        actual = breadth_first_reach(WITNESS, state)
        expected = int(bool((state & 2 and state & 4) or
                            (state & 2 and state & 16) or
                            (state & 8 and state & 16)))
        assert actual == expected
    # Exact probabilities, independently summed over all 16 assignments.
    for pu in (Fraction(1, 7), Fraction(1, 2), Fraction(4, 5)):
        for pv in (Fraction(1, 3), Fraction(5, 6)):
            for pw in (Fraction(1, 5), Fraction(2, 3)):
                for pz in (Fraction(2, 7), Fraction(3, 4)):
                    parameters = {1: pu, 2: pw, 3: pz, 4: pv}
                    def prob(protected):
                        result = Fraction(0)
                        for state in range(1 << N):
                            if (state & 33) != 33:
                                continue  # Source and target are permanently present.
                            weight = Fraction(1)
                            for i, q in parameters.items():
                                qi = Fraction(1) if i in protected else q
                                weight *= qi if state & (1 << i) else (1-qi)
                            result += weight * breadth_first_reach(WITNESS, state)
                        return result
                    inter = prob({1, 4})-prob({1})-prob({4})+prob(set())
                    formula = (1-pu)*(1-pv)*(1-pw-pz)
                    assert inter == formula, (inter, formula)
    return 24


def main():
    cases = full_census()
    assert witness_check() == 24
    print('PASS: all 32768 topologically ordered six-vertex DAGs')
    print('PASS: 196608 DAG/protected-pair cases, 18 exact profiles')
    print('PASS: 24 reversing cases, all at p = 1/2')
    print('PASS: independent breadth-first witness reachability, 64 states')
    print('PASS: 24 exact heterogeneous probability comparisons')


if __name__ == '__main__':
    main()
