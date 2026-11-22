# Sharp universal coefficient frontier for adaptive quintic matrix-sign and polar iterations

## Finding

Let \(a_*\) denote the unique root in \((29/20,3/2)\) of
\[
P(a)=128a^3+496a^2-1026a+27=0,
\qquad a_*=1.47222926097203\ldots.
\]
Consider the adaptive quintic Newton–Schulz map
\[
X_{k+1}=X_k\left(I+\tfrac12R_k+\alpha_kR_k^2\right).
\]
For square matrix-sign computation use \(R_k=I-X_k^2\). For rectangular polar-factor computation use \(R_k=I-X_k^\top X_k\). **Sharp coefficient-cap theorem:** For every fixed \(U<a_*\) with \(U\ge0\), every sequence of coefficients \(0\le\alpha_k\le U\), including history-dependent choices, converges to the correct matrix sign/polar factor from every qualifying input described below; the residual spectral norm decreases strictly at every nonzero residual. No universal assertion of this kind is possible for any cap \(U\ge a_*\): already a scalar initial value and the constant coefficient \(a_*\) converge in one update to a *wrong nonunit fixed point*. For each constant \(a>a_*\), a scalar positive input produces unbounded iterates.

This specifies the exact boundary for **all coefficient selections within a fixed interval**, not an assertion that a particular optimization/sketching routine fails beyond the boundary. In the motivating work the recommended empirical fifth-degree interval ends at \(29/20=1.45\); the exact endpoint is strictly larger, but the main result is its sharpness, including the failure mechanism.

## Assumptions and scope

All statements concern exact real arithmetic and the polynomial update shown above. In the square case, \(A\in\mathbb R^{n\times n}\) is invertible, \(A^2\) is symmetric positive definite, and all eigenvalues of \(A^2\) lie in \((0,1]\); put \(X_0=A\). Its matrix sign is \(A(A^2)^{-1/2}\). In the rectangular case, \(A\in\mathbb R^{m\times n}\), \(m\ge n\), has full column rank and singular values in \((0,1]\); put \(X_0=A\). Its polar factor is \(A(A^\top A)^{-1/2}\). Every coefficient \(\alpha_k\) is a single nonnegative real scalar, shared among all modes at iteration \(k\), with no further stochastic or computational assumptions. The theorem does not concern rank-deficient inputs or floating-point rounding.

## Proof

**Step 1: exact residual dynamics.** Since all updates are polynomials in the current symmetric Gram residual (or the symmetric square residual), they commute with it. On any eigenmode define \(r=1-x^2\), with \(x>0\) for the corresponding singular-value mode. The next residual is
\[
F_a(r)=1-(1-r)(1+r/2+ar^2)^2.
\]
This formula applies to each initial mode \(r\in[0,1)\). Two exact algebraic identities are
\[
F_a(r)-r=\frac{r(r-1)(2ar+1)(2ar^2+r+4)}4,
\]
\[
\frac{\partial F_a}{\partial r}
=\frac{r(10ar-8a+3)(2ar^2+r+2)}4.
\]
For every \(a\ge0\), \(0<r<1\) implies \(F_a(r)<r\). For \(a\le3/8\), the positivity of the Taylor coefficients in \((1-r)^{-1/2}\) gives \(1+r/2+ar^2\le(1-r)^{-1/2}\), hence \(F_a(r)\ge0\).

**Step 2: exact lower frontier and critical coefficient.** For \(a>3/8\), \(F_a\) on \([0,1]\) has exactly one interior minimum, at
\[
r_*(a)=\frac{8a-3}{10a}.
\]
Direct substitution yields the critical factorization
\[
F_a(r_*(a))+\frac1{2a}
=-\frac{(4a+1)^2P(a)}{25000a^3}.
\]
The cubic \(P\) is strictly convex for positive \(a\), negative at \(29/20\), positive at \(3/2\), and increasing throughout \([29/20,\infty)\). Thus \(a_*\) is the unique root above \(3/8\), and
\[
F_{a_*}(r_*(a_*))=-z_*,\qquad z_*:=\frac1{2a_*}<1.
\]
Because \(\partial_aF_a(r)=-2(1-r)r^2(1+r/2+ar^2)<0\) on \(0<r<1\), for every \(0\le a<a_*\) and \(r\in(0,1)\), \(F_a(r)>-z_*\). In particular every admissible first step enters \((-z_*,1)\).

**Step 3: strict contraction throughout the invariant interval.** First, for \(r\in(0,1)\) and \(0\le a\le a_*<3/2\), monotonicity in \(a\) gives \(F_a(r)+r\ge F_{3/2}(r)+r\). An exact positive Bernstein-form identity is
\[
F_{3/2}(r)+r=\frac r4\left(4(1-r)^4+7r(1-r)^3+4r^2(1-r)^2+8r^4\right)>0.
\]
Combined with Step 1, this proves \(|F_a(r)|<r\) for \(0<r<1\). Next write \(r=-t\), \(0<t\le z_*\). Since \(at<1/2\) when \(a\le U<a_*\), the multiplier \(g=1-t/2+at^2\) obeys \(0<g<1\). Consequently \(F_a(-t)=1-(1+t)g^2>-t\). Also \(F_a(-t)\le F_0(-t)=t^2(3-t)/4<t\) because \(0<t\le z_*<1\). Thus \(|F_a(-t)|<t\). Together the interval \((-z_*,1)\) is invariant, and every nonzero scalar residual contracts in absolute value.

For any fixed initial \(r_0<1\) and cap \(U<a_*\), \(|F_a(r)/r|\), continued as zero at \(r=0\), is jointly continuous and strictly below one on the compact set \([-z_*,r_0]\times[0,U]\); at the negative endpoint strictness uses \(U<a_*\). Therefore some uniform \(q<1\) satisfies \(|r_{k+1}|\le q|r_k|\) along every permissible adaptive sequence. Each finite collection of matrix modes converges to residual zero, and their positive multipliers preserve the initial polar/sign branches. It follows that the matrices converge to the stated sign or polar factor. Taking a maximum of finitely many strictly contracting mode residuals proves strict spectral-norm decrease whenever the residual is nonzero.

**Step 4: sharpness, nonunit trapping and divergence.** At \(a=a_*\), choose the positive scalar starting value \(x_0=\sqrt{1-r_*(a_*)}\). Step 2 gives \(r_1=-z_*\), so \(x_1=\sqrt{1+z_*}\ne1\). But for \(r=-z_*\),
\[
1+r/2+a_*r^2=1-z_*/2+a_*z_*^2=1,
\]
so \(x_1\) is an exact nonunit fixed point, invalidating every proposed universal cap \(U\ge a_*\) under arbitrary admissible coefficient sequences. For any fixed \(a>a_*\), the same construction with \(r_0=r_*(a)\) has \(r_1<-1/(2a)\) by the factorization in Step 2 and \(P(a)>0\). Writing \(r_k=-t_k\), then \(t_k>1/(2a)\) and
\[
t_{k+1}=(1+t_k)(1-t_k/2+at_k^2)^2-1>t_k.
\]
There is no finite limiting value above \(1/(2a)\), because the multiplier is strictly greater than one there. Hence \(t_k\to\infty\) and \(x_k\to\infty\). The exact rational choice \(a=3/2\), \(r_0=3/5\) gives \(r_1=-1107/3125<-1/3\).

## Verification

The embedded standalone `verify.py` uses SymPy exact symbolic algebra to confirm the polynomial factorization, derivative, minimizer substitution, threshold polynomial, Bernstein identity, rational endpoint signs and the \(a=3/2\) counterexample. It also checks rational residual grids and numerical changing-coefficient three-mode iterates. Run `python verify.py` with SymPy installed; the tested delivered source produced `VERIFY_OK` with 1651 assertions. The analytic proof above, not the finite test grid, establishes the universal quantifiers.

## Relationship to prior work

Yang, Wang, Balabanov, Erichson and Mahoney, *PRISM: Distribution-free Adaptive Computation of Matrix Functions for Accelerating Neural Network Training* (arXiv:2601.22137v1, January 29, 2026), introduce the adaptive polynomial and state a proved coefficient range for the lower-degree variant. Their Section 4.1 and Appendix A.1 recommend \([3/8,29/20]\) empirically for the degree-five version; their Appendix B analyzes the first-degree residual map rather than the exact sharp cap proved here. Amsel, Persson, Musco and Gower, *The Polar Express* (arXiv:2505.16932, first released May 22, 2025), study minimax-designed degree-five sign/polar updates over tracked spectral intervals, a distinct polynomial family/criterion, without the stated fixed-family scalar cap. Classical Padé/Newton–Schulz polynomial iteration and polar/sign functional calculus are prior tools. Related 2026 work on spectral-moment adaptive Newton–Schulz likewise motivates tuning but has not been established to contain this exact scalar cap. No claim is made that an absence of a found duplicate establishes absolute historical uniqueness.

## Limitations

The guarantee is uniform over **all** possible coefficients in an interval, which is stronger than a claim for the minimizer of a particular fitting loss; the wrong-fixed-point counterexample need not be chosen by that minimizer. The theorem concerns exact algebra, initially normalized full-rank matrices, nonnegative coefficients, and infinite iterations. It supplies neither finite-precision backward stability nor a bound on training performance. Although \(a_*\) exceeds the original empirical cap \(29/20\) by only about 1.53 percent, the mathematical content is the exact safety/failure boundary, the arbitrary-adaptation guarantee and its trapping/divergence mechanism. Historical equivalence with unindexed earlier matrix-sign results remains possible.

## References

1. Shenghao Yang, Zhichao Wang, Oleg Balabanov, N. Benjamin Erichson, Michael W. Mahoney, *PRISM: Distribution-free Adaptive Computation of Matrix Functions for Accelerating Neural Network Training*, arXiv:2601.22137v1 (2026-01-29), https://arxiv.org/html/2601.22137v1 (Sections 4.1, 5, Appendices A.1 and B).
2. Noah Amsel, David Persson, Christopher Musco, Robert M. Gower, *The Polar Express: Optimal Matrix Sign Methods and Their Application to the Muon Algorithm*, arXiv:2505.16932 (2025-05-22), https://arxiv.org/html/2505.16932v5 (Sections 1–3, Appendix B).
3. Kristi Topollai and Anna Choromanska, *Cost-free Spectral Estimation for Adaptive Newton–Schulz in Matrix Optimizers*, arXiv:2609.33047 (2026-09-27), https://arxiv.org/abs/2609.33047 (abstract-level comparison only).
