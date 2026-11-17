"""Exact finite certificate for the rational automorphism character of the
second independence complex of the 4 by 4 rook graph. Python 3 standard library.
"""
from itertools import permutations
from collections import Counter
from fractions import Fraction
import csv

N = 16
P = list(permutations(range(4)))
e = (0, 1, 2, 3)


def admissible(mask):
    chosen = [v for v in range(N) if mask & (1 << v)]
    return all(sum(v != w and (v // 4 == w // 4 or v % 4 == w % 4)
                   for w in chosen) <= 1 for v in chosen)


F = {mask for mask in range(1 << N) if admissible(mask)}
fs = Counter(mask.bit_count() for mask in F)
assert dict(fs) == {0: 1, 1: 16, 2: 120, 3: 384, 4: 528, 5: 144}


def simplices(k):
    return sorted(mask for mask in F if mask.bit_count() == k + 1)


def rank_mod2(k):
    lower = simplices(k-1)
    index = {x: i for i, x in enumerate(lower)}
    echelon = {}
    for col in simplices(k):
        vec = 0
        v = col
        while v:
            bit = v & -v
            vec ^= 1 << index[col ^ bit]
            v -= bit
        while vec:
            pivot = vec.bit_length() - 1
            if pivot in echelon:
                vec ^= echelon[pivot]
            else:
                echelon[pivot] = vec
                break
    return len(echelon)


r = [rank_mod2(k) for k in range(1, 5)]
assert r == [15, 105, 279, 144], r
# These F2 ranks force the Q ranks: r1 <= 15, r2 <= 120-r1,
# r3 <= 384-r2, r4 <= 144, and all F2 ranks are Q lower bounds.
# The resulting reduced Q homology has only beta3 = 528-279-144 = 105.


def permutation_class(p):
    seen = set()
    lengths = []
    for i in range(len(p)):
        if i not in seen:
            j, length = i, 0
            while j not in seen:
                seen.add(j)
                j = p[j]
                length += 1
            lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def mapping(p, q, swap):
    return tuple(4*p[j] + q[i] if swap else 4*p[i] + q[j]
                 for i in range(4) for j in range(4))


def inversion_sign(seq):
    n = sum(seq[i] > seq[j] for i in range(len(seq))
            for j in range(i+1, len(seq)))
    return 1 if n % 2 == 0 else -1


def character_by_faces(g):
    # Reduced Lefschetz formula in the only nonzero rational degree 3.
    tr = 1  # the empty simplex contributes to -reduced Lefschetz
    for mask in F:
        if not mask:
            continue
        v = [i for i in range(N) if (mask >> i) & 1]
        w = [g[i] for i in v]
        if sorted(w) == v:
            tr += (-1)**len(v) * inversion_sign(w)
    return tr


def character_by_cycles(g):
    # An invariant face is a union of cycles. Including the empty face,
    # its contribution is (-1) to the number of chosen cycles.
    seen = set()
    cycles = []
    for v in range(N):
        if v not in seen:
            j, mask = v, 0
            while j not in seen:
                seen.add(j)
                mask |= 1 << j
                j = g[j]
            cycles.append(mask)
    counts = [0] * (1 << len(cycles))
    count = 0
    for subset in range(1 << len(cycles)):
        mask, weight = 0, 1
        for i, cmask in enumerate(cycles):
            if (subset >> i) & 1:
                mask |= cmask
                weight = -weight
        if mask in F:
            count += weight
    return count


# Character-table rows for irreducible S4 Specht representations:
# partitions (4), (3,1), (2,2), (2,1,1), (1,1,1,1).
partition_names = ('4', '31', '22', '211', '1111')
chi_S4 = {
    (1, 1, 1, 1): (1, 3, 2, 3, 1),
    (2, 1, 1): (1, 1, 0, -1, -1),
    (2, 2): (1, -1, 2, -1, 1),
    (3, 1): (1, 0, -1, 0, 1),
    (4,): (1, -1, 0, 1, -1),
}
assert all(sum(chi_S4[permutation_class(p)][i] *
               chi_S4[permutation_class(p)][j] for p in P) ==
           (24 if i == j else 0)
           for i in range(5) for j in range(5))

classes_base = {}
classes_base_ordered = {}
classes_swap = {}
counts_base = Counter()
counts_base_ordered = Counter()
counts_swap = Counter()
all_maps = set()
for swap in (False, True):
    for p in P:
        for q in P:
            g = mapping(p, q, swap)
            assert g not in all_maps
            all_maps.add(g)
            # independently verify that every generated permutation acts
            # simplicially, not merely that it is intended to do so.
            for mask in F:
                image = sum(1 << g[v] for v in range(N) if (mask >> v) & 1)
                assert image in F
            a = character_by_faces(g)
            b = character_by_cycles(g)
            assert a == b, (p,q,swap,a,b)
            if swap:
                product = tuple(p[q[i]] for i in range(4))
                key = permutation_class(product)
                if key in classes_swap:
                    assert classes_swap[key] == a
                classes_swap[key] = a
                counts_swap[key] += 1
            else:
                ordered = (permutation_class(p), permutation_class(q))
                if ordered in classes_base_ordered:
                    assert classes_base_ordered[ordered] == a
                classes_base_ordered[ordered] = a
                counts_base_ordered[ordered] += 1
                key = tuple(sorted((permutation_class(p), permutation_class(q)),
                                   reverse=True))
                if key in classes_base:
                    assert classes_base[key] == a
                classes_base[key] = a
                counts_base[key] += 1
assert len(all_maps) == 1152
assert len(classes_base) == 15 and len(classes_swap) == 5
assert sum(counts_base.values()) == sum(counts_swap.values()) == 576
assert classes_base[((1,1,1,1),(1,1,1,1))] == 105

# Base-subgroup irreducible multiplicities. Store all tensor-product
# multiplicities, including zeros, to check that restriction is symmetric.
mults = {}
for i in range(5):
    for j in range(5):
        numerator = sum(classes_base_ordered[c]*counts_base_ordered[c]*
                        chi_S4[c[0]][i]*chi_S4[c[1]][j]
                        for c in classes_base_ordered)
        assert numerator % 576 == 0
        mults[i,j] = numerator//576
        assert mults[i,j] >= 0
assert all(mults[i,j] == mults[j,i] for i in range(5) for j in range(5))
assert mults == {
    (0,0):0,(0,1):0,(0,2):1,(0,3):0,(0,4):1,
    (1,0):0,(1,1):0,(1,2):1,(1,3):2,(1,4):1,
    (2,0):1,(2,1):1,(2,2):2,(2,3):0,(2,4):1,
    (3,0):0,(3,1):2,(3,2):0,(3,3):3,(3,4):1,
    (4,0):1,(4,1):1,(4,2):1,(4,3):1,(4,4):0,
}
# For each diagonal tensor representation, the coset swap traces are
# +/- chi_lambda(pq). Orthogonality extracts the extension imbalance.
imbalances = {}
for i in range(5):
    numerator = sum(classes_swap[k]*counts_swap[k]*chi_S4[k][i]
                    for k in classes_swap)
    assert numerator % 576 == 0
    imbalances[i] = numerator//576
assert imbalances == {0:0,1:0,2:0,3:1,4:0}
extensions = {partition_names[i]: (
    (mults[i,i] + imbalances[i])//2,
    (mults[i,i] - imbalances[i])//2) for i in range(5)}
assert extensions == {'4':(0,0),'31':(0,0),'22':(1,1),'211':(2,1),'1111':(0,0)}
base_fixed = sum(classes_base[k]*counts_base[k] for k in classes_base)
all_fixed = base_fixed + sum(classes_swap[k]*counts_swap[k] for k in classes_swap)
assert base_fixed == all_fixed == 0
assert (sum(classes_base[k]**2*counts_base[k] for k in classes_base)
        +sum(classes_swap[k]**2*counts_swap[k] for k in classes_swap))//1152 == 17

# Three natural quotient calculations (finite-group transfer over Q).
row_sum = sum(character_by_cycles(mapping(p,e,False)) for p in P)
diagonal_sum = sum(character_by_cycles(mapping(p,p,False)) for p in P)
diagonal_swap_sum = sum(character_by_cycles(mapping(p,p,True)) for p in P)
transpose_trace = character_by_cycles(mapping(e,e,True))
assert row_sum == 72 and diagonal_sum == 120
assert diagonal_swap_sum == 24
assert transpose_trace == 3
assert row_sum//24 == 3
assert diagonal_sum//24 == 5
assert (diagonal_sum+diagonal_swap_sum)//48 == 3

# Signed geometry has no positive-degree rational classes fixed by all
# row-and-column permutations, hence none fixed by the full group.
print('ROOK2_FACE_VECTOR',*[fs[k] for k in range(6)])
print('ROOK2_RANKS_MOD2',*r)
print('ROOK2_RATIONAL_BETTI3',105)
print('ROOK2_GROUP_ORDER',len(all_maps))
print('ROOK2_GROUP_CLASSES',len(classes_base)+len(classes_swap))
for k in sorted(classes_base):
    print('CLASS_BASE',str(k).replace(' ',''),counts_base[k],classes_base[k])
for k in sorted(classes_swap):
    print('CLASS_SWAP',str(k).replace(' ',''),counts_swap[k],classes_swap[k])
for i in range(5):
    for j in range(i+1,5):
        if mults[i,j]:
            print('OFFDIAGONAL',partition_names[i],partition_names[j],mults[i,j])
for i in range(5):
    if any(extensions[partition_names[i]]):
        print('DIAGONAL_EXTENSIONS',partition_names[i],*extensions[partition_names[i]])
print('ROOK2_BASE_FIXED_DIM',base_fixed//576)
print('ROOK2_FULL_FIXED_DIM',all_fixed//1152)
print('ROOK2_ROW_ONLY_FIXED_DIM',row_sum//24)
print('ROOK2_DIAGONAL_FIXED_DIM',diagonal_sum//24)
print('ROOK2_DIAGONAL_TRANSPOSE_FIXED_DIM',(diagonal_sum+diagonal_swap_sum)//48)
print('ROOK2_TRANSPOSE_TRACE',transpose_trace)
print('ROOK2_CHARACTER_NORM',17)
print('ROOK2_FULL_EQUIVARIANT_CHARACTER_PASS')
