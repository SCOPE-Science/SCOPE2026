# Universal critical relaxation for scalar epsilon-outside RMSProp

## Finding

Consider the epsilon-outside RMSProp algorithm for the strictly convex scalar quadratic \(L(x)=a x^2/2\), \(a>0\), with learning rate fixed at the stability boundary \(h=2\varepsilon/a\). The zero state is globally asymptotically stable for every \(\varepsilon>0\), every \(0<\beta<1\), and every initial \(x_0\in\mathbb R\), \(v_0\geq0\). More precisely, exactly one of the following occurs:

1. Some \(x_N=0\); then \(x_n=0\) for all \(n\geq N\), and \(v_n=\beta^{n-N}v_N\) for all \(n\geq N\).
2. Every \(x_n\ne0\); then the signs of \(x_n\) alternate from some iteration onward, and the exact critical asymptotics are
   \[
   \lim_{n\to\infty}n|x_n|=\frac{\varepsilon}{2a},
   \qquad
   \lim_{n\to\infty}n^2v_n=\frac{\varepsilon^2}{4}.
   \]

The rate constants do not depend on \(\beta\), and the memory constant does not depend on \(a\). No uniform finite-time onset of these asymptotics over arbitrary initial states is asserted.

## Assumptions and scope

Fix \(a>0\), \(\varepsilon>0\), \(0<\beta<1\), and set \(h=2\varepsilon/a\). For every initial pair \(x_0\in\mathbb R\), \(v_0\in[0,\infty)\), define the recursion for all \(n\geq0\) by
\[
v_{n+1}=\beta v_n+(1-\beta)a^2x_n^2,\qquad
x_{n+1}=x_n-\frac{ha x_n}{\sqrt{v_{n+1}}+\varepsilon}.
\]
The square root is the nonnegative one. This is the epsilon-**outside** algorithm: the denominator is \(\sqrt{v_{n+1}}+\varepsilon\), not \(\sqrt{v_{n+1}+\varepsilon}\). The update includes the newly accumulated memory. No stochastic gradients, momentum, or bias correction are included.

## Proof

Put \(q_n=|x_n|\) and \(s_n=\sqrt{v_{n+1}}/\varepsilon\). At the critical learning rate,
\[
x_{n+1}=x_n\frac{s_n-1}{s_n+1},
\qquad
q_{n+1}=q_n\frac{|s_n-1|}{s_n+1}.
\tag{1}
\]
For \(x_n\ne0\), the memory update gives \(v_{n+1}>(1-\beta)a^2x_n^2>0\); hence \(s_n>0\) and the factor in the second equation is strictly less than one. Thus \(q_n\) is nonincreasing and has a finite limit \(q_\infty\geq0\). Because the memory is a stable geometric average of the bounded sequence \(a^2q_n^2\), its recurrence implies \(v_n\to a^2q_\infty^2\). If \(q_\infty>0\), (1) would force
\[
\frac{q_{n+1}}{q_n}\longrightarrow
\frac{|a q_\infty-\varepsilon|}{a q_\infty+\varepsilon}<1,
\]
contradicting \(q_n\to q_\infty>0\). Therefore \(q_n\to0\) and \(v_n\to0\). Moreover \(q_n\leq q_0\) and
\[
0\leq v_n\leq\max\{v_0,a^2q_0^2\}
\]
for every \(n\), which establishes Lyapunov stability of the zero pair as well as global attraction.

If some \(x_N=0\), the asserted finite-hit alternative follows immediately from the recurrence. Suppose instead that \(x_n\ne0\) for all \(n\). Since \(v_n\to0\), eventually \(0<s_n<1\); the multiplier in (1) is then negative and the signs alternate. Also
\[
\frac{q_{n+1}}{q_n}=\frac{1-s_n}{1+s_n}\longrightarrow1.
\tag{2}
\]

The critical memory lemma is
\[
\frac{v_{n+1}}{a^2q_n^2}\longrightarrow1.
\tag{3}
\]
Here is a full justification despite the memory dependence. Fix \(\rho\) such that \(\sqrt{\beta}<\rho<1\). From (2), there is \(N\) such that \(q_{j+1}\geq\rho q_j\) whenever \(j\geq N\). Unrolling the memory update gives
\[
\frac{v_{n+1}}{a^2q_n^2}
=
\frac{\beta^{n+1}v_0}{a^2q_n^2}
+
(1-\beta)\sum_{k=0}^{n}\beta^k
\left(\frac{q_{n-k}}{q_n}\right)^2.
\tag{4}
\]
For \(0\leq k\leq n-N\), the summands are bounded by \((\beta/\rho^2)^k\), a summable geometric sequence, and each fixed-\(k\) ratio \(q_{n-k}/q_n\to1\). The initial-memory term and the finitely many old-history terms with \(n-k<N\) are \(O((\beta/\rho^2)^{n-N})\), since \(q_n\geq q_N\rho^{n-N}\). Dominated convergence in (4) therefore gives \((1-\beta)\sum_{k=0}^\infty\beta^k=1\), proving (3).

Equation (3) implies \(s_n/q_n\to a/\varepsilon\). For all sufficiently large \(n\), (1) yields the exact reciprocal increment
\[
\frac1{q_{n+1}}-\frac1{q_n}
=\frac{2s_n}{q_n(1-s_n)}
\longrightarrow\frac{2a}{\varepsilon}.
\tag{5}
\]
Cesàro averaging of (5) gives \((nq_n)^{-1}\to2a/\varepsilon\), or \(nq_n\to\varepsilon/(2a)\). Finally, (3) with index \(n-1\) shows \(v_n\sim a^2q_{n-1}^2\), so \(n^2v_n\to\varepsilon^2/4\). This proves every asserted limit and the dichotomy.

## Verification

A self-contained Python program, `checks/verify.py`, checks the exact rational critical-update identity for 36 parameter combinations, constructs an exact finite-hit initialization, and tests five independent parameter regimes. Each numerical regime runs 750,000 updates, checks nonincreasing amplitude and eventual sign alternation, and compares its scaled amplitude and memory with the theorem's constants. The run reported `VERIFY_OK finite_checks_only_analytic_proof_required`. The analytic argument above, not these finite tests, proves the all-parameter statement.

## Relationship to prior work

Loh, Mireles-James, Xu and Tao (arXiv:2610.30078v1, submitted October 21, 2026) prove global stability **strictly below** \(2\varepsilon/\lambda_{\max}(A)\), Lyapunov instability above it, and global trapping for learning rates at or above it. Their Theorems 4.4, 4.8 and 4.13, together with Sections 5 and 8 and the inspected appendices, do not imply attraction or a sharp decay rate *at equality*. For the one-dimensional quadratic, the present result fills that boundary case and supplies the universal \(n^{-1}\) and \(n^{-2}\) constants.

Dimitrieski, Honecker, Scherer and Ebenbauer (arXiv:2603.15823) establish global stability under strictly smaller steps and robustness to bounded perturbations, but their main stability hypothesis also excludes equality. Dereich, Jentzen and Riekert (arXiv:2504.19426), in Proposition 2.7, prove RMSProp convergence for steps strictly below the threshold. Their exponential-rate estimates assume an interior spectral contraction and do not supply this marginal-rate result. Database searches of related adaptive-optimizer dynamics did not reveal an equivalent scalar RMSProp equality theorem. The priority assessment remains provisional.

## Limitations

The theorem concerns only the scalar positive quadratic and epsilon-outside RMSProp with a constant critical learning rate; neither general non-diagonal multivariate dynamics nor nonquadratic losses are resolved. Finite-hit trajectories are excluded from the polynomial-asymptotic alternative, because they converge in finite time. The asymptotic onset may be arbitrarily late. No claim of independent proof review, comprehensive historical priority, or empirical training performance is made.

## References

1. K. Loh, J. Mireles-James, Z. Xu and M. Tao, *The Dynamics of RMSProp Beyond the Stability Threshold*, arXiv:2610.30078v1 (first public October 21, 2026), https://arxiv.org/abs/2610.30078.
2. N. Dimitrieski, M. C. Honecker, C. Scherer and C. Ebenbauer, *Global Stability and Step Size Robustness of RMSProp*, arXiv:2603.15823 (first public March 16, 2026), https://arxiv.org/abs/2603.15823.
3. S. Dereich, A. Jentzen and A. Riekert, *Sharp higher order convergence rates for the Adam optimizer*, arXiv:2504.19426 (first public April 28, 2025), https://arxiv.org/abs/2504.19426.
