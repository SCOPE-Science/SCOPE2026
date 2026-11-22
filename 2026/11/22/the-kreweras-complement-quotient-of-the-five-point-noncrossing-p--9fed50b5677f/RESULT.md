# The Kreweras-complement quotient of the five-point noncrossing partition complex is a five-torsion Moore space

## Finding

Let \(\mathrm{NC}_5\) be the lattice of noncrossing set partitions of five vertices of a convex pentagon, ordered by refinement, and let \(K=\Delta(\mathrm{NC}_5\setminus\{\hat0,\hat1\})\) be the order complex of its proper part. The right Kreweras complement generates a cyclic group of order ten on the geometric realization. The *ordinary geometric orbit space* has the exact homotopy type

\[
|K|/\langle\kappa\rangle\simeq M(\mathbb Z/5\mathbb Z,1)
= S^1\cup_{\deg 5}e^2.
\]

Consequently \(\pi_1(|K|/\langle\kappa\rangle)\cong\mathbb Z/5\mathbb Z\), and its integral homology is \(H_0\cong\mathbb Z\), \(H_1\cong\mathbb Z/5\mathbb Z\), and \(H_i=0\) for all \(i\ge2\). This is a homotopy statement, not merely a computation of cellular homology or rational invariants.

## Assumptions and scope

Write the vertices as \(0,1,2,3,4\) in counterclockwise cyclic order. A partition is noncrossing if no distinct blocks contain alternating vertices \(a,b,c,d\) with \(a<b<c<d\), \(a,c\) in the first block and \(b,d\) in the second. Remove both the discrete and indiscrete partitions. For a noncrossing partition \(\pi\), form a permutation \(w_\pi\) by writing each block as a cycle in increasing order and multiplying the disjoint cycles. Let \(c=(0\;1\;2\;3\;4)\), and define \(\kappa(\pi)\) by the cycle partition of \(w_\pi^{-1}c\).

This complement is an order-reversing lattice bijection. Its square is label rotation by one step in the inverse direction: \(\kappa^2(w)=c^{-1}wc\). The original complex has dimension two and is a wedge of fourteen two-spheres by the classical shellability/homology theorem. Here the action of \(\kappa\) is not assumed free: fixed cells are treated exactly.

## Proof

**1. The original finite poset.** Enumerate all set partitions of the five labels by inserting the minimum label into each possible block or creating a singleton block. Retain those satisfying the four-vertex noncrossing test, discarding the two extremes. This gives forty proper partitions: ten of rank one, twenty of rank two, and ten of rank three. Strict refinement chains give \(40\) vertices, \(150\) edges and \(125\) triangular faces of \(K\). A direct inverse-permutation computation checks that \(\kappa\) permutes this set, interchanges ranks one and three, fixes rank two as a set, reverses refinement, and has order ten.

**2. A stabilizer-correct orbit complex.** Take the barycentric subdivision \(\operatorname{sd}K\). Its vertices are nonempty faces of \(K\); its edges and triangles are strictly increasing inclusion flags of two and three nonempty faces. There are, respectively, \(315\), \(1050\), and \(750\) such simplices. Since \(\kappa\) preserves the cardinality of a face of \(K\), it preserves each rank of an inclusion flag. Thus every group element that stabilizes a simplex of \(\operatorname{sd}K\) fixes each vertex of that simplex; there are no inversions. The simplex-orbit cells therefore form an exact delta-complex for \(|K|/\langle\kappa\rangle\), with \(36\) vertices, \(110\) oriented edges and \(75\) oriented triangles. Parallel edges and fixed simplices are retained as distinct orbit cells where appropriate. Its Euler characteristic is one.

**3. The attaching words.** Index each orbit simplex by the lexicographically least representative of its ten complement iterates. Orient every subdivided edge by increasing face size. For an oriented triangle flag \((A\subset B\subset C)\), its attaching word follows \((A,B)(B,C)(A,C)^{-1}\). Use the deterministic first-available union–find spanning tree from the 110 indexed edges; it has 35 edges. Contracting it yields a single zero-cell, 75 loop edges, and 75 triangle attaching words in a free group on 75 generators. This contraction is a homotopy equivalence.

**4. Exact homotopy cancellations.** In an oriented cellular two-complex, if a two-cell attaching word contains some loop generator exactly once (with exponent \(\pm1\)), then that two-cell and generator can be removed by substituting the defining word into every other attaching map. This is a homotopy equivalence of two-complexes, stronger than abelian chain reduction. The supplied `cancellation_certificate.json` lists 74 such successive pairs by the canonical orbit-cell indices, and `verify.py` reconstructs the full initial presentation and validates each unique occurrence and each substitution. After these 74 cancellations, one loop generator and one two-cell remain, and the final attaching word is the fifth power of that generator, with no other cells. This is precisely \(S^1\cup_{\deg5}e^2\). Its integral homotopy and homology follow immediately.

## Verification

The standalone Python 3 verifier uses the standard library and recreates the forty proper noncrossing partitions, both chain complexes, every complement iterate, every orbit simplex and attaching map, the exact spanning tree and the complete cancellation sequence. It reads the accompanying JSON certificate, checks it against the independently reconstructed canonical sequence, and checks the terminal five-letter attaching word. Running `python3 verify.py` in the directory containing the certificate prints `KREWERAS_NC5_QUOTIENT_MOORE5_OK`.

A separate modular boundary calculation using the same orbit cells found chain-map ranks \((35,75)\) in characteristics two, three, seven and 101, and \((35,74)\) in characteristic five. Thus the mod-five homology has one class in each of degrees one and two, as expected; this secondary computation is not used in place of the homotopy proof.

## Relationship to prior work

Bessis and Reiner establish cyclic sieving for conjugation of noncrossing partitions, which counts fixed points but does not compute the homotopy type of a geometric quotient. Kenny proves the nonequivariant sphere-wedge homotopy structure for the proper noncrossing-partition complex. Armstrong–Stump–Thomas analyze Kreweras complementation and its cyclic sieving, and Heitsch counts its individual orbits through plane trees. Their enumerative conclusions do not determine the attaching maps of the quotient cell complex. A separate computation of fivefold rotation and pentagonal dihedral relabeling quotients concerns distinct group actions. Kreweras complementation has order ten but is *not* a pentagonal reflection: its square is rotation, and its odd powers reverse poset order. The extra action eliminates the two free two-sphere summands present in the rotation quotient.

## Limitations

The theorem treats the five-point classical type-A noncrossing lattice and ordinary geometric orbits under the full cyclic complement group. It does not assert an infinite-size formula, equivariant homotopy equivalences, or a classification of intermediate complement-power quotients. The exact finite computational certificate enumerates the complete finite object for this one parameter only, not any unbounded case. Priority against inaccessible or unindexed equivalent literature is not certified independently.

## References

1. David Bessis and Victor Reiner, *Cyclic sieving of noncrossing partitions for complex reflection groups* (2007). https://arxiv.org/abs/math/0701792
2. Aisling Kenny, *Geometrically Constructed Bases for Homology of Non-Crossing Partition Lattices* (2008). https://arxiv.org/abs/0806.4151
3. Drew Armstrong, Christian Stump and Hugh Thomas, *A uniform bijection between nonnesting and noncrossing partitions* (2011). https://arxiv.org/abs/1101.1277
4. Christine Heitsch, *Counting orbits under Kreweras complementation* (2023). https://arxiv.org/abs/2303.12240
