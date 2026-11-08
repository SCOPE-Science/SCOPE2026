# The two rational symmetry modules of the Petersen matching complex

## Finding
Let \(P\) be the Petersen graph with vertex set \(\binom{[5]}2\), in which two vertices are adjacent precisely when the represented pairs are disjoint. Let \(X=\mathsf M(P)\) denote the **ordinary matching complex**: its vertices are the fifteen edges of \(P\), and its simplices are pairwise vertex-disjoint collections of these edges. Permutations of the five symbols induce the full \(S_5=\operatorname{Aut}(P)\) action on \(X\). Then
\[
\widetilde H_2(X;\mathbb Q)\cong_{\mathbb Q[S_5]}\operatorname{sgn}\otimes\mathbb Q^{[5]},\qquad
\widetilde H_3(X;\mathbb Q)\cong_{\mathbb Q[S_5]}S^{(3,2)}.
\]
Every other reduced rational homology group vanishes. The first five-dimensional representation is reducible, whereas the second is an irreducible Specht module. On the seven cycle types \((1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)\), respectively, their traces are
\[
\chi_2=(5,-3,1,2,0,-1,0),\qquad
\chi_3=(5,1,1,-1,1,-1,0).
\]

## Assumptions and scope
The graph is exactly the ten-vertex, fifteen-edge Petersen graph as defined above. These are ordinary *edge matchings* of \(P\), not the classical complex \(\mathsf M(K_5)\) (whose one-skeleton is itself the Petersen graph), not the two-matching complex allowing vertex incidence twice, and not a graph-matching Morse complex. The coefficients are \(\mathbb Q\); no integral-torsion or full homotopy-type statement is asserted. The module \(\mathbb Q^{[5]}\) has basis the five symbols with their usual permutation action. The Specht module \(S^{(3,2)}\) is characterized here by the character of the ten-element permutation module on two-subsets minus the five-element permutation module on singletons.

## Proof
List the two-subsets of \([5]\) lexicographically, and list edges as lexicographically ordered disjoint pairs of those two-subsets. A face of dimension \(k\) is an increasing tuple of \(k+1\) such edge indices, with no Petersen-graph endpoint repeated. Exhaustive enumeration of the \(2^{15}\) possible edge subsets gives precisely \((15,75,145,90,6)\) faces in dimensions zero through four. This exhaustiveness follows since every matching contains at most five disjoint edges on ten graph vertices.

Form rational simplicial chain modules \(C_k\) with these oriented bases, and boundary matrices \(D_k\) with entry \((-1)^i\) for deletion of the \(i\)-th vertex from an oriented face. Exact Gaussian elimination over \(\mathbb Q\) gives
\[
\bigl(\operatorname{rank}D_1,\operatorname{rank}D_2,\operatorname{rank}D_3,\operatorname{rank}D_4\bigr)=(14,61,79,6).
\]
The script independently verifies \(D_{k-1}D_k=0\) in all applicable degrees. Rank-nullity now gives \(\widetilde b_2=145-61-79=5\), \(\widetilde b_3=90-79-6=5\), and zero otherwise.

For each of all \(120\) permutations \(g\in S_5\), transport the fifteen graph edges and each oriented simplex, multiplying by the sign of the sorting permutation. This defines explicit signed permutation matrices \(T_{k,g}\) commuting with the boundaries. For degree three, compute an exact basis of \(\ker D_3\), extend the columns of \(D_4\) to a basis of the kernel, express the image of each of the five complementary basis cycles in this basis, and sum the five diagonal coefficients of the induced quotient action. This yields the seven conjugacy-class traces \(\chi_3\) displayed above; all \(120\) permutations are individually verified.

For degree two, compute the combinatorial Lefschetz number \(L(g)=\sum_{k=0}^4(-1)^k\operatorname{tr}T_{k,g}\). Since rational homology is confined to degrees zero, two and three, \(L(g)=1+\chi_2(g)-\chi_3(g)\), so \(\chi_2(g)=L(g)-1+\chi_3(g)\). This gives the displayed second character for every permutation.

For each \(g\), the character of \(\operatorname{sgn}\otimes\mathbb Q^{[5]}\) is \(\operatorname{sgn}(g)\) times its number of fixed symbols, exactly \(\chi_2(g)\). The character of \(\mathbb Q^{\binom{[5]}2}-\mathbb Q^{[5]}\) is exactly \(\chi_3(g)\), and its irreducible constituent is the standard five-dimensional Specht module \(S^{(3,2)}\) (Young's rule). Maschke semisimplicity and uniqueness of rational characters identify the modules, completing the proof.

## Verification
Run `python verify.py` with Python 3 and SymPy. The program is self-contained: it reconstructs all 331 nonempty simplices; builds and ranks every boundary matrix; checks the chain equations; constructs degree-three homology as an exact quotient; checks all 120 induced symmetry actions; and verifies both character tables. Its recorded output in `verify_output.txt` ends with `VERIFY_OK`. This is an exact finite rational computation, not an inference from sampling.

## Relationship to prior work
Zaslavsky's **Six signed Petersen graphs, and their automorphisms** (§3 and §3.2) explicitly describes the Petersen graph as disjoint two-subsets, identifies \(S_5\) as its automorphism group, and classifies matching orbits; it does not calculate the ordinary matching simplicial complex's homology or either representation. Larrión, Pizaña and Villarroel-Flores discuss matching complexes of complete graphs and the Petersen graph realized as the classical matching graph on five points; the distinction between \(\mathsf M(K_5)\) and \(\mathsf M(P)\) is essential. Work on the *Petersen two-matching complex* or the *Petersen Morse complex* concerns different face conditions and does not imply this theorem. Direct exact-formulation searches did not find the pair of representations here. Absence of indexed matches is not proof of universal novelty; equivalent, unpublished or unindexed coverage remains a risk.

## Limitations
Only the exact ten-vertex Petersen graph and rational coefficient representations are covered; integral torsion, integral module extensions and homotopy type are not determined. The computational proof is exact and fully enumerable but should be independently reproduced before external use. No assertion of independent mathematical validation is made.

## References
- T. Zaslavsky, *Six signed Petersen graphs, and their automorphisms*, arXiv:1303.3347v1 (first posted 14 March 2013); see §3 and §3.2, https://arxiv.org/abs/1303.3347.
- F. Larrión, M. A. Pizaña and R. Villarroel-Flores, *The clique operator on matching and chessboard graphs*, Discrete Mathematics 309 (2009), 85–93, doi:10.1016/j.disc.2007.12.047. This reference concerns different matching graphs and provides terminology/background, not the asserted two representations.
