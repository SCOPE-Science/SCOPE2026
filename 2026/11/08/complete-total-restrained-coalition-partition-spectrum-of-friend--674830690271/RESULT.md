# Complete total restrained coalition-partition spectrum of friendship graphs

## Finding
For an integer \(m\ge 2\), let the **friendship graph** be
\[
F_m=K_1\vee(mK_2),
\]
with common apex \(h\) and \(m\) distinguishable peripheral edges (the triangle blades) \(E_1,\ldots,E_m\). A **total restrained dominating set** (TRD-set) \(S\) has the following two properties: every vertex has a neighbor in \(S\), and every vertex outside \(S\) has a neighbor outside \(S\). A **total restrained coalition partition** is a partition of the vertices into nonempty blocks, no block itself a TRD-set, such that every block can be joined to a different block to obtain a TRD-set.

Let \(c_m(k)\) be the number of such *unlabelled-block partitions of the labelled vertex set* with exactly \(k\) blocks. Write \(S(m,j)\) for the Stirling number of the second kind, the number of partitions of an \(m\)-element set into \(j\) nonempty, unordered blocks. Then, for every \(m\ge2\) and every integer \(k\),
\[
c_m(k)=
\begin{cases}
4^m-2^m+1,&k=2,\\
S(m,k-1),&3\le k\le m+1,\\
0,&\text{otherwise}.
\end{cases}
\]
Moreover, every such partition with at least three blocks consists of the singleton \(\{h\}\) and blocks formed by unions of complete peripheral edges. In every such partition, the associated total restrained coalition graph is precisely the star \(K_{1,k-1}\), centered at \(\{h\}\). A two-block coalition partition has coalition graph \(K_2\), which is also a star.

In particular,
\[
C_{tr}(F_m)=m+1,
\]
**the maximizing partition is unique**, and every integer block count \(2\le k\le m+1\) occurs. If \(B_m\) denotes the \(m\)-th Bell number, then the number of all total restrained coalition partitions is exactly
\[
\sum_k c_m(k)=4^m-2^m+B_m.
\]
The exceptional single-blade case \(F_1=K_3\) has exactly three two-block coalition partitions and no others; the uniqueness assertion is only for \(m\ge2\).

## Assumptions and scope
All graphs are finite, simple and undirected. The apex is adjacent to both ends of each blade and there are no edges between distinct blades. The TRD convention includes \(S=V(F_m)\) as a TRD-set: the outside-neighbor requirement is then vacuous. In counts \(c_m(k)\), graph vertices are fixed and distinguishable, but the blocks of a partition are not named or ordered. Distinct coalition edges are determined by whether the union of the corresponding blocks is TRD; no choice of a partner is counted separately.

## Proof
**Lemma 1 (complete TRD-set characterization).** A subset \(S\subseteq V(F_m)\) is a TRD-set if and only if it contains \(h\) and its peripheral vertices are a nonempty union of complete blades.

Indeed, suppose \(h\notin S\). Every peripheral vertex has neighbors only at its blade mate and at \(h\). Total domination forces both peripheral vertices in any blade having a selected vertex, and the requirement that unselected peripheral vertices have a selected neighbor forces every blade to have a selected vertex. Thus \(S\) would consist of all peripheral vertices, leaving the outside singleton \(\{h\}\) without an outside neighbor. This is impossible. If \(h\in S\), total domination requires at least one peripheral vertex in \(S\) to give \(h\) a selected neighbor. The complement lies in the disjoint peripheral edges and is isolate-free exactly when each blade contributes either zero or both of its vertices to the complement. Equivalently, \(S\setminus\{h\}\) is a nonempty union of whole blades. The same reasoning proves the converse, including the full vertex set.

**Two blocks.** Let \(H\) be the unique block containing \(h\). The other block cannot be a TRD-set by Lemma 1. Their union is the entire graph and therefore is TRD. Thus a two-block partition is a coalition partition exactly when \(H\) is not TRD. There are \(2^{2m}=4^m\) vertex subsets containing \(h\), obtained by choosing any peripheral subset, and precisely \(2^m-1\) of them are TRD by Lemma 1. Hence \(c_m(2)=4^m-2^m+1\). This count assigns no order to the blocks, because the apex identifies \(H\) uniquely.

**Three or more blocks.** Let \(\Phi\) have \(k\ge3\) blocks, with apex-containing block \(H\). Lemma 1 implies that no union of two blocks not containing \(H\) can be TRD. Consequently every other block must partner with \(H\). Suppose that \(H\) contains exactly one endpoint of some blade \(E_i\). Then every partner \(X\ne H\) must contain the other endpoint: otherwise \(H\cup X\) leaves precisely one peripheral vertex of \(E_i\) outside, isolated within the complement, contradicting Lemma 1. Two disjoint partner blocks cannot both contain that endpoint, a contradiction. Thus \(H\) contains no split blade. If \(H\) contained one complete blade, it would itself be TRD by Lemma 1, forbidden. Therefore \(H=\{h\}\).

Again by Lemma 1, a nonempty peripheral block \(X\) partners with \(\{h\}\) if and only if \(X\) is a union of whole blades. It follows that the other \(k-1\) blocks partition the \(m\) distinguishable blades into \(k-1\) nonempty, unordered classes. This correspondence is bijective. Therefore \(c_m(k)=S(m,k-1)\) for \(3\le k\le m+1\), and no larger partition exists. Only the apex block participates in coalition edges, so the coalition graph is the asserted star. For \(k=m+1\), the blade partition has \(m\) singleton classes, giving one maximizing vertex partition and no others.

The full count equals \((4^m-2^m+1)+(B_m-1)=4^m-2^m+B_m\), because for \(m\ge1\), exactly one partition of the blade set has a single block. When \(m=1\), the same two-block argument gives \(4-2+1=3\), and there are no higher-block coalition partitions.

## Verification
The included standalone `verify.py` constructs the graph adjacency lists without using Lemma 1, checks the TRD condition directly for every vertex subset, and enumerates every unordered set partition using a canonical restricted-growth recursion. For each accepted partition it independently builds its coalition graph and tests that its edges form the claimed star. The resulting complete enumerations agree with the theorem for \(1\le m\le5\):

| \(m\) | Total restrained coalition partitions, by block count \(k\) |
| ---: | --- |
| 1 | \(k=2:3\) |
| 2 | \(k=2:13,\ k=3:1\) |
| 3 | \(k=2:57,\ k=3:3,\ k=4:1\) |
| 4 | \(k=2:241,\ k=3:7,\ k=4:6,\ k=5:1\) |
| 5 | \(k=2:993,\ k=3:15,\ k=4:25,\ k=5:10,\ k=6:1\) |

Run `python3 verify.py` in the directory containing this file. It requires only the Python standard library and ends with `VERIFY_OK`. These finite computations corroborate the proof but do not establish the all-orders theorem without the preceding structural argument.

## Relationship to prior work
Chellali, Valenzuela-Tripodoro, Golmohammadi, Takhonov and Matrokhin introduced total restrained coalition partitions and their coalition graphs in arXiv:2412.18623 (first publicly submitted 17 December 2024). Their paper gives general bounds, exact results for complete graphs, complete bipartite graphs, stars, paths and cycles, and characterizes a triangle-free extremal case. Its complete-graph observation includes the single-blade triangle, so no novelty is claimed for \(F_1\). The paper does not establish the friendship-graph partition classification, Stirling/Bell enumerator or realizable coalition graphs stated here. Its general degree bounds do not imply these counts or the unique maximizing partition.

The friendship graphs \(F_m\), \(m\ge2\), are not complete multipartite: nonadjacency is not transitive among their peripheral vertices. Consequently, results that depend on being complete multipartite do not cover this classification. Research-index and literature searches for coalition-partition aliases, friendship/windmill graphs, Stirling counts and coalition graphs found related graph-invariant results but no statement implying this full partition spectrum. This is evidence of noncoverage among checked sources, not a proof of historical novelty.

## Limitations
The structural classification is proved for edge-blade friendship graphs only. It does not classify total restrained coalitions on generalized windmills with larger clique blades, arbitrary block graphs or arbitrary cactus graphs. Historical novelty is provisional: other terminology or unindexed results may exist. The proof and its computational corroboration have not undergone independent mathematical audit.

## References
1. M. Chellali, J. C. Valenzuela-Tripodoro, H. Golmohammadi, I. I. Takhonov and N. A. Matrokhin, *Total restrained coalitions in graphs*, arXiv:2412.18623, first version 2024-12-17; revised 2025-01-20. https://arxiv.org/abs/2412.18623 ; https://arxiv.org/html/2412.18623v2 .
2. M. Chellali et al., *Total restrained coalitions in graphs*, Computational and Applied Mathematics 45, article 50 (2026), first published online 2025-10-15, DOI:10.1007/s40314-025-03439-w. https://link.springer.com/article/10.1007/s40314-025-03439-w .
