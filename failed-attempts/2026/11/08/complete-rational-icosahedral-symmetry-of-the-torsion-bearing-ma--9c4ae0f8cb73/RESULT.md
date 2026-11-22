# Complete rational icosahedral symmetry of the torsion-bearing matching complex

## Finding
Let \(I\) be the twelve-vertex icosahedral graph and \(X=\mathcal M(I)\) its ordinary matching complex, with simplicial vertices the thirty graph edges and simplices the mutually disjoint edge collections. Its full simplicial action induced by graph automorphisms is \(G\cong A_5\times C_2\). Write \(z\) for the central antipodal involution, \(A_5\) for the orientation-preserving subgroup, and \(H^+\), \(H^-\) for the \(+1\) and \(-1\) eigenspaces of \(z\) on the reduced rational homology.

Let \(V_4,V_5\) be the rational irreducible \(A_5\)-modules of dimensions four and five, and let \(W_6\) be its six-dimensional rational irreducible whose complexification is the sum of the two conjugate three-dimensional irreducibles. Then the complete \(G\)-representation is concentrated in degree three and satisfies
\[
\widetilde H_3(X;\mathbb Q)^+\cong 2V_4\oplus4V_5\oplus2W_6,
\qquad
\widetilde H_3(X;\mathbb Q)^-\cong2V_4\oplus2V_5\oplus W_6.
\]
All other reduced rational homology groups vanish. In particular the antipodal eigenspaces have dimensions \(40\) and \(24\). No nonzero reduced rational homology class is fixed by all rotations, and consequently
\[
H^*(|X|/A_5;\mathbb Q)\cong H^*(|X|/G;\mathbb Q)\cong\mathbb Q.
\]
Here the isomorphisms are graded rational cohomology rings. They do not assert contractibility or a homotopy equivalence.

## Assumptions and scope
The result is for this specific ordinary matching complex, not a Morse complex or an independence complex on the original graph vertices. Label the graph vertices \(0,1,\ldots,11\), and let \(u_i=1+i\), \(v_i=6+i\) for \(i\in\mathbb Z/5\mathbb Z\). Its edges, with index arithmetic modulo five, are
\[
\{\{0,u_i\},\{11,v_i\},\{u_i,u_{i+1}\},\{v_i,v_{i+1}\},\{u_i,v_i\},\{u_i,v_{i-1}\}:i\in\mathbb Z/5\mathbb Z\}.
\]
The canonical order of matching-complex vertices is the lexicographic order of these thirty undirected edges. All simplicial orientations use ascending indices. The group action is the natural action induced by permutations of the twelve graph vertices.

For reference, the rational irreducible characters of \(A_5\), tabulated on elements of orders \(1,2,3,5\), are \(\chi_{V_4}=(4,0,1,-1)\), \(\chi_{V_5}=(5,1,-1,0)\), and \(\chi_{W_6}=(6,-2,0,1)\); the last entry applies to both classes of elements of order five. The character of \(W_6\) has complex-character norm two because it is the sum of two complex irreducible characters.

## Proof
**1. Exact homological concentration.** An exhaustive increasing-index enumeration gives the matching-complex face vector in dimensions zero through five:
\[
(30,315,1400,2535,1482,125).
\]
Exact bitset Gaussian elimination over \(\mathbb F_2\), performed on all oriented simplicial boundary matrices (whose signs reduce to one), gives the ranks in positive chain degrees \(1,\ldots,5\):
\[
(29,286,1114,1357,125).
\]
For an integral boundary matrix, its rank over \(\mathbb Q\) is at least its rank over \(\mathbb F_2\). Write \(r_k\) for rational rank in chain degree \(k\). The augmented degree-zero map has rank one. The relations \(\partial^2=0\) give \(r_1\le29\), \(r_1+r_2\le315\), \(r_2+r_3\le1400\), \(r_4+r_5\le1482\), and \(r_5\le125\). These inequalities and the five certified lower bounds force *equality* to every displayed modular rank: first \(r_1=29\), then \(r_2=286\) and \(r_3=1114\); independently \(r_5=125\) and \(r_4=1357\). Thus the rational Betti number is \(64\) in degree three and zero in all other reduced degrees, without relying on a previously computed homotopy type or on any assumption that finite-field ranks always equal rational ranks.

**2. Exact full automorphism group.** The twenty three-cycles of the icosahedral graph are its triangulated two-sphere faces; each edge belongs to exactly two. Any graph automorphism is uniquely determined by the image of an *ordered* triangular face. Propagation across adjacent triangles determines the images of every vertex. The supplied verifier reconstructs all \(20\cdot6=120\) valid maps, checks that each preserves all thirty edges, and constructs the two possible global sphere orientations by opposite incidence directions across every edge. Sixty maps preserve orientation; these give the classical rotational icosahedral group \(A_5\). The unique nonidentity central automorphism exchanges each vertex with its distance-three antipode, is orientation-reversing, and generates a complementary central \(C_2\). This identifies \(G=A_5\times C_2\).

**3. Character by a complete signed Lefschetz calculation.** A graph automorphism \(g\) acts on a sorted \(j\)-simplex \(e_0<\cdots<e_j\) by sending the indices to those of \(ge_0,\ldots,ge_j\), and reordering with the sign of that permutation. Thus the trace on the \(j\)-chains is the sum of signs over the \(j\)-simplices preserved as *unordered sets*. Since rational reduced homology is concentrated in degree three, the alternating-trace identity yields
\[
\operatorname{tr}(g\mid\widetilde H_3(X;\mathbb Q))
=1-\sum_{j=0}^5(-1)^j\operatorname{tr}(g\mid C_j(X;\mathbb Q)).
\]
The leading \(1\) accounts for the reduced empty simplex. Exhausting every simplex and all 120 group elements gives the following exact values. For positive-orientation elements of orders \(1,2,3,5\), the character is respectively \((64,0,-2,-1)\), on conjugacy-class sizes \((1,15,20,24)\). For the corresponding elements \(zg\), the values are \((16,0,-2,1)\). In particular \(\operatorname{tr}(z)=16\). The verifier checks the signed chain-map identity \(g\partial=\partial g\) along all \(120\cdot23130=2{,}775{,}600\) nonempty codimension-one incidences.

**4. Character decomposition.** The central-idempotent projections \((1\pm z)/2\) give \(A_5\)-characters on the even and odd rational eigenspaces. On rotations of orders \(1,2,3,5\), they are respectively
\[
\chi^+=(40,0,-2,0),\qquad\chi^-=(24,0,0,-1).
\]
Using the known \(A_5\) character table and conjugacy-class multiplicities \((1,15,20,24)\), the scalar products with \(V_4,V_5,W_6\) yield multiplicity triples \((2,4,2)\) and \((2,2,1)\), where the scalar product with \(W_6\) is divided by two to account for its complex splitting. The trivial representation has multiplicity zero in both eigenspaces. The displayed full rational decomposition follows.

**5. Quotients.** For a finite group acting simplicially, barycentric subdivision gives a cellular orbit decomposition, and with characteristic-zero coefficients averaging identifies the rational cohomology of the orbit space with the invariant cohomology of the original complex. Since the only reduced rational homology is the degree-three module and it has no rotation-invariant vectors, both asserted orbit-space cohomology rings equal \(\mathbb Q\) in degree zero.

## Verification
Run `python3 verify_icosahedral_symmetry.py` under Python 3.9 or later. No external packages are required. It independently generates the labelled graph, its 120 automorphisms by face propagation, all 5,887 nonempty simplices, the complete bitset boundary-rank certificate over \(\mathbb F_2\), the full signed traces, the central-idempotent characters, the rational irreducible multiplicities, and every signed boundary-equivariance relation. Its successful output is supplied verbatim as `verification_output.txt`. All integer counts and signs are reconstructed from the graph definition; the script does not read any cached data or previous findings.

## Relationship to prior work
Shareshian and Wachs (first public September 3, 2004) treat the topology and torsion of matching complexes of complete and complete bipartite graphs and survey the resulting symmetric-group representations; their methods motivate the equivariant question but do not determine the group action for the noncomplete icosahedral graph. Bayer, Jelić Milutinović and Vega (first public November 7, 2024) study *outerplanar* graph matching complexes, not this nonouterplanar triangulation. Bate, Everitt, Ford and Ramos (first public December 21, 2023) treat the matching complex of the *complete hypergraph*, with \(S_n\)-module decompositions, not the icosahedral graph or its rotational subgroup.

The publicly available 2026 icosahedral matching-complex calculation (record `28565ad1ea1a`) proves the nonequivariant integral homotopy decomposition \(\bigvee^{64}S^3\vee M(\mathbb Z/3,3)\). That earlier homotopy calculation establishes rational Betti number 64 but does **not** imply how any graph symmetry acts on homology; no equivariant decomposition or central-inversion trace occurs in its inspected result and proof. Here the rational homology ranks are independently re-established. The new contribution is the *complete full-group character and its rational representation decomposition*, including antipodal eigenspaces and the symmetry-quotient consequences; neither torsion nor the nonequivariant homotopy type is claimed as a new discovery.

## Limitations
This is a rational-equivariant theorem for one natural finite graph. It does not determine the integral \(\mathbb Z[A_5\times C_2]\)-lattice on the free homology, the group action on the three-torsion subgroup, the integral cohomology of either orbit space, a Borel quotient, or any equivariant homotopy equivalence. The exhaustive certificate is a conventional transparent finite proof component, not a formal proof assistant or independent verification. Searches of accessible records cannot rule out equivalent results in unindexed literature.

## References
1. J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054, first public 2004-09-03, https://arxiv.org/abs/math/0409054 .
2. M. Bayer, M. Jelić Milutinović, and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601, first public 2024-11-07, https://arxiv.org/html/2411.04601v2 .
3. M. Bate, B. Everitt, S. Ford, and E. Ramos, *Homology of matching complexes and representations of symmetric groups*, arXiv:2312.13750, first public 2023-12-21, https://arxiv.org/abs/2312.13750 .
4. *Three-torsion in the icosahedral matching complex: a planar counterexample*, public mathematical record `28565ad1ea1a` (2026); its `RESULT.md` and both verification methods were compared for object and mathematical implication.
