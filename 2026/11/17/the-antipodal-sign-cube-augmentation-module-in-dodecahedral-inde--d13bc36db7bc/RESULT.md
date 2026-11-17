# The antipodal-sign cube augmentation module in dodecahedral independence homology

## Finding
Let \(D=GP(10,2)\) be the twenty-vertex dodecahedral graph, \(X=\operatorname{Ind}(D)\) its ordinary independence complex, and \(G=\operatorname{Aut}(D)\). Let \(\mathcal C\) be the set of five maximum independent sets of eight vertices, geometrically the five inscribed cubes. Let \(\varepsilon:G\to\{\pm1\}\) be the character trivial on the sixty rotational automorphisms and equal to \(-1\) on the central antipodal inversion. Then, as rational \(G\)-modules,
\[
\boxed{\widetilde H_5(X;\mathbb Q)\cong\varepsilon\otimes\ker\!\left(\mathbb Q[\mathcal C]\xrightarrow{\sum}\mathbb Q\right),}\qquad
\widetilde H_j(X;\mathbb Q)=0\ (j\ne5).
\]
In particular, the four-dimensional module is absolutely irreducible, even after restriction to the rotational \(A_5\), and inversion acts by \(-I_4\). Its complete character is
\[
\boxed{\chi(g)=\varepsilon(g)(|\mathcal C^g|-1)}\quad(g\in G).
\]
The ordinary topological quotients by the full group, by the rotations, and by antipodal inversion are rationally acyclic. By contrast, the quotient by the rotational stabilizer of one inscribed cube has the rational cohomology ring of \(S^5\). Adding inversion to that stabilizer makes its quotient rationally acyclic.

## Assumptions and scope
Index the vertices by \(u_i=i\) and \(v_i=10+i\), with \(i\in\mathbb Z/10\mathbb Z\), and define edges
\[
\{u_i,u_{i+1}\},\quad\{u_i,v_i\},\quad\{v_i,v_{i+2}\}
\qquad(i\in\mathbb Z/10\mathbb Z).
\]
The independence complex consists of all vertex subsets spanning no graph edge, including the empty face in the reduced augmented simplicial chain complex. The five sets \(\mathcal C\) are exactly the independent eight-subsets; their indexed vertex lists are recorded by the standalone verifier. The central involution is \(a(u_i)=u_{i+5}\), \(a(v_i)=v_{i+5}\). The rotational subgroup is \(H=[G,G]\cong A_5\), and \(G=H\times\langle a\rangle\). The character \(\varepsilon\) is \(+1\) on \(H\) and \(-1\) on \(aH\). All homology and quotient claims here have rational coefficients unless explicitly stated otherwise.

## Proof
**1. Rational homology from a complete finite boundary computation.** An exhaustive recursion over subsets produces the numbers of independent sets by cardinality \(0,\ldots,8\):
\[
(1,20,160,660,1510,1912,1240,320,5).
\]
The augmented simplicial boundary maps, reduced modulo two, have ranks in cardinalities \(1,\ldots,8\):
\[
(1,19,141,519,991,921,315,5).
\]
The corresponding reduced mod-two Betti numbers in topological dimensions \(0,\ldots,7\) are \((0,0,0,0,0,4,0,0)\). These ranks are exact: the verifier constructs every column of each boundary matrix and performs complete bitwise Gaussian elimination, including the augmentation from vertices to the empty face. The universal coefficient theorem bounds each rational Betti number by the corresponding mod-two Betti number. The reduced Euler characteristic, computed from the face vector, is \(-4\). Therefore the unique rational reduced homology group is degree five, of dimension exactly four. This proof does not claim integral torsion-freeness.

**2. An exact signed Lefschetz formula.** For \(g\in G\), the reduced simplicial chain trace is computed by summing over setwise-fixed independent faces with their orientation signs, including the empty face with the augmented convention. Since reduced rational homology is concentrated in odd degree five, the Hopf trace formula gives
\[
\chi(g)=\sum_{\substack{S\subseteq V(D)\\S\ \mathrm{independent},\ gS=S}}
(-1)^{|S|}\operatorname{sgn}(g|_S).
\]
An invariant set \(S\) is a union of vertex cycles of \(g\); if it contains \(t\) such cycles, then \((-1)^{|S|}\operatorname{sgn}(g|_S)=(-1)^t\). Form a graph \(Q_g\) whose vertices are the \(g\)-orbits that are individually independent, joining two orbit-vertices if any original edge connects their members. Then the preceding sum is exactly the independent-set polynomial of \(Q_g\), evaluated at \(-1\). The verifier computes this formula and independently sums the original signed simplicial traces for **all** automorphisms; the two computations agree.

**3. Exact symmetry classification and character comparison.** A complete adjacency-preserving backtracking enumeration, checking every adjacency and nonadjacency against already assigned vertices, yields exactly \(120\) automorphisms. Their set of commutators is a subgroup of order \(60\); it maps bijectively onto the \(60\) even permutations induced on \(\mathcal C\). The kernel of the full action on \(\mathcal C\) is \(\{1,a\}\), and \(a\) is central. Hence \(G\cong A_5\times C_2\), with \(H=[G,G]\cong A_5\).

For each \(g\), the direct Lefschetz computation gives \(\varepsilon(g)(|\mathcal C^g|-1)\). This is checked for all \(120\) elements, not inferred from a sample. Equivalently, on the five rotational class types (identity, order-two, order-three, and the two order-five classes), the character values are respectively
\[
(4,0,1,-1,-1)
\]
and on the corresponding inversion cosets they are
\[
(-4,0,-1,1,1).
\]
Their class sizes are respectively \((1,15,20,12,12)\) in each coset. Thus the character is exactly that of \(\varepsilon\otimes\ker(\mathbb Q[\mathcal C]\to\mathbb Q)\). Rational representation semisimplicity establishes the asserted module isomorphism. Moreover, \(\sum_{g\in G}\chi(g)^2=120\) and \(\sum_{g\in H}\chi(g)^2=60\); hence the module and its rotational restriction have character norm one and are absolutely irreducible. Finally, \(\chi(a)=-4\) and \(a^2=1\) imply that \(a\) acts as \(-I_4\).

**4. Quotients.** For any finite simplicial group action, barycentric subdivision gives an admissible action. In characteristic zero the quotient cochain complex identifies with invariant cochains, and taking invariants is exact. Therefore \(H^*(|X|/J;\mathbb Q)\cong H^*(X;\mathbb Q)^J\) for each subgroup \(J\le G\). The module has no invariants under \(G\), \(H\), or \(\langle a\rangle\). For a stabilizer \(H_c\le H\) of one cube, the action on \(\mathcal C\) has two orbits, of sizes one and four, so the augmentation module has precisely one invariant direction. Adding \(a\) kills this direction. Since rational cohomology is otherwise concentrated in degrees zero and five, the asserted cohomology-ring descriptions follow.

## Verification
Run `python3 verify_dodecahedral_symmetry.py` with Python's standard library. It reconstructs the graph and all \(5,828\) faces, computes every augmented boundary rank modulo two, exhaustively finds every one of the \(120\) graph automorphisms, constructs the five geometric cube facets, checks all conjugacy classes and the group splitting, and independently compares orbit-graph evaluation with signed Lefschetz traces on every automorphism. It also verifies the character inner products and subgroup invariant dimensions. Its expected final marker is `DODECAHEDRAL_CUBE_AUGMENTATION_CHARACTER_PASS`; full output is in `verification_output.txt`. The group and homology conclusions follow from finite exhaustive computations and the stated general theorems; individual sampled cases are not used as universal certificates.

## Relationship to prior work
Barmak's 2010 paper develops star clusters and homotopy tools for graph independence complexes, but does not identify this dodecahedral equivariant homology character. Berghoff's work develops independence-complex homology methods and computes Petersen and cubical examples, not the dodecahedron's full automorphism representation. The published calculation *The dodecahedral independence complex is a wedge of four 5-spheres* establishes the nonequivariant homotopy type \(\bigvee^4S^5\); this type and its Betti number are **not** claimed as new. Classical geometry, including Baez's discussion of the five inscribed cubes, establishes the cube configuration and its rotational \(A_5\) action; it does not identify that permutation module with graph-independent-set homology or determine inversion's sign on homology. The new content is the exact representation identification, irreducibility, antipodal sign, and natural quotient contrast.

## Limitations
The theorem is specific to the twenty-vertex dodecahedral graph. It determines rational representations, not the isomorphism class of the integral \(G\)-lattice, possible integral quotient torsion, or equivariant homotopy types of quotient spaces. Rational acyclicity does not imply contractibility. The proof uses complete finite enumeration and exact arithmetic; it does not supply a purely conceptual closed-form chain equivalence to the cube augmentation lattice. Equivalent results in differently indexed literature remain a publication-priority risk. No independent mathematical audit is asserted.

## References
1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418, first posted 2010-07-02, https://arxiv.org/abs/1007.0418.
2. J. C. Baez, *Dodecahedron With 5 Tetrahedra*, AMS Visual Insight, 2015-05-15, https://blogs.ams.org/visualinsight/2015/05/15/dodecahedron-with-5-tetrahedra/ (discussion of five inscribed cubes).
3. M. Berghoff, *On the homology of independence complexes*, arXiv:2008.06267, first posted 2020-08-14, https://arxiv.org/abs/2008.06267.
4. *The dodecahedral independence complex is a wedge of four 5-spheres*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-dodecahedral-independence-complex-is-a-wedge-of-four-5-spher--ba0161fd495f (the nonequivariant homotopy-type computation).
