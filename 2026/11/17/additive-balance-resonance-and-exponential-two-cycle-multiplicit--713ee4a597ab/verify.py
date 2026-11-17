"""Finite independent checks for an exact majority dynamics theorem.
Only Python standard library is required. All labels and neighbor sets are explicit.
"""
from itertools import product
from math import comb


def expected(k):
    a, b, c, d = (2*k, 3*k, 4*k, 7*k)
    fixed = 2
    if k % 2 == 0:
        fixed += comb(a, a//2)*comb(b, b//2)*comb(c, c//2)*comb(d, d//2)
    return fixed, 2**(2*k)


def census_by_occupancies(k):
    sizes = (2*k, 3*k, 4*k, 7*k)
    total = sum(sizes)
    fixed = two_states = 0
    for counts in product(*(range(n + 1) for n in sizes)):
        summation = sum(counts)
        next_counts = tuple(
            n if 2*(summation - s) > total-n else
            0 if 2*(summation - s) < total-n else s
            for n, s in zip(sizes, counts)
        )
        twice_sum = sum(next_counts)
        again = tuple(
            n if 2*(twice_sum - s) > total-n else
            0 if 2*(twice_sum - s) < total-n else s
            for n, s in zip(sizes, next_counts)
        )
        multiplicity = 1
        for n, s in zip(sizes, counts):
            multiplicity *= comb(n, s)
        if next_counts == counts:
            fixed += multiplicity
        elif again == counts:
            two_states += multiplicity
    assert two_states % 2 == 0
    return fixed, two_states//2


def census_by_individual_vertices(sizes):
    nvertices = sum(sizes)
    offset = 0
    part_indices = []
    for size in sizes:
        part_indices.append(tuple(range(offset, offset + size)))
        offset += size
    groups = [set(g) for g in part_indices]
    vertex_group = {}
    for i, group in enumerate(groups):
        for v in group:
            vertex_group[v] = i
    neighborhoods = []
    for v in range(nvertices):
        m = 0
        for w in range(nvertices):
            if vertex_group[w] != vertex_group[v]:
                m |= 1 << w
        neighborhoods.append(m)

    def evolve(bits):
        output = 0
        for v, mask in enumerate(neighborhoods):
            ones = (bits & mask).bit_count()
            degree = mask.bit_count()
            bit = int(2*ones > degree) if 2*ones != degree else ((bits >> v) & 1)
            output |= bit << v
        return output

    fixed = two = 0
    for x in range(1 << nvertices):
        y = evolve(x)
        if y == x:
            fixed += 1
        elif evolve(y) == x:
            two += 1
    assert two % 2 == 0
    return fixed, two // 2


if __name__ == '__main__':
    for k in range(1, 8):
        a = census_by_occupancies(k)
        e = expected(k)
        assert a == e, (k,a,e)
        print(f'k={k}: count-based fixed={a[0]}, two-orbits={a[1]}, expected={e} OK')
    exact = census_by_individual_vertices((2,3,4,7))
    assert exact == expected(1), (exact,expected(1))
    print(f'16-vertex direct full-state enumeration: {2**16} states, fixed={exact[0]}, two-orbits={exact[1]} OK')
    for k in (1,2,3,4):
        sizes = (2*k,3*k,4*k,7*k)
        for s in range(2*k+1):
            A = (s,0,0,7*k)
            B = (s,3*k,4*k,0)
            total = 16*k
            def update(x):
                return tuple(n if 2*(sum(x)-t)>total-n else 0 if 2*(sum(x)-t)<total-n else t for n,t in zip(sizes,x))
            assert update(A)==B and update(B)==A
    print('Explicit orbit family verified for k=1..4 and all occupancies OK')
    print('VERIFY_OK')
