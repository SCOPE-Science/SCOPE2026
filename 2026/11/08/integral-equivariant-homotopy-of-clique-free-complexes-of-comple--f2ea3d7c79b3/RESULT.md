# Integral equivariant homotopy of clique-free complexes of complete split graphs

## Finding
For integers \(m\ge2\), \(n\ge2\), and \(3\le t\le m+1\), let \(G=K_m\vee\overline K_n\) be the complete split graph: its vertices are a clique \(C\) of size \(m\) and an independent set \(I\) of size \(n\), with every edge between the two parts. Let \(X=\mathsf{CF}_t(G)\) be the simplicial complex whose faces are vertex subsets containing no \(t\)-clique. Under the full graph-automorphism group \(\Gamma=S_C\times S_I\), there is a \(\Gamma\)-equivariant homotopy equivalence
\[
|X|\simeq_{\Gamma}\bigvee_{\substack{J\subseteq C\\|J|=t-1}} S^{t-2}_J,
\]
where \(S_J^{t-2}\) is the quotient of the \((t-2)\)-simplex on \(J\) by its boundary. The group \(S_C\) permutes these summands as oriented simplices (including the orientation sign when a summand is preserved), and \(S_I\) acts trivially on the displayed quotient model. Consequently, as an **integral** \(\mathbb Z[\Gamma]\)-module,
\[
\widetilde H_{t-2}(X;\mathbb Z)\cong \bigwedge^{t-1}\mathbb Z[C],
\]
and all other reduced integral homology vanishes. In particular \(X\simeq\bigvee^{\binom m{t-1}}S^{t-2}\) and \(\widetilde H_{t-2}(X;\mathbb Q)^\Gamma=0\). The homotopy type and integral symmetry module do not depend on \(n\ge2\), even though the complex dimension increases with \(n\).

## Assumptions and scope
All graphs are finite and simple; \(\vee\) denotes graph join, and \(\overline K_n\) is the edgeless graph on \(n\) labeled vertices. The phrase equivariant homotopy refers to the continuous geometric realization with its simplicial automorphism action. Since \(n\ge2\), clique vertices have degree \(m+n-1\) and independent vertices degree \(m\), hence \(\operatorname{Aut}(G)=S_C\times S_I\). A \(t\)-clique has \(t\) vertices, not necessarily induced (in a simple graph this distinction is immaterial for cliques). The stated domain is exactly \(m\ge2\), \(n\ge2\), \(3\le t\le m+1\).

## Proof
**Face decomposition.** Write \(\Delta(C)\) and \(\Delta(I)\) for full simplices. A subset \(F\) with \(F\cap I=\varnothing\) is allowed precisely when \(|F\cap C|\le t-1\). A subset meeting \(I\) is allowed precisely when \(|F\cap C|\le t-2\), because any clique contains at most one independent vertex and every independent vertex is adjacent to the entire core. Set
\[
A=\operatorname{sk}_{t-2}\Delta(C),\qquad D=\operatorname{sk}_{t-3}\Delta(C),\qquad B=D*\Delta(I).
\]
Then \(X=A\cup B\) and \(A\cap B=D\). This is an equality of simplicial complexes, not just a homotopy description.

**Equivariant contraction and quotient.** The barycenter \(b_I\) of the full simplex \(\Delta(I)\) is fixed by all of \(\Gamma\). Every point of \(|B|=|D*\Delta(I)|\) is joined to \(b_I\) by a segment inside \(|B|\); straight-line contraction to \(b_I\) is \(\Gamma\)-equivariant. The inclusion \(|B|\hookrightarrow |X|\) is a cofibration of finite \(\Gamma\)-CW complexes. Contracting \(B\) therefore gives a \(\Gamma\)-homotopy equivalence \(|X|\to |X|/|B|\): equivalently, this can be checked on \(H\)-fixed points for every subgroup \(H\le\Gamma\) by the ordinary cofibration and Whitehead criteria, since the same contraction makes \(|B|^H\) contractible. The quotient is naturally \(\Gamma\)-homeomorphic to \(|A|/|D|\).

**Sphere quotient.** All proper faces of each \((t-2)\)-simplex of \(A\) already belong to \(D\), and distinct top simplices intersect only within \(D\). Thus \(|A|/|D|\) is a one-point wedge of one \((t-2)\)-sphere for each \((t-1)\)-subset \(J\subseteq C\). This homeomorphism is \(\Gamma\)-equivariant if the group acts on the labeled simplex quotients. A permutation preserving \(J\) acts on the oriented top cell by its sign, while permutations of \(I\) act trivially. This proves the equivariant homotopy classification.

**Integral homology and character.** The quotient has one zero-cell and one cell of dimension \(t-2\ge1\) for each \(J\), with zero cellular differentials. Orient the cell \(J=\{j_1<\cdots<j_{t-1}\}\) by the ordered wedge \(e_{j_1}\wedge\cdots\wedge e_{j_{t-1}}\). The signed action is exactly the exterior-power permutation lattice \(\bigwedge^{t-1}\mathbb Z[C]\); no rationalization is needed. For \(\sigma\in S_m\) with \(c_j(\sigma)\) cycles of length \(j\), its rational homology character is
\[
\operatorname{tr}(\sigma)= [u^{t-1}]\prod_{j\ge1}\bigl(1+(-1)^{j-1}u^j\bigr)^{c_j(\sigma)}.
\]
The trace is independent of \(S_n\). Every orbit of \((t-1)\)-subsets has a stabilizing transposition within a chosen subset, which reverses its orientation when \(t-1\ge2\). Hence no nonzero rational class is \(S_m\)-invariant.

**Facets and face counts.** The two facet types are \((t-1)\)-subsets of \(C\) and unions of all of \(I\) with a \((t-2)\)-subset of \(C\). Their dimensions are \(t-2\) and \(n+t-3\), respectively. For every integer \(j\ge1\), with out-of-range binomial coefficients interpreted as zero, the exact number of \(j\)-vertex faces is
\[
\boxed{\ f_{j-1}=\binom mj\mathbf 1_{j\le t-1}+\sum_{a=0}^{\min(t-2,j-1)}\binom ma\binom n{j-a}\ }.
\]
The first term counts faces contained entirely in \(C\), and the second term counts faces meeting \(I\), so the contributions are disjoint.

## Verification
The standalone `verify.py` independently enumerates all vertex subsets, tests for the presence of complete \(t\)-subgraphs directly from the graph's adjacency matrix, and builds signed simplicial boundary maps. Its 30 tests cover \(2\le m\le5\), \(2\le n\le4\), and \(3\le t\le m+1\); homology ranks over \(\mathbb F_2\) and \(\mathbb F_3\) agree with the theorem. It also independently calculates 137 signed simplicial Lefschetz traces for part permutations and compares them with the exterior-power character. The output ends `ALL_VERIFY_OK`. These finite computations corroborate but do not replace the argument above, which holds for all stated parameters.

## Relationship to prior work
Ghosh and Selvaraja introduced systematic shellability criteria for clique-free complexes (arXiv:2602.09623, first submitted February 10, 2026). Their theorem for \(t\)-diamond-free chordal graphs does not cover this family: choosing \(t-1\) core vertices and two independent vertices induces two \(t\)-cliques intersecting in \(t-1\) vertices, with their remaining vertices nonadjacent. Their paper studies shellability, clique attachments and linear resolutions; the complete integral equivariant homotopy type above is not one of its results. Earlier work on clique ideals by Moradi (arXiv:1712.00583) concerns algebraic properties and other graph classes, and the publicly accessible abstract does not resolve the exact comparison for this family.

A previously available four-clique-free homotopy formula for joins of cliques with triangle-free graphs includes the **nonequivariant** \(t=4\) case here. This known implication is excluded from the originality claim. The present theorem concerns all thresholds in the displayed range and, essentially, the full equivariant sphere-quotient model and exact **integral** automorphism lattice; a nonequivariant wedge count does not determine these actions.

## Limitations
The theorem is limited to complete split graphs and does not classify arbitrary split graphs or their clique-free complexes. It does not claim a new nonequivariant classification at threshold four where the earlier join result already applies. It does not prove any shellability or Cohen–Macaulay assertion. The equivalence is equivariant under the stated finite automorphism group; no separate spectral or stable homotopy classification is claimed. Although targeted overlap searches found no covering equivariant theorem, unindexed or inaccessible work remains an originality risk.

## References
1. R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1 (February 10, 2026), https://arxiv.org/html/2602.09623v1.
2. S. Moradi, *\(t\)-clique ideal and \(t\)-independence ideal of a graph*, arXiv:1712.00583v1 (2017), https://arxiv.org/abs/1712.00583.
3. Standard equivariant CW cofibration and quotient homotopy principles; the explicit contraction and quotient decomposition required here are proved above.
