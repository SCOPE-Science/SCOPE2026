# Independent mathematical audit

## correctness

PASS

The finite model contains precisely the 255 nonempty subsets of the 8 binary words of length three. Direct literal string-state recursion examines every ordered maximum-overlap pair and all legal tie breakings, while an independent Hamilton-path/permutation recurrence computes true shortest-superstring length; distinct equal-length originals are substring-free. Reimplemented both independent recurrences over all 255 masks and confirmed max G/OPT=10/7 and exact masks 31,87,234,248, each |S|=5, OPT=7,G=10. Explicit S* has optimal witness 0100011 and legal 10-letter greedy chain. Independent C++ verifier and full census.csv were inspected. This is genuine finite exhaustion, not extrapolation to longer words.

## originality

PASS

The closest Chukhin-Kulikov-Mihajlin-Smal 2026 theorem establishes unrestricted-alphabet length-three greedy ratio 9/5, not the fixed binary sharp 10/7; arbitrary-alphabet upper bounds cannot determine equality and its four-word-set orbit. Resultary search found no other covering binary length-three theorem beyond this target. Historical priority remains conditional: inaccessible full Chukhin et al. text and possible prior unindexed finite tables must be disclosed.

## value

PASS

Binary is the smallest nontrivial alphabet, and 3-mers are the first regime where nontrivial ordered overlaps matter. The strict decrease from unrestricted 9/5 to 10/7 and a full classification of all equality sets supply a natural benchmark for fixed-alphabet shortest-common-superstring approximations, useful independently of any larger theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
