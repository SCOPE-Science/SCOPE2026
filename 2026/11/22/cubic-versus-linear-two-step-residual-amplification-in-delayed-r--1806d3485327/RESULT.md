# Cubic-versus-linear two-step residual amplification in delayed-residual linear solvers

## Finding

**Theorem.** Let \(K>1\) and let \(A=\operatorname{diag}(\sqrt K,1)\), so that the spectral condition number of \(A^{\mathsf T}A\) is \(K\). Consider the consistent system \(Ax=b\), start with \(x_0=0\), and choose any nonzero two-component right-hand side \(b\). Set \(r_j=b-Ax_j\), take the common initial residual-based surrogate-hyperplane step
\[
\alpha_0=\frac{\|r_0\|_2^2}{\|A^{\mathsf T}r_0\|_2^2},
\qquad x_1=x_0+\alpha_0 A^{\mathsf T}r_0,
\]
and then take exactly one further step using either the **delayed-residual** rule \(\alpha_1^{\mathrm{DR}}=\alpha_0\), or the **residual-difference** rule
\[
\alpha_1^{\mathrm{RD}}=\frac{\|r_1-r_0\|_2^2}{\|A^{\mathsf T}(r_1-r_0)\|_2^2}.
\]
Let \(M_{\mathrm{DR}}(K)\) and \(M_{\mathrm{RD}}(K)\) denote the supremum, over initial residuals with both components nonzero, of the ratio \(\|r_2\|_2/\|r_0\|_2\) under the respective rules. Then both suprema are attained, and
\[
\boxed{\lim_{K\to\infty}\frac{M_{\mathrm{DR}}(K)}{K^{3/2}}=\frac{3\sqrt3}{16},\qquad
\lim_{K\to\infty}\frac{M_{\mathrm{RD}}(K)}{K^{1/2}}=\frac12.}
\]
If \(t=|(r_0)_1|^2/|(r_0)_2|^2\) is the initial high-to-low squared residual ratio, every maximizing choice has \(Kt\to1/3\) for the delayed-residual rule, whereas \(K^3t\to1\) for the residual-difference rule. Thus the two rules have asymptotically different worst-startup scales even on the same two-dimensional, consistent, positive diagonal system.

## Assumptions and scope

All quantities are real and all arithmetic is exact. The matrix is diagonal, positive definite, and \(2\times2\), with \(K>1\). Both initial residual components are nonzero. For each fixed \(K\), both step rules use the same source-specified first step. The comparison concerns the Euclidean *physical residual* after precisely two updates; it does not assert a difference in eventual convergence rates or in the objective function's monotonicity. The condition number of \(A\) itself is \(\sqrt K\), so the blow-up exponents relative to \(\kappa_2(A)\) are three and one respectively.

## Proof

By homogeneity and symmetry of signs, write \(r_0=(\sqrt t,1)^{\mathsf T}/\sqrt{1+t}\), where \(t>0\). Set \(B=AA^{\mathsf T}=\operatorname{diag}(K,1)\). Since \(r_{j+1}=(I-\alpha_jB)r_j\), the common first step is
\[
\alpha_0=\frac{1+t}{1+Kt},\qquad
1-K\alpha_0=-\frac{K-1}{1+Kt},\qquad
1-\alpha_0=\frac{(K-1)t}{1+Kt}.
\]
The delayed rule repeats \(\alpha_0\) once, while \(r_1-r_0=-\alpha_0Br_0\) makes the residual-difference rule equal to
\[
\alpha_1^{\mathrm{RD}}=\frac{1+K^2t}{1+K^3t}.
\]
A second componentwise multiplication gives the following *exact* squared amplification functions, with no limiting approximation:
\[
D_K(t):=\frac{\|r_2^{\mathrm{DR}}\|_2^2}{\|r_0\|_2^2}
=\frac{(K-1)^4(t+t^4)}{(1+t)(1+Kt)^4},
\]
\[
R_K(t):=\frac{\|r_2^{\mathrm{RD}}\|_2^2}{\|r_0\|_2^2}
=\frac{(K-1)^4(t+K^4t^4)}{(1+t)(1+Kt)^2(1+K^3t)^2}.
\]
Both functions are strictly positive, continuous, and tend to zero as \(t\downarrow0\) or \(t\to\infty\); hence each has a positive interior maximum.

For the delayed rule substitute \(y=Kt\). The polynomial identity \((1+t^3)/(1+t)=1-t+t^2\) gives
\[
\frac{D_K(t)}{K^3}
=\left(1-\frac1K\right)^4
\frac{y(1-y/K+y^2/K^2)}{(1+y)^4}.
\]
For fixed \(y\ge0\), the expression tends to \(f(y)=y/(1+y)^4\). Uniform control of maximizing sequences follows from \(1-y/K+y^2/K^2\le(1+y)^2\) for \(K\ge1\): the normalized expression is at most \(y/(1+y)^2\), tending to zero uniformly at both tails. On compact \(y\)-intervals the convergence is uniform. Differentiation gives \(f'(y)=(1-3y)/(1+y)^5\), so the unique maximizer is \(y=1/3\), and its value is \(27/256\). Therefore \(\max_t D_K(t)/K^3\to27/256\), and every maximizing \(Kt\) tends to \(1/3\).

For the residual-difference rule substitute \(z=K^3t\). Then
\[
\frac{R_K(t)}K=\left(1-\frac1K\right)^4
\frac{z+z^4/K^5}{(1+z/K^3)(1+z/K^2)^2(1+z)^2}.
\]
Separate the two numerator terms. The first is at most \(z/(1+z)^2\le1/4\). For the second, its contribution before the prefactor is bounded by \(1/K\) uniformly in \(z>0\): for \(z\le K^2\) use \((1+z)^2\ge z^2\); for \(K^2\le z\le K^3\) additionally use \((1+z/K^2)^2\ge z^2/K^4\); for \(z\ge K^3\) also use \(1+z/K^3\ge z/K^3\). The three bounds are respectively \(z^2/K^5\), \(1/K\), and \(K^2/z\), each at most \(1/K\) in its range. Thus the limsup of the normalized maximum is at most \(1/4\). Taking \(z=1\) gives a matching lower limit of \(1/4\). Since the leading bound \(z/(1+z)^2\) has its unique maximum at \(z=1\), the same inequalities and compactness prove every maximizing \(z\to1\). Taking square roots establishes the theorem.

## Verification

The included standard-library Python checker `verification/check_two_step.py` independently forms the two componentwise updates using exact rational arithmetic, evaluates both derived rational formulas and both rescaled identities, and tests the global upper bound used for the residual-difference asymptotic. It passed 4,424 exact-rational assertions on nondegenerate test points and six floating-point checks of two explicit near-maximizers. These are corroborating finite checks only. The theorem for all real \(K>1\) and the limits rest on the displayed algebraic and uniform-tail arguments, not enumeration or simulation.

Reproduce with `python verification/check_two_step.py` from the extracted package directory; output: `VERIFY_OK 4430`.

## Relationship to prior work

Xin Xu's *Two-point residual step size gradient methods for linear systems* (2026, arXiv:2611.02743v1) defines both update rules, their common initial surrogate-hyperplane step, and proves a step-size ordering and a finite-window contraction analysis in the two-mode setting. The source reports nonmonotone residual spikes numerically. Equations (8), (14), (16), and (17) there supply the algorithmic starting point, not the two sharp startup amplification laws or their distinct maximizing initial-residual scales.

The classical Barzilai–Borwein literature and more recent sharp asymptotic analyses address long-run rates, monotonicity or spectral bounds for related gradient steps. A published sharp safety-frontier result for repeated Cauchy steps addresses a related two-step long-step component, but the present distinction is the quantitative **joint** worst-case residual comparison of the source's DR and RD rules under the same prescribed initialization; this is not inferred from a safety threshold or from the simple ordering of the stepsizes. The originality judgment remains conditional on accessible literature and is not an independent priority certificate.

## Limitations

The conclusions are exact-arithmetic, two-step, worst-initialization statements for one two-eigenvalue family. No conclusion is drawn about typical starts, higher-dimensional spectra, time to convergence, noisy right-hand sides, safeguarded or damped steps, or floating-point overflow. Theorems for other algorithms that share the same algebraic first step may overlap the delayed-residual half; the proposed contribution depends on the combined, sharp DR/RD rate separation and initial-data scale classification. Independent validation has not been performed.

## References

1. Xin Xu, *Two-point residual step size gradient methods for linear systems*, arXiv:2611.02743v1, first public release 2026-11-02, https://arxiv.org/abs/2611.02743.
2. Shutai Yang and Ya-Xiang Yuan, *The Sharp Worst-Case Asymptotic Rate of the Barzilai–Borwein Method in \(\mathbb R^d\) and Hilbert Spaces*, arXiv:2608.07839, https://arxiv.org/abs/2608.07839.
3. *Barzilai–Borwein Fails Superlinear Convergence on an Open Set of Quadratics for Every Dimension n at least 4*, arXiv:2607.21579, https://arxiv.org/abs/2607.21579.
4. Y.-K. Huang, Y.-H. Dai and X.-W. Liu, *Equipping the Barzilai–Borwein Method with the Two Dimensional Quadratic Termination Property*, SIAM J. Optim., doi:10.1137/21M1390785.
