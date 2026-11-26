# Exact inverse-spectrum dissipation and anisotropy frontier for planar Ornstein–Uhlenbeck steady states

## Finding

Consider every real two-dimensional Ornstein–Uhlenbeck diffusion with identity stationary covariance, real prescribed relaxation eigenvalues \(-a-b\) and \(-a+b\), where \(a>b>0\), and strictly positive-definite white-noise covariance. Let \(K\) be the spectral condition number of that covariance and \(\Phi\) the stationary entropy-production rate using the physical diffusion tensor. The **entire feasible thermodynamic diagram**, with no assumption on the orientation of the drift or noise, is

\[
K\in[K_0,\infty),\qquad K_0=\frac{a+b}{a-b},\qquad
\Phi=\frac{a^2(K-1)^2-b^2(K+1)^2}{2aK}.
\]

Every point on this curve is realized by a nondegenerate diffusion; \(\Phi\) increases strictly from zero to infinity. Consequently, subject to any finite noise-anisotropy cap \(K\le C\), the model class is nonempty exactly when \(C\ge K_0\), and the greatest possible entropy production is the displayed function evaluated at \(C\), attained at the boundary. In the same class the invariant probability distribution is always \(N(0,I_2)\), the sum of the two noise-variance eigenvalues is always \(4a\), and the drift spectrum is fixed. Thus equal-time statistics, relaxation eigenvalues and total noise intensity do not bound dissipation without an anisotropy constraint.

There is also a finite-lag obstruction to estimating the divergent dissipation. With \(C(\tau)=\mathbb E[X_tX_{t+\tau}^{\mathsf T}]\), for every \(\tau\ge0\),

\[
\|C(\tau)-C(\tau)^{\mathsf T}\|_{F}
=\frac{2\sqrt2\,e^{-a\tau}\sinh(b\tau)}{b}
\sqrt{\frac{a^2(K-1)^2}{(K+1)^2}-b^2}
\le\frac{2\sqrt2\sqrt{a^2-b^2}}{b}e^{-a\tau}\sinh(b\tau).
\]

The upper bound is approached as \(K\to\infty\), simultaneously with \(\Phi\to\infty\). This is a joint exact classification of dissipation and lag asymmetry at fixed stationary law and real spectrum, rather than an assertion that lag asymmetry itself vanishes.

## Assumptions and scope

Let \(a>b>0\). The state satisfies

\[
dX_t=A X_t\,dt+G\,dW_t,
\quad A\in\mathbb R^{2\times2},\quad B=GG^{\mathsf T}\succ0,
\quad \operatorname{spec}(A)=\{-a-b,-a+b\}.
\]

Assume \(W_t\) is standard two-dimensional Brownian motion, the mean is zero, and the unique stationary covariance is \(\Sigma=I_2\). Write \(D=B/2\), so the forward diffusion generator is \(L f=(Ax)\cdot\nabla f+D:\nabla^2f\). The stationary density is \(p(x)=(2\pi)^{-1}e^{-\|x\|^2/2}\). Its probability current is \(j(x)=(Ax-D\nabla\log p(x))p(x)=(A+D)x p(x)\). We use the standard dimensionless stationary entropy-production convention

\[
\Phi=\int_{\mathbb R^2}\frac{j(x)^{\mathsf T}D^{-1}j(x)}{p(x)}\,dx.
\]

\(K=\lambda_{\max}(B)/\lambda_{\min}(B)\) is the Euclidean spectral condition number. It is not an operator norm of the drift or a model-independent thermodynamic temperature ratio. Covariance and eigenvalues are specified exactly, not merely estimated from finite samples; the result is two-dimensional and requires nondegenerate diffusion and strictly distinct real stable eigenvalues.

## Proof

**1. The inverse stationary problem.** Since both eigenvalues of \(A\) are strictly negative, \(A\) is Hurwitz. The unique stationary covariance satisfies the Lyapunov equation \(A\Sigma+\Sigma A^{\mathsf T}+B=0\). Imposing \(\Sigma=I_2\) makes the noise covariance unique:

\[
B=-(A+A^{\mathsf T}),\qquad D=-\tfrac12(A+A^{\mathsf T}).
\]

As \(\operatorname{tr} A=-2a\), this identity also forces \(\operatorname{tr} B=4a\). Conversely, any such stable \(A\) with \(-(A+A^{\mathsf T})\succ0\) admits the required stationary Gaussian by the Lyapunov uniqueness theorem.

**2. Rotation-invariant normal form.** Write uniquely

\[
A=-aI_2+S+W,\quad S=\tfrac12(A+A^{\mathsf T})+aI_2,\quad W=\tfrac12(A-A^{\mathsf T}),
\]

where \(S\) is symmetric and traceless and \(W\) is skew-symmetric. For real scalars \(p,q,v\), necessarily

\[
S=\begin{pmatrix}p&q\\q&-p\end{pmatrix},\quad
W=\begin{pmatrix}0&v\\-v&0\end{pmatrix},\quad
c=\sqrt{p^2+q^2}.
\]

Direct multiplication gives \(S^2=c^2I_2\), \(W^2=-v^2I_2\), and \(SW+WS=0\). Thus \((A+aI_2)^2=(c^2-v^2)I_2\). The prescribed real eigenvalues force **exactly**

\[
c^2-v^2=b^2.
\]

Also \(D=aI_2-S\) has eigenvalues \(a-c,a+c\); its positivity is equivalent to \(c<a\). Consequently the complete feasible parameter set is \(b\le c<a\), with \(|v|=\sqrt{c^2-b^2}\). No other matrices are possible. Conversely, for every such \(c\), choose \(S=\operatorname{diag}(c,-c)\) and \(W=\bigl(\begin{smallmatrix}0&\sqrt{c^2-b^2}\\-\sqrt{c^2-b^2}&0\end{smallmatrix}\bigr)\); the constructed \(A\) and \(B=2(aI_2-S)\) satisfy all assumptions. All possibilities are equivalent to this form up to orthogonal conjugation and circulation orientation.

**3. Exact dissipation.** Because \(A+D=W\), the stationary current is \(j(x)=Wx\,p(x)\), zero if and only if \(v=0\). The invariant covariance is identity, so integrating the quadratic form yields

\[
\Phi=\operatorname{tr}(W^{\mathsf T}D^{-1}W)=v^2\operatorname{tr}(D^{-1})
=\frac{2av^2}{a^2-c^2}=\frac{2a(c^2-b^2)}{a^2-c^2}.
\]

No limit, simulation or asymptotic approximation was used here. The positivity restriction ensures the denominator is strictly positive.

**4. Elimination and sharp budget.** The noise covariance eigenvalues are \(2(a-c),2(a+c)\), hence

\[
K=\frac{a+c}{a-c},\quad c=a\frac{K-1}{K+1}.
\]

The allowed interval \(b\le c<a\) corresponds bijectively to \(K\in[K_0,\infty)\), where \(K_0=(a+b)/(a-b)\). Substituting into the expression for \(\Phi\) proves the formula in the finding. Its derivative is strictly positive:

\[
\frac{d\Phi}{dK}=\frac{a^2-b^2}{2a}\left(1-\frac1{K^2}\right)>0
\quad (K\ge K_0>1).
\]

(The equivalent form is \(\Phi=(a^2-b^2)(K+K^{-1})/(2a)-(a^2+b^2)/a\).) The endpoint \(c=b\) gives \(\Phi=0\); as \(c\uparrow a\), \(\Phi\uparrow\infty\). For any cap \(C\ge K_0\), choosing \(c=a(C-1)/(C+1)\) attains the bound. Equality demands \(K=C\), hence the magnitude of \(c\) and \(|v|\) is fixed, with the remaining freedom only spatial orthogonal orientation and circulation sign. There is no finite supremum without an anisotropy cap.

**5. Lag-asymmetry saturation.** For \(\tau\ge0\), stationarity gives \(C(\tau)=e^{A^{\mathsf T}\tau}\). The same anticommutation identity yields

\[
e^{A\tau}=e^{-a\tau}\left[\cosh(b\tau)I_2+\frac{\sinh(b\tau)}b(S+W)\right].
\]

Subtracting the transpose leaves \(C(\tau)-C(\tau)^{\mathsf T}=-2e^{-a\tau}\sinh(b\tau)W/b\). Since \(\|W\|_F=\sqrt2|v|\), this establishes the stated formula and the uniform bound \(|v|<\sqrt{a^2-b^2}\). At any fixed \(\tau>0\), the bound is a strict supremum, not an attained maximum in the positive-definite model class. At \(\tau=0\), both sides are zero.

## Verification

The standalone script `verify.py` reconstructs stable generators, solves the stationary continuous Lyapunov equation numerically, independently calculates the current-based quadratic entropy production, computes the diffusion condition number and lag covariance using matrix exponentials, and compares these with the exact expressions for four distinct parameter pairs and several nonnormality levels. It reports 328 deterministic assertions. These finite checks corroborate the algebra; the proof above, rather than numerical samples, establishes the all-matrices classification.

## Relationship to prior work

Troude and Sornette (2026, arXiv:2603.07206v1), especially their reduced nonnormal stochastic model and supplementary sections VI.2–VI.5, establish Gaussian lag asymmetry and an entropy-production formula for nonnormal drift with correlated noise. These are **prior** and are not presented as new. Their work studies forward dynamics with specified forcing; the statement here instead solves the inverse covariance-matching problem and classifies the exact joint feasible diagram of entropy production versus forcing anisotropy under fixed stationary law and fixed real drift spectrum, including sharp attainment and unbounded-cost/bounded-lag coexistence.

Godrèche and Luck (2018, arXiv:1807.00694), especially section 2.10 and equation (2.71), give a general closed-form entropy-production rate in two-dimensional Ornstein–Uhlenbeck systems, and section 3 already exhibits invariant distributions insensitive to dynamic asymmetry. Both points are credited. Those general identities supply ingredients used by the present constrained classification; its claim of distinctness rests on the explicit global inverse spectral constraint and sharp attainable condition-number frontier, not a new generic entropy-production identity. Nagayama, Kolchinsky and Ito (2026, arXiv:2606.07263) provide a broader oscillatory/nonnormal decomposition and relaxation-dissipation trade-offs, which are not asserted to be new here.

## Limitations

The classification requires an identity stationary covariance, specified distinct real eigenvalues, and strictly positive diffusion. A known nonidentity covariance can be whitened, but the Euclidean noise condition number is not preserved under arbitrary whitening, so the displayed noise-anisotropy frontier must not be transferred unmodified. There is no claim of high-dimensional optimality, unique dynamics from one-time data, independently measured entropy production, or an experimentally optimal design. The divergent dissipation occurs in a positive-definite family approaching a singular-noise boundary; it does not assign entropy production to the singular limiting diffusion. Different conventions for noise covariance versus physical diffusion multiply entropy-production expressions by convention-dependent factors. Prior general formulas might subsume the algebraic classification through a specialization not explicitly identified in the inspected sources; this remains an originality limitation.

## References

1. V. Troude and D. Sornette, *Pseudo-Coherence and Stochastic Synchronization: A Non-Normal Route to Collective Dynamics without Oscillators*, arXiv:2603.07206v1 (first publicly 2026-03-07), https://arxiv.org/html/2603.07206v1 .
2. C. Godrèche and J. M. Luck, *Characterising the nonequilibrium stationary states of Ornstein-Uhlenbeck processes*, arXiv:1807.00694, https://arxiv.org/pdf/1807.00694 .
3. R. Nagayama, A. Kolchinsky and S. Ito, *Oscillatory-nonnormal decomposition of dissipation in Ornstein-Uhlenbeck processes*, arXiv:2606.07263 (first publicly 2026-06-05), https://arxiv.org/abs/2606.07263 .
4. A. Strang, *A Theoretical Review of Area Production Rates as Test Statistics for Detecting Nonequilibrium Dynamics in Ornstein–Uhlenbeck Processes*, Axioms 13 (2024), 820, https://doi.org/10.3390/axioms13120820 .
