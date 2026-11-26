# Independent mathematical audit

## correctness

PASS

The quadratic form is the sum of three positively weighted squared differences and a strictly positive pin penalty, so the pinned matrix is positive definite. The supplied continuant correctly evaluates det(A_v-lambda I); four disjoint strict sign brackets exhaust the positive degree-four spectrum, and the interval quotient bounds compare the entire set of sites. Independently constructing all twelve characteristic polynomials and isolating their real roots using SymPy's exact polynomial interval procedure reproduced the nine strict winner inequalities for 2,4,2. For g tending to infinity, a unit Rayleigh minimizer has pinned coordinate tending to zero because the constrained Rayleigh minimum bounds its cost uniformly; compactness then gives convergence to the grounded principal minimum. Dividing the matrix by g in operator norm gives convergence to the rank-one projector and lambda_max/g -> 1. The minimum for site 2 is exactly 1: the isolated [1] block attains it and the other block minus identity has determinant 91 and positive first diagonal entry. The stated other-site test vectors have exact quotients 1/3, 650/677 and 110/147, each less than 1. A positive gap between the limiting scaled ratios therefore gives an eventual strict site-2 winner. Continuity and the finite strict margins give distinct changes in (10,50) and (50,500) and persistence under simultaneous small perturbations. The verifier docstring saying no floating-point operation is used is overbroad: line 67 converts exact bounds for diagnostic printing; no comparison assertion uses those floats.

## originality

PASS

The fixed-gain site-placement problem and augmented-Laplacian eigenratio are prior. The supported distinct claim is the strict return of the uniquely optimal site on one fixed weighted four-path, with a provable eventual winner and finite-gain perturbation robustness, not the general dependence of site choices on gain. The 2024 weighted path paper is the most plausible unresolved comparison; no claim about its unexamined fixed-gain content is made.

## value

PASS

A strict switch and return among all four placements on one simple fixed graph refutes the idea that a change in common gain generates only a one-way ordering of preferred sites. The test is exact, persists under simultaneous parameter perturbations, and includes a provable high-gain tail, so it is useful as a structural counterexample and a tiny regression case for gain-aware placement rather than a numerical tie or an isolated spectral value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
