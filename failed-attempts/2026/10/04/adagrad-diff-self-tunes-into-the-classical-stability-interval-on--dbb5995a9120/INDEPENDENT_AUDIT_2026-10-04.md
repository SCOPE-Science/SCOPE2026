# Independent mathematical audit

## correctness

PASS

On a diagonal quadratic the algorithm decouples into scalar recurrences \(x_i^{n+1}=(1-\eta\lambda_i/w_i^n)x_i^n\). The source Proposition 3.4 makes the cumulative gradient-difference square sum finite, so \(w_i^n\) has a finite limit. Source Theorem 2.5 gives convergence to the unique minimizer in finite dimension. If an active coordinate had \(w_i^\infty\le\eta\lambda_i/2\), monotonicity of \(w_i^n\) would make every multiplier have magnitude at least one, contradicting convergence. The limiting ratio and eventual Q-linear conclusion then follow directly, with finite exact hits handled separately.

## originality

FAIL

The final claim is mechanically implied by the source paper itself. Theorem 2.5 already gives convergence of the AdaGrad-Diff iterates in the smooth convex setting, and Proposition 3.4 already gives summability of successive gradient differences. On a separable quadratic, substituting the diagonal gradient into Algorithm 1 yields the displayed scalar multiplier immediately; the strict stability bound is then a one-line contradiction from convergence and monotone weights, and the asymptotic linear ratio is a direct limit. Under the rule that unstated corollaries and special cases count as covered, this is not an original theorem.

## value

FAIL

The stability-interval interpretation is intuitive and potentially pedagogically useful, but after the source theorems are accounted for the mathematics is only a scalar substitution, monotonicity observation, and limit. That is a routine corollary rather than a separately motivated mathematical gap under the stated value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
