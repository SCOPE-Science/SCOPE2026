# Dimension-independent Euclidean inballs and endpoint tangencies of chain–antichain twinned polytopes

## Finding

**Theorem (sharp inscribed-ball classification).** For every integer \(d\ge3\), set
\[
\Delta_d=\operatorname{conv}\{0,e_1,\ldots,e_d\},\qquad
P_d=\operatorname{conv}(\Delta_d\cup[-1,0]^d)\subset\mathbb R^d.
\]
The ambient metric is the standard Euclidean metric, with the coordinate vectors \(e_i\) orthonormal. Then the exact maximum Euclidean inscribed-ball radius is
\[
\boxed{r_{\mathrm{in}}(P_d)=1/\sqrt2}.
\]
The **complete** set of centers of balls having this radius is the nondegenerate segment
\[
\boxed{\left\{a\mathbf1:\quad 1/\sqrt2-1\le a\le1-\sqrt{3/2}\right\}},
\]
where \(\mathbf1=(1,\ldots,1)\). This segment has length \(\sqrt d\left(2-(\sqrt6+\sqrt2)/2\right)\) in Euclidean distance; its interval of scalar coordinates is independent of \(d\).

Every optimal ball is tangent to the \(d(d-1)\) facets \(x_i-x_j=1\) for ordered distinct \(i,j\). At the lower endpoint it is additionally tangent to exactly the \(d\) facets \(-x_j=1\). At the upper endpoint it is additionally tangent to exactly the \(d\binom{d-1}{2}\) facets \(x_i+x_k-x_j=1\), for distinct \(i,k,j\) with the two positive indices unordered. At strict interior scalar values there are no other facet tangencies.

The largest ball **constrained to be centered at the origin** has radius \(1/\sqrt d\), a factor of \(\sqrt{d/2}\) smaller than the unrestricted inradius. Neither the known facet count nor this elementary origin-centered radius alone determines the above nonunique optimal-center locus and endpoint contact changes.

## Assumptions and scope

The domain is exactly the infinite family of mixed chain–antichain twinned chain polytopes in the displayed standard coordinate realization, in integer dimensions \(d\ge3\). By the standard definitions, \(\Delta_d\) is the chain polytope of a total-order poset and \([0,1]^d\) is the chain polytope of an antichain; their signed convex hull is \(P_d\). Both the Euclidean metric and the placement in coordinates are essential. The theorem makes no assertion of the same radius under general linear changes of coordinates, nor for arbitrary poset pairs. The separate two-dimensional endpoint behavior is intentionally outside the claim.

A facet tangency means that the Euclidean ball touches the facet's supporting hyperplane (hence the facet itself, since the ball is contained in the full polytope). The contact counts are numbers of distinct facets, not numbers of boundary points.

## Proof

**Step 1 — reconstruct all supporting inequalities.** The origin lies in the interior of \(P_d\). For a vector \(y\), the polar conditions for \(\Delta_d\) and the negative cube are
\[
y_i\le1\quad(1\le i\le d),\qquad
\sum_{i=1}^{d}\max(0,-y_i)\le1.
\]
Fixing the signs of the coordinates, the negative-coordinate part is a simplex and every positive-coordinate part is an interval. Hence the vertices of this polar are among \(\mathbf1_S\) and \(\mathbf1_S-e_j\) with \(j\notin S\). For each proper subset \(S\ne[d]\), choosing \(j\notin S\) gives
\[
\mathbf1_S=\tfrac12\bigl(\mathbf1_{S\cup\{j\}}+\mathbf1_S-e_j\bigr),
\]
so these \(\mathbf1_S\) are not vertices. Conversely, \(\mathbf1\) is exposed by the sum of all coordinates, and each \(\mathbf1_S-e_j\) is exposed by a functional that heavily rewards the coordinates in \(S\), heavily penalizes coordinate \(j\), and mildly penalizes the remaining coordinates. Therefore, the full irredundant facet list of \(P_d\) is
\[
\sum_{i=1}^d x_i\le1,
\qquad \sum_{i\in S}x_i-x_j\le1
\quad(j\in[d],\ S\subseteq[d]\setminus\{j\}).\tag{1}
\]
There are \(1+d2^{d-1}\) facets. This count and the general facet construction are already established in the literature; the argument is included to fix normalization, directions, and equality cases, not to claim facet novelty.

**Step 2 — bound the radius and force all centers to the diagonal.** A Euclidean ball \(c+rB_2^d\) satisfies \(u\cdot x\le1\) precisely if
\[
u\cdot c+r\|u\|_2\le1.\tag{2}
\]
For every ordered pair of distinct indices \(i,j\), (1) includes both normals \(e_i-e_j\) and \(e_j-e_i\). Adding their conditions (2) yields \(2\sqrt2\,r\le2\), i.e. \(r\le1/\sqrt2\). If equality holds, both conditions require \(c_i=c_j\). Thus any radius-maximizing center, if the bound is attainable, must have the form \(c=a\mathbf1\).

**Step 3 — prove the complete diagonal interval is feasible.** Set \(r=1/\sqrt2\) and \(c=a\mathbf1\). A facet in (1) with \(s=|S|\) has unit-offset condition
\[
g_a(s)=(s-1)a+\sqrt{(s+1)/2}\le1\qquad(s=0,\ldots,d-1),\tag{3}
\]
while the all-ones facet gives
\[
h_a(d)=da+\sqrt{d/2}\le1.\tag{4}
\]
The condition at \(s=0\) is equivalent to \(a\ge a_-=1/\sqrt2-1\). At \(s=1\), equality holds identically. At \(s=2\), admissible because \(d\ge3\), condition (3) becomes \(a\le a_+=1-\sqrt{3/2}\).

The interval is nonempty since \(\sqrt6+\sqrt2<4\), equivalent upon squaring to \(\sqrt3<2\). For \(a\le a_+\) and real \(s\ge2\),
\[
\frac{\partial g_a}{\partial s}=a+\frac1{2\sqrt{2(s+1)}}\le1-\frac{5\sqrt6}{12}<0,
\]
where the final strict inequality is \(25\cdot6>12^2\). Thus every facet with \(s\ge2\) obeys \(g_a(s)\le g_a(2)\le1\), and the inequality is strict when \(s>2\). Similarly, for real \(d\ge3\), \(\partial h_a/\partial d\le1-5\sqrt6/12<0\). Therefore
\[
h_a(d)\le h_{a_+}(3)=3-\sqrt6<1.
\]
All inequalities (1) hold for the ball when and only when \(a_-\le a\le a_+\). Combined with Step 2, this proves the exact inradius and complete center locus.

**Step 4 — classify every contact facet, including endpoints.** Equation (3) has equality at \(s=1\) for all admissible \(a\); these are exactly the \(d(d-1)\) ordered difference facets. At \(s=0\), equality holds exactly at \(a=a_-\), yielding \(d\) additional facets. At \(s=2\), equality holds exactly at \(a=a_+\), yielding \(d\binom{d-1}{2}\) additional facets. For \(s>2\) the strict monotonicity proved above excludes equality, and (4) is always strict. These exhaust (1), so the classification is complete.

**Step 5 — quantify the intrinsic benefit of recentering.** At the origin, the largest admissible radius is \(1/\max_u\|u\|_2\) over the facet normals in (1). Those norms are \(\sqrt d\) for the all-ones facet and at most \(\sqrt d\) for every other facet, proving that the origin-centered radius is \(1/\sqrt d\). The ratio \((1/\sqrt2)/(1/\sqrt d)=\sqrt{d/2}\) follows. \(\square\)

## Verification

The accompanying standalone `verify_metric.py` enumerates every cube corner and simplex apex and every candidate supporting normal for dimensions \(3\le d\le7\), checks exact integral support values, checks every facet has full relative dimension through \(d=5\), and verifies all scalar inball barriers and tangent-facet counts at both endpoints and an interior center. Its actual package-path replay succeeded with **79,635** checks. Symbolic radical comparisons use SymPy; a precision fallback is employed only if SymPy cannot decide a strictly nonzero comparison. The all-dimensional conclusion rests on Steps 1–5, not finite testing.

## Relationship to prior work

Tsuchiya's *Volume, facets and dual polytopes of twinned chain polytopes* (2015 preprint) introduced and analyzed the relevant signed convex-hull construction and its general facet structure. Mori, Mori, and Ohsugi's *Facet numbers of non-centrally symmetric reflexive polytopes arising from posets* (2025 preprint, later journal publication) explicitly discusses the mixed chain–antichain case and cites the known facet count \(1+d2^{d-1}\). Neither of those inspected full texts determines the exact Euclidean inradius, the full line segment of optimal centers, or its distinct endpoint tangencies.

The minimum enclosing sphere of the **terminal-simplex subpolytope** \(\operatorname{conv}\{-\mathbf1,e_1,\ldots,e_d\}\) has previously been determined. That sphere-related prior result is not the subject of this theorem and is not treated as a separate novelty claim. General results on differently defined order, enriched-chain, signed-chain, or centrally symmetric cube-derived polytopes likewise do not imply (2)–(4) without an identification of the present facet normals.

## Limitations

This is a self-review, not an independent audit or a claim of established historical priority. The proof uses the specified standard Euclidean realization; affinely equivalent polytopes need not have the same insphere. The exact facet list was known before this work and is not claimed new. A differently indexed theorem specifically covering these metric center and contact statements could change priority. The finite checks have finite ranges and do not certify the infinite-dimensional index family.

## References

1. A. Mori, K. Mori, and H. Ohsugi, *Facet numbers of non-centrally symmetric reflexive polytopes arising from posets*, arXiv:2511.22981, initial public preprint 2025-11-28, https://arxiv.org/abs/2511.22981.
2. A. Tsuchiya, *Volume, facets and dual polytopes of twinned chain polytopes*, arXiv:1512.08332, initial public preprint 2015-12-28, https://arxiv.org/abs/1512.08332.
