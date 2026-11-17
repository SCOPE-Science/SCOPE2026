# Linear facet complexity and cube-scale inballs in low-expansion Boolean Cayley polytopes

## Finding
Let \(k\ge2\) and \(n\ge1\) be integers. Set \(C_k=[0,1]^k\), \(D_k=\operatorname{conv}(0,e_1,\ldots,e_k)\), and define the full-dimensional Euclidean polytope
\[
P_{n,k}=\operatorname{conv}\bigl((C_k^n\times D_k^n)\times\{0\}\;\cup\;(D_k^n\times C_k^n)\times\{1\}\bigr)\subset\mathbb R^{2kn+1}.
\]
Its complete, irredundant facet presentation is \(0\le t\le1\), nonnegativity of all \(2kn\) block coordinates, and, for each nonempty \(S\subseteq[k]\), the inequalities
\[
 \sum_{j\in S}x_{b,j}+(|S|-1)t\le |S|\quad(1\le b\le n),\qquad
 \sum_{j\in S}x_{b,j}-(|S|-1)t\le1\quad(n<b\le2n).
\]
Consequently the exact number of facets is
\[
 f_{2kn}(P_{n,k})=2n(2^k+k-1)+2.
\]
Put \(L_k=\sqrt{k^2-k+1}\). Its Euclidean inradius and **unique** incenter are
\[
 r_k=\frac{k+1}{2(k+L_k)},\qquad c_{n,k}=(r_k\mathbf1_{2kn},1/2).
\]
Exactly \(2n(k+1)\) facets touch the maximum inscribed ball: the \(2kn\) coordinate-zero facets and the \(2n\) full-block subset facets \(S=[k]\). The radius does not depend on \(n\), decreases strictly with \(k\), and tends to \(1/4\) as \(k\to\infty\).

The Euclidean diameter is \(\sqrt{2kn+1}\), with exactly \((k+1)^{2n}\) unordered diametral vertex pairs, each a complementary pair of Boolean vectors in opposite Cayley layers. The unique minimum-enclosing ball is centered at \(\mathbf1_{2kn+1}/2\), has radius \(\sqrt{2kn+1}/2\), and contacts all \(2(2^k(k+1))^n\) vertices.

Writing
\[
 V_k(t)=\sum_{j=0}^k\binom kj\frac{(1-t)^{k-j}t^j}{j!},
\]
the exact ambient Euclidean volume is
\[
 \operatorname{vol}_{2kn+1}(P_{n,k})=\int_0^1[V_k(t)V_k(1-t)]^n\,dt.
\]
For the original square–triangle case \(k=2\), this becomes
\[
 \operatorname{vol}_{4n+1}(P_{n,2})\sim
 \frac{7\sqrt\pi}{6\sqrt{2n}}\left(\frac{49}{64}\right)^n.
\]
The original \(k=2\) family therefore has only \(10n+2\) facets in dimension \(4n+1\) and inradius \(3/[2(2+\sqrt3)]\), more than \(80\%\) of the inradius of its ambient unit cube. This is compatible with, but geometrically distinct from, the exponentially small graph edge expansion established for that family in the source paper.

## Assumptions and scope
All coordinate lengths and volumes are Euclidean, with no affine rescaling. The two block groups have exactly \(n\) blocks each. A vertex means an extreme point; the Boolean vertex set comprises all products of the cube and simplex vertex sets in each layer. The parameter range is all integers \(k\ge2\), \(n\ge1\). The statement does **not** assert that higher-\(k\) family members have the original author's graph-expansion rate; that rate is cited for \(k=2\) only.

## Proof
**1. Complete slicing and facets.** At height \(0\le t\le1\), the section is the Cartesian product of \(n\) copies of \(K_t=(1-t)C_k+tD_k\) and \(n\) copies of \(K_{1-t}\). For \(a=1-t\), a vector \(z\in\mathbb R^k\) belongs to \(K_t\) precisely when \(z_i\ge0\) and \(\sum_{i\in S}z_i\le a|S|+t\) for every nonempty \(S\subseteq[k]\). The forward direction follows by taking subset sums in the cube and simplex. Conversely, set \(u_i=\min(z_i,a)\), \(v_i=(z_i-a)_+\). Applying the displayed subset bound to \(S=\{i:z_i>a\}\) yields \(\sum v_i\le t\), hence \(u\in aC_k\), \(v\in tD_k\), and \(z=u+v\). (If that set is empty, the conclusion is immediate.) Substituting \(a=1-t\) and then replacing \(t\) by \(1-t\) gives the asserted global inequalities.

The polytope contains the origin and every coordinate unit vector, so it is full-dimensional. Each of its proposed inequalities defines a facet: at \(t\in(0,1)\), every lower coordinate face and each singleton-upper-coordinate face of \(K_t\) has dimension \(k-1\). For a subset \(S\) of size \(s\ge2\), a maximizing point has \(u_i=a\) for all \(i\in S\), a simplex mass \(t\) distributed strictly positively among those \(s\) positions, and the remaining \(k-s\) coordinates varying independently in \((0,a)\); this is a face of dimension \((s-1)+(k-s)=k-1\). Allowing \(t\) to vary adds one dimension, while the other \(2n-1\) blocks vary freely. The faces \(t=0\), \(t=1\) are full-dimensional layer products. Thus all listed inequalities are genuine distinct facets, and because they define the polytope there are no others. Counting gives \(2kn+2n(2^k-1)+2\).

**2. Exact inball and uniqueness.** Let a ball of radius \(r\) centered at \((x,t)\) lie in the polytope. Distances to the coordinate-zero supporting facets require every block coordinate to be at least \(r\). The full-set facet normal has Euclidean length \(L_k=\sqrt{k+(k-1)^2}\). From any first-group and any second-group full-set facets,
\[
 (k+L_k)r\le k-(k-1)t,\qquad
 (k+L_k)r\le1+(k-1)t.
\]
The minimum of the two right-hand sides is at most \((k+1)/2\), giving \(r\le r_k\). Equality forces \(t=1/2\), and then equality in every full-set inequality and the lower-coordinate bounds forces every block coordinate to equal \(r_k\). Thus there can be only one incenter.

To see that this center works, for integer \(s\ge1\) let
\[
 r_s=\frac{s+1}{2\left(s+\sqrt{s^2-s+1}\right)}.
\]
The function \((x+\sqrt{x^2-x+1})/(x+1)\) is strictly increasing on \([1,\infty)\): the derivatives of its two summands \(x/(x+1)\) and \(\sqrt{x^2-x+1}/(x+1)\) are respectively \(1/(x+1)^2\) and \(3(x-1)/[2(x+1)^2\sqrt{x^2-x+1}]\). Hence \(r_s\) strictly decreases with \(s\). At the proposed center, normalized distance to each size-\(s\) subset facet is \((s+1-2sr_k)/(2\sqrt{s^2-s+1})\), at least \(r_k\) precisely because \(r_k\le r_s\). Lower-coordinate facet distance is exactly \(r_k\), while upper-singleton and \(t\)-endpoint distances are strictly larger because \(r_k<1/2\). Equality among subset facets occurs exactly for \(s=k\), proving the contact count.

**3. Diameter and enclosing sphere.** The polytope lies in the unit Boolean cube in dimension \(d=2kn+1\), so no pair of points can be farther apart than \(\sqrt d\). A complementary pair of vertices from opposite layers exists: in each first-group cube block choose any vector whose complement belongs to the simplex vertex set (there are \(k+1\) choices), and in each second-group simplex block choose any simplex vertex (again \(k+1\) choices). Every diametral pair must differ in every Boolean coordinate, including the layer coordinate; therefore the stated enumeration is exhaustive. Opposite vertices have midpoint \(\mathbf1_d/2\) and mutual distance \(\sqrt d\), forcing every enclosing ball to have radius at least \(\sqrt d/2\). The radius-\(\sqrt d/2\) ball at their midpoint contains every Boolean vertex and is uniquely minimizing. Every vertex touches its boundary.

**4. Volume and asymptotics.** At height \(t\), classify a point of \(K_t\) by the subset of coordinates exceeding \(1-t\). If this subset has size \(j\), the excess coordinates form a \(j\)-simplex of volume \(t^j/j!\), while the other coordinates range independently over intervals of length \(1-t\). Summing over the \(\binom kj\) subsets gives \(V_k(t)\). Products and Fubini yield the asserted volume integral. When \(k=2\), \(V_2(t)=1-t^2/2\); with \(t=1/2+s\), the product \(V_2(t)V_2(1-t)\) equals \(49/64-9s^2/8+s^4/4\). Its unique nondegenerate maximum on \([-1/2,1/2]\) occurs at \(s=0\); the quadratic term of its logarithm is \(-72s^2/49\). The standard one-dimensional Laplace estimate gives the displayed sharp equivalent with Gaussian factor \(\sqrt{49\pi/(72n)}\).

## Verification
The standalone `verify_geometry.py` independently enumerates all Boolean-layer vertices, checks every proposed facet inequality and its affine facet rank, solves the inscribed-ball linear program with all normalized supporting inequalities, counts complementary diametral pairs, checks independent convex-hull facet counts for three small dimensions, and compares computed convex-hull volumes with exact rational integrations. Test cases are \((k,n)=(2,1),(2,2),(3,1),(3,2),(4,1)\). On replay it reported **103232 passed finite assertions**. These finite checks corroborate the closed proofs above, not the all-parameter quantifiers by enumeration.

## Relationship to prior work
The Boolean Cayley construction, full-dimensionality, vertex-set characterization, cross-layer edge criterion, and exponentially poor graph edge expansion for \(k=2\) are due to Xiongxin Yang, *0/1-Polytopes with Exponentially Small Edge Expansion*, arXiv:2608.01870v1 (3 August 2026). The general cube/simplex block option for higher \(k\) is also explicitly mentioned in that work. The new subject here is the **complete minimal facet description, exact inball contact geometry, diameter-pair classification, and exact volume** of that realization. The present facet proof is compatible with general Cayley/Minkowski support principles; it makes no claim to invent that method. Qu and Lee, arXiv:2610.35668 (26 October 2026), discuss facet normals of a different, Stanley-triangulation Cayley construction. The results there do not directly give the displayed facet counts or metric formulas here. Published general Minkowski-sum and Cayley-sum results are likewise not claimed as new.

## Limitations
Historical originality is conditional on the literature and mathematical records inspected; search absence is not a proof of global novelty. The original v1 preprint was read through its legally available full-text transcription, including construction, edge analysis, and conclusions. The updated v2 full text was not available for material comparison; although search results describe the same construction, an unreported equivalent result in the update cannot be excluded. The related Qu–Lee paper was available at abstract level only and is not represented as full-text inspected. The exact asymptotic volume equivalent is established for \(k=2\); no general \(k\)-asymptotic constant is asserted. No new graph-expansion bound is proved in this note. Independent validation has not been performed.

## References
1. Xiongxin Yang, *0/1-Polytopes with Exponentially Small Edge Expansion*, arXiv:2608.01870v1, first public 2026-08-03; accessible full text: https://www.researchgate.net/publication/411181285_01-Polytopes_with_Exponentially_Small_Edge_Expansion .
2. Yushan Qu and Jon Lee, *On the facets of the Cayley polytope of Stanley's triangulation*, arXiv:2610.35668, 2026-10-26; abstract: https://arxiv.org/abs/2610.35668 .
3. Akiyoshi Tsuchiya, *Cayley Sums and Minkowski Sums of Lattice Polytopes*, SIAM Journal on Discrete Mathematics 37 (2023), DOI:10.1137/22M1507991 (general background).
4. Peter Gritzmann and Bernd Sturmfels, *Minkowski Addition of Polytopes: Computational Complexity and Applications to Gröbner Bases*, SIAM Journal on Discrete Mathematics, DOI:10.1137/0406019 (general background).
