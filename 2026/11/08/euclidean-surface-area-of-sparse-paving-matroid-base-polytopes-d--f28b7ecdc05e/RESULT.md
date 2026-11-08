# Euclidean surface area of sparse-paving matroid base polytopes depends only on their nonbases

## Finding

Let \(M\) be a connected sparse-paving matroid of rank \(r\) on \(n\) elements, where \(n\ge4\) and \(2\le r\le n-2\). Let \(\lambda\) be its number of circuit-hyperplanes (equivalently, its number of nonbases of size \(r\)). Let \(P(M)\) be its standard base polytope, the convex hull in \(\mathbb R^n\) of the indicator vectors of its bases, in its intrinsic affine space \(\sum_i x_i=r\). Write \(\mathcal A(P)\) for its ordinary \((n-2)\)-dimensional Euclidean boundary measure (not lattice-normalized surface area).

Set \(t=n-r\), and let \(E(m,j)\) denote the number of permutations of \(m\) elements with exactly \(j\) descents (zero outside \(0\le j<m\)). Define
\[
\mathcal A_0(n,r)=\frac{n\sqrt{n-1}}{(n-2)!}\bigl(E(n-2,r-1)+E(n-2,r-2)\bigr)
\]
and
\[
D(n,r)=\frac{\dfrac{\sqrt{n-1}}{n-2}\bigl(r(r-1)+t(t-1)\bigr)-\sqrt{rt}}{(r-1)!(t-1)!}.
\]
Then
\[
\boxed{\mathcal A(P(M))=\mathcal A_0(n,r)-\lambda D(n,r).}
\]
Furthermore, \(D(n,r)>0\). At fixed \(n\), the loss \(D(n,r)\) strictly increases as the rank approaches \(n/2\), apart from the unavoidable equality of the two complementary middle ranks when \(n\) is odd. Hence the coefficient is largest at the balanced rank(s).

In particular, two connected sparse-paving matroids of equal rank, ground-set size and number of circuit-hyperplanes have equal *ordinary Euclidean surface area*, even when their face vectors differ. For example, the rank-three matroids on six elements whose two nonbases are \(\{1,2,3\},\{4,5,6\}\), respectively \(\{1,2,3\},\{1,4,5\}\), both have
\[
\mathcal A(P(M))=4\sqrt5+\frac32,
\]
although their two nonbases intersect in zero versus one element. Published sparse-paving face-vector formulas distinguish these cases.

## Assumptions and scope

The matroid is connected, ensuring that \(P(M)\) is full dimensional in \(\sum_i x_i=r\). Sparse paving means every \(r\)-subset is either a basis or a circuit-hyperplane. Distinct circuit-hyperplanes \(H,H'\) satisfy \(|H\cap H'|\le r-2\). The metric is the inherited ambient Euclidean metric; the surface area is Hausdorff measure of the boundary in the \((n-1)\)-dimensional affine hull. The disconnected rank-two, four-element two-parallel-class case is excluded because its base polytope has lower affine dimension. No independence of the chosen circuit-hyperplanes is assumed.

## Proof

**1. Baseline.** The uniform matroid base polytope is the hypersimplex
\[
\Delta(n,r)=\{x\in[0,1]^n:\sum_i x_i=r\}.
\]
Its \(n\) coordinate-zero facets are isometric to \(\Delta(n-1,r)\), and its \(n\) coordinate-one facets to \(\Delta(n-1,r-1)\). The intrinsic Euclidean volume of \(\Delta(m,j)\) is
\[
\frac{\sqrt m}{(m-1)!}E(m-1,j-1).
\]
This gives \(\mathcal A_0(n,r)\).

**2. The exact corner removed by one nonbasis.** For any circuit-hyperplane \(H\), the valid inequality is \(\sum_{i\in H}x_i\le r-1\). The portion of \(\Delta(n,r)\) on the other side is the pyramid with apex \(\mathbf1_H\) and base
\[
F_H=\operatorname{conv}\{\mathbf1_H-e_i+e_j:i\in H,\ j\notin H\}.
\]
Its base is the orthogonal Cartesian product \(\Delta(r,r-1)\times\Delta(t,1)\), of dimension \(n-2\) and Euclidean area
\[
V_{\mathrm{new}}=\frac{\sqrt{rt}}{(r-1)!(t-1)!}.
\]
Exactly \(r\) original facets of the form \(x_i=1\), with \(i\in H\), and \(t\) original facets of the form \(x_j=0\), with \(j\notin H\), lose a corner. In any one of the former facets, the excised \((n-2)\)-volume is
\[
L_1=\frac{\sqrt{n-1}}{(n-2)(r-2)!(t-1)!}.
\]
Indeed, the base of this facet-level pyramid has \((n-3)\)-volume \(\sqrt{(r-1)t}/((r-2)!(t-1)!)\); its orthogonal height in the facet is \(\sqrt{(n-1)/((r-1)t)}\). Similarly, any affected \(x_j=0\) facet loses
\[
L_0=\frac{\sqrt{n-1}}{(n-2)(r-1)!(t-2)!}.
\]
Thus the net surface-area *decrease* from one circuit-hyperplane is
\[
rL_1+tL_0-V_{\mathrm{new}}=D(n,r).
\]
This calculation remains valid if an affected original facet disappears completely, since then its entire measure is subtracted.

**3. Additivity without assumptions on intersection patterns.** If \(H\ne H'\) are circuit-hyperplanes then \(|H\cap H'|\le r-2\). For every \(x\in\Delta(n,r)\),
\[
x(H)+x(H')=x(H\cup H')+x(H\cap H')\le r+(r-2)=2r-2.
\]
Consequently the *strict* removed corners \(x(H)>r-1\) and \(x(H')>r-1\) are disjoint. Every new cut face \(F_H\) lies in all the other admissible halfspaces, and any two distinct cut faces share no relatively open \((n-2)\)-dimensional piece (because their defining normals are distinct modulo the all-ones direction in the full-dimensional case). The removed patches of old facets likewise have disjoint relative interiors. As the matroid base polytope equals the hypersimplex intersected with these rank inequalities, the Euclidean boundary measure is exactly the original hypersimplex area minus the sum of all old patches, plus all the new cut-facet areas. This proves the asserted linear formula \(\mathcal A_0-\lambda D\).

**4. Positivity and the balanced-rank extremum.** Put \(c=\sqrt{n-1}/(n-2)\) and \(a(r,t)=r(r-1)+t(t-1)\). Since
\[
a(r,t)-rt=(r-t)^2+rt-n\ge0,
\]
and \(c\sqrt{rt}\ge\sqrt{2(n-1)/(n-2)}>\sqrt2>1\), the numerator \(c\,a(r,t)-\sqrt{rt}\) is strictly positive.

For strict rank monotonicity, take \(2\le r\le t-2\) at fixed \(n=r+t\), put \(d=t-r-1>0\), \(b=\sqrt{rt}\), \(b'=\sqrt{(r+1)(t-1)}\), and \(Q=c\,a(r,t)-b\). Then \(a(r+1,t-1)=a(r,t)-2d\) and \(b'-b=d/(b+b')\). Comparing the two factorial denominators shows that \(D(n,r+1)>D(n,r)\) is equivalent to
\[
c\bigl(a(r,t)-2(t-1)\bigr)>b+\frac{t-1}{b+b'}.
\]
The elementary inequality \(a(r,t)-2(t-1)\ge rt\) holds for \(t\ge r+2\): at \(t=r+2\), its difference from \(rt\) is \(r(r-2)\ge0\), and it grows with \(t\). Also
\[
\frac{t-1}{b+b'}\le\frac{t-1}{2b}<\frac{b}{2r}\le\frac b4,
\]
whereas \(c\,rt=b(c b)>b\sqrt2>5b/4\). Therefore the strict inequality holds. Symmetry under \(r\leftrightarrow t\) completes the rank comparison.

## Verification

The standalone `check_surface.py` constructs each incidence-vector polytope in an orthonormal basis of its intrinsic affine space, measures its boundary using convex-hull facets, and compares this independent computation with the stated formula. It checked 73 nondegenerate examples through seven elements, including families with multiple intersecting circuit-hyperplanes, and tested rank-coefficient positivity and monotonicity for 76 ground-set sizes. The two explicit six-element examples were checked independently. The script uses NumPy and SciPy; run `python check_surface.py`. These finite computations are corroboration, not the all-parameter proof.

## Relationship to prior work

Ferroni's work on circuit-hyperplane relaxation and sparse-paving Ehrhart polynomials, and Hanely et al.'s systematic hypersimplex slicing, supply the mathematical setting and the corner-decomposition perspective. Their Ehrhart boundary coefficients concern lattice-normalized boundary measure, not the intrinsic Euclidean measure computed here: the Euclidean covolume factors differ for the coordinate and circuit-hyperplane facets. Ferroni and Schröter's face-vector theorem depends additionally on pairs of circuit-hyperplanes meeting in \(r-2\) elements; the Euclidean surface area proved here does not. Neither result, as stated, gives this Euclidean additive coefficient and its sharp balanced-rank ordering.

## Limitations

Only connected sparse-paving matroids and their canonical incidence-vector embeddings are treated. The result does not assert uniqueness among all polytopes of the same area, does not determine higher intrinsic volumes, and does not show that the largest attainable loss among *all* matroids at fixed ground-set size occurs at balanced rank when the permissible number of circuit-hyperplanes is itself allowed to vary. The originality comparison is based on the cited primary literature and targeted searches; an earlier equivalent Euclidean boundary valuation under alternate terminology remains possible. No independent mathematical audit has been performed.

## References

1. L. Ferroni, *Matroids are not Ehrhart positive*, arXiv:2105.04465 (first public version May 10, 2021), especially §4 and the circuit-hyperplane relaxation statements.
2. D. Hanely, J. L. Martin, D. McGinnis, D. Miyata, G. D. Nasr, A. R. Vindas-Meléndez, and M. Yin, *Ehrhart Theory of Paving and Panhandle Matroids*, arXiv:2201.12442 (first public version January 28, 2022), §5.
3. L. Ferroni and B. Schröter, *Face enumeration for split matroid polytopes*, *Combinatorics, Probability and Computing* (2025), DOI:10.1017/S0963548325000021, Corollary 2.10.
4. G. Pineda-Villavicencio and B. Schröter, *Reconstructibility of Matroid Polytopes*, arXiv:2010.10227 (first public version October 20, 2020), especially its hypersimplex facet discussion.
