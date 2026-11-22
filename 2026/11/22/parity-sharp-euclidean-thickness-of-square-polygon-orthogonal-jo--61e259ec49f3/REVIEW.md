# Self-review

## Correctness — PASS

The proof uses the exact support-function identity for an orthogonal convex-hull join, then minimizes a one-dimensional two-max envelope. On the middle scalar interval the only possible stationary point is a maximum; outside that interval the objective is monotone. For odd polygon order, the opposite support pair has an angular parametrization with product at least \(\cos(\pi/q)\ge1/2\), forcing both candidate envelopes to decrease to their shared unique equality angle. The equality classification counts explicitly all oriented normals and divides by antipodal identification. The inradius follows from symmetrization of any admissible ball centre and a separate scalar minimax. Taylor coefficients and the square–pentagon radical are direct algebra. A standard-library checker spot-tested the actual support functions and predicted equality normals for \(3\le q\le30\); sampling is not treated as exhaustive.

## Originality — PASS, provisional

The directly relevant full-text paper is Medgyes, arXiv:2611.10078v1, especially Sections 2.4, 5, and 7: it proves volume maximality and identifies the square–pentagon join but does not state a minimum-width or full minimizer-count theorem. The closest published mathematical records found discuss the same orthogonal joins but their spherical nearest-vertex depth probabilities or normal-cone selection masses; neither stated result yields a minimum of the *paired* supports \(h(u)+h(-u)\) or the parity census. Several exact-phrase, alias and implication searches were conducted; missing a prior paper remains possible. Search results are not a proof of novelty and published-record full text was not accessible from the retrieved links.

## Mathematical value — PASS

The object family contains the newly established unique nine-vertex sphere-inscribed volume maximizer. The exact minimum width is a natural directional thickness invariant of that benchmark and all its regular-polygon extensions, rather than an arbitrarily selected numerical statistic. The theorem gives a universal all-order formula, rigid complete minimizing normals, an even/odd doubling phenomenon, and a sharp gap between thickness and twice the inradius. The different asymptotic coefficients identify the persistent geometric effect of the missing antipodal polygon vertices.

## Limitations and risks

The argument does not handle unequal radii or nonregular factors; those are different optimization problems. Full-text accessibility of some related published records was limited to their semantic summaries. A sufficiently general unlocated theorem on thickness of orthogonal free sums might subsume the result. The proof and included finite experiments were reviewed by the same model, not independently audited.

Self-review: passed. Independent audit: not yet performed.
