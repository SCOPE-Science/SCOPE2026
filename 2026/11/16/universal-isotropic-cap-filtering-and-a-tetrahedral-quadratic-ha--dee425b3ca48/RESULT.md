# Universal isotropic cap filtering and a tetrahedral quadratic-harmonic isometry

## Finding

Let \(\sigma\) be normalized area measure on \(S^2\), and let \(\mathcal H_2\) be the five-dimensional complex space of pure degree-two spherical harmonics. Suppose \(\nu\) is **any** probability measure of cap centers satisfying the second-moment isotropy identity
\[
\int_{S^2}uu^{\mathsf T}\,d\nu(u)=\frac13 I_3.
\]
For \(0<c<1\), form the probability distribution \(\mu_{\nu,c}\) by choosing \(u\sim\nu\) and then choosing \(x\) uniformly on the cap \(x\cdot u\ge c\). At the unique nontrivial universal radius parameter
\[
\boxed{c_*=\sqrt{3/7}},
\]
the smoothed center distribution is an **exact isometry on quadratic harmonics**:
\[
\boxed{\int q\overline r\,d\mu_{\nu,c_*}=\int q\overline r\,d\sigma\quad\text{for all }q,r\in\mathcal H_2.}
\]
The parameter is unique in \((0,1)\) for which this holds for *every* second-moment-isotropic center distribution.

The four vertices of a regular tetrahedron supply a sharp, disjoint-cap realization. Put
\[
U=\{(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)\}/\sqrt3,
\quad
\Omega_c=\bigcup_{u\in U}\{x\in S^2:x\cdot u\ge c\},
\]
where \(1/\sqrt3\le c<1\). For the concentration operator on \(\mathcal H_2\), with quadratic form \(\int_{\Omega_c}|q|^2\,d\sigma\), its **complete spectrum** is
\[
\boxed{D(c)=2(1-c)-\frac{c(1-c^2)(7c^2-3)}4}\qquad(\text{multiplicity }2),
\]
\[
\boxed{O(c)=2(1-c)+\frac{c(1-c^2)(7c^2-3)}6}\qquad(\text{multiplicity }3).
\]
The two-dimensional eigenspace consists of diagonal trace-free quadratics \(\operatorname{span}\{x^2-y^2,x^2+y^2-2z^2\}\); the three-dimensional eigenspace consists of mixed quadratics \(\operatorname{span}\{xy,xz,yz\}\). They exchange their relative concentration order **exactly once** at \(c_*\). At that parameter,
\[
\boxed{\int_{\Omega_{c_*}}q\overline r\,d\sigma=2(1-\sqrt{3/7})\int_{S^2}q\overline r\,d\sigma,}
\]
so the restriction is a scaled isometry. Its Gram condition number satisfies \(\kappa(c)\sim[3(1-c)]^{-1}\) as \(c\uparrow1\).

## Assumptions and scope

All measures use normalized surface area \(\sigma(S^2)=1\). A cap of threshold \(c\) has area fraction \((1-c)/2\), hence the conditional cap probability measure is \(2\mathbf1_{\{x\cdot u\ge c\}}d\sigma(x)/(1-c)\). The center measure \(\nu\) is arbitrary, including discrete and non-antipodal laws, provided it has the displayed isotropic second moment; no first-moment or fourth-moment assumption is imposed. Inner products are Hermitian and quadratic harmonics are homogeneous harmonic polynomials of degree two restricted to \(S^2\).

In the tetrahedral assertion, the caps have disjoint interiors for \(c\ge1/\sqrt3\), since the center separation has cosine \(-1/3\). Thus their union has area fraction \(m(c)=2(1-c)\). Eigenvalues refer to the Gram matrix with respect to the *whole-sphere* \(L^2(\sigma)\) inner product. At the endpoint where two cap boundaries touch, their intersection has zero area and all identities remain valid.

## Proof

**1. Harmonic filtering.** Write \(P_\ell\) for the Legendre polynomial with \(P_\ell(1)=1\). For \(H\in\mathcal H_\ell\), rotational symmetry of the cap and the Funk–Hecke formula give
\[
\int H(x)\,d\kappa_{u,c}(x)=a_\ell(c)H(u),\qquad
 a_\ell(c)=\frac{1}{1-c}\int_c^1P_\ell(t)\,dt.
\]
For the relevant fourth order,
\[
P_4(t)=\frac{35t^4-30t^2+3}{8},\qquad
 a_4(c)=\frac{c(1+c)(7c^2-3)}8.
\]
A product \(q\overline r\) of pure quadratic harmonics is an even polynomial of degree at most four on the sphere; its spherical-harmonic expansion has **only degrees 0, 2 and 4**. Every degree-two harmonic is a linear combination of \(u_i u_j-\delta_{ij}/3\); the isotropic second-moment hypothesis therefore gives \(\int H_2(u)\,d\nu(u)=0\). At \(c=c_*\), the fourth-harmonic multiplier also vanishes. Cap averaging hence preserves only the constant component of \(q\overline r\), and integrating over \(\nu\) yields the isometry.

**2. Uniqueness of the universal threshold.** In \(0<c<1\), the displayed factorization shows \(a_4(c)=0\) only when \(c=c_*\). The tetrahedral distribution in Step 3 is isotropic and has a nonzero fourth-harmonic moment: for \(q=x^2-y^2\), its values at all centers vanish while \(\int q^2d\sigma=4/15\). Therefore its fourth-harmonic center average is nonzero (the degree-two part averages to zero). If \(a_4(c)\ne0\), the cap-mixture norm of this \(q\) is not its sphere norm. This proves uniqueness for the **universal** claim, without asserting uniqueness for each individual \(\nu\).

**3. Exact tetrahedral eigenspaces.** The four displayed unit vectors satisfy \(\sum_{u\in U}uu^{\mathsf T}=\tfrac43I\); thus their uniform law is isotropic. Sign changes of pairs of coordinates and cyclic permutations preserve the four-center distribution. These symmetries eliminate all Gram cross terms between the diagonal and mixed quadratic subspaces and between distinct mixed coordinates; a cyclic rotation forces scalar action on the two-dimensional trace-free diagonal subspace. It remains to evaluate one vector in each sector.

For any real quadratic harmonic \(q\), its fourth-harmonic component \(H_4\) of \(q^2\) satisfies
\[
\sum_{u\in U}H_4(u)=\sum_{u\in U}q(u)^2-4\int q^2d\sigma,
\]
because the sum of its degree-two component vanishes. The unnormalized cap multiplier is
\[
k_4(c)=\int_{x\cdot u\ge c}P_4(x\cdot u)\,d\sigma(x)
=\frac12\int_c^1P_4(t)\,dt
=\frac{c(1-c^2)(7c^2-3)}{16}.
\]
Therefore
\[
\int_{\Omega_c}q^2d\sigma
=2(1-c)\int q^2d\sigma
+k_4(c)\left(\sum_{u\in U}q(u)^2-4\int q^2d\sigma\right).
\]
For \(q=x^2-y^2\), \(\int q^2d\sigma=4/15\) and \(\sum_Uq(u)^2=0\), giving \(D(c)=2(1-c)-4k_4(c)\). For \(q=xy\), \(\int q^2d\sigma=1/15\) and \(\sum_Uq(u)^2=4/9\), giving \(O(c)=2(1-c)+\tfrac83k_4(c)\). The symmetry argument then gives their full multiplicities, eigenspaces and **all five** eigenvalues.

**4. Crossing and endpoint condition.** Their difference factors as
\[
D(c)-O(c)=-\frac5{12}c(1-c^2)(7c^2-3).
\]
It changes sign exactly once in the stated interval, at \(c_*\). Both eigenvalues are strictly positive for \(c<1\): a nonzero spherical harmonic cannot vanish on any cap with nonempty interior. The diagonal branch factors as
\[
D(c)=\frac{(1-c)^2(7c^3+14c^2+11c+8)}4,
\]
so \(D(c)\sim10(1-c)^2\); direct expansion gives \(O(c)\sim\tfrac{10}3(1-c)\). The condition-number asymptotic follows and finishes the proof.

## Verification

Run `python verify_tetra_caps.py` with Python, NumPy and SymPy installed. Exact symbolic steps check the fourth-order Legendre integral, both spectral formulas, a factored characteristic comparison, the positive diagonal factor, the unique crossing and the condition-number limit. As a separate diagnostic, tensor-product Gauss–Legendre and azimuthal quadrature integrate all 25 Gram entries for six cap thresholds. Three different isotropic center laws (tetrahedral, orthogonal axial and antipodal-octahedral) independently reproduce the identity at \(c_*\). Those finite numerical comparisons corroborate but do not substitute for the analytic assertions, which concern all isotropic center measures and all admissible radii.

## Relationship to prior work

Classical Funk–Hecke theory supplies the cap convolution eigenmultipliers; spherical-design theory supplies the general idea of vanishing low-order moments. Roddy and McEwen (2021) study Slepian concentration and wavelets on incomplete spherical regions. Li and Chen (2024) study subdesigns and exact quadrature on a *single* spherical cap using high-strength spherical designs. Neither of these contributions, as examined, establishes the universal isotropic second-moment-to-fourth-moment cap filter at \(c_*\), nor the complete two-branch restriction spectrum for four disjoint tetrahedrally placed caps. The novelty claim is restricted to those precise derived statements, **not** the Funk–Hecke formula or the existence of spherical designs.

Related published calculations concern fourth-order volume moments of Platonic solids, or hemisphere concentration for arbitrary harmonic degrees; they neither imply the present cap-center distribution identity nor its two-branch tetrahedral extremizers. Equivalent results phrased as zonal convolution filters, cubature improvement or low-order spherical localization remain a bibliographic priority risk.

## Limitations

The universal assertion applies to **pure degree-two** harmonics on \(S^2\) and cap-center probability measures satisfying isotropic second moments. It does not cover mixed low-pass bands, arbitrary cap shapes or higher-degree harmonics. The explicit union-of-four-caps spectrum assumes equal radius and tetrahedral centers with disjoint interiors. The unique radius is unique **uniformly across all isotropic center laws**; particular distributions possessing additional fourth-moment isotropy can be tight for other radii. No assertion of an independent audit or historically certified priority is made.

## References

1. P. J. Roddy and J. D. McEwen, *Slepian Scale-Discretised Wavelets on the Sphere*, arXiv:2106.02023, first submitted June 3, 2021; later *IEEE Transactions on Signal Processing* 70 (2022), 6142–6153.
2. C. Li and X. Chen, *Spherical Designs for Approximations on Spherical Caps*, *SIAM Journal on Numerical Analysis* 62 (2024), 2506–2528, DOI: 10.1137/23M1555417.
3. The classical Funk–Hecke formula, used as a known spherical-harmonic convolution identity rather than a new theorem.
