# Integral circle persistence under clustered star-edge faults in biclique dissociation complexes

## Finding

Fix integers \(a,b\ge3\). Let \(A=\{u\}\sqcup A'\), with \(|A'|=a-1\), and \(B=\{v_1,\ldots,v_b\}\). For each \(0\le t\le b\), let
\[
G_t=K_{a,b}\setminus\{uv_1,\ldots,uv_t\},\qquad X_t=\operatorname{Ind}_2(G_t),
\]
where a face of \(\operatorname{Ind}_2(G)\) is a vertex set whose induced graph has no connected component on three or more vertices (equivalently, induced maximum degree at most one).

Then the complete integral homotopy classification is
\[
|X_0|\simeq\bigvee^{ab-1}S^1,\qquad
|X_t|\simeq\bigvee^{(a-1)(b-t)}S^1\quad(1\le t\le b).
\]
A wedge of zero circles means a point. In particular, \(X_b\) is contractible and all integral homology is torsion-free. Every inclusion \(X_{t-1}\hookrightarrow X_t\) induces a **split surjection** on integral first homology with kernel
\[
\ker\big(H_1(X_{t-1};\mathbb Z)\to H_1(X_t;\mathbb Z)\big)\cong
\begin{cases}
\mathbb Z^{a+b-2},&t=1,\\
\mathbb Z^{a-1},&2\le t\le b.
\end{cases}
\]
No positive-degree persistent homology classes are born along this deletion filtration. For \(1\le t\le b\), under the natural vertex-label-permutation subgroup \(S_{a-1}\times S_t\times S_{b-t}\), the full integral first-homology lattice is the permutation module \(\mathbb Z[A'\times\{v_{t+1},\ldots,v_b\}]\), with the middle symmetric group acting trivially. Its canonical basis consists of the oriented three-edge cycles
\[
c_{x,y}=[u,x]+[x,y]+[y,u]\quad(x\in A',\ y\in\{v_{t+1},\ldots,v_b\}).
\]
For \(t\ge2\), the inclusion homomorphism on these bases deletes exactly the \(a-1\) basis elements with \(y=v_t\) and fixes all other basis elements.

## Assumptions and scope

All graphs are finite, simple, labeled, and have the indicated two nonempty vertex shores. The connected-component condition and the maximum-degree-at-most-one condition coincide because a graph of maximum degree one is a disjoint union of isolated vertices and isolated edges. The geometric realizations include all simplices, not merely the one-skeleton. Both \(a,b\ge3\) and all \(t\) in the stated closed interval are quantified; no assertion concerns arbitrary non-star fault patterns.

## Proof

**Zero faults.** For \(t=0\), the only dissociation faces meeting both shores are one vertex from each shore. Thus \(X_0\) is the union of two disjoint simplices \(\Delta_A\), \(\Delta_B\) and all \(ab\) edges joining them, with no mixed triangles. Collapse the two contractible simplices separately to points: the resulting connected graph has two vertices and \(ab\) parallel one-cells, so \(|X_0|\simeq\bigvee^{ab-1}S^1\). This is an actual homotopy equivalence, not an Euler-characteristic inference.

**Classification of all faces for positive faults.** Fix \(t\ge1\), set \(B_0=\{v_1,\ldots,v_t\}\), \(B_1=B\setminus B_0\), and write \(D_{B_1}\) for the zero-dimensional complex on \(B_1\), including the empty face. A face is precisely one of the following, or a subface: a face of \(\Delta_A\); a face of \(\Delta_B\); a face of the cone
\[
U=u*(\Delta_{B_0}*D_{B_1});
\]
a mixed edge \(\{x,y\}\) with \(x\in A'\), \(y\in B\); or a mixed triangle \(\{u,x,z\}\) with \(x\in A'\), \(z\in B_0\). Indeed, when two vertices of \(A'\) and one of \(B\) are selected, the latter has degree at least two; when one vertex of \(A'\) and two of \(B\) are selected, that \(A'\)-vertex has degree at least two. Any face containing \(u\) and some \(x\in A'\) can therefore contain at most one vertex of \(B\), necessarily from \(B_0\); without an \(A'\)-vertex, it can contain arbitrarily many vertices of \(B_0\) and at most one of \(B_1\). This exhausts all cases.

**Explicit elementary collapses and a contractible core.** Each edge \(\{x,z\}\), with \(x\in A'\) and \(z\in B_0\), has exactly one coface of higher dimension, namely the triangle \(\{u,x,z\}\). Hence simultaneously indexed, successively executed elementary free-face collapses remove all \((a-1)t\) such edge-triangle pairs. The remainder is the contractible candidate
\[
C_t=\Delta_A\cup\Delta_B\cup U
\]
together with exactly \((a-1)(b-t)\) further cross edges \(\{x,y\}\) for \(x\in A'\), \(y\in B_1\). To verify contractibility, the intersection \(\Delta_B\cap U=\Delta_{B_0}*D_{B_1}\) is nonempty and contractible because \(t\ge1\) makes \(\Delta_{B_0}\) a nonempty simplex. Both \(\Delta_B\) and \(U\) are contractible, so their union is contractible by CW homotopy pushout. Its intersection with \(\Delta_A\) is exactly \(\{u\}\), and adjoining \(\Delta_A\) therefore leaves a contractible complex \(C_t\). Every remaining cross edge has both endpoints in the connected core but is absent from that core, and distinct edges have disjoint relative interiors. Attaching \(m=(a-1)(b-t)\) one-cells to a contractible CW space produces \(\bigvee^m S^1\), over the integers and as a genuine homotopy type.

**Explicit integral cycles, maps and symmetry.** For \(y\in B_1\), both \(\{u,x\}\) and \(\{u,y\}\) are edges of \(C_t\), so the cycle \(c_{x,y}\) runs over the new cross edge and a two-edge path in \(C_t\). Under the preceding CW reduction these cycles are exactly a \(\mathbb Z\)-basis of \(H_1(X_t;\mathbb Z)\). They are permuted without orientation signs by the shore-preserving permutations of \(A'\), \(B_0\), and \(B_1\), giving the claimed integral module. All cycles \(c_{x,y}\) for \(y\in B_1\) already exist as cycles in \(X_{t-1}\), including when \(t=1\). Therefore each inclusion induces a surjection on \(H_1\). For \(t\ge2\), the additional triangle \(\{u,x,v_t\}\) in \(X_t\) fills \(c_{x,v_t}\), whereas the remaining \(c_{x,y}\) persist unchanged. This gives the stated basis projection. For \(t=1\), the surjection has kernel rank \((ab-1)-(a-1)(b-1)=a+b-2\). All quotient groups are free abelian, so these kernels are primitive direct summands and the surjections split integrally. Since every \(X_t\) is a circle wedge, all other reduced integral homology groups vanish.

## Verification

The standalone Python 3 program `verify.py` independently enumerates \(2^{a+b}\) candidate subsets for each of 72 parameter triples \(2\le a,b\le5\), \(0\le t\le b\). It verifies (i) the complete face classification against the direct induced-degree predicate; (ii) all \((a-1)t\) free-edge/triangle pairs and the exact remaining core-edge decomposition; and (iii) complete reduced mod-two boundary ranks and the circle multiplicities. Representative output is in `verification_output.txt`. All 72 tested profiles passed. This is finite corroboration only; the all-parameter integral and homotopy assertions are proved by the preceding combinatorial CW argument.

## Relationship to prior work

R. Sawant's May 24, 2026 manuscript *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees* establishes vertex decomposability for trees and motivates structural investigation of higher independence complexes. The graphs here are non-tree bicliques with localized missing edges, and the result concerns exact integral homotopy and inclusion maps, so the tree theorem does not imply it. A. Carnero Bravo's *The Forest Filtration of a Graph* (2023) gives the intact biclique dissociation homotopy and studies categorical products, but not the present star-fault parameter family. The indexed result *Mixed-dimensional dissociation homotopy under partial matching deletion from \(K_{a,b}\)* treats pairwise **disjoint** deleted edges, giving circles and eventually two-spheres. It coincides with the current problem when exactly one edge is missing, but does not imply the later clustered-fault steps: for instance, when \(a=b=5\) and \(t=3\), the star-fault complex is \(\bigvee^8S^1\), while the three-matching-fault complex is \(\bigvee^4S^1\vee S^2\). This shows a sharp dependence on whether faults share a hub, not merely their count. The first-fault and intact cases are comparative endpoints, not independent new claims.

## Limitations

Only the two-shore, one-hub clustered-edge-deletion family and its specified filtration are classified. No classification for arbitrary deleted bipartite subgraphs, higher independence thresholds, or all graph automorphisms is asserted. Literature searches and inspected closely related full texts cannot exclude every unindexed equivalent treatment. No independent external mathematical validation has been performed.

## References

1. R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150, first posted 2026-05-24, https://arxiv.org/abs/2605.25150.
2. A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, first posted 2023-07-25, https://arxiv.org/abs/2307.13271.
3. *Mixed-dimensional dissociation homotopy under partial matching deletion from \(K_{a,b}\)*, public research record, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-mixed-dimensional-dissociation-homotopy-under-partial-matching-d--04d61268ad5a.
