# Sharp inball parity and complete incenter loci of complete-bipartite symmetric edge polytopes

## Finding
Let \(p,q\ge2\), \(N=p+q\), \(h=\max(p,q)\), \(\ell=\min(p,q)\), and \(\varepsilon=h\bmod2\). Define the intrinsic Euclidean symmetric edge polytope
\[
P_{p,q}=\operatorname{conv}\{\pm(e_i-e_{p+j}):1\le i\le p,\ 1\le j\le q\}\subset H,
\qquad H=\left\{x\in\mathbb R^N:\sum_{i=1}^{N}x_i=0\right\}.
\]
The **sharp Euclidean inradius** is
\[
\boxed{r_{p,q}=\left(h-\frac{\varepsilon}{N}\right)^{-1/2}.}
\]
Write
\[
B_h=\begin{cases}
\binom h{h/2},&h\text{ even},\\
2\binom h{(h-1)/2},&h\text{ odd}.
\end{cases}
\]
The largest ball centered at the origin contacts **exactly** \(B_h\) facets if \(p\ne q\) and exactly \(2B_h\) facets if \(p=q\).

The affine dimensions of the sets of *all* centers of maximum-radius balls are, respectively,
\[
\boxed{\dim\operatorname{aff}\mathcal I_{p,q}=
\begin{cases}
\ell,&p\ne q,\ h\text{ even},\\
\ell-1,&p\ne q,\ h\text{ odd},\\
1,&p=q\text{ even},\\
0,&p=q\text{ odd}.
\end{cases}}
\]
These dimensions are exact: the center sets have nonempty relative interior in the indicated affine spaces. This is a parity-controlled transition in *nonuniqueness of optimal balls*, not a change in the combinatorial dimension of the polytope.

When the parts have unequal cardinalities, reindex so that the larger part is the first, of size \(h\). If \(h\) is even, every optimal center has the form \(c=(a\mathbf1_h,b)\), with \(ha+\sum_jb_j=0\); if \(h\) is odd, every optimal center has the form \(c=(0,b)\), with \(\sum_jb_j=0\). These are the full **affine hulls** of the center sets; the inequalities below specify which points in them are actual centers.

When \(p=q=m\) is odd, the origin is the **unique** optimal center. When \(p=q=m\) is even, the entire center set is the explicit nondegenerate segment
\[
\boxed{\mathcal I_{m,m}=
\left\{(a\mathbf1_m,-a\mathbf1_m):
|a|\le\frac{1-\sqrt{1-2/m^2}}2\right\}.}
\]

## Assumptions and scope
All inner products, Euclidean distances, ball radii, and affine dimensions are intrinsic to \(H\) with the metric inherited from \(\mathbb R^N\). A facet is a codimension-one face of \(P_{p,q}\) in \(H\), not in the full \(N\)-dimensional ambient space. The parameters are **integers** \(p,q\ge2\), and the displayed realization has unit roots. These assertions are not invariant under arbitrary nonsingular linear transformations.

For a sign vector \(\sigma\in\{\pm1\}^p\), let \(s(\sigma)=\sum_{i=1}^p\sigma_i\) and let
\[
u_\sigma=\operatorname{proj}_H(\sigma_1,\ldots,\sigma_p,0,\ldots,0).
\]
Likewise, for \(\tau\in\{\pm1\}^q\), put \(t(\tau)=\sum_j\tau_j\), and
\[
v_\tau=\operatorname{proj}_H(0,\ldots,0,\tau_1,\ldots,\tau_q).
\]
Here projection subtracts the overall coordinate average. The complete irredundant facet system, already obtainable from the published complete-bipartite facet classification, is
\[
\boxed{\langle u_\sigma,x\rangle\le1\ (\sigma\in\{\pm1\}^p),\qquad
\langle v_\tau,x\rangle\le1\ (\tau\in\{\pm1\}^q),}
\]
with just two duplicated supporting hyperplanes between the two sign families, yielding \(2^p+2^q-2\) facets in total. The duplication occurs when all signs in each corresponding part are constant and opposite. Both sides of each inequality have fixed support value one.

For explicit center membership, define \(r=r_{p,q}\). Then
\[
\boxed{\begin{aligned}
\mathcal I_{p,q}=\{c\in H:~
&|\sum_{i=1}^{p}\sigma_i c_i|\le 1-r\sqrt{p-s(\sigma)^2/N} &&(\sigma\in\{\pm1\}^p),\\
&|\sum_{j=1}^{q}\tau_j c_{p+j}|\le 1-r\sqrt{q-t(\tau)^2/N} &&(\tau\in\{\pm1\}^q)\}.
\end{aligned}}
\]
This is a finite exact inequality description for the entire optimal-center polytope, including all its boundary points.

## Proof
**1. The established facet classification, reconstructed.** The polar of \(P_{p,q}\) in \(H\) consists of potentials whose cross-part coordinate differences have absolute value at most one. A potential is extreme precisely when the bipartite graph of tight cross-part pairs is connected. The forward direction follows because tight equalities propagate across a connected graph; for the reverse direction, disconnected components can be shifted by sufficiently small opposite increments while keeping all currently slack cross inequalities strict (and then recentered in \(H\)).

If the tight graph is connected, two coordinate values in the same part differ by an even integer, along an even-length tight path. Their range is at most two by the common-neighbor triangle bound. Hence values in each part are either constant or have range two. If one part has range two, all values on the other part must coincide at the midpoint; connectivity forces every coordinate in the varying part to be one of the two extreme values. If both parts are constant, their values differ by one. Thus the polar vertices are exactly the displayed signed potentials \(u_\sigma\) and \(v_\tau\), with two duplications from the constant patterns. This also proves these supporting inequalities are facets, without assuming a polyhedral software enumeration.

**2. Euclidean support-plane distances.** Since \(u_\sigma\) is the orthogonal projection of a vector with \(p\) entries of magnitude one and total sum \(s=s(\sigma)\),
\[
\|u_\sigma\|_2^2=p-\frac{s^2}{N};
\qquad
\|v_\tau\|_2^2=q-\frac{t^2}{N}.
\]
The distance from the origin to the facet's **supporting hyperplane** is the reciprocal of the corresponding norm. Among signs of length \(m\), the smallest attainable absolute sign sum is zero if \(m\) is even and one if \(m\) is odd. For unequal part sizes, the larger part always gives the strictly greater maximum squared normal length: if the sizes differ by at least one, then \(h-1/N>h-1\ge\ell\). Thus the overall maximum squared facet-normal length is exactly \(M=h-\varepsilon/N\).

Central symmetry of \(P_{p,q}\) implies that any feasible ball with center \(c\) has an equally large feasible ball centered at \(-c\). The center-feasibility region at fixed radius is convex, so the midpoint is feasible: there is always a maximum-radius ball centered at zero. Its radius is the minimum support-plane distance, \(1/\sqrt M\), proving the asserted sharp inradius. It touches exactly the facets with maximal normal norm, since a contained ball touches its supporting plane at the ball's radial point. The near-balanced sign counts are \(B_h\); in the equal-size case the two families have no near-balanced duplication because \(m\ge2\), giving twice that number.

**3. All possible optimal centers.** The ball \(c+rB_H\) belongs to \(P_{p,q}\) exactly when \(\langle z,c\rangle+r\|z\|\le1\) for every facet normal \(z\). The normal set is antipodally symmetric, yielding precisely the absolute-value inequalities in the statement. For a facet achieving norm \(\sqrt M\), both \(z\) and \(-z\) have zero remaining slack at radius \(r\). Consequently, any optimal center must satisfy \(\langle z,c\rangle=0\) for every such *active* normal.

Conversely, every nonactive inequality is strict at \(c=0\). There are finitely many of them, so all sufficiently small vectors orthogonal to the active normals satisfy every remaining inequality, while the active ones hold at equality. The affine hull of \(\mathcal I_{p,q}\) is therefore exactly the orthogonal complement in \(H\) of the active-normal span.

For a part of even size \(m\), its balanced sign vectors (zero sign sum) span exactly its coordinate contrast space of dimension \(m-1\): switching one plus and one minus yields all coordinate differences. For odd \(m\), its near-balanced sign vectors (sign sums \(\pm1\)) span the full coordinate space on that part: differences again give every contrast, while a nonzero common-sum direction is present. Their projections into \(H\) consequently span the within-part contrast space together with the one-dimensional between-part contrast line, for total dimension \(m\).

If the parts have unequal sizes, only the larger part is active. Thus the active-normal rank is \(h-1\) for even \(h\), and \(h\) for odd \(h\), leaving respective center dimensions \((N-1)-(h-1)=\ell\) and \((N-1)-h=\ell-1\). Its orthogonal complement consists precisely of the displayed forms \((a\mathbf1_h,b)\) and \((0,b)\). If the parts have equal size \(m\), both are active. For even \(m\), their contrast subspaces together have dimension \(2m-2\), leaving exactly one between-part direction; for odd \(m\), the active normals span all \(H\), so the only feasible center is zero. This proves the complete dimension and uniqueness table.

**4. Exact endpoints in the balanced even case.** When \(p=q=m\) is even, any optimal center is \((a\mathbf1_m,-a\mathbf1_m)\). A sign pattern with sum \(s\) on either part gives
\[
|as|\le1-\sqrt{1-\frac{s^2}{2m^2}}.
\]
The inequality is automatic for \(s=0\). For any nonzero allowable even \(|s|\), it is equivalent to
\[
|a|\le f_m(|s|),\quad
f_m(u)=\frac{1-\sqrt{1-u^2/(2m^2)}}u
=\frac{u}{2m^2(1+\sqrt{1-u^2/(2m^2)})}.
\]
For \(0<u\le m\), the latter expression is strictly increasing, because its numerator increases and its positive denominator decreases. The smallest nonzero allowable \(|s|\) is two, proving the exact closed interval \(|a|\le f_m(2)=(1-\sqrt{1-2/m^2})/2\) with no omitted endpoint constraints. The radius and all center classifications follow. \(\square\)

## Verification
The companion `verify.py` uses exact rational arithmetic and exact SymPy ranks. It reconstructs both facet-normal families, checks irredundant supporting facets in dimensions where independent incidence ranks are computed, verifies the maximal norm and all equality counts, and checks the codimensions of the active-normal spans for \(2\le p,q\le6\). It also makes exact symbolic comparisons of the even-balanced endpoint function for six even sizes. The run reported **1,462 successful finite assertions**; this is corroboration only. The proof above establishes the theorem for all integers \(p,q\ge2\) and the continuum of ball centers.

## Relationship to prior work
Higashitani, Jochemko and Michałek's *Arithmetic aspects of symmetric edge polytopes* (arXiv:1807.07678, Proposition 3.4) already gives the complete-bipartite facet combinatorics and signed-potential facet description, and it is the crucial starting point rather than a new result here. Codenotti, Riccardi and Venturello's 2025 preprint *The number of edges of a symmetric edge polytope* (arXiv:2512.16572v1) concerns sharp combinatorial edge bounds, not the metric center classification. Chen, Davis and Korchevskaia (arXiv:2107.12315) analyze facial subgraphs, not the full Euclidean incenter locus.

Related mathematical results determine the Euclidean inballs of **bipartite-cycle root polytopes** and the maximum-volume ellipsoids of **complete-bipartite graphical zonotopes**. The former has a different graph and affine realization; the latter a Minkowski sum of segments rather than the convex hull of edge roots. Facet counts of ordinary graph-metric Lipschitz-free balls also recover the already known count for \(P_{p,q}\), not the parity-dependent optimal-center geometry here. Consequently the contribution assessed as new is the complete **inball contact and center-set classification** (including its rank transitions and exact even-balanced interval), not the facet formula or the general existence of a centered maximal ball.

## Limitations
The metric formulas require the canonical unit-root embedding and the Euclidean structure inherited from \(\mathbb R^{p+q}\). They do not hold without change for weighted edges or arbitrary affine deformations. The exact inequality description of unequal-size center sets is finite but not a closed vertex enumeration of those center polytopes. Existing complete facet descriptions make the origin-centered radius accessible by an additional norm optimization; the potentially new structural part is the complete locus, its parity changes, sharp contact counts, and even-balanced endpoints. Priority remains provisional: an equivalent presentation of these incenter loci in broader Lipschitz-free or graph-root literature may exist. No independent audit has been performed.

## References
1. G. Codenotti, R. Riccardi and L. Venturello, *The number of edges of a symmetric edge polytope*, arXiv:2512.16572v1 (first public 2025-12-18), https://arxiv.org/abs/2512.16572 .
2. A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1 (first public 2018-07-20), https://arxiv.org/abs/1807.07678 .
3. T. Chen, R. Davis and E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315 (first public 2021-07-26), https://arxiv.org/abs/2107.12315 .
