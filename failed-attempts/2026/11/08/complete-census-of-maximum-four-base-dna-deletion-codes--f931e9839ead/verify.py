"""Independent standard-library verification of the length-four DNA-code census.

Run: python3 verify.py maximum_codebooks.tsv
This separately builds the compatibility graph and uses Bron--Kerbosch pivot
recursion (rather than a greedy-coloring branch bound) to find maximal cliques.
"""
import itertools
import sys
from collections import Counter

ALPHABET = "ACGT"
COMP = dict(zip("ACGT", "TGCA"))

def reverse_complement(word):
    return "".join(COMP[c] for c in word[::-1])

def deletion_set(word):
    return {word[:i] + word[i+1:] for i in range(len(word))}

words = ["".join(x) for x in itertools.product(ALPHABET, repeat=4)]
orbits = []
for word in words:
    mate = reverse_complement(word)
    if word >= mate:
        continue
    if deletion_set(word).isdisjoint(deletion_set(mate)):
        orbits.append((word, mate))
assert len(orbits) == 120

shadows = [deletion_set(a) | deletion_set(b) for a,b in orbits]
N = len(orbits)
neighbors = [set() for _ in range(N)]
for i in range(N):
    for j in range(i):
        if shadows[i].isdisjoint(shadows[j]):
            neighbors[i].add(j)
            neighbors[j].add(i)

maxima = set()

def bron_kerbosch(chosen, possible, excluded):
    if len(chosen) + len(possible) < 11:
        return
    if not possible and not excluded:
        assert len(chosen) <= 11, "Candidate larger than the established optimum"
        if len(chosen) == 11:
            maxima.add(tuple(sorted(orbits[i][0] for i in chosen)))
        return
    # Every maximal clique has a representative in P minus N(pivot).
    pool = possible | excluded
    pivot = max(pool, key=lambda x:len(possible & neighbors[x])) if pool else None
    branch = possible - (neighbors[pivot] if pivot is not None else set())
    for v in sorted(branch):
        bron_kerbosch(chosen + [v], possible & neighbors[v], excluded & neighbors[v])
        possible.remove(v)
        excluded.add(v)

bron_kerbosch([], set(range(N)), set())
assert len(maxima) == 44, len(maxima)

# Cross-check an independently generated complete certificate.
if len(sys.argv)>1:
    with open(sys.argv[1],encoding="utf-8") as inp:
        listed = {tuple(line.strip().split("\t")) for line in inp if line.strip()}
    assert listed == maxima, (len(listed),len(maxima))

permutations = []
for tuple_perm in itertools.permutations(ALPHABET):
    mapping = dict(zip(ALPHABET,tuple_perm))
    if all(mapping[COMP[c]] == COMP[mapping[c]] for c in ALPHABET):
        permutations.append(mapping)
assert len(permutations) == 8

def transformed(code, permutation):
    return tuple(sorted(min("".join(permutation[c] for c in w),
                                reverse_complement("".join(permutation[c] for c in w)))
                        for w in code))

unassigned = set(maxima)
orbit_sizes=[]
representatives=[]
while unassigned:
    example = min(unassigned)
    images = {transformed(example,mapping) for mapping in permutations}
    assert images <= maxima
    unassigned.difference_update(images)
    orbit_sizes.append(len(images))
    representatives.append((len(images),example))
assert sorted(orbit_sizes) == [4,4,4,4,4,4,4,8,8]
if len(sys.argv)>2 and sys.argv[2] != "--write-reps":
    with open(sys.argv[2],encoding="utf-8") as inp:
        listed_representatives = {(int(parts[0]),tuple(parts[1:]))
            for line in inp if (parts := line.strip().split("\t"))}
    assert listed_representatives == set(representatives)
common = set.intersection(*(set(code) for code in maxima))
assert common == {"AAAA", "CCCC"}
assert Counter(len(set().union(*(shadows[orbits.index(next(o for o in orbits if o[0]==word))] for word in code)))
               for code in maxima) == Counter({60:28,56:8,64:8})
if "--write-reps" in sys.argv:
    for sz,ex in representatives:
        print(str(sz)+"\t"+"\t".join(ex))
print("INDEPENDENT_VERIFICATION_OK",len(maxima),"maxima;",len(orbit_sizes),
      "symmetry classes; compulsory pairs",','.join(sorted(common)))
