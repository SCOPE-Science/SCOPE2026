# Full octahedral homology representation of the cuboctahedral matching complex

## Finding
Let \(Q_3\) be the graph on binary triples, with edges between words differing in one coordinate. Let \(C=L(Q_3)\), the twelve-vertex, twenty-four-edge cuboctahedral graph. Let \(X=\mathcal M(C)\) be its ordinary matching simplicial complex: vertices of \(X\) are graph edges of \(C\), and faces are disjoint collections of such edges.

The full automorphism group is the hyperoctahedral group \(G=\operatorname{Aut}(C)\cong B_3=C_2\wr S_3\), of order \(48\). The complex has reduced rational homology only in degree three, of rank \(57\). Write \(V_{\alpha,\beta}\) for the rational irreducible of \(B_3\) indexed by an ordered bipartition of total size three. Then the **complete rational homology representation** is
\[
\begin{aligned}
\widetilde H_3(X;\mathbb Q)\cong{}&V_{\varnothing,(3)}\oplus4V_{\varnothing,(2,1)}\oplus2V_{\varnothing,(1,1,1)}\\
&\oplus5V_{(1),(2)}\oplus2V_{(1),(1,1)}\oplus2V_{(2),(1)}\oplus2V_{(1,1),(1)}\\
&\oplus V_{(3),\varnothing}\oplus5V_{(2,1),\varnothing}\oplus2V_{(1,1,1),\varnothing}.
\end{aligned}
\]
The ten irreducible dimensions, in this order, are \(1,2,1,3,3,3,3,1,2,1\). Thus the listed multiplicities account for all \(57\) dimensions. The new claim is the action, not the previously known nonequivariant homotopy type \(X\simeq\bigvee^{57}S^3\).

Let \(z\) be inversion of all three cube coordinates. Its homology trace is \(11\), so the dimensions of its positive and negative eigenspaces are \(34\) and \(23\). There is exactly one \(G\)-fixed rational homology class. In particular,
\[
H^*(|X|/G;\mathbb Q)\cong\mathbb Q[u]/(u^2),\qquad\deg u=3,
\]
which is the rational cohomology ring of \(S^3\). This does not assert any homotopy equivalence between the quotient and \(S^3\).

## Assumptions and scope
Use the cube vertices \(\{0,\dots,7\}\), each identified with its three-bit binary expansion. The twelve edges \(\{v,v\oplus2^i\}\), ordered with smaller endpoint first, label vertices of \(C\). Two vertices of \(C\) are adjacent if their corresponding cube edges share a cube endpoint. Label the twenty-four graph edges of \(C\) lexicographically. They are the vertex labels of \(X\), and a subset is a simplex exactly when its graph edges have pairwise disjoint endpoints.

For \(\sigma\in S_3\) and \(b\in\mathbb F_2^3\), the cube automorphism \(g_{\sigma,b}\) sends a binary word \(x\) to the word whose coordinate \(\sigma(i)\) is \(x_i+b_i\pmod2\). Its induced action on \(C\) and \(X\) is simplicial. For every cycle of \(\sigma\), label its length *positive* if the sum of the corresponding entries of \(b\) is even and *negative* otherwise. The positive and negative cycle-length partitions form the signed-cycle type \((\lambda^+,\lambda^-)\).

For any ordered bipartition \((\alpha,\beta)\) of total size three, put \(a=|\alpha|\) and \(b=|\beta|\). The module \(V_{\alpha,\beta}\) is induced from \(B_a\times B_b\) to \(B_3\) by the outer tensor product of: the inflation of the Specht module \(S^\alpha\) in the first block; and the inflation of \(S^\beta\) twisted by the product-of-coordinate-flips sign character in the second block. This fixes the rational irreducible labeling and its sign convention.

## Proof
**Full symmetry group.** The cubic graph \(Q_3\) is triangle-free. The eight triangles of its line graph \(C\) are precisely the triples of cube edges incident to a given cube vertex: three pairwise incident edges otherwise would form a triangle in \(Q_3\). Each vertex of \(C\) belongs to two of these triangles, encoding the two endpoints of its cube edge. Thus every automorphism of \(C\) reconstructs an automorphism of \(Q_3\). Conversely every cube automorphism acts on \(C\). Cube automorphisms are exactly the eight coordinate translations and six coordinate permutations, so \(\operatorname{Aut}(C)\cong B_3\) and has order \(48\).

**Only one rational homology degree.** The numbers of simplices of cardinalities \(0,1,2,3,4,5,6\), including the empty face, are exactly
\[(1,24,204,744,1116,528,32).\]
An explicit exhaustive mod-two Gaussian elimination of the augmented simplicial boundary maps, in these cardinalities \(1\) through \(6\), gives ranks \((1,23,181,563,496,32)\). Hence the reduced mod-two Betti vector in chain degrees \(-1,0,1,2,3,4,5\) is \((0,0,0,0,57,0,0)\). Rational Betti numbers are bounded above by the corresponding mod-two Betti numbers. The reduced Euler characteristic is
\[-1+24-204+744-1116+528-32=-57,\]
so the only nonzero rational reduced group is \(\widetilde H_3(X;\mathbb Q)\cong\mathbb Q^{57}\). No integral torsion statement is inferred from mod-two elimination.

**Exact Lefschetz character.** Orient a simplex by increasing labels of its graph edges. Let \(t_k(g)\) be the signed count of setwise fixed simplices of cardinality \(k\), where the sign is the parity of the permutation of the \(k\) vertices induced by \(g\). Then the Hopf trace identity on the augmented simplicial chain complex gives the complete rational degree-three character:
\[
\chi_3(g)=1-\sum_{k=1}^6(-1)^{k-1}t_k(g).
\]
Exhaustively applying this formula to all \(48\) automorphisms gives the following class table. The order of the two partitions in each pair is **positive, negative**.

| Signed-cycle type \((\lambda^+,\lambda^-)\) | Class size | \(\chi_3\) |
|---|---:|---:|
| \(((1,1,1),\varnothing)\) | 1 | 57 |
| \(((2,1),\varnothing)\) | 6 | 1 |
| \(((3),\varnothing)\) | 8 | -3 |
| \(((1,1),(1))\) | 3 | -1 |
| \(((2),(1))\) | 6 | 3 |
| \(((1),(2))\) | 6 | -3 |
| \(((1),(1,1))\) | 3 | 13 |
| \((\varnothing,(3))\) | 8 | -1 |
| \((\varnothing,(2,1))\) | 6 | -5 |
| \((\varnothing,(1,1,1))\) | 1 | 11 |

**Irreducible decomposition.** For \((\alpha,\beta)\), the induction character can be calculated without character-table software. Partition the coordinate indices into an invariant set \(A\) of size \(|\alpha|\) and its complement \(B\). Sum over those \(A\) preserved by \(\sigma\) the products of the symmetric-group Specht character \(\chi_\alpha(\sigma|_A)\), the Specht character \(\chi_\beta(\sigma|_B)\), and \((-1)^{\sum_{i\in B}b_i}\). The ten resulting characters have pairwise orthonormal character inner products over the \(48\) automorphisms, and the sum of squared irreducible dimensions equals \(48\). Exact inner products with the displayed \(\chi_3\) give:

| \((\alpha,\beta)\) | Dimension | Multiplicity |
|---|---:|---:|
| \((\varnothing,(3))\) | 1 | 1 |
| \((\varnothing,(2,1))\) | 2 | 4 |
| \((\varnothing,(1,1,1))\) | 1 | 2 |
| \(((1),(2))\) | 3 | 5 |
| \(((1),(1,1))\) | 3 | 2 |
| \(((2),(1))\) | 3 | 2 |
| \(((1,1),(1))\) | 3 | 2 |
| \(((3),\varnothing)\) | 1 | 1 |
| \(((2,1),\varnothing)\) | 2 | 5 |
| \(((1,1,1),\varnothing)\) | 1 | 2 |

The trivial representation is \(V_{(3),\varnothing}\), with multiplicity one; equivalently \(48^{-1}\sum_{g\in G}\chi_3(g)=1\). Central inversion has signed-cycle type \((\varnothing,(1,1,1))\), with trace \(11\); its two eigenspaces therefore have dimensions \((57+11)/2=34\) and \((57-11)/2=23\).

**Orbit-space consequence.** Passing to a barycentric subdivision removes simplex inversions. For a finite group acting simplicially, rational cochains of the ordinary orbit space then identify with invariant rational cochains of the subdivided complex, because averaging over \(G\) is exact in characteristic zero. Hence \(H^*(|X|/G;\mathbb Q)=H^*(|X|;\mathbb Q)^G\). Since the only positive-degree rational cohomology is one invariant line in degree three, its square vanishes for dimensional reasons, giving the stated graded algebra.

## Verification
The attached standard-library script `verify_cuboctahedral_representation.py` constructs the graph from binary cube edges and enumerates faces in two independent ways. It computes all augmented boundary ranks exactly over \(\mathbb F_2\), all ten signed-cycle class characters, and all ten irreducible multiplicities. It checks signed chain-equivariance on \(478{,}080\) ordered face-deletion identities and character orthogonality over all 48 group elements. Run:

```text
python3 verify_cuboctahedral_representation.py
```

The attached `verification_output.txt` records the complete result. The script proves the exhaustive finite statements directly through asserted computations; it does not rely on any external data file.

## Relationship to prior work
Dong and Wachs (2002) establish symmetric-group representation results for the matching complex of the **complete graph**. That setting does not determine the full octahedral action for the noncomplete cuboctahedral graph. Engström (first public 2005) gives general connectivity results for claw-free independence complexes, a setting containing \(X=\operatorname{Ind}(L(C))\), but does not compute this full finite-group representation. Braun and Hough (first public 2016) analyze grid-derived matching complexes through Morse matchings, not this doubled line graph or its symmetry character.

The exact same cuboctahedral matching complex has already been shown to be homotopy equivalent to \(\bigvee^{57}S^3\) in the published result *The cuboctahedral matching complex is a wedge of 57 three-spheres* (October 11, 2026). Its full accessible scientific statement and proof identify the integral homotopy type using an acyclic matching and a unimodular Morse boundary minor, but make no equivariant homology-character or orbit-space cohomology claim. The previously known wedge decomposition is explicitly excluded from the novelty claim. Neither that nonequivariant homotopy type nor the automorphism-group order \(48\) recorded by MathWorld implies the above complete ten-irreducible representation decomposition without additional action data.

The **different** cuboctahedral three-cut complex and two-particle configuration space have separate recorded results; their faces and homology functors do not identify with \(\mathcal M(C)\).

## Limitations
The representation and quotient-ring assertions concern rational coefficients and this one 12-vertex graph. They do not classify the integral representation lattice, integral quotient cohomology, equivariant homotopy type, or matching complexes of all polyhedral line graphs. The computations are complete for the finite labeled graph, not statements about asymptotic families. Unindexed equivalent calculations cannot be ruled out. The present verification is a mathematical derivation plus reproducible finite computation; an independent audit has not been performed.

## References
1. X. Dong and M. L. Wachs, *Combinatorial Laplacian of the Matching Complex*, Electronic Journal of Combinatorics 9 (2002), #R17, publicly available April 2, 2002, https://doi.org/10.37236/1634.
2. A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420v1, first public December 17, 2005, https://arxiv.org/abs/math/0512420.
3. B. Braun and W. K. Hough, *Matching and Independence Complexes Related to Small Grids*, arXiv:1606.01204v1, first public June 3, 2016, https://arxiv.org/abs/1606.01204.
4. *The cuboctahedral matching complex is a wedge of 57 three-spheres*, publicly recorded October 11, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-cuboctahedral-matching-complex-is-a-wedge-of-57-three-sphere--42f20681b118.
5. E. W. Weisstein, *Cuboctahedral Graph*, MathWorld, https://mathworld.wolfram.com/CuboctahedralGraph.html.
