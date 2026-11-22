# Scientific review

## Correctness
The active inequality set has independent second-difference rows and a strictly complementary preimage, so its interpolation-space orthoprojector is an actual local Jacobian of convex regression. The explicit discrete mass matrix gives a diagonally dominant Jacobi inverse, with a unique geometric bulk Green kernel and a dominating geometric tail. A sign calculation computes the central row norm exactly. Convex-combination rows establish the exact operator norm of the bi-infinite discrete spline projection, without assuming a finite-face norm limit. Monotonicity under adjoining an unconstrained last coordinate extends the lower bound to all dimensions. The included checker tests 692 finite exact/numerical statements, not the infinite proof.

## Originality
The nearest published discrete convex-regression result, *Five-point nonlocal instability and a persistent lower bound for convex least-squares projection* (2026-11-01), proves \(1+1/\sqrt2\) using alternating curvature; its stated formulas neither contain nor dominate the period-three \((9+2\sqrt{33})/11\) result. A periodic continuous-spline derivative norm has a different domain and norm; the alternating continuous-spline projector concerns Lebesgue instead of discrete counting measure. The 2020 convex-regression algorithm paper and the older spline projection paper supply underlying methods rather than this exact extremal coefficient. Searches did not locate an equivalent earlier calculation, but old discrete Green-kernel literature could contain one.

## Mathematical value
The bound is a structurally distinct and quantitatively stronger obstruction to dimension-free sup-norm stability, improving the best located asymptotic lower bound from about 1.7071 to 1.86265. The exact algebraic coefficient also supplies a reproducible benchmark for the bi-infinite discrete piecewise-linear least-squares projection, making the link between curvature-face geometry and sensitivity explicit.

## Limits and priority risk
The result does not compute the unrestricted sharp limiting constant or handle irregular designs. Some earlier exact Green-matrix results may imply the face coefficient without matching wording; the accessible relevant full texts were compared but bibliography coverage is incomplete. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
