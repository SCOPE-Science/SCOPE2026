# Connected mutual visibility in triangular and rook graphs

## Statement

Let \(\mu(G)\) denote the ordinary mutual-visibility number, \(\mu_c(G)\) the connected mutual-visibility number, and \(\mu^-(G)\) the minimum cardinality of an inclusion-maximal ordinary mutual-visibility set.

### Theorem A: triangular graphs
For every \(n\ge 4\), every inclusion-maximal mutual-visibility set of the line graph \(L(K_n)\) induces a connected subgraph. Consequently,
\[
\mu_c(L(K_n))=\mu(L(K_n))=\operatorname{ex}(n,K_4)=\left\lfloor\frac{n^2}{3}\right\rfloor.
\]
Moreover,
\[
\mu^-(L(K_n))=\operatorname{sat}(n,K_4)=2n-3.
\]

### Theorem B: rook graphs
For every \(m,n\ge 2\), every inclusion-maximal mutual-visibility set of
\[
L(K_{m,n})\cong K_m\square K_n
\]
induces a connected subgraph. Consequently,
\[
\mu_c(K_m\square K_n)=\mu(K_m\square K_n)=z(m,n;2,2),
\]
where \(z(m,n;2,2)\) is the Zarankiewicz number, equivalently the largest number of edges in a \(C_4\)-free subgraph of \(K_{m,n}\).

Thus imposing connectedness costs nothing not only for a maximum mutual-visibility set in these two families: every inclusion-maximal ordinary mutual-visibility set is already connected.

For a prime power \(q\), putting \(N=q^2+q+1\) and using the classical projective-plane value gives
\[
\mu_c(K_N\square K_N)=(q+1)N.
\]
In particular, for balanced rook graphs,
\[
\mu_c(K_n\square K_n)=(1+o(1))n^{3/2}.
\]

## Context

Connected mutual visibility was introduced by Tonny K B and Shikhi M in September 2026. A connected mutual-visibility set is an ordinary mutual-visibility set whose induced subgraph is connected. Their first paper develops general bounds and exact results for geodetic graphs, joins, block graphs, cactus graphs, and several diameter-two families, but its current version does not treat line graphs, Cartesian products of complete graphs, or Zarankiewicz reductions.

Two older ordinary-mutual-visibility results are the starting point here. Cicerone, Di Stefano and Klavžar showed that a set of vertices in \(K_m\square K_n\) is mutual-visible exactly when the corresponding edge set of \(K_{m,n}\) is \(C_4\)-free. Cicerone, Di Stefano, Klavžar and Yero later showed that, for \(L(K_n)\), the corresponding edge set of \(K_n\) must be \(K_4\)-free. These translations determine the ordinary maxima by the Zarankiewicz and Turán problems, respectively.

The new observation is that maximality in either forbidden-subgraph model automatically supplies the connectivity required by \(\mu_c\).

## Proof

### 1. A saturation-connectivity observation
Suppose \(H\) is an inclusion-maximal \(K_4\)-free spanning subgraph of \(K_n\). If \(H\) were disconnected, choose vertices \(u,v\) in distinct components. The host edge \(uv\) is missing. Maximality says that adding \(uv\) creates a copy of \(K_4\) containing \(uv\). But within that \(K_4\), after deleting \(uv\), there remains a \(u\)-\(v\) path using old edges of \(H\), contradicting that \(u,v\) were in different components. Hence every \(K_4\)-saturated subgraph of \(K_n\) is connected.

For the bipartite version, let \(H\) be an inclusion-maximal \(C_4\)-free subgraph of \(K_{m,n}\), with \(m,n\ge2\). First, \(H\) has no isolated vertex: adding any host edge incident with an isolated vertex cannot create a \(C_4\), since that vertex would have only one incident edge after the addition. If \(H\) were disconnected, every component would therefore meet both bipartition classes. Choose vertices \(u,v\) in different components and opposite classes. The host edge \(uv\) is missing. Adding it cannot create a \(C_4\), because a new \(C_4\) containing \(uv\) would contain an old three-edge \(u\)-\(v\) path, again joining two components. This contradicts maximality. Thus every \(C_4\)-saturated spanning subgraph of \(K_{m,n}\) is connected.

This is the only additional graph-theoretic ingredient needed.

### 2. Triangular graphs
Identify the vertices of \(L(K_n)\) with the edges of \(K_n\). For \(F\subseteq E(K_n)\), write \(S_F\) for the corresponding vertex subset of \(L(K_n)\). The 2024 diameter-two analysis proves
\[
S_F\text{ is a mutual-visibility set of }L(K_n)
\quad\Longleftrightarrow\quad
(K_n)_F\text{ is }K_4\text{-free}.
\]
Therefore \(S_F\) is inclusion-maximal mutual-visible exactly when \((K_n)_F\) is \(K_4\)-saturated. By the observation above, \((K_n)_F\) is connected. Its line graph is exactly the induced graph \(L(K_n)[S_F]\), so \(S_F\) is a connected mutual-visibility set.

In particular a maximum ordinary mutual-visibility set is connected, whence
\[
\mu_c(L(K_n))=\mu(L(K_n)).
\]
The same forbidden-subgraph translation gives \(\mu(L(K_n))=\operatorname{ex}(n,K_4)\), and Turán's theorem yields
\[
\operatorname{ex}(n,K_4)=e(T_3(n))=\left\lfloor\frac{n^2}{3}\right\rfloor.
\]
Likewise, the smallest maximal mutual-visibility set corresponds exactly to the smallest \(K_4\)-saturated graph. The Erdős--Hajnal--Moon saturation theorem gives
\[
\operatorname{sat}(n,K_4)=2n-3,
\]
which proves the lower-mutual-visibility formula.

### 3. Rook graphs
Use the standard isomorphism \(L(K_{m,n})\cong K_m\square K_n\). A vertex set of the rook graph corresponds to an edge set \(F\subseteq E(K_{m,n})\). The Cartesian-product mutual-visibility criterion says
\[
S_F\text{ is mutual-visible}
\quad\Longleftrightarrow\quad
(K_{m,n})_F\text{ is }C_4\text{-free}.
\]
Thus an inclusion-maximal mutual-visibility set corresponds to a \(C_4\)-saturated bipartite graph, which is connected by the saturation-connectivity argument. Again the induced graph on \(S_F\) is the line graph of this selected-edge graph, hence is connected. Therefore every maximal ordinary mutual-visibility set is connected, and in particular
\[
\mu_c(K_m\square K_n)=\mu(K_m\square K_n)=z(m,n;2,2).
\]

The previously known lower-mutual-visibility identity
\[
\mu^-(K_m\square K_n)=m+n-1
\]
is consistent with the same picture: it is the minimum size of a saturated \(C_4\)-free bipartite edge set. It is prior work and is not claimed here as new.

## Verification

The standalone verifier in `artifacts/verify.py` works directly with the line-graph visibility condition rather than inserting the displayed closed forms. It exhaustively enumerates all selected edge sets for \(L(K_n)\), \(3\le n\le6\), and for rook graphs with parameters
\[
(2,2),(2,3),(2,4),(3,3),(3,4),(4,4).
\]
For each family it checks ordinary mutual visibility from shortest-path intermediates, identifies inclusion-maximal sets by one-vertex extensions, tests connectivity of the induced line graph, and computes both ordinary and connected maxima. No disconnected maximal mutual-visibility set occurs in the tested range. For \(L(K_n)\), the computed maximum also agrees with \(\lfloor n^2/3\rfloor\).

The finite computation is supporting evidence only; the theorems above are proved symbolically.

## Originality and limitations

To the best of our knowledge, the connected-mutual-visibility conclusions above are new. The connected parameter was introduced only in September 2026, and the current source paper does not contain `line graph`, `Cartesian`, or `Zarankiewicz` in its accessible full-text rendering. Searches for connected mutual visibility combined with line graphs, rook/Hamming graphs, Cartesian products of complete graphs, \(K_4\)-free graphs, \(C_4\)-free graphs, Turán, and Zarankiewicz found no prior statement of these formulas or of the stronger fact that every maximal ordinary mutual-visibility set is connected.

The forbidden-subgraph correspondences for ordinary mutual visibility, Turán's theorem, the Erdős--Hajnal--Moon saturation theorem, the Bollobás--Wessel result for the lower rook-graph parameter, and the classical Zarankiewicz/projective-plane estimates are prior work and are not claimed as new. The proof here is deliberately elementary once those correspondences are available.

The rook-graph formula inherits the classical difficulty of the Zarankiewicz problem: it is an exact reduction, not a general closed form for \(z(m,n;2,2)\). Because connected mutual visibility is extremely recent, unindexed parallel work or a subsequent revision of the September 2026 preprint remains the main residual originality risk. No specific inaccessible source was found whose known statement materially suggests prior coverage.

## References

1. Tonny K B and Shikhi M, *Connected Mutual-Visibility in Graphs*, arXiv:2609.18877 (2026). https://arxiv.org/abs/2609.18877
2. S. Cicerone, G. Di Stefano, S. Klavžar, *On the mutual-visibility in Cartesian products and in triangle-free graphs*, Applied Mathematics and Computation 438 (2023), 127619. https://doi.org/10.1016/j.amc.2022.127619
3. S. Cicerone, G. Di Stefano, S. Klavžar, I. G. Yero, *Mutual-visibility problems on graphs of diameter two*, European Journal of Combinatorics 120 (2024), 103995. https://doi.org/10.1016/j.ejc.2024.103995
4. B. Brešar, I. G. Yero, *Lower (total) mutual-visibility number in graphs*, Applied Mathematics and Computation 465 (2024), 128411. https://doi.org/10.1016/j.amc.2023.128411
5. P. Erdős, A. Hajnal, J. W. Moon, *A problem in graph theory*, American Mathematical Monthly 71 (1964), 1107--1110.
6. J. Tan, *An attack on Zarankiewicz's problem through SAT solving*, arXiv:2203.02283 (2022). https://arxiv.org/abs/2203.02283
