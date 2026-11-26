# Dominant mixed metric dimension of crown graphs
## Finding
For every integer \(n\ge3\), let
\[
\operatorname{Cr}_n=K_{n,n}-M
\]
be the crown graph obtained from the complete bipartite graph with parts
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\}
\]
by deleting the perfect matching
\[
M=\{a_i b_i:1\le i\le n\}.
\]
Then
\[
\gamma_{mr}(\operatorname{Cr}_n)=
\begin{cases}
3,&n=3,\\
n,&4\le n\le6,\\
n-1,&n\ge7.
\end{cases}
\]

For every \(n\ge7\), the minimum mixed resolving dominating sets are exactly the sets that omit one deleted matched pair \(\{a_h,b_h\}\), choose exactly one endpoint from every other deleted matched pair, and choose at least three vertices from each bipartition class. Consequently the number of minimum sets is
\[
n\bigl(2^{n-1}-n^2+n-2\bigr).
\]

## Assumptions and scope
All graphs are finite, simple, and connected. For a vertex landmark \(s\), the distance from \(s\) to an edge \(uv\) is
\[
d(s,uv)=\min\{d(s,u),d(s,v)\}.
\]
A mixed resolving set distinguishes every two distinct elements of \(V(G)\cup E(G)\) by their ordered distance vectors. A mixed resolving dominating set is simultaneously mixed resolving and dominating, and its minimum cardinality is denoted by \(\gamma_{mr}(G)\).

For a landmark set \(S\subseteq V(\operatorname{Cr}_n)\), put
\[
P=\{i:a_i\in S\},\qquad Q=\{i:b_i\in S\}.
\]

## Proof
In \(\operatorname{Cr}_n\), distinct vertices in the same bipartition class have distance \(2\), the deleted matched pair \(a_i,b_i\) has distance \(3\), and \(a_i,b_j\) have distance \(1\) when \(i\ne j\).

We first derive a lower bound for every mixed resolving set. Suppose \(a_i,a_j\notin S\) for distinct indices \(i,j\). Every selected \(a\)-vertex has distance \(2\) to both. A selected \(b_k\) distinguishes them only when \(k=i\) or \(k=j\), because otherwise its distance to both is \(1\). Thus, among indices outside \(P\), at most one can also lie outside \(Q\). Equivalently,
\[
|P\cup Q|\ge n-1.
\]
Therefore every mixed resolving set has size at least \(n-1\).

If equality holds, then
\[
|S|=n-1
\]
forces
\[
P\cap Q=\varnothing
\]
and
\[
P\cup Q=\{1,\ldots,n\}\setminus\{h\}
\]
for one index \(h\). Thus a size-\(n-1\) mixed generator must omit the whole deleted matched pair \(\{a_h,b_h\}\) and take exactly one endpoint from every other deleted matched pair.

We now classify which such transversals are mixed resolving. For an edge \(a_i b_j\), where \(i\ne j\), its distance to a selected \(a_k\) is
\[
\begin{cases}
0,&k=i,\\
2,&k=j,\\
1,&k\notin\{i,j\},
\end{cases}
\]
and its distance to a selected \(b_k\) is
\[
\begin{cases}
2,&k=i,\\
0,&k=j,\\
1,&k\notin\{i,j\}.
\end{cases}
\]
If \(|P|=1\), the sole selected \(a_i\) has the same representation as the edge \(a_i b_h\). If \(|P|=2\), say \(i,j\in P\), then the selected vertex \(a_i\) has the same representation as the edge \(a_i b_j\). Hence a nonempty \(P\) must have size at least \(3\). Symmetrically, a nonempty \(Q\) must have size at least \(3\).

Conversely, a transversal is mixed resolving whenever either one of \(P,Q\) is empty and the other has size at least \(3\), or both \(|P|\) and \(|Q|\) are at least \(3\). To see this, first note that every selected vertex has its own zero coordinate. An unselected vertex whose deleted mate is selected has a unique distance-\(3\) coordinate, so it cannot collide with a vertex or edge lacking that coordinate. The two wholly omitted vertices \(a_h,b_h\) have no zero or three coordinates; their vectors have respectively distance \(2\) on the selected \(A\)-coordinates and on the selected \(B\)-coordinates. When both sides are represented, each has at least three distance-\(2\) coordinates, while an edge can differ from the all-one vector in at most two landmark coordinates. When one selected side is empty, the two omitted vectors are respectively all ones and all twos, again unlike any edge vector.

Finally, the edge formula above is injective. The coordinates different from \(1\) identify the endpoint indices: at a selected \(a_k\), value \(0\) means \(k=i\) and value \(2\) means \(k=j\); at a selected \(b_k\), these roles reverse. If one endpoint index is the omitted index \(h\), the single exceptional coordinate identifies the other endpoint and its orientation, and \(h\) is already known from \(S\). Thus all edges are distinct. The only possible selected-vertex versus edge collision is exactly the one already exhibited when a selected side has size \(1\) or \(2\). This proves the classification of all size-\(n-1\) mixed bases.

Now impose domination. A one-sided transversal is not dominating: the omitted vertex in the selected bipartition class has no neighbor in \(S\). If both \(|P|,|Q|\ge3\), every omitted vertex has a selected neighbor in the opposite class, and every unselected mate of a selected vertex has another selected vertex in the opposite class. Hence every balanced mixed basis is dominating.

For \(n\ge7\), one can split the \(n-1\) selected indices with
\[
|P|\ge3,\qquad |Q|\ge3,
\]
so
\[
\gamma_{mr}(\operatorname{Cr}_n)=n-1.
\]
For \(4\le n\le6\), such a split is impossible; all size-\(n-1\) mixed bases are one-sided and fail domination. The full class \(A\) is mixed resolving and dominating: selected \(a_i\) has a zero at coordinate \(i\), unselected \(b_i\) has a unique distance \(3\) at coordinate \(i\), and an edge \(a_i b_j\) has a zero at \(i\), a \(2\) at \(j\), and ones elsewhere. Thus
\[
\gamma_{mr}(\operatorname{Cr}_n)=n
\]
for \(4\le n\le6\).

For \(n=3\), the same full-class construction has size \(3\), while every two-vertex candidate fails the size-\(n-1\) mixed-basis classification above. Hence
\[
\gamma_{mr}(\operatorname{Cr}_3)=3.
\]

For \(n\ge7\), choose the omitted index \(h\) in \(n\) ways. Among the remaining \(n-1\) indices, choose the \(A\)-selected indices in any size from \(3\) through \(n-4\); all others are \(B\)-selected. Therefore the number of minimum sets is
\[
n\sum_{p=3}^{n-4}\binom{n-1}{p}
=
n\bigl(2^{n-1}-n^2+n-2\bigr).
\]

## Verification
The included verifier constructs each crown graph directly, computes all-pairs shortest-path distances, and checks the mixed-resolving and domination conditions from their definitions.

For every \(3\le n\le9\), it exhaustively rejects every smaller candidate set and enumerates all minimum mixed resolving dominating sets. For \(n\ge7\), it compares the complete minimum family with the one-omitted-pair balanced-transversal classification and checks the closed count. It also independently verifies for \(4\le n\le6\) that every mixed basis of size \(n-1\) is one-sided and therefore non-dominating.

## Relationship to prior work
The 2024 paper introducing dominant mixed metric dimension proves the general bound
\[
\max\{\gamma(G),\dim_m(G)\}\le \gamma_{mr}(G)\le \min\{\gamma(G)+\dim_m(G),|V(G)|\}
\]
and gives exact values for paths, cycles, stars, wheels, friendship graphs, and complete graphs. Its inspected full text contains no occurrence of crown graphs, bipartite graphs, or matchings.

The crown family is not a specialization of any exact family treated there. The result above also resolves more than the scalar parameter: it classifies every minimum set in the stable regime and isolates a finite transition where imposing domination raises the optimum by one.

## Limitations
The complete minimum-set classification and count are stated for \(n\ge7\). The theorem determines the dominant mixed metric dimension for all \(n\ge3\), but does not enumerate every minimum set in the transition cases \(3\le n\le6\). No claim is made for unbalanced complete bipartite graphs with a matching deleted, or for deleting only a partial matching. The finite computation corroborates the proof but does not replace the all-\(n\) argument.

## References
1. R. Alfarisi, S. K. S. Husain, L. Susilowati, A. I. Kristiana, “Dominant Mixed Metric Dimension of Graph,” Statistics, Optimization & Information Computing 12(6) (2024), 1826–1833, DOI 10.19139/soic-2310-5070-1925. First published online 21 June 2024.
2. A. Kelenc, D. Kuziak, A. Taranenko, I. G. Yero, “Mixed metric dimension of graphs,” Applied Mathematics and Computation 314 (2017), 429–438, DOI 10.1016/j.amc.2017.07.027.
