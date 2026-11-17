# Scientific review

## Correctness: PASS

The proof fixes the standard orthonormal coordinates, identifies all within-edge midpoint sums and rules out all extraneous cross-edge collisions by distinct edge-coordinate supports and independent graph-vertex basis differences. It then proves complete recovery of core adjacency, pendant edges and isolated single-edge components. The squared-distance signature identifies equal midpoints precisely because the vertices affinely span their hull. The \(O(m^3)\) algorithm and the congruence equivalence follow directly. Standalone exhaustive integer regression checks 814 graph cases through five vertices and 157 additional seeded cases through eight vertices. The infinite theorem rests on the proof, not on those tests.

## Originality: PASS, with priority risk

The foundational 2017 source **already observed shared midpoints in triangle gluing**; that observation is credited and excluded from the contribution. The 2022 face theorem already recognizes centered cross-polytope vertex faces. A relevant 2025 account embeds the construction into ternary polytopes; 2026 work handles duals and canonical forms. The newly assessed statement is the exhaustive no-spurious-collision classification and the algorithmic inverse from **only unlabeled Euclidean distances**, with all degenerate leaf and disconnected cases and a cubic complexity bound. Similar published work on diameter-graph colorings and covariance volume does not imply this exact metric-only algorithm. There remains a historical-priority risk from an unindexed inverse theorem or an implicit consequence of the earlier face-lattice theory.

## Mathematical value: PASS

The inverse problem asks whether the graph-to-polytope construction loses information when all graph labels, ambient coordinates and facet incidences are forgotten. A complete and explicit answer is natural: the full metric determines the source graph, and cubic-time reconstruction avoids potentially expensive convex-hull and face enumeration. The distinction between repeated midpoint classes and unique pairs, the exact treatment of leaves and \(K_2\) components, and sharp necessity of the no-isolates assumption are structural rather than an arbitrary finite calculation.

## Closest prior work and limits

Arkani-Hamed–Benincasa–Postnikov (2017) introduced triangle midpoint gluing; Kühne–Monin (2022) gave all face classes, including centered cross-polytope vertex faces; Lavrov (2025) generalized the ternary-relation framework. Earlier results on cosmological diameters and covariance address different metric invariants. This work does not claim the existing gluing or vertex-face descriptions as new. Its exact-distance algorithm does not prove noise stability or apply automatically to other representations.

Self-review: passed. Independent audit: not yet performed.
