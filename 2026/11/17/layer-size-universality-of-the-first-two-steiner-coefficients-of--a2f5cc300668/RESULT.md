# Layer-size universality of the first two Steiner coefficients of layered chain polytopes

## Finding
Let \(r\ge3\), let \(m_1,\ldots,m_r\ge2\) be integers, and write \(n=\sum_{a=1}^r m_a\). For the standard Euclidean chain polytope \(C\subset\mathbb R^n\) of the ordinal sum of antichains with these sizes, the following *full-dimensional* intrinsic-volume identities hold:
\[
\frac{\operatorname{Area}_{n-1}(\partial C)}{\operatorname{Vol}_n(C)}=n(r+\sqrt r),
\]
\[
\frac{V_{n-2}(C)}{\operatorname{Vol}_n(C)}=
 n(n-1)\left(\frac{r^2}{8}+\frac{r\sqrt r}{4}
 +\frac{r\sqrt{2r-1}}{4\pi}\arccos\frac{r-1}{r}\right).
\]
Here \(V_{n-2}\) is the usual Euclidean Steiner intrinsic volume, so its coefficient in \(\operatorname{Vol}_n(C+tB_2^n)\) is \(\pi V_{n-2}(C)t^2\). Neither normalized invariant depends on the individual layer sizes once their number and total dimension are fixed. The result includes a complete three-class codimension-two face census. In the boundary case \(r=2\) the same formulas hold, but the chain and order polytopes are congruent by reflection of one coordinate block; the noncongruent three-or-more-layer regime is the focus.

## Assumptions and scope
All coordinates carry the unweighted standard Euclidean metric. Write \(B_a\) for the disjoint set of \(m_a\) coordinates of the \(a\)-th antichain. The polytope is
\[
C=\left\{x\in\mathbb R_{\ge0}^{n}:\sum_{a=1}^r x_{a,i_a}\le1
\text{ for every }(i_1,\ldots,i_r)\in\prod_{a=1}^r[m_a]\right\}.
\]
Its vertices are the origin and the nonempty coordinate \(0/1\) indicators supported inside a single block. Define \(L_{a,i}\) by \(x_{a,i}=0\) and \(U_\sigma\) by \(\sum_a x_{a,\sigma_a}=1\). These and only these are facets. Thus the number of facets is \(n+\prod_a m_a\). All dimensions and areas below refer to affine spans and ordinary Euclidean Hausdorff measures.

## Proof
**1. Volume and coarea.** The polytope is the orthogonal free join of the unit cubes on the mutually perpendicular coordinate blocks. Equivalently, for \(t_a=\max_{i\in[m_a]}x_{a,i}\), all \(t_a\ge0\) and \(\sum_a t_a\le1\). Integrating \(\prod_a m_a t_a^{m_a-1}\) over this simplex gives
\[
W:=\operatorname{Vol}_n(C)=\frac{\prod_a m_a!}{n!}.
\]
Each coordinate facet \(L_{a,i}\) has area \((m_a-1)!\prod_{b\ne a}m_b!/(n-1)!\). Each maximal-chain facet \(U_\sigma\), whose outer normal has norm \(\sqrt r\), has area \(\sqrt r\prod_a(m_a-1)!/(n-1)!\). Consequently their aggregate areas divided by \(W\) are \(nr\) and \(n\sqrt r\), respectively, proving the surface-area identity.

**2. Exhaustive ridge classification.** Every ridge is the intersection of two distinct facets of these types, and all such pairs are classified as follows. An \(L\)-\(L\) pair always defines a ridge. An \(L_{a,i}\)-\(U_\sigma\) pair defines a ridge precisely when \(i\ne\sigma_a\). If \(i=\sigma_a\), the other \(m_a-1\) entries in block \(a\) vanish on the intersection; with \(m_a\ge2\) this has codimension at least three. Finally, an \(U_\sigma\)-\(U_\tau\) pair defines a ridge precisely when the chains differ in exactly one block. If they differ in two or more blocks, their crossed replacements are also valid upper inequalities. Equality in both original inequalities forces equality of at least two coordinate pairs, in addition to one upper sum constraint, so codimension is at least three. For a single differing block, equality of the two selected entries and the shared upper sum gives exactly codimension two. The positive-coordinate point with the selected entries tied and every other entry strictly lower verifies that no additional inequality is forced. This also proves that no ridge types are omitted.

**3. Metric measures.** Divide the sum of \((n-2)\)-dimensional ridge areas in each class by \(n(n-1)W\). For \(L\)-\(L\), the normalized sum is \(r^2/2\): two entries in one block contribute \(1/2\) per block; two entries in distinct blocks contribute \(1\) per block pair. For \(L\)-\(U\), a selected upper-chain hyperplane has metric factor \(\sqrt r\), while removing a nonselected coordinate yields factorial measure \(\sqrt r(m_a-2)!\prod_{b\ne a}(m_b-1)!/(n-2)!\). Summing over every eligible pair yields \(r\sqrt r\).

For \(U\)-\(U\) differing in block \(a\), the two Euclidean normals have squared norms \(r\) and scalar product \(r-1\). Their normal-Gram determinant is \(r^2-(r-1)^2=2r-1\). Thus coarea gives each such ridge the exact measure
\[
\sqrt{2r-1}\,\frac{(m_a-2)!\prod_{b\ne a}(m_b-1)!}{(n-2)!}.
\]
There are \(\binom{m_a}{2}\prod_{b\ne a}m_b\) such pairs with changing block \(a\). After summing over blocks, the normalized aggregate measure is \(r\sqrt{2r-1}/2\). These factorial cancellations account for independence from the size profile.

**4. Exterior angles and the Steiner coefficient.** Every ridge of type \(L\)-\(L\) or eligible \(L\)-\(U\) has exterior dihedral angle \(\pi/2\), because its two outward facet normals are orthogonal. An \(U\)-\(U\) ridge has exterior angle \(\alpha_r=\arccos((r-1)/r)\). The standard polyhedral local Steiner formula in codimension two is
\[
V_{n-2}(C)=\sum_{\text{ridges }F}\frac{\alpha_F}{2\pi}\operatorname{Vol}_{n-2}(F).
\]
Inserting the three area aggregates gives the boxed identity without any asymptotic or enumeration hypothesis.

## Verification
Two standalone Python 3 scripts accompany this result. `check_chain_ridges.py` reconstructs all vertices and the complete facet system, verifies every facet-pair ridge criterion by direct affine ranks for nine layer profiles, and confirms 1,023 ridges. `check_chain_metric.py` independently uses SciPy convex hulls in each affine ridge span, verifies each of 268 ridge measures across five profiles against the factorial/Gram formulas, checks exact total Euclidean volume, and confirms the three aggregate ratios. These are independent finite checks of the all-parameter analytic proof; no finite experiment is used to prove an infinite statement. Run `python check_chain_ridges.py` and `python check_chain_metric.py` with Python 3, NumPy, and (for the second script) SciPy.

## Relationship to prior work
Ahmad, Fourier and Joswig (2023), *Order and chain polytopes of maximal ranked posets*, arXiv:2309.01626, establish the maximal-ranked-poset context and its combinatorial face descriptions, including the facet inequalities used here; their objective is the face-vector comparison, not metric ridge measures or Steiner coefficients. Mori (2024), *Triangular faces of the order and chain polytope of a maximal ranked poset*, arXiv:2404.00263, determines a class of two-dimensional face counts, not the Euclidean measures and angles of codimension-two faces. The present conclusion does not follow from a face-vector identity alone because the metric normal-Gram determinants and factorial face volumes enter essentially. For comparison, the corresponding Euclidean order polytopes of three or more layers have different boundary-area and second-Steiner formulas despite Ehrhart equivalence; the two-layer equality is explained by an orthogonal reflection.

## Limitations
The exact formulas require the canonical *unweighted* coordinate Euclidean metric and all layer sizes at least two. They give the first two nonleading Steiner coefficients, not the full intrinsic-volume sequence; no statement is made about arbitrary ranked posets, weighted layers, or independently validated priority. The verified literature/record searches do not establish absolute novelty, and an uncatalogued equivalent formula remains possible. Independent mathematical audit has not been performed.

## References
1. I. Ahmad, G. Fourier and M. Joswig, *Order and chain polytopes of maximal ranked posets*, arXiv:2309.01626, first version 2023-09-04, https://arxiv.org/abs/2309.01626.
2. A. Mori, *Triangular faces of the order and chain polytope of a maximal ranked poset*, arXiv:2404.00263, first version 2024-03-30, https://arxiv.org/abs/2404.00263.
3. R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23; classical definitions, vertex characterization, and Ehrhart equivalence.
4. R. Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, second edition, 2014; standard Steiner formula and codimension-two exterior-angle weights.
