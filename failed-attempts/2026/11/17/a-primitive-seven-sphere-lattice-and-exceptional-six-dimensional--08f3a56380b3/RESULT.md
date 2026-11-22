# A primitive seven-sphere lattice and exceptional six-dimensional Fano matroid homology

## Finding

Let \(F_7\) be the rank-three Fano vector matroid. Its independence complex \(K=\operatorname{Ind}(F_7)\) has integral reduced homology only in degree two, where it is \(\mathbb Z^{13}\). Every projective line \(L\) has a four-point complement \(Q_L\) spanning the entire boundary of a tetrahedron inside \(K\). These seven tetrahedral boundary cycles are, up to orientation, **all primitive** nonzero integral two-cycles of minimum support (four triangles); every nonzero cycle with that support is an integer multiple of one of them. Their supports partition the 28 triangular facets. They span a saturated, symmetry-stable rank-seven lattice \(\Lambda\) in the integral top homology, and

\[
\widetilde H_2(K;\mathbb Z)/\Lambda\cong\mathbb Z^6.
\]

Under the full automorphism group \(G=\operatorname{GL}_3(\mathbb F_2)\), of order 168, the rational top homology splits into an absolutely irreducible seven-dimensional geometric summand and a rationally irreducible six-dimensional quotient. The latter complexifies as the sum of the two Galois-conjugate three-dimensional irreducibles of \(G\). With classes ordered by element orders \((1,2,3,4,7,7)\), the respective characters are

\[
\begin{aligned}
\chi_{\mathrm{all}}&=(13,-3,1,1,-1,-1),\\
\chi_{\mathrm{geom}}&=(7,-1,1,-1,0,0),\\
\chi_{\mathrm{quot}}&=(6,-2,0,2,-1,-1).
\end{aligned}
\]

The associated class sizes are \((1,21,56,42,24,24)\). In particular, the geometrically canonical seven shortest-support spheres account for only seven of the thirteen homology directions; the other six directions carry an exceptional representation.

## Assumptions and scope

Identify the seven vertices \(P\) with \(\mathbb F_2^3\setminus\{0\}\). A Fano line is \(\{a,b,a+b\}\) for distinct nonzero vectors. A face of \(K\) is an independent subset: all vertices, all pairs, and precisely those three-subsets that are not lines. There are no faces of cardinality greater than three. Orient a simplex by increasing integer encoding of its vertices and use the usual alternating simplicial boundary. For a line \(L\), write \(Q_L=P\setminus L\) and \(z_L=\partial[Q_L]\), where the bracket is the formal oriented four-vertex simplex in the ambient simplex (not a face of \(K\)). The four triangles occurring in \(z_L\) all belong to \(K\).

The claim concerns ordinary reduced integral homology, the specified primitive sublattice and the ordinary rational \(G\)-representation. No splitting of the corresponding short exact sequence of **integral group modules** is claimed. The representation does split over \(\mathbb Q\) by semisimplicity.

## Proof

**Step 1: the seven canonical spheres partition the facets.** Every line intersects every other projective line. Thus a three-subset of \(Q_L\) cannot be a line, so all four triangular faces of the formal tetrahedron \([Q_L]\) belong to \(K\). Every independent triple \(T\) is disjoint from exactly one Fano line. Indeed, the three points lie on nine lines counted with multiplicity, and the three lines through the three pairs each contribute one double count; as \(T\) is not itself a line, exactly six of the seven lines meet \(T\). Hence its remaining line is disjoint. Thus the 28 triangles partition into seven disjoint four-triangle blocks, one per \(Q_L\).

**Step 2: integral homology.** The complex has seven vertices, 21 edges and 28 triangles. Its one-skeleton is complete. An oriented boundary of a triangle that is a missing line can be expressed as an integral combination of the three independent-triangle boundaries obtained by adjoining a point outside the line: apply the formal tetrahedron boundary identity. Together with the existing independent triangles, these generate the full one-cycle lattice of the complete graph. Therefore \(H_1(K;\mathbb Z)=0\) and the triangular boundary matrix has rank \(21-7+1=15\). As there are no three-faces, \(\widetilde H_2(K;\mathbb Z)=\ker\partial_2\cong\mathbb Z^{28-15}=\mathbb Z^{13}\), with all other reduced homology zero. Matroid shellability also gives the nonequivariant sphere-wedge interpretation; it is not the novel part of the result.

**Step 3: minimum cycles and saturated geometric sublattice.** Let a nonzero integral two-cycle have support at most four triangles. Every edge in any supported triangle must occur in at least one other supported triangle, to cancel its coefficient in the boundary. Starting from a supported triangle on \(a,b,c\), the three neighboring triangles forced to share its three edges must all use the same fourth vertex \(d\); otherwise one of their remaining edges is unpaired among four triangles. Thus four triangles constitute exactly the boundary of a tetrahedron, and the boundary equations force equal absolute coefficients. There is no nonzero cycle with fewer than four triangular faces. For the Fano matroid, the four-subsets whose every triple is independent are exactly the seven complements of lines: given any independent triple \(\{a,b,c\}\), the possible fourth vectors outside it are \(a+b\), \(a+c\), \(b+c\) and \(a+b+c\). Only the last choice avoids creating a three-point line. It therefore yields the unique four-cap extending that triple, already identified as the complement of its unique disjoint line. Hence the \(z_L\), up to sign, are exactly the primitive minimum-support cycles; every other integral cycle of the same minimum support is an integer multiple of one of them.

Each of the seven columns \(z_L\) has its own disjoint block of four nonzero integral coordinates in \(C_2(K;\mathbb Z)\). Selecting one face-coordinate from each block yields a \(7\)-by-\(7\) diagonal minor with entries \(\pm1\). Consequently the subgroup \(\Lambda\) spanned by these columns is a primitive direct summand of \(C_2(K;\mathbb Z)\). Since \(\Lambda\subset\ker\partial_2\subset C_2(K;\mathbb Z)\), the quotient \(\ker\partial_2/\Lambda\) embeds in a torsion-free group and is itself free; its rank is \(13-7=6\). Thus the claimed integral quotient follows without a rational-to-integral inference.

**Step 4: full homology character.** The linear group permutes all seven lines and their complementary tetrahedra, carrying \(z_L\) to the oriented sign of the induced four-point permutation times \(z_{gL}\). Thus \(\Lambda\) is stable and has signed-permutation character equal to the sum of the orientation signs of fixed complements. Since reduced homology occurs only in degree two, the cellular Lefschetz identity for every \(g\in G\) reads

\[
\operatorname{tr}(g\mid\widetilde H_2)=
\operatorname{tr}(g\mid C_0)-\operatorname{tr}(g\mid C_1)+
\operatorname{tr}(g\mid C_2)-1.
\]

Here the chain traces are signed counts of fixed oriented vertices, edges and independent triangles. Enumerating the invertible three-by-three matrices over \(\mathbb F_2\) gives six conjugacy classes with sizes \((1,21,56,42,24,24)\). The resulting full and geometric characters, and their difference, are the three rows displayed above. This uses finite sums over all 168 transformations, with the exact executable verifier providing each chain-map and trace check.

**Step 5: identify the irreducibles.** The standard character table for \(G\cong\operatorname{PSL}_2(7)\), in the same class ordering, contains the absolutely irreducible seven-dimensional row \((7,-1,1,-1,0,0)\) and the conjugate pair of three-dimensional rows whose sum is \((6,-2,0,2,-1,-1)\). The first has character norm one; the second has character norm two and is orthogonal to the first. Its two complex constituents form one Galois orbit and hence define an irreducible module over \(\mathbb Q\). Maschke's theorem completes the claimed rational direct-sum decomposition. The full module has no invariant rational line, as its character average is zero.

## Verification

`verify_fano.py` uses Python 3 and SymPy, with exact integer and rational arithmetic. It builds all seven points and lines, all 28 independent triangular faces, all 168 group transformations, all six conjugacy classes, and the seven geometric two-cycles. It checks the rank-15 signed boundary, zero first integral homology by the missing-line filling argument, a unimodular \(7\)-by-\(7\) cycle-coordinate minor, exhaustive minimum mod-two supports through size four, and equivariance of the chain maps and geometric sublattice under all group elements. For each class, a second method explicitly acts on a rational basis of \(\ker\partial_2\), confirming the signed Lefschetz trace. Output is reproduced in `verification_output.txt`.

Exhaustive finite tests here serve as complete computations on this finite complex, not as proofs of general results for larger projective geometries. The integer saturation claim follows separately from the displayed disjoint-support integral coordinate argument. Mod-two minimum-support enumeration is a cross-check on, not a replacement for, the integral support proof.

## Relationship to prior work

The Fano matroid and its seven lines are classical; the cited 2015 exposition publicly states their exact independence structure. Matroid shellability establishes the known general nonequivariant top-homology concentration. Moci–Pezzoli give general descriptions of automorphism representations on matroid independence homology, using duality and lattices of flats, but the inspected introduction, main theorem statements and detailed examples do not determine this particular Fano character, the seven shortest-support oriented cycles, or their saturated integral lattice. The standard \(\operatorname{PSL}_2(7)\) character table identifies the two constituents after the actual homology character has been calculated; the table alone does not imply which constituents occur.

The distinction from the automorphism representation of the Heawood **graph** independence or matching complex is structural: those are simplicial complexes on graph-independent sets or edge matchings, not on the seven vector-matroid independent sets. Similar geometric-cycle questions over other finite projective planes likewise do not determine the saturated Fano rank-seven submodule or its exceptional six-dimensional quotient.

## Limitations

The calculation concerns the binary seven-point rank-three matroid and its full linear collineation group only. It does not determine an integral equivariant splitting of the two summands, a cohomology-ring description of all quotients, or a uniform formula in the order of the projective plane. A mathematically equivalent formulation in unindexed literature remains possible. The scientific verification and literature comparison are not an independent audit.

## References

1. M. Baker, *A Celebration of Independence*, July 4, 2015, https://mattbaker.blog/2015/07/04/a-celebration-of-independence/ (Fano matroid and line structure).
2. A. Björner, *Topological Methods*, in *Handbook of Combinatorics* (1995), matroid independence shellability and top homology.
3. L. Moci and G. Pezzoli, *Representations of automorphism groups on the homology of matroids*, arXiv:2001.03760 (2020), https://arxiv.org/abs/2001.03760.
4. The standard \(\operatorname{PSL}_2(7)\) character table and conjugacy-class data, https://en.wikipedia.org/wiki/PSL(2,7).
5. Polymake documentation, *Matroid*, https://polymake.org/doku.php/documentation/matroid/matroid (Fano matroid as a standard example).
