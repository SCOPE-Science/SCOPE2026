# Cospectral quartic-line candidates with unequal four-color decompositions

## Finding

Let \(G_L\) be the following twenty-vertex simple graph associated to an order-four Latin square \(L\). Its sixteen grid vertices are \((i,j)\), with \(0\leq i,j<4\); two different grid vertices are adjacent exactly when they share a row or column. There are also four mutually nonadjacent vertices \(u_s\), with \(0\leq s<4\), and \(u_s\) is joined to \((i,j)\) exactly when \(L(i,j)=s\). Put
\[
L_{\mathrm{cyc}}(i,j)=i+j\pmod 4,\qquad
L_{\mathrm{Klein}}(i,j)=i\mathbin{\mathrm{xor}}j,
\]
with the second operation the addition law of \((\mathbb Z/2\mathbb Z)^2\) after the usual binary encoding.

The two graph isomorphism types of the twenty-line lattice-admissible dual configurations in Degtyarev--Rams, Theorem 3.20 and Remark 3.21, are represented by \(G_{\mathrm{cyc}}\) and \(G_{\mathrm{Klein}}\). Both have \(64\) edges and the **same adjacency characteristic polynomial**
\[
\det(zI-A)=(z-2)^6(z+2)^6(z^2-6z-4)(z^2+2z-4)^3.
\]
They nevertheless have **different counts of proper four-colorings** on a fixed, labeled four-color palette:
\[
P_{G_{\mathrm{cyc}}}(4)=5400,\qquad
P_{G_{\mathrm{Klein}}}(4)=8568.
\]
As the action permuting four colors is free, the corresponding numbers of partitions into four unlabeled nonempty independent sets are **\(225\)** and **\(357\)**. Thus the two possible dual configurations are provably nonisomorphic, while no adjacency spectral statistic can distinguish them.

The weighted geometric intersection matrices \(Q\), having diagonal entries \(-2\) at grid vertices and \(-1\) at the four extra vertices and off-diagonal entries prescribed by adjacency on the minimal resolution, also have the common polynomial
\[
\det(zI-Q)=z^9(z+4)^6(z+5)^3(z^2-3z-8).
\]
Their common rank is \(11\), with one positive, ten negative, and nine zero eigenvalues.

## Assumptions and scope

All graphs are finite simple undirected graphs, and proper colorings assign distinct colors to adjacent vertices. The geometric object is the **dual graph on the minimal resolution**, not the ordinary intersection graph of lines in the singular quartic. According to Convention 2.12 of the cited primary paper, the four lines through its distinguished singular point are pairwise disjoint on that resolution. The sixteen remaining lines correspond to the unique generalized quadrangle \(\mathrm{GQ}(3,1)\), whose point graph is the \(4\)-by-\(4\) rook graph. The cited work gives exactly two abstract twenty-line dual-graph types. It does **not** establish that both types occur on actual quartics. The theorem here concerns those two abstract, lattice-admissible types; it makes no new existence assertion.

## Proof

**Reduction to Latin squares.** Each extra vertex in the twenty-line graph is adjacent to a maximal independent set of four rook-graph vertices, and these four independent sets partition the sixteen grid vertices (Degtyarev--Rams, Theorem 3.20 and Remark 3.21). An independent set of size four in the \(4\)-by-\(4\) rook graph contains one vertex in every row and every column. Assigning one symbol to each part therefore produces an order-four Latin square \(L\), giving the displayed construction. The cyclic and Klein tables both give valid partitions. Their different four-coloring counts below prove that their graphs are nonisomorphic. Since the primary paper establishes exactly two possible isomorphism types, the displayed graphs represent both.

**Spectral calculation.** In grid/symbol block order,
\[
A=\begin{pmatrix}R&B\\ B^{\mathsf T}&0\end{pmatrix},
\]
where \(R\) is the \(4\)-by-\(4\) rook adjacency matrix and \(B_{(i,j),s}=1\) precisely when \(L(i,j)=s\). The Latin property gives
\[
B^{\mathsf T}B=4I_4,\qquad RB=2(J_{16,4}-B).
\]
The spectrum of \(R\) is \(6\) once, \(2\) six times, and \(-2\) nine times. On the two constant directions, the block matrix of \(A\), in the unnormalized constant-vector basis, is \(\left(\begin{smallmatrix}6&1\\4&0\end{smallmatrix}\right)\); its characteristic polynomial is \(z^2-6z-4\). For each of the three independent symbol-zero directions, orthonormalizing the corresponding column of \(B\) produces \(\left(\begin{smallmatrix}-2&2\\2&0\end{smallmatrix}\right)\), with polynomial \(z^2+2z-4\). The remaining rook modes have eigenvalue \(2\) with multiplicity six and \(-2\) with multiplicity six. This yields the common adjacency polynomial.

For the geometric Gram matrix \(Q=A-\operatorname{diag}(2I_{16},I_4)\), the same invariant decomposition gives the constant block \(\left(\begin{smallmatrix}4&1\\4&-1\end{smallmatrix}\right)\), the three symbol-zero blocks \(\left(\begin{smallmatrix}-4&2\\2&-1\end{smallmatrix}\right)\), and remaining eigenvalues \(0\) six times and \(-4\) six times. Hence its polynomial is \(z^9(z+4)^6(z+5)^3(z^2-3z-8)\), and its inertia is \((1,10,9)\). These conclusions do not depend on which Latin square is chosen.

**Exact four-color counts.** Restrict a proper four-coloring to the grid. Every grid row and column is a \(K_4\), so this restriction is itself an order-four Latin square \(C\), on the four labeled colors. Conversely, every such \(C\) properly colors the grid. For each symbol \(s\) of the original table \(L\), let \(m_s(C)\) be the number of distinct colors of \(C\) on the four cells satisfying \(L(i,j)=s\). The symbol vertices are mutually nonadjacent, so the exact number of extensions of \(C\) is
\[
\prod_{s=0}^{3}(4-m_s(C)).
\]
Thus the complete four-coloring count is the sum of this product over all order-four Latin squares \(C\). These are exhaustively obtained by choosing four permutations as rows and retaining only choices with all four columns permutations. This considers every possibility exactly once, and yields \(576\) tables. The complete certificate is:

| Sorted multiset of the four \(m_s(C)\) | Cyclic base: number of \(C\) | Klein base: number of \(C\) |
|---|---:|---:|
| \((1,1,1,1)\) | 24 | 24 |
| \((1,1,2,2)\) | 48 | 144 |
| \((1,2,3,3)\) | 192 | 0 |
| \((2,2,2,2)\) | 24 | 72 |
| \((2,2,4,4)\) | 96 | 0 |
| \((3,3,3,3)\) | 192 | 288 |
| \((4,4,4,4)\) | 0 | 48 |
| **Total** | **576** | **576** |

Multiplying each row count by \(\prod_s(4-m_s)\) gives \(5400\) for the cyclic table and \(8568\) for the Klein table. Every proper coloring uses all four colors because a row is a clique of size four. Color permutation therefore acts freely, giving \(5400/24=225\) and \(8568/24=357\) unlabeled partitions. The exact executable enumeration and an independently structured direct graph-coloring backtrack appear in `CHECK.py`.

## Verification

`CHECK.py` is self-contained Python 3 code using only the standard library. It constructs both twenty-vertex graphs from their exact definitions, checks all degrees and \(64\) edges, calculates both characteristic polynomials with integer traces and Newton identities, enumerates the full \(24^4\) row-permutation search space for all \(576\) Latin squares, checks every row of the certificate table, and separately enumerates proper graph colorings by a direct twenty-vertex backtrack. Both methods return exactly \(5400\) and \(8568\). The full run prints `ALL EXACT CHECKS PASSED`.

## Relationship to prior work

Degtyarev and Rams, *On large configurations of lines on quartic surfaces* (first publicly released June 28, 2025), establish the twenty-line bound and the generalized-quadrangle-plus-four-line geometry, including exactly two admissible abstract dual graphs. They do not state the shared adjacency or geometric Gram polynomials, or count the two graphs' four-color decompositions. Their unresolved question of geometric realizability of both abstract candidates is preserved here.

Besharati, Goddyn, Mahmoodian and Mortezaeefar, *On the chromatic number of Latin square graphs* (2016), study the **different** sixteen-vertex graph in which cells are also adjacent when they have the same Latin symbol. Their chromatic-number statements do not imply four-coloring counts of the present twenty-vertex augmented rook graphs, whose four symbol vertices are independent and separate from the cells. The standard theory of rook-graph spectra gives the spectrum of the sixteen-vertex subgraph but not immediately the twenty-vertex weighted intersection or four-coloring census.

## Limitations

The theorem gives graph and intersection-matrix invariants for two **lattice-admissible candidates**, not a classification of realizable quartic surfaces or a proof that both types actually occur. The original paper explicitly leaves the possible realization of both candidates open. The intersection-matrix signature is a statement about the proposed line classes and does not determine the full Néron--Severi lattice, its discriminant group, or embedding primitivity. Exact counts rely on a finite **exhaustive**, reproducible enumeration, not extrapolation from samples. Published or unindexed equivalent computations may exist; no claim of independently certified publication priority is made.

## References

1. A. Degtyarev and S. Rams, *On large configurations of lines on quartic surfaces*, arXiv:2506.22733v1 (first public submission 2025-06-28), especially Convention 2.12, Theorem 3.20, and Remark 3.21. https://arxiv.org/html/2506.22733v1
2. N. Besharati, L. Goddyn, E. S. Mahmoodian, and M. Mortezaeefar, *On the chromatic number of Latin square graphs*, arXiv:1510.02521v2; Discrete Mathematics 339 (2016), 2613--2619. https://arxiv.org/abs/1510.02521
3. V. González-Alonso and S. Rams, *Counting lines on quartic surfaces*, Taiwanese Journal of Mathematics 20 (2016), 769--785; arXiv:1505.02018. https://arxiv.org/abs/1505.02018
