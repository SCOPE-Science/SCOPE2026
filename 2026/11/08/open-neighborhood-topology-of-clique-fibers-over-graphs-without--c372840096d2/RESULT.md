# Open-neighborhood topology of clique fibers over graphs without short cycles

## Finding
Let \(H\) be any finite connected simple graph without triangles or four-cycles, including the one-vertex graph, and let \(m\ge4\) be an integer. Write \(n=|V(H)|\), \(e=|E(H)|\), and \(G=H\mathbin\square K_m\). The ordinary **open Lovász neighborhood complex** \(\mathcal N(G)\) is homotopy equivalent, integrally, to
\[
\boxed{\mathcal N(H\mathbin\square K_m)\simeq H\vee\bigvee^{n}S^{m-2}\vee\bigvee^{e(m^2-3m+1)}S^2.}
\]
The graph \(H\) on the right denotes its geometric realization; the wedge is based and connected. In particular,
\[
\pi_1(\mathcal N(G))\cong F_{e-n+1},
\]
with \(F_0\) the trivial group, and the reduced integral homology is free, with a summand \(\mathbb Z^{e-n+1}\) in degree one, \(\mathbb Z^{e(m^2-3m+1)}\) in degree two, and \(\mathbb Z^n\) in degree \(m-2\); summands in coinciding degrees are added. In the first nonlinear width, \(m=4\), the two sphere types merge and the total number of two-spheres is \(n+5e\).

More strongly, the complex admits an explicit sequence of
\[
\boxed{m2^{m-2}\sum_{v\in V(H)}\left(2^{\deg_H(v)}-\deg_H(v)-1\right)+2me\left(2^{m-2}-m+1\right)}
\]
genuine elementary simplicial free-face collapses onto a core of row-boundary spheres, inter-row edges and triangles. The remaining homotopy equivalence is obtained by integral elementary CW cancellations, not by an unverified finite-homology inference.

## Assumptions and scope
The product graph has vertices \((v,a)\) for \(v\in V(H)\), \(a\in\{1,\ldots,m\}\). Two vertices are adjacent exactly when they have equal base coordinate and distinct colors, or adjacent base coordinates and equal colors. For a finite simple graph, the **open** neighborhood complex consists of all finite vertex sets admitting a *common adjacent vertex*, without including the center among its own neighbors. The result is **not** about closed neighborhoods, intrinsic scale-two graph Čech nerves, clique complexes, or independence complexes.

Let \(R_v=\{(v,a):1\le a\le m\}\) be the complete-graph fiber and \(B_v=\partial\Delta(R_v)\cong S^{m-2}\) its simplicial boundary. Because \(m\ge4\), each \(B_v\) is simply connected. If \(H\) has no edges, connectedness forces \(n=1\), and the formula reduces to the classical \(\mathcal N(K_m)=S^{m-2}\).

## Proof
**1. Exact generating facets and uniqueness.** Every vertex \((v,a)\) has open-neighborhood simplex
\[
F_{v,a}=(R_v\setminus\{(v,a)\})\cup O_{v,a},\qquad
O_{v,a}=\{(u,a):u\sim_H v\}.
\]
These \(mn\) simplices generate \(\mathcal N(G)\). If \(u\ne w\) are neighbors of \(v\), they are nonadjacent (no triangles) and have no other common neighbor (no four-cycles). Consequently, a face containing two or more vertices of \(O_{v,a}\) belongs to the single generating simplex \(F_{v,a}\). Likewise, a face containing one \((u,a)\in O_{v,a}\) and at least two vertices of \(R_v\setminus\{(v,a)\}\) belongs to this single generating simplex: every other generating facet meets \(R_v\) in at most one vertex unless it is centered in row \(R_v\), and another color centered there has no neighbor \((u,a)\). These uniqueness facts are the precise uses of the girth restriction.

**2. Explicit first-stage collapses.** For every pair \((v,a)\), choose a pivot \(h_{v,a}=(v,b)\) with \(b\ne a\). Write \(U_{v,a}=R_v\setminus\{(v,a),h_{v,a}\}\). For every subset \(T\subseteq O_{v,a}\) with \(|T|\ge2\) and every \(A\subseteq U_{v,a}\), pair the simplex \(T\cup A\) with \(T\cup A\cup\{h_{v,a}\}\). Process pairs in descending order of \(|T|+|A|\). Every lower face has only the displayed upper face as a remaining coface: all other larger faces within its unique generator were removed first. Different generators' pairs are disjoint. Thus these are actual elementary free-face collapses. There are \(2^{m-2}(2^{\deg_H(v)}-\deg_H(v)-1)\) pairs for each \((v,a)\). All faces with at least two off-row vertices disappear.

**3. Second-stage collapses and exact core.** Fix a directed base edge \(v\to u\) and color \(a\). For every subset \(A\subseteq U_{v,a}\) of size at least two, pair \(\{(u,a)\}\cup A\) with its extension by \(h_{v,a}\), again in descending order of lower-face dimension. The uniqueness in Step 1, now with the first-stage pairs removed, makes every such pair elementary and free. These pairs number \(2^{m-2}-m+1\) for each directed base edge and color.

The resulting simplicial core \(L\) consists **exactly** of the full row boundaries \(B_v\), all cross edges \(\{(u,a),(v,b)\}\) for \(uv\in E(H)\) and \(a\ne b\), and the surviving triangles
\[
\{(u,a),h_{v,a},(v,c)\},\qquad uv\in E(H),\quad c\notin\{a,b\},
\]
with one such family for each direction of the base edge; here \(h_{v,a}=(v,b)\). There are no other mixed faces of dimension two or higher. Counting the two stages gives precisely the stated collapse count.

**4. A uniform calculation for one interface.** Fix a base edge \(uv\). There are \(E=m(m-1)\) cross edges from row \(R_u\) to row \(R_v\), indexed by the edges of the connected crown graph \(K_{m,m}\) with its diagonal perfect matching removed. There are \(q=2m(m-2)\) surviving triangles over this interface. Every triangle contains two cross edges sharing one endpoint of the crown graph and a third edge lying in a row boundary \(B_u\) or \(B_v\). For each fixed endpoint of the crown graph, these triangles identify the incident cross edges along a star of \(m-2\) relations; the collective relation graph on the \(E\) cross edges is connected, because the crown graph is connected and \(m\ge4\).

As \(B_u\) and \(B_v\) are simply connected, the row-side arc of each triangle is homotopic relative its endpoints to the chosen row path; no row loop contributes an additional attaching class. Choose \(E-1\) triangles whose cross-edge relations form a spanning tree. In a CW model relative to the row spheres, each such triangle has unit coefficient on a cross-edge generator not already eliminated. Standard elementary \(1\)-\(2\) CW cancellation removes these \(E-1\) surplus cross one-cells and two-cells, leaving precisely one connecting one-cell between the two row spheres. Each of the remaining \(q-E+1\) triangles has nullhomotopic attaching loop already within this interface and splits off a two-sphere. Its count is
\[
q-E+1=2m(m-2)-m(m-1)+1=m^2-3m+1.
\]
These cancellations preserve the row spaces, and the chosen spanning tree of relations has determinant \(\pm1\) on the eliminated integral generators; no torsion arises from this step.

**5. Glue all interfaces.** Different interfaces have no mixed face in common: a mixed edge joins vertices of exactly one base edge, and every surviving triangle uses that same base edge. They meet only along the row boundaries \(B_v\). Thus the relative CW cancellations in Step 4 can be applied simultaneously, one for each of the \(e\) base edges. The residual one-cells form a graph with exactly one edge over every edge of \(H\), connecting the corresponding row spheres; its graph spine is homeomorphic to \(H\). The \(n\) simply connected row spheres and \(e(m^2-3m+1)\) null-attached two-spheres split off as the asserted wedge. This proves the statement for all finite connected triangle- and four-cycle-free bases, including trees with branching and bases with multiple independent cycles.

## Verification
The included standalone script `verify_clique_fiber_open_girth.py` uses only standard Python 3. It constructs graph adjacency independently of the proof, generates every neighborhood face, checks triangle and four-cycle exclusions, performs **every actual elementary free-face collapse** in both stages, compares all surviving faces against the asserted core, checks each crown-interface relation graph is connected with the predicted surplus dimension, and independently computes reduced mod-two Betti numbers of the *original complex*. It verifies 19 cases with \(4\le m\le6\), including a singleton, edge, path, four-leaf star, five- and six-cycles, two pentagons joined at one vertex, and the Petersen graph. Altogether it verifies 6,844 elementary free-face pairs; the recorded final line is `ALL_CHECKS_PASS 19 total_verified_elementary_collapses 6844`. This finite computation corroborates the complete symbolic proof but is **not** an infinite-parameter proof or an independent audit.

## Relationship to prior work
Matsushita [1] establishes fundamental-group methods for open neighborhood complexes, but the stated results do not give this high-girth clique-fiber homotopy classification or its two kinds of higher-dimensional sphere summands. Shukla [2] classifies neighborhood complexes of maximum-degree-at-most-three graphs and four-regular circulants; the present products have vertex degree at least \(m-1+\deg_H(v)\), and, for positive-degree bases with \(m\ge4\), are not covered by the graph classes in [2] in general.

The closely related published cycle-product calculation [3] gives exactly the \(H=C_n\) specialization for \(n\ge5\). **That specialization and the local crown-graph cancellation method are prior work, not claimed as new.** The present theorem supplies a uniform result for arbitrary connected graphs with no triangles or four-cycles, including branching trees, connected graphs with multiple independent cycles, and the Petersen graph, together with an exact collapse count depending on local degrees. For example, with \(H\) the Petersen graph and \(m=4\), the result is \(\bigvee^{6}S^1\vee\bigvee^{85}S^2\), which is not an instance of the cycle-product theorem.

The published high-girth clique-fiber Čech calculation [4] treats **closed** neighborhoods, not open neighborhoods. It gives \(H\vee\bigvee^{e(m-1)^2}S^2\), which is different: for a path on four vertices with \(m=5\), the open result is \(\bigvee^{33}S^2\vee\bigvee^4 S^3\), whereas the closed-Čech result has \(48\) two-spheres and no three-spheres. The graph-join suspension theorem [5] concerns a graph **join** rather than the Cartesian graph product. These comparisons rule out the direct implications checked, but unindexed equivalent work remains possible.

## Limitations
The theorem requires the base graph to have no triangles or quadrilaterals and width \(m\ge4\); no claim is made outside those boundaries. The result is an ordinary, nonequivariant integral homotopy classification, not an equivariant homotopy equivalence or a classification of simple-homotopy types after the relative CW cancellations. Finite checks cover only specified graphs and do not independently validate the all-parameter topology argument. The prior-work comparison is bounded rather than a proof of publication priority.

## References
[1] T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803, first public 2012-10-10, Journal of Mathematical Sciences, University of Tokyo 24 (2017), 321–353. https://arxiv.org/abs/1210.2803

[2] S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, first public 2018-02-13, Electronic Journal of Combinatorics 26 (2019), P2.4. https://arxiv.org/abs/1802.04526

[3] *Mixed-dimensional neighborhood homotopy of complete-graph cycle products*, accessible published research record and complete proof, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-mixed-dimensional-neighborhood-homotopy-of-complete-graph-cycle--3a53c8927b3c

[4] *Clique-fiber Čech nerves over graphs of girth at least five*, accessible published research record and complete proof, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-clique-fiber-ech-nerves-over-graphs-of-girth-at-least-five--bcf5b8b96c75

[5] *Clique joins suspend Lovász neighborhood complexes*, accessible published research record and complete proof, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-clique-joins-suspend-lov-sz-neighborhood-complexes--46728c3e0714
