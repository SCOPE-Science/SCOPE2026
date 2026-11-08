# Four two-spheres in the Fano-polarity fixed locus of the Heawood matching complex

## Finding
Let \(H\) be the fourteen-vertex Heawood graph, represented as the incidence graph of the Fano projective plane. Label its points \(p_a\) and lines \(L_b\) by the seven nonzero elements \(a,b\) of \(\mathbb F_2^3\). An incidence \(p_aL_b\) is an edge exactly when the standard binary dot product satisfies \(a\cdot b=0\). The orthogonal polarity \(\tau\) exchanges \(p_a\) with \(L_a\); this is an order-two graph automorphism. Write \(\mathcal M(H)\) for the **ordinary** matching complex of all disjoint graph-edge collections, not the extendible-to-perfect-matching subcomplex.

Then the geometric fixed-point space has the integral homotopy type
\[
\boxed{\left|\mathcal M(H)\right|^{\langle\tau\rangle}\simeq\bigvee^4 S^2.}
\]
Consequently its reduced integral homology is \(\mathbb Z^4\) in dimension two and zero in every other dimension; in particular, its fundamental group is trivial and it has no integral homology torsion.

## Assumptions and scope
Use integers \(1,\ldots,7\) to encode nonzero three-bit vectors; binary dot products are computed modulo two. The chosen polarity is precisely \(\tau(p_a)=L_a\) and \(\tau(L_b)=p_b\). Since the incidence condition is symmetric, \(\tau\) preserves all graph edges. Geometric fixed points are taken **after realization** of the matching complex: vertices of the fixed-space model may be barycenters of two-element orbits of original matching-complex vertices.

The calculation is for this explicitly defined Fano polarity, not for arbitrary graph automorphisms. The complex is finite, and all chain groups and Morse matchings are over the integral simplicial face poset unless a field is explicitly stated for an independent check.

## Proof
**1. Model for geometric fixed points.** If a finite group permutes vertices of a simplicial complex \(K\), a point of \(|K|\) is fixed exactly when its barycentric coordinates are constant on every group orbit. Its support must therefore be a union of complete vertex orbits. On each allowable orbit, its fixed coordinates give a single orbit-barycenter coordinate. The convex pieces glue simplicially, yielding an explicit PL homeomorphism from the geometric fixed-point set to the orbit simplicial complex whose faces are collections of orbits with union a face of \(K\).

Here the vertices of \(\mathcal M(H)\) are the twenty-one incidences \((a,b)\) with \(a\cdot b=0\). The polarity maps the incidence \((a,b)\) to \((b,a)\). For \(a\ne b\), these are two disjoint graph edges; for \(a=b\), the edge is fixed. Every edge orbit is therefore individually an admissible vertex of the fixed model.

Identify the orbit \(\{(a,b),(b,a)\}\) with the unordered pair \(\{a,b\}\), and the singleton orbit \(\{(a,a)\}\) with a loop at label \(a\). Two such orbits can occur in one matching exactly when their underlying label supports are disjoint: the orbit associated with \(\{a,b\}\) occupies the point and line vertices with those labels. Thus the fixed model is the matching-type complex of a seven-label looped graph whose permitted unordered pairs (loops included) are exactly the orthogonal pairs. In lexicographic order they are

`(1,2), (1,4), (1,6), (2,4), (2,5), (3,3), (3,4), (3,7), (5,5), (5,7), (6,6), (6,7)`.

The ordered pairs with equal entries are loops in this auxiliary combinatorial model; they represent ordinary fixed edges of the original simple Heawood graph, not loop edges of \(H\).

**2. Complete face poset.** Index these twelve auxiliary edges from zero through eleven in the displayed order. A face is a set of indices whose label supports are pairwise disjoint. Exhaustively choosing such collections gives exactly \(138\) faces, including the empty face, with nonempty face vector \((12,45,59,21)\). The standalone checker also constructs every matching of the original twenty-one Heawood edges, obtains \(3462\) faces including the empty face, and verifies that its \(138\) polarity-invariant faces agree **exactly** with the unions of these orbit-model faces. This independently verifies the fixed-space identification.

**3. Complete acyclic discrete-Morse matching.** On the \(137\) nonempty faces of the orbit model, perform the following deterministic staged element matching. Initially every face is unmatched. Process the auxiliary vertex indices in the order

`[5,10,4,11,6,2,8,1,0,3,7,9]`.

At index \(j\), pair each currently unmatched face not containing \(j\) with its enlargement by \(j\), provided both faces are still unmatched. At every stage process remaining faces by increasing size and then lexicographically. This produces exactly \(66\) matching pairs and leaves precisely the five critical faces

`(5), (2,6,9), (2,7,8), (2,6,8), (6,8,11)`.

Every listed pair is a codimension-one face inclusion, and every face belongs to at most one pair. Acyclicity, the nonstandard essential point, is established by checking the **complete** nonempty face-poset Hasse diagram: its \(351\) cover relations are directed downwards except that all \(66\) matched arrows are reversed. The standalone certificate checker builds every one of these relations and performs Kahn's algorithm. All \(137\) faces are visited in a valid directed topological ordering, so no directed cycle exists. The check is exhaustive and finite, not a sampled search or a claim inferred from unsuccessful cycle detection.

Forman's discrete Morse theorem gives a CW complex homotopy equivalent to the fixed model with exactly one zero-cell and four two-cells, and no cells in any other dimension. Each two-cell attaches to a point because there are no one-cells. Hence the CW complex is exactly a wedge of four two-spheres. This proves the integral homotopy type and all asserted homological consequences.

## Verification
Place `verify_polarity.py` and `morse_certificate.json` in one directory and run `python3 verify_polarity.py` with Python 3.10 or later. No third-party modules are required. The checker independently enumerates the original incidence-graph matchings and the orbit-model faces; compares the invariant-original-face set with the expanded orbit-face set; reconstructs all \(66\) matched pairs and the five critical faces; checks every \(351\) nonempty Hasse relation and global acyclicity; and separately computes reduced mod-two homology using exact bit-vector Gaussian elimination. The nonempty face vector is \((12,45,59,21)\), and the mod-two boundary ranks in dimensions one through three are \((11,34,21)\). The resulting reduced mod-two Betti numbers are \((0,0,4,0)\), consistent with the stronger integral Morse conclusion. The successful marker is `POLARITY_HEAWOOD_FIXED_MORSE_OK`.

## Relationship to prior work
A 2026 study by Agarwal and Basak determines ordinary independence and **perfect-matching** complex homotopy types for Möbius and circular ladder graphs. Its main theorems, read in the accessible full text, do not concern the Heawood graph or geometric point-line-polarity fixed sets. The natural graph and group here differ from those families.

A separate publicly accessible Heawood calculation gives \(\mathcal M(H)\simeq\bigvee^{16}S^4\) for the entire ordinary matching complex (report 7150930ba12a). Another determines its complete **rational homology representation** under all \(336\) automorphisms (report d7a042784870). In the latter, the character of a point-line-exchanging involution on reduced fourth homology is \(4\). By Lefschetz theory that fixes the Euler characteristic of its geometric fixed space at \(5\), but it does **not** determine the fixed space's integral homotopy type, the dimension or torsion of its homology, or its fundamental group. The present result computes the geometric fixed space itself and gives \(\chi=1+4=5\), consistent with—but not implied by—that trace calculation.

The previously determined Heawood **perfect-matching** complex has type \(\bigvee^{16}S^2\) (report 0994476b8c0d), but it is a different simplicial complex, and the homotopy type of a subcomplex does not determine this fixed space of the ordinary complex. The literature and mathematical-record searches recorded in `AUDIT.json` found no equivalent geometric fixed-space classification. Failure to find one is not a proof of absolute historical novelty.

## Limitations
The claim concerns the chosen polarity of the fourteen-vertex Heawood graph. It does not classify all involutions, point-line dualities of arbitrary projective planes, symmetry quotients, or the complete equivariant homotopy type. The proof is finite and computer-assisted: the exhaustive verifier is part of the argument. The independently computed mod-two ranks alone would not prove the integral wedge decomposition. An equivalent unpublished or differently indexed fixed-space computation remains possible.

## References
1. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601v1, first public 2026-08-31 (subsequent v2 2026-09-14).
2. *The Heawood matching complex is a wedge of sixteen 4-spheres*, public mathematical report 7150930ba12a (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-heawood-matching-complex-is-a-wedge-of-sixteen-4-spheres--7150930ba12a.
3. *Full \(\operatorname{Aut}(H)\)-module of the Heawood matching complex*, public mathematical report d7a042784870 (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-full-operatorname-aut-h-module-of-the-heawood-matching-complex--d7a042784870.
4. *Perfect Morse reduction of the Heawood perfect-matching complex*, public mathematical report 0994476b8c0d (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-perfect-morse-reduction-of-the-heawood-perfect-matching-complex--0994476b8c0d.
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
