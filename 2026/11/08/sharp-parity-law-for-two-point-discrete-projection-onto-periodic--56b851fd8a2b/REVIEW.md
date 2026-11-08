# Scientific review

## Correctness — PASS

The normal matrix is the sum of the two symmetric two-site sampling Gram matrices. The cyclic Green function is verified by a bilateral second-order recurrence and periodization, not inferred from finite tests. It yields two signed geometric sample-coefficient rows whose exact absolute sum proves the all-parameter norm. Adjacent knot rows have opposing nonzero signs on a shared observation, proving strict exclusion of interior evaluation points. Constant reproduction gives the positivity defect. Parity, strict monotonicity, the midpoint boundary, and Gauss specialization follow by exact algebra. The attached standard-library checker independently forms and inverts 33 rational Gram matrices for \(3\le N\le13\), and checks the degenerate endpoint rules; its finite scope is stated openly.

## Originality — PASS, with residual priority risk

Grigorieff and Sloan (1998), *Stability of discrete orthogonal projections for continuous splines*, DOI 10.1017/S0004972700032263, is the closest paper. Its general interval-based \(L^p\)-stability theory for quadrature-defined projections gives no sharp periodic two-site coefficient formula, no exact Gauss constant, and no odd/even midpoint law. Crouzeix and Thomée (1987), DOI 10.1090/S0025-5718-1987-0878688-2, treats the continuous-measure \(L^2\) projector, not this discrete observation operator. Separately established continuous-measure periodic linear-spline constants do not imply the discrete constants: even Gauss quadrature reproduces the continuous mass matrix while changing the data functional. No covering result was located in targeted mathematical literature and published-results searches. The closest historical source is fully available, but equivalent older or unindexed formulas cannot be excluded categorically. The present claim does not assert novelty of tridiagonal inverses, spline-projection boundedness, or the positivity-defect identity in abstract form.

## Mathematical value — PASS

Exact uniform-norm stability constants are natural quantitative invariants of discrete least-squares spline approximation. The result classifies the entire symmetric two-point quadrature family and displays a sharp parity-dependent singular limit as the sites coalesce. The Gauss rule yields the dimension-free constant \(\sqrt3\), while arbitrary close midpoint pairs can produce unbounded amplification on even cycles. The conclusion also determines all norming evaluation points and sharp positivity loss. This is a genuine parameter-family stability classification, rather than a small numerical improvement or an arbitrarily chosen finite computation.

## Limitations and interpretation

The hypotheses are real, periodic, uniform-mesh, equal-weight, degree-one, and two-sample-per-cell; no result for nonuniform meshes or other quadrature rules is asserted. The dated online appearance of the 1998 journal article is 17 April 2009; its original print dissemination day is unknown. Independent mathematical audit has not been performed, and priority risk remains for formulas not indexed in the inspected sources.

Self-review: passed. Independent audit: not yet performed.
