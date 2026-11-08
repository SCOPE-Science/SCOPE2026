# Critical two-level spectra force square-root-dimensional overshoot in Frobenius-fitted matrix-sign iterations

## Finding

Consider the degree-one matrix-sign update \(X_1=X_0(I+\alpha R_0)\), with \(R_0=I-X_0^2\) and with the coefficient \(\alpha\ge 0\) chosen to minimize exactly the **squared Frobenius norm** of \(R_1=I-X_1^2\). For every positive-definite diagonal \(X_0\) with its spectrum strictly inside \((0,1)\), this nonnegative, unbounded coefficient minimization has a **unique** minimizer.

The one-step Frobenius benefit need not protect the spectral residual. Precisely, fix \(0<t<1\) and \(a>0\), put \(D=(1-t)t^2\), and for every sufficiently large integer \(n\) define
\[
r_{n}=1-\frac{a}{\sqrt n},\qquad R_{0,n}=\operatorname{diag}(r_n,\ldots,r_n,t)\in\mathbb R^{n\times n},\qquad X_{0,n}=(I-R_{0,n})^{1/2}.
\]
There are \(n-1\) copies of \(r_n\). Write \(\alpha_n\) for the unique optimal coefficient. Then
\[
\frac{\alpha_n}{n^{1/4}}\longrightarrow \sqrt{\frac{a}{a^2+D^2}},\qquad
\frac{\|R_{1,n}\|_2}{\sqrt n}\longrightarrow\frac{aD}{a^2+D^2},\qquad
\frac{\|R_{1,n}\|_F^2}{\|R_{0,n}\|_F^2}\longrightarrow\frac{D^2}{a^2+D^2}.
\]
In particular the asymptotic spectral-spike coefficient within this natural two-level critical scaling has the sharp maximum \(1/2\), attained **exactly when \(a=D\)**, whereas the corresponding squared Frobenius residual is halved. For the explicit choice \(t=1/2\), \(a=D=1/8\),
\[
\alpha_n\sim2n^{1/4},\quad \|R_{1,n}\|_2\sim\tfrac12\sqrt n,\quad
\frac{\|R_{1,n}\|_F^2}{\|R_{0,n}\|_F^2}\to\tfrac12,\quad
\|X_{1,n}-I\|_2\sim\frac{n^{1/4}}{\sqrt2}.
\]
The initial sign-approximation error \(\|X_{0,n}-I\|_2\) tends to \(1\), so even that **actual operator-norm error**, not merely the auxiliary residual, deteriorates without bound. Conversely, for every dimension and every positive-definite diagonal input with residual eigenvalues in \((0,1)\), the optimizer obeys \(\|R_1\|_2\le\sqrt n\,\|R_0\|_2\). Thus the exhibited \(\sqrt n\) order is optimal; the statement does not claim that \(1/2\) is a universal sharp prefactor outside the specified two-level critical family.

## Assumptions and scope

All matrices are real, diagonal and positive definite, and all computations are in exact arithmetic. The sign of every \(X_{0,n}\) is \(I\). The optimization is the *unbounded nonnegative* variant \(\alpha\in[0,\infty)\) of first-degree adaptive polynomial fitting. It is **not** the safeguarded procedure of Yang et al. (2026), which imposes \(\alpha\in[1/2,1]\), and it is **not** a result about its randomized sketch approximation. For general uniqueness, the residual eigenvalues lie strictly in \((0,1)\). For the two-level asymptotics \(n\) ranges over all sufficiently large integers, so \(0<r_n<1\). Constants \(a,t\) are fixed independently of \(n\).

## Proof

**Step 1 (the scalar error and its unique optimum).** For a residual eigenvalue \(r\in(0,1)\), the one-step residual eigenvalue is
\[
F_r(\alpha)=1-(1-r)(1+\alpha r)^2=r-b_r\alpha-c_r\alpha^2,
\qquad b_r=2r(1-r)>0,\quad c_r=r^2(1-r)>0.
\]
For eigenvalues \(r_1,\ldots,r_n\), the objective is \(M(\alpha)=\sum_iF_{r_i}(\alpha)^2\). Expanding gives a quartic \(M(\alpha)=\sum_{j=0}^4m_j\alpha^j\) with
\[
m_1=-2\sum_i r_i b_{r_i}<0,\quad m_3=2\sum_i b_{r_i}c_{r_i}>0,\quad m_4=\sum_i c_{r_i}^2>0.
\]
The coefficient \(m_2\) has no imposed sign. In descending order the coefficient signs of the cubic derivative \(M'(\alpha)\) are \((+,+,\operatorname{sgn}(m_2),-)\), which have exactly one sign change, including if \(m_2=0\). Descartes' rule therefore gives at most one positive root, counting multiplicities. Because \(M'(0)=m_1<0\) and \(M'(\alpha)\to+\infty\), there is exactly one; the coercive objective decreases before it and increases afterward. Hence the optimum over \(\alpha\ge0\) is unique and strictly positive.

**Step 2 (critical two-level scaling).** Put \(\alpha=n^{1/4}\beta\). With \(r_n=1-a/\sqrt n\), the two residual eigenvalues satisfy, locally uniformly for \(\beta\) in each compact subset of \([0,\infty)\),
\[
F_{r_n}(n^{1/4}\beta)\longrightarrow1-a\beta^2,\qquad
n^{-1/2}F_t(n^{1/4}\beta)\longrightarrow-D\beta^2.
\]
Therefore
\[
\frac{M_n(n^{1/4}\beta)}{n}\longrightarrow
Q(\beta)=(1-a\beta^2)^2+D^2\beta^4.
\]
The polynomial \(Q\) is a strictly convex quadratic in \(\beta^2\ge0\), with its unique minimizer at \(\beta_*^2=a/(a^2+D^2)\). The global minimizers \(\beta_n=\alpha_n/n^{1/4}\) are bounded: the trial \(\beta=\beta_*\) gives \(M_n(\alpha_n)=O(n)\), while the single \(t\)-eigenvalue has \(F_t(\alpha)=t-2t(1-t)\alpha-D\alpha^2\), whose magnitude grows quadratically for positive large \(\alpha\). Thus \(\alpha_n=O(n^{1/4})\). Every convergent subsequence of \(\beta_n\) minimizes \(Q\) by uniform convergence on compacts and comparison with fixed trial \(\beta\); uniqueness yields \(\beta_n\to\beta_*\).

**Step 3 (residual norms and sharp critical coefficient).** Substituting \(\beta_*\) into Step 2 gives
\[
F_{r_n}(\alpha_n)\to \frac{D^2}{a^2+D^2},\quad
\frac{F_t(\alpha_n)}{\sqrt n}\to-\frac{aD}{a^2+D^2},\quad
\frac{M_n(\alpha_n)}n\to\frac{D^2}{a^2+D^2}.
\]
Because \(M_n(0)/n\to1\) and the isolated eigenvalue dominates the new spectral norm, the first three displayed limits in the finding follow. Moreover \(2aD\le a^2+D^2\), with equality iff \(a=D\); hence the critical-family coefficient is at most and can equal \(1/2\).

**Step 4 (actual matrix-sign error and the universal order).** The exceptional updated matrix eigenvalue is
\[
\sqrt{1-t}\,(1+\alpha_nt)=t\sqrt{1-t}\,\beta_*n^{1/4}+o(n^{1/4}),
\]
while each of the other \(n-1\) updated eigenvalues tends to \(\sqrt a\,\beta_*\). Since \(\operatorname{sign}(X_{0,n})=I\), the operator-norm sign-approximation error grows as \(t\sqrt{1-t}\,\beta_*n^{1/4}\). The initial sign error tends to \(1\) due to the \(n-1\) vanishing entries. With \(t=1/2\), \(a=D=1/8\), one has \(\beta_*=2\), giving the stated coefficient \(1/\sqrt2\).

Finally, since the unbounded nonnegative fit admits \(\alpha=0\), its minimizer has \(\|R_1\|_F\le\|R_0\|_F\). For a real symmetric residual in dimension \(n\), norm comparison yields
\[
\|R_1\|_2\le\|R_1\|_F\le\|R_0\|_F\le\sqrt n\,\|R_0\|_2.
\]
The example attaining \((1/2+o(1))\sqrt n\) proves this order cannot be improved, without claiming the universal leading constant is optimal.

## Verification

Run `python3 verify.py` from a directory containing the embedded standalone script. It constructs the objective and derivative from spectral multiplicities, independently expands exact rational quartic coefficients for six sizes, checks the sign pattern of the derivative's coefficients, computes the unique positive minimizing root by bisection, and checks the predicted limiting rates through \(n=1024^4\) using multiplicities rather than allocating a dense matrix. A further four sets of constants check the general two-level formula. Numerical tests supplement, but are not a substitute for, Steps 1–4. They do not establish global iteration convergence, a universal optimal constant \(1/2\), or conclusions under finite precision or sketched fitting.

## Relationship to prior work

Yang, Wang, Balabanov, Erichson and Mahoney (2026), equations (2)–(3), use precisely the polynomial \(g_1(r;\alpha)=1+\alpha r\) and its Frobenius squared residual objective. Section 4.1 explicitly warns that without a coefficient interval the spectral residual may increase, and their theorem supplies the safeguard \([1/2,1]\). That warning **precedes and motivates** this result. The present proof adds the unique-positive-optimizer lemma, an explicit parameterized critical family, an exact asymptotic growth coefficient and an unbounded sign-error consequence. It does not treat the warning itself as original and does not disprove the safeguarded theorem.

Amsel, Persson, Musco and Gower (2025) optimize a *worst-case spectral* approximation over a prescribed interval instead of minimizing the empirical Frobenius residual. Grishina, Smirnov and Rakhuba (2025) likewise construct Chebyshev-optimized polynomials. Topollai and Choromanska (2026) estimate spectral moments to choose predesigned polynomial routines, rather than minimizing this unrestricted one-parameter Frobenius objective. Those formulations do not imply the exact two-scale asymptotic law. Familiar \(\ell_2\)-versus-\(\ell_\infty\) norm comparison proves the upper order alone, not that the specific globally optimal nonlinear fit attains it. No claim of exhaustive historical uniqueness is made.

## Limitations

This is a one-step diagonal, exact-fit result for an **unsafeguarded variant**; it must not be ascribed to the clipped or randomized versions of PRISM, and it does not establish failure of multi-step convergence. The singular values of the constructed inputs are in \((0,1)\), but they are not normalized to unit Frobenius norm. The universal spectral upper constant is not determined. The coefficient \(1/2\) is sharp only within the stated critical two-level family, and the indicated rates are limits rather than finite-\(n\) equalities. Independent mathematical evaluation and a complete historical-priority determination have not been performed.

## References

1. Shenghao Yang, Zhichao Wang, Oleg Balabanov, N. Benjamin Erichson, Michael W. Mahoney, *PRISM: Distribution-free Adaptive Computation of Matrix Functions for Accelerating Neural Network Training*, arXiv:2601.22137, first posted 2026-01-29. https://arxiv.org/html/2601.22137v1 (especially Section 4.1, Theorem 1 and Appendix B).
2. Noah Amsel, David Persson, Christopher Musco, Robert M. Gower, *The Polar Express: Optimal Matrix Sign Methods and Their Application to the Muon Algorithm*, arXiv:2505.16932, 2025. https://arxiv.org/html/2505.16932v1 (Sections 3–4).
3. Ekaterina Grishina, Matvey Smirnov, Maxim Rakhuba, *Accelerating Newton-Schulz Iteration for Orthogonalization via Chebyshev-type Polynomials*, arXiv:2506.10935, 2025. https://arxiv.org/html/2506.10935v1 (Section 3).
4. Kristi Topollai, Anna Choromanska, *Cost-free Spectral Estimation for Adaptive Newton-Schulz in Matrix Optimizers*, arXiv:2609.33047, first posted 2026-09-27. https://arxiv.org/html/2609.33047v1 (Sections 2, 4 and Appendix G).
