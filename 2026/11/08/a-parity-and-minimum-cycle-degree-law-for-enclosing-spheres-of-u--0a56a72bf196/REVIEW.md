# Review of the enclosing-sphere parity theorem

## Correctness — PASS

Central symmetry uniquely fixes the minimum-ball center at zero. Strict convexity reduces contacts to signed zonotope endpoints, for which the exact objective is \(\sum_v(|\operatorname{outdeg}(v)-\operatorname{indeg}(v)|+t)^2\). An even cycle admits two globally pure orientations; an odd cycle forces at least one mixed cycle vertex. A mixed degree-\(d\) vertex incurs at least \(4(d+t-1)\) squared-radius loss. Orientations with one defect of minimum cycle degree attain the bound. The equality analysis yields four distinct contacts per admissible defect vertex. The standalone verifier passed 8,490 formula/contact comparisons and 216 independent full-endpoint enumerations.

## Originality — PASS (provisional historical priority)

The complete accessible motivating paper by Glew introduces the Minkowski sum, facets, and face factorization, but not these Euclidean radius/contact formulas. The closest published geometrical comparisons are the full-coordinate cone-zonotope law and the edge-only complete-multipartite graphical zonotope theorem; neither includes the unicyclic in-in norm or its parity/degree law. The cone comparison is not an isometry: in the triangle example the squared full-cone radius is 20 versus 19 in the in-in coordinate metric. Prior literature on maximum *minimum* imbalance addresses a different objective. Targeted primary-literature, published mathematical-record, and accessible existing-claim comparisons found no covering result. Unindexed equivalent orientations or later literature remain a priority risk.

## Value — PASS

This is a complete and exact Euclidean extremal classification for a natural infinite graph-indexed family introduced in recent literature. Cycle parity and a single graph-theoretic local statistic control both the entire radius defect and a sharp two-versus-many contact transition, including all equality cases and diametral pairs. The result is not a generic symmetric-body bound or a computation of a small isolated instance; it persists under arbitrary pendant tree attachments and a continuous positive segment-length parameter.

## Limits

The theorem is realization-specific; it does not cover multiple cycles, arbitrary edge weights, or vanishing coordinate half-length. Exact finite verification corroborates the proof but does not replace it. Priority is provisional and independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
