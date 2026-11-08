# Integral six-axis homology and full icosahedral symmetry of an independence complex

## Finding
Let \(I\) be the graph of the regular icosahedron, with twelve vertices and thirty edges. Its **ordinary independence complex** \(X=\operatorname{Ind}(I)\) is the simplicial complex of vertex sets containing no adjacent pair. Write \(G=\operatorname{Aut}(I)\cong A_5\times C_2\), and let \(\iota\) be central antipodal inversion. There is a canonical \(G\)-invariant triangulated sphere \(S\subset X\); the complement \(X\setminus S\) consists of the interiors of exactly six one-simplices, one joining each antipodal vertex pair. Consequently,

\[
X\simeq S^2\vee\bigvee^6 S^1,
\qquad \widetilde H_1(X;\mathbb Z)\cong\mathbb Z^6,
\qquad \widetilde H_2(X;\mathbb Z)\cong\mathbb Z,
\]

and all remaining reduced integral homology vanishes. The displayed wedge equivalence is nonequivariant.

More precisely, the integral \(G\)-module \(\widetilde H_1(X;\mathbb Z)\) is the **signed permutation lattice** on the six unoriented icosahedral axes through antipodal vertices: an automorphism carries an oriented antipodal edge to its image with the sign of the induced edge orientation. The integral \(G\)-module \(\widetilde H_2(X;\mathbb Z)\) is the one-dimensional orientation character of the invariant sphere. Central inversion acts by \(-1\) in both degrees; all rotations act by \(+1\) in degree two.

On restriction to the rotational subgroup \(A_5\), first rational homology is the six-dimensional irreducible **rational** module whose complexification is the sum of the two Galois-conjugate three-dimensional icosahedral irreducibles. Writing \(W_6\) for this rational module and \(\varepsilon\) for the nontrivial character of \(G/A_5\), the complete rational classification is

\[
\widetilde H_1(X;\mathbb Q)\cong W_6\boxtimes\varepsilon,
\qquad \widetilde H_2(X;\mathbb Q)\cong\mathbf1\boxtimes\varepsilon.
\]

Here \(W_6\) is irreducible over \(\mathbb Q\), *not* over \(\mathbb C\). Every positive-degree rational homology group has zero fixed subspace under the full group. Under rotations, first homology has no invariant vector whereas second homology has a one-dimensional invariant space.

The entire ten-class rational character, with two distinct order-five classes in each coset, is:

| Group coset | Rotational order | Class size | Trace on \(\widetilde H_1\) | Trace on \(\widetilde H_2\) |
|---|---:|---:|---:|---:|
| \(A_5\) | 1 | 1 | 6 | 1 |
| \(A_5\) | 2 | 15 | -2 | 1 |
| \(A_5\) | 3 | 20 | 0 | 1 |
| \(A_5\) | 5A | 12 | 1 | 1 |
| \(A_5\) | 5B | 12 | 1 | 1 |
| \(\iota A_5\) | 1 | 1 | -6 | -1 |
| \(\iota A_5\) | 2 | 15 | 2 | -1 |
| \(\iota A_5\) | 3 | 20 | 0 | -1 |
| \(\iota A_5\) | 5A | 12 | -1 | -1 |
| \(\iota A_5\) | 5B | 12 | -1 | -1 |

The second column records the order of the rotational factor, not necessarily the order of the element in the inversion coset.

## Assumptions and scope
All graphs are finite, undirected and simple. In \(X\), a face is a nonempty set of pairwise *nonadjacent* icosahedral vertices, with the empty face implicit; the word independence never refers to independence of the graph's *edges*. Coefficients are integral unless rational coefficients are explicitly shown. The antipodal map is the unique fixed-point-free involution taking a vertex to the unique vertex at graph distance three. An axis is an unordered antipodal pair. Orientations of its corresponding one-simplex are arbitrary choices and changing such choices conjugates the signed action by diagonal signs without changing the module. The \(A_5\) subgroup comprises the orientation-preserving geometric icosahedral automorphisms.

For a fully reproducible combinatorial labeling, the adjacency lists indexed by \(0,\ldots,11\) are

```
0: 1 5 7 8 11
1: 0 2 5 6 8
2: 1 3 6 8 9
3: 2 4 6 9 10
4: 3 5 6 10 11
5: 0 1 4 6 11
6: 1 2 3 4 5
7: 0 8 9 10 11
8: 0 1 2 7 9
9: 2 3 7 8 10
10: 3 4 7 9 11
11: 0 4 5 7 10
```

This labeling is not part of the invariant claim. The six pairs are \((0,3),(1,10),(2,11),(4,8),(5,9),(6,7)\).

## Proof
**1. Canonical sphere and the six edges.** The icosahedral graph is antipodal and distance-regular, with each vertex having five neighbors at distance one, five at distance two, and one at distance three. An independent pair in \(I\) therefore consists either of a pair at distance two or an antipodal pair at distance three. Exactly thirty unordered pairs have distance two and six have distance three.

The twenty independent triples consist solely of pairs at distance two. Every one of the thirty distance-two edges belongs to exactly two such triangles, and the link of each of the twelve vertices in their union is a five-cycle. The union \(S\) is connected and has \(12\) vertices, \(30\) edges and \(20\) triangles; hence it is a connected closed triangulated two-manifold with Euler characteristic \(12-30+20=2\). By classification of closed surfaces, \(S\cong S^2\). This is an intrinsic graph definition and is preserved by every graph automorphism. The six antipodal edges occur in no triangle and are exactly the remaining edges of \(X\). There are no independent quadruples. All finite incidence assertions can also be verified by the complete labeled adjacency data and the independent certificate `check.py`.

**2. Integral homotopy and homology.** Attaching one interval with both endpoints in a connected simply connected sphere adds one circle up to homotopy. Attaching all six intervals gives \(X\simeq S^2\vee\bigvee^6S^1\). The associated relative pair \((X,S)\) satisfies \(H_1(X,S;\mathbb Z)\cong\mathbb Z^6\), canonically based by oriented antipodal edges, while all other relative homology groups vanish. Since \(H_1(S)=0\) and \(H_0(S)\to H_0(X)\) is an isomorphism, the long exact sequence gives an **equivariant integral isomorphism** \(H_1(X)\cong H_1(X,S)\). Furthermore \(H_2(X)\cong H_2(S)\cong\mathbb Z\), naturally and equivariantly. The isomorphism is not merely a rational rank equality; no torsion can occur.

**3. Group action.** Every automorphism preserves graph distance, hence the canonical sphere and antipodal edges. Thus its first-homology action is exactly the signed edge permutation. The action on top homology of the sphere is its orientation degree. Rotational icosahedral symmetries have degree \(+1\); central inversion has degree \(-1\), so \(H_2\) is the quotient-sign character and inversion acts negatively on \(H_1\) as well. The rotation group \(A_5\) has classes of sizes \(1,15,20,12,12\), represented by rotations of orders \(1,2,3,5,5\). Their signed fixed-axis counts are respectively \(6,-2,0,1,1\). Multiplication by central inversion negates each trace. The degree-two traces are \(+1\) on rotations and \(-1\) on the inversion coset. This proves the displayed ten-class character.

**4. Irreducibility and invariant dimensions.** On \(A_5\), the character \((6,-2,0,1,1)\) equals the sum of the two algebraically conjugate three-dimensional complex irreducible characters, which cannot be separated by a rational submodule; it is the six-dimensional rational irreducible. The central inversion acts by \(-1\), giving the claimed unique extension with that central sign. For the rotational group the average first-homology character is \((6+15(-2)+20(0)+12+12)/60=0\), whereas second homology is trivial. For the full group both degree-one and degree-two characters average to zero.

## Verification
Run `python check.py` using Python 3.10 or later with `networkx` and `sympy` installed (tested with the versions available in the verification environment). The program reconstructs the named twelve-vertex graph directly from the published adjacency lists; enumerates all independent subsets; verifies the thirty distance-two edges, six isolated antipodal edges, connected spherical manifold, and every vertex link; constructs integer simplicial boundary matrices; checks the boundary-square identity, exact ranks \(11,19\) and nineteen unit Smith factors; enumerates all 120 graph automorphisms; and checks two independent character computations on each automorphism: a signed-axis count and a signed-simplicial Lefschetz trace combined with the uniquely determined two-cycle orientation. `verification_output.txt` is the exact recorded stdout. The verification is a reproducible finite certificate for the combinatorial facts, not a substitute for the topological long-exact-sequence argument.

## Relationship to prior work
Engström's 2005 preprint studies connectivity of independence complexes of claw-free graphs, a class containing the icosahedral graph. Barmak's 2010 preprint develops general methods and connectivity bounds for independence complexes. Their general theorems do not themselves determine the present canonical sphere-plus-antipodal-edge decomposition, integral \(A_5\times C_2\) action, or character values. Classical enumerations of the icosahedral graph record its distance-regular intersection array and automorphism group, but these graph data alone are not an already tabulated equivariant homology classification. Existing related calculations for the icosahedral **neighborhood complex**, icosahedral **three-cut complex**, and dodecahedral **Rips complex** involve mathematically different simplicial complexes. An equivalently phrased, unindexed homology computation may exist; searching does not establish publication priority.

## Limitations
This determines the ordinary independence complex of precisely the twelve-vertex icosahedral graph and its integral homology modules. The displayed wedge equivalence is nonequivariant; no equivariant homotopy equivalence or integral decomposition beyond the specified signed six-axis lattice is asserted. The complex character alone is not claimed to distinguish the two conjugate complex three-dimensional constituents separately over the rationals. No generalized theorem for arbitrary Platonic or claw-free graphs follows. The result has not received independent mathematical validation, and publication-priority conclusions are provisional.

## References
- A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420, first posted 2005-12-17. https://arxiv.org/abs/math/0512420
- J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418, first posted 2010-07-02. https://arxiv.org/abs/1007.0418
- E. W. Weisstein, *Icosahedral Graph*, MathWorld, graph properties, including distance regularity and automorphism order. https://mathworld.wolfram.com/IcosahedralGraph.html
- *Icosahedron*, DistanceRegular.org, intersection array and automorphism group. https://www.math.mun.ca/distanceregular/graphs/icosahedron.html
