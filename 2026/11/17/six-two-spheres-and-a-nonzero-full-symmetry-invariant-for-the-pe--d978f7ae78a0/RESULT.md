# Six two-spheres and a nonzero full-symmetry invariant for the pentagonal-antiprism perfect-matching complex

## Finding
Let \(A\) be the pentagonal-antiprism graph on \(\mathbb Z/10\mathbb Z\), with an undirected edge between two vertices exactly when their cyclic distance is one or two. Let \(X=\mathcal P(A)\) be its *perfect-matching complex*: the vertices of \(X\) are graph edges and its simplices are exactly the edge subsets extendible to a perfect matching of \(A\). There is an integral homotopy equivalence
\[
X\simeq\bigvee^6 S^2.
\]
This is a pure four-dimensional complex with 22 facets, yet its integral reduced homology is supported only in degree two. Consequently \(X\) is not shellable.

Its full graph automorphism group is \(D_{10}=\langle r,s\mid r^{10}=s^2=1,\ srs=r^{-1}\rangle\), with \(r(i)=i+1\) and \(s(i)=-i\). The rational degree-two homology character for \(0\leq k\leq9\) is
\[
\chi(r^k)=(-1)^k+5\mathbf 1_{5\mid k},\qquad
\chi(r^ks)=1+(-1)^k.
\]
More intrinsically, as a rational dihedral module,
\[
\widetilde H_2(X;\mathbb Q)\cong\mathbf1\oplus\alpha\oplus\mathbb Q(\zeta_5),
\]
where \(\alpha(r)=-1\), \(\alpha(s)=1\), and \(r\) and \(s\) act on \(\mathbb Q(\zeta_5)\) respectively by multiplication by \(\zeta_5\) and by complex conjugation. Hence \(\widetilde H_2(X;\mathbb Q)^{D_{10}}\cong\mathbb Q\), and the full geometric quotient has \(\widetilde H_2(|X|/D_{10};\mathbb Q)\cong\mathbb Q\), with all other reduced rational homology zero.

## Assumptions and scope
All graphs are finite, simple, and undirected. Edges of \(A\) are lexicographically ordered by their two endpoints, giving 20 simplicial vertices. Facets of \(X\) are the perfect matchings, each consisting of five graph edges. This differs from the *ordinary matching complex*, which includes pairwise disjoint edge sets whether or not they extend to a perfect matching. The statement is for this single ten-vertex graph and its full dihedral symmetry, not for all antiprisms.

## Proof
**Exhausting the simplices.** Starting with the smallest uncovered graph vertex, match it with each available adjacent vertex and recurse; this enumerates all perfect matchings without repetition. Exactly 22 five-edge perfect matchings result. Taking their subsets gives 457 nonempty simplices, with counts \((20,115,190,110,22)\) in dimensions zero through four. Independently enumerating all pairwise disjoint edge sets gives the ordinary-matching counts \((20,130,310,225,22)\), so extendibility is a substantive constraint.

**A complete acyclic discrete-Morse matching.** Encode a face by the bitmask of its lexicographically indexed graph edges. Begin with the 457 nonempty faces. For pivot edges \(19,18,\ldots,0\) in that order, pair every presently unpaired face \(F\) omitting the pivot with \(F\cup\{e\}\) if both are still unpaired; remove both faces. This deterministic construction yields exactly 224 pairs and leaves one critical zero-face, one critical one-face, and seven critical two-faces. Reversing precisely the 224 matched cover relations in the complete face-poset Hasse diagram, with all other covers directed downward, gives a directed graph with 457 vertices and 1350 arrows. Exhaustive topological sorting visits all 457 vertices, establishing acyclicity rather than assuming it from the experimental output. Forman's theorem supplies a CW model with precisely these nine critical cells.

**Integral attaching degrees and homotopy type.** Orient each simplex by increasing graph-edge index. For a one-face \(e\) paired upward to a two-face \(t\), let \(c=\langle\partial t,e\rangle\in\{\pm1\}\). Replace \(e\) recursively by \(-c\) times the projections of the other terms in \(\partial t\); a critical one-face projects to its basis generator and a one-face paired downward projects to zero. Acyclicity makes the substitutions terminate and provides the exact integer Morse differential. For the seven critical two-faces, in increasing bitmask order \((16516,16576,20544,33028,65800,65824,81922)\), the degree-two to degree-one coefficients are
\[
(-1,-1,0,0,-1,0,0).
\]
In particular, one attaching map goes once around the unique one-cell with degree \(-1\). The subcomplex consisting of the single zero-cell, one-cell and that two-cell is contractible. Collapsing this contractible CW subcomplex is a homotopy equivalence, and every remaining two-cell then attaches to a point. This leaves a wedge of six two-spheres, proving the integral homotopy equivalence, including the absence of torsion.

**Full automorphism group and character.** In \(A\), edges of cyclic distance one lie in two graph triangles, whereas distance-two edges lie in exactly one. Every graph automorphism must therefore preserve the Hamiltonian ten-cycle consisting of distance-one edges. Its automorphism group is \(D_{10}\), and the displayed rotations and reflections realize all 20 elements.

For each \(g\in D_{10}\), evaluate the reduced alternating simplicial-chain trace: the augmented empty face contributes \(-1\), while each nonempty face fixed setwise contributes \((-1)^{\dim F}\) times the sign of the permutation induced by \(g\) on its increasing edge list. Enumerating all 457 faces for each element gives rotation traces \((6,-1,1,-1,1,4,1,-1,1,-1)\) and reflection traces \((2,0,2,0,2,0,2,0,2,0)\), for \(g=r^k\) and \(g=r^ks\), respectively. Since the only nonzero reduced homology lies in even degree two, these Lefschetz numbers are exactly its character traces. The trace of multiplication by \(\zeta_5^k\) on \(\mathbb Q(\zeta_5)\) is four if five divides \(k\), and minus one otherwise; all the reflection-type actions on this four-dimensional summand have trace zero. These trace values, together with the two one-dimensional characters, establish the stated decomposition. Averaging all 20 traces gives invariant rank one. Rational transfer after equivariant barycentric subdivision identifies the quotient's rational homology with invariants.

**Nonshellability.** A pure shellable four-dimensional simplicial complex has reduced integral homology only in top dimension (or none). Here \(\widetilde H_2(X;\mathbb Z)=\mathbb Z^6\), so it cannot be shellable.

## Verification
The accompanying standard-library `verify.py` generates the graph, all perfect matchings and all simplices from definitions; reproduces the 224-pair acyclic matching; checks each of the 1350 Hasse covers and the full directed acyclicity; computes the signed Morse attaching-degree row; and checks all twenty dihedral Lefschetz traces. Its complete output appears in `verification_output.json`, with `MORSE_CERTIFICATE.json` and `SYMMETRY_TABLE.json` supplying the explicit finite data. A separate `direct_check.py` computes independent ordinary simplicial boundary ranks modulo the primes two, three and five, obtaining ranks \((19,96,88,22)\) for the positive boundary maps and Betti vector \((1,0,6,0,0)\) over each field. The integral homotopy conclusion rests on the acyclic matching and unit attaching degree, not merely on the finite-field checks.

## Relationship to prior work
Agarwal and Basak determine the perfect-matching complexes of the cubic Möbius and circular ladder families in 2026 and identify other regular families as natural directions; the present graph is a distinct four-regular antiprism [1]. Chandrakar and Singh analyze polygonal *line* tilings, not this closed antiprism [2], and Bayer, Jelić Milutinović, and Vega study specified honeycomb regions [3]. A published calculation for the *ordinary* matching complex of this same pentagonal antiprism gives \(\bigvee^4S^2\vee\bigvee^8S^3\), which does not imply the extendibility-subcomplex result [5]. A separate calculation for the *hexagonal*-antiprism perfect-matching complex gives \(\bigvee^{19}S^2\) and zero full-dihedral invariant rank; it concerns a different graph [6]. The homotopy and representation claims here are therefore not implied by those closest identified statements.

## Limitations
No formula for antiprisms of arbitrary size, integral group-representation lattice, or equivariant sphere splitting is claimed. Exact finite verification proves this particular graph result, not an infinite-family periodicity statement. Searches and inspection of the identified primary and nearby published works cannot absolutely rule out an unindexed equivalent calculation. Independent external mathematical validation has not been performed.

## References
1. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601 (first posted 2026-08-31), https://arxiv.org/html/2608.30601v2.
2. H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809 (first posted 2024-07-08), https://arxiv.org/html/2407.05809v2.
3. M. Bayer, M. Jelić Milutinović and J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803 (first posted 2022-09-06), https://arxiv.org/abs/2209.02803.
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
5. *Pentagonal-antiprism matching homotopy and its dihedral character*, public mathematical result posted 2026-10-18 (ordinary matching complex of the pentagonal antiprism).
6. *A nineteen-sphere perfect-matching complex on the hexagonal antiprism*, public mathematical result posted 2026-11-08 (perfect-matching complex of the twelve-vertex antiprism).
