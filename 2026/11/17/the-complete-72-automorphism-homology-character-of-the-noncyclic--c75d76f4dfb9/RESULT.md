# The complete 72-automorphism homology character of the noncyclic order-five Latin-square clique complex

## Finding
Let \(L\) be the displayed Latin square and let \(X\) be the clique complex of its 25-vertex Latin-square graph, joining two distinct cells sharing a row, a column, or a symbol:
\[
L=\begin{pmatrix}0&1&2&3&4\\1&0&3&4&2\\2&3&4&0&1\\3&4&1&2&0\\4&2&0&1&3\end{pmatrix}.
\]
The full graph automorphism group \(A=\operatorname{Aut}(G(L))\) has order \(72\). Its rational representation on \(\widetilde H_2(X;\mathbb Q)\) has dimension \(60\) and **no invariant vectors**. Its complete character at each of the \(72\) explicitly numbered permutations is in `tables/character_table.csv`; the following partition records every value, with sorted vertex-cycle lengths written multiplicatively in prose:

| Vertex-permutation cycle pattern | Trace | Number of automorphisms |
|---|---:|---:|
| identity | 60 | 1 |
| one fixed vertex and four 6-cycles | 0 | 6 |
| one fixed vertex and six 4-cycles | 0 | 18 |
| one fixed vertex and eight 3-cycles | 3 / 0 | 8 / 2 |
| four fixed vertices and seven 3-cycles | 3 / 0 | 8 / 8 |
| one fixed vertex and twelve 2-cycles | 0 | 3 |
| five fixed vertices and ten 2-cycles | −6 | 18 |

In particular, vertex-cycle type alone does not determine the character: two patterns split into distinct trace values. The full symmetry quotient \(|X|/A\) has vanishing positive-degree **rational** homology. This does not assert integral acyclicity or contractibility.

## Assumptions and scope
The graph has vertex set \(\{0,1,\ldots,24\}\), with cell \(5i+j\) representing row \(i\), column \(j\) of \(L\). Every graph automorphism is a permutation of those 25 vertices. The complex \(X\) contains every clique, including its four-dimensional maximal simplices. The claim concerns the complete rational second-homology character, not a determination of the integral representation lattice or an equivariant homotopy type. Permutations in the data table are written by their images of vertices \(0,\ldots,24\).

## Proof
**Finite structure and group exhaustiveness.** Construct the graph from the exact row/column/symbol equality rule. Enumerating all cliques gives \(25,150,250,79,15\) faces of respective cardinalities one through five. A complete graph-isomorphism backtracking enumeration of \(G(L)\) with itself produces exactly \(72\) distinct automorphisms. Every output permutation preserves all edges, and exhaustive backtracking excludes unlisted automorphisms.

**Homological concentration.** Form all mod-two simplicial boundary matrices directly from the faces. Their ranks, for boundaries from cardinality two through five, are \(24,126,64,15\). Hence the reduced mod-two Betti numbers in dimensions zero through four are \((0,0,60,0,0)\). For finite free integral chain complexes, the universal coefficient theorem implies each rational Betti number is at most the corresponding mod-two Betti number. The reduced Euler characteristic computed from the face vector is \(60\); hence the only nonzero reduced rational homology is \(\widetilde H_2(X;\mathbb Q)\cong\mathbb Q^{60}\).

**Exact character.** For every graph automorphism \(a\), a fixed face \(F\) contributes the sign of the induced permutation of its increasing vertex order to the simplicial chain trace. The reduced alternating Lefschetz formula therefore gives
\[
\chi_2(a)=\sum_{k=1}^{5}(-1)^{k-1}\sum_{\substack{F\text{ clique}\\ |F|=k,\ aF=F}}\operatorname{sgn}(a|_F)-1.
\]
The displayed finite formula, applied exhaustively to the \(72\) automorphisms and every face, yields the exact table. The character sum is \(0\), so averaging over \(A\) gives \(\dim\widetilde H_2(X;\mathbb Q)^A=0\). Over rational coefficients, finite-group coinvariants equal invariants; the simplicial quotient has the same rational homology as the coinvariants. Thus \(|X|/A\) is rationally acyclic in positive degrees.

## Verification
Run `python checks/verify.py` after installing the dependency declared in `checks/requirements.txt`. It reconstructs the graph and every face, enumerates all graph automorphisms, checks the reduced mod-two boundary ranks, evaluates every signed Lefschetz trace, prints the class-value distribution and asserts the stated group order, dimension, character sum, and character distribution. `checks/output.txt` records its successful run. The row-wise complete character is separately included in `tables/character_table.csv`. The proof is finite and exhaustive for this one 25-vertex complex.

## Relationship to prior work
Cioabă and Mim (2026) determine the **ordinary homology ranks over arbitrary fields** of Latin-square graph clique complexes; their order-five formula already implies the rank \(60\). The present result **does not claim that rank or the underlying sphere-wedge homotopy type as new**. Separate prior work determines translation characters for Latin-square graphs arising from abelian group tables, including the cyclic order-five case; those results do not supply the full 72-element character of the noncyclic order-five graph. The new information is the exhaustive character, the two cycle-pattern splits, and absence of invariants under full symmetry.

## Limitations
The calculation is specific to the displayed noncyclic Latin square and every graph isomorphic to its Latin-square graph. It gives no general character formula for higher-order Latin squares, no integral homology lattice classification, and no claim about integral quotient torsion. The previously published nonequivariant ranks are credited rather than republished as a discovery. An independently authored verification has not been performed; an equivalent unpublished character table cannot be excluded.

## References
- S. M. Cioabă and M. Mim, *On the homology groups of clique complexes of strongly regular graphs*, arXiv:2606.27328 (first posted 2026-06-25), https://arxiv.org/abs/2606.27328.
- *Translation characters of cyclic Latin-square clique complexes in all odd orders* (2026); result concerning the cyclic group-table family.
- `checks/verify.py` and `tables/character_table.csv`, full finite calculation and explicit character data.
