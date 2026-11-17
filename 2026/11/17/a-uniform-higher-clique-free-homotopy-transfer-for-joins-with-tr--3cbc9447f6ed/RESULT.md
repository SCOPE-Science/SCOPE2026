# A uniform higher-clique-free homotopy transfer for joins with triangle-free graphs

## Finding

Let \(H\) be a finite nonempty triangle-free simple graph, let \(s\geq2\), let \(t\geq5\), and put \(k=t-2\). For the graph join \(G=K_s\vee H\), the simplicial complex of vertex sets inducing no clique of order \(t\) has the integral homotopy type

\[
\boxed{\mathsf{CF}_t(G)\simeq
\bigvee^{\binom{s}{k}}\Sigma^{k}|\operatorname{Ind}(H)|
\;\vee\;
\bigvee^{\binom{s}{k+1}}S^k.}
\]

Here suspension is the **unreduced** topological suspension, and the wedge of zero copies means a point. This holds without assuming that \(\operatorname{Ind}(H)\) is connected or that its homology is torsion-free. In particular, for every integer \(j\),

\[
\widetilde H_j(\mathsf{CF}_t(G);\mathbb Z)
\cong
\widetilde H_{j-k}(\operatorname{Ind}(H);\mathbb Z)^{\oplus\binom{s}{k}}
\oplus
\begin{cases}\mathbb Z^{\binom{s}{k+1}},&j=k,\\0,&j\ne k.\end{cases}
\]

The isomorphism and wedge splitting are nonequivariant. This theorem treats all forbidden-clique orders \(t\geq5\) simultaneously, rather than extrapolating from one threshold.

## Assumptions and scope

Graphs are finite, simple and undirected. The join \(K_s\vee H\) adds all edges between the vertices of the complete graph and the vertices of \(H\). The clique-free complex \(\mathsf{CF}_t(G)\) contains exactly those subsets of \(V(G)\) with no complete subgraph on \(t\) vertices. The independence complex \(\operatorname{Ind}(H)\) contains all subsets spanning no edges. A triangle-free graph has clique number at most two. For all integers \(a,b\), the binomial coefficient \(\binom ab\) is zero when \(b<0\) or \(b>a\). If \(s<t-2\), the displayed formula means contractibility and agrees with the fact that \(G\) has no \(t\)-clique.

## Proof

Write \(S\) for the \(s\)-element center-clique vertex set, \(I=\operatorname{Ind}(H)\), and \(\Delta_S\) and \(\Delta_H\) for the corresponding full simplices. Set \(L_r=\operatorname{skel}_r\Delta_S\), interpreting \(L_r\) as the complex consisting only of the empty face when \(r<0\). A vertex subset is a face of \(\mathsf{CF}_t(K_s\vee H)\) according to its number \(j\) of vertices in \(S\):

- for \(0\leq j\leq k-1\), any subset of \(H\) is permitted because the largest possible clique uses at most \(j+2\leq k+1=t-1\) vertices;
- for \(j=k\), the subset of \(H\) must be independent;
- for \(j=k+1\), the subset of \(H\) must be empty;
- for \(j\geq k+2=t\), the center vertices themselves contain a forbidden clique.

Therefore the following equality of *simplicial complexes* is exact:

\[
X:=\mathsf{CF}_t(K_s\vee H)
= A\cup B\cup C,
\qquad
A=L_{k-2}*\Delta_H,\quad
B=L_{k-1}*I,\quad
C=L_k.
\]

If \(s<k\), then \(L_{k-2}=\Delta_S\) and \(X=\Delta_S*\Delta_H\) is a simplex, while both binomial coefficients vanish. Hence assume \(s\geq k\). Since \(H\) has at least one vertex, \(\Delta_H\) is a nonempty simplex; hence \(A\) is contractible. The simplicial inclusion \(A\subseteq X\) is a CW cofibration. Collapsing \(A\) to a point is therefore a homotopy equivalence \(X\simeq X/A\).

First consider \((A\cup B)/A\cong B/(A\cap B)\). The intersection is \(A\cap B=L_{k-2}*I\). For each \(k\)-element subset \(F\subseteq S\), the new faces of \(B\) not already in \(A\cap B\) are precisely the faces containing all of \(F\). Distinct such pieces meet only in \(A\cap B\). Consequently there is a homeomorphism of quotient CW complexes

\[
B/(A\cap B)\ \cong\
\bigvee_{F\in\binom Sk}
\bigl((\Delta_F*I)/(\partial\Delta_F*I)\bigr).
\]

Each factor is the reduced quotient of a cone on \(\partial\Delta_F*I\), so it is homotopy equivalent to \(\Sigma(\partial\Delta_F*|I|)\simeq\Sigma^k|I|\). The latter identification uses \(\partial\Delta_F\cong S^{k-2}\); the unreduced suspension convention is essential when \(I\) is disconnected. Hence

\[
(A\cup B)/A\simeq\bigvee^{\binom{s}{k}}\Sigma^k|I|.
\]

Finally \(C\) adjoins exactly one \(k\)-cell for each \((k+1)\)-element subset of \(S\), along its boundary lying in \(L_{k-1}\subseteq A\cup B\). Every space \(\Sigma^k|I|\) is \((k-1)\)-connected for \(k\geq2\), because \(|I|\) is nonempty; so is their wedge. Each attaching map \(S^{k-1}\to(A\cup B)/A\) is therefore nullhomotopic. Attaching these \(\binom{s}{k+1}\) cells yields a wedge of that many \(k\)-spheres in addition to the preceding summands. This proves the formula as a genuine homotopy equivalence, not just an equality of homology ranks. Integral homology follows by the suspension isomorphism and the homology of a wedge. \(\square\)

## Verification

The standalone Python 3 script `verify_transfer.py` enumerates faces directly from the forbidden \(t\)-cliques and independently computes the augmented simplicial boundary ranks over \(\mathbb F_2\). It compares the resulting reduced Betti numbers with the formula, using a separate independence-complex computation on \(H\). It exhausts every triangle-free labelled graph with one through four vertices within the indicated center and threshold ranges, and includes three cycle-six cases. The recorded execution reports 675 comparisons passed, including 470 target-threshold cases with \(t\geq5\). The 205 cases with \(t=4\) benchmark the previously known special case rather than constitute a new claim. These finite checks are corroboration; they neither certify integral torsion nor replace the above infinite-parameter proof.

As an illustrative consequence, the standard equivalence \(\operatorname{Ind}(C_6)\simeq S^1\vee S^1\) yields

\[
\mathsf{CF}_5(K_4\vee C_6)\simeq S^3\vee\bigvee^8S^4,
\qquad
\mathsf{CF}_6(K_5\vee C_6)\simeq S^4\vee\bigvee^{10}S^5.
\]

## Relationship to prior work

Ghosh and Selvaraja (first public preprint February 10, 2026, arXiv:2602.09623) systematically study these clique-free complexes, proving decomposability and shellability criteria, notably for diamond-free chordal graphs and clique attachments. Their Sections 3–5 do not provide a uniform arbitrary-triangle-free-join homotopy decomposition. **The \(t=4\) case of the present formula is previously published**, under the title *Double-suspension splitting for four-clique-free complexes of clique joins* (November 1, 2026). It is cited as a known boundary case and explicitly excluded from the new theorem.

A separate complete-split-graph classification already determines all clique-free thresholds when the graph \(H\) is edgeless, even equivariantly. That specialization is acknowledged as known and is not presented as original; the new information concerns arbitrary triangle-free \(H\), including graphs with edges and noncontractible independence complexes.

The published record *Clique joins transfer independence homology into triangle-free complexes with universal free loops* treats forbidden triangles. The established four-clique-free splitting uses two-dimensional edge blocks and triangle attachments; its claim and proof do not establish the variable higher-dimensional center skeleta, higher suspension powers and \(t\geq5\) cases here. The new theorem is **not** the \(t=4\) result, a restatement of it, or its numerical recomputation: it supplies one simultaneous classification at every strictly higher forbidden-clique order. General CW-cofibration and suspension tools are standard. An implicit extension of the earlier proof remains an originality risk; a failed search is not proof of novelty.

## Limitations

The graph \(H\) must be nonempty and triangle-free, and the theorem assumes \(t\geq5\). The splitting is nonequivariant and does not identify automorphism representations or homology of symmetry quotients. Inaccessible or unindexed equivalent literature could exist. The verifier tests only finite cases and mod-two homology, not integral homotopy or arbitrary orders.

## References

1. R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623, first submitted 2026-02-10, https://arxiv.org/abs/2602.09623 .
2. *Double-suspension splitting for four-clique-free complexes of clique joins*, publicly available research record (2026-11-01), https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-double-suspension-splitting-for-four-clique-free-complexes-of-cl--d3e82c39a4e9/RESULT.md .
3. *Clique joins transfer independence homology into triangle-free complexes with universal free loops*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-clique-joins-transfer-independence-homology-into-triangle-free-c--7b46ace7b0d6 .
4. *Integral equivariant homotopy of clique-free complexes of complete split graphs*, publicly available research record (2026-11-08), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-integral-equivariant-homotopy-of-clique-free-complexes-of-comple--f2ea3d7c79b3/RESULT.md .
5. M. Moradi, *t-clique ideal and t-independence ideal of a graph* (2018), cited for the clique-ideal framework only; no claim about the present homotopy formula is attributed to it.
