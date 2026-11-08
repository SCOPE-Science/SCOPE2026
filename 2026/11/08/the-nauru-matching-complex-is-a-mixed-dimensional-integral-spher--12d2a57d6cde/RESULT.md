# The Nauru matching complex is a mixed-dimensional integral sphere wedge

## Finding
Let \(G=\operatorname{GP}(12,5)\) be the 24-vertex Nauru graph. Its ordinary matching complex \(\mathcal M(G)\) is homotopy equivalent, over the integers, to
\[
\boxed{\mathcal M(G)\simeq\bigvee^{98}S^7\vee\bigvee^{6}S^8.}
\]
Consequently, \(\widetilde H_7(\mathcal M(G);\mathbb Z)\cong\mathbb Z^{98}\) and \(\widetilde H_8(\mathcal M(G);\mathbb Z)\cong\mathbb Z^6\), with all other reduced integral homology groups zero. In particular there is no integral homology torsion. This classifies ordinary homotopy, not the equivariant homotopy type.

## Assumptions and scope
Let the graph's vertices be \(u_i,v_i\), with \(i\in\mathbb Z/12\mathbb Z\). Its 36 edges are precisely \(\{u_i,u_{i+1}\}\), \(\{u_i,v_i\}\), and \(\{v_i,v_{i+5}\}\) for all 12 values of \(i\). Give these edges indices \(3i,3i+1,3i+2\), respectively. Each simplex of \(\mathcal M(G)\) consists of pairwise vertex-disjoint graph edges, independently of how the graph itself may be embedded on a surface. No assertion is made for all generalized Petersen graphs, a different graph complex, or rational homology alone.

## Proof
**Finite exhaustion.** A recursive binary decision on each of the 36 edges enumerates every subset once, excluding an edge precisely when an endpoint is already occupied. The numbers of matchings of cardinalities zero through twelve are
\[
(1,36,558,4884,26613,93888,216228,320256,293436,155024,41832,4608,120).
\]
Their sum is \(1{,}157{,}484\), including the empty simplex, and the reduced Euler characteristic is \(-92\). An independent recursion on subsets of the 24 graph vertices derives the same polynomial by the deletion–matching identity, without enumerating edge subsets.

**Complete discrete-Morse matching.** On the augmented face poset, repeatedly consider each indexed graph edge \(e\) in order zero through thirty-five. Among the faces still unpaired, pair every nonempty face \(\sigma\) not containing \(e\) to \(\sigma\cup\{e\}\) if that coface exists and remains unpaired, deleting both from further stages. This produces exactly 578,655 disjoint Hasse pairs and leaves precisely one empty face, one critical vertex, 132 critical seven-simplices and 40 critical eight-simplices. (The empty face is kept as an unpaired augmentation and is not a CW cell.) The full directed Hasse diagram, with matched incidences upward and all others downward, has exactly \(8{,}344{,}008\) arcs. A complete topological sort visits all \(1{,}157{,}484\) faces, hence the matching is acyclic. The standard discrete-Morse construction therefore gives a CW complex with one zero-cell, 132 seven-cells and 40 eight-cells, and no cells in other dimensions.

**Integral boundary.** Orient every simplex by increasing edge index. The boundary of an oriented simplex is the usual alternating sum of its codimension-one faces. For a matched pair \(t\subset s\) of dimensions seven and eight, the coefficient of \(t\) in \(\partial s\) is \(+1\) or \(-1\). Use its boundary relation to eliminate \(t\) integrally; the acyclic gradient relation gives a terminating recursion. Apply these eliminations to the boundary of every critical eight-simplex. In the ascending order of critical bitmasks, the resulting signed Morse boundary is the explicit integer \(132\times40\) matrix `morse_boundary.txt`. It has 336 nonzero entries with absolute value at most two. Exact Smith normal form over \(\mathbb Z\) has 34 diagonal unit factors and six remaining zero diagonal factors. The file `morse_certificate.cpp` regenerates that exact matrix, the complete matching, and the Hasse-DAG check; `verify.py` tests the matrix bytes and independently computes the Smith form.

**Homotopy classification.** The seven-skeleton of the resulting CW complex is a wedge of 132 seven-spheres. Since \(\pi_7(\bigvee^{132}S^7)\cong\mathbb Z^{132}\), the attaching map of each eight-cell is determined by its degree vector. Unimodular changes of cellular bases are realized by self-homotopy equivalences of the wedge and changes of attaching-cell bases. The 34 unit Smith factors each yield a contractible seven/eight-cell pair, while the other six eight-cells attach nullhomotopically. The remaining 98 seven-spheres and six eight-spheres give precisely the asserted homotopy equivalence. Neither reduction modulo a prime nor the Euler characteristic alone would establish this integral homotopy statement.

## Verification
In one directory containing `morse_certificate.cpp`, `morse_boundary.txt`, and `verify.py`, run `python3 verify.py`. The verifier requires GNU `g++` with C++17 support and SymPy (for exact integer Smith normal form). It independently computes the matching polynomial from the vertex-deletion recurrence, compiles and runs the C++ executable in a temporary directory, checks complete face enumeration and full Hasse acyclicity, compares the generated oriented Morse boundary byte-for-byte against `morse_boundary.txt`, and checks its exact Smith form. Integer-overflow checks are included in the integral gradient and boundary accumulations. The expected literal output is included in `verification_output.txt`; successful execution ends with `NAURU_HOMOTOPY_WEDGE_PASS: 98 S7 plus 6 S8`.

## Relationship to prior work
Wachs surveys matching-complex topology, with the standard complete-graph matching and complete-bipartite chessboard complexes as central cases; the inspected material does not compute this 36-edge Nauru-specific complex. Marietti and Testa give an integral sphere-wedge theorem for matching complexes of *forests*, not cyclic generalized Petersen graphs. Bayer, Jelić Milutinović, and Vega prove a result for *outerplanar* graphs, whereas the Nauru graph is nonplanar. These are motivating methods and relevant stronger-sounding classes, but their hypotheses do not cover this object.

Two especially close published mathematical calculations were inspected in full. The Nauru *vertex-independence* complex has integral homotopy \(\bigvee^4S^5\vee S^6\); its simplices are independent vertex sets, not matchings of graph edges. The Desargues \(\operatorname{GP}(10,3)\) *matching* complex has \(\bigvee^5S^5\vee\bigvee^{45}S^6\), but a different graph and no statement for all generalized Petersen parameters. Neither statement implies the present \(\operatorname{GP}(12,5)\) result. Literature and record searches included the Nauru, order-four permutation-star, generalized-Petersen, and line-graph independence formulations, and direct exact-multiplicity searches; no equivalent or dominating claim was found in the inspected sources. This is not proof that inaccessible, unindexed or unpublished equivalents do not exist.

## Limitations
The computation is exhaustive but finite and specific to this graph. Every key nonstandard step relies on replay of the deterministic full-face Hasse check and exact signed integral boundary, not just an asserted rank. It establishes no family-wide classification, symmetry representation or equivariant homotopy splitting. The standard discrete-Morse correspondence and the fact that maps from a seven-sphere to a wedge of seven-spheres are classified by degree are used. A coincident unindexed calculation remains an originality risk. Independent mathematical validation has not been performed.

## References
1. M. L. Wachs, *Topology of matching, chessboard, and general bounded degree graph complexes*, Algebra Universalis 49 (2003), 345–385, DOI:10.1007/s00012-003-1825-1; public date 2003-10-01; https://www.math.miami.edu/~wachs/papers/tmc.pdf.
2. M. Marietti and D. Testa, *A uniform approach to complexes arising from forests*, arXiv:0705.1461v1 (2007-05-10), especially the matching-complex theorem for forests; https://arxiv.org/pdf/0705.1461.
3. M. Bayer, M. Jelić Milutinović and M. Vega, *Matching complexes of outerplanar graphs are contractible or wedges of spheres*, arXiv:2411.04601v1 (2024-11-07), Theorem 2; https://arxiv.org/pdf/2411.04601.
4. *The Nauru independence complex is \(\bigvee^4 S^5\vee S^6\)*, public scientific record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-nauru-independence-complex-is-bigvee-4-s-5-vee-s-6--7c319734d8d8.
5. *The Desargues matching complex is a mixed-dimensional wedge of spheres*, public scientific record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-desargues-matching-complex-is-a-mixed-dimensional-wedge-of-s--67ff1e627721.
6. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
