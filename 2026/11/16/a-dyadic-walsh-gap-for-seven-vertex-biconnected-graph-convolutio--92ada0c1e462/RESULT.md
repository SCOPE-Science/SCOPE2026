# A dyadic Walsh gap for seven-vertex biconnected graph convolution

## Finding
Let \(3\le n\le7\), let \(E_n=E(K_n)\), and let \(\mathcal B_n\subseteq\mathbb F_2^{E_n}\) consist of the incidence vectors of all labelled simple **2-vertex-connected** graphs on vertex set \(\{0,\ldots,n-1\}\). For every edge set \(S\subseteq E_n\), define the unnormalized Walsh multiplier
\[
W_n(S)=\sum_{G\in\mathcal B_n}(-1)^{|S\cap G|}.
\]
Then every multiplier is nonzero, and the *sharp* minimum absolute multiplier for vertex orders \(n=3,4,5,6,7\), respectively, is \(1,2,2,8,8\). More precisely,
\[
W_7(S)\equiv 8\pmod {16}\quad\text{and}\quad W_6(S)\equiv8\pmod{16}\qquad\text{for every }S,
\]
while \(W_4(S)\equiv W_5(S)\equiv2\pmod4\), and \(W_3(S)\) is odd. Hence counting convolution by the seven-vertex biconnected-graph indicator on the Boolean edge group is invertible. Its sharp inverse \(\ell^2\)-operator norm is \(1/8\), and its sharp \(\ell^2\)-condition number is \(126861\).

A key strengthening over merely checking nonzero entries is the low-order incidence certificate: the seven-vertex congruence is forced entirely by the counts of biconnected supergraphs of every fixed edge pattern with at most three edges, hence by only nine isomorphism types of small patterns.

## Assumptions and scope
Graphs are labelled, simple, undirected, with all \(n\) vertices present, and are 2-vertex-connected exactly when deleting any single vertex leaves a connected graph. For each \(n\), the edge coordinates are ordered lexicographically \(01,02,\ldots,0(n-1),12,\ldots,(n-2)(n-1)\). Walsh transforms are **unnormalized** and convolution is \((Tf)(x)=\sum_{g\in\mathcal B_n}f(x+g)\). The theorem concerns only the exact finite range \(3\le n\le7\).

## Proof
For \(T\subseteq E_n\), define the forced-edge incidence count
\[
F_n(T)=\#\{G\in\mathcal B_n:T\subseteq G\}.
\]
Expanding the sign character edge by edge gives the exact integer identity, for every \(S\subseteq E_n\),
\[
W_n(S)=\sum_{T\subseteq S}(-2)^{|T|}F_n(T).
\]
Modulo \(16\), terms with \(|T|\ge4\) disappear. The following seven-vertex counts are exhaustive over all isomorphism types of fixed edge sets with at most three edges. The degree signature records the positive degrees of the fixed edge set in increasing order; zero-degree vertices are omitted.

| \(|T|\) | Degree signature | Number of such \(T\) | \(F_7(T)\) |
|---:|:---:|---:|---:|
| 0 | empty | 1 | 1014888 |
| 1 | 11 | 21 | 581464 |
| 2 | 1111 | 105 | 335060 |
| 2 | 112 | 105 | 320432 |
| 3 | 111111 | 105 | 194284 |
| 3 | 11112 | 630 | 185444 |
| 3 | 1113 | 140 | 172568 |
| 3 | 1122 | 420 | 177322 |
| 3 | 222 | 35 | 168096 |

These cover exactly \(1+21+210+1330=1562\) fixed edge patterns. Their counts follow from exact exhaustive graph enumeration: for each of the \(2^{21}\) possible labelled graphs, check connectivity after deleting each vertex; perform a superset zeta transform on the resulting \(0\)-\(1\) indicator, and inspect the 1562 entries with at most three fixed edges. The included `moment_certificate.cpp` implements this directly and checks the nine signatures. A separately implemented articulation-point DFS (`independent_tarjan.cpp`) independently verifies the underlying membership and all Fourier coefficients.

Since \(1014888\equiv8\pmod{16}\), \(581464\equiv0\pmod8\), the two two-edge counts are divisible by \(4\), and all five three-edge counts are even, the expansion proves \(W_7(S)\equiv8\pmod{16}\) for **every** \(S\). Consequently no multiplier vanishes and every absolute magnitude is at least \(8\). A direct signed sum at the lexicographic edge-mask \(S=2396\) equals \(W_7(S)=8\); thus the bound is attained.

For \(n=6\), the same forced-edge argument uses the following counts: \(F_6(\varnothing)=11368\); the unique one-edge count is \(7032\); the two two-edge counts are \(4412,4128\); and the five three-edge counts are \(2812,2620,2328,2454,2252\). These obey the same divisibility conditions, so \(W_6(S)\equiv8\pmod{16}\). At mask \(107\), \(W_6(107)=-8\).

For \(n=4,5\), the total counts are \(10,238\), both congruent to \(2\pmod4\), and the respective one-edge supergraph counts are \(8,164\), both even; thus \(W_n(S)\equiv2\pmod4\) for these two orders. Direct signed sums attain magnitude \(2\) at masks \(3\) and \(21\). For \(n=3\), the only admissible graph is the triangle, so every Walsh multiplier has magnitude \(1\).

Finally, each Walsh character is a unit eigenvector of the counting convolution operator, with eigenvalue \(W_n(S)\). At \(n=7\), the smallest absolute eigenvalue is \(8\), while the largest is \(1014888\), attained at the trivial frequency (and no character can exceed the total graph count by the triangle inequality). Therefore \(\|T^{-1}\|_{\ell^2\to\ell^2}=1/8\) and \(\kappa_2(T)=1014888/8=126861\).

## Verification
Compile and run the two standalone C++17 programs in this package:

```sh
g++ -O3 -std=c++17 moment_certificate.cpp -o moment_certificate
./moment_certificate
g++ -O3 -std=c++17 independent_tarjan.cpp -o independent_tarjan
./independent_tarjan
```

The first uses vertex-deleted reachability, an exact superset zeta transform for \(F_n\), and an in-place Walsh-Hadamard transform. The second uses Tarjan low-link articulation detection and a differently structured recursive Walsh-Hadamard transform, also checking direct signed sums of the sharp witnesses. Both enumerate all graphs for \(3\le n\le7\) and assert the same counts, nonvanishing and minimum multipliers. At \(n=7\), both give \(1014888\) biconnected graphs, zero vanishing multipliers among \(2097152\) frequencies, minimum magnitude \(8\), and Parseval sum \(2128374398976=2097152\cdot1014888\). For \(n=6\), the analogous Parseval sum is \(372506624\).

## Relationship to prior work
The 2007 work of Mestre provides a recursive generation scheme for connected and biconnected graphs, including a biconnected-graph recursion in Section 4.1 and small graph appendices. Kemkes, Sato and Wormald (2010) derive asymptotic counts of sparse labelled two-connected graphs by their order and edge count; these are not the evaluated signed edge-wise Walsh sums. The established labelled counts \(10,238,11368,1014888\) appear in OEIS A013922 and are not claimed as new. The new part is the exact low-order forced-edge divisibility, its all-frequency Fourier nonvanishing consequence through order seven, and the sharp inversion constant at order seven. Searches of relevant public records did not identify an equivalent Fourier claim or a theorem that forces these congruences; this does not establish exhaustive historical priority.

## Limitations
The result is an exact finite theorem only through seven vertices; no extrapolation to larger orders is proved. The forced-edge counts require deterministic finite enumeration, supplied as executable source, rather than a closed combinatorial formula valid for arbitrary orders. No general distribution of all signed Fourier magnitudes is asserted. Historical literature and unindexed data may contain overlapping numerical results, and an independent mathematical audit has not yet been performed.

## References
1. A. Mestre, *Generating connected and biconnected graphs*, arXiv:0710.5711 (first submitted 2007-10-30), https://arxiv.org/abs/0710.5711 . Relevant material: Introduction, Section 4.1, Appendix B.
2. G. Kemkes, C. M. Sato, N. C. Wormald, *Asymptotic enumeration of sparse 2-connected graphs*, arXiv:1010.2516 (first submitted 2010-10-12), https://arxiv.org/abs/1010.2516 . Relevant material: Sections 1–2 and 7.
3. OEIS Foundation, A013922, *Number of labeled connected graphs with n nodes and 0 cutpoints*, https://oeis.org/A013922 . Established count sequence; no Fourier claims attributed.
4. E. M. Wright, *The number of connected sparsely edged graphs. II. Smooth graphs and blocks*, Journal of Graph Theory 2 (1978), 299–305, https://doi.org/10.1002/jgt.3190020403 . Abstract used for historical context; full text not assessed.
