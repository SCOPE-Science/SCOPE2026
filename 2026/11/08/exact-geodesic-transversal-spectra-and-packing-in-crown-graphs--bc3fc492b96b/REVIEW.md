# Scientific review

## Correctness — PASS

The proof identifies every maximal geodesic as a three-edge path between the two vertices of a deleted matched pair, with two distinct intermediate indices. The reduction to missing-shore index sets \(R,C\) is an exact if-and-only-if statement. Its three alternatives are exhaustive and disjoint after the stated inclusion-exclusion adjustment. Inclusion-minimality is proved in both directions for each class, including the coincident degrees at \(n=4\). The vertex-disjoint packing construction works because \(\lfloor n/2\rfloor\ge2\) for every stated order. Independently implemented breadth-first-search and endpoint-extension tests checked all \(87,296\) vertex subsets for orders \(4\) through \(8\). No finite test is used as an infinite proof.

## Originality — PASS, subject to publication-priority risk

The primary 2021 geodesic-transversal paper defines the invariant and proves complexity/algorithmic results for trees and spread cactus graphs, with a short complete-bipartite observation, but not this matching-deleted-biclique classification. The 2022 geodesic-packing paper proves general packing/transversal inequalities, rook-graph results and tree/strong-product results; it does not give the crown-graph formulas. The 2023 networks paper treats meshes, tree-derived networks, coronas and chemical networks, not crowns. The 2021 maximal-shortest-path-cover paper addresses the equivalent invariant but its accessible descriptions and inspected sections do not identify an encompassing crown theorem. Database searches for crown, matching-deleted biclique, geodesic transversal, maximal shortest path cover, and diametral path transversal found related but different results, notably counts of geodesic subpaths and edge-metric bases. The absence of coverage in these searches is not proof of global priority. A full-text access limitation for one related journal article and possible unindexed treatments are genuine residual risks.

## Mathematical value — PASS

This is a motivated complete classification for a classical regular bipartite graph family of a recently introduced hitting-path invariant. It gives not only the minimum but the all-set and inclusion-minimal polynomials, upper-minimal parameter, exact cardinality gaps, and the dual geodesic-packing number. In particular, a three-family minimal-set structure creates an unbounded gap between sizes \(n\) and \(2n-4\), a phenomenon not implied by the minimum geodesic transversal number alone. The exact formulas may serve as benchmarks for path-hitting and packing algorithms.

## Limits

The theorem is for \(n\ge4\), and the computational census is through \(n=8\). Priority relative to unindexed or inaccessible literature is not established conclusively. The proof is self-contained but has not received independent review.

Self-review: passed. Independent audit: not yet performed.
