# Radial conditioning and exact tail transitions for Kronecker Gaussian trace estimators

## Finding
Fix a nonzero real positive-semidefinite matrix \(H\) acting on \(\mathbb R^{n_1}\otimes\cdots\otimes\mathbb R^{n_d}\), with \(d\ge2\) and positive integer mode dimensions. In a Kronecker Gaussian trace probe, replace the Gaussian vectors in any selected subset \(J\subseteq\{1,\ldots,d\}\) by isotropic uniform-sphere vectors, and keep the remaining factors Gaussian. The resulting trace estimators are all unbiased. Normalizing additional factors decreases every convex loss under an exact mean-preserving coupling. More importantly, if \(r=d-|J|\ge1\) Gaussian factors remain, then the mean of \(m\ge1\) independent probes has the **exact logarithmic upper-tail law**

\[
\lim_{t\to\infty}t^{-1/r}\log\Pr\{\overline Z_{J,m}>t\}
=-\frac r2\left(\frac{m}{c_J\rho(H)}\right)^{1/r},
\qquad c_J=\prod_{j\in J}n_j,
\]

where the product-state numerical radius is

\[
\rho(H)=\max_{\|u_j\|_2=1}
\left(\bigotimes_{j=1}^du_j\right)^\mathsf TH
\left(\bigotimes_{j=1}^du_j\right)>0.
\]

When all \(d\) factors are normalized, the estimator is bounded and has essential supremum \(\left(\prod_jn_j\right)\rho(H)\). Thus each radial normalization removes one unit from the reciprocal stretched-exponential tail exponent; \(d-1\) normalizations are necessary and sufficient to restore a positive exponential moment, while all \(d\) give bounded support. These are fixed-dimension, fixed-sample-count asymptotics in the tail threshold \(t\).

## Assumptions and scope
Let \(H=H^\mathsf T\succeq0\), \(H\neq0\), and \(N=\prod_{j=1}^d n_j\). For each independent sample \(\ell=1,\ldots,m\) and mode \(j\), draw a real standard Gaussian \(G_{\ell,j}\in\mathbb R^{n_j}\), and set \(R_{\ell,j}=\|G_{\ell,j}\|_2\), \(U_{\ell,j}=G_{\ell,j}/R_{\ell,j}\). Almost surely all radii are positive. Then \(R_{\ell,j}^2\sim\chi^2_{n_j}\) and the directions \(U_{\ell,j}\) are uniform on their unit spheres, with all radii independent of all directions. For \(J\subseteq[d]\), set \(X_{\ell,j}^{(J)}=\sqrt{n_j}U_{\ell,j}\) for \(j\in J\), and \(X_{\ell,j}^{(J)}=G_{\ell,j}\) otherwise. Define

\[
Z_{J,\ell}=\left(\bigotimes_j X_{\ell,j}^{(J)}\right)^\mathsf TH
\left(\bigotimes_j X_{\ell,j}^{(J)}\right),\qquad
\overline Z_{J,m}=\frac1m\sum_{\ell=1}^m Z_{J,\ell}.
\]

All independence refers to the Gaussian draws; different \(J\) values are compared through the same underlying draws. No particular structure of \(H\) beyond real symmetric positive semidefiniteness is required; it may be supplied only through products with rank-one Kronecker vectors.

## Proof
**1. Unbiasedness and coupling.** Gaussian and scaled unit-sphere vectors both have second moment matrix \(I_{n_j}\), so independence gives \(\mathbb E Z_{J,\ell}=\operatorname{tr}H\). Define \(q(U)=\left(\bigotimes_jU_j\right)^\mathsf TH\left(\bigotimes_jU_j\right)\). Each probe satisfies the exact identity

\[
Z_{J,\ell}=c_Jq(U_\ell)\prod_{j\notin J}R_{\ell,j}^2.
\]

For \(J\subset K\), condition on every direction and the radii with indices outside \(K\). Since \(\mathbb E R_{\ell,j}^2=n_j\), the conditional mean of \(Z_{J,\ell}\) equals \(Z_{K,\ell}\). Apply this conditioning simultaneously to the \(m\) independent samples. Thus

\[
\overline Z_{K,m}\preceq_{\mathrm{cx}}\overline Z_{J,m},
\]

that is, \(\mathbb E\varphi(\overline Z_{K,m})\le\mathbb E\varphi(\overline Z_{J,m})\) for every convex \(\varphi\) for which the expectations are defined. Because \(q(U)>0\) with positive probability and removed chi-square radii are nondegenerate, the inequality is strict for any strictly convex loss with finite expectations whenever \(J\subsetneq K\). For second moments,

\[
\mathbb E Z_K^2=\mathbb E Z_J^2\prod_{j\in K\setminus J}\frac{n_j}{n_j+2},\quad
\operatorname{Var}(\overline Z_{J,m})=
\frac{\mathbb E Z_J^2-(\operatorname{tr}H)^2}{m}.
\]

The second-moment identity follows from \(\mathbb E(R_j^2/n_j)^2=1+2/n_j\); it is independent of the geometry of \(H\).

**2. Positivity of the geometric constant.** The unit-sphere product is compact, so \(q\) attains its maximum \(\rho(H)\). Positive semidefiniteness gives \(q\ge0\), while \(\mathbb E q(U)=\operatorname{tr}H/N>0\); hence \(0<\rho(H)\le\|H\|_2\). Every spherical neighborhood of any maximizer has positive probability.

**3. Sharp upper tail with remaining Gaussian modes.** Let \(r=d-|J|\ge1\) and \(c=c_J\). For sample \(\ell\), put \(s_\ell=\sum_{j\notin J}R_{\ell,j}^2\). The arithmetic-geometric mean inequality gives \(\prod_{j\notin J}R_{\ell,j}^2\le(s_\ell/r)^r\). Since \(q\le\rho(H)\), and \(\sum_\ell s_\ell^r\le(\sum_\ell s_\ell)^r\),

\[
\overline Z_{J,m}\le
\frac{c\rho(H)}{mr^r}\,T^r,
\qquad T=\sum_{\ell=1}^m\sum_{j\notin J}R_{\ell,j}^2
\sim\chi^2_{m\sum_{j\notin J}n_j}.
\]

Therefore \(\{\overline Z_{J,m}>t\}\) implies \(T>r(mt/(c\rho(H)))^{1/r}\). The elementary chi-square tail limit \(\lim_{x\to\infty}x^{-1}\log\Pr(\chi^2_\nu>x)=-1/2\), valid for every fixed positive integer \(\nu\), gives the desired upper logarithmic bound.

For the matching lower bound, fix \(0<\varepsilon<\rho(H)\). In sample \(\ell=1\), insist that the direction tuple belongs to the positive-probability open set \(\{q>\rho(H)-\varepsilon\}\), and each of its \(r\) remaining squared Gaussian radii exceeds \(b_t=(mt/[c(\rho(H)-\varepsilon)])^{1/r}\). Then \(Z_{J,1}>mt\); the other samples contribute nonnegative terms, so \(\overline Z_{J,m}>t\). Independence and the same chi-square tail limit yield

\[
\liminf_{t\to\infty}t^{-1/r}\log\Pr\{\overline Z_{J,m}>t\}
\ge-\frac r2\left(\frac{m}{c(\rho(H)-\varepsilon)}\right)^{1/r}.
\]

Let \(\varepsilon\downarrow0\). This matches the upper bound and proves the displayed exact constant for every \(r\ge1\), without a moment approximation or an unverified numerical extremum.

**4. Exponential-integrability transition and full normalization.** For \(r\ge2\), the proved logarithmic asymptotic has power \(1/r<1\), implying \(\mathbb E e^{\theta\overline Z_{J,m}}=\infty\) for every \(\theta>0\). For \(r=1\), the same upper bound is \(\overline Z_{J,m}\le (c\rho(H)/m)T\), so the chi-square moment generating function is finite whenever \(0<\theta<m/[2c\rho(H)]\); the sharp tail implies divergence for \(\theta>m/[2c\rho(H)]\). No assertion is made at equality. For \(r=0\), \(\overline Z_{J,m}=\left(\prod_jn_j\right)m^{-1}\sum_\ell q(U_\ell)\) is bounded above by \(\left(\prod_jn_j\right)\rho(H)\), with equality at its essential supremum by full angular support.

## Verification
Run `python3 verify.py` using the standard library. The script evaluates fourth-coordinate-moment tensor contractions in exact rational arithmetic and checks 52 equalities across identity matrices, rank-one positive-semidefinite matrices, and two- and three-factor tensor systems. These tests independently confirm the moment normalization formula. The infinite-tail formula is established by the two-sided chi-square comparison above, not by the finite checks.

For \(d=2\), \(n_1=n_2=2\), and \(H=I_4\), all-Gaussian probes have \(\mathbb E Z^2=64\) and \(\log\Pr(Z>t)\sim-\sqrt t\). Normalizing one factor gives \(Z=2\chi^2_2\) with \(\mathbb E Z^2=32\) and \(\log\Pr(Z>t)=-t/4\). Normalizing both gives \(Z=4\) exactly, with second moment \(16\).

For the rank-one projector onto \((e_1\otimes e_1+e_2\otimes e_2)/\sqrt2\), the product-state radius is \(\rho(H)=1/2\) although \(\|H\|_2=1\). The exact second moments are \(6\), \(3\), and \(3/2\) for zero, one, and two normalized factors respectively. This example demonstrates the necessity of the product-state numerical radius, not merely the ordinary spectral norm, in the sharp tail constant.

## Relationship to prior work
Bujanović and Kressner [1] introduced Gaussian and Rademacher rank-one norm/trace estimators and analyzed probability bounds, including the heavy right-tail obstruction. Meyer and Avron [2] derived exact variances for all-Gaussian product probes and for all-spherical product probes, using the same Gaussian radial decomposition; neither full-normalization variance reduction nor this decomposition is claimed as new. The present result instead addresses *every intermediate subset* of normalized factors, its convex-order structure, and the exact matrix-dependent logarithmic tail constant and exponential-moment transition. Chen, Sun and Xi [3] examine tensor-product Gaussian Frobenius-norm probes and moments but not this intermediate-normalization tail ladder. Classical Gaussian-chaos and large-deviation theory gives related stretched-exponential scales; the specialized exact product-state constant and conditional design comparison are the proposed distinction, not a claim to invent the general tail method.

## Limitations
The analysis assumes a finite-dimensional **real** nonzero positive-semidefinite matrix, Gaussian factors, independent probes, and a fixed sample count. No statement about indefinite trace estimators, complex probes, arbitrary non-Gaussian factors, or dimension-uniform concentration follows. Computing \(\rho(H)\) may itself be difficult for a general matrix accessible only through Kronecker products; the theorem identifies the exact mathematical coefficient, not a polynomial-time algorithm to obtain it. The logarithmic asymptotic does not supply a finite-threshold error bound or a prefactor. The boundary exponential moment for one remaining Gaussian factor is not classified. Literature precedence, especially consequences of general homogeneous-Gaussian-function large deviation principles, remains a risk requiring independent specialist assessment.

## References
[1] Z. Bujanović and D. Kressner, *Norm and trace estimation with random rank-one vectors*, arXiv:2004.06433v1 (first public 2020-04-14), https://arxiv.org/abs/2004.06433. Later SIAM J. Matrix Anal. Appl. 42 (2021), 202–223, DOI:10.1137/20M1331718, primary MSC 65F35.

[2] R. A. Meyer and H. Avron, *Hutchinson's Estimator Is Bad at Kronecker-Trace-Estimation*, arXiv:2309.04952v1 (first public 2023-09-10), https://arxiv.org/abs/2309.04952. Sections 1.2 and 3.2, Corollary 3.

[3] Y. Chen, F. Sun and H. Xi, *Quaternion Gaussian Probes for Tensor Frobenius-Norm Estimation*, arXiv:2610.12534v1 (2026), https://arxiv.org/abs/2610.12534. Studied as contemporary literature, not used to date the motivating source.
