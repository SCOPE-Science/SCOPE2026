# Independent mathematical audit

## correctness

PASS

Strict convexity of tr[(L+11ᵀ/(2s))⁻¹] on the connected feasible edge weights follows by the positive inverse-trace Hessian and injectivity of the edge-weight-to-Laplacian map. The compact stochastic domain has finite candidates and divergent objective toward disconnection; thus the unique optimizer is fixed by nongateway permutations and clique interchange. The within-clique zero-sum eigenvalue is u+(s−1)v with total multiplicity 2(s−2). The symmetric two-level modes give 0 and su; the antisymmetric block has sum su+2t and product 2ut, yielding the stated reciprocal trace. At fixed u>0 the objective strictly decreases with v and t, independently saturating both budgets. The resulting scalar objective has strictly positive second derivative and opposite infinite derivative limits at the two endpoints. For x=su, the scaled objective tends locally uniformly to 2+1/x+1/[2(1−x)]. A fixed interior comparison bounds the optimum uniformly; the reciprocal terms force x bounded below and t=1−(1−1/s)x bounded below, so x is uniformly away from 1 for large s. The limiting unique optimum is 2−√2, with objective 7/2+√2 and bridge √2−1. Setting all edge weights to 1/s gives s²/2+3s−3 exactly. Full inverse matrices reproduce representative cases, including the maximum-degree normalization.

## originality

PASS

Fixed-stationarity convex optimization already covers the problem formulation, and prior work calculates the degree-proportional walk. A particularly close same-date fastest-mixing barbell result has the same limiting bridge constant, so the numerical constant alone is not a distinct contribution. For x=su of order one, the smallest antisymmetric eigenvalue is asymptotic to 2xt/[s(x+2t)], so the slow mode is common to the spectral objectives; the Kemeny optimum also needs to optimize all other eigenvalues. The distinct claim supported here is the exact finite-size inverse-trace optimizer and all-hold saturation, with the corresponding optimal value and benchmark gap.

## value

PASS

For a natural bottleneck family this provides the complete symmetric allocation, with proof that no holding or asymmetric design improves it. A bridge carrying constant probability despite the growing clique degrees and a drop from quadratic to linear Kemeny cost explain an order-of-growth failure of the maximum-degree heuristic. This is more than restating a solver or recognizing a matching limiting constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
