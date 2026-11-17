# The complete wreath-product homology character of the four-by-four rook dissociation complex

## Finding

Let \(R=K_4\square K_4\) be the rook graph on the sixteen cells of a \(4\times4\) board, and let \(X=\operatorname{Ind}_2(R)\) consist of all cell sets whose induced graph components have at most two vertices. Its graph automorphism group is \(G=(S_4\times S_4)\rtimes C_2\), of order \(1152\), in which the last factor interchanges the two coordinates. The complete rational degree-three homology character of \(G\), including its twenty conjugacy classes, is given in `character_table.csv`; all other reduced rational homology groups vanish, and \(\dim_\mathbb Q\widetilde H_3(X;\mathbb Q)=105\).

Write \(V_\lambda\) for the rational Specht module of \(S_4\) indexed by a partition \(\lambda\vdash4\). For distinct \(\lambda,\mu\), set \(I_{\lambda,\mu}=\operatorname{Ind}_{S_4\times S_4}^{G}(V_\lambda\boxtimes V_\mu)\). For equal factors, \(D_\lambda^\pm\) denotes \(V_\lambda\boxtimes V_\lambda\) extended to \(G\) by the signed tensor-factor flip. These are irreducible rational representations. The complete decomposition is

\[
\begin{aligned}
\widetilde H_3(X;\mathbb Q)\cong{}&I_{(4),(2,2)}\oplus I_{(4),(1^4)}\oplus I_{(3,1),(2,2)}\\
&\oplus 2I_{(3,1),(2,1,1)}\oplus I_{(3,1),(1^4)}\\
&\oplus I_{(2,2),(1^4)}\oplus I_{(2,1,1),(1^4)}\\
&\oplus D_{(2,2)}^+\oplus D_{(2,2)}^-\oplus 2D_{(2,1,1)}^+\oplus D_{(2,1,1)}^-.
\end{aligned}
\]

No nonzero rational class survives the full group or the row-and-column subgroup \(S_4\times S_4\). By contrast, the spaces of classes invariant under the row-only group, the simultaneous-diagonal group, and the simultaneous-diagonal group extended by coordinate interchange have respective dimensions \(3,5,3\). In particular the ordinary symmetry quotient \(|X|/G\) is rationally acyclic, while the diagonal and diagonal-plus-interchange quotients have respectively three-dimensional homology of ranks five and three and no other positive-degree rational homology.

## Assumptions and scope

The simplicial faces are exactly the subsets \(F\subseteq\{0,1,2,3\}^2\) for which every cell in \(F\) has at most one other selected cell in its row or column. Empty face included. Homology is reduced simplicial homology with rational coefficients; topology of quotients refers to the ordinary orbit space of the geometric realization. The symbol \(I_{\lambda,\mu}\) is indexed by an unordered pair of *different* partitions, so it is unambiguous. The sign \(\pm\) in \(D_\lambda^\pm\) means that the coordinate interchange acts as plus or minus the vector-space factor swap. The notation \((1^4)\) denotes the four-part sign partition.

## Proof

**Rational homology and its concentration.** Exhaustive enumeration of all \(2^{16}\) vertex subsets using the stated induced-degree predicate gives face counts by cardinality \((1,16,120,384,528,144)\), including the empty face. The standalone code constructs exact simplicial boundary columns and computes the ranks over \(\mathbb F_2\) of \(\partial_1,\partial_2,\partial_3,\partial_4\) as \((15,105,279,144)\). The same boundaries have rational ranks at least these values. Their rational ranks are simultaneously bounded above by \(15\), \(120-\operatorname{rank}\partial_1\), \(384-\operatorname{rank}\partial_2\), and \(144\), respectively, by \(\partial^2=0\) and the relevant chain dimensions. Reading these inequalities successively proves equality for every rank. Hence reduced homology is nonzero only in degree three and has dimension \(528-279-144=105\). No inference from a finite sample to an infinite family is used; this is a complete finite calculation.

**Full character.** The graph's maximal four-cliques are precisely its four rows and four columns; their intersection structure makes the full automorphism group \((S_4\times S_4)\rtimes C_2\). For each of its \(1152\) permutations, the script verifies that every face maps to a face. If \(g\) preserves a face \(F\) setwise, let \(\epsilon(g,F)\) denote its orientation sign on the ordered vertices of \(F\). The reduced Lefschetz formula and concentration in odd degree three imply

\[
\operatorname{tr}\bigl(g\mid \widetilde H_3(X;\mathbb Q)\bigr)
=\sum_{gF=F}(-1)^{|F|}\epsilon(g,F),
\]

where the sum includes the empty face with sign one. A second algorithm enumerates unions of vertex-permutation cycles: an admissible union of \(s\) cycles contributes \((-1)^s\). Both methods agree for all \(1152\) elements and yield the twenty class values tabulated in `character_table.csv`. In the non-interchanged coset, the class label is an unordered pair of \(S_4\) cycle types; in the interchanged coset, it is the cycle type of the product of the two coordinate permutations.

**Irreducible decomposition.** For the normal subgroup \(S_4\times S_4\), take inner products of the character with every tensor product of the five irreducible \(S_4\) characters. The resulting ordered multiplicity matrix is

\[
\begin{pmatrix}
0&0&1&0&1\\
0&0&1&2&1\\
1&1&2&0&1\\
0&2&0&3&1\\
1&1&1&1&0
\end{pmatrix},
\]

in partition order \((4),(3,1),(2,2),(2,1,1),(1^4)\). Every off-diagonal pair gives the indicated induced irreducible. For a diagonal representation, the difference between plus and minus multiplicities equals the normalized coset character inner product with the relevant \(S_4\) character of the coordinate-permutation product. These differences are \((0,0,0,1,0)\), so the plus/minus multiplicities are \((1,1)\) for \((2,2)\) and \((2,1)\) for \((2,1,1)\), with all others zero. The displayed decomposition has total dimension \(105\), as required, and the character squared norm is \(17\), equal to the sum of squares of its multiplicities.

**Quotients.** For a finite simplicial group action, barycentric subdivision permits transfer and identifies the rational cohomology of the ordinary quotient with invariant rational cohomology. Averaging the computed character over the indicated subgroups gives fixed-subspace dimensions \(0\), \(0\), \(3\), \(5\), and \(3\) for \(G\), \(S_4\times S_4\), row-only \(S_4\), diagonal \(S_4\), and diagonal \(S_4\) extended by coordinate flip, respectively. Since the only nonzero positive-degree cohomology lies in degree three, each quotient's rational ring is uniquely determined by these ranks (all positive-degree products vanish).

## Verification

Run `python3 verify_rook2.py` using Python 3 and its standard library. The verifier checks face preservation for all \(1152\) automorphisms, independently computes each signed trace in two ways, verifies all class sizes and multiplicities, and checks the indicated modular boundary ranks. The exact recorded output is in `verification_output.txt` and ends with `ROOK2_FULL_EQUIVARIANT_CHARACTER_PASS`. The character table is reproduced separately in `character_table.csv` and can be reconstructed from the code. Modular ranks are used only with the explicit characteristic-zero upper bounds proved above; they are not treated as standalone rational-rank proof.

## Relationship to prior work

The rook graph's spectral, Smith-group and critical-group structures were treated by Ducey–Gerhard–Watson (2016), but those adjacency/Laplacian calculations do not determine the present complex or its homological character. Deshpande–Singh (2020) introduce and study higher-independence complexes for complete multipartite, whiskered, cyclic and tree families; Abdelmalek et al. (2021) analyze chordal graphs and related classes. Neither inspected work supplies this full wreath-product action for the present rook complex. The nonequivariant homotopy type \(X\simeq\bigvee^{105}S^3\) has previously been established and is *not* claimed as a new finding. The ordinary rook chessboard complex, the two-matching complex of the complete bipartite graph, radius-one rook Čech complexes and rook three-cut complexes are different simplicial complexes; their automorphism results do not imply this character without an additional unproved equivalence.

## Limitations

The claim is an exact finite computation for a single rook graph, not a uniform theorem for all board sizes. It determines rational, not integral, group representations or quotient torsion; rational cohomology does not imply a quotient homotopy type. It was checked mathematically by a reproducible complete finite program and reviewed against accessible literature, but it has not received an independent mathematical audit. Unindexed or inaccessible publications remain a priority risk.

## References

- J. E. Ducey, J. Gerhard and N. Watson, *The Smith and Critical Groups of the Square Rook's Graph and its Complement*, Electronic Journal of Combinatorics **23** (2016), P4.9, DOI: 10.37236/5442, published 2016-10-14.
- P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, first posted 2020-01-15.
- F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, first posted 2021-06-21.
