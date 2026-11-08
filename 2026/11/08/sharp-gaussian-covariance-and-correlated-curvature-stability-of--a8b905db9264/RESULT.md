# Sharp Gaussian covariance and correlated-curvature stability of random-coordinate Langevin sampling

## Finding
For the random-coordinate, full-noise overdamped Langevin discretization of a strongly convex quadratic, two exact statements hold. First, in any dimension with a constant Hessian diagonal, its finite-variance invariant covariance is an isotropic scalar inflation of the *full inverse Hessian*, with a sharp, correlation-independent stepsize boundary. Second, in dimension two, correlations between unequally curved coordinates strictly enlarge the sharp mean-square stable stepsize, by a factor approaching at most \((1+\sqrt 2)/2\). The upper factor is sharp and is not attained within the positive-definite class.

Let \(d\ge2\), \(H\in\mathbb R^{d\times d}\) be symmetric positive definite, and \(e_j\) the coordinate unit vectors. Independently for each iteration, choose \(J_n\) uniformly in \(\{1,\ldots,d\}\) and \(\xi_n\sim N(0,I_d)\). For \(h>0\), define
\[
X_{n+1}=(I_d-dh e_{J_n}e_{J_n}^{\mathsf T}H)X_n+\sqrt{2h}\,\xi_n.
\]
This is the uniform-coordinate RCD-O-LMC recursion with **full-dimensional Gaussian noise**, not the distinct single-coordinate-noise RC-LMC scheme.

**Constant-diagonal theorem.** If \(H_{jj}=a>0\) for all \(j\), then there exists a unique finite-second-moment invariant probability law precisely for
\[
0<h<\frac{2}{da}.
\]
Its mean is zero and its covariance is exactly
\[
\boxed{\Sigma_h=\frac{1}{1-dah/2}\,H^{-1}.}
\]
For \(h\ge2/(da)\), the expected quadratic energy grows at least linearly from every finite-energy initial law, and no finite-second-moment invariant probability exists. The finite-step invariant law itself is not asserted to be Gaussian.

**Sharp two-coordinate theorem.** For \(d=2\), write
\[
H=\begin{pmatrix}a&c\\c&b\end{pmatrix},\qquad a,b>0,\quad ab>c^2,
\quad K=\begin{pmatrix}a-\delta&\delta\\\delta&b-\delta\end{pmatrix},\quad
\delta=\frac{c^2}{a+b}.
\]
The finite-second-moment stationary law exists uniquely precisely when \(0<h<h_*\), where
\[
\boxed{h_* = \frac{1}{\lambda_{\max}(K)}
=\frac{2(a+b)}{(a+b)^2-2c^2+\sqrt{(a+b)^2(a-b)^2+4c^4}}.}
\]
At and above this boundary, second moments diverge from a zero start, linearly at the boundary in the projected critical mode and at least geometrically above it. When \(a\ne b\) and \(c\ne0\), the strict improvement and its optimal sharp envelope are
\[
\frac{1}{\max(a,b)}<h_*<\frac{1+\sqrt2}{2\max(a,b)}.
\]
When \(a=b\), \(h_*=1/a\) for every \(|c|<a\). The upper gain factor is approached as \(c^2\uparrow ab\) and \(\min(a,b)/\max(a,b)\to\sqrt2-1\). For example, \(H=\bigl(\begin{smallmatrix}1&1\\1&4\end{smallmatrix}\bigr)\) has \(h_*=10/(23+\sqrt{229})\approx0.2622418016526148\), strictly above the diagonal-only bound \(1/4\).

## Assumptions and scope
All coordinates use the same positive timestep, unbiased uniform-coordinate gradient estimates, and independent, full-dimensional additive Gaussian increments at every iteration. The Hessian is constant and strictly positive definite; no reversibility or Gaussianity of the *discrete* invariant law is assumed. Stability means convergence of the covariance recursion / geometric decay of synchronous-coupling second moments, equivalently existence of a unique invariant law with finite second moment. A stationary probability with infinite second moment at an unstable step is not ruled out. Results concern per-step sampling dynamics and do not assert wall-clock or physical-time optimality.

## Proof
**Exact moment operator.** Put \(M_j=I_d-dh e_je_j^{\mathsf T}H\). For any second-moment matrix \(S_n=\mathbb E[X_nX_n^{\mathsf T}]\), independence and centered noise imply
\[
S_{n+1}=\mathcal T_h(S_n)+2hI_d,\qquad
\mathcal T_h(S)=\frac1d\sum_{j=1}^{d}M_j S M_j^{\mathsf T}.
\]
The same homogeneous map propagates second moments of a synchronous-coupling difference. An invariant covariance solves \(S=\mathcal T_h(S)+2hI_d\).

**Uniform diagonal.** Expanding exactly,
\[
\mathcal T_h(H^{-1})=H^{-1}-2hI_d+dh^2\operatorname{diag}(H_{11},\ldots,H_{dd}).
\]
Consequently if every diagonal entry equals \(a\) and \(h<2/(da)\), the claimed \(\Sigma_h\) solves the stationary covariance equation. To prove stability rather than merely solve its linear equations, conditional expansion of the \(H\)-energy gives
\[
\mathbb E[\|M_{J_n}v\|_H^2]=\|v\|_H^2
-2h(1-dah/2)\|Hv\|_2^2.
\]
Because \(H\) is positive definite, the negative term controls a fixed positive fraction of \(\|v\|_H^2\) when \(h<2/(da)\), so synchronous couplings contract geometrically. Summing the independent Gaussian forcing then constructs a unique invariant probability in the finite-second-moment Wasserstein class. Its mean is zero, so the computed second-moment matrix is indeed its covariance. For \(h\ge2/(da)\), the exact inhomogeneous energy identity is
\[
\mathbb E[\|X_{n+1}\|_H^2]-\mathbb E[\|X_n\|_H^2]
=-2h(1-dah/2)\mathbb E\|HX_n\|_2^2+2h\operatorname{tr}H
\ge 2h\operatorname{tr}H.
\]
This proves divergence and finite-second-moment nonexistence, including the endpoint.

**Sharp two-coordinate stability.** Let \(Y_n=H^{1/2}X_n\), \(w_j=H^{1/2}e_j\), and \(B_j=I_2-2h w_jw_j^{\mathsf T}\). The covariance map in these coordinates is
\[
\widetilde{\mathcal T}_h(U)=\frac12\sum_{j=1}^2 B_j U B_j.
\]
It is self-adjoint in the Frobenius inner product and preserves the cone of positive-semidefinite matrices. In addition, its spectral radius equals its largest algebraic eigenvalue: decomposing any real symmetric \(U\) into positive/negative spectral parts gives \(|\langle U,\widetilde{\mathcal T}_h U\rangle|\le\langle |U|,\widetilde{\mathcal T}_h|U|\rangle\), with \(\||U|\|_F=\|U\|_F\). Therefore \(\rho(\widetilde{\mathcal T}_h)<1\) is equivalent to positive definiteness of \(I-\widetilde{\mathcal T}_h\) as a quadratic form.

Expansion yields the *exact* criterion
\[
\langle U,(I-\widetilde{\mathcal T}_h)U\rangle
=2h\left(\operatorname{tr}(HU^2)-h\sum_{j=1}^2(w_j^{\mathsf T}Uw_j)^2\right).
\]
Define the positive definite Sylvester operator \(\mathcal L(U)=(HU+UH)/2\), and the evaluation map \(\mathcal C(U)_j=w_j^{\mathsf T}Uw_j\). Hence the criterion becomes \(h\lambda_{\max}(\mathcal C\mathcal L^{-1}\mathcal C^*)<1\). Solving the two Sylvester equations \(\mathcal L(U_j)=w_jw_j^{\mathsf T}\) gives
\[
\mathcal C\mathcal L^{-1}\mathcal C^*=K=
\begin{pmatrix}a-c^2/(a+b)&c^2/(a+b)\\c^2/(a+b)&b-c^2/(a+b)\end{pmatrix}.
\]
The two-by-two eigenvalue formula gives the displayed \(h_*\). At \(h\ge h_*\), the positive cone map has a nonzero positive-semidefinite leading eigenmatrix; its positive dual projection pairs strictly positively with the transformed noise covariance \(2hH\). The resulting forced scalar moment recurrence is nondecaying at equality and exponentially growing above it, proving the asserted divergence and exclusion of finite-variance stationarity. Below the threshold, covariance-contraction and additive forcing give existence and uniqueness as before.

**Exact gain ceiling.** Increasing \(c^2\) decreases \(K\) in Loewner order, since \(K=\operatorname{diag}(a,b)-\delta(1,-1)^{\mathsf T}(1,-1)\). For unequal diagonal entries and nonzero \(c\), the largest eigenvalue decreases strictly from \(\max(a,b)\), yielding strict improvement. Let \(M=\max(a,b)\), \(r=\min(a,b)/M\). Taking \(c^2\uparrow ab\) drives \(\lambda_{\max}(K)\) down to \((a^2+b^2)/(a+b)\). Thus
\[
h_*M\le\frac{1+r}{1+r^2}\le\frac{1+\sqrt2}{2},
\]
with the latter equality only at \(r=\sqrt2-1\), and the former attained only at the excluded singular Hessian limit when \(a\ne b\). This proves the sharp unattained envelope.

## Verification
Run `python3 check.py` using Python 3's standard library. The checker exercises the moment operator with exact rational arithmetic for five constant-diagonal matrices through dimension four, checks direct anisotropic covariance fixed points and their positivity, verifies strict stability gains and the sharp supremum, and reproduces the explicit \(2\times2\) witness. The included `check_output.txt` records 427 passed assertions. These computations are diagnostic and **not** substitutes for the analytic universal proofs above.

## Relationship to prior work
Ding and Li's 2020 first-public preprint, later expanded into *Langevin Monte Carlo: random coordinate descent and variance reduction* (JMLR 22, 2021), defines precisely the full-noise, unbiased uniform-coordinate update (Algorithm 2, equations (16)–(17)) and proves nonasymptotic Wasserstein estimates with conservative stepsize conditions (Theorem 3). The present statements concern exact Gaussian covariance and a *necessary-and-sufficient* sharp mean-square stability boundary, not a new sampling algorithm or an improvement to their general Wasserstein theorem. The paper's explicit lower-bound construction is for an underdamped example, and does not imply the two-coordinate correlated threshold. Ding, Li, Lu and Wright's *Random Coordinate Langevin Monte Carlo* (arXiv:2010.01405) uses a different single-coordinate noise/update rule; its complexity estimates are not equivalent to this full-noise covariance law. The relevant general matrix moment and Sylvester techniques are classical; no novelty is claimed for these component tools.

## Limitations
The exact uniform-diagonal covariance law does not extend verbatim to all anisotropic diagonals; the sharp anisotropic frontier is proved only in dimension two. It measures finite-second-moment stability, not total variation mixing, exact target-distribution sampling, or a sharp Wasserstein bias. At steps beyond the frontier, existence of an invariant probability without finite second moment is not decided. The stationary law below the frontier is generally a Gaussian mixture, not asserted Gaussian. Historical specialist work on random affine recursions or quadratic stochastic-gradient samplers could contain equivalent statements despite the comparisons reported here.

## References
- Z. Ding and Q. Li, *Variance reduction for Random Coordinate Descent-Langevin Monte Carlo*, first public arXiv version 2020-06-10. https://arxiv.org/abs/2006.06068
- Z. Ding and Q. Li, *Langevin Monte Carlo: random coordinate descent and variance reduction*, Journal of Machine Learning Research 22 (2021), article 205, especially Algorithm 2, Theorem 3, and Section 4.3. https://jmlr.csail.mit.edu/papers/volume22/20-1205/20-1205.pdf
- Z. Ding, Q. Li, J. Lu and S. J. Wright, *Random Coordinate Langevin Monte Carlo*, arXiv first version 2020-10-03, and PMLR 134 (2021), pp. 1683–1710; Algorithm 1 uses coordinate-local noise. https://arxiv.org/abs/2010.01405
