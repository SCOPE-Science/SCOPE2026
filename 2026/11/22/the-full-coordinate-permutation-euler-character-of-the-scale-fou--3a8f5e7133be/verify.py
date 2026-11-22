"""Exact orbit-complex Euler-character and S_6 character verification.

Run with CPython 3.10+ (standard library only): python verify.py
No external data, files, or network access needed.
"""
from functools import lru_cache
from itertools import combinations
from math import factorial

N = 6
R = 4


def partitions(n, hi=None):
    if n == 0:
        yield ()
    else:
        for k in range(min(n, n if hi is None else hi), 0, -1):
            for t in partitions(n - k, k):
                yield (k,) + t


def representative(cycle_type):
    p = list(range(N))
    offset = 0
    for length in cycle_type:
        for j in range(length):
            p[offset + j] = offset + (j + 1) % length
        offset += length
    return p


def map_word(x, p):
    result = 0
    for i, q in enumerate(p):
        if (x >> i) & 1:
            result |= 1 << q
    return result


def orbit_graph(p):
    """Incompatibility graph of admissible vertex orbits; output bitset adjacencies."""
    unseen = set(range(1 << N))
    orbits = []
    while unseen:
        start = min(unseen)
        orbit, u = [], start
        while u not in orbit:
            orbit.append(u)
            unseen.remove(u)
            u = map_word(u, p)
        if all((a ^ b).bit_count() <= R for a in orbit for b in orbit):
            orbits.append(tuple(orbit))
    adj = [0] * len(orbits)
    for i, oi in enumerate(orbits):
        for j in range(i):
            if any((a ^ b).bit_count() > R for a in oi for b in orbits[j]):
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    return orbits, tuple(adj)


def signed_independence(adj, reverse_ties=False):
    """Exact I_G(-1), by vertex-deletion and closed-neighborhood deletion."""
    states = 0

    @lru_cache(None)
    def run(mask):
        nonlocal states
        states += 1
        if mask == 0:
            return 1
        active = mask
        chosen, maximum = -1, -1
        while active:
            bit = active & -active
            active ^= bit
            v = bit.bit_length() - 1
            d = (adj[v] & mask).bit_count()
            if d > maximum or (reverse_ties and d == maximum):
                chosen, maximum = v, d
        b = 1 << chosen
        return run(mask ^ b) - run(mask & ~(b | adj[chosen]))

    val = run((1 << len(adj)) - 1)
    return val, states


def brute_independence(adj):
    result = 0
    n = len(adj)
    for mask in range(1 << n):
        if all(not (adj[i] & mask & ~((1 << (i + 1)) - 1))
               for i in range(n) if mask & (1 << i)):
            result += (-1) ** mask.bit_count()
    return result


def compare_small_cases():
    # A second finite check: for small hypercubes, direct face enumeration
    # agrees with the graph-independence recurrence for coordinate actions.
    for dim in (2, 3):
        for typ in partitions(dim):
            p = list(range(dim))
            offset = 0
            for length in typ:
                for j in range(length):
                    p[offset+j] = offset + (j+1) % length
                offset += length
            # Independent, non-bitset orbit-generation implementation.
            unseen = set(range(1 << dim))
            obs = []
            while unseen:
                y = min(unseen)
                orb = set()
                while y not in orb:
                    orb.add(y)
                    unseen.discard(y)
                    y = sum(((y >> i) & 1) << p[i] for i in range(dim))
                if all((a ^ b).bit_count() <= min(2, dim) for a in orb for b in orb):
                    obs.append(orb)
            adj = [0]*len(obs)
            for i, a in enumerate(obs):
                for j in range(i):
                    if any((x^y).bit_count()> min(2,dim) for x in a for y in obs[j]):
                        adj[i] |= 1<<j
                        adj[j] |= 1<<i
            assert brute_independence(adj) == signed_independence(tuple(adj))[0]
    return True


def cells(part):
    return frozenset((i, j) for i, k in enumerate(part) for j in range(k))


def rim_hook(part, smaller):
    skew = cells(part) - cells(smaller)
    if not skew:
        return None
    reached = {next(iter(skew))}
    while True:
        grown = reached | {v for i, j in reached
                           for v in ((i+1,j), (i-1,j), (i,j+1), (i,j-1))
                           if v in skew}
        if grown == reached:
            break
        reached = grown
    if reached != skew:
        return None
    if any((i+1,j) in skew and (i,j+1) in skew and (i+1,j+1) in skew
           for i, j in skew):
        return None
    return len(set(i for i, j in skew))


@lru_cache(None)
def specht_char(part, conj):
    if not conj:
        return int(len(part) == 0)
    k = conj[0]
    answer = 0
    for sub in partitions(sum(part) - k):
        if len(sub) <= len(part) and all(sub[i] <= part[i] for i in range(len(sub))):
            height = rim_hook(part, sub)
            if height is not None:
                answer += (-1) ** (height-1) * specht_char(sub, conj[1:])
    return answer


def class_size(conj):
    denom = 1
    for k in set(conj):
        denom *= k ** conj.count(k) * factorial(conj.count(k))
    return factorial(sum(conj)) // denom


def main():
    compare_small_cases()
    out = {}
    for typ in partitions(N):
        obs, adj = orbit_graph(representative(typ))
        first, n1 = signed_independence(adj)
        second, n2 = signed_independence(adj, reverse_ties=True)
        assert first == second, (typ, first, second)
        out[typ] = first
        print('cycle_type=%s admissible_orbits=%d I(-1)=%d states=(%d,%d)' %
              (typ, len(obs), first, n1, n2), flush=True)
    assert sum(class_size(t) for t in out) == factorial(N)
    shapes = tuple(partitions(N))
    # Independent exact check that the Murnaghan--Nakayama character table
    # is orthonormal in the class-weighted inner product.
    for i, shape_i in enumerate(shapes):
        for j, shape_j in enumerate(shapes):
            scalar = sum(class_size(t) * specht_char(shape_i, t)
                         * specht_char(shape_j, t) for t in out)
            assert scalar == factorial(N) * (i == j)
    multiplicities = {}
    for shape in partitions(N):
        numerator = sum(class_size(t)*val*specht_char(shape,t)
                        for t,val in out.items())
        assert numerator % factorial(N) == 0
        multiplicities[shape] = numerator // factorial(N)
        assert multiplicities[shape] >= 0
        print('Specht %s multiplicity=%d dim=%d' %
              (shape, multiplicities[shape], specht_char(shape, (1,)*N)))
    assert sum(multiplicities[s] * specht_char(s, (1,)*N)
               for s in multiplicities) == out[(1,)*N] == 253
    assert multiplicities[(6,)] == 7
    print('PASS: 11 exact class values, two pivot orders, Specht orthogonality, quotient reduced Euler=-7')


if __name__ == '__main__':
    main()
