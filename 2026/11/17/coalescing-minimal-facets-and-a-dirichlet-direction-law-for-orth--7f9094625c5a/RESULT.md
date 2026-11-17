# Coalescing minimal facets and a Dirichlet direction law for orthotope hyperplane shadows

## Finding

Fix an integer \(d\ge4\). Let \(K=\prod_{j=1}^d[0,a_j]\subset\mathbb R^d\), with all \(a_j>0\). For a Haar-uniform unit normal \(U\) let \(B_K(U)\) be the \((d-1)\)-dimensional volume of the orthogonal shadow on \(U^\perp\). Define \(w_i=\prod_{j\ne i}a_j\), \(m=\min_i w_i\), \(I=\{i:w_i=m\}\), and \(s_{d-1}=2\pi^{d/2}/\Gamma(d/2)\). Then \(B_K(U)=\sum_iw_i|U_i|\), and its minimum equals \(m\). For a **fixed** orthotope, as \(t\downarrow0\),
\[
\Pr\{B_K<m+t\}=\frac{2^d t^{d-1}}{s_{d-1}(d-1)!}
\sum_{i\in I}\frac{1}{\prod_{j\ne i}w_j}
\left[1+\frac{mt}{d}\sum_{j\ne i}\frac1{w_j^2}+O_K(t^2)\right].\tag{1}
\]
The **main conditional result** permits genuinely competing, nearly minimal facets. For every \(t>0\) let an orthotope have positive face weights \(w_j(t)\), satisfying \(w_j(t)=w_j^0+\lambda_jt+o(t)\) as \(t\downarrow0\), for fixed \(w_j^0>0\) and real \(\lambda_j\). Set \(m_0=\min_jw_j^0\), \(I_0=\{j:w_j^0=m_0\}\), \(p=d-1\), and assume at least one \(i\in I_0\) has \(\lambda_i<1\). Then
\[
\lim_{t\downarrow0}t^{-p}\Pr\{B_{K(t)}(U)<m_0+t\}
=\frac{2^d}{s_{d-1}p!}\sum_{i\in I_0}
\frac{(1-\lambda_i)_+^p}{\prod_{j\ne i}w_j^0},\tag{2}
\]
where \(z_+=\max(z,0)\). On this rare event label \(J\) the index of largest \(|U_i|\), uniquely almost surely. Conditional on \(J=i\), for any \(\lambda_i<1\), the full vector \((U_j/t)_{j\ne i}\) converges **in total variation** to uniform Lebesgue probability measure on the weighted crosspolytope
\[
T_i=\left\{y\in\mathbb R^p:\sum_{j\ne i}w_j^0|y_j|<1-\lambda_i\right\}.\tag{3}
\]
The limiting label probabilities are proportional to \((1-\lambda_i)_+^p/\prod_{j\ne i}w_j^0\), with labels outside \(I_0\) receiving zero. Given an active label, its axial sign and all tangent signs tend jointly to independent fair signs, independent of the unsigned coordinates. If \(Y\) has the law in (3), then the \(d\)-component vector
\[
\left(\frac{w_j^0|Y_j|}{1-\lambda_i}\right)_{j\ne i}
\quad\text{together with}\quad
1-\frac{\sum_{j\ne i}w_j^0|Y_j|}{1-\lambda_i}
\]
has exactly the \(\operatorname{Dirichlet}(1,\ldots,1)\) law. Equivalently, the proportion of the normalized budget used is \(\operatorname{Beta}(d-1,1)\), independently of the fair signs. These joint limits hold in total variation for the canonically labelled marked observations.

In dimension \(d=4\), the face weights \(w(t)=(1,1+\alpha t,c,c)\) for any \(c>1\), \(\alpha\ge0\), arise from actual four-dimensional orthotopes. At threshold \(1+t\),
\[
\lim_{t\downarrow0}t^{-3}\Pr\{B_{K(t)}<1+t\}
=\frac{4}{3\pi^2c^2}\left[1+(1-\alpha)_+^3\right].\tag{4}
\]
Thus the competing minimum switches off exactly at \(\alpha=1\), with a cubic (rather than an artificial piecewise choice) phase law and a corresponding sharp transition in the conditional direction mixture.

## Assumptions and scope

All statements concern fixed finite \(d\ge4\) and uniformly random oriented hyperplanes through the origin, with normal distributed according to normalized spherical surface area. Shadows are \((d-1)\)-dimensional Euclidean volumes; they are not line widths in a projected plane. We assume strictly positive side lengths for each \(t\), and in (2) weights approach strictly positive limits; all \(o(t)\) are for the finitely many coordinates simultaneously. Every positive weight vector is realized by a unique orthotope side vector: put \(V=(\prod_jw_j)^{1/(d-1)}\) and \(a_j=V/w_j\). The strict inequalities may be replaced by nonstrict ones without affecting probabilities. There is no claim of a uniform remainder as the limiting weights approach zero or as dimension grows.

The scalar full-width law in dimension three and the high-tail spherical-cap laws of boxes are established prior work and are not claimed here. The new target is the **near-minimum, dimension-at-least-four, marked critical-window law** and its quantitative fixed-shape expansion.

## Proof

**Projection identity and localization.** Cauchy's projection formula, or direct decomposition into the box's mutually opposite facets, gives \(B_K(U)=\sum_iw_i|U_i|\). Since \(\|U\|_1\ge\|U\|_2=1\), \(B_K(U)\ge m\). Equality occurs precisely at the finitely many poles \(\pm e_i\) with \(i\in I\). By compactness, the event \(B_K<m+t\) lies in disjoint small neighborhoods of these poles once \(t\) is small. The same statement holds uniformly for \(w(t)\to w^0\) with the poles indexed by \(I_0\); any indices outside \(I_0\) are separated by a positive fixed gap.

**Local surface coordinates.** Near either sign of pole \(e_i\), write \(U_i=\pm\sqrt{1-|x|^2}\), \(U_j=x_j\) for \(j\ne i\), \(x\in\mathbb R^{d-1}\). The normalized spherical measure has density \((s_{d-1}\sqrt{1-|x|^2})^{-1}\,dx\). In the fixed-shape case,
\[
B_K=m+\sum_{j\ne i}w_j|x_j|-\tfrac m2|x|^2+O_K(|x|^4).
\]
The event forces \(x=O_K(t)\). This follows first from the nonnegative linear term and the bound \(1-\sqrt{1-r^2}\le r^2\), using a sufficiently small fixed chart, which yields a linear lower bound in \(|x|\). Write \(x=ty\). The limiting region in each tangent chart is the weighted \(\ell_1\) ball \(\sum_{j\ne i}w_j|y_j|<1\), of Euclidean volume \(2^{d-1}/((d-1)!\prod_{j\ne i}w_j)\). There are two pole signs. This establishes the leading term in (1).

**Second-order fixed-shape coefficient.** Put \(p=d-1\) and in each tangential orthant write \(x_j=(t/w_j)r z_j\) with \(z_j\ge0\), \(\sum_{j\ne i}z_j=1\). The boundary equation for the rare event becomes
\[
r+\frac mt\biggl(\sqrt{1-t^2r^2\sum_{j\ne i}z_j^2/w_j^2}-1\biggr)=1.
\]
For all simplex parameters, its unique small positive root satisfies uniformly
\[
r_{\max}=1+\frac{mt}{2}\sum_{j\ne i}\frac{z_j^2}{w_j^2}+O_K(t^2).
\]
The surface Jacobian differs from one by \(O_K(t^2)\). Uniform measure on the simplex parameters \(z\) has \(\mathbb Ez_j^2=2/[p(p+1)]\). The radial integral gives \(r_{\max}^p\), so its first relative correction is \(p(mt/2)\,2/[p(p+1)]\sum w_j^{-2}=mt\sum w_j^{-2}/d\). The expansion is uniform on the compact parameter simplex and may be integrated term by term. Summing all active poles proves (1), including multiplicities.

**Competing minima and total-variation convergence.** For \(w(t)=w^0+\lambda t+o(t)\) and \(i\in I_0\), use the same local chart and \(x=ty\). Uniformly for \(y\) in every bounded region,
\[
\frac{B_{K(t)}-m_0}{t}=\lambda_i+\sum_{j\ne i}w_j^0|y_j|+o(1).
\]
All possible conditional \(y\) lie in a common compact set, because the strictly positive limiting weights give a fixed local linear lower bound. The rescaled unnormalized density for each pole is \(t^p[s_{d-1}\sqrt{1-t^2|y|^2}]^{-1}\) times the indicator of this inequality. It converges pointwise almost everywhere and in \(L^1(dy)\) to \(t^p/s_{d-1}\) times the indicator of (3). The boundary of the crosspolytope has Lebesgue measure zero; when \(\lambda_i\ge1\), the limiting region is empty. Summing the \(2d\) disjoint charts proves (2). Normalizing a finite mixture of these \(L^1\)-convergent densities by its strictly positive total mass establishes total-variation convergence, both for each active component and jointly with the discrete label and pole sign. Invariance under tangent coordinate sign reversals proves the independent fair signs.

**Dirichlet law and crossover.** A uniform point of a weighted crosspolytope has uniform signs and, after multiplying absolute coordinates by their weights and dividing by the budget, uniform Lebesgue measure on \(\{z_j\ge0:\sum z_j<1\}\). Its first \(p\) coordinates together with their slack have constant density \(p!\) on the standard \(p\)-simplex: this is exactly \(\operatorname{Dirichlet}(1,\ldots,1)\). The sum of the first \(p\) components is \(\operatorname{Beta}(p,1)\). In dimension four, substitute \(w^0=(1,1,c,c)\), \(\lambda_1=0\), \(\lambda_2=\alpha\) into (2), using \(s_3=2\pi^2\), to obtain (4). Every displayed weight vector is physically realized by the positive side lengths in the scope statement. This completes the proof.

## Verification

The standalone `check_brightness.py` independently simulates uniformly directed shadows, uses local surface-Jacobian importance integration for rare events, and compares the measured probabilities with the two-term fixed-shape and competing-facet formulas for dimensions at least four. It also checks normalized simplex-budget moments against their Dirichlet limits. Execute `python3 check_brightness.py` after installing `numpy` and `scipy` from `requirements.txt`. The output marker is `ORTHOTOPE_MINIMUM_SHADOW_PHASE_OK`. All numerical tests are finite diagnostics; the universal statements follow from the proof, not the simulation.

## Relationship to prior work

Paouris–Pivovarov–Zinn (2012) study Gaussian fluctuations of cube projections with fixed projected dimension and ambient dimension tending to infinity. Their full text provides a different asymptotic regime and does not assert the fixed-dimensional, moving-aspect-ratio conditional law (2)–(3). Kabluchko–Litvak–Zaporozhets (2015) give moment machinery for regular-polytope widths; their regular-cube moment implications are acknowledged and not treated as new.

The full publicly available reports *Exact directional width law of the cube and its first spherical-cap transition* (2026) and *First spherical-cap width transitions of anisotropic orthotopes in dimension four and higher* (2026) were inspected in full. Both concern the opposite, near-**maximum** endpoint. The first also gives the entire three-dimensional cube width density; it cannot be used to claim that scalar cube endpoint values are new. The second explicitly restricts its new analysis to the first **upper** spherical-cap crossing and does not derive marked near-minimum mixtures.

Abas, *Width distributions for rectangular boxes* (2026), reports that Walters previously derived the complete three-dimensional rectangular-box projected-area distribution; hence no such three-dimensional scalar law is claimed here. Abas's *Width Laws and Spectral Geometry* (2026) gives all-dimensional moments and side reconstruction; the abstract does not state the orientation-marked joint total-variation law for degenerating weights, although its full content could contain relevant broader coverage. The fully explicit near-minimum marked mixture and sharp moving-facet crossover, not an assertion that the scalar law is unavailable in principle, is the contribution considered here.

## Limitations

The signed normal direction is measured relative to the box's known labelled facet normals; if those labels are unavailable, only the unlabeled mixture is observable. The limit concerns near-minimum shadows for fixed dimension and strictly positive limiting face weights, not degenerations where a box side vanishes. It gives a conditional asymptotic—not an exact finite-threshold law—and does not provide convergence rates under merely \(o(t)\) weight perturbations. Formula (1) has a fixed-shape \(O_K(t^2)\) relative remainder but no uniformity when facet gaps vary at the critical scale. The full text of the modern boxed-width papers and Walters's original derivation was not accessible for line-by-line examination; these create residual historical-priority uncertainty. No independent scientific validation is asserted.

## References

1. G. Paouris, P. Pivovarov, J. Zinn, *A central limit theorem for projections of the cube*, arXiv:1210.7012, first publicly posted 2012-10-25, https://arxiv.org/abs/1210.7012.
2. Z. Kabluchko, A. E. Litvak, D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479, first posted 2015-11-26, https://arxiv.org/abs/1511.08479.
3. O. Abas, *Width distributions for rectangular boxes*, arXiv:2608.03305, first posted 2026-08-04, https://arxiv.org/abs/2608.03305.
4. O. Abas, *Width Laws and Spectral Geometry*, arXiv:2608.06348, first posted 2026-08-06, https://arxiv.org/abs/2608.06348.
5. *Exact directional width law of the cube and its first spherical-cap transition*, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-exact-directional-width-law-of-the-cube-and-its-first-spherical--c1e6aa54ecb2/RESULT.md.
6. *First spherical-cap width transitions of anisotropic orthotopes in dimension four and higher*, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-first-spherical-cap-width-transitions-of-anisotropic-orthotopes--b4261bcc2c93/RESULT.md.
