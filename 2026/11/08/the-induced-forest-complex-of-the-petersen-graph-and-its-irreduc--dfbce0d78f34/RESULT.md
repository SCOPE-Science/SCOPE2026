# The induced-forest complex of the Petersen graph and its irreducible \(S_5\)-homology

## Finding
Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph. Its vertex set comprises the ten unordered two-element subsets of \(\{0,1,2,3,4\}\), with adjacency precisely for disjoint pairs. Define the *induced-forest complex* \(\mathcal F(P)\) to contain precisely those vertex subsets whose induced graph is acyclic. Then
\[
\mathcal F(P)\simeq\bigvee^{6}S^{5}.
\]
The natural permutation action of \(S_5\) on the five underlying letters induces an action on its rational reduced fifth homology, and
\[
\widetilde H_5(\mathcal F(P);\mathbb Q)\cong\bigwedge^{2}V\cong S^{(3,1,1)},
\]
where \(V\subset\mathbb Q^5\) is the standard four-dimensional augmentation representation. The representation is irreducible. The result is an integral homotopy equivalence and a rational equivariant homology identification; no equivariant homotopy equivalence is asserted.

## Assumptions and scope
All graphs are finite and simple. Faces are *vertex* subsets inducing forests; this is not the graphic-matroid complex whose faces are edge forests, nor the ordinary independence, matching, Morse, or cut complexes. A graph on a vertex set is considered acyclic if it has no undirected cycles; isolated vertices are allowed. Index the ten Petersen vertices by the lexicographically increasing two-letter pairs. Encode a face by a ten-bit nonnegative integer. The empty face is included in the abstract complex, but is not a topological cell. The action is by relabeling the underlying five letters, not by arbitrary permutations of the ten graph vertices.

## Proof
**Complete face enumeration.** The exhaustive membership test constructs the fifteen Petersen edges and checks whether each selected edge joins two previously disconnected components in a disjoint-set forest. A second, independent depth-first-search cycle test agrees on every one of the \(2^{10}=1024\) possible subsets. Exactly 786 subsets are acyclic, including the empty subset; the nonempty face vector in dimensions zero through six is
\[
(10,45,120,210,240,140,20).
\]
No simplex has higher dimension.

**Integral homotopy type.** Set aside the empty face. Start with all 785 nonempty faces unmatched. For each vertex index \(i=0,\ldots,9\), in increasing order, inspect all still-unmatched faces \(A\) not containing \(i\), in increasing numerical mask order, and match \(A\) to \(A\cup\{i\}\) whenever this larger face remains unmatched. Remove each paired face from the active set. The resulting finite matching has 389 pairs, with precisely seven unmatched faces: mask \(1\) in dimension zero and masks \(946,948,952,978,980,984\) in dimension five. To prove acyclicity, direct every nonempty codimension-one face-poset covering downward, except for matching edges, which are reversed. This generates exactly 3470 directed edges on 785 face vertices. An exhaustive indegree-based topological sort visits all 785 vertices, so the orientation has no directed cycles. These verifiable finite assertions supply a complete discrete-Morse certificate.

Forman's discrete-Morse theorem gives a CW model with one zero-cell and six five-cells and no other cells. Each five-cell attaches to the sole zero-cell because the four-skeleton is a point. Its attaching map is therefore constant, proving an integral homotopy equivalence to a wedge of six five-spheres. This argument establishes homotopy, rather than inferring it merely from homology ranks.

**Symmetry action.** For any permutation \(g\in S_5\), a nonempty face \(A\) fixed setwise by \(g\) contributes \((-1)^{|A|-1}\operatorname{sgn}(g|_A)\) to the ordinary simplicial Lefschetz number. Directly summing these signs across the complete face set and using the homology concentration gives the character of rational fifth homology, in conjugacy-class order
\[
(1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5):\quad (6,0,-2,0,0,0,1).
\]
To compute the comparison character independently, let \(f(g)\) be the number of fixed letters in the five-letter permutation. The standard representation has trace \(f(g)-1\), so the exterior-square trace is
\[
\chi_{\wedge^{2}V}(g)=\frac{(f(g)-1)^2-(f(g^2)-1)}{2}.
\]
Exhaustively checking all 120 permutations verifies the two characters coincide. Their class-weighted character inner product is \(1\), proving irreducibility, and semisimplicity identifies the rational representation with \(\bigwedge^2V\).

## Verification
Run the bundled `verify.py` with Python 3.8 or newer; it uses only the standard library and aborts on failed assertions. It independently compares two cycle-detection algorithms on all 1024 subsets; verifies every matching pair, residual critical mask and oriented Hasse cover; checks the entire oriented graph for directed cycles; independently calculates the reduced simplicial mod-two boundary ranks and finds exactly six generators in degree five; and computes signed fixed-face traces for all 120 coordinate permutations against the exterior-square formula. All assertions are exact integer computations, not probabilistic tests or sampled enumerations. The recorded output is `verification_output.txt`.

## Relationship to prior work
Taylan's 2015 paper develops forbidden-induced-subgraph complexes and generalized matching-tree methods but its explicit graph-family classifications do not give this Petersen induced-forest homotopy or representation. Carnero Bravo's forest-filtration paper (first public 2023; latest inspected text revised 2025) explicitly defines \(\mathcal F_\infty(G)\) as the vertex-induced forest complex and determines homotopy types for paths, cycles, double stars, cactus graphs and certain graph operations. Its inspected family theorems do not include the Petersen graph, and no Petersen or Kneser instance occurs in its searchable full text.

The independently published *Petersen three-cut* calculation determines \(\Delta_3(P)\simeq\bigvee^6S^6\) with the same \(S_5\) character \(S^{(3,1,1)}\), but that cut complex consists of subsets lying inside complements of disconnected induced triples, not all induced forests. Its nonzero homology is in degree six rather than five, and its assertions do not supply a natural suspension equivalence or calculate this induced-forest complex. The shared representation is an interesting comparison, not a claim that the complexes are identical. No inspected prior statement implies both the new integral homotopy type and the equivariant character of this object.

## Limitations
This is a complete calculation for one ten-vertex graph, not a classification of all Kneser graphs or induced-forest complexes. The equivariant conclusion is rational and does not specify integral representation lattices or an equivariant homotopy equivalence. An indexed or unindexed exact calculation under other terminology could establish publication priority; the literature comparison is bounded and not a proof of global novelty. Independent validation is not claimed.

## References
1. D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754, first submitted January 27, 2015. https://arxiv.org/abs/1501.06754
2. A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, first submitted July 25, 2023, revised March 2025. https://arxiv.org/abs/2307.13271
3. *An irreducible \(S_5\)-module in the Petersen three-cut complex*, published mathematical-record entry. https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-an-irreducible-s-5-module-in-the-petersen-three-cut-complex--0eae16654cf3/RESULT.md
4. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
