# Independent mathematical audit

## correctness

PASS

The synchronous rule can be computed from four shifted copies of the infection mask, one per coordinate. A vertex is added if its bit occurs in at least two of those copies. Each nonterminal step strictly increases the mask. An independent exact census over all 65,536 masks gave 63,687 percolating sets and 256 minimal ones; one-vertex deletion tests suffice by monotonicity. The size/time counts were (3,4):48, (3,5):96, (4,3):16 and (4,4):96. Taking all affine coordinate permutations of each representative gave four disjoint orbits whose union equals the minimal census. Enumerating Hamming signatures, XOR and disjointness of the two distance-one pairs at sizes 3 and 4 gave the same set exactly. There were 96 five-round triples and 96 five-round four-sets, with no other sizes, and direct inclusion tests gave a bijection by unique extension (e.g. {0011,0100,1000} extends by 1100). All slow four-sets are nonminimal since they contain their slow triple.

## originality

PASS

The two minimal four-seed isomorphism classes, the five-round maximum, and an example in the slow-triple orbit are prior work and credited. What is supported as distinct is the joint labelled geometry/time census and the exhaustive equality classification with its unique extension bijection. No inspected distinct record establishes those claims.

## value

PASS

The four-cube already distinguishes minimum-size spanning seeds from larger irredundant seeds, so their full geometry/time census specifies a natural transition rather than an arbitrary slice. The exact equality cases for a known sharp time bound are useful independently: a five-round triple has a unique one-vertex augmentation that does not speed up spreading, and these are all the nonminimal equality cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
