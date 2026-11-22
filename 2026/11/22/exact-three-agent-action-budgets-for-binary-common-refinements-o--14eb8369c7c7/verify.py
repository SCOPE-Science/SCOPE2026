"""Standalone exact action-budget and minimality checks for three partition-valued agents."""
from itertools import product
from random import Random


def vertex_cover(vertices, triangles):
    edges = set()
    for t in triangles:
        for i in range(3):
            for j in range(i + 1, 3):
                edges.add(tuple(sorted((t[i], t[j]))))
    for size in range(len(vertices) + 1):
        from itertools import combinations
        for inds in combinations(range(len(vertices)), size):
            chosen = {vertices[i] for i in inds}
            if all(x in chosen or y in chosen for x, y in edges):
                return chosen, edges
    raise AssertionError('No vertex cover')


def build_outcomes(sizes, chosen, cell_sizes):
    """Each cell is a canonical disjoint collection of labelled outcomes."""
    table = {}
    labels = {}
    for ix, cs in cell_sizes.items():
        labels[ix] = tuple((ix, t) for t in range(cs))
    for ix in cell_sizes:
        mi = [sizes[a][ix[a]] for a in range(3)]
        if cell_sizes[ix] == 2:
            agents = [a for a in range(3) if (a, ix[a]) in chosen]
            assert len(agents) >= 2
            p, q = agents[:2]
        for cc in product(*(range(x) for x in mi)):
            value = labels[ix][(cc[p] + cc[q]) % 2] if cell_sizes[ix] == 2 else labels[ix][0]
            table[(ix, cc)] = value
    return table, labels


def check_effectivity(sizes, table, labels):
    for agent in range(3):
        for block in range(len(sizes[agent])):
            target = {p for ix, points in labels.items() if ix[agent] == block for p in points}
            for copy in range(sizes[agent][block]):
                got = {out for (ix, cc), out in table.items() if ix[agent] == block and cc[agent] == copy}
                assert got == target, (agent, block, copy, got, target)


def check_small_cell_exhaustive():
    checked = 0
    for a, b, c in product((1, 2), repeat=3):
        seen = False
        for bits in product((0, 1), repeat=a*b*c):
            colorings = dict(zip(product(range(a),range(b),range(c)),bits))
            if all({colorings[q] for q in colorings if q[axis] == idx} == {0, 1}
                   for axis, copies in enumerate((a,b,c)) for idx in range(copies)):
                seen = True
                break
        assert seen == (sum(x >= 2 for x in (a,b,c)) >= 2)
        checked += 1
    return checked


def check_all_two_by_two_by_two_masks():
    vertices = [(a,i) for a in range(3) for i in range(2)]
    triples = tuple(product(range(2), repeat=3))
    checked = 0
    covers = {}
    for mask in range(256):
        cells = {t: 1 + ((mask >> j) & 1) for j,t in enumerate(triples)}
        triangles = [tuple((a,t[a]) for a in range(3)) for t in triples if cells[t] == 2]
        cover, edges = vertex_cover(vertices,triangles)
        sizes = [[2 if (a,i) in cover else 1 for i in range(2)] for a in range(3)]
        assert sum(map(sum,sizes)) == 6 + len(cover)
        table, labels = build_outcomes(sizes,cover,cells)
        check_effectivity(sizes,table,labels)
        # Independently enumerate all binary-budget assignments, not only the chosen optimum.
        feasible = []
        for pickmask in range(64):
            selected = {vertices[j] for j in range(6) if pickmask >> j & 1}
            desired = all(sum((a,t[a]) in selected for a in range(3)) >= 2 for t in triples if cells[t]==2)
            cover_check = all(u in selected or v in selected for u,v in edges)
            assert desired == cover_check
            if desired:
                feasible.append(len(selected))
        assert min(feasible) == len(cover)
        covers[len(cover)] = covers.get(len(cover),0) + 1
        checked += 1
    return checked, covers


def check_heterogeneous_samples():
    rng=Random(20261115)
    count=0
    for _ in range(800):
        shape = [rng.randrange(1,4) for _ in range(3)]
        types=list(product(*(range(t) for t in shape)))
        cells = {t:rng.choice((1,2)) for t in types}
        sizes=[[rng.randrange(1,5) for _ in range(shape[a])] for a in range(3)]
        feasible=all(sum(sizes[a][t[a]]>=2 for a in range(3)) >=2 for t in types if cells[t]==2)
        if not feasible:
            continue
        doubled={(a,i) for a in range(3) for i in range(shape[a]) if sizes[a][i]>=2}
        table,labels=build_outcomes(sizes,doubled,cells)
        check_effectivity(sizes,table,labels)
        count+=1
    return count

if __name__=='__main__':
    small=check_small_cell_exhaustive()
    n,covers=check_all_two_by_two_by_two_masks()
    random_ok=check_heterogeneous_samples()
    assert n == 256 and random_ok > 10
    print(f'VERIFY_OK local_exact={small} masks={n} cover_distribution={covers} heterogeneous={random_ok}')
