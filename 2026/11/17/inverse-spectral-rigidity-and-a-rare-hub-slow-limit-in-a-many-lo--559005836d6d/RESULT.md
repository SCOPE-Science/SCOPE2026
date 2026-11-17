# Inverse spectral rigidity and a rare-hub slow limit in a many-loci quadratic system

## Finding
Consider the symmetric weighted-star specialization of the many-loci quadratic stochastic operator in [1]. For any finite positive central-locus mass and equal peripheral-locus masses, the entire unordered collection of hub–periphery interaction coefficients is recovered uniquely from the nonzero relaxation eigenvalues, with an explicit coefficient formula, even if coefficients are repeated. As the central mass tends to zero, the apparently disconnected peripheral loci instead evolve on a slow time scale according to an explicitly derived complete-graph Markov generator. In the distinct-coefficient case, its nonzero relaxation eigenvalues strictly interlace the original interaction coefficients.

## Assumptions and scope
Let \(r\geq2\) be an integer, let \(0<\varepsilon<1\), and choose real \(0<\alpha_i\leq1\) for \(1\leq i\leq r\). There are \(r+1\) loci, indexed \(0,1,\ldots,r\); each has two types \(x_{i,+},x_{i,-}\geq0\). Their conserved masses are \(c_0=\varepsilon\) and \(c_i=(1-\varepsilon)/r\) for \(i\geq1\), and the sum of all type masses is one. Set \(a_{0i}=a_{i0}=\alpha_i\) and every other interaction \(a_{ij}=0\). Define the quadratic stochastic map exactly by
\[
 x_{i,+}'=x_{i,+}+\sum_{j=0}^r a_{ij}(x_{i,-}x_{j,+}-x_{i,+}x_{j,-}),\qquad x_{i,-}'=c_i-x_{i,+}'.
\]
This is a specialization of the quadratic operator in [1]. Nonnegativity follows from the stochastic convex-mixture form below. Define \(q_i=x_{i,+}/c_i\in[0,1]\), \(A=r^{-1}\sum_{i=1}^r\alpha_i\), and \(U(z)=\prod_{i=1}^r(z-\alpha_i)=\sum_{k=0}^r b_kz^k\) with \(b_r=1\).

**Exact inverse relaxation spectrum.** The fraction vector evolves linearly by \(q(n+1)=P_\varepsilon q(n)\), where
\[
 (P_\varepsilon q)_0=\left[1-(1-\varepsilon)A\right]q_0+\frac{1-\varepsilon}{r}\sum_{i=1}^r\alpha_iq_i,
 \qquad (P_\varepsilon q)_i=(1-\varepsilon\alpha_i)q_i+\varepsilon\alpha_iq_0.
\]
Let \(L_\varepsilon=I-P_\varepsilon\); it has one zero eigenvalue and \(r\) strictly positive real eigenvalues \(\nu_1,\ldots,\nu_r\), with algebraic multiplicity. Set \(z_j=\nu_j/\varepsilon\) and form the directly observable polynomial
\[
 R_\varepsilon(z)=\varepsilon\prod_{j=1}^r(z-z_j).
\]
Then \(R_\varepsilon(z)=U(z)-(1-\varepsilon)zU'(z)/r\), and every coefficient is recovered by
\[
 \boxed{\displaystyle b_k=\frac{[z^k]R_\varepsilon(z)}{1-(1-\varepsilon)k/r},\qquad 0\leq k\leq r.}
\]
Every denominator is at least \(\varepsilon>0\). Hence the unordered spectrum determines the unordered multiset \(\{\alpha_1,\ldots,\alpha_r\}\) uniquely, including coincident values. This is exact identifiability, not a numerical stability guarantee. The central mass \(\varepsilon\) and the number of leaves \(r\) are assumed known.

**Rare-hub slow evolution.** Fix \(r\) and the coefficients, let \(\varepsilon\downarrow0\), and prescribe an initial hub fraction \(q_0(0)=h\in[0,1]\) and initial peripheral fractions \(u(0)\in[0,1]^r\) independent of \(\varepsilon\). Put \(\beta=\sum_i\alpha_i=rA\), \(\alpha=(\alpha_1,\ldots,\alpha_r)^\mathsf T\), and
\[
 Q=-\operatorname{diag}(\alpha_i)+\frac{\alpha\alpha^\mathsf T}{\beta},\qquad Z(u)=\frac{\sum_i\alpha_iu_i}{\beta}.
\]
This \(Q\) is the generator of a symmetric irreducible continuous-time Markov chain on the **complete** graph of peripheral loci: \(Q_{ij}=\alpha_i\alpha_j/\beta>0\) for distinct \(i,j\). For each fixed \(T>0\) there are constants \(C_T<\infty\) and \(\varepsilon_T>0\), depending only on \(T,r,\alpha\), such that for all \(0<\varepsilon<\varepsilon_T\) and integers \(0\leq n\leq T/\varepsilon\),
\[
 \boxed{\displaystyle \|q_{1:r}(n)-e^{\varepsilon nQ}u(0)\|_\infty\leq C_T\varepsilon,}\qquad
 \boxed{\displaystyle |q_0(n)-Z(e^{\varepsilon nQ}u(0))|\leq C_T\left((1-A/2)^n+\varepsilon\right).}
\]
The second bound allows the genuine initial fast boundary layer. In particular, the peripheral fractions converge uniformly on the accelerated time interval \(t=\varepsilon n\in[0,T]\) to \(e^{tQ}u(0)\), while the hub is slaved after the boundary layer to the weighted peripheral average \(Z\).

If the coefficients are pairwise distinct and sorted \(0<\alpha_1<\cdots<\alpha_r\), let \(0<\mu_1<\cdots<\mu_{r-1}\) be the nonzero eigenvalues of \(-Q\). They obey the strict interlacing
\[
 \boxed{\alpha_j<\mu_j<\alpha_{j+1}\qquad(1\leq j<r).}
\]
The relaxation spectrum splits into \(r-1\) slow values \(\nu_j(\varepsilon)=\varepsilon\mu_j+O(\varepsilon^2)\) and one fast value \(\nu_{\mathrm f}(\varepsilon)=A+O(\varepsilon)\). The hub and leaf dynamics therefore exhibit two different intrinsic time scales. Repeated coefficients remain covered by the exact inversion and the slow semigroup bounds; strict interlacing is asserted only for distinct coefficients.

## Proof
The conservation laws give \(x_{i,-}x_{j,+}-x_{i,+}x_{j,-}=c_ic_j(q_j-q_i)\). Dividing by \(c_i\) yields \(q_i'=q_i+\sum_ja_{ij}c_j(q_j-q_i)\), which is exactly the displayed row-stochastic \(P_\varepsilon\). Since \(c_i(P_\varepsilon)_{ij}=c_j(P_\varepsilon)_{ji}\), the chain is reversible, and every positive spoke gives irreducibility. Consequently \(L_\varepsilon\) is similar to a real symmetric positive-semidefinite matrix with one-dimensional kernel, so its other \(r\) eigenvalues are real and strictly positive.

In the order hub, then leaves, write
\[
 L_\varepsilon=\begin{pmatrix}(1-\varepsilon)A&-(1-\varepsilon)\alpha^\mathsf T/r\\ -\varepsilon\alpha&\varepsilon\operatorname{diag}(\alpha_i)\end{pmatrix}.
\]
The Schur complement of the peripheral diagonal block in \(\varepsilon zI-L_\varepsilon\), initially for \(z\) away from the \(\alpha_i\), gives
\[
 \begin{aligned}
 \det(\varepsilon zI-L_\varepsilon)
 &=\varepsilon^rU(z)\left[\varepsilon z-(1-\varepsilon)A-\frac{1-\varepsilon}{r}\sum_i\frac{\alpha_i^2}{z-\alpha_i}\right]\\
 &=\varepsilon^rz\left[U(z)-\frac{1-\varepsilon}{r}zU'(z)\right].
 \end{aligned}
\]
The second identity uses \(\sum_i[\alpha_i+\alpha_i^2/(z-\alpha_i)]=z[zU'(z)/U(z)-r]\). Polynomial continuation removes the restriction on \(z\). One determinant factor is \(z\); the other is \(R_\varepsilon\) because its leading coefficient is \(\varepsilon\). Coefficient comparison proves inversion. Since the coefficient multipliers are strictly positive, no two monic coupling polynomials with the same observed spectrum can differ.

For the singular limit write \(u_n=q_{1:r}(n)\) and \(e_n=q_0(n)-Z(u_n)\). The exact update becomes
\[
 u_{n+1}=u_n+\varepsilon Qu_n+\varepsilon\alpha e_n,
\]
and
\[
 e_{n+1}=\big[1-(1-\varepsilon)A\big]e_n+Z(u_n)-Z(u_{n+1}).
\]
Because all fractions stay in the unit cube, \(\|u_{n+1}-u_n\|_\infty\leq\varepsilon\), hence \(|Z(u_{n+1})-Z(u_n)|\leq\varepsilon\). For \(\varepsilon\leq1/2\), the hub contraction factor lies between zero and \(1-A/2\), so
\[
 |e_n|\leq (1-A/2)^n|e_0|+2\varepsilon/A.
\]
In particular \(\sum_{n=0}^{\lfloor T/\varepsilon\rfloor}|e_n|\leq(4+2T)/A\), because \(|e_0|\leq1\). The forced Euler recurrence and \(\|e^{\varepsilon Q}-(I+\varepsilon Q)\|=O(\varepsilon^2)\) now show, by discrete Gronwall or telescoping with the bounded Markov semigroup, that \(\|u_n-e^{\varepsilon nQ}u(0)\|_\infty\leq C_T\varepsilon\). Applying the linear functional \(Z\) yields the asserted hub bound.

For spectral separation, the rank-one determinant formula gives
\[
 \det(zI+Q)=\det(zI+\operatorname{diag}(-\alpha_i)+\alpha\alpha^\mathsf T/\beta)
 =-\frac zA\left[U(z)-\frac zrU'(z)\right].
\]
Equivalently, on \((\alpha_j,\alpha_{j+1})\), the scalar secular equation for a nonzero eigenvalue of \(-Q\) is \(\sum_i\alpha_i^2/(\alpha_i-z)=\beta\); its left side is strictly increasing, with limits \(-\infty\) and \(+\infty\) across the interval (after ordering signs appropriately), and therefore has one root in each interval. More directly, the equation \(\sum_i\alpha_i/(z-\alpha_i)=0\), equivalent to \(U(z)-zU'(z)/r=0\) for \(z\ne0\), is strictly decreasing from \(+\infty\) to \(-\infty\) between successive ordered poles, giving the same strict interlacing. As \(\varepsilon\to0\), \(R_\varepsilon(z)\to U(z)-zU'(z)/r\) on compact subsets, a degree-\(r-1\) polynomial whose distinct real roots are the \(\mu_j\). Polynomial root perturbation gives \(z_j=\mu_j+O(\varepsilon)\) for these roots and the remaining root diverges. The trace \(\operatorname{tr}L_\varepsilon=A+\varepsilon(r-1)A\) establishes \(\nu_{\mathrm f}=A+O(\varepsilon)\).

## Verification
The accompanying standalone Python script `check_star_inverse.py` symbolically tests the determinant identity on an exact rational four-leaf instance, numerically reconstructs distinct and repeated couplings over several central masses, tests strict interlacing, and compares the discrete trajectories against the limiting matrix semigroup at four shrinking central masses. Its successful marker is `RARE_HUB_INVERSE_AND_SLOW_LIMIT_OK`. These computations are consistency checks; the proof above, not finite testing, establishes the all-parameter result.

## Relationship to prior work
Omirov and Rozikov [1] introduce the exact many-loci quadratic stochastic operator, its invariant pair-mass fibers, associated linear maps, and convergence. The star specialization and algebraic reduction originate from their framework and are not claimed as new. The present theorem instead proves spectrum-only identification of **all** star interaction coefficients, including multiplicities, and a singular rare-hub limit with a dense effective peripheral generator and precise interlacing. Classical inverse problems for arrowhead matrices [2] provide a relevant comparison, but their stated reconstruction data include selected eigenvalues of leading principal submatrices (and, in nonsymmetric settings, an eigenvector), unlike the single full relaxation spectrum used here. These comparisons do not certify global publication priority.

## Limitations
The inverse result presupposes known \(\varepsilon\), known equal peripheral masses, exact full nonzero eigenvalues, and the specified symmetric star interactions. Repeated or closely spaced coefficients can make numerical root recovery ill-conditioned; uniqueness does not imply stable estimation. Uniform slow-limit estimates hold for fixed positive coefficients and fixed finite accelerated horizon, not uniformly as a coupling vanishes or as time grows without bound. Strict interlacing is restricted to distinct coefficients. Wider inverse spectral and averaging literature may contain equivalent formulations not identified in the comparison; no independent mathematical audit has been performed.

## References
[1] B. A. Omirov and U. A. Rozikov, *A many-loci system with evolution characterized by uncountable linear operators*, arXiv:2409.19687v1 (first publicly available 2024-09-29), https://arxiv.org/abs/2409.19687 .

[2] H. Pickmann-Soto, S. Arela-Pérez, J. Egaña, and D. Carrasco-Olivera, *On the inverse eigenproblem for symmetric and nonsymmetric arrowhead matrices*, Proyecciones 38 (2019), 811–828, DOI:10.22199/issn.0717-6279-2019-04-0053.
