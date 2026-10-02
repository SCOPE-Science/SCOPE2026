# Outer multiset resolving sets of complete multipartite graphs

## Statement

Let
\[
G=K_{n_1,\ldots,n_r},\qquad r\ge 2,
\]
be a complete multipartite graph, let \(n=\sum_{i=1}^r n_i\), and let
\[
Q=\{n_i:1\le i\le r\}
\]
be the set of distinct part sizes. For \(q\in Q\), write
\[
m_q=\#\{i:n_i=q\},
\qquad d=|Q|.
\]

For \(S\subseteq V(G)\), the following are equivalent.

1. \(S\) is an outer multiset resolving set.
2. Its complement \(U=V(G)\setminus S\) contains at most one vertex from each part, and no two vertices of \(U\) lie in parts of the same size.
3. If
   \[
   B_q=\bigcup_{i:n_i=q}P_i,
   \]
   where \(P_i\) are the multipartite classes, then
   \[
   |U\cap B_q|\le 1
   \quad\text{for every }q\in Q.
   \]

Consequently the complements of the outer multiset resolving sets are exactly the independent sets of the partition matroid whose blocks are \(B_q\), each of capacity one. In particular,
\[
\boxed{\operatorname{odim}(K_{n_1,\ldots,n_r})=n-d.}
\]

The complete size enumerator of outer multiset resolving sets therefore factors as
\[
\boxed{
R_G(z):=\sum_{\substack{S\subseteq V(G)\\S\text{ outer multiset resolving}}}
z^{|S|}
=
z^{\,n-d}\prod_{q\in Q}(z+m_qq).
}
\]
Hence the number of outer multiset bases is
\[
\boxed{\prod_{q\in Q}m_qq,}
\]
and the total number of outer multiset resolving sets is
\[
\boxed{\prod_{q\in Q}(1+m_qq).}
\]
All nonzero roots of \(R_G\) are negative integers, so its coefficient sequence is log-concave and unimodal.

## Proof

Fix \(S\subseteq V(G)\), put \(t=|S|\), and let
\[
s_i=|S\cap P_i|.
\]
If \(x\in P_i\setminus S\), then every landmark in \(P_i\) is at distance \(2\) from \(x\), while every landmark outside \(P_i\) is at distance \(1\). Thus
\[
m_G(x\mid S)=\{\!\{1^{\,t-s_i},\,2^{\,s_i}\}\!\}.
\]
Therefore two vertices outside \(S\) have the same multiset representation exactly when the corresponding values \(s_i\) agree.

If two vertices of \(P_i\) are outside \(S\), they have identical representations, so an outer multiset resolving set omits at most one vertex from each part. When exactly one vertex is omitted from \(P_i\),
\[
s_i=n_i-1.
\]
Thus omitted vertices from two distinct parts \(P_i,P_j\) collide exactly when
\[
n_i-1=n_j-1,
\]
equivalently \(n_i=n_j\). This proves the equivalence of (1), (2), and (3).

The largest possible complement therefore chooses one vertex from one part in each distinct size class, and has size \(d\). Hence
\[
\operatorname{odim}(G)=n-d.
\]

For the enumerator, a size class \(q\) contributes either no omitted vertex, or one omitted vertex chosen from the \(m_q q\) vertices lying in parts of size \(q\). Choices from distinct size classes are independent. Thus the complement-size generating function is
\[
\prod_{q\in Q}(1+m_qq\,y).
\]
Replacing \(y\) by \(z^{-1}\) and multiplying by \(z^n\) gives
\[
R_G(z)
=z^n\prod_{q\in Q}(1+m_qq\,z^{-1})
=z^{n-d}\prod_{q\in Q}(z+m_qq).
\]
The formulas for bases and for the total number of resolving sets follow by taking the lowest-degree coefficient and evaluating at \(z=1\), respectively. The real-rootedness statement is immediate from the factorization.

## Fixed-order extremal consequence

For a connected complete multipartite graph of order \(n\ge2\), let
\[
D(n)=\left\lfloor\frac{\sqrt{8n+1}-1}{2}\right\rfloor.
\]
If there are \(d\) distinct part sizes, then choosing one part of each size gives \(d\) distinct positive integers with total at most \(n\), so
\[
\frac{d(d+1)}2\le n
\]
and therefore \(d\le D(n)\).

Conversely, every \(1\le d\le D(n)\) occurs. For \(d=1\), use \(K_n=K_{1,\ldots,1}\). For \(d\ge2\), use the \(d\) part sizes
\[
1,2,\ldots,d-1,\quad n-\frac{d(d-1)}2,
\]
whose last term is at least \(d\). Therefore the complete set of possible outer multiset dimensions among connected complete multipartite graphs of order \(n\) is
\[
\boxed{\{n-D(n),\,n-D(n)+1,\ldots,n-1\}.}
\]
In particular, the minimum is \(n-D(n)\), attained exactly when the graph has \(D(n)\) distinct part sizes; the maximum is \(n-1\), attained exactly when all parts have one common size.

## Relation to prior results

Gil-Pons, Ramírez-Cruz, Trujillo-Rasua, and Yero introduced the outer multiset dimension and established exact values for several graph families. Klavžar, Kuziak, and Yero subsequently proved that \(\operatorname{odim}(G)=n(G)-1\) exactly for regular graphs of diameter at most two. In the same paper they explicitly noted two complete-multipartite cases:
\[
\operatorname{odim}(K_{r,\ldots,r})=kr-1
\]
for balanced complete \(k\)-partite graphs, and
\[
\operatorname{odim}(K_{r_1,\ldots,r_k})=r_1+\cdots+r_k-k
\]
when \(2\le r_1<\cdots<r_k\). The theorem above unifies these two extremes and determines the arbitrary multiplicity pattern of the part sizes. It additionally characterizes every resolving set, identifies the complement system as a partition matroid, and gives the factored resolving-set enumerator and fixed-order spectrum.

The parameter remains active: Peng recently determined the outer multiset dimension of all toroidal grids, resolving a problem posed in the 2023 work.

## Verification

A standalone definition-level verifier is included in `artifacts/verify_complete_multipartite.py`. It exhaustively checks all 58 connected complete-multipartite isomorphism types of orders \(2\) through \(8\). For every vertex subset it compares the direct distance-multiset definition with the structural criterion above, and then compares the full size distribution with the factored enumerator. It also checks the fixed-order spectrum through order \(20\). The recorded output is in `artifacts/verification.txt`.

The finite verification supports but does not replace the proof.

## Limitations and originality scope

The result is specific to complete multipartite graphs. It does not determine outer multiset dimension for arbitrary diameter-two graphs, joins, or multipartite graphs with missing cross-edges.

Originality is asserted only to the best of our knowledge. The 2023 primary source was inspected at the complete-multipartite passage: it states the balanced case and the strictly increasing-part-size case, but not arbitrary repetitions of part sizes, the characterization of all resolving sets, the partition-matroid interpretation, or the factored enumerator. Targeted searches for complete multipartite outer multiset dimension, outer multiset bases, resolving-set counting, and matroid formulations did not locate an equivalent general result. Recent surveys and papers may be incompletely indexed, and older literature may use different terminology; these remain residual risks.

## References

1. R. Gil-Pons, Y. Ramírez-Cruz, R. Trujillo-Rasua, I. G. Yero, “Distance-based vertex identification in graphs: the outer multiset dimension,” *Applied Mathematics and Computation* 363 (2019), 124612. https://arxiv.org/abs/1902.03017
2. S. Klavžar, D. Kuziak, I. G. Yero, “Further Contributions on the Outer Multiset Dimension of Graphs,” *Results in Mathematics* 78 (2023), 50. https://doi.org/10.1007/s00025-022-01829-8
3. B. Peng, “The Outer Multiset Dimension of Toroidal Grids,” arXiv:2609.20073 (2026). https://arxiv.org/abs/2609.20073
4. H. Pervaiz, R. Simanjuntak, S. W. Saputro, “Outer multiset dimension of joined graphs,” *Indonesian Journal of Combinatorics* 9(2) (2025). https://doi.org/10.19184/ijc.2025.9.2.1
