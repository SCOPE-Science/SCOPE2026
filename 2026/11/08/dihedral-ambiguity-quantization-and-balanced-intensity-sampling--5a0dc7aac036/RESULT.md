# Balanced linear intensity-profile sampling on two crossing circles

## Finding

Let \(C_1,C_2\subset\mathbb C\) be two distinct Euclidean circles intersecting transversely at exactly two points \(a\ne b\). Fix an integer \(d\ge1\), and let \(\mathcal P_d\) be the complex polynomials of degree at most \(d\). Consider the **real linear span of the restrictions** of the functions \(|p(z)|^2\), \(p\in\mathcal P_d\), to \(C_1\cup C_2\). This space has real dimension exactly \(4d\).

Choose exactly \(2d\) distinct points on each circle, none at either intersection. Parametrize \(C_j\) as \(z=c_j+r_j e^{it}\), and let \(t_{j,1},\ldots,t_{j,2d}\) denote the sampling angles. Define the real trigonometric polynomial
\[
 h_j(t)=\prod_{\ell=1}^{2d}\sin\left(\frac{t-t_{j,\ell}}2\right).
\]
Here \(h_j(a),h_j(b)\) mean evaluation at the angular coordinates of the indicated intersection on \(C_j\).

**Theorem (balanced-sampling criterion).** Evaluation at these \(4d\) points is injective on the entire real intensity-profile span **if and only if**
\[
\boxed{\Delta=h_1(a)h_2(b)-h_1(b)h_2(a)\ne0.}
\]
This condition holds on an open, dense, full-Lebesgue-measure subset of balanced sampling configurations. Thus \(4d\) point evaluations suffice generically, and fewer than \(4d\) **real-linear** intensity evaluations cannot recover every profile in this span. The statement is about interpolation of *linear intensity profiles*, not a lower bound for nonlinear phase retrieval of individual polynomials.

If continuous intensity data on \(C_1\cup C_2\) uniquely determine a degree-at-most-\(d\) polynomial up to phase, any balanced set with \(\Delta\ne0\) also gives that determination: reconstruct the entire intensity restriction first. In particular, the known rational-angle degree threshold can be applied after interpolation, but that threshold and the existence of some \(4d\)-point two-circle designs are earlier results, **not novel assertions here**.

## Proof

**1. The real restriction space.** Every \(|p|^2\) is the restriction of a Hermitian bivariate polynomial
\[
F(z,w)=\sum_{j,k=0}^d H_{jk}z^jw^k,\quad H_{jk}=\overline{H_{kj}},
\]
where \(w=\overline z\) on the original real plane. Rank-one Hermitian forms span the real vector space of all Hermitian matrices, so their restrictions span precisely the image of this \((d+1)^2\)-dimensional real vector space. The complexified equation of \(C_j\) is
\[
L_j(z,w)=(z-c_j)(w-\overline{c_j})-r_j^2=0.
\]
Polynomial division after substituting \(w=\overline{c_j}+r_j^2/(z-c_j)\) shows that a polynomial vanishing on the entire circle is divisible by \(L_j\). Because the circles are distinct, the irreducible polynomials \(L_1,L_2\) are coprime. Thus a polynomial of bidegree at most \((d,d)\) vanishes on both exactly when it is \(L_1L_2G\) with \(G\) Hermitian of bidegree at most \((d-2,d-2)\). The kernel dimension is \((d-1)^2\) for \(d\ge2\), and zero when \(d=1\). Hence the image dimension is \((d+1)^2-(d-1)^2=4d\), valid at \(d=1\) too.

**2. Matched trigonometric traces.** On either circle, the restriction of any Hermitian bivariate polynomial has a real Fourier expansion of order at most \(d\). Conversely, the restrictions of \(1\), \(2\operatorname{Re}(z-c_j)^k\), and \(2\operatorname{Im}(z-c_j)^k\) span every real trigonometric polynomial of degree at most \(d\) on \(C_j\). A pair of such traces coming from one global polynomial must agree at \(a\) and \(b\). Those are two independent conditions on the \(4d+2\)-dimensional product of trace spaces, so the matching-traces space has dimension \(4d\). It contains the actual restriction image, which already has dimension \(4d\) by Step 1, hence they coincide.

**3. Evaluation kernel.** A nonzero real trigonometric polynomial of degree at most \(d\) has at most \(2d\) distinct zeros in one period. The real vector space of traces vanishing at the chosen \(2d\) distinct sites on circle \(j\) is one-dimensional and is spanned by \(h_j\). Consequently a matched pair vanishing at every sample is necessarily \((Ah_1,Bh_2)\) with real \(A,B\). Matching at both crossings yields
\[
Ah_1(a)=Bh_2(a),\qquad Ah_1(b)=Bh_2(b).
\]
A nonzero solution exists precisely when \(\Delta=0\). This proves injectivity, the exact criterion, and the dimension-based lower bound for arbitrary real-linear reconstruction.

**4. Genericity.** Omitting the intersections ensures all four factors \(h_j(a),h_j(b)\) are nonzero. As a single sample angle \(t_{1,\ell}\) moves, the ratio \(h_1(a)/h_1(b)\) varies nontrivially since the two crossing angles are distinct. Thus \(\Delta\) is not the zero real-analytic function on the configuration space. Its zero set has empty interior and measure zero, while the nonzero set is open. This completes the proof. \(\square\)

## Relation to previous results and limitations

The general rational-angle ambiguity quotient and its degree-quantization threshold are already established by *Degree quantization and complete phase-ambiguity normal form on intersecting circles* (published 2026-11-02; Resultary, `aa4f300e3a86`). The irrational-angle two-circle uniqueness criterion is also earlier work of Chalendar and Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255 (2024). Bodmann and Hammen, *Stable phase retrieval with low-redundancy frames*, arXiv:1302.5487, provide special \(4d\)-magnitude designs; neither the count \(4d\) by itself nor the established polynomial uniqueness threshold is claimed new. The surviving result is the *complete determinant criterion for arbitrary balanced* \(2d+2d\) **linear profile** interpolation designs, for any transverse crossing geometry, including rational-angle cases in which polynomial phase retrieval itself fails.

No quantitative conditioning, noisy stability estimate, minimal nonlinear sampling count, tangential-circle formula, or result for general analytic curves is asserted. Earlier equivalent interpolation criteria might exist; the originality assessment is best-of-knowledge, not a priority certification.
