# The Dürer matching complex: an integral sphere wedge and its full dihedral character

## Finding
Let \(G=GP(6,2)\) be the Dürer graph, and let \(K=\mathcal M(G)\) be its **ordinary edge-matching complex**, whose simplicial vertices are the graph edges and whose faces are pairwise vertex-disjoint edge collections. Then
\[
K\simeq \bigvee^{22}S^3.
\]
This is an integral homotopy equivalence, rather than an identification of rational or modular Betti numbers. The full graph automorphism group \(D_6\) acts on \(\widetilde H_3(K;\mathbb Q)\) with character
\[
(\chi(1),\chi(r),\ldots,\chi(r^5))=(22,0,-2,6,-2,0),
\qquad \chi(r^ks)=0\quad(0\le k<6).
\]
Let \(\lambda_{a,b}\) be the one-dimensional representation satisfying \(r\mapsto a\) and \(s\mapsto b\), for \(a,b\in\{1,-1\}\). Let \(V_j\) be the rational two-dimensional representation with \(r\)-eigenvalues \(e^{\pm 2\pi i j/6}\) and reflection trace zero, for \(j=1,2\). Then
\[
\widetilde H_3(K;\mathbb Q)\cong
2\lambda_{1,1}\oplus2\lambda_{1,-1}\oplus\lambda_{-1,1}\oplus\lambda_{-1,-1}
\oplus3V_1\oplus5V_2.
\]
In particular, the globally invariant subspace has dimension \(2\); the half-turn has trace \(6\), and every reflection has trace \(0\).

## Assumptions and scope
The vertex set is \(\{u_i,v_i:i\in\mathbb Z/6\mathbb Z\}\), with the 18 undirected edges \(\{u_i,u_{i+1}\}\), \(\{u_i,v_i\}\), \(\{v_i,v_{i+2}\}\), where indices are modulo \(6\). There are no other edges. The vertices \(u_i\) and \(v_i\) are represented by integers \(i\) and \(6+i\), respectively, in `verify.py`; graph edges are sorted lexicographically. A simplex is an arbitrary nonempty matching, with the empty face included conventionally. The result concerns this graph only, with rational coefficients for the representation and integral homotopy type for the underlying complex.

The transformations \(r:u_i\mapsto u_{i+1}, v_i\mapsto v_{i+1}\) and \(s:u_i\mapsto u_{-i},v_i\mapsto v_{-i}\) generate a group of order \(12\). Exhaustive degree-and-adjacency-preserving permutation backtracking confirms that they give **every** graph automorphism, not only a selected dihedral subgroup.

## Proof
**Finite simplices.** The graph has 12 vertices, 18 edges, and degree three at each vertex. The matching complex has exactly \(1037\) nonempty simplices, in dimensions \(0\) through \(5\) with counts \((18,117,334,402,156,10)\). Two distinct enumeration procedures give these counts: successive insertion of matching-compatible graph edges and a recursive occupation-of-vertices traversal. The Euler characteristic is \(-21\).

**Acyclic discrete matching.** Enumerate the 18 graph edges in lexicographic order and represent a nonempty simplex by its 18-bit indicator mask. At stage \(j\), among the faces not matched in earlier stages, pair every mask \(f\) not containing bit \(j\) with \(f\cup\{j\}\) when the latter is a face that is also unmatched. The 18 stage pair counts are

`[204,103,54,26,14,45,23,10,7,0,11,0,0,0,5,2,1,1]`.

These are \(506\) disjoint face/coface pairs, leaving one critical zero-cell, 23 critical three-cells and one critical four-cell. Orient every codimension-one face-poset edge downwards except the 506 matched edges, which point upwards. The explicit topological sort of the resulting directed graph visits all 1037 simplex nodes and all 3684 covering relations; the matching is acyclic. Forman's theorem gives a homotopy-equivalent CW complex with exactly these critical cells.

**Integral attaching degree.** With simplices oriented by increasing edge indices, the ordinary simplicial boundary is \(\partial(e_{i_0}\wedge\cdots\wedge e_{i_q})=\sum_t(-1)^t(e_{i_0}\wedge\cdots\widehat{e_{i_t}}\cdots\wedge e_{i_q})\). Cancel the 506 matched chain-basis pairs using their integral unit incidence pivots: for a pair \((\ell,h)\), with \(p=[\ell]\partial h=\pm1\), replace each remaining column \(\partial x\) by \(\partial x-([\ell]\partial x)p\,\partial h\), and then delete coordinates \(\ell,h\). The replay verifies all 506 pivots have absolute value one and all coefficients remain integral. On the 25 critical cells, the only nonzero differential is the boundary of the unique four-cell, with two coefficients \(+1\), on the three-cell indicator masks `6408` and `17476`. This primitive boundary gives integral \(\widetilde H_3\cong\mathbb Z^{22}\), with all other reduced homology zero.

Because the Morse CW model has just one zero-cell, 23 three-cells, and one four-cell, its three-skeleton is \(\bigvee^{23}S^3\). The attaching map of the four-cell has homotopy class in \(\pi_3(\bigvee^{23}S^3)\cong\mathbb Z^{23}\), determined exactly by its degree vector. A primitive degree vector extends to an integral basis; the corresponding change of basis is realized by a homotopy self-equivalence of the wedge. Thus the four-cell kills one sphere and leaves \(\bigvee^{22}S^3\).

**Full symmetry character.** For a graph automorphism \(g\), write \(g_E\) for the induced permutation of the 18 simplex vertices (graph edges). The simplicial Lefschetz number is
\[
L(g)=\sum_{\varnothing\ne\sigma\in K,\,g_E\sigma=\sigma}
(-1)^{\dim\sigma}\operatorname{sgn}(g_E|_\sigma).
\]
The complex has rational homology only in degrees zero and three; therefore \(\chi(g)=1-L(g)\). Direct enumeration of the 12 complete graph automorphisms yields \(\chi(r^k)=(22,0,-2,6,-2,0)\) and six zero reflection traces. Taking inner products with the six rational irreducible characters of \(D_6\) gives multiplicities \(2,2,1,1,3,5\) in the order claimed. The character has degree \(22\) and integer nonnegative multiplicities, and its invariant dimension is the multiplicity of \(\lambda_{1,1}\), namely two.

## Verification
Run `python3 verify.py` using Python 3.10 or later, without third-party modules. The verifier constructs the graph from the stated definition, enumerates all faces twice, checks the complete acyclic Morse matching, performs all integral unit-pivot cancellations, enumerates all graph automorphisms independently, checks their generation by \(r,s\), and compares every signed Lefschetz trace with the formula. A second, separately implemented modular boundary-rank checker `rank_independent.py` verifies the ranks of the five positive-dimensional boundary maps as \((17,100,234,146,10)\) modulo each of \(2,3,5\); its recorded output is `rank_output.txt`. This finite-field corroboration is not used as a substitute for the integral unit-pivot proof. The principal recorded output is in `verification_output.txt`. The expected final line is `DURER_MATCHING_EQUIVARIANT_H3_PASS`.

## Relationship to prior work
Forman's discrete Morse theory supplies the homotopy-reduction machinery, but not this graph-specific computation. Marietti and Testa establish a sphere-wedge result for matching complexes of **forests**; the Dürer graph contains cycles and therefore is not covered. Bayer, Jelić Milutinović and Vega prove that matching complexes of **outerplanar** graphs are sphere wedges. Their result does not apply because this 3-regular 3-connected polyhedral graph is not outerplanar (every nontrivial outerplanar graph has a vertex of degree at most two). The latter paper explicitly identifies matching complexes with independence complexes of line graphs, so that equivalent terminology has also been checked. Existing public polyhedral-graph descriptions establish the Dürer graph and its symmetry group, not the above integral homotopy or homology character. Other indexed graph-specific matching-complex calculations concern different underlying graphs; the closest results are discussed in REVIEW.md.

## Limitations
This is a finite, exact classification of one canonical polyhedral graph. It is not a theorem for all generalized Petersen graphs, all cubic graphs, or all well-covered graphs. Rational representation multiplicities do not identify integral group-ring lattices or an equivariant wedge decomposition. The computation and proof are reproducible but have not received independent mathematical review; publication priority remains subject to unindexed literature.

## References
1. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics **134** (1998), 90–145, DOI `10.1006/aima.1997.1650`. Full author text: https://webhomes.maths.ed.ac.uk/~v1ranick/papers/forman5.pdf.
2. M. Marietti and D. Testa, *A Simple Uniform Approach to Complexes Arising from Forests*, arXiv:0705.1461v1, first posted 2007-05-10. https://arxiv.org/abs/0705.1461.
3. M. Bayer, M. Jelić Milutinović, and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601v1, first posted 2024-11-07. https://arxiv.org/abs/2411.04601.
4. SageMath graph generators, `DurerGraph()` examples, https://doc.sagemath.org/html/en/reference/graphs/sage/graphs/generators/smallgraphs.html.
5. E. W. Weisstein, *Dürer Graph*, MathWorld, https://mathworld.wolfram.com/DuererGraph.html.
