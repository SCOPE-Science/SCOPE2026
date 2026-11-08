"""Exact verification of a minimal contact-addition SIR lifetime reversal.

Requires Python 3 and SymPy. This code enumerates every graph up to
three vertices and every possible addition of one missing undirected edge.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
import sympy as sp


def edges_of_mask(vertices, mask):
    options = list(combinations(range(vertices), 2))
    return tuple(e for j, e in enumerate(options) if mask & (1 << j))


def outgoing(state, edges, beta):
    nbrs = [set() for _ in state]
    for a, b in edges:
        nbrs[a].add(b)
        nbrs[b].add(a)
    for vertex, condition in enumerate(state):
        if condition == 1:
            y = list(state)
            y[vertex] = 2
            yield (beta * 0 + 1, tuple(y), 0)
        if condition == 0:
            infected_neighbors = sum(state[u] == 1 for u in nbrs[vertex])
            if infected_neighbors:
                y = list(state)
                y[vertex] = 1
                yield (beta * infected_neighbors, tuple(y), 1)


def backward(n, edges, seed, beta):
    @lru_cache(None)
    def h(state):
        if 1 not in state:
            return beta * 0, beta * 0
        events = list(outgoing(state, edges, beta))
        q = sum((r for r, _, _ in events), beta * 0)
        time = (beta * 0 + 1) / q
        new_cases = beta * 0
        for rate, nxt, infection in events:
            future_t, future_c = h(nxt)
            time += rate / q * future_t
            new_cases += rate / q * (future_c + infection)
        return time, new_cases
    return h(tuple(1 if v == seed else 0 for v in range(n)))


def forward(n, edges, seed, beta):
    """Independent forward state-probability computation in an acyclic chain."""
    initial = tuple(1 if v == seed else 0 for v in range(n))
    mass = {initial: Fraction(1)}
    time = Fraction(0)
    new_cases = Fraction(0)
    for state in sorted(product(range(3), repeat=n), key=sum):
        weight = mass.get(state, Fraction(0))
        if not weight or 1 not in state:
            continue
        events = list(outgoing(state, edges, beta))
        q = sum(rate for rate, _, _ in events)
        time += weight / q
        for rate, nxt, case in events:
            probability = weight * rate / q
            mass[nxt] = mass.get(nxt, Fraction(0)) + probability
            new_cases += probability * case
    assert sum(weight for state, weight in mass.items() if 1 not in state) == 1
    return time, new_cases


def verify():
    beta = sp.symbols('beta', positive=True)
    comparisons = 0
    positive_cases = 0
    zero_cases = 0
    for n in (1, 2, 3):
        all_edges = list(combinations(range(n), 2))
        for mask in range(1 << len(all_edges)):
            base = edges_of_mask(n, mask)
            for edge in all_edges:
                if edge in base:
                    continue
                for seed in range(n):
                    earlier, _ = backward(n, base, seed, beta)
                    later, _ = backward(n, base + (edge,), seed, beta)
                    diff = sp.cancel(later - earlier)
                    numerator, denominator = sp.fraction(diff)
                    # Every nonzero polynomial coefficient is nonnegative;
                    # denominators have strictly positive constant terms.
                    p = sp.Poly(numerator, beta)
                    q = sp.Poly(denominator, beta)
                    assert all(int(a) >= 0 for a in p.all_coeffs()), (n, base, edge, seed, diff)
                    assert all(int(a) >= 0 for a in q.all_coeffs()) and q.eval(0) > 0
                    comparisons += 1
                    if numerator == 0:
                        zero_cases += 1
                    else:
                        positive_cases += 1
    assert comparisons == 38, comparisons
    base = ((0, 2), (0, 3), (1, 2), (1, 3))
    augmented = base + ((0, 1),)
    seed = 2
    b = Fraction(10)
    bt, bc = backward(4, base, seed, b)
    at, ac = backward(4, augmented, seed, b)
    assert bt == Fraction(3961259, 1928619)
    assert at == Fraction(1329351899, 648015984)
    assert at - bt == -Fraction(1631125, 648015984)
    assert ac - bc == Fraction(8200, 586971)
    assert (bt, bc) == forward(4, base, seed, b)
    assert (at, ac) == forward(4, augmented, seed, b)
    print('PASS: symbolic small-graph comparisons =', comparisons,
          'positive =', positive_cases, 'zero =', zero_cases)
    print('PASS: exact backward and independent forward SIR expectations')
    print('original expected duration =', bt)
    print('augmented expected duration =', at)
    print('duration change =', at - bt)
    print('expected final size increase =', ac - bc)


if __name__ == '__main__':
    verify()
