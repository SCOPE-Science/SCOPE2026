# Sharp finite-moment tomography of orthotopes in every dimension

## Finding

For every integer \(d\ge2\), let \(Q=\prod_{i=1}^d[-a_i/2,a_i/2]\subset\mathbb R^d\) be an orthotope with \(a_i>0\). Choose \(U\) uniformly on \(S^{d-1}\), and let \(B_Q(U)=\operatorname{Vol}_{d-1}(Q\mid U^\perp)\) be its orthogonal projection volume. Define the population moments \(m_k=\mathbb E[B_Q(U)^k]\) for positive integers \(k\).

**Finite determination and minimality.** Exactly the first \(d\) moments \(m_1,\ldots,m_d\) determine the unordered side-length list \(\{a_1,\ldots,a_d\}\), by the constructive inversion below. The first \(d-1\) moments do not determine the box: at every box with pairwise distinct facet areas there are continuously many nearby noncongruent boxes with all those moments equal.

**Sharp inverse stability.** Given \(0<\ell<L<\infty\), there is \(C_{d,\ell,L}<\infty\) such that for all two orthotopes \(Q,Q'\) with side lengths in \([\ell,L]\),

\[
\min_{\sigma\in S_d}\max_i |a_i-a'_{\sigma(i)}|
\le C_{d,\ell,L}\left(\max_{1\le k\le d}|m_k(Q)-m_k(Q')|\right)^{1/d}.
\]

The exponent \(1/d\) is optimal on every neighborhood of a cube. Where all facet areas are pairwise different, the inverse is locally Lipschitz.

The key fact permitting the exact all-dimensional inversion is that **every positive-order cumulant of the standard half-normal distribution is nonzero**. Here is an explicit proof, rather than an unverified generic nondegeneracy assumption.

## Assumptions and scope

All dimensions \(d\ge2\) are fixed finite integers; all side lengths are positive. Directions are Haar-uniform, the projected volume is the ordinary \((d-1)\)-dimensional Euclidean volume, and moments are exact distributional moments. Translation and orthogonal orientation are intentionally unidentifiable. Stability constants depend on dimension and the displayed compact positive side-length interval. There is no statement about empirical sampling errors or arbitrary non-orthogonal parallelotopes.

## Proof

**1. From projections to independent half-normals.** Put \(q_i=\prod_{j\ne i}a_j\). The Cauchy projection formula for the \(2d\) facets of an orthotope gives, for every unit vector \(U\),

\[
B_Q(U)=\sum_{i=1}^d q_i|U_i|.
\]

Every positive \(q\)-tuple corresponds to a unique positive side tuple, via

\[
a_i=\frac{(\prod_{j=1}^d q_j)^{1/(d-1)}}{q_i}.
\]

Let \(G_i\) be independent standard normal variables, let \(R=(\sum_iG_i^2)^{1/2}\), and let \(U=G/R\). The random variables \(R\) and \(U\) are independent, with \(U\) uniform on the sphere and \(\rho_{d,k}:=\mathbb E R^k=2^{k/2}\Gamma((d+k)/2)/\Gamma(d/2)\). Therefore

\[
H:=\sum_{i=1}^d q_i|G_i|=RB_Q(U),\qquad h_k:=\mathbb E H^k=\rho_{d,k}m_k.
\]

Thus the first \(d\) projection moments give exactly the first \(d\) raw moments of a weighted sum of independent half-normal random variables.

**2. All half-normal cumulants are nonzero.** For \(X=|G_1|\), its moment-generating function near zero is

\[
M_X(z)=e^{z^2/2}\bigl(1+\operatorname{erf}(z/\sqrt2)\bigr)
=e^{z^2/2}(1+tF(z)),\qquad t=\sqrt{2/\pi},
\]

where

\[
F(z)=\sum_{r=0}^\infty\frac{(-1)^r z^{2r+1}}{2^r r!(2r+1)}
=z+O(z^3)\in\mathbb Q[[z]].
\]

Let \(\kappa_k=k![z^k]\log M_X(z)\) be the cumulant of order \(k\ge1\). Since

\[
\log M_X(z)=\frac{z^2}{2}+
\sum_{j=1}^\infty\frac{(-1)^{j+1}}j t^j F(z)^j,
\]

\(\kappa_k\) is a polynomial in \(t\) with rational coefficients. Its top-degree coefficient is \((-1)^{k+1}(k-1)!\), coming from \(F(z)^k=z^k+O(z^{k+2})\), and is nonzero. The number \(t=\sqrt{2/\pi}\) is transcendental because \(\pi\) is transcendental; hence no nonzero polynomial over \(\mathbb Q\) can vanish at \(t\). Thus \(\kappa_k\ne0\) for **every** positive integer \(k\). This exact algebraic argument does not assume all cumulants have the same sign (they do not).

**3. Constructive inversion.** Define \(K_k\) as the order-\(k\) cumulant computed from \(h_1,\ldots,h_k\), using the standard moment–cumulant recursion

\[
K_k=h_k-\sum_{j=1}^{k-1}\binom{k-1}{j-1}K_jh_{k-j},\qquad h_0=1.
\]

Cumulants add for independent summands, and the \(k\)-th cumulant of \(q_iX\) is \(q_i^k\kappa_k\), so

\[
K_k=\kappa_k\sum_{i=1}^d q_i^k.
\]

By Step 2, the first \(d\) moments recover every power sum \(p_k:=\sum_iq_i^k=K_k/\kappa_k\) for \(1\le k\le d\). Newton's identities

\[
e_0=1,\qquad ke_k=\sum_{j=1}^k(-1)^{j-1}e_{k-j}p_j
\]

recover all elementary symmetric functions \(e_1,\ldots,e_d\). The \(d\) positive roots, with multiplicities, of

\[
z^d-e_1z^{d-1}+e_2z^{d-2}-\cdots+(-1)^d e_d
\]

are \(q_1,\ldots,q_d\), which recover the sides by Step 1. No orientation, translation, or order of the sides is required.

**4. Necessity of \(d\) moments.** Start with any distinct positive \(q_i\), and the simple-root polynomial \(P(z)=\prod_i(z-q_i)\). For every sufficiently small real \(\tau\), the polynomial \(P(z)+\tau\) has \(d\) positive real simple roots near those of \(P\), by continuous local inverse branches at its simple roots. Varying \(\tau\) changes only the constant coefficient. Consequently \(e_1,\ldots,e_{d-1}\), the first \(d-1\) power sums, the first \(d-1\) cumulants \(K_k\), and hence the first \(d-1\) projected-volume moments are all unchanged. The roots, and therefore the side lengths, do change. This gives continuous local counterfamilies wherever the facet areas are distinct.

**5. Quantitative stability.** Restrict \(a_i\in[\ell,L]\). Then \(q_i\in[\ell^{d-1},L^{d-1}]\). The finite algebraic recursions in Step 3, and the fact that all fixed \(\kappa_k\) are nonzero, imply that a moment discrepancy \(\delta\) changes every coefficient of the associated monic root polynomial by at most \(C_0\delta\), with \(C_0=C_0(d,\ell,L)\). On a common bounded complex disk the two monic polynomials thus differ by at most \(C_1\delta\).

For small \(\delta\), draw complex disks of radius \(r=(2C_1\delta)^{1/d}\) around the \(d\) roots of the first polynomial. At every boundary point of a connected component of their union, the modulus of that polynomial is at least \(r^d\), exceeding the difference of the two polynomials. Rouché's theorem ensures each component contains exactly as many roots of the second polynomial as of the first. Each component has diameter at most \(2dr\), so the root multisets can be matched within \(2dr\). Larger discrepancies follow after adjusting a constant, by compact boundedness. Finally the side-recovery map is Lipschitz on the positive compact cube, yielding the claimed exponent \(1/d\). When all roots are distinct, the root-to-coefficient Jacobian is a nonsingular Vandermonde matrix, hence local inverse Lipschitz continuity follows from the inverse function theorem.

**6. Optimal exponent at cubes.** Choose \(d\) distinct real numbers \(u_1,\ldots,u_d\) and let \(f(z)=\prod_i(z-u_i)\). For a sufficiently small nonzero constant \(\tau\), the polynomial \(f(z)+\tau\) has \(d\) distinct real roots \(v_1,\ldots,v_d\). The multisets \(u\) and \(v\) differ but their elementary symmetric functions through order \(d-1\) agree. For sufficiently small \(\varepsilon>0\), construct positive facet-area tuples

\[
q_i(\varepsilon)=1+\varepsilon u_i,\qquad
q'_i(\varepsilon)=1+\varepsilon v_i.
\]

Their first \(d-1\) power sums, cumulants, and projection moments agree exactly. Their degree-\(d\) elementary symmetric functions differ by a nonzero multiple of \(\varepsilon^d\); Newton's identities and \(\kappa_d\ne0\) show

\[
|m_d(Q_\varepsilon)-m_d(Q'_\varepsilon)|=c_d\varepsilon^d,
\qquad c_d>0.
\]

Meanwhile the smooth invertible facet-to-side transformation has a nonsingular derivative at \(q_i=1\), so the two sorted side-length lists differ by \(\Theta(\varepsilon)\). Both boxes approach the unit cube. Any exponent greater than \(1/d\) in a uniform inverse inequality fails on this pair as \(\varepsilon\downarrow0\). This completes the exact, all-dimensional stability classification.

## Verification

The standalone Python 3 script `verify.py` checks the moment formulas and inversions on several dimensions, evaluates finite cumulants independently from the half-normal raw moments, verifies positive-root examples and the sharpness construction, and (in dimension three) independently calculates shadow areas of projected eight-vertex convex hulls. Its finite computations are diagnostics, not proofs of nonvanishing at all orders or of infinite-quantifier optimality. Those conclusions follow from the displayed formal-series transcendence argument and the exact polynomial perturbation construction.

## Relationship to prior work

Paouris, Pivovarov and Zinn (2012) study asymptotic random projections of cubes, while Kim, Yaskin and Zvavitch (2015) show broad nonuniqueness of unlabeled projection-volume distributions for general convex bodies. Kabluchko, Litvak and Zaporozhets (2015) provide higher-moment identities for **one-dimensional widths** of regular polytopes; their formulas imply familiar special cases of the present projection moments. The spherical-to-Gaussian conversion, cumulant additivity, Newton identities, and polynomial-root perturbation are standard ingredients and are not individually claimed as new. The assessed result is their exact *all-order nondegenerate half-normal cumulant* connection to arbitrary-dimensional orthotope projection tomography, proving a dimension-sharp minimal moment number and optimal inverse exponent across every dimension.

## Limitations

The theorem is restricted to true orthotopes, not general parallelotopes, and to exact isotropic population projection moments. It recovers no orientation or position, makes no claim of finite-sample statistical optimality, and supplies no dimension-uniform bound on its constants. Algebraic nonvanishing invokes the established transcendence of \(\pi\). Prior unindexed inverse-statistics literature may contain equivalent moment identifiability, so historical originality is not certified exhaustively.

## References

1. G. Paouris, P. Pivovarov and J. Zinn, *A central limit theorem for projections of the cube*, arXiv:1210.7012v1, first public 2012-10-25, especially Sections 1–2.
2. J. Kim, V. Yaskin and A. Zvavitch, *Distribution functions of sections and projections of convex bodies*, arXiv:1512.07289v1, first public 2015-12-22, especially Sections 1, 3–4.
3. Z. Kabluchko, A. E. Litvak and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479v1, first public 2015-11-26, especially Section 3 on moments of one-dimensional widths.
