# Independent mathematical audit

## correctness

PASS

The final repaired core is the explicit positive lower bound for the log-curvature ratio and the exact zero value for the specified relaxing profile. Factoring the slow exponential makes K_j=log(1+(1−q)^2 z/(1+qz)^2) at z=sq^j; this is strictly positive. In u=log z, write log K=F(U(u)) with F(v)=log log(1+exp(v)) and U(u)=2log(1−q)+u−2log(1+q exp(u)). Direct differentiation gives F′>1/(1+exp(v)), F″<0, and −U″=2qz/(1+qz)^2, so the chain rule yields −(log K)″>2qz/[(1+z)(1+q²z)]. The exact central second-difference integral with triangular kernel has total weight (log q)^2. The minimum of the rational factor is at an endpoint since its derivative has sign 1−q²z². This verifies universality and strictness. For the comparison, K_j=β exp(−κ(t_0+jh))(1−exp(−κh))², which is geometric. Independently recalculated the illustrative curvatures log(10/9), log(27/25), log(85/81); the gap is approximately 0.15380809 and the lower bound 0.09043821. The explicit four-point witness is valid: the initial value, first log decrement and first two curvatures determine the first four logs, and a>0 follows from k_0²/(k_0−k_1)<250/567<log(8/3). For the contextual sample-count claim, verified both rank and the two-node quadrature proof in the repaired RESULT.md: positive mass at infinitely many nodes in (0,exp(−ah)] gives positive definite Hankel order three; a quadratic orthogonal to 1 and x has two distinct interior zeros by the sign-change argument. Division with remainder gives exactness through degree three, and integrating squared Lagrange basis polynomials proves positive weights. The nodes convert to distinct positive decay rates; weights can be rescaled back from t_0. This replay is analytic; the supplied numerical script was inspected, not executed. No noise tolerance, unequal-spacing guarantee or extension to other mechanisms is claimed.

## originality

PASS

The original package counted the positive four-point alias among its new mathematical contributions. That claim to novelty does not survive: two-node Gauss quadrature gives a stronger overlap theorem by a direct moment reduction. The specific numerical witness can remain an illustration, not a second research contribution. The corrected Finding, SLOGAN, REVIEW and AUDIT files in /workspace/repairs/3/ retain only the explicit strict quantitative lower bound as the contribution. No inspected exact, equivalent or stronger result supplies that margin; the pass applies to the repaired claim only.

## value

PASS

For two motivated but easily confounded scalar loss profiles, the revised finding gives an explicit scale-free separation margin rather than merely certifying distinguishability by rank. Its dependence on observation spacing, rate contrast and mixture balance exposes when exact separation can be weak. Standard four-point overlap is context, not this value judgment. The result is a useful theoretical diagnostic for exact data and does not claim a uniform positive or field-calibrated noise margin.

The dated certificate retains the supplied scientific assessment, sources and limitations.
