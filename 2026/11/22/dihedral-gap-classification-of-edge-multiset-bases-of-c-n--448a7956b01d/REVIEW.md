# Review: dihedral gap classification of edge-multiset bases of \(C_n\)

## Correctness — PASS
The argument applies to every integer \(n\ge7\), not just tested orders. An equality of unordered edge-distance codes yields a permutation of the three landmarks; the edge-centre isometry lemma proves that each matched landmark is transported by the corresponding rotation or reflection. An identity is impossible, a transposition yields either a reflection-symmetric triple or the \(n\equiv2\pmod4\) antipodal exception, and a three-cycle forces a repeated clockwise gap. Both obstructions produce explicit edge-code collisions. Inclusion–exclusion gives the exact all-order count; all surviving gap triples have trivial dihedral stabilizers. The standalone BFS graph-distance checker exhaustively agrees for \(3\le n\le28\). The prior scalar result supplies the minimum cardinality three for \(n\ge7\).

## Originality — PASS (provisional historical priority)
The 2023 foundational paper [1, Section 4.6, Theorem 12] proves a scalar dimension of three and exhibits a specific resolving triple, but does not enumerate or classify all bases. A 2026 survey [2, Section 6.1, Theorem 6.4] repeats that scalar cycle result without a gap characterization. The new claim is a statement about *all* bases and their dihedral equivalence classes, not simply a different example attaining the known bound. Searches for edge-multiset cycle resolving bases, cyclic gaps, equivalent antipodal conditions, and general stronger results in a mathematical findings index did not identify a result whose conclusions imply these assertions. Comparable results on edge-general-position cycles, monitoring edge-geodetic cycles, multiset vertex resolution and edge-metric resolution concern different predicates. Historical priority cannot be guaranteed by bounded searches; unindexed or unpublished computations remain possible.

## Mathematical value — PASS
The count of landmark bases is a natural refinement of a published edge-identification invariant, whose minimum cardinality alone gives no information about available optimal placements. The result supplies a complete all-size-of-cycle classification, an exact formula and orbit count, and isolates a nonobvious mod-four antipodal obstruction while the scalar dimension remains fixed. The new all-order structural description is more informative than a routine re-evaluation of a known scalar value.

## Limits and sources
The theorem concerns three-element bases of simple unweighted cycles of order at least seven only, not larger resolving sets. Exact finite checking is corroboration rather than a proof of all orders. Independent mathematical verification and exhaustive priority clearance have not been performed.

[1] Ikhlaq, Ismail, Siddiqui, Nadeem, “A New Technique to Uniquely Identify the Edges of a Graph,” *Symmetry* 15 (2023), 762, DOI:10.3390/sym15030762; Section 4.6.

[2] Farhan, Klavžar, Kuziak, Yero, “Multiset resolvability parameters in graphs: A survey with new results and open problems,” arXiv:2607.10311; Section 6.1.

Self-review: passed. Independent audit: not yet performed.
