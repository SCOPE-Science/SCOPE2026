# Scientific review: four-variable recognition of projective-plane incidence graphs

## Correctness — PASS

The six explicitly stated closed clauses all use only four variable names. Their first four clauses force an exactly two-sided bipartition defined internally through the common-neighbor relation. The degree and common-neighbor clauses force the incidence and quadrangle axioms, and any finite projective plane conversely satisfies them. The lower bound uses a permanent three-pebble invariant: the Fano \(2\)-\((7,3,1)\) design and its complementary \(2\)-\((7,4,2)\) design have all relative one-point adjacency extension patterns present for up to two occupied vertices. Yet the complementary incidence graph violates the unique common-neighbor clause. All three separately implemented standard-library verification programs reproduce the indicated finite examples. Their finite experiments do not replace the universal proof.

## Originality — PASS, qualified

The comparison examined full texts of De Winter–Lazebnik–Verstraëte (2008), which characterizes projective planes by extremal graph-cycle counts; Pikhurko–Verbitsky (2010), which develops the general variable-width/pebble-game framework; and Venema (1999), which axiomatizes a *two-sorted modal logic* for projective planes rather than sharp one-sorted graph FO-variable recognizability. Searches for 4-variable projective-plane recognition, Fano/complement-Fano three-pebble indistinguishability, and related symmetric-design equivalence found no covering statement. The searched results concerned other invariants (homology, topology, regularity) or other graph families. This supports provisional originality but is not exhaustive: an older logical definability theorem or translation could imply the characterization.

## Mathematical value — PASS

The result has a natural object and a sharp boundary: the entire class of finite projective-plane incidence graphs, regardless of order or coordinatizability, has a dimension-independent four-variable recognition sentence but cannot be recognized at width three, even at unlimited depth. The lower bound also exposes the much larger three-variable equivalence class of symmetric designs, a reusable distinction between graph-combinatorial local regularity and global incidence axioms. This is a complete, motivated logical classification boundary rather than a narrow finite tabulation.

## Limits and closest background

Only finite simple graphs, the pure adjacency/equality language, and ordinary counting-free first-order logic are covered. The proof does not optimize quantifier rank or identify all three-variable equivalent graphs. The literature-priority risk remains nonzero; this review is not an independent certification.

Self-review: passed. Independent audit: not yet performed.
