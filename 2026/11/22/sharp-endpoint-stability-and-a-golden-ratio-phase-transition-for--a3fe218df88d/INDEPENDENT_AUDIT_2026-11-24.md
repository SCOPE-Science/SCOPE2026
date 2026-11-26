# Independent mathematical audit

## correctness

PASS

The KKT multiplier outside the cone is the unique positive root of tau+lambda=sum_j w_j(|y_j|-lambda w_j)_+. On a fixed strict signed cell the nonzero block is the Euclidean hyperplane projection I-vv^T/(1+S_I), v=(s_j w_j,-1); inactive rows vanish. The scalar and coordinate absolute row sums are exactly those claimed. The apex derivative is zero on the interior apex cell, not necessarily on its boundary; continuity and a finite subdivision of any input segment into closed affine cells suffice there. Every signed nonempty support occurs on an open cell, by prescribing positive active magnitudes, lambda=1, zero inactive inputs, and tau=weighted output level minus 1. A small displacement of the input with signs matching the maximizing row attains the row-sum quotient. For a positive optimal ratio rho (dividing out w_i in a fixed spatial row), adding or deleting a nonmandatory weight is controlled exactly by a-rho a². Hence all weights below the common threshold 1/rho are selected and those above are excluded, with equality weights interchangeable; a sorted prefix exists even with ties. Prefix sums of weights and squares plus a membership test give O(1) per candidate after sorting. The identity row covers nonpositive excesses. Singletons force all weights to be one for nonexpansivity, and the full support then gives 2n/(n+1), which is also the maximum since the unit-weight row sums are 2k/(k+1) at support size k. The product-one geometric family has largest weight M at each support; when M>=R the scalar excess is O(1/R), its largest coordinate has nonpositive excess, and all other weights are at most M/R² giving O(1/R²). When M<=1 at most one weight is 1 and the rest are O(R^-2). This proves the unattained infimum. In the plane the only potentially dominating rows reduce to A and B by the singleton and larger-weight comparisons. Their difference factors at 1 and the golden ratio, and the derivative numerator for B is strictly increasing on [1,infinity), negative at 1 and positive at the golden ratio. A decreases strictly past 1, and factoring B-1/3 proves the single nontrivial return before the switch. Independent bisection of the stated polynomials gives r_* about 1.203277832047, r_c about 1.485583997689 and L(r_*) about 1.363352315804, consistent with the frozen approximations.

## originality

PASS

The general proximal root formula and active-face projection calculus are not new; in this polyhedral problem the finite row-sum formulation is a direct consequence once all the faces are accessible. The supported contribution is the explicit global sensitivity analysis, in particular the normalized weight-design infimum and nonmonotone planar switch, with the prefix optimization for the full two-input map. The closest inspected catalogue results have a fixed level or a squared-norm proximal map. The closest 2015 paper on the same epigraph's differential properties was not obtainable as full text; it remains a specific priority caveat, not evidence of coverage or noncoverage.

## value

PASS

The exact coordinate sensitivity answers a stability question not answered by Euclidean nonexpansivity, and the prefix reduction makes an otherwise exponential active-face maximum evaluable in quadratic arithmetic. The fixed-product design comparison is meaningful: stable limiting anisotropy is unattainable at finite weights, and even in two coordinates an initial departure from balance worsens amplification before the governing output row changes. These provide usable computation and a sharp counterpoint to weight-balancing intuition, not a new local calculus for its own sake.

The dated certificate retains the supplied scientific assessment, sources and limitations.
