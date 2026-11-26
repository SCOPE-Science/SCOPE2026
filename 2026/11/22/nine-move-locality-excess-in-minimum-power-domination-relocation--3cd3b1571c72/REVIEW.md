# Independent mathematical audit

## correctness

PASS

The construction is the duad–syntheme incidence graph. A fresh enumeration used sequential forcing: an enabled still-unobserved target remains enabled as observation grows, so iteration to a fixed point gives the same least closure as synchronous rounds. Exhaustive testing at sizes 0 through 4 yielded counts 0,0,0,0,6540. Bucketing the four-sets by a shared triple generates exactly all jumps without duplicates; filtering the two differing vertices by incidence generates exactly the slides. I checked all 1440 permutations used for orbit reduction against the base graph. The induced side-preserving action is full: two duads have a common syntheme iff disjoint, and in the complementary intersection graph on duads the size-five cliques are exactly the six stars; fixing the stars fixes the duads and hence the synthemes. A checked duality supplies the other coset. Orbit BFS reaches all 6540 states in both graphs; weighting source histograms by orbit size and halving distinct ordered counts gives the exact unordered histograms. This independently reproduced the ten orbit rows, 126240 and 23040 edges, the jump radius and diameter 4, slide radius 11 and diameter 13, and slide eccentricity counts 1680,3420,1440 at 11,12,13. The penalty histogram agrees at every entry. Its largest entry index is 9, attained by 1440 pairs, all at (jump,slide)=(4,13); I also checked legality and geodesicity of the recorded 13-slide path.

## originality

PASS

The closest inspected work supplies the general minimum-sensor reconfiguration framework, cubic bounds, or the same comparison on different named cages. It does not imply the exact optimum family and complete sharp joint distance census on this cage. The indexed exact hit was the assigned record itself. This is a best-of-knowledge comparison, not historical priority certification.

## value

PASS

This canonical small cage is a natural fixed-budget benchmark: connectedness survives local moves, yet imposing physical adjacency forces a sharp nine-move overhead on a nontrivial class of pairs. The exact pair census and orbit profiles separate typical from extremal behavior and let a researcher verify a relocation algorithm on a symmetric instance with genuine obstructions. This is more informative than an isolated optimum count or diameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
