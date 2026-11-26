# Sharp oracle-coupling reversal for noisy two-step slingshot descent-ascent

## Finding

Consider the scalar bilinear saddle problem \(\min_x\max_y\,\sigma xy\) with \(\sigma>0\). Apply the paired signed-stepsize gradient-descent-ascent method of Shugart and Altschuler at a constant positive magnitude \(h\). At each individual gradient evaluation add a centered Gaussian vector \(\xi_{m,j}\in\mathbb R^2\), where the first and second evaluations within pair \(m\) have the **same separate marginal** \(N(0,vI_2)\), \(v>0\), but may be coupled arbitrarily; distinct pairs are identically distributed and independent. Put \(r=h\sigma\).

For every \(0<r<\sqrt2\), every deterministic initial point, and every integer number of completed pairs \(n\ge1\), the coupling that minimizes \(\mathbb E\|z_{2n}\|^2\) is **independent of the horizon** and has a sharp transition:

\[
\boxed{\begin{array}{ll}
\xi_{m,1}=\xi_{m,0}\ \text{almost surely},&0<r<1,\\
\xi_{m,1}=S\xi_{m,0}\ \text{almost surely},&1<r<\sqrt2,
\end{array}\qquad S=\begin{pmatrix}0&1\\1&0\end{pmatrix}.}
\]

Each is the unique minimizing coupling in its open regime, even if non-Gaussian joint laws with the specified Gaussian marginals are admitted. At \(r=1\), both displayed couplings minimize and there are further minimizers. Let \(R_*(r)\) denote the smallest stationary expected squared Euclidean distance to the saddle, calculated at the ends of pairs. Then

\[
\boxed{
R_*(r)=\frac{2v}{\sigma^2(2-r^2)}
\begin{cases}
r^2,&0<r\le1,\\
1+(r-1)^2,&1\le r<\sqrt2.
\end{cases}}
\]

The finite-horizon optimum is exactly
\[
\boxed{\min\mathbb E\|z_{2n}\|^2
=(1-r^2)^{2n}\|z_0\|^2
+\bigl(1-(1-r^2)^{2n}\bigr)R_*(r).}
\]

For comparison, independent noise in the two calls has stationary risk
\[
R_{\mathrm{ind}}(r)=\frac{2v(2+r^2)}{\sigma^2(2-r^2)},
\]
while simply reusing the same noise in both calls has stationary risk
\[
R_{\mathrm{same}}(r)=\frac{2vr^2}{\sigma^2(2-r^2)}.
\]
Thus \(\lim_{r\downarrow0}R_{\mathrm{ind}}(r)=2v/\sigma^2\) despite vanishing stepsizes, whereas \(R_*(r)\sim vr^2/\sigma^2\). For \(r>1\), *swapping the two Gaussian noise components* strictly outperforms identical sample reuse. These are statements about a fixed-marginal **coupled-oracle model**; the minimizing second call is generally not conditionally unbiased after observing the first call.

## Assumptions and scope

The variables \(x,y\) are real scalars, \(z=(x,y)^\top\), \(\sigma,h,v\) are strictly positive, and the initial state is deterministic. A pair consists of the two genuine gradient-descent-ascent updates with steps
\[
(\alpha_{2m},\beta_{2m})=(h,-h),\qquad
(\alpha_{2m+1},\beta_{2m+1})=(-h,h).
\]
At update \(k\), the observed gradient of the bilinear objective is \((\sigma y,\sigma x)^\top+\xi_{m,j}\); the signs are applied as in ordinary descent in \(x\) and ascent in \(y\). Each pair of centered noises is independent of all preceding pairs and the initial point, has two \(N(0,vI_2)\) marginals, and is otherwise arbitrary. The coupling may be selected using \(r\), but not using the current state. Both oracle calls are counted, with equal noise marginal variance in each. Correlation between the two calls is permitted; no adaptive conditional-unbiasedness requirement is made. At a fresh pair's first call, the noise is independent of the state. At the second call, a reused or swapped noise may be conditionally predictable given the intermediate iterate: that distinction is essential.

The strict stationarity statements concern \(0<r<\sqrt2\). Outside this interval, the deterministic two-step multiplier is not strictly contractive, and stationary finite-risk conclusions are not asserted. The finite-step algebra holds for arbitrary positive \(r\) but the theorem's stated optimality range is the contractive one. This is an exact scalar bilinear benchmark, not a general nonlinear or multidimensional stochastic optimization guarantee.

## Proof

**1. Paired recursion and its stability.** Set
\[
U_-=I_2-rS,\qquad U_+=I_2+rS.
\]
The two signed GDA steps are exactly
\[
z_{2m+1}=U_-z_{2m}-h\xi_{m,0},\qquad
z_{2m+2}=U_+z_{2m+1}+h\xi_{m,1}.
\]
Since \(S^2=I_2\), substitution gives
\[
\boxed{z_{2m+2}=(1-r^2)z_{2m}
+h(\xi_{m,1}-U_+\xi_{m,0}).}
\]
Write \(a=1-r^2\). Then \(|a|<1\) exactly for \(0<r<\sqrt2\).

**2. Exact finite-horizon risk.** Independent, centered pairs imply
\[
\mathbb E\|z_{2n}\|^2
=a^{2n}\|z_0\|^2
+h^2\sum_{j=0}^{n-1}a^{2j}
\mathbb E\|\xi_1-U_+\xi_0\|^2.
\]
The sum equals \((1-a^{2n})/(1-a^2)\), where
\[
1-a^2=r^2(2-r^2)>0.
\]
Thus every horizon and the stationary risk are minimized by the same coupling that minimizes the *one-pair noise energy* \(\mathbb E\|\xi_1-U_+\xi_0\|^2\).

**3. Exact coupling optimum.** The real symmetric \(U_+\) has eigenvalues \(\lambda_+=1+r>0\) and \(\lambda_-=1-r\), with orthogonal eigenvectors of \(S\). In that orthonormal basis, let \(X_\pm,Y_\pm\) be the respective coordinates of \(\xi_0,\xi_1\). Every coordinate has centered marginal variance \(v\), irrespective of the coupling. Cauchy--Schwarz gives, for each sign,
\[
\mathbb E(Y_\pm-\lambda_\pm X_\pm)^2
=v(1+\lambda_\pm^2)-2\lambda_\pm\mathbb E(X_\pm Y_\pm)
\ge v(|\lambda_\pm|-1)^2.
\]
Equality for \(\lambda_\pm\ne0\) forces \(Y_\pm=\operatorname{sgn}(\lambda_\pm)X_\pm\) almost surely. Summing shows the exact minimum
\[
v\bigl[r^2+(|1-r|-1)^2\bigr].
\]
Because the isotropic Gaussian marginals are invariant under every orthogonal map, these simultaneous equality conditions are feasible: they require \(\xi_1=\xi_0\) for \(r<1\), and \(\xi_1=S\xi_0\) for \(r>1\). Equality conditions establish uniqueness in each open regime even among nonlinear couplings of the two marginals. At \(r=1\), \(\lambda_-=0\), and the corresponding cross-correlation does not affect the objective, so uniqueness fails.

**4. Stationary risk and sharp transition.** Substitute the preceding minimum into the geometric-series formula. Using \(h^2/r^2=1/\sigma^2\) gives exactly the displayed piecewise \(R_*(r)\) and the finite-horizon formula. The strict preference changes at \(r=1\): for \(r<1\), the shared coupling aligns both eigencoordinates with their positive multipliers; for \(r>1\), the antisymmetric eigencoordinate's multiplier is negative, requiring sign reversal. The boundary is sharp because neither coupling minimizes on the opposite open interval.

**5. Comparators and small-step obstruction.** Independent calls have zero cross-covariance, so
\[
\mathbb E\|\xi_1-U_+\xi_0\|^2
=v\operatorname{tr}(I_2+U_+^2)=v(4+2r^2).
\]
Same-noise reuse gives \(\xi_1-U_+\xi_0=-rS\xi_0\), hence one-pair energy \(2vr^2\). These yield \(R_{\mathrm{ind}}\) and \(R_{\mathrm{same}}\) as claimed. When \(r\downarrow0\), each fresh-oracle perturbation is of size \(h\), while per-pair deterministic damping is only of order \(h^2\). Reusing the same Gaussian noise cancels the first-order random perturbations, and the optimal stationary risk vanishes at order \(h^2\). The formulas, rather than this heuristic, prove both limits.

## Verification

The standalone standard-library program `verify.py` computes the paired matrices and the one-pair second-moment formulas with exact rational arithmetic. It checks 5,676 orthogonal-coupling and finite-horizon comparisons across 129 admissible rational-step pairs, as well as the explicit witnesses \(r=3/5\) and \(r=6/5\). The symbolic proof covers all real \(r\) in the stated interval; these finitely many checks do not replace it. Run `python verify.py` from the extracted package directory.

## Relationship to prior work

Shugart and Altschuler (arXiv:2505.01423, first released May 2, 2025) introduced the exact paired positive/negative stepsize schedule and its deterministic polynomial reduction. The relevant full text (Sections 1.2, 3.1, 6, and Appendix A) motivates stochastic-gradient and robustness questions but does not establish the fixed-Gaussian-marginal, finite-horizon noise-coupling optimum or the swap transition here. The deterministic method is fully credited to them.

Gorbunov, Berard, Gidel, and Loizou (arXiv:2111.08611) distinguish same-sample and independent-sample stochastic extragradient schemes; Vlatakis-Gkaragkounis, Giannou, Chen, and Xie (arXiv:2306.16502) study invariant laws for stochastic extragradient and GDA. Neither is the signed two-step bilinear scheme analyzed here. Classical covariance alignment, optimal transport and Cauchy--Schwarz supply the underlying coupling inequality; those general principles are not claimed as new. The contribution is the precise slingshot-specific finite-horizon/stationary noise law, the sharp change in optimal coupled-oracle design, and the contrast with fresh calls. Historical priority is not independently certified.

## Limitations

The result assumes a single scalar bilinear coupling, fixed step magnitude, isotropic Gaussian oracle marginals, unlimited within-pair noise coupling, and independence across pairs. A rotated or reused second noise is not an ordinary conditionally unbiased *second* stochastic oracle at the random intermediate point. If such conditional unbiasedness is required, the relevant cross-covariance vanishes and independent-call second-moment risk is unavoidable. A joint Gaussian coupling with swapped noise components is mathematically feasible but may not be realizable in every application from ordinary data sampling. The theorem does not characterize noise coupling in nonlinear games, floating-point robustness, multiple singular modes with a single shared design, or general finite-sum oracle constraints.

## References

- H. Shugart and J. M. Altschuler, *Negative Stepsizes Make Gradient-Descent-Ascent Converge*, arXiv:2505.01423, initial public version 2025-05-02. https://arxiv.org/abs/2505.01423 ; full text https://arxiv.org/html/2505.01423v2 .
- E. Gorbunov, H. Berard, G. Gidel, and N. Loizou, *Stochastic Extragradient: General Analysis and Improved Rates*, arXiv:2111.08611 (2021/2022). https://arxiv.org/abs/2111.08611 .
- E.-V. Vlatakis-Gkaragkounis, A. Giannou, Y. Chen, and Q. Xie, *Stochastic Methods in Variational Inequalities: Ergodicity, Bias and Refinements*, arXiv:2306.16502 (2023). https://arxiv.org/abs/2306.16502 .
