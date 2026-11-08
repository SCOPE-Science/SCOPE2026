# Rational \(S_5\)-homology of the Petersen matching complex

## Finding
Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph: its vertices are the two-element subsets of \([5]=\{1,2,3,4,5\}\), and two vertices are adjacent exactly when they are disjoint. Let \(X=\mathcal M(P)\) be its **ordinary** matching complex, with one simplicial vertex for each of the 15 graph edges and a face for each collection of mutually vertex-disjoint graph edges. The canonical group \(S_5\) acts by relabeling \([5]\).

The complete reduced rational homology and its full natural \(S_5\)-module structure are
\[
\widetilde H_i(X;\mathbb Q)\cong
\begin{cases}
\operatorname{sgn}\otimes\mathbb Q^{[5]},&i=2,\\
S^{(3,2)},&i=3,\\
0,&i\ne2,3.
\end{cases}
\]
Here \(\mathbb Q^{[5]}\) is the five-dimensional permutation module on the five letters; \(S^{(3,2)}\) is the five-dimensional irreducible rational Specht module. Equivalently, for every \(g\in S_5\), writing \(f(g)\) for its number of fixed letters, \(t(g)\) for its number of transpositions in its disjoint cycle decomposition, and \(\epsilon(g)\) for its sign,
\[
\operatorname{tr}(g\mid\widetilde H_2(X;\mathbb Q))=\epsilon(g)f(g),\qquad
\operatorname{tr}(g\mid\widetilde H_3(X;\mathbb Q))=\binom{f(g)}2+t(g)-f(g).
\]
Both positive-degree representations have zero \(S_5\)-fixed subspace. Consequently the orbit space \(|X|/S_5\) is **rationally acyclic**, i.e. \(H_i(|X|/S_5;\mathbb Q)=0\) for every \(i>0\). This is an equality of rational modules; no integral equivariant lattice classification is asserted.

## Assumptions and scope
All graph edges are unordered; all simplicial chains are over \(\mathbb Q\) with each simplex oriented by increasing graph-edge index. Vertex indices in the verifier run from 0 to 4; that indexing is identified with \([5]\) by adding one. The group is the natural permutation group on those five labels. Matching means pairwise **vertex-disjoint** edges, not a subgraph with matching number bounded by another threshold. All module isomorphisms and quotient homology conclusions are rational, and the assertion concerns this one finite simplicial complex only.

## Proof
**Exact chain complex.** Order the ten graph vertices lexicographically, then order the fifteen graph edges lexicographically. Enumerate all subsets of the fifteen edges and retain exactly those whose endpoints are pairwise disjoint. The numbers of nonempty faces of cardinalities one through five are
\[
(15,75,145,90,6).
\]
Orient each face \((e_1<\cdots<e_k)\) by that ordering, and let the simplicial boundary delete \(e_j\) with sign \((-1)^{j-1}\). The exact rational ranks of the boundary maps from cardinalities two, three, four, and five are respectively
\[
(14,61,79,6).
\]
The complete reproducible elimination, without floating-point or finite-field arithmetic, appears in `verify_petersen_matching.py`. It reconstructs the face list and signed matrices, establishes \(\partial^2=0\), and computes all independent columns using rational row-reduced echelon forms. These values imply \(\widetilde b_0=\widetilde b_1=\widetilde b_4=0\) and \(\widetilde b_2=\widetilde b_3=5\). There are no higher-dimensional faces.

**Equivariant trace extraction.** Every label permutation carries each ordered graph edge and face to another one, with the orientation sign equal to the parity of the resulting edge reordering. The verifier checks \(g\partial=\partial g\) for all 120 permutations and every positive-dimensional oriented face. For a differential \(d\), choose a full-rank column submatrix \(A\) spanning \(\operatorname{im}d\), then choose row indices \(I\) so that the square matrix \(A_I\) is invertible. Since the image is invariant, the action there has trace
\[
\operatorname{tr}(g\mid\operatorname{im}d)=
\operatorname{tr}\bigl(A_I^{-1}(gA)_I\bigr).
\]
All inverses and matrix products here are taken over exact rational numbers. For each chain degree the two exact short sequences involving cycles and boundaries give
\[
\operatorname{tr}(g\mid H_k)
=\operatorname{tr}(g\mid C_k)
-\operatorname{tr}(g\mid\operatorname{im}\partial_k)
-\operatorname{tr}(g\mid\operatorname{im}\partial_{k+1}).
\]
Applying the formula to one representative of each conjugacy class yields the following class data; the entries are the traces in homological degrees two and three, respectively:

| Cycle type | Class size | \(\chi_2\) | \(\chi_3\) |
| --- | ---: | ---: | ---: |
| \(1^5\) | 1 | 5 | 5 |
| \(2\,1^3\) | 10 | -3 | 1 |
| \(2^2\,1\) | 15 | 1 | 1 |
| \(3\,1^2\) | 20 | 2 | -1 |
| \(3\,2\) | 20 | 0 | 1 |
| \(4\,1\) | 30 | -1 | -1 |
| \(5\) | 24 | 0 | 0 |

The first column of characters is precisely \(\epsilon(g)f(g)\). The second is the character of the two-subset permutation representation minus the five-letter permutation representation. The usual permutation action on two-element subsets decomposes as the direct sum of the trivial, four-dimensional standard and irreducible \(S^{(3,2)}\) modules, while the five-letter permutation module is trivial plus standard. Alternatively, the exact character inner product of the second representation with itself is one, showing irreducibility, and its conventional Specht label is \((3,2)\). Maschke semisimplicity over \(\mathbb Q\) proves the stated module isomorphisms.

**Quotient.** The multiplicity of the trivial character is zero in both modules, by class averaging. A finite simplicial group action can be barycentrically subdivided so the rational cellular chains of the quotient agree with invariant rational chains; exactness of invariants in characteristic zero implies the rational homology of the quotient equals the invariant homology. This proves the acyclicity assertion.

## Verification
Run `python3 verify_petersen_matching.py` with Python 3 and SymPy. The companion file `verification_output.txt` is the actual exact-arithmetic output. The executable reconstructs every matrix and checks all 120 group elements, not a sample, and the seven conjugacy-class representatives cover all elements. The elimination works in \(\mathbb Q\), not merely modulo a prime. The separate finite combinatorial set of 120 automorphisms and all faces exhausts the stated objects; no extrapolation to other graphs is made.

## Relationship to prior work
Jonsson's *Simplicial Complexes of Graphs* (2007 print edition) develops the matching-complex methodology and surveys classical homology problems. Bate–Everitt–Ford–Ramos (2026) compute representations for complete-hypergraph matching complexes; their actual full-text theorems concern those complete hypergraphs and fibre-closed families, rather than the proper noncomplete graph \(\operatorname{KG}(5,2)\) used here. Berghoff (2022), Example 6.2, determines the ordinary homology of the **independence complex of the Petersen graph itself**, which is not the matching complex of that graph (the latter is the independence complex of its **line graph**). These objects are not interchangeable.

The presently asserted contribution is the explicit **two-degree full rational automorphism-module classification**, not the general matching-complex definitions, nonequivariant homology techniques, or topology of the Petersen graph alone. A prior nonequivariant sphere-wedge classification for this matching complex supplies dimensions only; those dimensions do not imply the two character formulas. Searches of relevant public literature and mathematical research indices did not identify the exact formulas, but absence of search matches does not certify publication priority.

## Limitations
This is one finite graph and the rational action of its natural \(S_5\)-symmetry. The result neither identifies integral homology lattices as \(\mathbb Z[S_5]\)-modules nor determines the quotient's integral torsion, ring structure, or equivariant homotopy type. The matching chapter in the 2007 survey was accessible only as a publisher preview; its full text was not inspected. Although no identical claim was found in the inspected materials, unindexed results and unpublished calculations are residual novelty risks. Independent mathematical verification has not been performed.

## References
1. J. Jonsson, *Simplicial Complexes of Graphs*, Springer Lecture Notes in Mathematics 1928, matching chapter, print release November 15, 2007; DOI: https://doi.org/10.1007/978-3-540-75859-4_11.
2. M. Bate, B. Everitt, S. Ford and E. Ramos, *Homology of matching complexes and representations of symmetric groups*, author-accepted manuscript deposited 2025, published 2026; DOI: https://doi.org/10.1090/proc/17573; open full text: https://eprints.whiterose.ac.uk/id/eprint/234058/7/Homological_reps_of_symmetric_groups_1.pdf.
3. M. Berghoff, *On the homology of independence complexes*, *Combinatorial Theory* **2** (2022), Article 8; DOI: https://doi.org/10.5070/C62156880; Example 6.2 concerns the independence complex of the Petersen graph itself.
