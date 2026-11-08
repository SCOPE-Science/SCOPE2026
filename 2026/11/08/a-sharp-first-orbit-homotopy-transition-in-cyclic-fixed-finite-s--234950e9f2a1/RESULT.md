# A sharp first-orbit homotopy transition in cyclic fixed finite-subset spheres

## Finding
Let \(m\ge3\) and let \(C_m\) act on the unit two-sphere by rotation of angle \(2\pi/m\) about the north–south axis. Write \(N,S\) for its poles. Define \(\operatorname{exp}_k(S^2)\) to be the space of **nonempty unordered subsets** of \(S^2\) of cardinality at most \(k\), with quotient topology from \((S^2)^k\), with repeated entries forgotten. Let
\[
F_{m,k}=\bigl(\operatorname{exp}_k(S^2)\bigr)^{C_m}.
\]
**Theorem.** For every pair of integers \(m\ge3\) and \(1\le k<2m\),
\[
F_{m,k}\simeq
\begin{cases}
\{N,S\},&k=1,\\
\{\mathrm{three\ points}\},&2\le k<m,\\
S^2\sqcup\{\mathrm{point}\},&k=m,\\
S^1\vee\bigvee^3 S^2,&k=m+1,\\
\bigvee^2 S^1\vee\bigvee^4 S^2,&m+2\le k<2m.
\end{cases}
\]
The last range is nonempty for all \(m\ge3\). This determines every integral homology group and fundamental group in the stated first-free-orbit range: the groups are free abelian; in the connected cases, the fundamental group is respectively trivial, free of rank one, and free of rank two. In particular, nontrivial first homology starts **exactly** when \(k=m+1\), independently of the rotation order.

More precisely, there is a *homeomorphic* model made of at most four copies of \(S^2\), each attached only at finite subsets of the two poles; this gives a quotient-space description stronger than the displayed homotopy equivalences. The inclusions between positive-dimensional homology groups along the cardinality filtration are injective whenever both corresponding groups are defined, since successive sphere sheets attach along polar points.

## Assumptions and scope
The cyclic action is effective and rotates around the fixed north–south axis, so all nonpolar points have orbits of exactly \(m\) elements and \(N,S\) alone are fixed. The exponent-space topology identifies repeated entries and uses *sets*, not multisets. Only subsets with \(1\le k<2m\) are considered, so at most one free orbit of size \(m\) occurs. A wedge of no spheres is a point; a disjoint union is not understood as a wedge. Fundamental groups are asserted only for path-connected cases; no group is assigned to a disconnected space without a chosen base component. All homology assertions are integral, not merely rational.

## Proof
**1. Complete enumeration of fixed subsets.** A point of \(F_{m,k}\) is exactly a nonempty subset invariant under all rotations in \(C_m\). Such a set uniquely splits into a polar part \(P\subseteq\{N,S\}\) and a union of distinct free orbits of nonpolar points. Every free orbit has cardinality \(m\), so for \(k<2m\) there is at most one. If there is no free orbit, the only candidates are \(\{N\}\), \(\{S\}\), and (provided \(k\ge2\)) \(\{N,S\}\). If there is a free orbit, it can be accompanied by the polar set \(P\) precisely when \(m+|P|\le k\). There are thus exactly four possible sheet types indexed by \(P=\varnothing,\{N\},\{S\},\{N,S\}\), appearing successively at cardinalities \(m,m+1,m+1,m+2\).

**2. A sphere for each allowed polar part.** The orbit quotient \(S^2/C_m\) is homeomorphic to \(S^2\): a longitude coordinate is divided out by a finite cyclic angular rotation and the two poles remain the suspension points of a circle. For each permitted \(P\), consider
\[
\Phi_P:S^2/C_m\longrightarrow F_{m,k},\qquad [x]\longmapsto C_mx\cup P.
\]
This is continuous, since finite union of the finitely many continuous orbit maps descends through the quotient. Its image is compact. It is injective on the nonpolar stratum, whose elements remember the free orbit and the polar part, and at the two quotient poles one has the exact endpoint formulae
\[
\Phi_P([N])=P\cup\{N\},\qquad \Phi_P([S])=P\cup\{S\}.
\]
These are also the **only** identifications within the image and between different images: different nonpolar orbits cannot yield the same underlying subset, and the polar set is recovered uniquely from the subset. The target is Hausdorff because it is a quotient of a compact Hausdorff space by a closed finite-coordinate set-equivalence relation, so the union of the maps is a quotient of a compact disjoint union onto the full fixed space. Consequently the geometric fixed space is *exactly*, up to homeomorphism, the finite union of the indicated sphere sheets glued at their polar endpoints. For \(P=\{N,S\}\) the north and south poles of one sheet become a *single* point \(\{N,S\}\); in the other three sheets the endpoints remain distinct.

**3. Collapse to a graph of spheres.** For \(k\ge2\) the polar configurations give three vertices, denoted \(A=\{N\}\), \(B=\{S\}\), \(C=\{N,S\}\). Every attached copy of a sphere with two distinct endpoint vertices contributes one sphere class and an edge connecting these vertices in the underlying incidence multigraph. A sheet with its two endpoints identified contributes one sphere class and one loop edge. A cellular subdivision of the sheets has one two-dimensional fundamental cycle per sheet and a graph-equivalent one-skeleton. Collapsing a spanning tree of this one-skeleton yields a homotopy equivalence to a wedge of one \(S^2\) per sheet and one \(S^1\) for each independent incidence-graph cycle. This follows, for example, by presenting each sphere as two disks glued along their common boundary and using disjoint paths from its two marked poles to a chosen basepoint; all attachments are at points, and thus do not produce nontrivial maps of the two-dimensional sphere cells.

For \(k<m\), only polar vertices appear: exactly two if \(k=1\), otherwise all three. For \(k=m\), the \(P=\varnothing\) sheet connects \(A\) to \(B\), giving one sphere and leaving \(C\) isolated. At \(k=m+1\) the two extra sheets \(P=\{N\}\) and \(P=\{S\}\) give graph edges \(A-C\) and \(B-C\), creating precisely one graph cycle; there are three sphere sheets. At \(k=m+2\), the fourth sheet \(P=\{N,S\}\) adds a loop at \(C\), creating a second graph cycle and a fourth sphere sheet. Since no second free orbit is allowed below \(2m\), the result then remains unchanged through \(k=2m-1\). The stated homotopy types follow.

**4. Integral homology and the exact threshold.** A finite wedge of circles and two-spheres has free integral homology in degrees one and two and none in higher degrees, while the initial disconnected cases have the stated zero-th homology. Each new sheet is attached along a finite set of old polar vertices, so the inclusion does not kill pre-existing positive-degree cycles. The component \(C\) first joins the sphere at \(k=m+1\), where the graph gains its first cycle and the fundamental group becomes infinite cyclic; a second free generator appears at \(k=m+2\). This proves the sharpness of both thresholds.

## Verification
The supplied `verify.py` constructs a finite cellular model directly from the four orbit-sheet types. For each \(3\le m\le11\) and \(1\le k<2m\) it creates a three-segment equator and two capped hemispheres for each sheet, with distinct radial edges even when the polar endpoints of the final sheet are identified. It verifies \(\partial_1\partial_2=0\), computes exact rational ranks of the cellular boundary maps, checks every predicted connected-component count and first and second Betti number, and independently verifies the Euler characteristic. There are 117 parameter cases; the recorded output is `ALL_VERIFY_OK cases=117 max_total_cells=75`. These checks are finite corroboration, not a proof for arbitrarily large \(m\); the proof above uses the free-orbit classification uniformly.

## Relationship to prior work
Mostovoy [1, Theorem 1] provides the complete rational homology of the *ambient* finite subset spaces of spheres. These ambient Betti numbers do not determine the homotopy types or fundamental groups of geometric fixed-point subspaces. A related study [2] determines the rational orthogonal homology characters of the ambient spaces and rational homology of finite orthogonal *quotients*. Its geometric reflection-fixed set appears only through an Euler-characteristic computation, and its theorem does not yield the rotation-fixed integral homotopy types classified here. Schwede [3] studies stable equivariant **symmetric products**, not the unstable finite-subset quotient that forgets multiplicities, so those stable results do not cover this theorem. The present result identifies the sharp first-free-orbit filtration regime and its geometric changes, not just ambient characters or fixed Euler numbers.

## Limitations
The topological classification is restricted to rotations of the two-sphere and to \(k<2m\). At and above \(2m\), fixed subsets can contain multiple distinct free orbits, so the exact four-sheet argument does not apply. The theorem does not classify arbitrary finite rotation groups, full equivariant homotopy types, or fixed-point spaces in higher-dimensional spheres. The cited sources were compared for mathematical implication, but unindexed equivalent treatments cannot be ruled out. A 2026 paper on ordinary Euler characteristics of finite subset spaces [4] was located, but no complete text was available for a conclusive detailed comparison; its subject does not itself establish this homotopy classification.

## References
1. Jacob Mostovoy, *Finite subset spaces of spheres*, arXiv:2603.01439v1, first public March 2, 2026, especially Theorem 1 and Sections 2 and 4. https://arxiv.org/html/2603.01439v1
2. *Orthogonal homology characters and quotient dichotomy for finite subset spheres*, published mathematical research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-orthogonal-homology-characters-and-quotient-dichotomy-for-finite--ecd0c222ac84
3. Stefan Schwede, *Equivariant properties of symmetric products*, arXiv:1403.1355v2, 2017, Introduction and Section 3. https://arxiv.org/html/1403.1355v2
4. Walid Taamallah, *The Euler Characteristic of Finite Subset Spaces*, arXiv:2607.17830v1, 2026 (title and abstract only; full text not inspected). https://arxiv.org/abs/2607.17830
