# Scientific review

## Correctness: PASS

The definition of the binary one-step tortoise map agrees with the published map. The proof distinguishes zero, one, and at-least-two marker classes. Every multi-marker factor is parameterized by its first marker index and starting offset; the second marker must be the next power marker. The first one in the tortoise image has position \(K=r+2^j-1\), and the disjoint dyadic intervals for \(K\) establish unique recovery. Summing all admissible first-marker gaps yields \(M(n)\), the two exact complexities, and the \(n=1\) boundary. The direct and structural checkers independently reproduced the formulas at stated finite lengths. No experimental check is substituted for the proof.

## Originality: PASS relative to inspected evidence

The closest primary work is Campbell--Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811 (2026), especially Theorem 1. Its uniform bounded-defect theorem assumes bounded gaps between ones; the sparse word here has unbounded gaps and an exactly linear defect. Its applications concern Thue--Morse and paperfolding, not the power-marker indicator. Defant--Kravitz (arXiv:1809.09158) supplies the map and studies sorting/preimage behavior, not this factor-complexity instance. Searchable related work on the power-marker word concerns distinct invariants (minimal absent factors, string attractors, and parsing), and related tortoise findings concern other source words. The implication comparisons do not show a prior theorem covering this exact claim. An unindexed equivalent remains a residual risk, and an independent historical-priority review is still outstanding.

## Value: PASS

The known bounded-defect theorem leaves a concrete structural boundary: whether bounded symbol gaps can be removed while maintaining linear factor complexity. The result establishes a sharp negative answer through an exact entire-length loss \(n-1\), gives the full dyadic image-complexity profile, and isolates the only nontrivial inverse fiber of a sorting map. This is a motivated infinite family of identities with a conceptual explanation; not an arbitrary finite table or an unsupported claim of broad classification.

## Scientific limitations

The proof is restricted to the fixed power-marker source and one tortoise step. It does not imply a converse or classify other sparse words. Finite tests validate computations but not priority. A complete independent audit of correctness and originality remains unperformed.

Self-review: passed. Independent audit: not yet performed.
