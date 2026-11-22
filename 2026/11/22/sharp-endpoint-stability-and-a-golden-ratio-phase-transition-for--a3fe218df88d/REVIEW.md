# Scientific review

## Correctness — PASS
The active-face KKT scalar multiplier is unique. Its Jacobian is an orthogonal hyperplane projection, giving exact absolute row sums. Every face is strictly attainable, and segment integration yields the global coefficient. The sorted-prefix reduction follows from the sign of \(a-\rho a^2\) under candidate additions/deletions, separately for the scalar row and a fixed spatial row. Exact factorization gives the planar branch transition and uniqueness. The standalone checker passed 13,838 supplementary assertions; these are not substitutes for the proof.

## Originality — PASS, with residual historical-priority uncertainty
The 2021 epigraphical projection source provides the scalar multiplier and general perspective framework, not an inspected exact globally optimized coordinate maximum-norm coefficient, prefix algorithm or golden-ratio phase. A 2015 paper directly analyzes derivatives of the *same* weighted epigraph cone. Its full text could not be accessed. No claim that its entire contents are noncovering is made; its potentially dominating derivative theorem is the principal unresolved historical source. Published records on fixed \(\ell_1\)-ball projection and Euclidean Lorentz-cone projection involve distinct sets or ambient objectives. Prior local derivatives are acknowledged rather than claimed as new.

## Mathematical value — PASS
For a canonical nonsmooth convex cone, this is an exact perturbation budget with polynomial evaluation, a sharp contractivity classification, an unattained normalized design infimum and a two-dimensional nonmonotone phase boundary. These distinctions matter when comparing geometric encodings and choosing weights in epigraph-based projections.

## Limitations and closest literature
The statement applies to Euclidean nearest-point projection and the unweighted coordinate maximum norm, finite dimensions and strictly positive weights. The 2015 differential-properties article is the closest known potential historical overlap, full-text comparison outstanding; the 2021 perspective-epigraph paper and other related projector records were compared in scope and implication. Independent validation is absent.

Self-review: passed. Independent audit: not yet performed.
