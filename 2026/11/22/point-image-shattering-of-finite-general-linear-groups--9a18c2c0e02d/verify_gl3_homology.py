"""Enumerate the binary 3-dimensional partial-basis-bijection complex and its F2 boundary rank."""
from itertools import combinations, permutations, product

def rank_binary(numbers):
    pivots = {}
    for number in numbers:
        while number:
            p = number.bit_length()-1
            if p not in pivots:
                pivots[p] = number
                break
            number ^= pivots[p]
    return len(pivots)

vectors = list(range(1,8))
cells = list(product(vectors,vectors))
cell_index = {e:i for i,e in enumerate(cells)}
faces = [[],[],[],[]]
faces[0] = [()]
faces[1] = [(i,) for i in range(49)]
faces[2] = [(i,j) for i,j in combinations(range(49),2)
            if rank_binary([cells[i][0],cells[j][0]]) == 2
            and rank_binary([cells[i][1],cells[j][1]]) == 2]
for xs in combinations(vectors,3):
    if rank_binary(xs) < 3:continue
    for ys in combinations(vectors,3):
        if rank_binary(ys) < 3:continue
        for perm in permutations(ys):
            faces[3].append(tuple(sorted(cell_index[pair] for pair in zip(xs,perm))))
assert [len(f) for f in faces] == [1,49,882,4704]
edge_index = {e:i for i,e in enumerate(faces[2])}
pivots = {}
for triangle in faces[3]:
    boundary = 0
    for e in combinations(triangle,2):boundary ^= 1 << edge_index[e]
    while boundary:
        p=boundary.bit_length()-1
        if p in pivots:boundary ^= pivots[p]
        else:pivots[p]=boundary;break
rank_boundary_2=len(pivots)
# The one-skeleton is connected: two cells can be connected via a cell
# with a different first and second coordinate, or via two such cells.
rank_boundary_1=48
betti_1=len(faces[2])-rank_boundary_1-rank_boundary_2
betti_2=len(faces[3])-rank_boundary_2
assert (rank_boundary_2,betti_1,betti_2)==(834,0,3870)
print('f_vector=1,49,882,4704')
print(f'rank_boundary_1={rank_boundary_1} rank_boundary_2={rank_boundary_2}')
print(f'betti_1={betti_1} betti_2={betti_2}')
print('GL3_HOMOLOGY_PASS')
