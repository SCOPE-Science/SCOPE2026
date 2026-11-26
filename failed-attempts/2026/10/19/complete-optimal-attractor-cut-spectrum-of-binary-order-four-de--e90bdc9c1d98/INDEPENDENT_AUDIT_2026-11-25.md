# Independent mathematical audit

## correctness

PASS

Each of the 16 distinct length-four windows must be hit; each mark hits at most four. Equality partitions their starting positions into disjoint consecutive blocks of four, forcing the marks at 4,8,12,16. Every cyclic class contains one unique occurrence of 0000, so a prefix walk anchored there that appends an unused four-gram until all 16 are visited and checks final closure enumerates the classes exactly once. Running python3 /workspace/reproductions/attractor.py generated 16 classes and all 256 cuts, used the union of the occurrence intervals for each nonempty factor to verify full, not just sharp, attractors, and reproduced every frozen TSV witness and minimum, including the lexicographically first five-position witnesses. It returned 192 four-mark cuts, 64 five-mark cuts, and cycle histogram {8:4,12:8,16:4}. No higher-order claim was tested or needed.

## originality

FAIL

A distinct earlier-dated Resultary record states the same full classification, the unique four-set, and the same 16 cycle profiles, and even supplies a common five-set. The frozen census is correct, but there is no distinct mathematical remainder supported by its additional individual witnesses.

## value

FAIL

The all-cuts question is mathematically motivated and the enumeration is useful for replication. As a claimed distinct finding, however, the exact profiles and the rigidity statement are already recorded, with a stronger five-mark assertion. Recomputed witnesses for known minima do not yield a separate useful invariant or new bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
