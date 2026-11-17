"""Exact checks of dihedral homology characters for cycle Mycielskians.

Reconstructs graphs and calculates reduced signed-Lefschetz numbers by a
vertex-orbit independence polynomial. Also checks small mod-two Betti ranks.
No external dependencies are required.
"""
from functools import lru_cache
from collections import Counter


def graph(n, ell):
    if n < 5 or n % 2 == 0 or n % 3 == 0 or ell < 0:
        raise ValueError('n must be odd, at least 5 and not divisible by 3')
    v = [(i, t) for t in range(ell + 1) for i in range(n)] + [('apex', -1)]
    edges = set()
    for t in range(ell):
        for i in range(n):
            for d in (-1, 1):
                edges.add(frozenset(((i, t), ((i + d) % n, t + 1))))
    for i in range(n):
        edges.add(frozenset(((i, 0), ('apex', -1))))
        for d in (-1, 1):
            edges.add(frozenset(((i, ell), ((i + d) % n, ell))))
    return v, edges


def at_minus_one(v, edges, action):
    orbits = []
    seen = set()
    for x in v:
        if x in seen:
            continue
        orbit = []
        y = x
        while y not in seen:
            seen.add(y)
            orbit.append(y)
            y = action(y)
        assert y == x
        orbits.append(orbit)
    index = {x: k for k, o in enumerate(orbits) for x in o}
    adjacent = [0] * len(orbits)
    allowed = (1 << len(orbits)) - 1
    for e in edges:
        x, y = tuple(e)
        i, j = index[x], index[y]
        if i == j:
            allowed &= ~(1 << i)
        else:
            adjacent[i] |= 1 << j
            adjacent[j] |= 1 << i

    @lru_cache(maxsize=None)
    def independent_value(mask):
        if not mask:
            return 1
        b = mask & -mask
        j = b.bit_length() - 1
        return independent_value(mask ^ b) - independent_value(mask & ~b & ~adjacent[j])

    return independent_value(allowed)


def path_value(m):
    a, b = 1, 0
    if m == 0:
        return a
    if m == 1:
        return b
    for _ in range(2, m + 1):
        a, b = b, b - a
    return b


def signs(n):
    return path_value((n - 1) // 2), -path_value(n + 1)


def sphere_degrees(n, ell):
    r = n // 3
    d = r - 1 if n % 3 == 1 else r
    e = 2 * r
    k, q = divmod(ell, 3)
    alpha, beta = signs(n)
    if q == 0:
        return {k * (e + 1): beta**k, d + k * (e + 1): alpha * beta**k}
    if q == 1:
        return {d + k * (e + 1) + 1: alpha * beta**k}
    return {(k + 1) * (e + 1) - 1: beta**(k + 1)}


def expected_trace(n, ell, reflect):
    return sum((-1)**degree * (orientation if reflect else 1)
               for degree, orientation in sphere_degrees(n, ell).items())


def reduced_lefschetz(n, ell, a, reflect):
    v, edges = graph(n, ell)
    def action(x):
        if x == ('apex', -1):
            return x
        i, t = x
        return (((-i if reflect else i) + a) % n, t)
    return -at_minus_one(v, edges, action)


def reduced_mod2_betti(n, ell):
    v, edges = graph(n, ell)
    index = {x: i for i, x in enumerate(v)}
    adj = [0] * len(v)
    for e in edges:
        x, y = tuple(e)
        i, j = index[x], index[y]
        adj[i] |= 1 << j
        adj[j] |= 1 << i
    faces = {}
    def append(mask, elig, count):
        faces.setdefault(count, []).append(mask)
        while elig:
            b = elig & -elig
            elig ^= b
            append(mask | b, elig & ~adj[b.bit_length() - 1], count + 1)
    append(0, (1 << len(v))-1, 0)
    ranks = {}
    for k in range(1, max(faces) + 1):
        lower = {face:i for i, face in enumerate(faces[k-1])}
        basis = {}
        for face in faces[k]:
            col = 0
            bits = face
            while bits:
                b = bits & -bits
                bits ^= b
                col ^= 1 << lower[face ^ b]
            while col:
                i = col.bit_length() - 1
                if i not in basis:
                    basis[i] = col
                    break
                col ^= basis[i]
        ranks[k] = len(basis)
    return {k-1:len(vect)-ranks.get(k,0)-ranks.get(k+1,0)
            for k,vect in faces.items()
            if len(vect)-ranks.get(k,0)-ranks.get(k+1,0)}, sum(map(len, faces.values()))


def main():
    cases = [(5, list(range(19))), (7, list(range(9))),
             (11, list(range(4))), (13, list(range(3)))]
    total = 0
    for n, levels in cases:
        alpha,beta = signs(n)
        assert (alpha,beta) in {(-1,-1), (-1,1), (1,-1), (1,1)}
        for ell in levels:
            for a in range(n):
                for reflect in (False, True):
                    actual = reduced_lefschetz(n, ell, a, reflect)
                    predicted = expected_trace(n, ell, reflect)
                    assert actual == predicted, (n,ell,a,reflect,actual,predicted)
                    total += 1
        print(f'n={n}: alpha={alpha:+d}, beta={beta:+d}, checked ell={levels[0]}..{levels[-1]}')
    print(f'complete dihedral signed Lefschetz comparisons: {total}')
    for n, ell in [(5, 0),(5,1),(5,2),(5,3),(5,4),(7,0),(7,1)]:
        actual, count = reduced_mod2_betti(n,ell)
        pred = {deg:1 for deg in sphere_degrees(n,ell)}
        assert actual == pred, (n,ell,actual,pred)
        print(f'mod-two homology n={n}, ell={ell}: {count} augmented faces, ranks={actual}')
    # For reflection of the canonical double cover, the orbit graph is
    # exactly a path on n+1 vertices; direct orbit evaluation confirms it.
    for n in [5,7,11,13,17,19]:
        v = [(i,a) for i in range(n) for a in range(2)]
        edges={frozenset(((i,a),((i+1)%n,1-a)))
                for i in range(n) for a in range(2)}
        z=at_minus_one(v,edges,lambda x: ((-x[0]) % n,x[1]))
        assert z == path_value(n+1)
    print('canonical double-cover reflection path-quotient checks: 6/6')
    print('GENERAL_CYCLE_MYCIELSKI_DIHEDRAL_CHECKS_PASS')


if __name__ == '__main__':
    main()
