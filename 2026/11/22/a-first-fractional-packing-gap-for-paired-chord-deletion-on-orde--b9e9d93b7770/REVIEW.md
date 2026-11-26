# Independent mathematical audit

## correctness

PASS

Each unordered pair has two endpoints, the endpoint order is fixed, and the deletion output is the set of distinct order-standardized submatchings after removal of one whole pair. Equivalently, generate words with exactly two copies of each symbol and canonicalize symbols by first appearance; remove both copies of one symbol and canonicalize again. A code is valid exactly when its nonempty shadows are disjoint. The subset recurrence partitions by whether the least remaining output is unused or is covered by its unique selected source, counting distinct sources even when their shadows coincide. Independent exact replay (/workspace/reviews/replay-5.py, standard library) generates canonical double words by a Cartesian product, constructs shadows by deleting a symbol type, and exhausts sorted disjoint-shadow source subsets of the certified upper-bound size without using that recurrence or a maximal-clique algorithm. It confirms source counts (1,3,15,105), output counts (1,1,3,15), maxima (1,1,3,7), and multiplicities (1,3,1,278). For m≤3 summing the receiver constraints gives P_m≤number of outputs, and the rederived optimal codes attain this bound. At m=4 the packaged seven sources have pairwise disjoint shadows and the certified descriptions match the reconstructed indices. The integer half-unit primal loads are 2 at 14 outputs and 1 at one; the dual covers have values 2,3,4 at respectively 31,50,24 sources. Both totals are 15 half-units, and all weights are nonnegative, proving P_4=15/2 by weak duality and A_4≤7 by integrality. Thus the standard LP optimum first differs from the integer value at m=4, though flooring still gives 7. Reversing each word and recanonicalizing is the same order reversal as the endpoint map, preserves the code family, and fixes exactly 136 of the 278 maxima; enumeration of orbit representatives and Burnside both give 207. No claim is made about arbitrary two-position deletions, reconstructing from the full deck, larger m, or any other symmetry quotient. The source checker was inspected as evidence, not executed.

## originality

PASS

Qualified best-of-knowledge assessment for the exact first LP gap and optimal-code census of the whole-pair, order-standardized channel. The underlying ordered matchings, double-word representation, shadow-packing LP and generic packing machinery are not claimed new.

## value

PASS

The channel asks a natural zero-error question under the removal of one complete matching edge, so the first discrepancy between integral and fractional shadow packing is meaningful without a theorem for all sizes. The sharp small case has an exact rational certificate and a complete, nontrivial equality and reversal census useful for checking future constructions and LP relaxations. The gap is fractional only: the floor of the relaxation still gives the right capacity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
