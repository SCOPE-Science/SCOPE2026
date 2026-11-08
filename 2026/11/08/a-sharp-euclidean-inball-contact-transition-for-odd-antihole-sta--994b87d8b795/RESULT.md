# A sharp Euclidean inball contact transition for odd-antihole stable-set polytopes

## Finding
For every integer \(a\ge 2\), put \(n=2a+1\), let \(G=\overline{C_n}\) be the complement of the simple odd cycle, and form its standard, full-dimensional stable-set polytope \(P_a\subset\mathbb R^n\). Its unique largest Euclidean inscribed ball has center \(r_a\mathbf 1\) and radius
\[
r_a=\min\!\left\{\frac{2}{2a+1+\sqrt{2a+1}},\;\frac{1}{a+\sqrt a}\right\}.
\]
There is a sharp facet-contact transition. For \(a=2,3\), exactly the \(n\) nonnegativity facets and the whole-graph rank facet touch the ball (\(n+1\) facets). For \(a=4\), both the rank facet and the \(n\) maximum-clique facets touch, in addition to all \(n\) nonnegativity facets (\(2n+1=19\) tangent facets at \(n=9\)). For all \(a\ge5\), exactly the \(n\) maximum-clique facets and the \(n\) nonnegativity facets touch (\(2n\) tangent facets). At the transition the radius is \(1/6\), and the polytope has 22 facets, of which 19 touch.

The stronger, complete *Euclidean facet supporting-hyperplane distance multiset* is as follows. The supporting hyperplanes of the \(n\) coordinate facets have distance \(r_a\) from the incenter, and the rank-facet supporting hyperplane has distance
\[
d_R=\frac{2-nr_a}{\sqrt n}.
\]
For every integer \(s\) with \(\lceil n/3\rceil\le s\le a\), there are exactly
\[
M_{n,s}=\frac ns\binom{s}{n-2s}
\]
maximal-clique facets whose supporting hyperplanes each have distance
\[
d_s=\frac{1-sr_a}{\sqrt s}.
\]
These are distances to the infinite supporting hyperplanes, not necessarily to the compact facet faces themselves; they count multiplicities, not necessarily distinct numerical distances. The number of facets is \(n+1+\sum_s M_{n,s}\), and the minimum of the displayed distances is precisely \(r_a\).

## Assumptions and scope
The cycle \(C_n\) has vertices indexed by \(\mathbb Z/n\mathbb Z\), with consecutive vertices adjacent; the complement graph has two vertices adjacent precisely when they are *not* adjacent in the cycle. A stable set of the complement consists of zero vertices, one vertex, or one consecutive cycle pair. Thus, with \(e_i\) the standard coordinate vectors,
\[
P_a=\operatorname{conv}\bigl(\{0\}\cup\{e_i:i\in\mathbb Z/n\mathbb Z\}\cup\{e_i+e_{i+1}:i\in\mathbb Z/n\mathbb Z\}\bigr).
\]
All radii and distances are ordinary Euclidean quantities in \(\mathbb R^n\), not intrinsic distances in a lower-dimensional embedding and not lattice-normalized values. The displayed \(n+1+\sum_sM_{n,s}\) facet count uses the irredundant facets of \(P_a\).

## Proof
**1. Complete facet description, established without an assumed polyhedral oracle.** The origin and all \(e_i\) lie in \(P_a\), so it is full-dimensional. Its polar is
\[
P_a^\circ=\{y:y_i\le1,\ y_i+y_{i+1}\le1\text{ for all }i\}.
\]
Write \(z_i=1-y_i\); the transformed polar is the fractional vertex-cover polyhedron of the odd cycle,
\[
Q=\{z:z_i\ge0,\ z_i+z_{i+1}\ge1\text{ for all }i\}.
\]
At a vertex of \(Q\) with some zero coordinate, the tight-edge subgraph cannot contain the complete odd cycle: the equations around that cycle would force all coordinates to equal \(1/2\). Thus its tight-edge graph is a disjoint union of paths. The corresponding edge--vertex incidence matrix, augmented with unit rows from active nonnegativity constraints, is totally unimodular, so the vertex has integer coordinates. Every integer vertex has entries in \(\{0,1\}\): an entry greater than one has both neighboring covering constraints slack and can be perturbed. Such integer vertices are exactly the indicator vectors of inclusion-minimal vertex covers of \(C_n\). Indeed, if a selected vertex could be deleted from its cover, its coordinate can be perturbed; conversely, every selected vertex of a minimal cover has a zero neighbor, and the tight constraints fix the cover uniquely. If a vertex of \(Q\) has no zero coordinate, all \(n\) edge inequalities must be tight for full rank, whence \(z_i=1/2\) for every \(i\), because \(n\) is odd. The recession cone of \(Q\) is the nonnegative orthant, with extreme rays \(e_i\).

Under polar duality, the complete facet list of \(P_a\) is therefore
\[
x_i\ge0,\qquad \sum_{i\in S}x_i\le1\quad(S\text{ maximal independent in }C_n),\qquad\sum_{i=1}^n x_i\le2.
\]
The middle inequalities are the maximal-clique inequalities of \(G\). The last rank inequality is a facet: its tight points \(e_i+e_{i+1}\) affinely span a hyperplane because the odd circulant matrix \(I+\mathrm{shift}\) is nonsingular. Each maximal-clique inequality is also a facet, as follows from the extreme-point description of the polar (or by using the corresponding singletons and neighboring consecutive pairs to construct \(n\) affinely independent tight points). Coordinate inequalities are facets using the origin and the remaining coordinate vectors. Hence none of these is a redundant inequality.

**2. Sharp radius and center.** If a ball of radius \(r\) centered at \(c\) is contained in \(P_a\), coordinate facets give \(c_i\ge r\). The rank facet gives \(\sum_i c_i+\sqrt n\,r\le2\), so \(r\le2/(n+\sqrt n)\). Any cycle-independent set of maximum size \(a\) gives \(\sum_{i\in S}c_i+\sqrt a\,r\le1\), whence \(r\le1/(a+\sqrt a)\). Conversely, set \(c=r_a\mathbf1\): all coordinate inequalities contain the ball, the rank inequality does by the first bound, and every maximal-clique inequality does because \(|S|\le a\) and \(s+\sqrt s\) is increasing. Thus the upper bound is attained.

If the rank bound is sharp, the sum of \(c_i\ge r_a\) equals the rank-facet upper bound, forcing each \(c_i=r_a\). If the clique bound is sharp, every maximum independent set \(S\) forces \(c_i=r_a\) for all \(i\in S\); these sets cover all cycle vertices. Thus the incenter is unique in every case.

**3. Contact transition.** The comparison of the reciprocal candidate radii reduces to the sign of
\[
F(a)=2\sqrt a-1-\sqrt{2a+1}.
\]
For real \(a\ge2\) its derivative is \(1/\sqrt a-1/\sqrt{2a+1}>0\), and \(F(4)=0\). Therefore the rank bound is strictly active for \(a=2,3\), both bounds tie at \(a=4\), and the maximum-clique bound is strictly active for all \(a\ge5\). Since \(s+\sqrt{s}\) strictly increases with \(s\), no smaller clique facet is tangent when the maximum-clique bound is active; the rank facet is tangent only when its own bound is active. Every coordinate facet is tangent. For odd \(n=2a+1\), exactly \(n\) independent sets of \(C_n\) have maximum cardinality \(a\), giving the stated counts.

**4. Every remaining facet distance and multiplicity.** A maximal independent set of \(C_n\) with \(s\) selected vertices has successive cyclic gaps of length two or three: gaps of one violate independence, while a gap of four or more allows adding a vertex. If \(j=n-2s\) gaps have length three, the other \(s-j\) have length two. Counting a distinguished selected vertex and a gap word, then dividing by the \(s\) possible choices of the distinguished selected vertex, gives \(M_{n,s}=\frac ns\binom{s}{n-2s}\). This is possible precisely for \(\lceil n/3\rceil\le s\le a\). Taking Euclidean distances from \(r_a\mathbf1\) to the displayed normalized facet hyperplanes yields \(d_R\), \(d_s\), and the coordinate distance \(r_a\), proving the full multiset formula.

## Verification
Run `python checker.py` with the versions or compatible versions listed in `requirements.txt`. The checker directly generates the true \(2n+1\) stable-set vertices and all claimed facets, checks that all facets have the required affine rank, solves independent Euclidean inball linear programs, compares random-direction support functions with LP over the facet description, and checks every facet-shell count for \(a=2,3,4,5,6,7\). The observed marker is `ODD_ANTIHOL_EUCLIDEAN_INBALL_FINITE_CHECKS_PASSED`. These finite tests are supportive; the general theorem follows from the proof above.

## Relationship to prior work
The classical stable-set-polytope facet theory of minimally imperfect graphs and near-perfect antiwebs provides the combinatorial background. Wagler's antiweb classification and subsequent papers on circular-interval stable-set facets and small-right-hand-side rank inequalities study valid and facet-inducing inequalities, rather than their ordinary Euclidean insphere or shell multiplicities. The present proof independently reconstructs its exact required facet description via the polar cycle-cover polyhedron, then establishes a metric classification and its transition. No assertion is made that the underlying odd-antihole facet inequalities are new.

## Limitations
The result is restricted to unweighted, standard-coordinate stable-set polytopes of complements of simple odd cycles of length at least five. It does not claim a corresponding formula for arbitrary webs, nonuniform coordinate weights, other Euclidean embeddings, or arbitrary near-perfect graphs. Historical priority for the metric theorem remains provisional pending broader expert examination; the cited combinatorial descriptions are established earlier work. No independent mathematical audit has been performed.

## References
1. S. Coniglio and S. Gualandi, “Optimizing over the Closure of Rank Inequalities with a Small Right-Hand Side for the Maximum Stable Set Problem via Bilevel Programming,” *INFORMS Journal on Computing* 34 (2022), 1006–1023. First public online date: 2021-11-29. DOI: 10.1287/ijoc.2021.1115.
2. G. Oriolo and G. Stauffer, “On the facets of stable set polytopes of circular interval graphs,” *Annals of Operations Research* 312 (2022), 1007–1029. Public date: 2022-03-03. DOI: 10.1007/s10479-021-04449-7.
3. A. Wagler, “Antiwebs are rank-perfect,” *4OR* 2 (2004), 149–152. DOI: 10.1007/s10288-003-0032-4.
4. G. R. Argiroffo and S. M. Bianchi, “On the set covering polyhedron of circulant matrices,” *Discrete Optimization* 6 (2009), 162–173. DOI: 10.1016/j.disopt.2008.11.001.
5. M. Moszyńska and E. Saorín Gómez, “On the kernel center of a convex body,” *Beiträge zur Algebra und Geometrie* 55 (2014), 595–602. DOI: 10.1007/s13366-013-0176-0.
