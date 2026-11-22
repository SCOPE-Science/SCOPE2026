# Two-moment universality and sharp spectral islands for radial harmonic Toeplitz quadratics

## Finding
Let \(\mu\) be any rotationally invariant Borel probability measure on the closed unit disk whose radial squared-modulus distribution is not a point mass and whose support reaches radius one. Define \(m_j=\int |z|^{2j}\,d\mu(z)\), \(j\ge0\), and \(\rho=m_2/m_1^2>1\). Let \(H_\mu\) be the closure in \(L^2(\mu)\) of the complex harmonic polynomials, \(P_\mu\) its orthogonal projection, and \(T_p=P_\mu M_p|_{H_\mu}\).

For every analytic quadratic \(p(z)=a z^2+b z+c\) with complex \(a\ne0\), set \(t=b/a\). Its *complete* operator spectrum is
\[
\sigma(T_p)=p(\mathbb T)\cup
\begin{cases}
\{c-a\rho t^2/(1+\rho)^2\},&1+1/\rho<|t|<1+\rho,\\
\varnothing,&\text{otherwise},
\end{cases}
\]
where \(\mathbb T=\{z\in\mathbb C:|z|=1\}\). In the open interval the extra point is an isolated eigenvalue of algebraic multiplicity one. There is no additional off-curve spectrum even when the essential curve self-intersects. In particular **every two such radial measures with the same \(m_2/m_1^2\) have identical spectra for every analytic quadratic**, even if their remaining moments and supports differ.

For the standard beta-weighted area measure \(d\mu_\alpha=(\alpha+1)(1-|z|^2)^\alpha dA\), \(\alpha>-1\), the sharp coefficient window is
\[
1+\frac{\alpha+3}{2(\alpha+2)}<|b/a|<1+\frac{2(\alpha+2)}{\alpha+3}.
\]
The quadratic \(p(z)=z^2+\tfrac52z\) has no isolated spectral point at \(\alpha=0\), but has the simple isolated eigenvalue \(-375/256\) at \(\alpha=3\). Conversely, ordinary normalized area measure and the singular rotational measure consisting of \(1/4\) mass at the origin and \(3/4\) normalized angular mass on the unit circle are spectrally indistinguishable by *all* such quadratic compressions: both have \(\rho=4/3\).

## Assumptions and scope
The radial support condition is \(\sup\{|z|:z\in\operatorname{supp}\mu\}=1\); \(\mu\) may be absolutely continuous, singular, or have atoms. The non-point-mass hypothesis refers to the distribution of \(|z|^2\), ensuring strict \(m_2>m_1^2\). For each \(j\ge0\) let \(e_j=z^j/\sqrt{m_j}\), and for each \(j\ge1\) let \(e_{-j}=\bar z^j/\sqrt{m_j}\). These form an orthonormal basis of \(H_\mu\). If \(a=0\), the separate linear-symbol formula is \(\sigma(T_{bz+c})=c+b\mathbb T\). If the radial distribution is a point mass at radius one, the defect vanishes and the quadratic spectrum is simply its boundary curve; that degenerate case is excluded from the strict-window assertion. No assertion is made for polynomials of degree at least three or nonanalytic symbols.

## Proof
**Moment shift and its spectrum.** For \(S=T_z\), angular orthogonality gives the bilateral weighted shift \(S e_j=w_j e_{j+1}\) with
\[
w_j=\begin{cases}\sqrt{m_{j+1}/m_j},&j\ge0,\\
\sqrt{m_{-j}/m_{-j-1}},&j\le-1.
\end{cases}
\]
The radial-moment ratios \(m_{j+1}/m_j\) increase to one: their monotonicity is Cauchy--Schwarz, and their limit equals the right endpoint of the radial support (here one). Thus \(w_j\to1\) at both ends, so \(S\) is a compact perturbation of the bilateral unitary shift. All weights are strictly positive and bounded away from zero, hence \(S\) is invertible. Off the unit circle the compact-perturbation Fredholm index is zero. The eigenvector recurrence \(x_{j+1}=w_jx_j/\lambda\) excludes a nonzero square-summable eigenvector for \(|\lambda|<1\) by growth at \(+\infty\), and for \(|\lambda|>1\) by growth at \(-\infty\). Consequently \(\sigma(S)=\sigma_{\mathrm e}(S)=\mathbb T\), and \(\sigma(q(S))=q(\mathbb T)\) for every polynomial \(q\).

**Single defect.** Direct projection onto the harmonic Fourier basis gives \(T_{z^2}e_j=S^2e_j\) for every \(j\ne-1\), while
\[
T_{z^2}e_{-1}=\frac{m_2}{m_1}e_1,\qquad S^2e_{-1}=m_1e_1.
\]
Set \(\delta=m_2/m_1-m_1=m_1(\rho-1)>0\), and let \(E_{1,-1}x=\langle x,e_{-1}\rangle e_1\). Then
\[
T_p=a\bigl(S^2+tS+\delta E_{1,-1}\bigr)+cI.
\]
Therefore its essential spectrum is \(p(\mathbb T)\), and every point outside that curve is governed by a rank-one Fredholm determinant.

**Resolvent matrix coefficient.** Normalize \(a=1,c=0\), and write \(q(z)=z^2+tz\). For \(\lambda\notin q(\mathbb T)\), let \(u,v\) be the roots of \(z^2+tz-\lambda\), with multiplicity. For any \(s\notin\mathbb T\), the geometric resolvent expansions yield
\[
\langle (S-sI)^{-1}e_1,e_{-1}\rangle=
\begin{cases}s/m_1,&|s|<1,\\0,&|s|>1.
\end{cases}
\]
Indeed among the negative powers only \(S^{-2}e_1=e_{-1}/m_1\) contributes; no nonnegative power connects those basis positions. For distinct roots, partial fractions give
\[
\langle(q(S)-\lambda I)^{-1}e_1,e_{-1}\rangle
=\frac{g(u)-g(v)}{u-v},\quad
 g(s)=\begin{cases}s/m_1,&|s|<1,\\0,&|s|>1.
 \end{cases}
\]
If both roots lie outside, this equals zero; if both lie inside, it equals \(1/m_1\). The corresponding values for repeated roots follow by differentiation. The rank-one invertibility condition is
\[
F(\lambda)=1+\delta\langle(q(S)-\lambda I)^{-1}e_1,e_{-1}\rangle\ne0.
\]
Thus outside the mixed-root case \(F\) is either \(1\) or \(\rho\), hence never zero.

**Unique mixed-root zero and multiplicity.** Label the inside root \(u\) and outside root \(v\). Then
\[
F(\lambda)=1+(\rho-1)\frac{u}{u-v},
\]
so \(F=0\) precisely when \(v=\rho u\). Vieta's formula \(u+v=-t\) forces \(u=-t/(1+\rho)\), \(v=-\rho t/(1+\rho)\), and \(\lambda=-\rho t^2/(1+\rho)^2\). The strict location conditions \(|u|<1<|v|\) are equivalent to \(1+1/\rho<|t|<1+\rho\). This determines exactly one off-curve spectral point. When this interval holds, both roots are distinct and \(t\ne0\). Differentiating the root equations gives \(u'=1/(u-v)\), \(v'=-1/(u-v)\), hence
\[
F'(\lambda)=(\rho-1)\frac{t}{(u-v)^3}\ne0.
\]
The rank-one resolvent formula therefore has a simple pole and the isolated eigenvalue has algebraic multiplicity one. Restoring \(a,b,c\) proves the theorem.

**Two-moment consequences.** The formula depends on \(\mu\) only through \(\rho\). For the beta family, \(m_1=1/(\alpha+2)\) and \(m_2=2/((\alpha+2)(\alpha+3))\), so \(\rho=2(\alpha+2)/(\alpha+3)\). Substitution yields the displayed sharp window and concrete \(\alpha=0,3\) example. The singular two-radius measure has \(m_j=3/4\) for every \(j\ge1\), so \(\rho=(3/4)/(3/4)^2=4/3\), just as normalized area measure with \(m_1=1/2,m_2=1/3\).

## Verification
The proof is self-contained after standard moment log-convexity, bilateral-shift spectral facts, and the rank-one resolvent identity. Run `python3 verify.py` using the Python 3 standard library. It checks exact finite Fourier projection identities, the root-location/determinant algebra, two moment-isospectral measures, and the distinct beta-weighted phase example using rational arithmetic. Its output is `RADIAL_QUADRATIC_CHECK_OK 2182`. These finite checks do not establish an infinite-dimensional spectral theorem; the Fredholm argument and complete classification of root configurations do.

## Relationship to prior work
Huang, Wang and Zhao, *The spectral structure of Toeplitz operators with polynomial symbols on the harmonic Bergman space* (arXiv:2610.09638v1, first public October 7, 2026), establish the finite-outlier spectral structure for the **unweighted** harmonic Bergman space and recall Wang--Zhao's 2021 quadratic disconnected-spectrum example. In particular, the case \(m_j=1/(j+1)\), \(\rho=4/3\) is **prior knowledge**, not a new quadratic classification. Subsequent quantitative unweighted quadratic spectral-island and Riesz-projection reports likewise treat that same fixed area measure. The contribution here is the exact theorem for arbitrary radial measures, the collapse of the entire quadratic spectral classification to the first two radial moments, and the explicit weight-induced creation of an isolated eigenvalue. The unweighted determinant criteria do not themselves imply independence from all higher radial moments.

Sadraoui and Halouani (2024) study commuting Toeplitz operators on standard weighted harmonic Bergman spaces, rather than quadratic spectra. Wang and Zhao (2018) treat nonnegative-symbol boundedness, compactness and Schatten classes on weighted harmonic Bergman spaces; their setting does not provide the present complex analytic quadratic spectral-island law. The full 2021 Wang--Zhao article was not available in the comparison, so an older equivalent weighted statement remains a bibliographic risk.

## Limitations
The results concern closed harmonic-polynomial subspaces for rotationally invariant probability measures with radial support reaching the circle. They need not hold for nonradial measures or higher polynomial degrees. No spectral-projection norm or pseudospectral estimate is asserted. The case of a radial point mass is excluded. The spectral-island formula is exact, but publication priority for all radial measures has not been independently established; older uninspected weighted sources may affect originality. No independent mathematical audit has been performed.

## References
1. M. Huang, J. Wang and X. Zhao, *The spectral structure of Toeplitz operators with polynomial symbols on the harmonic Bergman space*, arXiv:2610.09638v1 (first public October 7, 2026), Theorem 3.1 and proof. https://arxiv.org/abs/2610.09638
2. C. Wang and X. Zhao, *Weyl's theorem for Toeplitz operators with polynomial symbols on the harmonic Bergman space*, J. Math. Anal. Appl. 495 (2021), 124770. https://doi.org/10.1016/j.jmaa.2020.124770
3. H. Sadraoui and B. Halouani, *Commuting Toeplitz operators on weighted harmonic Bergman spaces and hyponormality on the Bergman space of the punctured unit disk*, AIMS Mathematics 9 (2024), 20043--20057. https://doi.org/10.3934/math.2024977
4. Z. Wang and X. Zhao, *Toeplitz operators on weighted harmonic Bergman spaces*, Banach J. Math. Anal. 12 (2018), 808--842; earlier open preprint arXiv:1603.06085. https://arxiv.org/abs/1603.06085
