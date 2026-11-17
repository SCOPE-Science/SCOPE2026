# Integral homology and full dihedral character of the Herschel three-cut complex

## Finding
Let \(H\) be the canonical eleven-vertex, eighteen-edge Herschel graph, with the labeling and adjacency specified below. Let \(\Delta=\Delta_3(H)\) be its **ordinary** three-cut complex: every facet is the complement of a three-vertex subset inducing a disconnected subgraph. Then \(\Delta\) is pure of dimension seven, and its *complete reduced integral homology* is
\[
\widetilde H_i(\Delta;\mathbb Z)\cong
\begin{cases}\mathbb Z,&i=6,\\\mathbb Z^{13},&i=7,\\0,&\text{otherwise}.
\end{cases}
\]
In particular, \(\Delta\) is not shellable.

The full automorphism group \(G=\operatorname{Aut}(H)\cong S_3\times C_2\cong D_6\) acts on both rational homology groups. The complete rational character table, organized by the cycle type of each automorphism on the original eleven vertices, is

| Vertex cycle type | Number of elements | \(\operatorname{tr}(g\mid\widetilde H_6)\) | \(\operatorname{tr}(g\mid\widetilde H_7)\) |
|---|---:|---:|---:|
| \(1^{11}\) | 1 | 1 | 13 |
| \(1^5 2^3\) | 3 | 1 | -5 |
| \(1^3 2^4\) | 1 | -1 | -1 |
| \(1^1 2^5\) | 3 | -1 | 1 |
| \(1^2 3^3\) | 2 | 1 | 1 |
| \(2^1 3^1 6^1\) | 2 | -1 | -1 |

Let \(\varepsilon\) denote the nontrivial one-dimensional character of \(C_2\), let \(\operatorname{sgn}\) denote the sign character of \(S_3\), and let \(V\) be its standard two-dimensional rational representation. The character table equivalently gives
\[
\widetilde H_6(\Delta;\mathbb Q)\cong \mathbf1\boxtimes\varepsilon,
\]
\[
\widetilde H_7(\Delta;\mathbb Q)\cong
(2\operatorname{sgn}\oplus2V)\boxtimes\mathbf1 \oplus
(3\operatorname{sgn}\oplus2V)\boxtimes\varepsilon.
\]
Consequently both invariant spaces vanish:
\[
\widetilde H_6(\Delta;\mathbb Q)^G=
\widetilde H_7(\Delta;\mathbb Q)^G=0.
\]
These are homology and representation claims; no homotopy decomposition or equivariant homotopy equivalence is asserted.

## Assumptions and scope
Use vertices \(\{0,1,\dots,10\}\) and the eighteen undirected edges specified by the following upper-triangular adjacency dictionary. Each listed neighbor is larger than its key.

```
0: 1 3 4
1: 2 5 6
2: 3 7
3: 8 9
4: 5 9
5: 10
6: 7 10
7: 8
8: 10
9: 10
```

The graph is bipartite with three vertices of degree four, namely \(\{1,3,10\}\), and eight of degree three. This is the standard Herschel graph up to graph isomorphism, and all computations here use the explicit labeling above. For an oriented simplex we adopt increasing vertex order; deleting its \(j\)-th vertex gives coefficient \((-1)^j\). Homology uses ordinary simplicial integer chains and reduced homology, with cohomology over \(\mathbb Z\) where indicated.

## Proof
**1. Construct the dual.** Let \(K=\Delta^\vee\) be the combinatorial Alexander dual on the same eleven vertices. A set \(S\) is a face of \(K\) precisely when every three-subset of \(S\) induces a connected graph. Thus all vertices and edges belong to \(K\), and because \(H\) is triangle-free its triangles are exactly the 42 induced two-edge paths (counted as \(\sum_v\binom{\deg_H(v)}2=3\binom42+8\binom32=42\)). A four-vertex face is exactly a four-cycle: every triple must contain two edges, forcing four edges on the four vertices. The explicit adjacency yields precisely nine such squares:

```
0 1 2 3     0 1 4 5     1 2 6 7
2 3 7 8     0 3 4 9     1 5 6 10
6 7 8 10    4 5 9 10    3 8 9 10
```

Every edge of \(H\) appears in exactly two squares, so these squares are **not edge-disjoint**. No five-vertex set belongs to \(K\): among ten triples on five vertices each would need at least two edges, while each graph edge lies in three of these triples, forcing at least seven edges, contrary to the six-edge bound for triangle-free graphs on five vertices. Hence
\[
(f_0(K),f_1(K),f_2(K),f_3(K))=(11,55,42,9)
\]
and these are all its nonempty faces.

**2. Integral boundary groups.** Build the signed chain matrices \(\partial_1\) (\(11\times55\)), \(\partial_2\) (\(55\times42\)), and \(\partial_3\) (\(42\times9\)). The attached standalone Python verifier reconstructs all these matrices from the displayed graph. Using **integer row and column operations of determinant \(\pm1\)**, it reduces the three matrices individually to a unit block and a zero residual block, of respective sizes \(10\), \(32\), \(9\). These are complete integer rank and saturation certificates: every nonzero Smith invariant is a unit. Since consecutive boundaries compose to zero, the resulting free reduced integral homology of \(K\) is
\[
\widetilde H_1(K;\mathbb Z)\cong\mathbb Z^{55-10-32}=\mathbb Z^{13},
\qquad H_2(K;\mathbb Z)\cong\mathbb Z^{42-32-9}=\mathbb Z.
\]
All other reduced groups vanish; neither degree has torsion. The Smith-unit condition ensures that each boundary subgroup is primitive in the relevant free chain lattice, so the indicated homology quotients have no hidden torsion. Integer combinatorial Alexander duality, with \(n=11\), gives
\[
\widetilde H_i(\Delta;\mathbb Z)\cong\widetilde H^{8-i}(K;\mathbb Z),
\]
which proves the displayed integral homology. The 123 disconnected triples give 123 distinct seven-dimensional facets of \(\Delta\), making it pure. As \(\widetilde H_6(\Delta;\mathbb Z)\ne0\) below its top dimension seven, this pure complex cannot be shellable.

**3. Determine all automorphisms.** Every automorphism permutes the degree-four vertices \(A=\{1,3,10\}\). The vertices \(Z=\{4,7\}\) are distinguished among degree-three vertices by having no degree-four neighbor, hence \(Z\) is preserved setwise. The other six vertices are uniquely determined by their **pair** of degree-four neighbors and their unique neighbor in \(Z\). Conversely, any permutation of \(A\) and any permutation of \(Z\) extend uniquely to an adjacency-preserving permutation of all eleven vertices. Therefore \(\operatorname{Aut}(H)\cong S_3\times C_2\), with exactly twelve automorphisms. The six rows of the table are its six conjugacy classes, classified by their distinct vertex-cycle types.

**4. Recover the dual action exactly.** An explicit integral two-cycle in \(K\), written as an oriented sum of triangles, is

```
+012 +023 -015 +045 -127 +167 -238 +278 -678
+039 -049 +1,5,10 -4,5,10 -1,6,10 +3,8,10
-6,8,10 -3,9,10 +4,9,10
```

Here `+012` abbreviates the oriented triangle with vertices \((0,1,2)\), and commas separate the vertices of two-digit labels. Its signed boundary is exactly zero in \(C_1(K;\mathbb Z)\). Its class is nonzero modulo three, because adjoining this cycle to the nine columns of \(\partial_3\) increases the rank over \(\mathbb F_3\) from nine to ten. Since \(H_2(K;\mathbb Q)\) is one-dimensional, each of the twelve automorphisms acts on it by \(+1\) or \(-1\), and the sign can be determined by whether the transformed cycle differs from the original or its negative by a boundary modulo three. The verifier tests this for all twelve automorphisms and finds exactly one valid sign each time.

For each automorphism \(g\), let \(t_j(g)\) be the signed trace of its permutation action on oriented \(j\)-faces of \(K\). The reduced Lefschetz formula gives
\[
\chi_{H_1(K)}(g)=\chi_{H_2(K)}(g)-\left(\sum_{j=0}^{3}(-1)^j t_j(g)-1\right).
\]
Finally, the equivariant combinatorial Alexander duality isomorphism includes the orientation character \(\epsilon_{11}(g)\), the sign of the permutation of all eleven vertices. Hence
\[
\chi_{\widetilde H_6(\Delta)}(g)=\epsilon_{11}(g)\chi_{H_2(K)}(g),\qquad
\chi_{\widetilde H_7(\Delta)}(g)=\epsilon_{11}(g)\chi_{H_1(K)}(g).
\]
The enumerated signed traces produce the six table rows exactly. Their averages over the twelve group elements both equal zero, proving the invariant-space claims. The displayed irreducible decompositions follow by taking character inner products with the four one-dimensional and two two-dimensional rational irreducibles of \(S_3\times C_2\).

## Verification
Run `python3 verify_herschel.py` in a Python 3 environment using only the standard library. It independently constructs both simplicial complexes from the supplied graph, enumerates every vertex subset, replays three integer elimination certificates with only unit pivots, checks the explicit integral two-cycle and its nonzero mod-three class, generates all twelve graph automorphisms from graph-theoretic signatures, computes the six rational character rows, independently confirms all seven mod-two boundary ranks directly on the original complex, and independently computes all twelve reduced signed Lefschetz traces on the **original cut complex** to check the character difference. The observed face vector of \(\Delta\) is \((11,55,165,330,462,462,321,123)\), totaling 1929 nonempty faces. The expected terminal output is `VERIFY_OK`; the captured output is included.

These are exhaustive finite calculations on the one specified graph, not sampling. They establish the stated exact integral ranks and group characters. A general homotopy type of \(\Delta\) and arbitrary graph families are not inferred.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced ordinary cut complexes and analyzed several graph families, including group actions, in *Topology of Cut Complexes of Graphs* (first public 2023-04-26). Their sequel (first public 2024-07-11) treats squared paths, grid graphs, disjoint unions and selected representations. Their inspected statements do not determine the integral and full equivariant homology for the present Herschel graph.

Two related general published calculations concern triangle-free graphs with **no** four-cycles, and triangle-free graphs whose four-cycles have **pairwise edge-disjoint** edge sets. Neither applies to \(H\): it contains nine four-cycles, and **every one of its eighteen edges belongs to two distinct four-cycles**. In particular, the latter theorem's sole-top-degree homology conclusion cannot subsume the two-degree homology calculated here. A published calculation of \(\operatorname{Ind}(H)\), the Herschel **independence** complex, studies a different simplicial complex and does not imply the present statements. These distinctions compare hypotheses and implications, not merely result names.

## Limitations
The classification is confined to the ordinary three-cut complex of the precisely defined graph and its rational automorphism action. No claim is made about the **homotopy** type of the cut complex, an integral decomposition as a \(\mathbb Z[G]\)-module, an equivariant homotopy equivalence, or wider families of graphs. The simple-homotopy classification of the dual is also not asserted. The integer calculation uses fully reconstructible exhaustive finite matrices; an unindexed earlier equivalent calculation cannot be ruled out definitively by source searches alone. Independent external validation remains outstanding.

## References
[1] M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first public 2023-04-26, https://arxiv.org/abs/2304.13675.

[2] M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first public 2024-07-11, https://arxiv.org/abs/2407.08158.

[3] *Three-cut complexes of triangle-free graphs with edge-disjoint squares*, publicly available full mathematical statement and proof, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-three-cut-complexes-of-triangle-free-graphs-with-edge-disjoint-s--8ca830284420/RESULT.md.

[4] *Three-cut complexes of graphs without short cycles: sphere wedges and symmetry characters*, publicly available full mathematical statement and proof, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-three-cut-complexes-of-graphs-without-short-cycles-sphere-wedges--868c7d2aa0e7/RESULT.md.

[5] *The Herschel graph independence complex and its complete vertex-deletion profile*, publicly available full mathematical statement and proof, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-the-herschel-graph-independence-complex-and-its-complete-vertex--e6d752a4b77d/RESULT.md.

[6] SageMath graph generator `HerschelGraph`, https://doc.sagemath.org/html/en/reference/graphs/sage/graphs/generators/smallgraphs.html.
