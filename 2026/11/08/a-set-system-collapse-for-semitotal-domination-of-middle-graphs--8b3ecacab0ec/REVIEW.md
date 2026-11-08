# Review of the middle-graph semitotal-domination set-system theorem

## Correctness

PASS. The domination characterization reduces exactly to the selected original vertices and selected edge-vertices covering all original vertices. The proof establishes that every selected original vertex and every selected edge-vertex has a distinct selected partner at distance at most two using only connectedness and the at-least-three-vertices hypothesis. The finite sum follows from independent choices among already-covered original vertices. The path/cycle minimum census is exhaustive because capacity forces either a perfect matching (even order), one removed original vertex plus a perfect matching, or a one-overlap edge cover (odd order); these exhaust all equality cases. Independent enumeration on 1,004 connected root instances and paths/cycles through order 12 agreed.

## Originality

PASS, provisional priority. Full text of arXiv:2609.33932, particularly Theorem 2.2 and its proof, concerns the minimum independent domination layer, not all possibly nonindependent dominating sets. Full text of arXiv:2008.02975, particularly Sections 2 and 3, establishes the edge-cover equality and path/cycle scalar bounds but not the all-set semitotal equivalence or the exact enumerator and optimizer counts. Specific searches for equivalent set families, semitotal middle-graph domination polynomials, and minimum-solution enumerations did not disclose a covering statement. This is evidence of an uncovered gap, not proof of world-first priority. Classical 1978 sources are partially inaccessible and remain a named risk.

## Mathematical value

PASS. An additional distance-two support constraint usually changes the feasible-set system, but disappears identically on an infinite graph-operator class. Consequently the whole semitotal-domination polynomial, not just its minimum degree, can be calculated from the original graph's edge-subset coverage data. Complete optimizer classifications and parity-sensitive exact counts on both paths and cycles give concrete non-scalar consequences. These facts are not implied by equality of the previously known minimum numbers.

## Closest sources and limitations

The principal direct comparisons are arXiv:2609.33932 (2026) and arXiv:2008.02975 (2020). The result does not give a faster algorithm for general graph domination-polynomial computation, does not cover the connected two-vertex boundary, and does not claim the previously known minimum sizes as novel. Full texts of selected early 1978 sources could not be reviewed. No independent validation is asserted.

Self-review: passed. Independent audit: not yet performed.
