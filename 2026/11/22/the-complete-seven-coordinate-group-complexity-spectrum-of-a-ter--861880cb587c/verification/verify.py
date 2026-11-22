"""Finite certificate for the length-seven group-complexity spectrum.

Requires Python 3.10+ standard library only. Index coordinates from zero.
The completeness of the seven transitive degree-seven group types is the
published transitive-subgroup classification (see RESULT.md); all conjugates
and group actions used here are explicitly enumerated.
"""
from collections import Counter
from itertools import permutations

N = 7
ID = tuple(range(N))
ALL = tuple(permutations(range(N)))

def mu(w):
    return ''.join('01' if c == '0' else '0' for c in w)

def psi(w):
    return ''.join('0' if c == '0' else '12' for c in w)

def factors(w, n):
    return {w[i:i+n] for i in range(len(w)-n+1)}

blocks = {'0': '0', '1': '1'}
for _ in range(5):
    blocks = {c: mu(blocks[c]) for c in '01'}
assert min(len(psi(blocks[c])) for c in '01') >= N
F = sorted(set.union(*(factors(psi(blocks[a]+blocks[b]), N)
                       for a, b in ('00', '01', '10'))))
assert F == ['0012001', '0012012', '0120012', '0120120',
             '1200120', '1201200', '2001200', '2001201', '2012001']
assert len({tuple(w.count(c) for c in '012') for w in F}) == 3

# Each intransitive G preserves some nonempty proper subset A. It is a
# subgroup of S_A x S_{A^c}; that maximal block group is tested directly.
block_counts = Counter()
block_witnesses = {}
for mask in range(1, (1 << N)-1):
    if not (mask & 1):
        continue  # A and its complement give the same group.
    A = [i for i in range(N) if (mask >> i) & 1]
    B = [i for i in range(N) if not (mask >> i) & 1]
    def parikh(w, coordinates):
        return tuple(sum(w[i] == c for i in coordinates) for c in '012')
    count = len({(parikh(w, A), parikh(w, B)) for w in F})
    block_counts[count] += 1
    block_witnesses.setdefault(count, A)
assert sum(block_counts.values()) == 63
assert dict(block_counts) == {5:21, 6:7, 7:21, 8:7, 9:7}
assert block_witnesses == {5:[0], 6:[0,1], 7:[0,1,3],
                           8:[0,3], 9:[0,1,4]}

def compose(p, q):
    return tuple(p[q[i]] for i in range(N))

def inverse(p):
    return tuple(p.index(i) for i in range(N))

def generate(gens):
    have = {ID}
    todo = [ID]
    for x in todo:
        for y in gens:
            z = compose(x, y)
            if z not in have:
                have.add(z)
                todo.append(z)
    return frozenset(have)

# Transitive group representatives: affine maps on F_7 and GL_3(F_2)
# acting on the seven nonzero vectors of F_2^3.
rot = tuple((i+1) % 7 for i in range(7))
refl = tuple((-i) % 7 for i in range(7))
mul2 = tuple((2*i) % 7 for i in range(7))
mul3 = tuple((3*i) % 7 for i in range(7))
V = tuple(range(1,8)); ix = {x:i for i,x in enumerate(V)}
A = tuple(ix[x ^ (4 if x & 1 else 0)] for x in V)
B = tuple(ix[((x&1)<<1) | ((x&2)>>1) | (x&4)] for x in V)
C = tuple(ix[((x&2)<<1) | ((x&4)>>1) | (x&1)] for x in V)
representatives = {
    'C7': ([rot], 7, 120, {3:1,6:7,7:14,8:28,9:70}),
    'D7': ([rot,refl], 14, 120, {3:1,6:7,7:14,8:28,9:70}),
    'F21': ([rot,mul2], 21, 120, {3:1,5:7,6:28,7:49,8:35}),
    'F42': ([rot,mul3], 42, 120, {3:1,5:21,6:35,7:56,8:7}),
    'GL3(2)': ([A,B,C], 168, 30, {3:2,5:28}),
}
idx = {w:i for i,w in enumerate(F)}
# Precalculate every coordinate permutation's action on each factor. A
# move is kept exactly when the image is another member of F.
acts = {p:tuple(idx.get(''.join(w[p[j]] for j in range(N)), -1)
                for w in F) for p in ALL}

def complexity(group):
    par = list(range(len(F)))
    def root(i):
        while par[i] != i:
            i = par[i]
        return i
    for p in group:
        for i, j in enumerate(acts[p]):
            if j != -1:
                par[root(i)] = root(j)
    return len({root(i) for i in range(len(F))})

print('seven factors:', ' '.join(F))
print('abelian complexity: 3; ordinary complexity: 9')
print('intransitive maximal block groups:', sorted(block_counts.items()))
for name, (gens, order, expected_n, expected_distribution) in representatives.items():
    group = generate(gens)
    assert len(group) == order
    # Check transitivity directly, no external group software.
    assert {g[0] for g in group} == set(range(N))
    visited = set()
    distribution = Counter()
    for h in ALL:
        ih = inverse(h)
        conjugate = frozenset(compose(compose(h, g), ih) for g in group)
        if conjugate not in visited:
            visited.add(conjugate)
            distribution[complexity(conjugate)] += 1
    assert len(visited) == expected_n
    assert dict(distribution) == expected_distribution
    print(name, 'order', order, 'conjugates', len(visited),
          'complexity distribution', sorted(distribution.items()))

# A7 and S7 have the same ternary Parikh orbits since every word in F
# has at least two equal letters, providing an odd permutation stabilizer.
assert all(any(w.count(c) >= 2 for c in '012') for w in F)
print('A7, S7: complexity 3 by parity-adjustment argument')
print('complete spectrum: 3 5 6 7 8 9; forbidden value: 4')
print('PASS')
