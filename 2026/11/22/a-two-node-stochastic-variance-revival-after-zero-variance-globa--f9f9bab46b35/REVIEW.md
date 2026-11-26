# Independent mathematical audit

## correctness

PASS

Identity-started scalar-coefficient global Lanczos uses the counting spectral measure. The inverse residual formula follows from the polynomial [1−q_m(x)²/q_m(0)²]/x and double vanishing at the Ritz nodes. For the base family, centering its eigenvalues at μ=3/2 gives sum of centered squares 7/8 and sum of centered cubes 9/32, so the monic two-node polynomial in y=x−μ is y²−(9/28)y−7/(8n), equal to the displayed q_2(x). The one-node residual on the rotated eigenpair 1 and 9/4 is 1/9 at both, giving a diagonal matrix in probe coordinates. Evaluating q_2 on the same eigenpair gives scalar residual difference Δ_n>0; the sole off-diagonal pair is therefore −Δ_n/2. Each probe's centered quadratic form is −Δ_n z_1z_2, and independent probes give exact variance Δ_n²/s. Summing scalar residuals gives the stated deficits and E_1−E_2=98n/[3(153n−49)]>0; exact Fraction evaluations at n=3,4,8,30 corroborate the symbolic computation, including Δ_3=35/15129. Trace is constant under the tridiagonal perturbation. Differentiating A^{-1}−4I/3+4A/9 gives the nonzero derivatives −2/15 at (2,3) for n=3 and −4/45 at (3,4) for n≥4. The variance is therefore positive of order t²/s at one node for small positive t, while it has a positive two-node limit. Weyl verifies κ<19/7 for 0<t<1/16. At most two spectral atoms imply exactness by two nodes or earlier breakdown, establishing dimension minimality. The exact zero is at the reducible base, not asserted for its irreducible perturbations.

## originality

PASS

The estimator, Hermite residual and sign-probe variance identity are prior work. The distinct result is a concrete one-to-two-node zero-to-positive reversal within that same estimator, with its exact law and an unbounded ratio on nearby uniformly well-conditioned irreducible tridiagonals. Known one-node comparisons to ordinary Hutchinson and two-node single-vector quadrature formulas do not establish this comparison.

## value

PASS

This is a dimension-minimal witness against using improving deterministic quadrature accuracy as a proxy for cross-depth Rademacher sampling accuracy. The effect does not require severe conditioning or disconnected sparsity: the irreducible fixed-dimension perturbations have arbitrarily large ratios with κ<3. The exact sign law makes this a concrete estimator diagnostic, not just a variance-bound comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
