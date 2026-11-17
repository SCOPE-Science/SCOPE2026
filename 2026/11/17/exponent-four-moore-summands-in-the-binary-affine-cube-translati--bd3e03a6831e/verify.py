#!/usr/bin/env python3
"""Exact standard-library check of the translation quotient of binary AG(3,2)."""
from itertools import combinations, permutations
from collections import Counter
from math import gcd

V = range(8)

def xor_all(indices):
    ans = 0
    for i in indices:
        ans ^= i
    return ans

def mask(indices):
    return sum(1 << i for i in indices)

def translate_mask(m, v):
    return mask(i ^ v for i in V if (m >> i) & 1)

def translates(chain):
    return [tuple(translate_mask(m, v) for m in chain) for v in V]

def representative(chain):
    return min(translates(chain))

def det(A):
    # Exact permutation formula, used only on matrices of size at most four.
    n = len(A)
    if n == 0:
        return 1
    out = 0
    for p in permutations(range(n)):
        inv = sum(p[i] > p[j] for i in range(n) for j in range(i+1,n))
        prod = 1
        for i in range(n):
            prod *= A[i][p[i]]
        out += (-1 if inv % 2 else 1)*prod
    return out

def invariant_factors(A):
    n = len(A)
    previous = 1
    factors = []
    minors = []
    for k in range(1, n+1):
        g = 0
        for rr in combinations(range(n), k):
            for cc in combinations(range(n), k):
                g = gcd(g,abs(det([[A[i][j] for j in cc] for i in rr])))
        assert g % previous == 0
        minors.append(g)
        factors.append(g // previous)
        previous = g
    return factors, minors

# Affine independence over GF(2): every distinct triple is independent,
# a four-subset is independent if and only if its point XOR is nonzero.
faces = set()
for k in range(1,5):
    for comb in combinations(V,k):
        if k < 4 or xor_all(comb) != 0:
            faces.add(mask(comb))
face_counts = tuple(sum(m.bit_count()==k for m in faces) for k in range(1,5))
assert face_counts == (8,28,56,56)
planes = tuple(mask(c) for c in combinations(V,4) if xor_all(c)==0)
assert len(planes) == 14
assert all(translate_mask(m, v) in faces for m in faces for v in V)

# All strict inclusion flags of the face poset, indexed by flag dimension.
levels = [sorted(m for m in faces if m.bit_count()==k) for k in range(1,5)]
flags = [set() for _ in range(4)]
for sizes in (s for k in range(1,5) for s in combinations(range(4),k)):
    for ch in __import__('itertools').product(*(levels[i] for i in sizes)):
        if all(ch[i] & ch[i+1] == ch[i] for i in range(len(ch)-1)):
            flags[len(ch)-1].add(ch)
original_flags = tuple(len(level) for level in flags)
assert original_flags == (148,1176,2352,1344)

# Translation preserves ranks in a flag, so the action on the barycentric
# subdivision has no inversions. Orbit flags are genuine quotient simplices.
reps = [sorted({representative(c) for c in level}) for level in flags]
indexes = [{c:i for i,c in enumerate(level)} for level in reps]
counts = tuple(len(level) for level in reps)
assert counts == (22,147,294,168)

# Independent Burnside verification of orbit-flag counts.
for dimension, level in enumerate(flags):
    fixed_sum = sum(sum(all(translate_mask(m,v)==m for m in ch) for ch in level) for v in V)
    assert fixed_sum == 8 * counts[dimension]

# Signed orbit-flag boundaries. Each flag is oriented in increasing rank order.
B = []
for d in range(1,4):
    entries = {}
    for col, chain in enumerate(reps[d]):
        acc = Counter()
        for i in range(d+1):
            face = chain[:i] + chain[i+1:]
            acc[indexes[d-1][representative(face)]] += (-1)**i
        for row,value in acc.items():
            if value:
                entries[(row,col)]=value
    B.append(entries)

def chain_squared_zero(B):
    for low in range(2):
        a,b = B[low], B[low+1]
        bycolumn = {}
        for (i,j),v in b.items():
            bycolumn.setdefault(j,[]).append((i,v))
        for j,items in bycolumn.items():
            check=Counter()
            for i,v in items:
                for (r,c),w in a.items():
                    if c==i:check[r]+=v*w
            assert not any(check.values())
chain_squared_zero(B)

# Exact integral cellular cancellations: a +-1 differential coefficient
# produces a contractible chain summand. Schur-complement updates are integral.
active=[set(range(n)) for n in counts]
cancel_counts = [0,0,0]
for degree in [1,2,3,1,2,3]:
    b=B[degree-1]
    while True:
        row_degrees=Counter(i for i,j in b)
        col_degrees=Counter(j for i,j in b)
        pivots=[(row_degrees[i]*col_degrees[j],i,j,v)
                for (i,j),v in b.items() if abs(v)==1]
        if not pivots:break
        _,r,c,p=min(pivots)
        row={j:v for (i,j),v in b.items() if i==r and j!=c}
        col={i:v for (i,j),v in b.items() if j==c and i!=r}
        for i,x in col.items():
            for j,y in row.items():
                new=b.get((i,j),0)-x*y*p
                if new:b[i,j]=new
                else:b.pop((i,j),None)
        for i in (*col,r):b.pop((i,c),None)
        for j in row:b.pop((r,j),None)
        active[degree-1].remove(r)
        active[degree].remove(c)
        if degree>1:
            B[degree-2]={ij:v for ij,v in B[degree-2].items() if ij[1]!=r}
        if degree<3:
            B[degree]={ij:v for ij,v in B[degree].items() if ij[0]!=c}
        cancel_counts[degree-1]+=1
assert tuple(cancel_counts)==(21,126,164)
assert tuple(map(len,active))==(1,0,4,4)
assert not B[0] and not B[1]
chain_squared_zero(B)
rows=sorted(active[2]); cols=sorted(active[3])
remaining=[[B[2].get((i,j),0) for j in cols] for i in rows]
invariants,determinantal_divisors=invariant_factors(remaining)
assert invariants==[2,4,4,4]
assert determinantal_divisors==[2,8,32,128]

# Euler characteristic and Lefschetz sanity checks from the unquotiented complex.
assert sum((-1)**k*v for k,v in enumerate(face_counts))==-20
assert sum((-1)**k*v for k,v in enumerate(counts))==1
assert 8-28+56-56 == 1-21
for t in range(1,8):
    fixed_pairs=[m for m in levels[1] if translate_mask(m,t)==m]
    assert len(fixed_pairs)==4
    assert not any(translate_mask(m,t)==m for m in levels[0]+levels[2]+levels[3])
# Each nonzero translation fixes an edge barycenter, the key condition
# in the orbit fundamental-group theorem.
print('AG(3,2) independent faces:',face_counts)
print('Affine planes:',len(planes),'covering top Betti number:',21)
print('Barycentric flags:',original_flags)
print('Quotient flag cells:',counts)
print('Integral unit cancellations by degree:',tuple(cancel_counts))
print('Remaining 3-boundary:',remaining)
print('Determinantal divisors:',determinantal_divisors)
print('Nonunit Smith factors:',invariants)
print('Quotient Euler characteristic:',1)
print('Topological deduction: simply connected; wedge M(Z/2,2) and 3 M(Z/4,2).')
