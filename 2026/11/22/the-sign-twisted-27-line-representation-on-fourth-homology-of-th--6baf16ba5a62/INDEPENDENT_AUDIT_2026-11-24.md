# Independent mathematical audit

## correctness

PASS

The marked divisor classes give the 27 vertices and intersection-zero gives geometric disjointness. No seven can be mutually skew: their Gram matrix would be negative definite of rank seven in signature (1,6). I independently enumerated cliques without a size cutoff and computed signed boundary ranks modulo 3 (rather than the supplied mod-two elimination). With augmented face counts 1,27,216,720,1080,648,72 the ranks in ascending face size are 1,26,190,530,550,72. Every rational rank is at least its modular rank, and consecutive sums saturate the chain dimensions through degree three and the last boundary saturates degree five. This forces each displayed rational rank and leaves only degree four, of dimension 26. I regenerated all Weyl permutations using five exceptional swaps and the Cremona reflection in the last rather than first three exceptionals, checking graph preservation, word determinant consistency, size 51840, and complete partition into 25 conjugacy classes. Each generator is an actual Picard root reflection, so its root determinant is -1. To check traces independently, discard non-skew cycles on the 27 lines and construct the compatibility graph of surviving cycles. An invariant simplex consisting of j cycles on m vertices contributes (-1)^(m-1)(-1)^(m-j)=(-1)^(j-1); the empty face contributes -1. The resulting reduced traces over all 25 classes agree exactly with root determinant times (fixed lines minus one); e.g. -14 for the 15-fixed-line reflection and +8 for the nine-fixed-line order-three class. Reduced homology is in even degree four so no further sign appears. Character equality yields the rational module by finite-group semisimplicity and descent of character equality to Q. This is an exhaustive finite certificate, not sampled evidence for an arbitrary surface. Replay: python3 /workspace/audit-checks/skew.py.

## originality

PASS

Only the full signed rational homology-character identification is credited. The identical complex and stronger nonequivariant homotopy type are already known. The closest same-day equivariant result gives a complete unsigned face permutation census, and its orbit-union algorithm is a useful starting point for an alternate character computation. Its actual output sums the orbit-unions with positive weight, not with the parity of their number of constituent line orbits. The exact compact relation between the resulting signed alternating sum and the reflection determinant times the line augmentation character is not asserted there and does not follow from the unsigned cycle table alone.

## value

PASS

The topological invariant is the natural homology action of the full Weyl group on a canonical geometric line complex. Knowing there are 26 generators does not identify this action or even the sign of reflection trace. The formula identifies every class trace via an easily accessible fixed-line count and the root sign and hence fixes the rational representation, useful for studying any subgroup action or comparing with the known permutation representations. This is more than the new listing of some unoriented face counts or recomputation of a known Betti number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
