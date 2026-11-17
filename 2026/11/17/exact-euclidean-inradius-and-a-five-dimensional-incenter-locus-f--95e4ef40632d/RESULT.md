# Exact Euclidean inradius and a five-dimensional incenter locus for the four-node bounded-imset polytope

## Finding

Let \(P\subset\mathbb R^{10}\) be the degree-two-bounded characteristic-imset polytope on four labeled nodes. Thus \(P\) is the convex hull of the characteristic imsets of all directed acyclic graphs \(G\) on \([4]\) whose vertices have at most two parents. Coordinates are indexed by the six pairs \(ij\) and four triples \(ijk\) of \([4]\); the fourth-order characteristic-imset coordinate vanishes identically. Equip this explicit coordinate space with its ordinary Euclidean metric.

**Theorem.** The radius of a largest closed Euclidean ball contained in \(P\) is exactly
\[
 r_* = \frac{3}{4+\sqrt{22}+\sqrt{10}}
      =0.2531070275503737\ldots .
\]
One center \(c_*\) has all pair coordinates equal to
\[
 t_* =\frac{8+\sqrt{22}}6r_*=0.5353389018912209\ldots,
\]
and all four triple coordinates equal to \(r_*\). Its ball touches precisely six of the 94 facets: the four triple-coordinate nonnegativity facets, the complete-four-node connected-graph path facet, and the complete-four-node clique facet. Every other facet has Euclidean supporting-hyperplane clearance strictly greater than \(r_*+9/200\) at \(c_*\).

The locus \(\mathcal I\) of **all** centers of largest inscribed balls is a five-dimensional convex polytope (not a singleton). More explicitly, writing \(E\) for the six pairs, \(T\) for the four triples, and \(\mathcal H_{94}\) for the explicitly specified irredundant facet inequalities \(a\cdot x\le b\) from the cited complete description (reconstructed by the standalone checker),
\[
 \mathcal I = \left\{x\in\mathbb R^{10}:\;
 x_{ijk}=r_*\ \text{for every }ijk\in T,\quad
 \sum_{ij\in E}x_{ij}=(8+\sqrt{22})r_*,\quad
 a\cdot x+r_*\|a\|_2\le b\ \text{for every }(a,b)\in\mathcal H_{94}
 \right\}.
\]
This exact half-space description has affine dimension five. Every center in \(\mathcal I\) has the six specified facet contacts; a center in its relative interior has **exactly** those six contacts. Other centers on the boundary can acquire additional contacts.

## Assumptions and scope

The characteristic imset of a directed acyclic graph \(G\) has pair coordinate \(c_G(ij)=1\) exactly when \(i,j\) are adjacent (in either direction), and triple coordinate \(c_G(ijk)=1\) exactly when one of the triple's nodes has both others as parents. No coordinate rescaling or quotient metric is used. The graph class has **four labeled nodes and maximum indegree two**. Its 150 distinct characteristic-imset vertices span the full ten-dimensional ambient space. The full 94-facet \(\mathcal H\)-representation is established in Coons–Hollering–Chakrabarty Paul (2026), using connected-graph path, tree, clique, disconnected-support, and elementary triple inequalities. That completeness is an input rather than a new result here.

An inscribed ball of radius \(r\ge0\) and center \(x\) meets the facet condition \(a\cdot x+r\|a\|_2\le b\) for each \(a\cdot y\le b\). The result concerns the metric in the ten characteristic-imset coordinates as given, rather than a metric on equivalence classes of Bayesian networks or an intrinsic statistical metric.

## Proof

**1. Six universal upper-bound inequalities.** For each triple \(ijk\subset[4]\), \(x_{ijk}\ge0\) is a facet. Thus, for a radius-\(r\) ball center \(x\), every triple coordinate is at least \(r\), whence
\[
 T_x:=\sum_{i<j<k}x_{ijk}\ge4r.
\]
The path facet arising from the complete graph on four nodes is
\[
 -\sum_{i<j}x_{ij}+2\sum_{i<j<k}x_{ijk}\le0.
\]
Its coefficient vector has six entries \(-1\) and four entries \(2\), so squared Euclidean norm \(22\). Setting \(S_x:=\sum_{i<j}x_{ij}\), any radius-\(r\) ball center satisfies
\[
 S_x\ge2T_x+\sqrt{22}\,r.
\]
The clique facet of the same four nodes is
\[
 \sum_{i<j}x_{ij}-\sum_{i<j<k}x_{ijk}\le3.
\]
Its normal has squared norm \(10\). Therefore
\[
 S_x\le3+T_x-\sqrt{10}\,r.
\]
Combining the two bounds yields
\[
 4r\le T_x\le3-(\sqrt{22}+\sqrt{10})r,
\]
and hence \(r\le r_*\), for **every** center, with no symmetry assumption.

**2. A ball attaining the bound.** Define \(c_*\) by \((c_*)_{ij}=t_*\) on all six pairs and \((c_*)_{ijk}=r_*\) on all four triples. Its four nonnegativity conditions, complete-graph path condition, and complete-graph clique condition are tight for an inscribed ball of radius \(r_*\), by direct substitution:
\[
 6t_*=(8+\sqrt{22})r_*,\qquad
 (4+\sqrt{22}+\sqrt{10})r_*=3.
\]
It remains to verify the other 88 inequalities. The complete facet system has 18 orbits under relabeling the four nodes. For a representative facet \(a\cdot x\le b\), write \(E_a=\sum_{ij}a_{ij}\), \(U_a=\sum_{ijk}a_{ijk}\), and \(N_a=\|a\|_2^2\). The relevant margin is exactly
\[
 b-E_at_*-U_ar_*-\sqrt{N_a}\,r_*.
\]
The following table gives all distinct signatures \((E_a,U_a,N_a,b)\), with facet multiplicities. The three rows marked yes are tight; all other rows have strictly positive margins. The table and the complete coefficient vectors are regenerated by the checker using the source's explicit facet families.

| \(E_a\) | \(U_a\) | \(N_a\) | \(b\) | Facets | Contact? |
|---:|---:|---:|---:|---:|:---:|
| -6 | 8 | 22 | 0 | 1 | yes |
| -5 | 6 | 15 | 0 | 6 | no |
| -4 | 4 | 8 | 0 | 3 | no |
| -4 | 4 | 10 | 0 | 12 | no |
| -3 | 2 | 5 | 0 | 12 | no |
| -3 | 2 | 7 | 0 | 4 | no |
| -3 | 3 | 6 | 0 | 4 | no |
| -3 | 5 | 10 | 1 | 4 | no |
| -2 | 1 | 3 | 0 | 12 | no |
| -1 | 0 | 1 | 0 | 6 | no |
| 0 | -1 | 1 | 0 | 4 | yes |
| 0 | 1 | 1 | 1 | 4 | no |
| 0 | 4 | 4 | 2 | 1 | no |
| 1 | 0 | 1 | 1 | 6 | no |
| 1 | 2 | 3 | 2 | 6 | no |
| 3 | -1 | 4 | 2 | 4 | no |
| 3 | 1 | 4 | 3 | 4 | no |
| 6 | -4 | 10 | 3 | 1 | yes |

To certify strict positivity without floating-point inference, the checker bounds each square root \(\sqrt m\) between \(\lfloor10^{10}\sqrt m\rfloor/10^{10}\) and that rational number plus \(10^{-10}\), with the integer floor computed by exact integer square root. Propagating the resulting rational interval bounds for \(r_*\), \(t_*\), and each of the 88 inequalities proves the stronger strict bound
\[
 b-E_at_*-U_ar_*>\left(r_*+\frac9{200}\right)\sqrt{N_a}
\]
for every noncontact facet. Hence the radius-\(r_*\) ball is contained in \(P\), and the upper bound is attained.

**3. All centers and their dimension.** If a center \(x\) attains \(r_*\), equality throughout Step 1 forces \(T_x=4r_*\). Since each triple coordinate is at least \(r_*\), each is exactly \(r_*\). Equality in the two global inequalities gives \(S_x=(8+\sqrt{22})r_*\). The remaining conditions for a valid radius-\(r_*\) ball are precisely the inequalities defining \(\mathcal I\) in the theorem. They fix the four triple coordinates and one independent sum of the six pair coordinates, so the affine dimension is at most five. At the symmetric center \(c_*\), each of the other 88 facet conditions is *strict*, as established in Step 2. Therefore a sufficiently small open neighborhood of \(c_*\) inside the five-dimensional affine slice is feasible. Thus the dimension is exactly five. Strictness also establishes the claimed six-contact count at \(c_*\) and throughout the relative interior.

## Verification

Execute the embedded standard-library Python 3 script `check_geometry.py`. It enumerates all facet normals from the complete published constructions (94 distinct coefficient/right-side pairs), enumerates and deduplicates characteristic imsets of all four-node indegree-at-most-two DAGs (150 vertices), and verifies exact integral validity of every inequality on every vertex. Modular nonzero-rank witnesses confirm affine dimension ten and verify that every reconstructed inequality supports a nine-dimensional facet. The script also certifies with *rational interval arithmetic* that all 88 noncontact facets have Euclidean clearance at least \(9/200\) above the proposed inradius. The analytical proof above, together with the published completeness of the facet list, establishes the result for all possible ball centers; the finite certificate performs only genuinely finite algebra.

## Relationship to prior work

Coons, Hollering, and Chakrabarty Paul (2026) introduce degree-bounded characteristic-imset polytopes, establish their dimensions, list the 150 vertices and 94 facets in the four-node indegree-two case, and prove completeness of the relevant facet constructions. This work uses that published geometry as its input. It adds the exact Euclidean inradius, six-contact pattern, quantitative noncontact clearance, and five-dimensional family of optimal centers, none of which are stated in that source.

Xi and Yoshida (2012/2015) describe characteristic-imset polytopes for ordered-node and diagnosis models and obtain products of simplices in particular cases. Fixed-order/diagnosis polytopes differ from the present unrestricted-order, bounded-indegree four-node polytope. General algorithms for Chebyshev centers apply to any given facet system, but do not provide these explicit parameters or the present nonuniqueness classification. A search of relevant mathematical records found no directly equivalent theorem; historical priority cannot be guaranteed and should be checked independently.

## Limitations

This is an exact result for one canonical, first nontrivial member of the degree-two-bounded characteristic-imset family, not a formula for arbitrary node count. The full incenter set is characterized exactly by an affine slice and 94 explicitly generable metric-offset inequalities; no claim about its complete face vector is made. The Euclidean metric depends on the original characteristic-imset coordinates. The geometric finding does not imply a statistical learning rate or performance guarantee. Independent validation and historical-priority certification have not been performed.

## References

1. J. I. Coons, B. Hollering, N. Chakrabarty Paul, *Polyhedral Geometry of Degree-Bounded Characteristic Imset Polytopes*, arXiv:2611.09633, first released 2026-11-06. Theorems 4.6, 5.2, 6.3, 6.6; Proposition 6.5; Section 7.
2. J. Xi, R. Yoshida, *The characteristic imset polytope of Bayesian networks with ordered nodes*, arXiv:1206.0406 (2012); SIAM Journal on Discrete Mathematics 29 (2015), 697–715.
3. J. Cussens, D. Haws, M. Studený, *Polyhedral aspects of score equivalence in Bayesian network structure learning*, Mathematical Programming 164 (2017), 285–324, originally public 2016.
