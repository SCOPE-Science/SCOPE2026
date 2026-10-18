from itertools import permutations, combinations

M = [
    [-2,0,4,6,4,0],
    [0,-2,0,4,6,4],
    [4,0,-2,0,4,6],
    [6,4,0,-2,0,4],
    [4,6,4,0,-2,0],
    [0,4,6,4,0,-2],
]

# The deck involution is the half-turn j -> j+3 (zero-based indices).
deck = tuple((j+3) % 6 for j in range(6))
assert all(M[deck[i]][deck[j]] == M[i][j] for i in range(6) for j in range(6))
assert deck == (3,4,5,0,1,2)

orbits=[]
seen=set()
for i in range(6):
    if i not in seen:
        o=tuple(sorted({i,deck[i]}))
        seen.update(o)
        orbits.append(o)
assert sorted(orbits) == [(0,3),(1,4),(2,5)]

# Each opposite pair has intersection 6; adjacent and distance-two pairs have 0 and 4.
for i in range(6):
    assert M[i][(i+1)%6] == 0
    assert M[i][(i+2)%6] == 4
    assert M[i][(i+3)%6] == 6

# UFD degree obstruction used in the square-presentation proof:
# a factor of q1*q2*q3 can only have degree equal to a sum of 2's.
possible_subset_degrees={2*len(S) for r in range(4) for S in combinations(range(3),r)}
assert possible_subset_degrees == {0,2,4,6}
assert 3 not in possible_subset_degrees

print('VERIFY_OK')
