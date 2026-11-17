# Curvature universality and the complete ridge spectrum of layered enriched chain polytopes

## Finding
Let \(P=A_1\oplus\cdots\oplus A_r\) be the ordinal sum of \(r\ge2\) nonempty antichains, \(|A_i|=a_i\ge1\), \(n=\sum_i a_i\ge3\), and \(s=|\{i:a_i=1\}|\). The enriched chain polytope \(E(P)\subset\mathbb R^n\) is defined by the signed antichain indicators in [1]. Set
\[
K(r,s)=(r-s)\sqrt{2r-1}\arccos\frac{r-1}{r}+s\sqrt{r-1}\arccos\frac{r-2}{r}.
\]
With the standard coordinate Euclidean metric and standard intrinsic-volume normalization \(\operatorname{Vol}_n(E+tB_n)=\sum_{j=0}^n\kappa_{n-j}V_j(E)t^{n-j}\), where \(\kappa_1=2\), \(\kappa_2=\pi\), the exact formulas are
\[
\operatorname{Vol}_n(E)=\frac{2^n\prod_i a_i!}{n!},\qquad
\frac{V_{n-1}(E)}{\operatorname{Vol}_n(E)}=\frac{n\sqrt r}{2},\qquad
\boxed{\frac{V_{n-2}(E)}{\operatorname{Vol}_n(E)}=\frac{n(n-1)}{4\pi}K(r,s).}
\]
Equivalently, as \(t\downarrow0\),
\[
\frac{\operatorname{Vol}_n(E+tB_n)}{\operatorname{Vol}_n(E)}
=1+n\sqrt r\,t+\frac{n(n-1)}4K(r,s)t^2+O_{P}(t^3).
\]
Thus the first two relative outer-parallel-volume coefficients depend on the level sizes only through the total order \(n\), number of levels \(r\), and number of singleton levels \(s\). This invariance holds even for distinct level-size profiles with different Euclidean volumes.

Write \(F=2^r\prod_i a_i\). The polytope has exactly \(F\) facets. For each level with \(a_i\ge2\), exactly \(F(a_i-1)\) ridges are obtained by changing the signed coordinate chosen in that level between two distinct coordinates; each has exterior dihedral angle \(\arccos((r-1)/r)\). For each singleton level, exactly \(F/2\) ridges are obtained by reversing its sign, with angle \(\arccos((r-2)/r)\). These are all ridges. In particular the complete Euclidean ridge-angle spectrum has at most two values, independent of the sizes of the nonsingleton levels.

## Assumptions and scope
An ordinal sum means every element of \(A_i\) is below every element of \(A_j\) for \(i<j\), and elements within a level are incomparable. Its antichains are contained within single levels, so
\[
E(P)=\operatorname{conv}\left(\bigcup_{i=1}^r\{0\}^{a_1+\cdots+a_{i-1}}\times[-1,1]^{a_i}\times\{0\}^{a_{i+1}+\cdots+a_r}\right)
=\left\{x:\sum_i\|x^{(i)}\|_\infty\le1\right\}.
\]
The dimension is \(n\). Here \(V_{n-2}\) is an ordinary Euclidean intrinsic volume, not normalized lattice volume. The claimed ridge classifications include degenerate singleton levels and all admissible profiles, without asymptotic conditions. In two dimensions the analogous identity reduces to \(V_0=1\), but the stated main range starts at dimension three.

## Proof
**Facets and adjacency.** The displayed gauge gives exactly one facet inequality for every tuple \((j_i,\epsilon_i)\), with \(j_i\in\{1,\ldots,a_i\}\) and \(\epsilon_i\in\{-1,1\}\):
\[
\sum_{i=1}^r\epsilon_i x_{i,j_i}\le1.
\]
Every chosen combination is a genuine facet: choose strictly positive \(t_i\) summing to one, set \(x_{i,j_i}=\epsilon_i t_i\), and put every other coordinate strictly between \(-t_i\) and \(t_i\). Thus the facet count is \(F=\prod_i(2a_i)\). The polar is the Cartesian product of the \(a_i\)-dimensional cross-polytopes \(\operatorname{conv}\{\pm e_j\}\), one per level. Two facets of the original share a ridge precisely when their polar vertices span an edge. An edge of the product changes one factor and leaves all other factors fixed. In a cross-polytope of dimension at least two, vertices are joined exactly when they are distinct and nonopposite; there are \(2a_i(a_i-1)\) such edges. In dimension one the single edge joins opposite endpoints. This proves the asserted ridge counts and exhaustiveness.

The outward facet normals have exactly \(r\) entries of magnitude one and hence norm \(\sqrt r\). Adjacent normals have scalar product \(r-1\) when the changing level has size at least two, or \(r-2\) when it is a singleton. The exterior dihedral angle is the arccosine of the normalized scalar product. This proves the two angular classes (interior dihedral angles are their supplements).

**Facet and ridge measures.** A facet parameterization uses levels \(t_i\ge0\) with \(\sum_i t_i=1\). Every unchosen coordinate in level \(i\) ranges independently over \([-t_i,t_i]\). The Euclidean Jacobian along the chosen-coordinate simplex is \(\sqrt r\). The multivariate beta integral therefore gives each facet area
\[
A_F=\frac{\sqrt r\,2^{n-r}\prod_i(a_i-1)!}{(n-1)!}.
\]
Summing over all \(F\) facets gives the surface area \(S(E)=2^n\sqrt r\prod_i a_i!/(n-1)!\).

Fix a nonsingleton level \(i\) and a ridge coming from two different signed coordinate choices in it. The two selected signed coordinates are equal to a common positive level value \(t_i\); there are \(a_i-2\) other free coordinates in this level. The Gram determinant for the chosen-coordinate simplex is \(2r-1\), because level \(i\) contributes twice to its Euclidean metric and the other levels once. The ridge \((n-2)\)-measure is
\[
A_{R,i}^{(2)}=\frac{\sqrt{2r-1}\,2^{n-r-1}(a_i-2)!\prod_{j\ne i}(a_j-1)!}{(n-2)!}.
\]
For a singleton level \(i\), the opposite-sign facet pair intersects at its coordinate zero; the remaining \(r-1\) chosen levels sum to one. Its Gram factor is \(\sqrt{r-1}\), and the ridge measure is
\[
A_{R,i}^{(1)}=\frac{\sqrt{r-1}\,2^{n-r}\prod_{j\ne i}(a_j-1)!}{(n-2)!}.
\]
All formulas remain valid when \(r=2\), with zero-dimensional parameter simplices interpreted as points. Each beta integral follows from
\[
\int_{\substack{t_i\ge0\\\sum_i t_i=1}}\prod_i t_i^{b_i-1}\,dt_1\cdots dt_{r-1}=\frac{\prod_i\Gamma(b_i)}{\Gamma(\sum_i b_i)}.
\]
Multiplying ridge measure by the corresponding ridge counts yields, **for each individual level**, a total ridge measure of \(2^{n-1}\prod_j a_j!/(n-2)!\) times \(\sqrt{2r-1}\) in the nonsingleton case or \(\sqrt{r-1}\) in the singleton case. Dependence on individual nonsingleton sizes cancels exactly.

**Intrinsic volumes.** The Euclidean volume follows directly from the Dirichlet integral on the nonnegative orthant, or equivalently from the free-sum volume product [3]: \(\operatorname{Vol}_n(E)=2^n\prod_i a_i!/n!\). For any full-dimensional Euclidean convex polytope, the codimension-two intrinsic volume is
\[
V_{n-2}(E)=\frac1{2\pi}\sum_{R\text{ ridge}}\operatorname{Vol}_{n-2}(R)\,\theta_R,
\]
where \(\theta_R\) is the exterior dihedral angle. This follows from the second-order circular-sector contribution around each ridge in the outer parallel body. Substituting the two counts, two measures, and two angles yields
\[
V_{n-2}(E)=\frac{2^{n-2}\prod_i a_i!}{\pi(n-2)!}\,K(r,s).
\]
Dividing by \(\operatorname{Vol}_n(E)\), and using \(V_{n-1}=S(E)/2\), proves every formula and the claimed universality.

## Verification
The standalone script `verify_layered_curvature.py` reconstructs signed-cube vertices and facet normals independently, enumerates facet pairs, checks which pairs meet in codimension two, and computes their actual Euclidean ridge measures by orthogonal projection and convex hull. It checks 11 distinct profiles in dimensions two through five, comprising 466 ridges, and 262125 additional integer profile/multiplicity identities through total dimension 18. The script reports `LAYERED_CURVATURE_PASS`. Finite tests are corroboration; the all-dimensional proof is the beta-integral and polar-adjacency calculation above.

## Relationship to prior work
Ohsugi and Tsuchiya [1] introduced enriched chain polytopes via signed antichain indicators and studied triangulations and Ehrhart invariants. Okada and Tsuchiya [2] studied enriched transfer maps and triangulations and gave maximal-chain inequalities. These supply the underlying objects and facet setting but do not state this normalized Euclidean second-intrinsic-volume or ridge-angle classification in the material inspected. The free-sum normalized lattice-volume product [3] explains the volume factor but has no angle or curvature conclusion. The present formula derives a further metric invariant, not a lattice-volume reformulation.

## Limitations
The universality is asserted only for ordinal sums of antichains in their unscaled canonical Euclidean coordinates. It does not extend as stated to general posets, arbitrary block scalings, or higher intrinsic-volume orders. This is an internally checked proof, not an independent mathematical review or a verified priority certificate. Equivalent geometric formulas in broader free-sum literature may exist beyond the sources searched.

## References
[1] H. Ohsugi and A. Tsuchiya, *Enriched chain polytopes*, arXiv:1812.02097, first posted 2018-12-05, https://arxiv.org/abs/1812.02097 .

[2] S. Okada and A. Tsuchiya, *Two enriched poset polytopes*, arXiv:2003.12271, first posted 2020-03-27, https://arxiv.org/abs/2003.12271 .

[3] T. Chen and R. Davis, *A Product Formula for the Normalized Volume of Free Sums of Lattice Polytopes*, arXiv:1711.11130, first posted 2017-11-29, https://arxiv.org/abs/1711.11130 .
