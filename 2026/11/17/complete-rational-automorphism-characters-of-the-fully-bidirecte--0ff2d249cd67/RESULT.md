# Complete rational automorphism characters of the fully bidirected \(K_{3,3}\) multipath complex

## Finding
Let \(D=\overleftrightarrow{K}_{3,3}\) have a vertex bipartition of size three and two opposite directed arcs for every cross-part edge. Let \(X=X(D)\) be the multipath complex, with simplices the sets of arcs forming a vertex-disjoint union of directed simple paths, and let \(G=(\mathfrak S_3\times\mathfrak S_3)\rtimes C_2\) act by vertex permutations and interchange of the parts.

Write \(T,S,V\) for the trivial, sign, and two-dimensional standard rational representations of \(\mathfrak S_3\). For distinct \(U,W\in\{T,S,V\}\), write \(UW=\operatorname{Ind}_{\mathfrak S_3\times\mathfrak S_3}^G(U\boxtimes W)\). Write \(U^+\) and \(U^-\) for the two extensions of \(U\boxtimes U\), with the part interchange acting as plus or minus the tensor-factor flip. Then the **complete rational homology representations** are
\[
\begin{aligned}
\widetilde H_3(X;\mathbb Q)&\cong TV\oplus SV\oplus T^+\oplus T^-\oplus S^-\oplus V^+\oplus V^-,\\
\widetilde H_4(X;\mathbb Q)&\cong TS\oplus T^-\oplus S^-\oplus V^+\oplus V^-.
\end{aligned}
\]
Every displayed constituent occurs with multiplicity one; no other reduced rational homology occurs. Thus the ranks are respectively \(19\) and \(12\). The invariant subspace under the entire order-\(72\) group has dimension one in degree three and zero in degree four. Therefore \(\widetilde H_*(|X|/G;\mathbb Q)\cong\widetilde H_*(S^3;\mathbb Q)\) as graded rational vector spaces. **No homotopy equivalence of the quotient with a sphere is asserted.**

## Assumptions and scope
The underlying vertices are \(\{0,1,2\}\sqcup\{3,4,5\}\). The \(18\) arcs are ordered first by all \((a,b)\) with \(a\in\{0,1,2\}\), \(b\in\{3,4,5\}\), then by all reverse arcs \((b,a)\), both groups in lexicographic order. A set of arcs is a simplex exactly when every vertex has indegree at most one and outdegree at most one and there is no directed cycle. This is an exact predicate, including the exclusion of directed two-, four-, and six-cycles. Every chain basis uses increasing arc-index orientation. Homology is reduced, coefficients are as displayed, and the full automorphism group of the digraph is \(G\).

There are nine conjugacy classes. For classes without part exchange, specify the unordered pair of cycle types of its two \(\mathfrak S_3\) factors; label types \(0\) (identity), \(1\) (transposition), and \(2\) (three-cycle). For exchanged parts, specify the cycle type of the product of the two permutations, denoted \(\operatorname{swap}(i)\). The characters of degree three and degree four are, in this order:

| Class | Size | \(\chi_3\) | \(\chi_4\) |
|:--|--:|--:|--:|
| \((0,0)\) | 1 | 19 | 12 |
| \((0,1)\) | 6 | 1 | 0 |
| \((0,2)\) | 4 | 1 | 0 |
| \((1,1)\) | 9 | 3 | 0 |
| \((1,2)\) | 12 | 1 | 0 |
| \((2,2)\) | 4 | 1 | 6 |
| \(\operatorname{swap}(0)\) | 6 | -1 | -2 |
| \(\operatorname{swap}(1)\) | 18 | 1 | 0 |
| \(\operatorname{swap}(2)\) | 12 | -1 | -2 |

## Proof
**Exact finite chain model.** Enumerate the \(2^{18}\) arc subsets under the admissibility predicate. There are \(714\) nonempty faces with \(f\)-vector \((18,108,264,252,72)\). A deterministic greedy discrete-Morse matching pairs every possible surviving face not containing the next arc with its coface containing that arc, never matching the empty simplex. The \(336\) pairs leave precisely one critical vertex, five critical two-cells, \(24\) critical three-cells and \(12\) critical four-cells. Orient every nonempty face incidence downward except matching incidences, which are oriented upward. A topological sort visits all \(714\) faces after checking all \(2376\) incidences. This certifies acyclicity of the complete matching.

**Integral cellular concentration.** Apply elementary algebraic Morse cancellation to the integral simplicial boundary matrices along the specified pairs. Every pivot is a unit. In the resulting reduced Morse cellular chain complex, the degree-four-to-three matrix is zero and the degree-three-to-two matrix has size \(5\times24\), full rank five, and determinant \(+1\) on its first five columns. Thus the latter has surjective integral image with a split kernel, yielding reduced integral ranks \(19\) in degree three and \(12\) in degree four and zero in the other degrees. As an independent check on these ranks, the original mod-two simplicial boundary ranks for dimensions one through four are \((17,91,173,60)\). The exact Morse matrix and its critical simplex masks are recorded by the executable verifier.

**Degree-four character.** The original top chain group has \(72\) oriented four-simplices and no five-simplices. Hence \(\widetilde H_4(X;\mathbb Q)=\ker(\partial_4)\). Construct its exact \(252\times72\) integer boundary matrix and perform rational row reduction. Its rank is \(60\), leaving \(12\) free columns that define a canonical cycle basis. For each of the nine representative vertex permutations, map an arc set to its image and multiply by the sign of the permutation needed to restore increasing arc order. Express the image of the cycle basis through its \(12\) free coordinates. The trace is exactly \(\chi_4\) in the table.

**Degree-three character.** For any group element \(g\), the reduced simplicial Lefschetz number is
\[
\widetilde L(g)=-1+\sum_{d\ge0}(-1)^d\operatorname{tr}(g\mid C_d(X;\mathbb Q)),
\]
where a basis simplex contributes only if it is setwise fixed, with its induced orientation sign. Homology concentration gives \(\widetilde L(g)=-\chi_3(g)+\chi_4(g)\). Explicit signed enumeration yields the nine Lefschetz numbers \((-7,-1,-1,-3,-1,5,-1,-1,-1)\), hence the stated \(\chi_3\). The enumeration also verifies that Lefschetz numbers are constant on each class over all \(72\) group elements.

**Irreducible decomposition and quotient.** The nine stated induced/extended representations are the full irreducible list of \(G\). Their characters follow from \(\chi_{UW}(a,b)=\chi_U(a)\chi_W(b)+\chi_W(a)\chi_U(b)\), with zero trace on exchanging elements, and \(\chi_{U^\pm}(\operatorname{swap}(ab))=\pm\chi_U(ab)\). Direct weighted character inner products are the identity matrix. Their inner products with the two computed homology characters are exactly the multiplicities stated in the Finding. Only \(T^+\) is trivial. Finally, rational transfer for a finite simplicial group action (after equivariant subdivision) identifies rational quotient homology with invariant rational homology, proving the quotient assertion.

## Verification
Run `python verify.py` with Python 3.10 or later and SymPy 1.12 or later, using `requirements.txt`. The script reconstructs all input faces, direct and Morse differentials, free-column cycle coordinates, all nine class characters, and the nine irreducible characters; it asserts exact integral algebra and character orthogonality. The successful output begins `K33_MULTIPATH_EQUIVARIANT_EXACT_PASS`. The accompanying `verification_output.txt` records the actual numerical matrices, critical masks, class traces and multiplicities. In addition to the complete graph-incidence check, the verifier tests every group element on every face and checks the full-group Lefschetz class invariance. These exhaustions are finite proofs for this fixed object, not numerical samples extrapolated to a family.

## Relationship to prior work
A previously established nonequivariant classification gives \(X\simeq\bigvee^{19}S^3\vee\bigvee^{12}S^4\). **That homotopy classification is not a new claim here**; it supplies ranks but cannot determine the automorphism representations or invariant quotient homology. The 2026 work of Caputi, Collari and Smith treats bidirected paths and polygons, not this complete bipartite digraph. Deshpande and Sawant study the equivalent directed-linear-forest formulation and graph-theoretic hypotheses but do not supply this case's full homology characters. An earlier paper by Caputi, Collari, Di Trani and Smith treats complete bipartite digraphs oriented from one part to the other in its Section 3.2; its chessboard-complex result does not cover two arcs for each cross edge. In particular, the ordinary discrete-Morse matching complex of the undirected \(K_{3,3}\) is another, distinct simplicial complex and does not imply the present characters.

## Limitations
The computation classifies a particular six-vertex digraph and its **rational** equivariant homology. It neither provides an integral equivariant module classification nor an integral equivariant homotopy splitting, and does not generalize the characters to \(\overleftrightarrow{K}_{m,n}\) with other parameters. The quotient is only proved rationally homologous to a sphere, not homotopy equivalent to one. Unindexed equivalent literature remains possible. The verification is a reproducible exact calculation, not an independent external audit.

## References
1. Luigi Caputi, Carlo Collari, Jason P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670, first posted January 9, 2026.
2. Priyavrat Deshpande, Rutuja Sawant, *Vertex decomposable complexes of directed forests, conflict graphs and chordality*, arXiv:2602.14936, first posted February 16, 2026.
3. Luigi Caputi, Carlo Collari, Sabino Di Trani, Jason P. Smith, *On the homotopy type of multipath complexes*, 2024, lawful author postprint, https://ntu.eprints-hosting.org/id/eprint/50523/1/1844094_Smih.pdf (especially Sections 2 and 3.2).
