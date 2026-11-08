# Self-review

## Correctness — PASS

The proof defines precise component lengths using two variable names: predecessor/successor depth formulas recover the exact rank and co-rank in a strict chain. A \(k\)-variable formula chooses up to \(k\) pairwise incomparable witnesses of a given chain length. In the other direction, the permanent \(k\)-pebble invariant tracks component lengths and within-component ranks; at most \(k-1\) occupied components remain after lifting a moving pebble. The invariant survives every move, proving all-quantifier-rank equivalence. The relative width formula, canonical minimum representative, and Euler product follow. Checks were independently replayed from packaged paths. No inference from finite checking to infinite cases is used.

## Originality — PASS, qualified

Queries of mathematical research records and inspected source material did not identify the same all-width disjoint-chain classification or its logical partition spectrum. Grohe–Schweikardt (2005) studies variable-fragment succinctness on one linear order and supplies a length-detection ingredient, not arbitrary component multiplicities. Szwast–Tendera (2013) studies general transitive-relation models and does not state this special invariant in inspected sections; its broad decidability claim was subsequently corrected and is not relied upon. Nearby records about finite weak orders, directed paths, and complete multipartite graphs do not imply this exact statement in the strict-order signature without additional reasoning. A general finite-variable disjoint-union composition theorem might nonetheless cover the result; this is an explicit residual priority risk. The underlying partition Euler identity is classical and is not claimed as new.

## Value — PASS

The precise gap is a complete, sharp fixed-variable equivalence invariant for a natural infinite class of finite posets containing chains of arbitrarily many lengths and arbitrarily many components. In addition to the theorem, it gives a unique minimum representative, exact individual defining widths within the class, a strict hierarchy, and the unexpected identification of the theory spectrum with restricted integer partitions. These are mathematically motivated classification invariants rather than a single arbitrary numerical sample.

## Limits

Pure strict-order signature, nonempty finite disjoint-chain posets, no counting quantifiers, no claim for arbitrary posets or global defining width. Computations corroborate only finite samples. Novelty is provisional pending independent exhaustive literature review. Independent mathematical audit not performed.

Self-review: passed. Independent audit: not yet performed.
