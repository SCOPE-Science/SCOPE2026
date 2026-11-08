"""Independent four-triangle block contraction of the finite Potts sector spectrum."""
from itertools import product
from collections import defaultdict

# Each triangle i carries three colors indexed by the other tetrahedral vertices in sorted order.
other = {i: tuple(j for j in range(4) if j != i) for i in range(4)}
states = tuple(product(range(3), repeat=3))
entry = [dict(zip(other[i], s)) for i in range(4) for s in states]
expected_e = (4,3,2,1,0,1,2,4,6,9,12,15,18)
expected_count = (24,192,504,480,120,480,384,960,480,576,192,24,1)
# Precompute triangle-local color collisions and occupied preferred-color sites.
local = []
for s in states:
    col = [sum(x == c for x in s) for c in range(3)]
    local.append((col[0], sum(t*(t-1)//2 for t in col)))
hist = defaultdict(int)
for a in range(27):
    for b in range(27):
        for c in range(27):
            for d in range(27):
                indexes = (a,b,c,d)
                row = [dict(zip(other[i], states[indexes[i]])) for i in range(4)]
                k = sum(local[z][0] for z in indexes)
                e = sum(local[z][1] for z in indexes)
                for i in range(4):
                    for j in range(i+1,4):
                        e += int(row[i][j] == row[j][i])
                hist[k,e] += 1
assert sum(hist.values()) == 3**12
for k in range(13):
    best=min(e for kk,e in hist if kk==k and hist[kk,e]>0)
    assert (best,hist[k,best])==(expected_e[k],expected_count[k])
for x,expected in ((-1,1320),(1,984),(2,1824),(3,1273)):
    best=min(expected_e[k]-x*k for k in range(13))
    actual=sum(expected_count[k] for k in range(13) if expected_e[k]-x*k==best)
    assert actual==expected
# The sector envelope is the 5 supporting affine pieces; prove for all real x
# by checking ordered slopes and every intervening lattice point.
vertices=(0,4,6,8,12)
slopes=[]
for left,right in zip(vertices,vertices[1:]):
    num=expected_e[right]-expected_e[left]
    den=right-left
    slopes.append((num,den))
    for k in range(left,right+1):
        assert (expected_e[k]-expected_e[left])*den >= num*(k-left)
assert slopes==[(-4,4),(2,2),(4,2),(12,4)]
print('BLOCK_CONTRACTION_PASSED',len(hist),'nonzero sector-energy cells; total',sum(hist.values()))
