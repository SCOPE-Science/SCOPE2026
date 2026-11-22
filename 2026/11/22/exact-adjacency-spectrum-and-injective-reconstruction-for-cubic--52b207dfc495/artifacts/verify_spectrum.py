"""Exact finite certificate for the intersection-four graph of cubic-contact bitangent hexads.

Only Python standard library is required. The linear-algebra certificate is integral.
"""
from itertools import combinations
from collections import Counter, defaultdict
from fractions import Fraction
from math import comb

def parity(x):
    return (x.bit_count() & 1)

def q(x):
    return parity((x & 7) & (x >> 3))

def pairing(x, y):
    return parity(((x & 7) & (y >> 3)) ^ ((x >> 3) & (y & 7)))

odd = tuple(x for x in range(64) if q(x))
assert len(odd) == 28
odd_set = set(odd)
blocks = set()
for tup in combinations(odd, 5):
    sixth = 0
    for v in tup:
        sixth ^= v
    if sixth in odd_set and sixth not in tup:
        blocks.add(tuple(sorted((*tup, sixth))))
blocks = sorted(blocks)
assert len(blocks) == 6048
lookup = {b:i for i,b in enumerate(blocks)}

def even_triples(tup):
    return sum(q(x ^ y ^ z) == 0 for x,y,z in combinations(tup,3))
type_of = [0 if even_triples(B)==20 else 1 for B in blocks]
assert Counter(even_triples(B) for B in blocks) == {20:1008,12:5040}
parts = [[i for i in range(len(blocks)) if type_of[i] == t] for t in (0,1)]
assert [len(x) for x in parts]==[1008,5040]

def orbit(seed):
    visited = {seed}
    queue = [seed]
    for index in queue:
        bs = blocks[index]
        for w in range(1,64):
            qw = q(w)
            moved = tuple(sorted(x ^ w if (qw + 1 + pairing(x,w))%2 else x for x in bs))
            target = lookup[moved]
            if target not in visited:
                visited.add(target)
                queue.append(target)
    return visited
assert orbit(parts[0][0]) == set(parts[0])
assert orbit(parts[1][0]) == set(parts[1])

# Disjoint-type intersection-four adjacency, sparse column neighbors.
col_lists = [[] for _ in parts[1]]
pos1 = {b:j for j,b in enumerate(parts[1])}
# Each admissible pair of hexads sharing four elements is found via tetrads.
tetrad0 = defaultdict(list)
tetrad1 = defaultdict(list)
for i in parts[0]:
    for subset in combinations(blocks[i],4):
        tetrad0[subset].append(i)
for i in parts[1]:
    for subset in combinations(blocks[i],4):
        tetrad1[subset].append(pos1[i])
row_adj = [set() for _ in parts[0]]
pos0 = {b:j for j,b in enumerate(parts[0])}
for quad,left in tetrad0.items():
    for i in left:
        for j in tetrad1.get(quad,()):
            row_adj[pos0[i]].add(j)
            col_lists[j].append(pos0[i])
assert all(len(s)==45 for s in row_adj)
assert all(len(col)==9 and len(set(col))==9 for col in col_lists)
assert sum(map(len,row_adj))==45360
assert all({i for i in col_lists[j]} == {i for i in range(1008) if j in row_adj[i]} for j in range(5040))

G = [defaultdict(int) for _ in range(1008)]
for neighbors in col_lists:
    for a in neighbors:
        for b in neighbors:
            G[a][b] += 1
assert all(G[i].get(i,0)==45 for i in range(1008))
assert all(sum(row.values())==405 for row in G)

def multiply(v):
    return [sum(w*v[j] for j,w in row.items()) for row in G]

def poly_multiply(A,B):
    out=[0]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        for j,b in enumerate(B):out[i+j] += a*b
    return out
factors=[[-21,1],[-24,1],[-45,1],[-48,1],[-405,1],[3888,-141,1],[19440,-285,1]]
poly=[1]
for f in factors:
    poly=poly_multiply(poly,f)
assert len(poly)==10
# Full zero matrix follows by transitivity: it suffices to check the first column.
v=[0]*1008
v[0]=1
powers=[v]
for k in range(1,10):
    powers.append(multiply(powers[-1]))
for i in range(1008):
    assert sum(poly[k]*powers[k][i] for k in range(10))==0

# Since the action is transitive, trace(G^k) = 1008 (G^k)_{0,0}.
traces=[1008]+[1008*powers[k][0] for k in range(1,7)]
def pair_sum(A,B,k):
    if k==0: return 2
    if k==1: return A
    x,y=2,A
    for _ in range(2,k+1):
        x,y=y,A*y-B*x
    return y
S=[]
for k in range(7):
    S.append([Fraction(r**k) for r in (21,24,45,48,405)] +
             [Fraction(pair_sum(141,3888,k)), Fraction(pair_sum(285,19440,k)),Fraction(traces[k])])
# Exact fraction Gaussian elimination for multiplicities.
for col in range(7):
    pivot=next(j for j in range(col,7) if S[j][col])
    S[col],S[pivot]=S[pivot],S[col]
    p=S[col][col]
    S[col]=[x/p for x in S[col]]
    for row in range(7):
        if row==col:continue
        p=S[row][col]
        S[row]=[S[row][j]-p*S[col][j] for j in range(8)]
mult=[row[7] for row in S]
assert mult==[105,280,168,330,1,35,27],mult
print('CHECK_OK hexads=6048,types=(1008,5040),exchange_edges=45360')
print('G_polynomial_coefficients_ascending',poly)
print('G_trace_powers_0_to_6',traces)
print('G_factor_multiplicities',mult)
