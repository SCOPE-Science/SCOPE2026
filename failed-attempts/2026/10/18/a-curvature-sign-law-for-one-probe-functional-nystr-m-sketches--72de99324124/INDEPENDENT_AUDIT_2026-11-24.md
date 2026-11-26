# Independent mathematical audit

## correctness

PASS

The single nonzero sketch eigenvalue is the ratio of the squared norm of B^q g to the positive scalar g^T B^(2q−1)g. In the diagonal basis put p=2q−1 and w_i equal to squared probe coordinates. If no positive eigenvalue is active, both approximants are zero. Otherwise each trace is determined by a weighted Lehmer mean, f(Σw_i a_i^(p+1)/Σw_i a_i^p) versus Σw_i f(a_i)^(p+1)/Σw_i f(a_i)^p. Tilting the second weight law by (a_i/f(a_i))^p yields the first. Its covariance with f(a_i) is nonnegative in the concave case and nonpositive in the convex case because f(t)/t is respectively decreasing or increasing in the weak sense. Jensen gives the other step with the same inequality direction, strictly for strict curvature and nonconstant active spectrum. One active value gives equality, as does positive linear f. Each rank-one captured trace is at most f(max a_i) and nonnegative. For the Gaussian examples the direct deficit on diag(1,s) is s(1+u²)/(u²+s) with u standard Cauchy; cancellation against the density integrates to √s exactly. The function-after trace uses the eigenvalue λ=(u²+ε²)/(u²+ε). For 0<ε<1, substituting u=√ε v in E(1−λ^α) leaves a factor √ε and a dominated integrand, bounded on compact sets with a uniform O(v^(−2)) tail. For α=1/2 the limiting integral before the Cauchy factor 2/π is ∫₀∞(1−v/√(1+v²))dv=1. For α=2 it is ∫₀∞(2/(1+v²)−1/(1+v²)²)dv=3π/4. Adding the ε^α term yields the stated constants and divergent ratios. This does not assert an ordering of the matrices themselves.

## originality

FAIL

The deterministic core is a routine scalar specialization of an existing more general comparison theorem for nonsymmetric generalized Bajraktarević means. The comparison identifies Eq. (14) and discharges both of its hypotheses by direct substitution and the elementary supporting-line/ratio properties of curvature. Extending to the stated continuous case is by smoothing and taking the trace limits. The examples do not leave an independent novel core: exact direct deficits and the first two residual moments are covered by the rank-two specialization of the indexed half-moment law, which also gives the square function-after asymptotic by a polynomial identity. The square-root function-after example is independently covered by homogeneity and the indexed Gaussian crossover. These are coverage judgments, not date-based claims about conception priority.

## value

FAIL

The algorithm-order question is well motivated, and the statements are useful as exposition. But the one-column comparison is a routine specialization once the rank-one eigenvalue is written as a weighted scalar mean. The quantitative witnesses do not supply a separate unknown exact invariant: the normalization, substitutions and first two known residual moments already give all their differing rates and constants. With no result for higher rank or an independent nontrivial regime in the frozen claim, there is no genuinely surviving contribution to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
