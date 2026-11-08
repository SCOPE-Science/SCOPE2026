# Sharp sphere–torus obstructions for finite Farey-type graphs

## Finding

Fix an integer \(k\ge4\). A **Farey-type graph** is a finite simple undirected graph \(G\) satisfying the local axiom \(\varphi_0\): every vertex has degree at least three and every edge belongs to exactly two distinct triangles. A vertex of an induced subgraph \(H\) is **removable** if its degree in \(H\) is at most one, or if it has degree two and its two neighbors in \(H\) are adjacent. Let \(\psi_k\) mean that every nonempty induced subgraph of \(G\) with at most \(k\) vertices has a removable vertex.

**Theorem.** Every finite Farey-type graph satisfying \(\psi_k\) obeys
\[
\boxed{\delta(G)\ge k+1.}
\]
If \(G\) has \(v\) vertices and embeds in an orientable surface of genus \(g\), then
\[
\boxed{g\ge1+\frac{(k-5)v}{12}.}
\]
For \(k\ge6\), the inequality and \(v\ge k+2\) give the integer lower bound
\[
 g\ge1+\left\lceil\frac{(k-5)(k+2)}{12}\right\rceil.
\]
The first two topological thresholds are **sharp**:

* On the sphere, \(\varphi_0+\psi_4\) is realizable, but \(\varphi_0+\psi_5\) is not. Every planar realization of \(\varphi_0+\psi_4\) has at least \(12\) vertices, and the unique one on \(12\) vertices (up to isomorphism) is the icosahedral graph.
* On the torus, \(\varphi_0+\psi_5\) is realizable, but \(\varphi_0+\psi_6\) is not. For every integer \(m\ge6\), the \(m^2\)-vertex triangular torus graph described below realizes \(\varphi_0+\psi_5\).

The theorem concerns **induced** subgraphs throughout. No claim of optimal genus for \(k\ge6\), or of minimal vertex order for toroidal realizations, is made.

## Assumptions and scope

All graphs are finite, nonempty, simple, and undirected. A triangle is a three-vertex clique. The two triangles on each edge have distinct third vertices. Genus refers to orientable surface embedding, with the sphere having genus zero and the torus genus one. The axiom \(\psi_k\) is monotone in \(k\): its satisfaction implies satisfaction at every smaller positive integer. The primary context is the finite-local axiom scheme for the Farey graph; the argument does not identify finite approximants with finite models of its complete theory.

The icosahedral witness has vertices \(p,q,a_i,b_i\) for \(i\in\mathbb Z/5\mathbb Z\). Its edges are \(pa_i\), \(qb_i\), \(a_i a_{i+1}\), \(b_i b_{i+1}\), \(a_i b_i\), and \(a_{i+1}b_i\) for all \(i\). These make the two pentagonal rings, two poles, and the usual planar icosahedron.

For \(m\ge6\), the toroidal witness \(T_m\) has vertex set \((\mathbb Z/m\mathbb Z)^2\), with each vertex adjacent to its six translates by
\[
\pm(1,0),\qquad\pm(0,1),\qquad\pm(1,-1).
\]
The standard triangular tessellation of the plane descends under the translations by \(m\mathbb Z^2\) to a torus embedding of \(T_m\).

## Proof

**1. The triangle-link lemma.** Fix \(x\in G\) and write \(N(x)\) for its open neighborhood. For every \(y\in N(x)\), the neighbors of \(y\) *inside* \(N(x)\) are exactly the third vertices of the triangles through \(xy\). By \(\varphi_0\), there are exactly two. Thus \(G[N(x)]\) is a simple \(2\)-regular graph: a disjoint union of cycles of length at least three. Moreover, in the closed neighborhood \(G[N[x]]\), every vertex has degree at least three: the center has degree \(\deg(x)\ge3\), and a neighbor has the center plus its two link neighbors.

**2. The degree barrier.** Suppose that \(\deg(x)\le k-1\). The closed neighborhood has at most \(k\) vertices and no removable vertex, contradicting \(\psi_k\). Suppose instead that \(\deg(x)=k\). If a component of \(G[N(x)]\) is a triangle, that triangle together with \(x\) induces a \(K_4\); this four-vertex graph has no removable vertex and contradicts \(\psi_k\) because \(k\ge4\). Otherwise, every component of the link is a cycle of length at least four, and the whole \(k\)-vertex induced link has no removable vertex: each vertex has degree two with nonadjacent neighbors. Again \(\psi_k\) fails. Hence \(\deg(x)\ge k+1\) for every \(x\).

**3. Euler's inequality.** For a simple graph with \(v\ge3\) vertices embedded in an orientable surface of genus \(g\), the standard edge bound is \(|E(G)|\le3v-6+6g\). From the degree barrier, \(|E(G)|\ge(k+1)v/2\). Rearranging gives the displayed genus inequality. Also, simplicity gives \(v\ge k+2\), yielding its integer specialization for \(k\ge6\). On the sphere, \(k=5\) would require \(|E(G)|\ge3v>3v-6\). On the torus, \(k=6\) would require \(|E(G)|\ge7v/2>3v\). These are the two asserted impossibilities. With \(k=4\), a planar graph has \(5v/2\le3v-6\), hence \(v\ge12\).

**4. The icosahedral minimum.** In the explicit twelve-vertex graph, each vertex has degree five; each edge lies in exactly two triangles; every vertex link is a chordless five-cycle. The graph contains no \(K_4\) (its vertex links have no triangles). Nor does it contain an induced four-cycle: this is seen directly from the edge description, or from the property that any two nonadjacent vertices sharing neighbors have exactly two such neighbors and those neighbors are adjacent. A graph on at most four vertices with neither an induced \(K_4\) nor an induced four-cycle must have a removable vertex (equivalently, its chordal components have a simplicial vertex of degree at most two). Therefore \(\psi_4\) holds. Every vertex link is an induced five-cycle, so \(\psi_5\) fails.

For uniqueness at the planar lower order \(v=12\), equality in the planar edge bound and the degree sum forces the graph to be five-regular. By the triangle-link lemma every vertex link is a five-cycle. Choose a vertex \(p\) with link \(a_0\ldots a_4\). The edge \(a_i a_{i+1}\) has a unique second common neighbor \(b_i\) other than \(p\), and this vertex lies outside \(N[p]\). Distinct \(b_i\) cannot coincide: a coincidence gives a vertex adjacent to two nonconsecutive rim vertices and hence an induced four-cycle with \(p\). Each \(a_i\) now has the five neighbors \(p,a_{i-1},a_{i+1},b_{i-1},b_i\), exhausting its degree. The edge \(a_i b_i\) has common neighbor \(a_{i+1}\); its second common neighbor must be \(b_{i-1}\), since neither \(p\) nor \(a_{i-1}\) can be adjacent to \(b_i\) (the latter would make an induced four-cycle with \(p\)). Thus the five \(b_i\) form a cycle. Exactly one vertex \(q\) remains; all rim and center degrees are saturated, and \(q\) has degree five, so it meets every \(b_i\). This forces precisely the displayed icosahedral adjacency.

**5. The toroidal witness.** For \(m\ge6\), the six-neighbor rule for \(T_m\) yields a simple six-regular graph with exactly two common neighbors for every adjacent pair; hence it satisfies \(\varphi_0\). Its vertex links are induced six-cycles, so no \(K_4\) occurs.

We show that \(T_m\) has no induced cycle of length four or five. Any cycle of length at most five lifts to a closed cycle in the infinite triangular lattice: each step changes each integer coordinate by at most one, and an accumulated coordinate displacement divisible by \(m\ge6\) must be zero. A chord in that lift would project to a chord in the original cycle. But the triangular lattice has no induced cycle of length four or five. Indeed, such a cycle would bound a triangularly tiled disk with no internal boundary chords. If the disk has no interior vertices, triangulation requires a boundary chord. Otherwise each boundary vertex has at least one interior neighbor, while each interior vertex has degree six in the disk. Writing \(b\) for the boundary length, the triangulated-disk Euler degree identity gives
\[
\sum_{z\in\partial D}\deg_D(z)=4b-6.
\]
Every boundary degree is at least three, so \(3b\le4b-6\), forcing \(b\ge6\), a contradiction.

It follows that every induced subgraph of \(T_m\) on at most five vertices has neither \(K_4\) nor an induced cycle of length at least four. It is therefore chordal, and the standard simplicial-vertex theorem supplies a vertex whose neighbors form a clique. Because \(K_4\) is absent, this vertex has degree at most two and is removable. Thus \(T_m\models\psi_5\). Its six-cycle vertex links show that \(\psi_6\) fails, completing sharpness.

## Verification

The included standalone `checker.py` uses only Python's standard library. It builds the twelve-vertex and thirty-six-vertex witnesses from the explicit edge rules, verifies each degree and edge's exact triangle multiplicity, checks the forbidden induced configurations, and exhaustively tests all vertex subsets of size at most four in the icosahedral graph and at most five in the triangular torus graph. It also identifies a nonremovable five-cycle and six-cycle in their respective vertex links. Run `python checker.py` from the extracted artifact directory; the expected final status is `ALL_FAREY_BOUNDARY_CHECKS_OK`.

The universal lower bound is a symbolic proof for every \(k\ge4\); finite experiments only verify the two small explicit witnesses. The torus construction is proved for every \(m\ge6\), not merely the checked case \(m=6\).

## Relationship to prior work

Lockhart's 2026 pseudofiniteness paper proves that \(\varphi_0+\psi_6\) has no finite planar realization, using a closed-neighborhood obstruction. The present statement identifies the exact planar cutoff \(\psi_4/\psi_5\), provides an optimal twelve-vertex planar model, establishes the distinct toroidal cutoff \(\psi_5/\psi_6\), and exhibits toroidal models. The stronger link-cycle argument also sharpens the necessary minimum-degree condition and its genus consequences. The broader question of genus growth for finite approximants was studied previously; the quadratic lower-bound phenomenon alone is not claimed as new. Tent and Mohammadi provide the underlying axioms, while the icosahedral local structure and Euler inequalities are classical.

## Limitations

These are local finite-model obstructions, not a new proof of pseudofiniteness or a classification of all finite approximations. The genus inequalities for \(k\ge6\) are lower bounds, not optimality results. The construction does not determine the smallest toroidal model of \(\varphi_0+\psi_5\) or a minimum-genus model at higher axiom depth. Priority has been assessed against identified sources, without independent literature certification.

## References

1. Connor Martinez Lockhart, *Pseudofiniteness of the Farey Graph*, arXiv:2603.23900, first public version 25 March 2026; especially Proposition 4 and Theorem 12. https://arxiv.org/abs/2603.23900
2. Zahra Mohammadi Khangheshlaghi and Katrin Tent, *On the model theory of the Farey graph*, arXiv:2503.02121, first public version 3 March 2025; especially Theorem 1.1 and Definition 2.2. https://arxiv.org/abs/2503.02121
3. Zuosong Liang and Huandi Wei, *A Linear-Time Algorithm for 4-Coloring Some Classes of Planar Graphs*, 2021, doi:10.1155/2021/7667656, Observation 5 (icosahedral local uniqueness). https://pmc.ncbi.nlm.nih.gov/articles/PMC8510826/
4. Eric W. Weisstein, *Icosahedral Graph*, MathWorld (standard graph parameters and connectivity). https://mathworld.wolfram.com/IcosahedralGraph.html
