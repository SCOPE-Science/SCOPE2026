# Scientific review

## Correctness — PASS
The claim is stated for all nondegenerate Euclidean triangles with normalized boundary arclength, not area. The Spieker barycentric weights follow from the three weighted side-midpoint contributions. The one-vertex boundary-arc minimization is reduced to a one-variable strictly convex rational function with either a feasible W-line or a boundary cevian. A separate monotonicity argument shows that the vertex opposite the longest side controls the global minimum. The endpoint branch is strictly above one-third by the strict triangle inequality; the W-line branch is handled by a feasible-ratio bound and an exact polynomial factorization. The flattened isosceles limit demonstrates sharpness without claiming equality in a degenerate triangle. `verify.py` performs independent angular/segment tests; their finite status is explicitly limited.

## Originality — PASS (priority provisional)
The motivating 2026 Berele--Catoiu paper treats lines through the area centroid and proves the sharp \(3/10\) lower limit; the present exact two-branch result is for the different perimeter centroid and proves the sharp \(1/3\) lower limit. The 2022 Amadtohed--Chaidee--Racha-in--Theerakarn envelope description treats all perimeter proportions for each triangle, but does not state the specific Spieker minimax or the sharp uniform inequality, and this conclusion requires further shape-dependent optimization. A priori the envelope approach could be specialized to derive the new statement; this is the principal historical-priority risk. Actual published-finding corpus comparison queries and accessible historical claims revealed related but not equivalent explicit results, without establishing absolute novelty.

## Mathematical value — PASS
A canonical, explicitly constructible geometric center is shown to be a uniform centerpoint for the triangle's perimeter measure, unlike the area centroid's \(3/10\) worst case. The exact two-regime profile and the identified minimizing vertex/line provide shape-sensitive information beyond an existential centerpoint bound, with a sharp degenerating extremal family. The natural invariant and proof are independent of exhaustive enumeration.

## Limits
No conclusion for arbitrary convex curves, arbitrary measures, or global optimality of the Spieker point. Unindexed classical sources and possible implicit derivation from full envelope literature remain prior-art risks. The independent audit is outstanding.

Self-review: passed. Independent audit: not yet performed.
