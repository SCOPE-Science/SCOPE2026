# The globally optimal sixteen-node spherical ring determinant and its six-chamber hierarchy

## Finding

Let \(\mathcal H_3=\bigoplus_{\ell=0}^{3}\mathcal Y_\ell(\mathbb S^2)\) be the sixteen-dimensional space of complex spherical harmonics of degrees through three. Sample it at the south pole and at regular rings of respectively three, five, and seven points. Write \(x_j\in(-1,1)\) for the height of the \((2j+1)\)-point ring (\(j=1,2,3\)); assume the three heights are distinct. The ring rotations are arbitrary. Let \(M(x_1,x_2,x_3)\) be the sixteen-by-sixteen evaluation matrix in any full-area-orthonormal spherical-harmonic basis, and put \(D(x)=|\det M(x)|^2\).

For a permutation \(\pi=(i,j,k)\) of \((1,2,3)\), its chamber is \(x_i<x_j<x_k\). Each chamber contains one and only one maximizer of \(D\), and the six *chamber-maximum values* have the following exact strict order:

\[
\boxed{(2,3,1)\succ(3,2,1)\succ(1,3,2)\succ(3,1,2)\succ(2,1,3)\succ(1,2,3).}
\]

Consequently the unique globally determinant-optimal height assignment satisfies \(x_2<x_3<x_1\): the five-point ring lies south of the seven-point ring, and the three-point ring lies to the north. Its unique coordinates are the solution of the three explicit stationary equations in the proof in that chamber, and lie within \(10^{-8}\) (in Euclidean norm) of

\[
(x_1,x_2,x_3)=(0.8685804158,-0.6042361642,0.2022056534).
\]

Writing \(D_*\) for this global optimum and \(D_{\mathrm{second}}\) for the maximum in the second-best chamber \((3,2,1)\), their **sharp** ratio satisfies the rigorously certified bounds

\[
\boxed{4.77011<\frac{D_*}{D_{\mathrm{second}}}<4.77012.}
\]

In particular, the best squared determinant exceeds the optimum of *each of the five other chambers* by a factor strictly greater than four. This concerns determinant volume, not the smallest singular value, the condition number, quadrature error, or the Lebesgue constant.

## Assumptions and scope

The sphere is the unit sphere with surface area measure \(d\sigma\) of total mass \(4\pi\). A spherical harmonic of degree \(\ell\) and order \(m\) is normalized to have \(L^2(d\sigma)\)-norm one. The south-pole sample is at \(x_0=-1\). For \(j=1,2,3\), ring \(j\) consists of points with height \(x_j\) and longitudes \(\phi_j+2\pi r/(2j+1)\), for \(0\le r\le 2j\), with arbitrary \(\phi_j\in\mathbb R\). All sixteen samples have equal evaluation weight. Exactly three nonpolar, distinct heights are optimized over; arbitrary sets of sixteen sphere points, freely moved polar nodes, oversampling, and numerical stability objectives are outside the claim.

Define \(Q(x)=D(x)/C_4\), where \(C_4>0\) is the basis-normalization constant. The exact height-dependent formula is

\[
Q(x)=\prod_{j=1}^{3}(1-x_j^2)^{j(j+1)}\prod_{0\le i<j\le3}|x_j-x_i|^{2(2i+1)},\qquad x_0=-1.
\]

An explicit value, not needed for optimizing, is

\[
C_4=\prod_{j=0}^{3}(2j+1)^{2j+1}
\prod_{m=-3}^{3}\prod_{\ell=|m|}^{3}
\left(\frac{2\ell+1}{4\pi}\frac{(\ell-|m|)!}{(\ell+|m|)!}\right)
\left(\frac{(2\ell)!}{2^\ell\ell!(\ell-|m|)!}\right)^2.
\]

## Proof

**Determinant factorization.** Apply a unitary discrete Fourier transform to the \(2j+1\) rows of ring \(j\). Order the resulting ring Fourier rows and the spherical harmonic columns by decreasing absolute angular order. A Fourier residue of absolute order \(k\) can receive contributions only from harmonic orders of absolute value at least \(k\), so the evaluation matrix becomes block triangular. For each harmonic order \(m\in\{-3,\ldots,3\}\), its diagonal block has rows \(j=|m|,\ldots,3\) and columns \(\ell=|m|,\ldots,3\). Up to unimodular row phases and column signs its entries are

\[
\sqrt{2j+1}\left(\frac{2\ell+1}{4\pi}\frac{(\ell-|m|)!}{(\ell+|m|)!}\right)^{1/2}
(1-x_j^2)^{|m|/2}P_\ell^{(|m|)}(x_j).
\]

Here the superscript \((|m|)\) means the ordinary derivative of the Legendre polynomial. These derivatives have successive polynomial degrees \(0,1,\ldots,3-|m|\), with leading coefficient \((2\ell)!/[2^\ell\ell!(\ell-|m|)!]\). Their determinant is a leading-coefficient product times a Vandermonde product. Multiplication over all \(m\) gives exactly \(D=C_4Q\): each height obtains exponent \(\sum_{m=-j}^j|m|=j(j+1)\), and each pair \(i<j\) appears in \(2i+1\) blocks and obtains squared-determinant exponent \(2(2i+1)\). The arbitrary longitude phases therefore cancel in \(|\det M|\).

**Existence, uniqueness, and a global curvature bound.** In a fixed ordering chamber put \(F=\log Q\). With \(v_0=0\) its Hessian satisfies

\[
 v^{\mathsf T}(\nabla^2F)v=
 -\sum_{j=1}^{3}\frac{2j(j+1)(1+x_j^2)}{(1-x_j^2)^2}v_j^2
 -\sum_{0\le i<j\le3}\frac{2(2i+1)}{(x_j-x_i)^2}(v_j-v_i)^2
 \le-4\|v\|_2^2.
\]

Every chamber is convex; \(F\to-\infty\) on its boundary (at a pole or a collision), so it has exactly one interior maximizer, with nonsingular Hessian. Its coordinates solve \(\nabla F=0\), explicitly

\[
-\frac{2j(j+1)x_j}{1-x_j^2}
+\sum_{i=0}^{j-1}\frac{2(2i+1)}{x_j-x_i}
+\sum_{k=j+1}^{3}\frac{2(2j+1)}{x_j-x_k}=0,
\qquad j=1,2,3.
\]

The bound \(\nabla^2F\preceq-4I\) gives, for any point \(q\) of a chamber, its unique maximizer \(x^*\), and \(g=\nabla F(q)\),

\[
\|x^*-q\|_2\le\frac{\|g\|_2}{4},\qquad
 F(x^*)\le F(q)+\frac{\|g\|_2^2}{8}.
\]

Whenever \(\|g\|_2^2<1\), the elementary inequality \(e^u\le1+2u\) for \(0\le u\le1/2\) therefore yields the **rational upper certificate**

\[
 Q(x^*)\le Q(q)\left(1+\frac{\|g\|_2^2}{4}\right).
\]

**Exact comparison of all six maxima.** The following table gives the three signed integers \((n_1,n_2,n_3)\) defining a rational point \(q_j=n_j/10^{10}\) in each chamber. Thus every entry of \(Q(q)\), \(\nabla F(q)\), and \(\|\nabla F(q)\|_2^2\) is an exact rational number.

| Ordering chamber | \(n_1\) | \(n_2\) | \(n_3\) |
|---|---:|---:|---:|
| \((2,3,1)\) | 8685804158 | −6042361642 | 2022056534 |
| \((3,2,1)\) | 8828424289 | 3096304714 | −4566685205 |
| \((1,3,2)\) | −7224748987 | 7215671467 | −629158625 |
| \((3,1,2)\) | 1711718224 | 7433256806 | −4614491244 |
| \((2,1,3)\) | 300179852 | −6231431047 | 5750945098 |
| \((1,2,3)\) | −7453364257 | −1443429094 | 5653891177 |

The included standalone `CHECKER.py` performs the following operations using Python's *exact* rational arithmetic: it verifies that every listed point is in its claimed chamber, that every squared gradient norm is below \(10^{-15}\), and, for every adjacent pair of chamber labels \(\alpha\succ\beta\) in the displayed ordering, that

\[
 Q(q_\alpha)>Q(q_\beta)\left(1+\frac{\|\nabla F(q_\beta)\|_2^2}{4}\right).
\]

These rational inequalities, together with the preceding global curvature bound, prove the strict ordering of **the actual chamber maxima**, not merely of six sampled determinants. In particular, they rigorously determine the unique winning chamber. The gradient bound gives \(\|x^*-q\|_2<10^{-8}\) in every chamber. Lastly the same exact-rational checker compares the best and runner-up values by bounding both chamber maxima and verifies the sharp ratio enclosure \(4.77011<D_*/D_{\mathrm{second}}<4.77012\).

## Verification

Run `python CHECKER.py` using only the Python standard library. It checks the six chamber assignments, positive rational determinant factors, six gradient norm bounds, five adjacent strict rankings, the winning-to-runner-up two-sided ratio bounds, and the factor-four separation. It produces a PASS report or stops at the first failed exact integer/rational assertion. No optimization routine, floating-point calculation, external source, or file outside the package is required to *verify the finite comparisons*.

The derivation of \(D=C_4Q\), the strict curvature bound, and the implication of the finite inequalities for all real height triples are analytic arguments stated above. Finite rational comparisons alone do **not** prove those infinite-domain steps. A separate direct sixteen-by-sixteen complex spherical-harmonic evaluation at the displayed optimum was also compared numerically with \(C_4Q\), agreeing to relative floating error below \(10^{-12}\); that test is supplementary, not a proof.

## Relationship to prior work

The odd-ring sampling geometry was already proposed by Giacaglia–Lundquist (1972), while its modern orderwise spherical-harmonic treatment is developed by Khalid–Kennedy–McEwen (2014), and Nafees–Khalid–Kennedy–McEwen (2017). The 1972 source recommends an essentially fixed near-uniform ring placement, not determinant maximization over its six height-ordering chambers. The 2014 and 2017 papers focus on reconstruction and the condition numbers of per-order systems, not on continuous-height determinant optimization and ranking all orderings. Khalid (2026), posted after the selected 2026-11-08 literature anchor, optimizes a different amplification criterion for this point architecture and likewise does not give the six-chamber determinant ranking. Dell'Accio–Nudo–Pérez–Piñar (2026) establishes general interpolation–regression rank and stability criteria for spherical nodes rather than a degree-three, sixteen-node D-optimal ring configuration. Beltrán–Marzo–Ortega-Cerdà (2026) studies spherical point distributions with optimal discrepancy and energy rates, which are distinct objectives from this restricted harmonic determinant.

An existing all-bandwidth ring-determinant factorization and strict concavity theorem supplies the relevant structural starting point, including the fact that every ordering chamber has one maximum; it does **not** identify which chamber wins for bandwidth four or rank its six maxima. The present contribution is exactly that global and quantitative ranking. Prior small-band quadratic nine-node height optimization does not imply the cubic sixteen-node comparison. The relevant published comparisons and remaining bibliographic risks are detailed in `REVIEW.md` and `AUDIT.json`.

## Limitations

Only the specified sixteen-node one-pole/three-regular-ring architecture is optimized. The theorem does not claim that this point set is a global Fekete configuration among arbitrary sixteen points, that it optimizes numerical condition numbers or Lebesgue constants, or that the winning height ordering persists at higher bandlimits. The optimal heights are characterized by a uniquely solvable algebraic stationarity system and certified approximations, not claimed to have a simple closed radical form. The full six-chamber ordering has an exact rational proof certificate; its novelty is assessed only relative to inspected accessible literature, not independently audited.

## References

- G. E. O. Giacaglia, C. A. Lundquist, *Sampling Functions for Geophysics*, Smithsonian Astrophysical Observatory Special Report 344 (1972), section 3.2. https://ntrs.nasa.gov/citations/19730008792
- Z. Khalid, *An \(O(L^3)\) Spherical Harmonic Transform on \(L^2\) Samples*, arXiv:2611.16441, first posted 2026-11-12 (comparison only, after the literature eligibility anchor). https://arxiv.org/html/2611.16441v1
- F. Dell'Accio, F. Nudo, T. E. Pérez, M. A. Piñar, *Polynomial interpolation–regression on the sphere*, arXiv:2605.13124, first posted 2026-05-13. https://arxiv.org/abs/2605.13124
- C. Beltrán, J. Marzo, J. Ortega-Cerdà, *A set of points with optimal \(L^2\) spherical cap discrepancy*, arXiv:2609.27708, first posted 2026-09-23. https://arxiv.org/abs/2609.27708
- Z. Khalid, R. A. Kennedy, J. D. McEwen, *An Optimal-Dimensionality Sampling Scheme on the Sphere with Fast Spherical Harmonic Transforms*, arXiv:1403.4661 (2014). https://arxiv.org/abs/1403.4661
- W. Nafees, Z. Khalid, R. A. Kennedy, J. D. McEwen, *Optimal-Dimensionality Sampling on the Sphere: Improvements and Variations*, arXiv:1709.02497 (2017). https://arxiv.org/abs/1709.02497
