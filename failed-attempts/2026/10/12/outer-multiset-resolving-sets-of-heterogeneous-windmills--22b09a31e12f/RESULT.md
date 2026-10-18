# Outer multiset resolving sets of heterogeneous windmills
## Finding
Let
\[
G=K_1\vee(K_{k_1}\cup\cdots\cup K_{k_r}),
\qquad r\ge2,\qquad k_i\ge2.
\]
Write \(c\) for the universal center and \(C_i\) for the peripheral clique of order \(k_i\).

A set \(S\subseteq V(G)\) is outer multiset resolving if and only if it omits at most one vertex from each \(C_i\), and any two cliques from which a vertex is omitted have different orders. The center may be selected or omitted independently.

Let
\[
Q=\{k_i:1\le i\le r\},\qquad
m_q=|\{i:k_i=q\}|,\qquad
K=\sum_{i=1}^r k_i,\qquad
d=|Q|.
\]
Then
\[
\operatorname{dim}_{\mathrm{ms}}(G)=K-d=|V(G)|-(d+1).
\]

The complete cardinality enumerator is
\[
\mathcal O_G(z)
=
(1+z)\prod_{q\in Q}\left(z^{qm_q}+m_q q\,z^{qm_q-1}\right)
=
(1+z)z^{K-d}\prod_{q\in Q}(z+m_q q).
\]

Every minimum set omits the center and, for each distinct clique order \(q\), omits exactly one peripheral vertex from exactly one clique of order \(q\). Hence the number of outer multiset bases is
\[
\prod_{q\in Q}m_q q.
\]

For the uniform generalized windmill \(K_1\vee rK_k\), this specializes to the published scalar value
\[
\operatorname{dim}_{\mathrm{ms}}(K_1\vee rK_k)=rk-1.
\]

## Assumptions and scope
All graphs are finite, simple, connected, and undirected. For \(S\subseteq V(G)\), the multiset representation of a vertex \(v\notin S\) is the multiset of distances from \(v\) to the vertices of \(S\). A set is outer multiset resolving when distinct vertices outside it have distinct multiset representations.

Every peripheral clique has order at least \(2\).

## Proof
Vertices within one peripheral clique are true twins, so an outer multiset resolving set can omit at most one vertex from each clique.

Assume \(x_i\in C_i\setminus S\) is the unique omitted vertex of \(C_i\), and put
\[
\varepsilon=
\begin{cases}
1,&c\in S,\\
0,&c\notin S.
\end{cases}
\]
The selected vertices in \(C_i\) and, when applicable, the center are at distance \(1\) from \(x_i\); selected vertices in all other peripheral cliques are at distance \(2\). Thus
\[
m(x_i\mid S)
=
\{\!\{1^{\,k_i-1+\varepsilon},
2^{\,|S|-k_i+1-\varepsilon}\}\!\}.
\tag{1}
\]
Hence two omitted peripheral vertices have the same representation if and only if their clique orders are equal.

If the center is omitted, its representation consists only of distance \(1\). Every omitted peripheral vertex has at least one selected vertex at distance \(2\) in another peripheral clique, because there are at least two cliques, each of order at least \(2\), and at most one vertex can be omitted from any clique. Therefore an omitted center never collides with an omitted peripheral vertex.

This proves the classification.

For a fixed clique order \(q\) occurring \(m_q\) times, either all \(qm_q\) vertices are selected, or exactly one peripheral vertex is omitted from exactly one of those cliques. These choices contribute
\[
z^{qm_q}+m_q q\,z^{qm_q-1}.
\]
Different clique-order classes are independent, and the center contributes the factor \(1+z\). Multiplication gives the enumerator. The smallest exponent is obtained by omitting the center and one peripheral vertex for each distinct clique order, proving the dimension and basis-count formulas.

## Verification
The included checker constructs every heterogeneous windmill with total peripheral order between \(4\) and \(10\), at least two peripheral cliques, and every clique order at least \(2\). It computes all-pairs distances, enumerates every vertex subset, tests the outer multiset condition directly, and compares the result with the structural criterion, every coefficient of the product formula, the dimension, and the minimum-basis count.

## Relationship to prior work
Outer multiset dimension was introduced in 2019. A 2025 paper on joined graphs determines exact scalar values for several join families. For the uniform generalized windmill \(K_1\vee rK_k\), its Theorem 2.3 proves the scalar value \(rk-1\).

That theorem assumes all peripheral cliques have the same order. The present result extends it to arbitrary peripheral clique orders and strengthens the scalar conclusion to a complete all-set classification, a factored enumerator, and an exact minimum-basis count.

Targeted searches using heterogeneous windmill, clique bouquet, block graph, unequal clique sizes, and join-of-cliques terminology did not locate an equivalent variable-size theorem.

## Limitations
Singleton peripheral cliques are excluded; they create an additional center-versus-peripheral boundary.

The uniform scalar windmill value is prior work and is not claimed as new. The finite exhaustive verification is corroborative only; the arbitrary-parameter theorem follows from the exact representation formula.

A differently phrased or non-indexed variable-size clique-bouquet result may exist.

## References
1. R. Gil-Pons, Y. Ramírez-Cruz, R. Trujillo-Rasua, I. G. Yero, “Distance-based vertex identification in graphs: the outer multiset dimension,” arXiv:1902.03017v1, 8 February 2019; Applied Mathematics and Computation 363 (2019), 124612, DOI 10.1016/j.amc.2019.124612.
2. H. Pervaiz, R. Simanjuntak, S. W. Saputro, “Outer Multiset Dimension of Joined Graphs,” Indonesian Journal of Combinatorics 9 (2025), 61–68, DOI 10.19184/ijc.2025.9.2.1.
