# Scientific review

## Correctness — PASS
The graph distances determine the three Boolean clauses \(L,R,P\) for the complete pair types. Every single-vertex addition has one of six stated occupancy effects. Threshold capping each occupancy count at four preserves both current-visibility tests and post-addition tests, making an exhaustive 2360-type enumeration a proof for all \(n\ge4\). The attached standard-library program checks this complete finite decision table and independently checks \(1,397,760\) vertex subsets by shortest paths for orders four through nine. The seven surviving families have distinct configurations and enumerations that yield the stated polynomial. Computational evidence is supplementary; the capping lemma is essential.

## Originality — PASS, with provisional priority
The July 2023 primary preprint gives the definition and lower mutual-visibility framework without the near-crown distribution. The 2025 primary visibility-polynomial paper covers general polynomials and \(K_{n,n}\), not near-crowns. The 2025 class-by-class papers concern cycles and other families. A closely related, explicitly **known** 2026 OEIS entry enumerates all mutual-visibility sets of *perfect* crowns, \(K_{n,n}-M_n\). It does not give the inclusion-maximal polynomial after adding one unmatched vertex to each side. The relevant existing work on matching-deleted bicliques computes different parameters. Published record and primary source comparisons found no dominating statement, but an unindexed equivalent characterization remains a publication-priority risk.

## Mathematical value — PASS
The lower mutual-visibility number concerns greedy maximal configurations. A complete closed profile for a natural matching-deleted bipartite family determines all achievable sizes, their multiplicities, the unique maximum configuration, and an unbounded gap among maximal sizes. This goes beyond an isolated scalar invariant or an arbitrary small example and delineates a sharp behavior under adding unmatched vertices to a crown graph.

## Limitations
Only \(n\ge4\); not all visible sets or other visibility variants. Mathematical proof relies on a short, independently replayable exhaustive Boolean case analysis with a proved finite-state reduction. Priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.
