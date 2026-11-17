# Full tetrahedral symmetry of truncated-tetrahedral matching homology

## Finding
Let \(T\) be the twelve-vertex truncated-tetrahedral graph, with vertices the ordered pairs \((a,b)\) of distinct elements of \(\{0,1,2,3\}\), and with two distinct ordered pairs adjacent when their first coordinates agree or they are mutual reversals. Let \(K=\mathcal M(T)\) be the simplicial complex of matchings in \(T\), and let \(S_4\) act by simultaneously permuting the four labels. The full graph automorphism group is \(\operatorname{Aut}(T)\cong S_4\). As a rational representation of that group,
\[
\boxed{\widetilde H_3(K;\mathbb Q)\cong S^{(1,1,1,1)}\oplus 3S^{(3,1)}\oplus 2S^{(2,1,1)}\oplus 3S^{(2,2)}.}
\]
All other reduced rational homology groups are zero. The complete third-homology character on the five \(S_4\) cycle types \((1,1,1,1),(2,1,1),(2,2),(3,1),(4)\), respectively, is \((22,0,2,-2,-2)\). Here \(S^\lambda\) denotes the rational Specht representation of partition \(\lambda\); in particular, \(S^{(1,1,1,1)}\) is the sign representation.

For the ordinary topological quotients, the full quotient has no reduced rational cohomology, while the orientation-preserving tetrahedral quotient retains one degree-three class:
\[
\boxed{\widetilde H^*(|K|/S_4;\mathbb Q)=0,\qquad H^*(|K|/A_4;\mathbb Q)\cong H^*(S^3;\mathbb Q).}
\]
The cohomology-ring isomorphism does not imply a homotopy equivalence of the quotient with a sphere.

## Assumptions and scope
Work with the finite simple graph \(T\) defined above. It has four disjoint triangles, one for each first coordinate, and six reversal edges \(\{(a,b),(b,a)\}\) for unordered distinct \(a,b\). Thus \(|V(T)|=12\), \(|E(T)|=18\), and the ordinary matching complex has one simplicial vertex for each of the eighteen graph edges. A face is any set of pairwise vertex-disjoint graph edges. We use the usual reduced simplicial homology with rational coefficients, including the augmentation in degree \(-1\). The action on a simplex is the signed permutation of its ordered graph-edge vertices, not merely its setwise action.

The only three-cycles in \(T\) are its four first-coordinate triangles: endpoints of a reversal edge have no common neighbor, while edges within one first-coordinate triangle are entirely internal. Consequently every graph automorphism permutes those four triangles. The reversal edges force its action on each \((a,b)\) to be \((\sigma(a),\sigma(b))\) for a unique \(\sigma\in S_4\). Conversely all twenty-four such permutations are automorphisms. This proves that the displayed \(S_4\) action is the *full* automorphism action.

## Proof
**Rational homology.** Order the twelve ordered-pair vertices and eighteen undirected graph edges lexicographically. An exhaustive recursive construction of all matchings, including the empty matching, yields \(1010\) faces, or \(1009\) nonempty simplices, with nonempty face vector by dimension
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(18,117,332,390,144,8).
\]
As a separate enumeration check, a vertex-deletion recurrence for the matching polynomial produces the same face vector. For the augmented chain groups \(C_{k-1}\), indexed by matchings of cardinality \(k\), exact Gaussian elimination over \(\mathbb F_2\) gives boundary ranks for \(k=1,\ldots,6\)
\[
(1,17,100,232,136,8).
\]
The resulting reduced \(\mathbb F_2\)-Betti numbers vanish except in dimension three, where the dimension is \(22\). Each integral boundary matrix has rank over \(\mathbb Q\) at least its rank over \(\mathbb F_2\): a nonzero determinant of a minor modulo two is also a nonzero integer determinant. Hence every rational Betti number is at most the corresponding mod-two Betti number. The reduced Euler characteristic, calculated from the face vector, equals \(-22\). Therefore the *only* nonzero reduced rational Betti number is \(\dim\widetilde H_3(K;\mathbb Q)=22\), not merely an upper bound obtained from modular ranks.

**Signed traces and character.** Let \(g\in S_4\), acting on the eighteen edge-vertices of \(K\). The reduced simplicial Lefschetz trace is
\[
L(g)=\sum_{k=-1}^{5}(-1)^k\operatorname{tr}(g\mid \widetilde C_k(K;\mathbb Q)).
\]
For each setwise fixed \(k\)-simplex, its contribution is \((-1)^k\) times the sign of the permutation induced by \(g\) on its ordered vertices; nonfixed simplices contribute zero. Because reduced rational homology occurs only in degree three, \(\chi_3(g)=-L(g)\).

There is an independent fixed-orbit formula. Partition the eighteen graph edges into orbits of the permutation induced by \(g\). Discard any orbit whose edges are not pairwise disjoint; two remaining orbits are compatible precisely when the union of their edges remains a matching. Then
\[
\chi_3(g)=\sum_{\mathcal A}(-1)^{|\mathcal A|},
\]
where \(\mathcal A\) ranges over compatible subcollections of admissible edge orbits, including the empty subcollection. Indeed, a fixed matching is a union of entire edge orbits; if it comprises \(r\) orbits and \(s\) edges, its simplex sign is \((-1)^{s-r}\), while its degree contributes \((-1)^{s-1}\). Their product to \(L(g)\) is \((-1)^{r+1}\), giving the formula after negation. These two calculations agree on all twenty-four permutations, and each is constant on cycle type:

| Cycle type | Class size | Character value |
| --- | ---: | ---: |
| \((1,1,1,1)\) | 1 | 22 |
| \((2,1,1)\) | 6 | 0 |
| \((2,2)\) | 3 | 2 |
| \((3,1)\) | 8 | -2 |
| \((4)\) | 6 | -2 |

**Irreducible decomposition.** The five irreducible rational characters of \(S_4\), in the above class order, are the trivial \((1,1,1,1,1)\), sign \((1,-1,1,1,-1)\), standard \((3,1,-1,0,-1)\), signed standard \((3,-1,-1,0,1)\), and two-dimensional \((2,0,2,-1,0)\) characters. Their exact inner products with \((22,0,2,-2,-2)\), weighted by class sizes \((1,6,3,8,6)\) and divided by \(24\), are respectively \((0,1,3,2,3)\). These nonnegative integer multiplicities sum to dimension \(1+9+6+6=22\), proving the stated rational representation isomorphism.

**Topological quotients.** After barycentric subdivision, the action has simplex stabilizers that fix their simplices pointwise. Rational averaging for finite groups therefore identifies \(H^*(|K|/H;\mathbb Q)\) with \(H^*(|K|;\mathbb Q)^H\) for each subgroup \(H\le S_4\). The multiplicity of the trivial representation is zero, so the full quotient has no reduced rational cohomology. The only irreducible representation among the listed summands that becomes trivial on \(A_4\) is the sign line. Hence the quotient by \(A_4\) has precisely one nonzero reduced rational cohomology group, of dimension one in degree three; its ring is the sphere cohomology ring since there are no other positive degrees. For additional reproducibility the same character averages give invariant dimensions \(7\) for the normal Klein-four subgroup and \(3\) for a point-stabilizing \(S_3\).

## Verification
Execute `python3 verify.py` from a directory containing the standalone `verify.py`. The program uses only the Python standard library. It independently reconstructs graph edges, all matching faces by both edge enumeration and a vertex-deletion matching-polynomial recurrence, augmented boundary ranks, all twenty-four group actions, signed Lefschetz traces and the alternative compatible-orbit sum. It also computes the character inner products and subgroup averages. The supplied `output.txt` is the actual console output of this verifier. Successful execution ends with `TRUNCATED_TETRAHEDRON_MATCHING_CHARACTER_PASS`.

## Relationship to prior work
Engström's *Independence complexes of claw-free graphs* (arXiv:math/0512420v1; first public 2005-12-17) supplies the archived motivation: matching complexes are independence complexes of claw-free line graphs, with connectivity tools but not this automorphism representation. Barmak's *Star clusters in independence complexes of graphs* (arXiv:1007.0418v1) discusses matching complexes and general homotopy/connectivity constructions, not the complete character of this graph. Bate, Everitt, Ford and Ramos (arXiv:2312.13750v3) compute representations for matching complexes of complete hypergraphs and asymptotic fibre-closed families, not the matching complex of this truncated-tetrahedral graph. The published *Edge-orbit matching-complex homotopy of the truncated tetrahedron* (2026-10-11, see reference below) already proves the stronger **nonequivariant** homotopy classification \(K\simeq\bigvee^{22}S^3\) and edge-orbit deletion/link classifications. None of those results is claimed as new here; those homotopy statements, without a compatible equivariant construction, do not imply the rational character or invariant dimensions. The new claim is precisely the complete \(S_4\)-module and its quotient consequences. Results about the *vertex* independence or two-independence complex of the same graph concern different spaces, while the octahedral graph's matching complex has different vertices and homology degree. Published-index searches under these formulations identified no direct covering character theorem, but absence of a match is not a proof of worldwide priority.

## Limitations
This is an exact finite calculation for the ordinary matching complex of one twelve-vertex graph. It makes no claim about integral equivariant lattices, torsion in integral quotient homology, integral homotopy of the quotients, or an infinite family. The mod-two rank computation is used to prove rational Betti numbers, **not** to assert integral torsion-freeness; the nonequivariant integral sphere-wedge theorem is properly attributed to earlier work. Priority relative to unindexed or unpublished treatments is not certified, and no independent external mathematical audit has been performed.

## References
1. A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420v1, submitted 2005-12-17, https://arxiv.org/abs/math/0512420.
2. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, submitted 2010-07-02, https://arxiv.org/abs/1007.0418.
3. M. Bate, B. Everitt, S. Ford and E. Ramos, *Homology of matching complexes and representations of symmetric groups*, arXiv:2312.13750v3 (first public 2023-12-21), https://arxiv.org/abs/2312.13750.
4. *Edge-orbit matching-complex homotopy of the truncated tetrahedron*, published research result (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-edge-orbit-matching-complex-homotopy-of-the-truncated-tetrahedro--f5ae4a359c83.
