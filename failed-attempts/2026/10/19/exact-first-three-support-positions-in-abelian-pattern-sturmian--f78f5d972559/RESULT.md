# Exact first-three support positions in Abelian pattern Sturmian words

## Finding

A binary infinite word is *Abelian pattern Sturmian* if, for each positive pattern size \(k\), its Abelian maximal pattern complexity is the smallest positive integer \(m\) satisfying \(\binom{m}{2}\ge k\). The 2026 incidence-forest characterization cited below identifies these words, after renaming the alphabet, as characteristic words of infinite sets of nonnegative integer positions whose bipartite sum-incidence graph is a forest.

For arbitrary integers \(0\le a<b<c\), put
\[
 d=c-b,\qquad g=\gcd(b-a,c-b).
\]
There exists an Abelian pattern Sturmian binary word whose **first three occurrences of the sparse letter** are at positions exactly \(a,b,c\) if and only if
\[
\boxed{a<d-g.}
\]
More precisely, for the finite support \(F=\{a,b,c\}\), its bipartite sum-incidence graph has exact cyclomatic number (first Betti number)
\[
\boxed{\beta_1(\Gamma_F)=\max\{0,a+1-d+g\}.}
\]
Thus the arithmetic condition is both necessary and sufficient, not merely a growth test. For instance, \(\{0,6,10\}\) is extendible despite its last two positions not satisfying the stronger sufficient doubling inequality, whereas the non-arithmetic-progression triple \(\{1,2,4\}\) is not extendible.

## Assumptions and scope

All positions are zero-based nonnegative integers. For any \(F\subseteq\mathbb N_0\), let \(\Gamma_F\) have two disjoint copies \(L_i,R_j\) of \(\mathbb N_0\), with an undirected edge \(L_iR_j\) precisely when \(i+j\in F\). Its finite-cycle rank \(\beta_1\) is the dimension of its first graph homology over any field, equivalently the number of edges minus vertices plus connected components after deleting isolated vertices. Only the finite-support graph \(\Gamma_{\{a,b,c\}}\) is used in the cycle-rank formula.

The existence assertion uses the incidence-forest characterization of Zeng, Xue, and Zeng (2026); it does not claim that every infinite extension of an admissible triple retains the forest property. It gives an explicit extension.

## Proof

**1. Two antidiagonals form disjoint paths.** Work on the finite graph with vertices \(L_0,\ldots,L_c,R_0,\ldots,R_c\); all other vertices are isolated. First retain only edges whose endpoint labels sum to \(b\) or \(c\). The \(c\)-edges form a perfect matching \(L_iR_{c-i}\), \(0\le i\le c\). Contract these matching edges and label the contracted vertices \(0,\ldots,c\) by their left label. Each \(b\)-edge \(L_iR_{b-i}\) becomes an edge between \(i\) and \(c-(b-i)=i+d\) for \(0\le i\le b=c-d\). Hence these two antidiagonals form exactly \(d\) trees: paths indexed by residues modulo \(d\), each containing the contracted indices in that residue class. Contraction of a forest preserves the cycle rank of a graph obtained by adding further edges.

**2. The third antidiagonal becomes arithmetic edges.** Set \(s=b-a\). A new \(a\)-edge \(L_iR_{a-i}\), \(0\le i\le a\), has endpoints in the two path components whose residues modulo \(d\) are \(i\) and
\[
 c-(a-i)=i+(c-a)=i+d+s\equiv i+s\pmod d.
\]
Contracting the \(d\) paths produces a multigraph on \(\mathbb Z/d\mathbb Z\) with exactly the edges \(i\to i+s\) for each integer \(0\le i\le a\). Loops and multiple edges are retained, since they contribute genuine cycles before contraction.

**3. Exact cycle rank of that multigraph.** The complete permutation \(r\mapsto r+s\pmod d\) has exactly \(g=\gcd(s,d)\) disjoint directed orbits, each containing the residue class \(r\pmod g\) and consisting of \(d/g\) vertices. If \(a<d\), every selected edge has a distinct starting residue. A selected subgraph of a directed permutation cycle has an undirected cycle (including loops and parallel length-two cycles) exactly when *all* edges of that orbit have been selected. The orbit indexed by \(r\), \(0\le r<g\), is fully selected precisely when its largest representative, \(r+d-g\), does not exceed \(a\). Therefore the number of independent cycles in this range is
\[
 \max\{0,a+1-d+g\}.
\]
If \(a\ge d\), the first \(d\) selected edges already connect every one of the \(g\) orbits and contribute \(g\) cycles; each of the remaining \(a+1-d\) edges increases the cycle rank by one. The same formula follows. This proves the cycle-rank identity for every \(a,b,c\). The graph is a forest exactly when \(a+1-d+g\le0\), equivalently \(a<d-g\).

**4. Realizability as an infinite-word prefix.** If the finite triple fails the forest test, it creates a cycle in the graph of *every* larger support containing it. Hence the cited incidence-forest characterization forbids it as the first three sparse-letter positions of an Abelian pattern Sturmian word.

Conversely, suppose \(\Gamma_{\{a,b,c\}}\) is a forest. Let \(t_2=c\), and recursively choose \(t_{j+1}=2t_j+1\) for \(j\ge2\). Set
\[
 E=\{a,b,c,t_3,t_4,\ldots\}.
\]
If the graph of the previous finite support is a forest with maximum sum \(m\), adding the sum \(t>2m\) introduces the matching \(L_iR_{t-i}\), \(0\le i\le t\). Every such edge has at least one endpoint label exceeding \(m\), and each vertex exceeding \(m\) is incident with no previous edge and with at most one new edge. Therefore no new cycle appears. Inductively all finite truncations of \(\Gamma_E\) are forests. Every cycle would use finitely many edges, so \(\Gamma_E\) is a forest. The cited characterization makes the characteristic word \(\mathbf 1_E\) Abelian pattern Sturmian, and its first three one-positions are exactly \(a,b,c\). This proves sufficiency.

## Verification

The accompanying standalone Python checker builds the finite bipartite graph and independently computes its cycle rank by disjoint-set unions and the Euler characteristic. It exhaustively compares the value to the closed formula for all \(0\le a<b<c\le44\) (14,190 triples), verifies examples on both sides of the boundary, and tests forest-preserving infinite-extension prefixes for 2,505 cases. All checks pass. These finite checks are not a proof of the universal formula; Steps 1–4 supply that proof.

Run from the files supplied with this result using `python3 check_three_sums.py`.

## Relationship to prior work

Zeng, Xue, and Zeng (2026, arXiv:2609.28059) characterize Abelian pattern Sturmian words by acyclicity of the bipartite sum-incidence graph. They also give a sufficient rapidly growing support construction and discuss additive restrictions. The new statement supplies an exact arithmetic, necessary-and-sufficient **three-position** test, a quantitative graph cycle-rank formula, and completion of every admissible triple to an infinite extremal word. The earlier abstract-level characterization does not itself state or calculate this three-parameter formula.

A related published support-envelope result establishes logarithmic growth restrictions for the sparse letter. Such overall bounds do not distinguish, for example, admissible \(\{0,6,10\}\) from inadmissible \(\{1,2,4\}\), nor calculate the exact cyclomatic number. The present classification is local, arithmetic, and logically different from an envelope bound. The general literature on cyclomatic number and union of matchings is used only as standard graph background.

## Limitations

The formula is exact only for the sum graph of a support with **three** elements. It does not characterize forestness of arbitrary finite supports with four or more elements, and the infinite-word theorem prescribes just the first three sparse-letter positions. The construction gives one rapidly growing continuation, not a classification of all continuations. Publication-priority comparisons are limited by incomplete access to the full 2026 primary PDF; the exact-formula novelty claim is made only relative to material actually examined and the referenced published comparisons, not as independent priority certification.

## References

1. Qingcheng Zeng, Yumei Xue, Cheng Zeng, “Abelian maximal pattern complexity and extremal words,” arXiv:2609.28059v1 (first posted 2026-09-23), especially the incidence-forest characterization and the fast-growth sufficient construction. https://arxiv.org/abs/2609.28059
2. Teturo Kamae, Steven Widmer, Luca Q. Zamboni, “Abelian maximal pattern complexity of words,” *Ergodic Theory and Dynamical Systems* 35 (2015), 142–151; https://doi.org/10.1017/etds.2013.51.
3. “Sharp logarithmic support envelope for Abelian pattern Sturmian words,” publicly available research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-logarithmic-support-envelope-for-abelian-pattern-sturmian--71c60228ce20.
