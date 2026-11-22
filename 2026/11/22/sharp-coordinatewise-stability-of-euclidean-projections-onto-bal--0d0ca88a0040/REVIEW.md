# Scientific review: sharp coordinatewise stability of ball–cube projection

## Correctness — PASS

The KKT system for the intersection of a coordinate cube and a Euclidean ball yields clipped scalar scaling. On a smooth stratum with \(k\) saturated coordinates, the free-block Jacobian is \(s^{-1}(I-uu^{\mathsf T})\). Its exact maximum row sum reduces to a one-variable optimization subject to an explicit feasible interval. Cauchy–Schwarz proves the upper bound, and a capped-face KKT construction with \(s\downarrow1\) realizes all permitted upper bounds as limiting two-input quotients. Euclidean nonexpansivity and integration along generic segments justify the global bound. The explicit thirteen-coordinate strict comparison and the limiting radius jump are algebraically verified. The standalone test file passed 2,951 supplementary numerical assertions; these are corroboration, not proofs of infinite parameter statements.

## Originality — PASS, with residual priority risk

Direct literature comparison used the accessible mathematical text of Liu–Wang–Song (2019), including its optimization model, KKT characterizations, and algorithms for intersections of \(\ell_1\) and \(\ell_2\) balls; the norm cap here is instead \(\ell_\infty\), and the desired invariant is a two-input sharp coordinatewise modulus. Vasil'eva (2020) analyzes Kolmogorov widths of norm-ball intersections, including the present set type but not sensitivity of Euclidean nearest-point projection. Bauschke–Bui–Wang (2017) concerns intersections of cones with balls or spheres; the inspected abstract and available excerpt do not settle box–ball projection stability. A publicly indexed theorem on Euclidean-ball clipping recovers the already-known contained-ball regime only, not the saturated-face regime or the discontinuity at \(r=\sqrt n\). The closest retrieved projection and affine-projection results concern other sets or different operators. Earlier work on bound-constrained trust-region projections may contain equivalent formulas, especially if expressed through active-set condition numbers: historical priority is not independently established.

## Mathematical value — PASS

Simultaneous amplitude and energy constraints define a canonical, naturally parameterized convex feasibility set. The exact two-input coordinatewise robustness constant matters for errors bounded individually rather than in Euclidean total magnitude. The finite formula distinguishes clipping-active faces from the no-clipping ball boundary, finds a nontrivial thirteen-coordinate example where the former wins, and shows that the sharp stability modulus is not continuous at the exact redundancy threshold of the energy constraint. These are structural properties of a natural full parameter family rather than an arbitrary finite numerical slice.

## Scope and limitations

The theorem applies to real centered uniform box constraints and an origin-centered Euclidean ball in dimensions \(n\ge2\), with global \(\ell_\infty\)-to-\(\ell_\infty\) perturbation measurement. It gives no result for nonuniform boxes, translated balls, other fidelity metrics, or independent scholarly verification. Finite perturbation tests do not certify the all-dimensional claim. The most relevant related source on intersection-of-balls widths was read in full HTML; the conic-projection publication was only partly accessible, so an implicit prior result remains possible.

Self-review: passed. Independent audit: not yet performed.
