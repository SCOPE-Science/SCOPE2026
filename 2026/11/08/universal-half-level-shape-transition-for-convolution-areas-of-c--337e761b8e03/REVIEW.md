# Scientific review of the co-oriented parallelogram transition

## Correctness — PASS

The conclusion is a global minimum over all planar pairs sharing two edge directions, with both areas fixed, for every real \(0<\theta<1\). The proof verifies affine covariance, symmetry under exchanging the bodies, the exact overlap law (an atom plus two uniform ramps in each coordinate), and the explicit two-variable area integral. It then excludes both crossed-ratio sectors by a strictly negative derivative and proves the sharp nested-sector minimization by a one-variable arithmetic-geometric mean comparison. Equality, the entire critical minimizer manifold, and the derivative cusp follow from strictness and the explicit branches. The independent-coordinate numerical quadrature in `verify.py` completed 6,171 reproducible checks; finite checks are supporting evidence only. The only assumptions are positive areas, a common unordered pair of edge directions, and a threshold strictly between zero and one.

## Originality — PASS, with historical-priority limitations

The 2026 study by Martín Goñi addresses the unrestricted normalized Brunn--Minkowski lower envelope, attained by oppositely related simplices in its exact regime. It neither states nor implies the minimum within aligned parallelograms with two separately fixed areas. The 2013 and 2024 general convolution-body papers establish the definition, affine framework, and general estimates. Gasparyan–Ohanyan (2014) computes the *single-body* parallelogram covariogram, not the constrained two-body optimization. The 2024 preprint of Haddad addresses planar *self*-convolution bodies. Published mathematical-record searches and primary-literature searches sought aliases such as rectangular cross covariograms, superlevel sets of products of triangular overlap functions, and half-level phase transitions. No encompassing result was found. The novelty claim excludes the elementary factorized overlap formula itself, standard affine invariance, and the known global inequalities. Unindexed older special-case formulas remain a genuine historical-priority risk, and search silence is not a mathematical proof of novelty.

## Mathematical value — PASS

At fixed areas, general convex-body lower bounds do not describe which *parallelogram* geometry is best. The theorem solves this natural affine-constrained problem exactly, identifies a ratio-independent critical level, proves a full minimizer classification including a nonisolated critical family, and quantifies the sharp cusp. It gives a model case in which smoothing by convolution-level interpolation changes the optimal geometry discontinuously. The result is not claimed to settle arbitrary orientations, arbitrary convex bodies, or independent historical priority.

## Verification and external review

Run the fully standalone `verify.py` with standard Python 3 to reproduce the numerical checks. Universal correctness rests on the analytic proof in `RESULT.md`. No external or independent mathematical assessment has been conducted.

Self-review: passed. Independent audit: not yet performed.
