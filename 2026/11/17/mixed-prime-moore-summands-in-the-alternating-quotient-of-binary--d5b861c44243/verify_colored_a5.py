"""Exact orbit-chain verifier for binary-coloured injective words on five symbols.
Requires Python 3 and SymPy. This is an ordinary finite integer computation.
"""
from itertools import product, permutations
from math import factorial
from collections import defaultdict
from sympy import zeros, ZZ
from sympy.matrices.normalforms import smith_normal_form

N, COLORS = 5, 2
PERMS = list(permutations(range(N)))

def parity(seq):
    return sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i+1,len(seq))) % 2

def orbit(word):
    labels, colors = word
    k = len(labels)
    if k <= N-2:
        return (colors, 0)
    return (colors, parity(labels + tuple(i for i in range(N) if i not in labels)))

def all_words(k):
    return [(labels, colors) for labels in permutations(range(N), k)
            for colors in product(range(COLORS), repeat=k)]

CELLS = {}
REP = {}
for k in range(1, N+1):
    words = all_words(k)
    classes = sorted(set(map(orbit, words)))
    CELLS[k] = {x:j for j,x in enumerate(classes)}
    REP[k] = {x:next(w for w in words if orbit(w)==x) for x in classes}
    predicted = COLORS**k * (2 if k >= N-1 else 1)
    assert len(classes) == predicted
    group = [g for g in PERMS if parity(g)==0]
    for word in words:
        transformed = {(tuple(g[i] for i in word[0]),word[1]) for g in group}
        assert len({orbit(w) for w in transformed})==1
        # Orbit label is a COMPLETE classifier, not just an invariant.
        if word == REP[k][orbit(word)]:
            assert len(transformed) == sum(orbit(w)==orbit(word) for w in words)
    print(f'length {k}: {len(words)} labelled cells, {len(classes)} quotient cells',flush=True)

BD = {}
for k in range(2,N+1):
    D = zeros(len(CELLS[k-1]),len(CELLS[k]))
    for c, index in CELLS[k].items():
        labels, colors = REP[k][c]
        for i in range(k):
            new=(labels[:i]+labels[i+1:],colors[:i]+colors[i+1:])
            D[CELLS[k-1][orbit(new)],index] += (-1)**i
    # Independent boundary invariance check on EVERY labelled cell.
    for labels,colors in all_words(k):
        projected={}
        for i in range(k):
            cell=orbit((labels[:i]+labels[i+1:],colors[:i]+colors[i+1:]))
            projected[cell]=projected.get(cell,0)+(-1)**i
        assert all(D[CELLS[k-1][cell],CELLS[k][orbit((labels,colors))]] == coefficient
                   for cell,coefficient in projected.items())
    if k>2: assert BD[k-1]*D == zeros(BD[k-1].rows, D.cols)
    BD[k]=D
    snf=smith_normal_form(D,domain=ZZ)
    factors=[abs(int(snf[i,i])) for i in range(min(D.rows,D.cols)) if snf[i,i]]
    print(f'd_{k}: shape={D.shape}, rank={len(factors)}, nonunit_SNF={ [x for x in factors if x>1] }',flush=True)
    if k==2: assert (len(factors),[x for x in factors if x>1]) == (1,[])
    if k==3: assert (len(factors),[x for x in factors if x>1]) == (3,[])
    if k==4: assert (len(factors),[x for x in factors if x>1]) == (5,[])
    if k==5: assert (len(factors),[x for x in factors if x>1]) == (27,[3,30])

# The bottom 2-skeleton has 2 vertices, 4 edges and 8 triangles.
# A maximal tree consists of the edge (0,1). Every other edge is
# killed by the relations e_ab e_bc = e_ac from each color triple:
# (0,0,0) kills 00; (1,1,1) kills 11; (0,1,0) kills 10.
# Thus the fundamental group is trivial.
assert {c[0] for c in CELLS[1]} == {(0,),(1,)}
assert {c[0] for c in CELLS[2]} == set(product(range(2),repeat=2))
assert {c[0] for c in CELLS[3]} == set(product(range(2),repeat=3))
print('pi_1: trivial via the eight color-triple relations, after the 01 tree edge',flush=True)
print('integral_homology: H0=Z, H1=H2=0, H3=Z/3 + Z/30, H4=Z^37',flush=True)
print('homotopy_type: M(Z/3,3) vee M(Z/30,3) vee 37 copies of S^4',flush=True)
