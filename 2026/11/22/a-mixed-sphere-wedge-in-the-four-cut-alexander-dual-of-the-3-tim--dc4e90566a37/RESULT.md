# A mixed sphere wedge in the four-cut Alexander dual of the \(3\times3\) rook graph

## Finding

Let \(R=K_3\square K_3\) be the graph with vertex set \(\{0,1,2\}^2\), in which distinct vertices are adjacent exactly when they share a coordinate. Let \(\Delta_4(R)\) be the **ordinary** four-cut complex, with facets the complements of four-vertex sets inducing disconnected subgraphs. On all nine vertices take its combinatorial Alexander dual \(L=\Delta_4(R)^\vee\). Then the complete **integral homotopy type** of the dual is
\[
L\simeq\left(\bigvee^{6}S^2\right)\vee S^3.
\]
Consequently, the complete reduced integral homology of the ordinary cut complex is
\[
\widetilde H_i(\Delta_4(R);\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=3,\\
\mathbb Z^6,&i=4,\\
0,&\text{otherwise}.
\end{cases}
\]
The ordinary cut complex is pure of dimension \(4\), but not shellable (or Cohen--Macaulay over any field).

## Assumptions and scope

All complexes are finite abstract simplicial complexes with geometric realizations; reduced groups use integral coefficients. A graph-induced four-set is connected when every pair of its vertices is joined by a path using only the four vertices. The graph \(R\) is also the line graph of \(K_{3,3}\), not the \(3\times3\) *path grid* \(P_3\square P_3\). The result is for the ordinary four-cut complex, not the total four-cut complex, nor the ordinary three-cut complex. The homotopy assertion concerns \(L\); only the stated additive homology, not a wedge decomposition, is asserted for \(\Delta_4(R)\).

Label \((a,b)\) by \(3a+b\in\{0,\ldots,8\}\). The dual has the explicit characterization
\[
L=\{\sigma\subseteq V(R):\text{every four-element subset of }\sigma\text{ induces a connected subgraph of }R\}.
\]
In particular, **every** vertex set of cardinality at most three is a face of \(L\).

## Proof

**1. Establish the exact dual.** The definition of \(\Delta_4(R)\) means that \(V\setminus\sigma\) is one of its faces if and only if some disconnected induced four-set lies inside \(\sigma\). Taking the combinatorial Alexander dual therefore gives the displayed characterization of \(L\). Its three-skeleton is not complete, but its entire two-skeleton is the two-skeleton of the eight-simplex on nine vertices. In particular \(\pi_1(L)=0\).

There are \(\binom94=126\) four-subsets. Induced-connectivity enumeration gives exactly \(81\) connected four-subsets and \(45\) disconnected ones. Enumerating all \(2^9\) subsets against these \(45\) forbidden sets produces the complete face counts by cardinality
\[
(1,9,36,84,81,36,6).
\]
These are respectively the empty face, vertices, edges, triangles, tetrahedra, four-simplices and five-simplices; there are no larger faces. The companion `evidence/verify.py` independently builds the cut complex from its \(45\) facets and checks the Alexander-dual identity for every subset.

**2. Collapse to a three-dimensional complex.** For each currently present nonempty face \(\sigma\), list all its codimension-one cofaces in the remaining complex. Whenever exactly one coface \(\tau\) exists, the pair \((\sigma,\tau)\) is a valid elementary simplicial collapse: any higher coface would supply at least two codimension-one cofaces of \(\sigma\). Choose the available pair minimizing \((-|\tau|,\operatorname{mask}(\sigma))\), where \(\operatorname{mask}(\sigma)=\sum_{v\in\sigma}2^v\), and repeat. Every free-face condition is checked at the time of removal. After exactly \(69\) elementary collapses the remaining complex \(Y\) has face counts by cardinality
\[
(1,9,36,51,18),
\]
and no simplex above dimension \(3\). Thus \(Y\simeq L\) and \(\pi_1(Y)=0\). The deterministic rule and all exhaustive checks are reproduced by the standalone code; the proof does not rely on partial enumeration or random sampling.

**3. Exact integral boundaries.** Orient a simplex by its increasing sequence of vertex indices, with its boundary obtained by deleting the vertex in position \(j\) with coefficient \((-1)^j\). The three nontrivial cellular boundary matrices of \(Y\) have sizes \(9\times36\), \(36\times51\), and \(51\times18\). Integer row and column operations find unit pivots and clear both their rows and columns. The algorithm verifies a *zero* remaining block after precisely \(8\), \(28\), and \(17\) unit pivots respectively. Every operation is unimodular over \(\mathbb Z\), so these are the complete Smith forms, not just rational ranks or tests modulo primes. The nonzero invariant factors of all three differentials are all \(1\). As the chain groups have ranks \(9,36,51,18\), the reduced homology groups of \(Y\), and hence \(L\), are free of ranks \(6\) in degree \(2\) and \(1\) in degree \(3\), with all others zero.

**4. Upgrade from homology to homotopy.** Attaching three-cells does not change fundamental groups, so \(Y^{(2)}\) is simply connected. It has \(51-28=23\) independent integral two-cycles. By the degree-two Hurewicz theorem, \(\pi_2(Y^{(2)})\cong H_2(Y^{(2)};\mathbb Z)\cong\mathbb Z^{23}\); choosing representatives gives a homology equivalence from a wedge of \(23\) two-spheres and hence, by the simply-connected homological Whitehead theorem, a homotopy equivalence. The \(18\) three-cell attaching maps are classified by the integral homomorphism from \(\mathbb Z^{18}\) to \(\mathbb Z^{23}\). The Smith computation above shows that this map has \(17\) unit invariant factors and one zero factor. Changing bases by unimodular transformations therefore cancels \(17\) two-spheres against \(17\) three-cells, while the last three-cell attaches trivially. This proves \(Y\simeq\bigvee^6S^2\vee S^3\).

**5. Return to the ordinary cut complex.** Integral combinatorial Alexander duality on nine vertices gives
\[
\widetilde H_i(\Delta_4(R);\mathbb Z)\cong\widetilde H^{6-i}(L;\mathbb Z).
\]
The universal coefficient theorem and the torsion-free dual homology give exactly the two displayed groups. Since the \(45\) disconnected four-subsets yield facets of cardinality five, \(\Delta_4(R)\) is pure of dimension four. Its nonzero third homology is below the top dimension, which rules out pure shellability and Cohen--Macaulayness over every field.

## Verification

The standalone `evidence/verify.py` requires only Python 3 and its standard library. Run `python3 evidence/verify.py` from the extracted package root. It exhaustively checks the graph-induced connectivity of all four-sets, constructs the dual by forbidden-four-set testing, and independently constructs the original cut complex from its facets. It validates every one of the \(69\) elementary collapses, then performs exact unimodular reduction of all remaining integral boundary matrices and requires every residual entry to vanish. Finally it recomputes the original cut-side simplicial boundary ranks independently over \(\mathbb F_2\), obtaining \((8,28,50,39)\) in degrees one through four. The matching output is in `evidence/verification_output.txt`. This code does not use external databases or numerical tolerances.

## Relationship to prior work

Bayer et al. introduced ordinary cut complexes in arXiv:2304.13675 (first submitted April 26, 2023). Their full paper treats complete multipartite graphs, cycles, squared cycles and clique prisms, but does not classify this graph's four-cut complex. Its sequel arXiv:2407.08158 studies four-cut complexes of *path* grids, which do not have the rook graph's complete rows and columns. A previous rook-graph result (published-finding corpus, October 11, 2026) determines ordinary **three-cut** homology and symmetry for every \(K_m\square K_n\), but not the four-cut case. Another result (published-finding corpus, November 2, 2026) gives additive ordinary four-cut homology for the **four-by-four** rook graph and its Shrikhande mate; it neither covers the nine-vertex case nor gives this mixed homotopy type for its Alexander dual.

These are distinctions of objects, hypotheses, and logical implication, not title matching. Neither the three-cut theorem nor the four-by-four calculation entails this small-board classification, and the two cited foundational papers do not state a general rook four-cut theorem. Absence from the inspected sources does not establish global priority.

## Limitations

The finding is a complete, finite, nine-vertex classification, not a formula for all rectangular rook graphs. It does not determine the integral homotopy type or cohomology ring of the ordinary cut complex itself, and does not claim a symmetry-character decomposition. The explicit collapse is specific to this graph. Equivalent work might exist outside the inspected sources; no independent external validation has been performed.

## References

1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first public April 26, 2023, https://arxiv.org/abs/2304.13675.
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first public July 11, 2024, https://arxiv.org/abs/2407.08158.
3. *Integral and equivariant homology of three-cut complexes of rook graphs*, published-finding corpus record, October 11, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-integral-and-equivariant-homology-of-three-cut-complexes-of-rook--bd50464fc17f.
4. *Integral four-cut homology separates the Shrikhande and rook graphs*, published-finding corpus record, November 2, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-integral-four-cut-homology-separates-the-shrikhande-and-rook-gra--de2f98e55b1f.
