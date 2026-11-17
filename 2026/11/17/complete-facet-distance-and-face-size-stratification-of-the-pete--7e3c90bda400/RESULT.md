# Complete facet-distance and face-size stratification of the Petersen symmetric edge polytope

## Finding
Let \(G=KG(5,2)\) be the Petersen graph with vertex set the ten two-element subsets of \([5]\), where disjoint subsets are adjacent. In the nine-dimensional Euclidean zero-sum hyperplane \(H\), put
\[
P=\operatorname{conv}\{\pm(e_U-e_V):UV\in E(G)\}.
\]
Every one of the \(1410\) facets of \(P\) belongs to exactly one of **eleven distinct Euclidean supporting-hyperplane distance shells**, and the facets split into exactly **eighteen orbits** under the natural \(S_5\) action together with central inversion. More precisely, let \(d\) denote the distance from the origin to a facet-supporting hyperplane, and let \(t\) denote the number of vertices in that facet. The complete joint enumeration is:

| \(K=10/d^2\) | \(t=9\) | \(t=10\) | \(t=11\) | \(t=12\) | Total |
|---:|---:|---:|---:|---:|---:|
| 56 | 0 | 0 | 0 | 30 | 30 |
| 49 | 0 | 0 | 180 | 0 | 180 |
| 45 | 20 | 0 | 0 | 0 | 20 |
| 44 | 0 | 120 | 0 | 0 | 120 |
| 41 | 120 | 0 | 180 | 0 | 300 |
| 40 | 0 | 120 | 0 | 30 | 150 |
| 36 | 0 | 240 | 0 | 40 | 280 |
| 29 | 60 | 0 | 0 | 0 | 60 |
| 25 | 60 | 0 | 60 | 0 | 120 |
| 24 | 0 | 120 | 0 | 10 | 130 |
| 21 | 20 | 0 | 0 | 0 | 20 |
| **Total** | **280** | **600** | **420** | **110** | **1410** |

Thus exactly \(280\) facets are simplices. The previously known origin-centered inball has \(30\) tangent facets, all with twelve vertices; **the nearest other facets** are precisely \(180\) eleven-vertex facets in two symmetry orbits of sizes \(60\) and \(120\). The sharp Euclidean clearance is
\[
\boxed{d_{\mathrm{next}}-d_{\mathrm{tangent}}=\frac{\sqrt{10}}7-\sqrt{\frac5{28}}>0.}
\]
The complete orbit representatives, including their metric and combinatorial types, appear under Verification.

## Assumptions and scope
The graph is the unweighted, simple Petersen graph \(KG(5,2)\); the polytope is the **symmetric edge polytope**, not a cut polytope or an eigenpolytope. Euclidean inner products are inherited from \(\mathbb R^{10}\) on its zero-sum hyperplane, rather than from an arbitrary affine projection. Each facet is counted once; its supporting hyperplane is normalized to support value one, and \(d>0\) is the Euclidean distance to the origin. The natural symmetry group considered here is \(S_5\times C_2\), where \(S_5\) permutes the five underlying symbols and \(C_2\) sends every facet to its antipode. No assertion about additional exotic affine symmetries is needed.

## Proof
**Polar correspondence.** The polar is the compact Lipschitz polytope
\[
Q=P^\circ=\bigl\{h\in H:|h_U-h_V|\le 1\text{ for every edge }UV\in E(G)\bigr\}.
\]
Its vertices \(h\) correspond bijectively to facets \(h\cdot x=1\) of \(P\). Such a hyperplane has distance \(d=1/\lVert h\rVert_2\). For any feasible \(h\), call an edge **tight** if \(|h_U-h_V|=1\). The tight edges span a connected graph if and only if \(h\) is a vertex of \(Q\): connectedness makes the tight incidence equations rank nine on \(H\), whereas disconnectedness allows an arbitrarily small, mean-zero, componentwise constant perturbation without violating any strict inequalities. The latter uses the finite positive slack on all nontight edges.

**Finite reduction.** On a spanning tree of tight edges the coordinate differences of a vertex are signed units; hence all differences are integral. The Petersen graph has diameter two, so every one-Lipschitz labeling has total range at most two. Adding a common constant yields a unique representative \(p\in\{0,1,2\}^{10}\) with minimum zero. Conversely any such labeling satisfying all edge inequalities and having connected tight-edge graph determines a polar vertex after subtracting its mean. Thus **all** facets, with no unexamined fractional or large-range exceptions, are obtained from a finite list of \(3^{10}=59049\) candidate words.

For a candidate word, let \(a,b\) count its zero and two labels. Its centered Euclidean squared norm is
\[
\sum_U(p_U-\overline p)^2=a+b-\frac{(a-b)^2}{10}.
\]
Equivalently, the exact integer \(K=10\sum_U p_U^2-(\sum_U p_U)^2\) satisfies \(d=\sqrt{10/K}\). The facet vertices are precisely the root vectors \(\operatorname{sgn}(p_U-p_V)(e_U-e_V)\) belonging to tight graph edges. Each root vector is a vertex of \(P\) (its own root functional exposes it), so the number \(t\) of facet vertices equals the number of tight edges. It follows that the table in Finding gives a complete simultaneous classification of facet distances and facet vertex counts.

**Exhaustive finite certificate.** The standalone script `artifacts/verify.py` implements the following bounded procedure using integer comparisons only. Enumerate all ten-coordinate ternary words; keep a word only if its minimum is zero, all fifteen disjoint-pair graph edges have label difference at most one, and the subgraph of unit-difference edges is connected. Increment the table entry indexed by \((K,t)\). The script also implements a second, separately parameterized exhaustive enumeration: fix a spanning-tree root at zero, assign each of the remaining nine tree edges one of \(-1,0,1\), integrate these increments along the tree, and test the same feasibility and connectedness conditions. This checks all \(3^9=19683\) rooted tree assignments. It verifies exact equality of the two sets of normalized vertices as well as all entries in the displayed joint table. Unlike sampling or a search timeout, these loops cover the entire rigorously bounded finite space. The small, standalone source code is part of the proof certificate and is sufficient to rederive every integer in the table.

**Orbit decomposition.** A permutation of \([5]\) acts on the ten unordered two-subsets and preserves disjointness. Central negation sends a representative \(p\) to \(\max(p)-p\), followed by renormalization. These \(240\) transformations preserve the facet conditions, \(K\), and \(t\). Enumerating all transformations of the explicit representatives in the following table produces pairwise disjoint orbits whose sizes sum to \(1410\). The exhaustive code checks orbit membership against the **entire** facet list, proving there are no additional orbits. Every representative is specified by its zero-labeled pair set \(A\) and two-labeled pair set \(B\); all other pairs receive label one. For example, `12` denotes \(\{1,2\}\).

| \(K\) | Orbit size | \(t\) | \(A\): zero-labeled pairs | \(B\): two-labeled pairs |
|---:|---:|---:|---|---|
|56|30|12|12,13,25,35|15,23|
|49|120|11|12,13,25|15,23|
|49|60|11|12,13,45|14,15|
|45|20|9|12,13,14,25,35,45|15|
|44|120|10|12,13,14,25,35|15|
|41|120|11|12,13,14,25|15|
|41|120|9|12,13,24,35|23|
|41|60|11|12,13,24,34|23|
|40|120|10|12,13|15,23|
|40|30|12|12,13|14,15|
|36|240|10|12,13,24|23|
|36|40|12|12,13,14|15|
|29|60|9|12,13|23|
|25|60|11|12,13,14,15,23|none|
|25|60|9|12,13,14,23,25|none|
|24|120|10|12,13,14,15,23,24|none|
|24|10|12|12,13,14,15|none|
|21|20|9|12,13,14,15,23,24,25|none|

The largest value \(K=56\) and its thirty contacts were already established in earlier work. The new part is the **complete** joint stratification and its eighteen symmetry classes, in particular the exact first noncontact gap and the two types achieving it.

## Verification
From a directory containing `artifacts/verify.py`, execute `python3 artifacts/verify.py`. The script uses only the Python standard library and prints:

`PETERSEN_FACET_SPECTRUM_CHECKS_PASSED words=59049 tree_words=19683 facets=1410 shells=11 symmetry_orbits=18`

It additionally prints the complete shell totals and orbit-size profiles, and asserts equality with the theorem. Both enumerations use integer arithmetic. They do not rely on external polyhedral software, approximation, or a stored table of previously enumerated facets. The theorem is a **finite exact classification**; no inference about an unbounded graph family is made.

## Relationship to prior work
D’Alì, Delucchi and Michałek [1] give the symmetric edge / Lipschitz-polar framework and study facets of other graph families. Chen, Davis and Korchevskaia [2] study facet subgraphs and maximal bipartite subgraphs. Braun and Bruegge [3, Theorem 2.3] recall the integral one-Lipschitz tight-edge characterization of facets. These results yield a general decision criterion but do not state the Petersen-specific joint metric/face-size table or the eighteen orbit types. An earlier study of the Petersen symmetric edge polytope [4] computes its inradius, its thirty tangent facets, and the total of \(1410\) facets. Neither its stated theorem nor its standalone enumerator gives the eleven-shell histogram, the facet-size refinement, or the eighteen \(S_5\times C_2\) orbit classification. The existing inradius is explicitly treated as known, not reclaimed here. A study of **cut polytopes** on Petersen graphs [5] concerns a different polytope and does not imply this classification.

## Limitations
The classification is specific to the **canonical Euclidean embedding** of the Petersen symmetric edge polytope and does not extend without new argument to general Kneser graphs or graph-metric polytopes. The proofs of the 11-by-4 table and eighteen-orbit list use small exhaustive finite enumeration, with the completeness reduction given above; no symbolic unbounded-family theorem is claimed. Priority should be checked against specialist unpublished tables and alternative formulations involving facet subgraphs, Lipschitz functions, or graph spread.

## References
1. A. D’Alì, E. Delucchi, M. Michałek, “Many faces of symmetric edge polytopes,” arXiv:1910.05193, publicly posted 2019-10-11. https://arxiv.org/html/1910.05193v1
2. T. Chen, R. Davis, E. Korchevskaia, “Facets and facet subgraphs of symmetric edge polytopes,” arXiv:2107.12315, publicly posted 2021-07-26. https://arxiv.org/abs/2107.12315
3. B. Braun, K. Bruegge, “Facets of Symmetric Edge Polytopes for Graphs with Few Edges,” arXiv:2201.13303, publicly posted 2022-01-31. https://arxiv.org/abs/2201.13303
4. “Exact inradius and contact-facet rigidity of the Petersen symmetric edge polytope,” publicly available research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-inradius-and-contact-facet-rigidity-of-the-petersen-symmet--af8a32ec1f59
5. M. Deza, M. Dutour Sikirić, “Enumeration of the facets of cut polytopes over some highly symmetric graphs,” arXiv:1501.05407 (2015). https://arxiv.org/abs/1501.05407
