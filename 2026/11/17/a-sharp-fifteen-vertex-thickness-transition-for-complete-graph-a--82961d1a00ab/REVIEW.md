# Mathematical assessment

## Correctness — PASS
The Minkowski-sum support calculation yields the exact subset-crossing counts and the exponentially increasing orbit coordinates. Reduction to two-level cut normals follows from the complete subset-facet structure of the difference permutohedron and insphere tangency. The complete-stage phase is proved by 36 exact integer comparisons below 15 and strict analytical inequalities for the infinite tail, with all equality cases. A standalone standard-library checker replays the stated finite checks. The unrestricted conclusion rests on the proof rather than samples.

## Originality — PASS (historical priority provisional)
Pešović–Stojadinović's graph-polytope definition and Postnikov's generalized permutohedron framework precede this result; these supply its objects and supporting representation, not the sharp Euclidean minimum-thickness transition. A closely related published complete-bipartite theorem has the same numerical phase threshold 15, but uses the mixed two-class tube count, rather than the complete-graph all-subsets count. A published fixed-uniformity hyper-permutahedron minimum-width theorem supplies the general cut approach, but does not imply the mixed-size strict phase. Undiscovered equivalent older theorems remain a genuine priority risk.

## Mathematical value — PASS
The sharp dimension threshold and exhaustive list of minimum-width directions distinguish two geometric phases of a canonical infinite family; the exact intermediate-stage cut formula also permits evaluation of every truncated graph interpolation. The phase classification depends on proved global inequalities and is not a routine single calculation.

## Limitations and reproducibility
Only the unscaled coordinate-simplex realization and intrinsic Euclidean norm are covered. Intermediate stages have a finite exact minimization formula, not a universal closed phase classification. Run `python3 verify_width.py` alongside this report; it uses standard-library exact arithmetic. The leading source was publicly available September 24, 2022.

Self-review: passed. Independent audit: not yet performed.
