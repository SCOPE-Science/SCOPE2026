#!/usr/bin/env python3
"""Exact finite verification of a four-robust grid complex and its D4 character.

All faces, chain traces, and matching arrows are recomputed; no external packages.
"""
from itertools import combinations
from collections import Counter, deque

N = 9
V = tuple(range(N))

def coord(v):
    return divmod(v, 3)

def edge(u, v):
    a, b = coord(u), coord(v)
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1

def is_independent_quad(q):
    return all(not edge(a, b) for a, b in combinations(q, 2))

# Method 1: forbidden independent four-subsets, with all 2^9 subsets tested.
forbidden = set()
for q in combinations(V, 4):
    if is_independent_quad(q):
        forbidden.add(sum(1 << v for v in q))
assert len(forbidden) == 6
faces_a = set()
for mask in range(1, 1 << N):
    if not any(mask & q == q for q in forbidden):
        faces_a.add(mask)

# Method 2: bipartite maximum matching, alpha(G[W]) = |W| - nu(G[W]).
# The augmenting-path routine never queries the forbidden-set calculation.
def max_matching_in_induced(mask):
    left = [v for v in V if (mask >> v) & 1 and sum(coord(v)) % 2 == 0]
    right = [v for v in V if (mask >> v) & 1 and sum(coord(v)) % 2 == 1]
    partner = {}
    def augment(u, visited):
        for w in right:
            if not edge(u, w) or w in visited:
                continue
            visited.add(w)
            if w not in partner or augment(partner[w], visited):
                partner[w] = u
                return True
        return False
    return sum(augment(u, set()) for u in left)

faces_b = {mask for mask in range(1, 1 << N)
           if mask.bit_count() - max_matching_in_induced(mask) <= 3}
assert faces_a == faces_b
faces = faces_a
counts = Counter(mask.bit_count()-1 for mask in faces)
assert tuple(counts[i] for i in range(6)) == (9, 36, 84, 120, 100, 40)
assert all(all((mask ^ (1 << u)) in faces for u in V if mask & (1 << u))
           for mask in faces if mask.bit_count() > 1)
print('FACE_SETS_AGREE',len(forbidden),len(faces),tuple(counts[i] for i in range(6)))

# Deterministic ascending-vertex toggle matching, leaving the empty face unused.
unmatched = set(faces)
pairs = []
for v in V:
    bit = 1 << v
    for low in sorted(unmatched):
        upper = low | bit
        if low & bit == 0 and upper in unmatched:
            assert upper.bit_count() == low.bit_count() + 1
            unmatched.remove(low)
            unmatched.remove(upper)
            pairs.append((low, upper))
critical = Counter(mask.bit_count()-1 for mask in unmatched)
assert len(pairs) == 192 and critical == {0: 1, 5: 4}
assert len(pairs)*2+len(unmatched) == len(faces)
print('MORSE_MATCHING',len(pairs),sorted(critical.items()), sorted(unmatched))

# Global directed Hasse test: unmatched incidence points down; matched incidence up.
P = set(pairs)
indeg = {mask: 0 for mask in faces}
adj = {mask: [] for mask in faces}
arrows = 0
for upper in faces:
    for v in V:
        if upper & (1 << v):
            low = upper ^ (1 << v)
            if not low:
                continue
            arrows += 1
            if (low, upper) in P:
                frm, to = low, upper
            else:
                frm, to = upper, low
            adj[frm].append(to)
            indeg[to] += 1
queue = deque(mask for mask in faces if indeg[mask] == 0)
seen = 0
while queue:
    mask = queue.popleft()
    seen += 1
    for nxt in adj[mask]:
        indeg[nxt] -= 1
        if indeg[nxt] == 0:
            queue.append(nxt)
assert seen == len(faces) and arrows == 1544
print('HASSE_ACYCLIC',seen,arrows)

# All eight grid symmetries. Rotate and reflect vertex coordinates, not face masks.
ops = {
    'identity': lambda r,c: (r,c),
    'rotation90': lambda r,c: (c,2-r),
    'rotation180': lambda r,c: (2-r,2-c),
    'rotation270': lambda r,c: (2-c,r),
    'horizontal_reflection': lambda r,c: (2-r,c),
    'vertical_reflection': lambda r,c: (r,2-c),
    'main_diagonal_reflection': lambda r,c: (c,r),
    'other_diagonal_reflection': lambda r,c: (2-c,2-r),
}
expected_character = {
    'identity': 4, 'rotation90':0, 'rotation180':0, 'rotation270':0,
    'horizontal_reflection':0, 'vertical_reflection':0,
    'main_diagonal_reflection':-2, 'other_diagonal_reflection':-2,
}
centers = ((1,1),(1,3),(3,1),(3,3)) # doubled coordinates of unit square centers
for name, op in ops.items():
    permutation = [3*op(*coord(v))[0]+op(*coord(v))[1] for v in V]
    assert len(set(permutation)) == N
    assert all(edge(u,v) == edge(permutation[u],permutation[v]) for u,v in combinations(V,2))
    chain_lefschetz = 0
    fixed_faces = 0
    for mask in faces:
        verts = [u for u in V if mask & (1 << u)]
        moved = [permutation[u] for u in verts]
        if sorted(moved) != verts:
            continue
        fixed_faces += 1
        inversions = sum(moved[i] > moved[j] for i in range(len(moved)) for j in range(i+1,len(moved)))
        chain_lefschetz += (-1) ** (len(verts)-1+inversions)
    character = 1-chain_lefschetz
    # The same formula acts on doubled square centers (using a 4-unit frame).
    def transform_center(a,b):
        if name == 'identity':return a,b
        if name == 'rotation90':return b,4-a
        if name == 'rotation180':return 4-a,4-b
        if name == 'rotation270':return 4-b,a
        if name == 'horizontal_reflection':return 4-a,b
        if name == 'vertical_reflection':return a,4-b
        if name == 'main_diagonal_reflection':return b,a
        if name == 'other_diagonal_reflection':return 4-b,4-a
        raise AssertionError
    square_fixed = sum(transform_center(*x) == x for x in centers)
    determinant = -1 if 'reflection' in name else 1
    assert character == determinant*square_fixed == expected_character[name]
    print('D4_CHARACTER',name,'fixed_faces',fixed_faces,'lefschetz',chain_lefschetz,
          'trace',character,'signed_square_trace',determinant*square_fixed)
# The Alexander dual is the total four-cut complex: its facets are
# complements of the independent four-sets. The prior homology count of four
# is reproduced here only as a check; the symmetry character is additional.
full = (1 << N) - 1
dual_faces = {mask for mask in range(1, 1 << N)
              if any((full ^ mask) & q == q for q in forbidden)}
assert tuple(sum(mask.bit_count()==d+1 for mask in dual_faces)
             for d in range(5)) == (9,36,44,26,6)

def mod2_betti(K):
    maxdim = max(mask.bit_count() - 1 for mask in K)
    levels = [sorted(mask for mask in K if mask.bit_count() == d+1)
              for d in range(maxdim+1)]
    ranks = [0]*(maxdim+2)
    for d in range(1,maxdim+1):
        rows = {face:i for i,face in enumerate(levels[d-1])}
        pivots={}
        for face in levels[d]:
            col=0
            for v in V:
                if face & (1<<v):
                    col ^= 1 << rows[face^(1<<v)]
            while col:
                i=col.bit_length()-1
                if i in pivots: col^=pivots[i]
                else:
                    pivots[i]=col
                    break
        ranks[d]=len(pivots)
    betti=[len(levels[d])-ranks[d]-ranks[d+1] for d in range(maxdim+1)]
    betti[0]-=1 # Reduced zero-th homology
    return betti
assert mod2_betti(faces)==[0,0,0,0,0,4]
assert mod2_betti(dual_faces)==[0,4,0,0,0]
print('MOD2_HOMOLOGY_ROBUST_AND_TOTAL_DUAL_OK', len(dual_faces), (9,36,44,26,6))
for name,op in ops.items():
    permutation = [3*op(*coord(v))[0]+op(*coord(v))[1] for v in V]
    trace_alternating = 0
    for mask in dual_faces:
        verts = [v for v in V if mask & (1<<v)]
        moved = [permutation[v] for v in verts]
        if sorted(moved) != verts:continue
        inversions=sum(moved[i]>moved[j] for i in range(len(moved))
                       for j in range(i+1,len(moved)))
        trace_alternating += (-1)**(len(verts)-1+inversions)
    first_homology_trace=1-trace_alternating
    def square_center_image(a,b):
        if name=='identity': return a,b
        if name=='rotation90': return b,4-a
        if name=='rotation180': return 4-a,4-b
        if name=='rotation270': return 4-b,a
        if name=='horizontal_reflection': return 4-a,b
        if name=='vertical_reflection': return a,4-b
        if name=='main_diagonal_reflection': return b,a
        if name=='other_diagonal_reflection': return 4-b,4-a
        raise AssertionError
    square_fixed=sum(square_center_image(*x)==x for x in centers)
    assert first_homology_trace == square_fixed
    print('DUAL_D4_CHARACTER',name,first_homology_trace)
# Exact integral five-cycle and unimodular dihedral orbit certificates.
# The certificate records cycles, not opaque ranks or logs.
import json
from pathlib import Path
with Path(__file__).with_name('integral_certificate.json').open(encoding='utf-8') as stream:
    cert=json.load(stream)
critical_top=sorted(f for f in unmatched if f.bit_count()==6)
matched_top=sorted(u for l,u in pairs if u.bit_count()==6)
matched_ridges=sorted(l for l,u in pairs if u.bit_count()==6)
assert critical_top==cert['critical_top_masks']
assert matched_top==cert['matched_top_masks']
assert matched_ridges==cert['matched_ridge_masks']

def boundary_incidence(upper,lower):
    if upper.bit_count()!=6 or lower.bit_count()!=5 or upper&lower!=lower:
        return 0
    verts=[v for v in V if upper>>v&1]
    removed=(upper^lower).bit_length()-1
    return (-1)**verts.index(removed)

# Bareiss fraction-free elimination computes the exact determinant.
def determinant_integer(M):
    a=[row[:] for row in M]
    n=len(a); sign=1;den=1
    for k in range(n-1):
        if a[k][k]==0:
            j=next((j for j in range(k+1,n) if a[j][k]),None)
            if j is None:return 0
            a[k],a[j]=a[j],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pivot-a[i][k]*a[k][j]
                assert num%den==0
                a[i][j]=num//den
            a[i][k]=0
        den=pivot
    return sign*a[-1][-1]

matched_boundary=[[boundary_incidence(u,l) for u in matched_top]
                  for l in matched_ridges]
assert abs(determinant_integer(matched_boundary))==1

cycles=[]
for idx,cyc in enumerate(cert['basis_cycles']):
    assert len(cyc)==len(set(mask for mask,coeff in cyc))
    z={int(mask):int(coeff) for mask,coeff in cyc}
    assert z and all(mask in faces and mask.bit_count()==6 and coeff!=0
                     for mask,coeff in z.items())
    assert [z.get(f,0) for f in critical_top]==[int(i==idx) for i in range(4)]
    assert all(sum(boundary_incidence(u,l)*x for u,x in z.items())==0
               for l in faces if l.bit_count()==5)
    cycles.append(z)
print('INTEGRAL_CYCLE_BASIS_OK',len(matched_top),[len(z) for z in cycles])

# A matrix of g acting on the integral homology basis is obtained by reading
# transformed critical face coefficients. This is legitimate because the
# certified cycles form a primitive top-homology basis.
def action(name):
    op=ops[name]
    perm=[3*op(*coord(v))[0]+op(*coord(v))[1] for v in V]
    mat=[[0]*4 for _ in range(4)]
    for j,z in enumerate(cycles):
        for face,x in z.items():
            vert=[v for v in V if face>>v&1]
            moved=[perm[v] for v in vert]
            mask=sum(1<<v for v in moved)
            if mask not in critical_top: continue
            inv=sum(moved[i]>moved[k] for i in range(6) for k in range(i+1,6))
            mat[critical_top.index(mask)][j]+=(-1)**inv*x
    return mat

def matvec(M,x):return [sum(a*b for a,b in zip(row,x)) for row in M]

R=action('rotation90'); S=action('main_diagonal_reflection')
x=cert['base_orbit_coefficients']
assert x==[-1,-1,-1,-1]
assert matvec(S,x)==[-a for a in x]
orbit=[x]
for _ in range(3):orbit.append(matvec(R,orbit[-1]))
assert matvec(R,orbit[-1])==x
orbit_matrix=[[orbit[j][i] for j in range(4)] for i in range(4)]
assert abs(determinant_integer(orbit_matrix))==1
print('INTEGRAL_D4_SIGNED_PERMUTATION_OK', 'orbit_basis_determinant',
      determinant_integer(orbit_matrix), 'orbit_basis_columns',orbit)

# On nine vertices, each geometric reflection permutes three disjoint pairs,
# and every rotation is even. The ambient orientation character is det.
for name,op in ops.items():
    perm=[3*op(*coord(v))[0]+op(*coord(v))[1] for v in V]
    sign=(-1)**sum(perm[i]>perm[j] for i in range(N) for j in range(i+1,N))
    assert sign==(-1 if 'reflection' in name else 1)
print('ALEXANDER_DUAL_INTEGRAL_TWIST_OK')
print('ALL_VERIFY_OK')
