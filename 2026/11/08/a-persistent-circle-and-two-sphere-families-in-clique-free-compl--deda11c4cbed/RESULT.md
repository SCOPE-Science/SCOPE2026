# A persistent circle and two sphere families in clique-free complexes of edge-glued complete graphs

## Finding
For integers \(q\ge4\) and \(k\ge2\), let \(E_{q,k}\) be the simple graph obtained by identifying one common **edge** in \(k\) copies of \(K_q\), with all other vertices distinct and no edges between the private vertex sets of different copies. Let \(X_{q,k}=\mathsf{CF}_3(E_{q,k})\) be the simplicial complex of vertex subsets containing no triangle. Put \(m=q-2\), and interpret a wedge with zero summands as a point. Then, as an **ordinary** homotopy equivalence,
\[
 |X_{q,k}|\simeq S^1\vee
 \bigvee^{2(m-1)^k}S^k\vee
 \bigvee^{\binom{m-1}{2}^{k}}S^{2k-1}.
\]
All integral homology is free; in particular, \(\pi_1(|X_{q,k}|)\cong\mathbb Z\). For \(q=4,k=2\), the space is \(S^1\vee S^2\vee S^2\); for \(q=5,k=2\), it is \(S^1\vee\bigvee^8 S^2\vee S^3\).

The full graph automorphism group is \(\Gamma\cong S_2\times(S_m\wr S_k)\), where the first factor interchanges the endpoints of the common edge. Set \(U_m=\ker(\mathbb Z^m\xrightarrow{\sum}\mathbb Z)\). As integral representations of \(\Gamma\), the three nonzero reduced homology groups are:

* \(\widetilde H_1\cong\mathbb Z_{\mathrm{sgn}}\), with the common-edge interchange acting by \(-1\) and all private-block permutations acting trivially;
* \(\widetilde H_k\cong\mathbb Z^2\otimes U_m^{\otimes k}\), with the common-edge interchange swapping the two standard basis vectors and private-block permutations acting by their natural tensor action, including sign \(-1\) for each transposition of tensor factors;
* \(\widetilde H_{2k-1}\cong(\bigwedge^2 U_m)^{\otimes k}\), with common-edge interchange trivial, natural within-block actions, and **no extra sign** for permutations of the tensor factors.

If \(m=2\), the final representation is zero. These module statements do **not** claim an equivariant wedge decomposition. As a consequence, the geometric quotient \(|X_{q,k}|/\Gamma\) is connected and has zero reduced **rational** homology.

## Assumptions and scope
A triangle is a set of three mutually adjacent vertices; a face of \(\mathsf{CF}_3(G)\) is any vertex subset inducing no triangle. The \(k\) private blocks \(P_1,\ldots,P_k\) each have \(m=q-2\) vertices; the common-edge endpoints are \(u,v\). Exactly the edges within each complete graph on \(P_i\cup\{u,v\}\) are present. Thus a face \(F\) must satisfy \(|F\cap P_i|+|F\cap\{u,v\}|\le2\) for each \(i\). This rule defines the complex without ambiguity, including small parameter boundaries.

## Proof
Let \(S_s(m)\) denote the simplicial complex on an \(m\)-element set consisting of subsets of cardinality at most \(s\). Its augmented integral chain complex identifies with the truncation of the exterior Koszul chain complex \((\bigwedge^{\bullet}\mathbb Z^m,\iota_\varepsilon)\), where \(\varepsilon\) is the sum of coordinates. Splitting \(\mathbb Z^m=\mathbb Z e_1\oplus U_m\) with \(\varepsilon(e_1)=1\) shows that the only possible nonzero reduced homology is
\[
 \widetilde H_{s-1}(S_s(m);\mathbb Z)\cong\bigwedge^s U_m
\]
when \(1\le s\le m\), and its rank is \(\binom{m-1}{s}\). If \(s=m\), the complex is a simplex and the displayed exterior power vanishes. Standard skeleton connectivity and the CW dimension imply that \(S_s(m)\) is a wedge of precisely that many \((s-1)\)-spheres (with the usual interpretation for \(s=1\)).

Write \(A=S_2(m)^{*k}\) and \(B=S_1(m)^{*k}\), where the factors use the disjoint private vertex blocks. The face rule gives the **exact equality of subcomplex unions**
\[
 X_{q,k}=A\cup(u*B)\cup(v*B)\cup\{u,v\},
\]
where \(u*B\) and \(v*B\) are cones, and the final term denotes the edge with its faces. By the join homology and homotopy formula,
\[
 A\simeq\bigvee^{\binom{m-1}{2}^k}S^{2k-1},\qquad
 B\simeq\bigvee^{(m-1)^k}S^{k-1}.
\]
The complex \(A\) is \((2k-2)\)-connected whenever noncontractible; otherwise it is contractible. Since \(B\) has CW dimension \(k-1\) and \(k\ge2\), the inclusion \(B\hookrightarrow A\) is nullhomotopic. Attaching each of the two cones along this null map contributes **one suspension of \(B\)**, giving
\[
 T=A\cup(u*B)\cup(v*B)\simeq A\vee\Sigma B\vee\Sigma B.
\]
Here the second cone still attaches by a null map because its base lies in the first cone, which is contractible. The space \(T\) is path connected, so adding the extra edge \(uv\) between its already-present endpoints contributes \(S^1\). This proves the ordinary wedge classification, the integral torsion statement, and the fundamental group.

For the integral symmetry modules, the chain isomorphism \(\widetilde H_{s-1}(S_s(m))\cong\bigwedge^s U_m\) is natural for permutations of the \(m\) vertices. Interchanging two factors in a join of complexes with top reduced homology in degree \(s-1\) introduces the Koszul sign \((-1)^{s^2}=(-1)^s\). The high-degree group is inherited from \(A\), with \(s=2\), yielding the asserted even factor-permutation action. In degree \(k\), the natural relative-chain description for \((T,A)\) identifies the two summands with the two cone tips \(u,v\), and the common-edge transposition swaps these summands. Here \(s=1\), so permuting private factors contributes the odd sign. Finally, \(T\) is simply connected, as its nonzero reduced homology arises only in degrees at least two and the described homotopy wedge contains no circles. The added edge generates \(H_1\); swapping its endpoints reverses its orientation, while private-block automorphisms fix the edge and act trivially on that class.

To obtain the quotient claim, subdivide the complex barycentrically so finite-group transfer applies. Over \(\mathbb Q\), the homology of the quotient is the \(\Gamma\)-invariant part of rational homology. For \(1\le s\le m-1\), the symmetric group \(S_m\) has no invariants in \(\bigwedge^s U_m\): its invariant exterior tensors are zero (for example by the standard decomposition of exterior powers of the permutation augmentation module). Therefore the private-block subgroup kills invariants in both higher-degree modules, and the edge interchange kills the sole degree-one class. This establishes rational acyclicity; no integral acyclicity or contractibility of the quotient is asserted.

## Verification
The standalone `verify.py` enumerates face sets directly from the triangle avoidance condition. It computes exact mod-\(2\) and mod-\(3\) boundary ranks and compares reduced Betti numbers with all three predicted degrees. It also evaluates signed fixed-simplex traces of the common-edge swap, a private-vertex transposition, and a page transposition, comparing their reduced Lefschetz numbers with the predicted integral representation characters. The check covers \(7\) parameter pairs, \(14\) modular homology comparisons and \(21\) signed character comparisons. This finite verification corroborates but does not replace the unrestricted proof above.

## Relationship to prior work
Ghosh and Selvaraja (2026) prove shellability for clique-free complexes of \(t\)-diamond-free chordal graphs, including block graphs, and discuss obstructions beyond that class. An edge-glued complete-graph book contains overlapping triangles sharing an edge, so it is not in that hypothesis. Their inspected preprint establishes no exact three-degree homotopy formula or full integral symmetry modules for this edge-glued family. Earlier calculations for **vertex-glued** windmills do not imply this edge-glued result: the additional shared edge introduces a persistent fundamental-circle class, and each endpoint contributes a separate suspension of the private-block link. This is a statement-and-implication comparison, not a novelty proof from the absence of a matching title.

## Limitations
The theorem treats exactly triangle avoidance, a common **edge**, equal clique sizes, and at least two pages. It does not classify larger common cores, arbitrary chordal graphs, or higher \(t\)-clique-free complexes. The wedge splitting is nonequivariant; the representation formulas are canonical only at the level of integral homology. The rationally acyclic quotient may have integral torsion and is not claimed contractible. Unindexed equivalent work remains a literature risk.

## References
1. R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623, first publicly posted 2026-02-10, especially Theorem 3.3 and Example 3.6.
2. Standard augmented-simplex chain and join calculations for simplicial complexes, e.g. A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002, Sections 0 and 2.
