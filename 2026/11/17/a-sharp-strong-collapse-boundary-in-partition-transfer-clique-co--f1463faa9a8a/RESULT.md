# A sharp strong-collapse boundary in partition-transfer clique complexes

## Finding

For an integer \(n\ge1\) and \(k\ge1\), let \(G_{n,\le k}\) be the **induced subgraph** of the one-cell-transfer graph on partitions of \(n\), retaining precisely partitions with at most \(k\) nonzero parts. Let \(K_{n,\le k}=\operatorname{Cl}(G_{n,\le k})\) be its flag complex. Then the following combined sharp-boundary theorem holds:

1. **Uniform strong collapse.** For every integer \(n\ge1\), the complex \(K_{n,\le3}\) strongly collapses to its single vertex \((n)\), by an explicit lexicographic ordering of its vertices. In particular, it is contractible and has zero reduced integral homology in all degrees.
2. **First four-part witness.** At size \(n=8\), \(K_{8,\le4}\) strongly collapses onto the boundary of an octahedron, so \(\lvert K_{8,\le4}\rvert\simeq S^2\) and \(\widetilde H_2(K_{8,\le4};\mathbb Z)\cong\mathbb Z\), with every other reduced integral homology group zero.

Thus four permitted parts, rather than three, are necessary to realize nontrivial reduced topology within this natural length truncation, and four parts already suffice at size eight. The result is not a classification of \(K_{n,\le4}\) for all \(n\).

## Assumptions and scope

A partition of \(n\) is a weakly decreasing list \((\lambda_1,\ldots,\lambda_t)\) of positive integers summing to \(n\). Its **length** is \(t\). Distinct partitions are adjacent when one can be obtained from the other by decreasing one existing positive part by one and increasing a *different* part by one, possibly creating a new unit part, and resorting. This is exactly the Ferrers-corner cell-transfer adjacency of Lyudogovskiy (arXiv:2603.14370v1; equivalent formulation in arXiv:2603.18696v1). The graph is simple, and \(K_{n,\le k}\) is the flag complex of the induced graph, **not** the length-restricted clique collection with intermediate transfer paths allowed to pass through longer partitions.

In a graph, a vertex \(v\) is dominated by \(w\ne v\) if its closed neighborhood is contained in that of \(w\). Deleting a dominated vertex is a strong collapse of the associated flag complex: its link is a cone with apex \(w\). A sequence of such deletions gives an integral homotopy equivalence, not only a homology equivalence.

## Proof

**1. Coordinate description of all later neighbors.** Write each partition of length at most three as \(\lambda=(a,b,c)\), padded with zero parts, where \(a\ge b\ge c\ge0\) and \(a+b+c=n\). Order these triples lexicographically by increasing \((a,b)\). For any nonterminal triple \(\lambda\ne(n,0,0)\), put

\[
 w(\lambda)=\begin{cases}(a+1,b,c-1),&c>0,\\(a+1,b-1,0),&c=0.\end{cases}
\]

The displayed coordinates are already nonincreasing, and \(w(\lambda)\) is a later neighbor. Indeed, a single transfer increases the first part by one using a unit from the third part when \(c>0\), or from the second part when \(c=0\).

Every neighbor of \(\lambda\) which is later in this ordering belongs to the following list, after sorting and omitting inadmissible/duplicate values:

\[
 U=(a,b+1,c-1),\quad V=(a+1,b,c-1),\quad W=(a+1,b-1,c).
\]

Here \(U\) requires \(c>0\) and may sort to \(V\) when \(a=b\); \(V\) requires \(c>0\); \(W\) requires \(b>0\). To see exhaustiveness, a transfer changes one part by \(+1\), one other part by \(-1\), and nothing else. Increasing the largest part produces only \(V\) or \(W\); preserving the largest part while advancing the second produces only \(U\). Moves that reduce the largest part or the second part are earlier in the ordered list. Repeated entries can only identify, not add, a new later neighbor.

**2. Dominating later neighbor.** When \(c>0\), take \(w=V\). It is adjacent to \(U\) (move one cell from the second part of \(U\) to its largest part); it is adjacent to \(W\) (move one cell from the third part of \(W\) to its second part, when \(b>c\); for \(b=c\), \(V=W\)). It is also adjacent to \(\lambda\). Thus every later neighbor of \(\lambda\) lies in the closed neighborhood of \(V\). When \(c=0\), the only possible later neighbor is \(W=(a+1,b-1,0)\), so \(W\) dominates \(\lambda\). At each stage earlier vertices have already been removed; the closed neighborhood inclusion holds **in the current induced graph**. All triples except \((n,0,0)\) are therefore deleted by strong collapses. This proves the first assertion for all \(n\ge1\), including zero parts and equality cases.

**3. The four-part witness.** For \(n=8\), there are fifteen partitions of length at most four. The following nine vertex/dominator pairs, in the stated order, are all valid closed-neighborhood dominations in the current graph:

\[
\begin{array}{c|c}
\text{deleted partition}&\text{dominating partition}\\\hline
(2,2,2,2)&(3,2,2,1)\\
(4,4)&(5,3)\\
(5,1,1,1)&(5,2,1)\\
(5,3)&(5,2,1)\\
(6,1,1)&(6,2)\\
(8)&(7,1)\\
(7,1)&(6,2)\\
(6,2)&(5,2,1)\\
(5,2,1)&(4,3,1)
\end{array}
\]

The six remaining partitions are

\[
(4,3,1),\ (4,2,2),\ (4,2,1,1),\ (3,3,2),\ (3,3,1,1),\ (3,2,2,1).
\]

Their induced graph has exactly three nonedges, the disjoint pairs

\[
\{(4,3,1),(3,2,2,1)\},\quad
\{(4,2,2),(3,3,1,1)\},\quad
\{(4,2,1,1),(3,3,2)\}.
\]

Therefore this graph is the complete graph on six vertices minus a perfect matching. Its clique complex is the join of three discrete two-point spaces, namely \(S^0*S^0*S^0\cong S^2\), the octahedral boundary. The nine valid strong collapses establish the claimed *integral homotopy* equivalence.

## Verification

The enclosed standalone `verify.py` (Python 3, standard library only) constructs the restricted partition-transfer graphs independently from row transfers and from conjugate-coordinate differences. The independent constructions agree for every \(1\le n\le30\) at length at most three and for \(n=8\) at length at most four. It checks the **specific** domination witness above at each step for every \(1\le n\le150\) (100,300 verified deletions), rather than searching for a suitable replacement. It separately replays all nine four-part domination steps, checks the exact three nonedges of the remaining six-vertex graph, and independently enumerates its clique face vector \((6,12,8)\). The original fifteen-vertex graph has clique counts \((15,30,18,1)\). Execute `python3 verify.py` from the extracted package; `verification_output.txt` records an exact execution.

The unrestricted statement is established by Steps 1–2, not extrapolated from these finite checks. The \(n=8\) classification is an exhaustive finite proof using all fifteen partitions and explicit elementary strong collapses.

## Relationship to prior work

Lyudogovskiy proved that the **unrestricted** clique complex \(K_n\) is a wedge of two-spheres and tabulated the first sphere counts, including \(K_8\simeq S^2\). This does not imply the strong collapsibility of the induced length-three truncation: a contractible or spherical full complex can contain induced subcomplexes of other homotopy types. The distinct present assertion is a universal vertex-folding scheme **inside** the length-at-most-three induced graph, together with a concrete induced four-part octahedral survivor at the first nontrivial size. The local transfer-neighborhood theorem in arXiv:2603.18696 provides useful independent adjacency context but does not establish this global length-stratified collapse.

Related later work gives positive partition-statistic formulas for the full complex's two-sphere multiplicity and filtrations by a *height* statistic. Those address total or height-filtered homology, not the strong-collapse sequence for the **number-of-parts** induced filtration or its four-part core. Distinct filtration parameters cannot be substituted without an implication proof.

## Limitations

Only the three-part truncations for all sizes and the single four-part example \(n=8\) are classified. No assertion is made that every larger four-part truncation has the same homotopy type, that all length-truncation inclusions are homology injections, or that the full complex strongly collapses to its low-length subcomplex. An equivalent unindexed length-filtration result is possible. Independent mathematical validation has not been performed.

## References

[1] F. B. Lyudogovskiy, *The homotopy type of the clique complex of the partition graph*, arXiv:2603.14370v1, first public 2026-03-15, https://arxiv.org/html/2603.14370v1.

[2] F. B. Lyudogovskiy, *Local Morphology of the Partition Graph*, arXiv:2603.18696v1, first public 2026-03-19, https://arxiv.org/html/2603.18696v1.

[3] F. B. Lyudogovskiy, *Numerical topology of the clique complex of the partition graph*, arXiv:2603.26656v1, first public 2026-03-27, https://arxiv.org/abs/2603.26656.

[4] F. B. Lyudogovskiy, *Local Complexity, Overlap Control, and Global Simplicity in Partition Graphs*, arXiv:2606.20773v1, first public 2026-06-18, https://arxiv.org/abs/2606.20773.
