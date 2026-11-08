# Scientific review

## Correctness

**PASS.** All integers \(n\ge3\), \(m\ge2\), and positive block-size selections (with repetitions) are covered, including impossible total sizes where the factorial moment is zero. The rooted-block decomposition and formal Lagrange inversion yield the exact mixed falling-factorial moment \(M_{m,s}\). An independent algebraic ratio comparison shows that the additional marked-block moment is at most \(\kappa_n\mu_b\) times its predecessor: first monotonicity in \(a=n-s\), then in \(c=n-m\), then in the target size \(b\). The denominator factors remain positive in the admissible range; the equality cases for two marked blocks are explicitly checked. Finite enumeration through eight positions, plus exact parameter checks through size 99, is consistent with the symbolic proof. The checks neither imply nor replace the analytic all-order argument.

## Originality

**PASS, with residual priority risk.** Kargin (2019, arXiv:1907.00632, Theorem 2.2 and equations (3)–(4)) provides exact one-/two-size enumerators and marginal Gaussian asymptotics; those enumerators imply the relevant low-order moments. Kortchemski–Marzouk (2015, arXiv:1503.09174) treat much broader block weighting and tree bijections, allowing joint moments in principle. Gatea–Huang (2026, arXiv:2610.34775) treat factorial moments for restricted noncrossing families. The material inspected does not state the universal *all-order, quantitative, finite-size* multiplicative repulsion bound with best uniform one-step constant and equality classification. The proof needs a new global monotonicity argument across marked-block size and number. The source generating functions provide the inputs, not a cited inequality, but an earlier implicit or general conditional-composition inequality could subsume this comparison. The claim is limited to the inequality and equality statement, not to the known generating functions or negative asymptotic covariance.

## Value

**PASS.** Distributional joint-count control of block sizes matters for Catalan random structures: an exact, uniform product upper bound for any number of prescribed block-size occurrences is stronger than pairwise asymptotic covariance and directly bounds higher factorial moments. The explicit strictly subunit constant is best possible for all size pairs, yields strict finite-size negative covariance between distinct counts, and sub-Poisson variance for each count. This is not a routine restatement of Kargin's asymptotic Gaussian limit, nor does it claim broader negative association. The finite-size optimality and arbitrary factorial order make the statement a meaningful structural dependence law.

## Closest evidence and limits

The three full-text scientific sources were inspected at the generating-function and moment theorem/proposition sections. The nearest broad enumerators are acknowledged; historical priority beyond the inspected results remains uncertain. Independent mathematical audit is not performed.

Self-review: passed. Independent audit: not yet performed.
