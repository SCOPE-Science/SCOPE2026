# General-position rigidity and the first mixed coefficient in affine-plane incidence graphs

## Finding
Let \(G\) be the point–line incidence graph of any finite affine plane \(\mathcal A\) of order \(q\ge2\). A set \(S\subseteq V(G)\) is in *general position* when no three distinct vertices of \(S\) lie on a common shortest path. A *mixed* set meets both point and line parts. Write \(\Psi_G(z)=\sum_{S\text{ in general position}}z^{|S|}\).

**Theorem.** Every general-position set with at least three vertices is independent, and its selected line vertices either belong to one parallel class or include at most one line from each parallel class. Conversely, every such independent set is in general position. For \(q\ge3\), the largest general-position set is uniquely the full set of \(q^2\) point vertices. The largest mixed general-position sets have size \(q^2-q+1\), and exactly \(q(q+1)\) attain this bound. Each consists of one line together with all points outside it. Thus

\[
[z^k]\Psi_G(z)=\binom{q^2}{k}\quad(q^2-q+2\le k\le q^2),
\]

and

\[
[z^{q^2-q+1}]\Psi_G(z)=\binom{q^2}{q-1}+q(q+1).
\]

At \(q=2\), the general-position number is four, with exactly five maximizers: the four-point shore and four sets of three pairwise nonparallel, nonconcurrent lines together with the unique point outside their union.

## Assumptions and scope
A finite affine plane of order \(q\) has \(q^2\) points and \(q(q+1)\) lines; each line contains \(q\) points, every two points determine a line, and its lines partition into \(q+1\) classes of \(q\) pairwise disjoint lines. Distinct nonparallel lines meet exactly once. No Desarguesian or field-coordinate assumption is made for the theorem. For a selected set write \(P\) and \(B\) for its point and line vertices, and \(U(B)\) for points lying on at least one selected line. Distances in the incidence graph are graph distances.

## Proof
**1. Geodesic characterization.** In any connected bipartite graph, a general-position set of cardinality at least three is independent. Indeed, if an edge has both ends selected and a third vertex is selected, their distances from that third vertex have opposite parity and differ by at most one; one end of the edge lies on a shortest path between the other end and the third vertex. In an affine Levi graph, two distinct points have distance two. Two intersecting lines have distance two, while two parallel lines have distance four. An incident point and line have distance one; a nonincident point and line have distance three. Therefore, for an independent set \(S\), no selected point can be an internal vertex of a geodesic between any two selected vertices: for two selected lines the only possible point interior vertices are on an endpoint line, and for other endpoint pairs the distance constraints give the same conclusion. A selected line can be internal to a geodesic between two selected parallel lines precisely when it meets both; such a line is a transversal to their parallel class. No selected line can otherwise be an interior vertex. Hence a selected independent set is in general position if and only if it contains no two parallel selected lines together with a transversal selected line. This is exactly the stated line-family dichotomy: if a pair is parallel, all selected lines belong to its class; otherwise every class contributes at most one.

**2. Mixed upper bounds.** Let \(b=|B|\ge1\) and note that \(P\cap U(B)=\varnothing\). If all selected lines are parallel, their point sets are disjoint, whence
\[
|S|\le q^2-bq+b=q^2-b(q-1)\le q^2-q+1,
\]
with equality only for \(b=1\). If there is at most one line from each parallel class then \(1\le b\le q+1\). Any two selected lines meet in at most one point, so
\[
|U(B)|\ge bq-\binom b2,\qquad |S|\le q^2-b(q-1)+\binom b2.
\]
For \(q\ge4\), the concave function \(f(b)=b(q-1)-\binom b2\), on integer \(1\le b\le q+1\), has \(f(1)=q-1\), \(f(q+1)=(q+1)(q-2)/2>q-1\), and \(f(b)>q-1\) for every \(b\ge2\). Thus only \(b=1\) attains the mixed bound. For \(q=3\) the only additional potential equality is \(b=4\), demanding that all six pairwise intersections of four differently directed lines be distinct. Adjoin the projective line at infinity. Those four lines plus the infinity line would be five lines with no triple intersection in the projective plane of odd order three. This is impossible: in any projective plane of odd order \(q\), a hypothetical family of \(q+2\) lines with no three concurrent covers fewer than all points (its union has \((q+2)(q+1)/2\) points). Choose an uncovered point \(X\). Every line of the pencil through \(X\) meeting one family line meets exactly one other at the same point, because every point on a family line is its intersection with another family line. Hence the \(q+2\) family lines pair up, forcing \(q+2\) even, a contradiction. This excludes \(b=4\) at order three. All mixed maximizers for \(q\ge3\) thus consist of one chosen line and all off-line points; there are \(q(q+1)\) such choices.

**3. Polynomial and exceptional case.** A general-position set consisting entirely of point vertices is arbitrary, so contributes \((1+z)^{q^2}\). The largest all-line general-position sets have size at most \(q+1\), and the mixed bound is strictly below \(q^2\) for \(q\ge3\). For \(q=3\), the line-only bound is four, below the displayed coefficient degree seven; for larger orders it is also below that degree. The two coefficient formulas and unique maximum now follow. For \(q=2\), the line-only maximum is three. Mixed sets of size four must consist of three differently directed lines and one point outside their union. Exactly four of the eight choices of one line from each direction yield a three-point union; each has one point outside. The four-point shore is the fifth maximum set.

## Verification
A standalone C++17 program (`verify_affine_gp.cpp`) constructs the incidence graphs over the fields of orders two and three, computes all-pairs shortest paths by breadth-first search, and enumerates every vertex subset, classifying a subset by whether it has any selected vertex on a geodesic between two other selected vertices. It checks all \(2^{10}\) subsets at order two and all \(2^{21}\) subsets at order three. The results are: for order two, exactly five maximum general-position sets of size four, including four mixed sets; for order three, exactly one overall maximum of size nine, and exactly twelve mixed maxima of size seven, with degree-seven polynomial coefficient 48. An independent Python program (`verify_direction_tuples.py`) enumerates all one-per-direction line families: their union-size histograms are \(\{3:4,4:4\}\) for order two and \(\{7:72,9:9\}\) for order three. These finite checks independently corroborate the exceptional cases; the all-order results follow from the geometric proof, not extrapolation.

Run `g++ -O3 -std=c++17 verify_affine_gp.cpp -o verify_affine_gp && ./verify_affine_gp` and `python3 verify_direction_tuples.py`. The C++ checker enumerates all subsets only at field orders two and three.

## Relationship to prior work
Hoffman and Ray-Chaudhuri (1965) defined precisely this affine point–line incidence graph \(G(\Pi)\), studying spectral characterization of its *line graph*, rather than graph general-position sets. Hauschild, Ortiz and Vega (2014) studied well-covered dimension of Levi graphs of point–line configurations, a different graph invariant. Anand and collaborators (arXiv:1812.08460) established general bipartite general-position facts, including a diameter-at-most-three setting; the affine Levi graph has diameter four and the present line-parallelism classification is not implied by that diameter theorem. Iršič and collaborators (arXiv:2401.05696) developed general-position polynomials in other graph classes. The contribution here is the mixed-line structural characterization, the gap below the unique maximum, and the first mixed coefficient for every finite affine plane.

## Limitations
This does not provide the entire polynomial \(\Psi_G(z)\) below degree \(q^2-q+1\). Priority is assessed only against literature and records located and inspected; a differently named or unindexed earlier classification cannot be ruled out. The finite verifier treats only the two small Desarguesian planes and does not independently enumerate non-Desarguesian planes; the general claim relies on the incidence-axiom proof. No independent scholarly audit has been performed.

## References
1. A. J. Hoffman and D. K. Ray-Chaudhuri, *On the line graph of a finite affine plane*, Canadian Journal of Mathematics **17** (1965), 687–694. https://doi.org/10.4153/CJM-1965-069-6
2. J. Hauschild, J. Ortiz, O. Vega, *On the Levi Graph of Point-Line Configurations*, arXiv:1408.2879 (first posted 2014-08-12). https://arxiv.org/abs/1408.2879
3. B. Anand et al., *The general position problem in graphs*, arXiv:1812.08460 (2018). https://arxiv.org/abs/1812.08460
4. V. Iršič et al., *General position polynomials*, arXiv:2401.05696 (2024). https://arxiv.org/abs/2401.05696
