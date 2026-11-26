# Edge-hitting criterion and vertex-cover complexity of Milnor attractors on finite graphs

## Finding

Let \(X\) be a nondegenerate connected finite metric graph with positive edge lengths, and equip it with a nonatomic Borel probability measure \(\mu\) that gives every nonempty open subset positive mass. Write \(V_*\) for the points of topological valence different from two. When \(V_*\ne\varnothing\), the *essential closed edges* \(\mathcal E\) are the closures of the connected components of \(X\setminus V_*\). These are finitely many compact arcs (possibly loops with endpoints identified).

**Classification.** A nonempty closed set \(A\subseteq X\) is the Milnor global attractor of some homeomorphism \(h:X\to X\) precisely when

\[
A\cap E\ne\varnothing\qquad\text{for each }E\in\mathcal E.
\]

The realizing homeomorphism can fix \(A\cup V_*\) pointwise, and almost every forward orbit converges to a point of \(A\). If \(V_*=\varnothing\), then \(X\) is a circle and any nonempty closed subset is realizable.

For any connected finite simple graph \(G\) with no vertices of degree two, let \(\tau(G)\) be its minimum vertex-cover cardinality. Then

\[
\min_{h\in\operatorname{Homeo}(|G|)}\bigl|\Lambda_\mu(h)\bigr|=\tau(G),
\]

where the minimum is over homeomorphisms with *finite* Milnor global attractor. In particular, deciding from \((G,k)\) whether such an attractor has at most \(k\) points is NP-complete even for connected cubic planar simple graphs.

## Assumptions and scope

A finite metric graph is a compact one-dimensional topological CW complex formed from finitely many positive-length edges, without isolated points. Its reference measure is nonatomic and full-support; it need not be invariant under \(h\) or equivalent to arclength. Points of valence two are suppressed in the essential-edge decomposition. A circle has no essential vertices and is treated separately. An essential edge may be a loop, whose two parameter endpoints represent the same essential vertex.

For a continuous map \(h\), let \(\omega_h(x)\) denote the accumulation set of the forward orbit. The *Milnor global attractor* \(\Lambda_\mu(h)\) is the smallest closed set \(C\) for which \(\mu(\{x:\omega_h(x)\subseteq C\})=1\). The minima and finite-cardinality decision in the statement refer to this measure-theoretic attractor, not a topologically attracting invariant set.

## Proof

**1. Edge necessity.** A graph homeomorphism preserves the finite essential-vertex set \(V_*\); it therefore permutes the finitely many open essential edges. For any open essential edge \(e\), choose \(q\ge1\) so that \(h^q(e)=e\). The compact closure \(E=\overline e\) is invariant under \(h^q\). For every \(x\in e\), a convergent subsequence of \(h^{qn}(x)\) accumulates inside \(E\), whence \(\omega_h(x)\cap E\ne\varnothing\). If \(A\cap E=\varnothing\), no point of \(e\) has its entire omega-limit set in \(A\). Since \(e\) is nonempty open and \(\mu(e)>0\), \(A\) cannot be a full-basin attractor. This works for bridges, cycles, loops, and edge permutations alike.

**2. A local interval homeomorphism.** Set \(\varepsilon=1/2\). On \([0,1]\), define

\[
\phi_-(u)=u-\varepsilon u(1-u),\qquad
\phi_+(u)=u+\varepsilon u(1-u).
\]

Each is a strictly increasing homeomorphism fixing zero and one; its derivative lies in \([1/2,3/2]\). Every interior orbit of \(\phi_-\) tends to zero and every interior orbit of \(\phi_+\) tends to one. Their displacements are at most \(\varepsilon\min\{u,1-u\}\). Affine rescalings of these formulas work on any compact interval.

**3. Construction on the essential edges.** Parametrize each essential edge by \([0,L]\), identifying endpoints if the edge is a loop. Let \(K\) be the union of the two parameter endpoints with the inverse image of \(A\cap E\). This \(K\) is compact. On \(K\) use the identity. Each complementary interval \((a,b)\) of \([0,L]\setminus K\) has at least one endpoint in the inverse image of \(A\): if both endpoints were excluded, they would have to be the two parameter endpoints, forcing \(A\cap E=\varnothing\), contrary to the hypothesis.

If only \(a\) belongs to \(A\), use the affinely rescaled \(\phi_-\) on \([a,b]\); if only \(b\) belongs to \(A\), use \(\phi_+\). If both belong to \(A\), bisect \([a,b]\), use \(\phi_-\) on the left half and \(\phi_+\) on the right half, fixing their common midpoint. Every point in each open half converges to its attracting endpoint in \(A\). All essential vertices are fixed, including those outside \(A\), and the endpoint identifications on loops agree.

In all pieces the displacement satisfies

\[
|h(t)-t|\le \tfrac12\,\operatorname{dist}(t,K),
\]

since the affine maps move toward a fixed boundary by at most half the distance to the nearest boundary. This uniform bound ensures continuity at accumulation points of \(K\). Each edgewise map is increasing and fixes both endpoints, hence is a continuous bijection of the edge onto itself; the finite edgewise gluing is a continuous bijection of the compact graph, therefore a homeomorphism. The same argument applies on the circle after cutting it at any chosen point of \(A\) and identifying the endpoints.

**4. Full basin and minimality.** On each essential edge, points not in \(A\) that fail to converge to \(A\) consist only of finitely many essential vertices and at most one fixed midpoint of each complementary gap with both endpoints in \(A\). There are countably many gaps. Because \(\mu\) is nonatomic, this exceptional set has zero measure. Consequently the basin of \(A\) has full measure, and almost every forward orbit converges to a singleton in \(A\).

To establish *minimality*, let \(C\subsetneq A\) be closed and choose \(a\in A\setminus C\), with an open neighborhood \(U\) of \(a\) such that \(\overline U\cap C=\varnothing\). If \(U\) contains a nonempty open set contained in \(A\), the fixed points of that open set have positive \(\mu\)-mass and their limits lie outside \(C\). Otherwise every smaller neighborhood of \(a\) meets \(X\setminus A\); a complementary interval has an endpoint \(r\in A\cap U\) (choose the interval sufficiently close to \(a\)). By construction a nonempty open one-sided portion of that interval converges to \(r\), so this positive-mass set also has omega-limit outside \(C\). In either case \(C\) does not have full basin. If any other closed set \(D\) has full basin, then so does its closed intersection \(D\cap A\), since the two basins have full measure; the preceding argument forces \(D\cap A=A\). Thus \(A\) is the smallest closed full-basin set. The circle case has the same local argument.

**5. Vertex-cover identity and complexity.** In a simple graph with no degree-two vertices, the essential closed edges coincide with the usual closed geometric edges. Every vertex cover is a finite closed subset meeting every edge, and hence is a realizable Milnor attractor. Conversely, if a finite set \(A\) meets all closed edges, replace each of its edge-interior points by an endpoint of that edge. Edge interiors are disjoint, so these replacements cannot uncover any other edge, and may only decrease the number of points. The result is a vertex cover with at most \(|A|\) vertices. Therefore the optimal finite-attractor cardinality equals \(\tau(G)\).

The finite-attractor decision problem is in NP: the corresponding vertex-cover certificate is checked by inspecting all edges. Its NP-hardness follows from the identity reduction on connected cubic planar graphs, for which VERTEX COVER is already NP-complete (Uehara 1996). All vertices of a cubic graph have degree three, so no vertex suppression or auxiliary gadget is needed.

## Verification

The supplied `CHECK.py` uses exact rational arithmetic to verify 903 local edge-coordinate monotonicity/boundary constraints across seven target sets and tests 6 graph classes for equality of vertex-cover and finite candidate edge-hitting minima. The checks include a tripod, a tetrahedron, \(K_{3,3}\), and a triangular prism. The infinitely many possible closed subsets, the universal necessity argument and the NP-completeness implication are mathematical proofs, not conclusions inferred from those finite tests.

## Relationship to prior work

Hantáková and Mlíchová (arXiv:2611.15353v1, 11 November 2026), Sections 3–4, give a general root-contracting construction and realize every nonempty closed subset of a compact interval or circle; their Section 6.2 proves a specific nonrealizable singleton on a tripod and states the broader branched-continuum classification problem. The *sufficiency technique* above is an explicit graphwise application of their root-contracting idea. The *complete edgewise necessity-and-sufficiency criterion*, vertex-cover optimum, and computational complexity consequence are the claims distinguished here and are not stated in the inspected portions of that work. The graph classification is not claimed for infinite dendrites or more general branched continua.

Robinson and Sánchez-Gabites (2016) consider classical global attractors of homeomorphisms of normed linear spaces, a different attractor notion and ambient category. Uehara (1996) supplies the external cubic-planar vertex-cover hardness theorem; no novelty is asserted for that theorem itself.

## Limitations

This is a theorem for finite connected graphs and nonatomic full-support measures. Atomic measures can invalidate the null-exception argument. It concerns existence of *some* homeomorphism, not all homeomorphisms or prescribed dynamics on \(A\). The circle requires the separate no-essential-vertex case. General branched continua and graph maps that are noninvertible fall outside the statement. Priority relative to all historical graph-dynamical literature has not been independently established.

## References

1. J. Hantáková and M. Mlíchová, *Universal Realization of Milnor Attractors in Low Dimensions*, arXiv:2611.15353v1 (11 November 2026), Sections 2–4 and 6.2. https://arxiv.org/abs/2611.15353
2. R. Uehara, *NP-complete problems on a 3-connected cubic planar graph and their applications*, Technical Report 4 (1996), abstract and introduction. https://www.jaist.ac.jp/~uehara/pdf/triangle.pdf
3. J. C. Robinson and J. J. Sánchez-Gabites, *On finite-dimensional global attractors of homeomorphisms*, Bull. Lond. Math. Soc. 48 (2016), 483–498. https://doi.org/10.1112/blms/bdw011
