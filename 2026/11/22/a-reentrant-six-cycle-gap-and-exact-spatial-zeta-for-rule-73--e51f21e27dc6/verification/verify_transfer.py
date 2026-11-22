#!/usr/bin/env python3
"""Exact, reproducible finite-history calculation for Rule 73's temporal-six orbits.

No external libraries or network access. Integer arithmetic certifies every
coefficient of the determinant polynomials; the graph construction supplies
an all-spatial-circumference proof rather than finite-size extrapolation.
"""
from collections import defaultdict
from fractions import Fraction

RULE = 73


def graph(t):
    q = 1 << t
    edges = defaultdict(list)
    for a in range(q):
        for b in range(q):
            for c in range(q):
                if all(((b >> ((j + 1) % t)) & 1)
                       == ((RULE >> (4 * ((a >> j) & 1)
                                   + 2 * ((b >> j) & 1)
                                   + ((c >> j) & 1))) & 1)
                       for j in range(t)):
                    edges[a * q + b].append(b * q + c)
    return dict(edges)


def cyclic_components(edges):
    vertices = set(edges)
    rev = defaultdict(list)
    for u, destinations in edges.items():
        for v in destinations:
            vertices.add(v)
            rev[v].append(u)
    visited, finishing = set(), []
    for start in sorted(vertices):
        if start in visited:
            continue
        visited.add(start)
        dfs = [(start, 0)]
        while dfs:
            u, i = dfs[-1]
            destinations = edges.get(u, ())
            if i == len(destinations):
                finishing.append(u)
                dfs.pop()
                continue
            v = destinations[i]
            dfs[-1] = (u, i + 1)
            if v not in visited:
                visited.add(v)
                dfs.append((v, 0))
    visited.clear()
    result = []
    for start in reversed(finishing):
        if start in visited:
            continue
        visited.add(start)
        stack, component = [start], []
        while stack:
            u = stack.pop()
            component.append(u)
            for v in rev[u]:
                if v not in visited:
                    visited.add(v)
                    stack.append(v)
        if len(component) > 1 or start in edges.get(start, ()):
            result.append(sorted(component))
    return result


def multiply(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return result


def determinant(component, edges):
    """Newton identities applied to all exact closed-walk trace coefficients."""
    d = len(component)
    trace = [0] * (d + 1)
    for start in component:
        current = {start: 1}
        for k in range(1, d + 1):
            nxt = defaultdict(int)
            for u, count in current.items():
                for v in edges.get(u, ()):
                    nxt[v] += count
            current = nxt
            trace[k] += current.get(start, 0)
    coefficients = [1]
    for k in range(1, d + 1):
        numerator = -sum(coefficients[k - j] * trace[j]
                         for j in range(1, k + 1))
        assert numerator % k == 0
        coefficients.append(numerator // k)
    return coefficients


# Constant coefficient first; no symbolic software needed to verify.
A = [1, 0, 0, -1, -1]
B = [1, 0, -2, -1, 1]
C = [1, 0, 0, -1, -3, -2, 0, -1, 1, 2]
E = [1, 0, -1, -1, -3, -3, 3, 1, 1, 7, 3, -2]
FACTORS = {
    1: [(A, 1)],
    2: [([1, -1], 2), ([1, 0, 1], 2), (B, 1)],
    3: [([1, 1, 1], 2), ([1, -1, 0, 1], 2), (C, 1)],
    6: [([1, -1], 5), ([1, 1], 3), ([1, 0, 1], 4),
        ([1, 0, 0, 0, 1], 3), ([1, 1, 1], 2),
        ([1, -1, 0, 1], 2), (E, 1)],
}


def expanded(factors):
    output = [1]
    for factor, multiplicity in factors:
        for _ in range(multiplicity):
            output = multiply(output, factor)
    return output


def trace_from_determinant(coefficients, limit):
    """Trace series identity D(z)*sum(T_n z^n)=-z D'(z)."""
    output = [0] * (limit + 1)
    for n in range(1, limit + 1):
        right = -n * coefficients[n] if n < len(coefficients) else 0
        output[n] = right - sum(coefficients[j] * output[n - j]
                                for j in range(1, min(n, len(coefficients)-1)+1))
    return output


def column_has_period(value, divisor, t=6):
    return all(((value >> j) & 1) == ((value >> ((j + divisor) % t)) & 1)
               for j in range(t))


def explicit_walk(edges, start, ends, length):
    """Return one closed path of given length visiting any node from `ends`."""
    cur = {(start, False): None}
    parents = []
    for _ in range(length):
        nxt = {}
        for (u, flag) in sorted(cur):
            for v in edges.get(u, ()):
                state = (v, flag or v in ends)
                if state not in nxt:
                    nxt[state] = (u, flag)
        parents.append(nxt)
        cur = nxt
    goal = (start, True)
    if goal not in cur:
        return None
    vertices = [start] * (length + 1)
    state = goal
    for pos in range(length - 1, -1, -1):
        vertices[pos+1] = state[0]
        state = parents[pos][state]
    vertices[0] = start
    assert vertices[-1] == start
    assert any(v in ends for v in vertices)
    assert all(vertices[k+1] in edges.get(vertices[k], ()) for k in range(length))
    return vertices


def has_directed_cycle_of_length(edges, nodes, length):
    nodes = set(nodes)
    for v in nodes:
        current = {v}
        for _ in range(length):
            current = {w for u in current for w in edges.get(u, ()) if w in nodes}
        if v in current:
            return True
    return False


def perron_enclosure(edges, nodes):
    """Collatz-Wielandt rational inequalities using A^180 1."""
    nodes = set(nodes)
    current = {v: 1 for v in nodes}
    for _ in range(180):
        current = {v: sum(current[w] for w in edges.get(v, ()) if w in nodes)
                   for v in nodes}
    next_vals = {v: sum(current[w] for w in edges.get(v, ()) if w in nodes)
                 for v in nodes}
    assert min(current.values()) > 0
    return min(Fraction(next_vals[v], current[v]) for v in nodes), max(Fraction(next_vals[v], current[v]) for v in nodes)


def main():
    graphs, comps, traces = {}, {}, {}
    for t in (1, 2, 3, 6):
        edges = graph(t)
        graph_components = cyclic_components(edges)
        D = [1]
        for comp in graph_components:
            D = multiply(D, determinant(comp, edges))
        expected = expanded(FACTORS[t])
        assert D == expected, (t, 'polynomial coefficients differ')
        graphs[t], comps[t] = edges, graph_components
        traces[t] = trace_from_determinant(D, 70)
        print('temporal_divisor', t, 'cyclic_components',
              sorted((len(c) for c in graph_components), reverse=True),
              'determinant_degree', len(D)-1)

    N6 = [traces[6][n] - traces[3][n] - traces[2][n] + traces[1][n]
          for n in range(71)]
    assert all(v >= 0 and v % 6 == 0 for v in N6[1:])
    assert [N6[n] for n in range(1, 17)] == [0,0,0,0,0,0,0,24,0,0,0,72,78,84,270,696]
    print('primitive_six_states_first_16', [N6[n] for n in range(1, 17)])

    main_component = max(comps[6], key=len)
    assert len(main_component) == 23
    core_det = determinant(main_component, graphs[6])
    core_expected = expanded([([1,0,1],1), ([1,1,1],2),
                             ([1,-1,0,1],2), (E,1)])
    assert core_det == core_expected
    for comp in comps[6]:
        if len(comp) == 8:
            assert determinant(comp, graphs[6]) == [1,0,0,0,0,0,0,0,-1]
            assert sum(1 for u in comp for w in graphs[6].get(u, ()) if w in comp) == 8
    assert has_directed_cycle_of_length(graphs[6], main_component, 3)
    assert has_directed_cycle_of_length(graphs[6], main_component, 4)
    core = set(main_component)
    two = {v for v in core if column_has_period(v//64,2)
           and column_has_period(v%64,2)
           and not (column_has_period(v//64,3) and column_has_period(v%64,3))}
    three = {v for v in core if column_has_period(v//64,3)
             and column_has_period(v%64,3)
             and not (column_has_period(v//64,2) and column_has_period(v%64,2))}
    assert 21 in two and len(three) == 15
    for length in range(12,24):
        witness = explicit_walk(graphs[6],21,three,length)
        assert witness is not None
        assert any(v in two for v in witness)
        print('mixed_clock_return_length',length,'walk',','.join(map(str,witness)))
    for t in (2,3,6):
        lo,hi=perron_enclosure(graphs[t], max(comps[t],key=len))
        print('temporal_divisor',t,'Perron_bound',format(float(lo),'.12f'),format(float(hi),'.12f'))
        if t == 6: assert Fraction(161574,100000)<lo<=hi<Fraction(161576,100000)
        if t == 3: assert hi < Fraction(15458,10000)
        if t == 2: assert hi < Fraction(14903,10000)
    print('EXACT_TRANSFER_OK')

if __name__ == '__main__':
    main()
