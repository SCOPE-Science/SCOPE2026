# Exact Weyl constant for coordinate Hankel operators on radial power Fock spaces in several variables

## Finding

Fix an integer \(d\ge2\) and a real \(m>1\). In the weighted Fock space
\[
\mathcal F^2_{m,d}=\left\{f\in\mathrm{Hol}(\mathbb C^d):\int_{\mathbb C^d}|f(z)|^2e^{-\|z\|^{2m}}\,dV(z)<\infty\right\},
\]
write \(P\) for orthogonal projection and \(H=(I-P)M_{\overline z_1}\) for the anti-holomorphic coordinate Hankel operator, initially on holomorphic polynomials. Let \(s_k(H)\) denote its singular values in nonincreasing order, with \(k\ge1\). Define
\[
q=\frac{m-1}{m},\qquad p_c=\frac{2d}{q},\qquad
C_{m,d}=\frac{m^{-d/(m-1)}}{d!}(d-1)\int_0^1(1-t)^{d-2}(1-qt)^{d/q}\,dt.
\]
**Theorem.** The operator \(H\) extends uniquely to a bounded compact operator. The exact counting asymptotic is
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{p_c}\#\{k:s_k(H)>\varepsilon\}=C_{m,d}>0.
\]
Equivalently, \(s_k(H)\sim(C_{m,d}/k)^{1/p_c}\). Therefore \(H\) lies in the weak Schatten ideal \(\mathcal S_{p_c,\infty}\) but not in \(\mathcal S_{p_c}\), while the positive operator \(|H|^{p_c}\) is Dixmier measurable: every Dixmier trace equals \(C_{m,d}\). The coefficient is an angular average over a simplex, not simply the dimension-counting volume. For the quartic weight in two complex variables,
\[
(m,d)=(2,2),\qquad p_c=8,\qquad C_{2,2}=\frac{31}{640}.
\]

## Assumptions and scope

Complex dimension \(d\) is any fixed integer at least two; real exponent \(m>1\) is fixed as \(\varepsilon\downarrow0\). The ambient volume \(dV\) is ordinary Euclidean Lebesgue measure on \(\mathbb C^d\); multiplying the measure by a positive global constant changes neither \(H\) nor its singular values. The symbol is the coordinate anti-holomorphic function \(\overline z_1\), with other coordinates equivalent by unitary invariance. Weak Schatten \(\mathcal S_{p,\infty}\) means \(\sup_{k\ge1}k^{1/p}s_k<\infty\). For a positive compact operator in the Dixmier class, its Dixmier trace agrees with the logarithmic singular-value Cesàro limit when that limit exists. No assertion is made at \(m=1\), or for general symbols or general radial weights.

## Proof

**1. Exact orthogonal monomial computation.** For a multi-index \(\alpha\in\mathbb N_0^d\), let \(n=|\alpha|\) and \(\alpha!=\prod_{j=1}^d\alpha_j!\). Spherical beta integration followed by the radial gamma integral gives the exact norm
\[
\|z^\alpha\|^2=\frac{\pi^d}{m}\frac{\alpha!\,\Gamma((n+d)/m)}{\Gamma(n+d)}.
\]
Put \(r_n=\Gamma((n+d+1)/m)/((n+d)\Gamma((n+d)/m))\), for \(n\ge0\). Since monomials form an orthogonal basis, \(P(\overline z_1z^\alpha)=0\) when \(\alpha_1=0\), and otherwise it equals \(\|z^\alpha\|^2z^{\alpha-e_1}/\|z^{\alpha-e_1}\|^2\). Both \(T_{|z_1|^2}\) and \(T_{z_1}T_{\overline z_1}\) are diagonal on monomials. Their difference is \(H^*H\). Consequently each normalized \(z^\alpha\) is an eigenvector of \(H^*H\) with exact eigenvalue
\[
\lambda_\alpha=(\alpha_1+1)r_n-\mathbf 1_{\{\alpha_1\ge1\}}\alpha_1r_{n-1}.
\]
All eigenvalues are strictly positive because \(\overline z_1 z^\alpha\) is not holomorphic and hence has nonzero orthogonal projection to the complement. These eigenvalues are precisely the squared singular values, including multiplicities.

**2. Uniform spectral scale.** Let \(q=(m-1)/m\in(0,1)\). The standard gamma-ratio expansion at fixed \(m,d\) yields
\[
r_n=m^{-1/m}n^{-q}\left(1-\frac{q(d+1/2)}{n}+O_{m,d}(n^{-2})\right),\qquad
r_n-r_{n-1}=-q\,m^{-1/m}n^{-q-1}+O_{m,d}(n^{-q-2}).
\]
As \(0\le\alpha_1\le n\), substitution into the exact eigenvalue formula is **uniform in the entire degree shell**:
\[
\lambda_\alpha=m^{-1/m}n^{-q}\left(1-q\frac{\alpha_1}{n}+O_{m,d}(n^{-1})\right),\qquad n\longrightarrow\infty.
\]
The angular factor lies in \([1/m,1]\), so the eigenvalues are positive and decrease to zero uniformly over degree shells. The diagonal operator \(H^*H\) is therefore bounded and compact; equivalently, the densely defined Hankel operator extends uniquely and compactly to the full space.

**3. Lattice-point Weyl limit.** Put \(h=\varepsilon^{2/q}\), and scale \(x=h\alpha\in[0,\infty)^d\). For \(x\ne0\), the rescaled spectral inequality \(\lambda_\alpha>\varepsilon^2\) tends to
\[
\sum_{j=1}^d x_j < R\!\left(\frac{x_1}{\sum_jx_j}\right),\qquad
R(t)=\left[m^{-1/m}(1-qt)\right]^{1/q}.
\]
Uniformity from Step 2 brackets the indicator sets, away from finitely many low-degree shells, between the corresponding regions with multiplicative radius errors tending to zero. The limiting region is bounded, its radial boundary has Lebesgue measure zero, and a small neighborhood of the origin has arbitrarily small volume. Hence the elementary lattice Riemann-sum theorem applies and gives
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{2d/q}\#\{\alpha:\lambda_\alpha>\varepsilon^2\}
=\operatorname{Vol}\{x\in[0,\infty)^d:\sum_jx_j<R(x_1/\sum_jx_j)\}.
\]
Writing \(x_j=su_j\), where \(u_j\ge0\) and \(\sum_j u_j=1\), gives the Jacobian \(s^{d-1}\) and
\[
\operatorname{Vol}=\frac1d\int_{\Delta_{d-1}}R(u_1)^d\,du_1\cdots du_{d-1}
=\frac1{d!}\mathbb E\left[R(U_1)^d\right],
\]
where \((U_1,\ldots,U_d)\) is uniform on the standard simplex and \(U_1\) has density \((d-1)(1-t)^{d-2}\) on \([0,1]\). Inserting \(R\) gives exactly \(C_{m,d}\), proving the claimed limit.

**4. Ideal endpoint and trace.** Monotonicity of the counting function and \(C_{m,d}>0\) invert the asymptotic to \(s_k(H)\sim(C_{m,d}/k)^{1/p_c}\). Thus \(\sup_k k^{1/p_c}s_k(H)<\infty\), while \(\sum_k s_k(H)^{p_c}\) diverges like \(C_{m,d}\log k\). In fact,
\[
\lim_{N\to\infty}\frac1{\log N}\sum_{k=1}^{N}s_k(H)^{p_c}=C_{m,d}.
\]
The limit proves measurability and determines every Dixmier trace of \(|H|^{p_c}\).

**5. Exact first multivariable coefficient.** For \(m=d=2\), \(q=1/2\). Then
\[
C_{2,2}=\frac18\int_0^1\left(1-\frac t2\right)^4dt=\frac18\cdot\frac{31}{80}=\frac{31}{640}.
\]
This exhibits an exact angular correction that is invisible to Schatten-threshold information alone. \(\square\)

## Verification

The accompanying standalone standard-library script `CHECKER.py` recomputes the exact monomial/gamma quotient eigenvalue formula at selected degrees, checks the uniform shell asymptotic numerically for three representative parameters, and evaluates the special quartic-weight integral by exact rational arithmetic. These calculations are reproducibility checks, **not** a substitute for the infinite-dimensional lattice limit proved above. The proof is fully analytic and has no external computational dependency.

## Relationship to prior work

Liu–Wang–Zeng (2026, arXiv:2609.26810, first public release 2026-09-16), with primary MSC2020 32A36, studies weighted Fock kernels, boundedness and compactness of Hankel operators in several variables; its sections on Hankel operators do not state this coordinate singular-value Weyl coefficient. Bommier-Hato–Youssfi (2007) already proves boundedness, compactness and the **sharp Schatten threshold** for polynomial anti-holomorphic symbols on exactly this family of radial power weights. That membership conclusion is known and is not claimed as new. Bommier-Hato–Constantin (2018) proves general vector-valued Fock boundedness/compactness/Schatten criteria; the inspected theorems use comparability/ideal membership, not a singular-value counting coefficient. Fan–Wang–Zeng (2024) characterizes singular-value rates up to two-sided comparability for weighted Bergman and one-variable Fock settings; the inspected full text does not give this exact higher-dimensional angular coefficient. Bommier-Hato–Engliš–Youssfi (2014) determines Dixmier classes and traces on the complex **plane**, and hence does not on its stated domain imply the formula for \(d\ge2\). The present contribution is the explicit \(d\)-dimensional **Weyl leading constant**, equivalently the precise critical logarithmic trace density, not the known order of decay.

## Limitations

The asymptotic is for a coordinate anti-holomorphic symbol and a fixed radial power weight, not a general anti-holomorphic symbol or all plurisubharmonic weights. It does not provide an error term uniform in \(d\) or \(m\). The 2007 source and 2014 source were available through abstracts and bibliographic descriptions but their full texts could not be retrieved through available lawful access; those remain priority risks for comparisons beyond their stated conclusions. The leading coefficient may be obtainable as an unstated corollary of an unidentified general trace theorem, so external independent priority review remains desirable. No independent audit has been performed.

## References

1. G. Liu, X. Wang, Z. Zeng, *Bergman Kernels and Hankel Operators on Weighted Fock Spaces in Several Complex Variables*, arXiv:2609.26810 (first public release 2026-09-16), https://arxiv.org/abs/2609.26810 .
2. H. Bommier-Hato, E.-H. Youssfi, *Hankel Operators on Weighted Fock Spaces*, Integral Equations and Operator Theory **59** (2007), 1–17, DOI 10.1007/s00020-007-1513-1.
3. H. Bommier-Hato, O. Constantin, *Big Hankel Operators on Vector-Valued Fock Spaces in \(\mathbb C^d\)*, Integral Equations and Operator Theory **90** (2018), article 2, DOI 10.1007/s00020-018-2433-y.
4. Z. Fan, X. Wang, Z. Zeng, *IDA Function and Asymptotic Behavior of Singular Values of Hankel Operators on Weighted Bergman Spaces*, arXiv:2410.20082 (first release 2024-10-26); Advances in Mathematics (2026).
5. H. Bommier-Hato, M. Engliš, E.-H. Youssfi, *Dixmier Classes on Generalized Segal–Bargmann–Fock Spaces*, Journal of Functional Analysis **266** (2014), 2096–2124, DOI 10.1016/j.jfa.2013.08.007.
