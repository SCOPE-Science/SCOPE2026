# The Wagner graph four-cut complex: a two-sphere and its dihedral orientation character

## Finding
Let \(W\) be the Wagner (eight-vertex Möbius-ladder) graph with vertex set \(\mathbb Z/8\mathbb Z\), in which \(i\) is adjacent to \(i+1\), \(i-1\), and \(i+4\), with arithmetic modulo eight. Let \(\Delta_4(W)\) be the **ordinary** four-cut complex: its facets are the complements of four-vertex sets inducing a disconnected subgraph of \(W\). Then

\[
\Delta_4(W)\simeq S^2.
\]

The complex is pure of dimension three and has face vector \((8,28,48,26)\), in dimensions zero through three; hence it is not shellable. The eight cyclic rim edges and four opposite-vertex edges distinguish two intrinsic edge orbits, and the automorphism group is the dihedral group of order sixteen. Under its standard generators \(r(i)=i+1\) and \(s(i)=-i\), the integral second homology is the one-dimensional character

\[
H_2(\Delta_4(W);\mathbb Z)\cong\mathbb Z,\qquad r_*=-1,\qquad s_*=-1.
\]

A primitive integral generator is represented by the oriented boundary of the octahedron on six consecutive vertices, with opposite pairs \(\{0,1\}\), \(\{2,3\}\), and \(\{4,5\}\). In particular the inclusion of this octahedral boundary induces an isomorphism on second integral homology (and, by simple connectivity, a homotopy equivalence).

## Assumptions and scope
All graphs are finite and simple. The ordinary cut complex is distinct from the **total** cut complex, whose complements are independent sets. A face is a subset of a facet; all homology groups use integral coefficients unless specified. The simplicial structure is the abstract complex on the eight vertices, not a hyperplane-cut cubical complex. All statements refer only to the precisely specified graph \(W\) and cut parameter four.

## Proof
**1. Exact facets and dimensions.** There are exactly \(\binom{8}{4}=70\) vertex quadruples. Testing connectivity in each induced graph gives 26 disconnected quadruples. Their complements are the 26 tetrahedral facets. Closing these facets under subsets gives precisely one empty face, eight vertices, 28 edges, 48 triangles, and 26 tetrahedra. The face enumerator and its independent boundary construction are implemented in `verify.py`.

**2. Complete acyclic Morse reduction.** Represent a face by the eight-bit mask \(m=\sum_{i\in\sigma}2^i\). For each pivot vertex \(i=0,1,\ldots,7\), pair currently unmatched faces \(\sigma\) and \(\sigma\cup\{i\}\) when both are present; process faces in increasing mask order. This yields 53 disjoint pairs, leaving precisely a critical vertex (mask 1), two critical triangles (masks 38 and 50), and one critical tetrahedron (mask 180). Directing each matched Hasse edge upward and each unmatched Hasse edge downward produces a directed acyclic graph on all 110 nonempty faces, with 304 cover incidences. The program performs a complete topological-sort check. Reversing the pivot order supplies a second, independently checked acyclic matching of the same critical-cell dimensions.

**3. Integral attaching degree.** Orient each simplex by its increasing list of vertices. Algebraic Morse gradient-path reduction of the boundary of the critical tetrahedron gives the exact integer column \((-1,1)^\mathsf T\) in the ordered critical-triangle basis \((38,50)\). Thus the reduced Morse CW complex has one zero-cell, two two-cells, one three-cell, no one-cells, and a primitive three-cell attaching-degree vector. The two-skeleton is \(S^2\vee S^2\). By the Hurewicz isomorphism \(\pi_2(S^2\vee S^2)\cong\mathbb Z^2\), the attaching map is classified by its degrees. A unimodular change of the two two-sphere generators takes the primitive vector to \((1,0)\), showing that the three-cell cancels one two-sphere up to homotopy. This proves \(\Delta_4(W)\simeq S^2\) over the integers. As a separate certificate, the ordinary simplicial top boundary has a displayed \(26\times26\) minor of determinant \(+1\); the mod-two boundary ranks in degrees one, two and three are \((7,21,26)\).

**4. A primitive geometric sphere.** For each of the eight choices of one vertex from every opposite pair \((0,1),(2,3),(4,5)\), include the corresponding triangle with the alternating orientation determined by the product of the three oriented zero-spheres. These triangles are all faces, and the signed boundary cancels exactly. Projecting this integral cycle through the same acyclic Morse matching gives the critical-triangle coordinate vector \((1,0)\). Modulo the critical three-cell boundary \((-1,1)\), its degree is \(+1\), so it represents a primitive generator. Its inclusion is a homology isomorphism, and both complexes are simply connected; the homology form of Whitehead's theorem gives the asserted homotopy equivalence for this inclusion.

**5. Full dihedral orientation character.** The opposite-vertex chords lie in exactly two four-cycles each, while rim edges lie in exactly one, so every automorphism preserves the rim cycle and the full automorphism group is the dihedral group generated by \(r\) and \(s\). The chain-level Hopf trace formula, with orientation signs on fixed simplices, gives

\[
\operatorname{tr}(r^k\mid H_2)=(-1)^k,\qquad
\operatorname{tr}(r^ks\mid H_2)=(-1)^{k+1}\quad (0\le k<8).
\]

All sixteen permutations, including their graph automorphism property and signed simplex traces, are checked exactly by `verify.py`. Since \(H_2\) has rank one, these traces are the actual integral automorphism actions.

## Verification
Run `python3 verify.py` with only the Python standard library. The program reconstructs the graph, independently enumerates all 70 possible quadruples, lists every face, verifies both directed Morse matchings across 304 Hasse incidences, computes both exact integer Morse boundary columns, checks the primitive octahedral two-cycle, evaluates a \(26\times26\) integer determinant by fraction-free elimination, calculates independent mod-two chain ranks, and checks sixteen signed equivariant traces. `verification_output.txt` is its recorded output. These are exact exhaustive finite checks, not samples. The proof above explains why they establish the stated infinite homotopy claim for this finite CW complex.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced ordinary cut complexes and determined many graph-family homotopy types. Their squared-cycle graph \(C_n^2\) has chords of cyclic length two and is **not** the degree-three Wagner graph, whose added chords have cyclic length four. Their prism-over-a-clique theorem and two-cut theorem likewise do not specialize to the present four-cut complex. Subsequent work on squared paths and rectangular grids does not specialize to this graph either. The published three-cube four-cut calculation concerns a distinct cubic eight-vertex graph, and the total three-cut calculation for the Wagner graph uses a different face rule. These nearby examples contextualize, but do not imply, the present equivariant classification.

## Limitations
No classification for larger Möbius ladders, other values of the cut parameter, or arbitrary cubic graphs is asserted. No equivariant homotopy equivalence of spaces is claimed: the symmetry conclusion describes the induced integral homology representation. The literature comparisons establish best-knowledge originality rather than a proof that no unpublished equivalent result exists. Independent external audit has not been performed.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, first available April 26, 2023, arXiv:2304.13675v1, especially Sections 1, 6 and 7, https://arxiv.org/abs/2304.13675 .
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, first available July 11, 2024, arXiv:2407.08158v1, especially Sections 4–6, https://arxiv.org/abs/2407.08158 .
3. H. Chandrakar, N. R. Hazra, D. Rout and A. Singh, *Topology of total cut complexes and cut complexes of grid graphs*, first available August 14, 2024, arXiv:2408.07646v1, especially Sections 1 and 5, https://arxiv.org/abs/2408.07646 .
