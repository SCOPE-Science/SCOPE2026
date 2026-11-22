# Scientific review

## Correctness — PASS

The fixed-forest extension probability is reconstructed by contracting forest components and using the weighted complete-graph tree enumerator. It gives exact probabilities \(2/n\) for one edge, \(3/n^2\) for incident edge pairs, and \(4/n^2\) for disjoint pairs. The weighted matrix-tree theorem recovers the *previously known* binomial edge-count law. A coupling at fixed edge count, using exchangeable uniform matchings and explicit wedge-probability bounds, proves the whole-graph total-variation inequality. The wedge Poisson limits follow from fixed-order factorial moments: vertex-disjoint wedges supply the limiting moments, and all overlapping union types vanish at the critical scale. The point-process limit follows from independent-edge Laplace functionals transferred by graph total variation. The finite checker passed 142 exact rational assertions, supplementing but not replacing the infinite proofs.

## Originality — PASS, with priority limitations

The reviewed primary full texts are Grimmett–Winkler's paper on negative dependence of uniform spanning-tree edges (arXiv:math/0302185), Hackl–Panholzer–Wagner on uncovering the vertex-labeled tree and its *edge counts* (arXiv:2301.00664, especially Section 2), and Janson on uncovering graph edge-count and small-subgraph fluctuations (arXiv:2312.13823, especially Sections 1 and 9). The exact edge-count marginal and scalar first-edge scale are already covered or directly implied by Hackl–Panholzer–Wagner and are expressly not asserted to be novel. The distinct claim is a total-variation coupling for the **full labeled induced graph**, its sharp \(n^{2/3}\) obstruction distinguished by two Poisson wedge intensities, and the labeled-endpoint point-process law. Further nearby scientific records on *bivariate induced-edge counts* and *singleton-count covariances* were compared by statement and inspected in full; neither of those scalar/bivariate-count results states the complete induced-graph approximation or sharp wedge separator. No publication search can exclude unpublished or unindexed equivalent results; independent priority certification remains outstanding.

## Value — PASS

The precise scale \(k=o(n^{2/3})\) characterizes when an induced random tree may be replaced by an independent-edge random graph as a **whole labeled object**. The threshold failure is witnessed by a natural, easily observable local motif with distinct explicit intensities \(3c^3/2\) and \(2c^3\). Thus the result identifies where a common independent-edge approximation breaks and why, with a location-marked Poisson description at the earlier edge-onset scale. This is a structural threshold with use for analysis of random-tree uncovering and local rare subgraphs, rather than an arbitrary finite statistic.

## Closest sources and limitations

The 2023 and 2025 works treat number-of-edge processes, including results implied by the present proof; they are explicitly credited. The 2003 source supplies a verified archival anchoring and edge-dependence context, not the new claim. Index coverage cannot prove absence of earlier equivalent work. The upper bound is not optimized and the exact critical total-variation limit is not calculated. Computer checks cover only \(3\le n\le7\); infinite-dimensional results rely on the mathematical proof.

Self-review: passed. Independent audit: not yet performed.

