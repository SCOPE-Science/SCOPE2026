"""Exact CW and homotopy-preserving word-reduction verifier for Pi_5/C_5.

Run with Python 3: python verify.py
Uses only the Python standard library. The complete certificate is certificate.json.
"""
from collections import Counter, defaultdict
from itertools import combinations
import json
from pathlib import Path

N = 5

def canonical(blocks):
    return tuple(sorted(tuple(sorted(b)) for b in blocks))

def partitions(n):
    def rec(labels, maximum):
        if len(labels) == n:
            blocks = defaultdict(list)
            for i, b in enumerate(labels):
                blocks[b].append(i)
            yield canonical(blocks.values())
            return
        for b in range(maximum + 2):
            yield from rec(labels + [b], max(maximum, b))
    yield from rec([0], 0)

def rotate(part, t):
    return canonical({(i + t) % N for i in block} for block in part)

def orbit_representative(chain):
    return min(tuple(rotate(part, t) for part in chain) for t in range(N))

def refinement(finer, coarser):
    return all(any(set(block) <= set(coarse) for coarse in coarser)
               for block in finer)

def reduce_word(word):
    stack = []
    for symbol in word:
        if stack and stack[-1] == -symbol:
            stack.pop()
        else:
            stack.append(symbol)
    while len(stack) >= 2 and stack[-1] == -stack[0]:
        stack = stack[1:-1]
    return stack

def inverse(word):
    return [-x for x in reversed(word)]

def canonical_word(word):
    word = reduce_word(word)
    if not word:
        return []
    rotations = []
    for current in (word, inverse(word)):
        for i in range(len(current)):
            rotations.append(current[i:] + current[:i])
    return min(rotations)

def compute_certificate():
    all_partitions = sorted(partitions(N))
    assert len(all_partitions) == 52
    objects = sorted(p for p in all_partitions if 1 < len(p) < N)
    assert [sum(len(p) == k for p in objects) for k in (4, 3, 2)] == [10, 25, 15]
    assert len(objects) == 50
    vertex_orbits = sorted({orbit_representative((p,)) for p in objects})
    vi = {v: i for i, v in enumerate(vertex_orbits)}
    original_edges = sorted((a, b) for a in objects for b in objects
                            if len(a) > len(b) and refinement(a, b))
    original_triangles = sorted((a, b, c)
        for a in objects for b in objects for c in objects
        if len(a) == 4 and len(b) == 3 and len(c) == 2
        and refinement(a, b) and refinement(b, c))
    edges = sorted({orbit_representative(e) for e in original_edges})
    triangles = sorted({orbit_representative(t) for t in original_triangles})
    assert (len(original_edges), len(original_triangles)) == (205, 180)
    assert (len(vertex_orbits), len(edges), len(triangles)) == (10, 41, 36)
    for cells, quotient in ((objects, vertex_orbits),
                            (original_edges, edges), (original_triangles, triangles)):
        assert all(sum(orbit_representative(cell if isinstance(cell[0], tuple) and isinstance(cell[0][0], tuple) else (cell,)) == q for cell in cells) == N for q in quotient)
    ei = {e: i for i, e in enumerate(edges)}
    endpoints = [(vi[orbit_representative((a,))], vi[orbit_representative((b,))])
                 for a, b in edges]
    boundaries = [(ei[orbit_representative((a, b))],
                   ei[orbit_representative((b, c))],
                   ei[orbit_representative((a, c))]) for a, b, c in triangles]
    # Check d_1 d_2 = 0 in the integral quotient cellular complex.
    for ab, bc, ac in boundaries:
        sum_vertices = Counter()
        for edge_index, coefficient in ((ab, 1), (bc, 1), (ac, -1)):
            source, target = endpoints[edge_index]
            sum_vertices[source] -= coefficient
            sum_vertices[target] += coefficient
        assert all(m == 0 for m in sum_vertices.values())
    parent = list(range(len(vertex_orbits)))
    def root(x):
        while x != parent[x]:
            x = parent[x]
        return x
    tree = set()
    for idx, (a, b) in enumerate(endpoints):
        ra, rb = root(a), root(b)
        if ra != rb:
            parent[ra] = rb
            tree.add(idx)
    assert len(tree) == 9 and len({root(v) for v in range(10)}) == 1
    non_tree = [e for e in range(len(edges)) if e not in tree]
    generators = {e: i+1 for i, e in enumerate(non_tree)}
    words = []
    for eab, ebc, eac in boundaries:
        word = [sign * generators[e]
                for e, sign in ((eab, 1), (ebc, 1), (eac, -1))
                if e in generators]
        words.append(canonical_word(word))
    initial_lengths = dict(sorted(Counter(map(len, words)).items()))
    remaining = set(generators.values())
    pivots = []
    while True:
        choices = [(len(word), gen, row)
                   for row, word in enumerate(words)
                   for gen in remaining
                   if Counter(map(abs, word))[gen] == 1]
        if not choices:
            break
        _, gen, row = min(choices)
        word = words[row]
        pos = next(i for i, letter in enumerate(word) if abs(letter) == gen)
        cyclic = word[pos:] + word[:pos]
        replacement = inverse(cyclic[1:]) if cyclic[0] == gen else cyclic[1:]
        assert cyclic[0] in (gen, -gen)
        def substitute(word):
            replaced = []
            for symbol in word:
                if symbol == gen:
                    replaced.extend(replacement)
                elif symbol == -gen:
                    replaced.extend(inverse(replacement))
                else:
                    replaced.append(symbol)
            return canonical_word(replaced)
        words = [substitute(w) for j, w in enumerate(words) if j != row]
        pivots.append({'generator': gen, 'relator_index': row,
                       'cyclic_relator': cyclic, 'replacement': replacement})
        remaining.remove(gen)
    assert len(pivots) == 31
    assert len(remaining) == 1 and len(words) == 5
    assert sum(not w for w in words) == 3
    nonempty = [w for w in words if w]
    assert len(nonempty) == 2 and nonempty[0] == nonempty[1]
    assert len(nonempty[0]) == 5 and len(set(nonempty[0])) == 1
    # Two identical degree-five disks: one gives M(Z/5,1),
    # the other attaches by a nullhomotopic loop and splits off S^2.
    return {'cell_counts_original': [50, 205, 180],
            'cell_counts_quotient': [10, 41, 36],
            'edge_endpoints': endpoints, 'triangle_boundary_edges': boundaries,
            'spanning_tree_edges': sorted(tree), 'non_tree_edges': non_tree,
            'initial_relator_length_counts': initial_lengths,
            'pivots': pivots, 'remaining_generators': sorted(remaining),
            'remaining_relators': words}

if __name__ == '__main__':
    expected = json.loads(Path(__file__).with_name('certificate.json').read_text(encoding='utf-8'))
    actual = compute_certificate()
    # JSON object keys are strings. Parse-serialize actual to align integer count keys.
    assert json.loads(json.dumps(actual)) == expected
    print('VERIFY_OK: 10/41/36 cells; 31 geometric generator/2-cell eliminations; '
          'one generator with two degree-five and three trivial 2-cells')
