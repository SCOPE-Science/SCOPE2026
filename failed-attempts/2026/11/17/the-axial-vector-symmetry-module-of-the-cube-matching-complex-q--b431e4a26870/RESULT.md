# The axial-vector symmetry module of the cube matching complex \(Q_3\)

## Finding

Let \(Q_3\) be the graph whose vertices are the binary triples \(\mathbb F_2^3\), with two vertices adjacent when they differ in exactly one coordinate. Let \(K=\mathcal M(Q_3)\) be its **ordinary matching complex**: the vertices of \(K\) are the twelve edges of \(Q_3\), and its simplices are all nonempty collections of pairwise vertex-disjoint cube edges, together with the empty face. Let \(G=\operatorname{Aut}(Q_3)\). For \(g=(b,\sigma)\in\mathbb F_2^3\rtimes S_3\), its action on vertices is \(x\mapsto b+\sigma x\). Define the one-dimensional character \(\varepsilon(g)=(-1)^{b_1+b_2+b_3}\), the signed geometric three-dimensional representation \(\rho(g)=\operatorname{diag}((-1)^{b_1},(-1)^{b_2},(-1)^{b_3})P_\sigma\), and \(\delta(g)=\det\rho(g)=\varepsilon(g)\operatorname{sgn}(\sigma)\).

**Theorem.** There is an isomorphism of rational \(G\)-modules
\[
\widetilde H_2(K;\mathbb Q)\cong\varepsilon\oplus(\delta\otimes\rho),
\]
and \(\widetilde H_i(K;\mathbb Q)=0\) for every \(i\ne2\). The two constituents, of dimensions one and three, are absolutely irreducible and nonisomorphic. Equivalently, for every \(g=(b,\sigma)\),
\[
\operatorname{tr}(g\mid\widetilde H_2(K;\mathbb Q))
=(-1)^{b_1+b_2+b_3}
\left[1+\operatorname{sgn}(\sigma)\sum_{i:\,\sigma(i)=i}(-1)^{b_i}\right].
\]
The three-dimensional constituent is the axial-vector (orientation-twisted geometric) representation: central inversion acts as the identity on this constituent but negates the one-dimensional constituent.

For the actual ordinary topological quotient spaces, rational cohomology satisfies
\[
\dim_\mathbb Q\widetilde H^2(|K|/H;\mathbb Q)=
\begin{cases}
3,&H=\langle x\mapsto x+(1,1,1)\rangle,\\
1,&H=S_3\text{ (coordinate permutations)},\\
1,&H=\{b\in\mathbb F_2^3:\sum_i b_i=0\}\text{ (translations)},\\
0,&H=\mathbb F_2^3,\\
0,&H=G.
\end{cases}
\]
All other reduced rational cohomology groups of these quotients vanish. Thus the antipodal quotient retains three independent rational degree-two classes, whereas the full cube-symmetry quotient is rationally acyclic.

## Assumptions and scope

The group action is the natural action by cube graph automorphisms, extended simplicially to \(K\). All modules and quotient cohomology claims are **rational**; no integral torsion, equivariant homotopy equivalence, or quotient homotopy type is asserted. A matching is any disjoint-edge set, not necessarily extendable to a perfect matching. The binary coordinates \(b_i\) in the formulas are interpreted in \(\{0,1\}\); \(P_\sigma\) sends coordinate unit vector \(e_i\) to \(e_{\sigma(i)}\).

## Proof

**1. Group and chain complex.** An automorphism of \(Q_3\) is determined by the image of the zero vertex (eight choices) and by the permutation of its three neighbors (six choices), because graph distance and intersections of coordinate-neighbor sets determine the remaining vertices. Each affine signed coordinate permutation realizes such a choice, so \(|G|=48\) and \(G=\mathbb F_2^3\rtimes S_3\). Enumerating all disjoint-edge subsets yields face numbers \(f_0=12,f_1=42,f_2=44,f_3=9\), no higher faces, and connected one-skeleton.

**2. Rational homology dimensions without an assumed prior Betti number.** Number each cube edge lexicographically as the unordered pair of its endpoints. Form unsigned simplicial boundary matrices over \(\mathbb F_2\). Exhaustive bit-vector elimination, given explicitly in the accompanying program, yields
\[
\big(\operatorname{rank}_{\mathbb F_2}\partial_1,
\operatorname{rank}_{\mathbb F_2}\partial_2,
\operatorname{rank}_{\mathbb F_2}\partial_3\big)=(11,31,9).
\]
Over \(\mathbb Q\), each rank is at least its mod-two value. On the other hand \(\operatorname{rank}\partial_1\le11\) (augmentation), \(\operatorname{rank}\partial_3\le9\) (nine source columns), and \(\operatorname{rank}\partial_2\le42-\operatorname{rank}\partial_1\le31\) (chain-complex identity). Hence all three ranks agree with the displayed values over \(\mathbb Q\). Euler/chain algebra now gives \(\dim\widetilde H_2=44-31-9=4\), and all other reduced rational homology is zero.

**3. Signed Lefschetz calculation.** Given a matching \(F\) containing \(r\) edges, a cube automorphism carries its oriented \((r-1)\)-simplex to the simplex of the image matching, with sign equal to the sign of the induced permutation on its ordered edge set. The trace of \(g\) on the simplicial \((r-1)\)-chains is therefore the signed count of invariant size-\(r\) matchings. The reduced alternating trace is
\[
L_{\mathrm{red}}(g)=-1+
\sum_{r=1}^4(-1)^{r-1}
\sum_{F\in\mathcal M_r(Q_3):\,gF=F}
\operatorname{sgn}(g\mid F).
\]
Since reduced rational homology is concentrated in degree two, this is exactly its character. The finite exhaustive computation in `verify_cube_matching.py` constructs all \(48\) automorphisms, their induced permutations of the twelve graph edges, and all \(107\) nonempty simplices. It calculates both sides from their definitions for each automorphism, **not** from a stored character table, and checks the identity
\[
L_{\mathrm{red}}(b,\sigma)
=\varepsilon(b,\sigma)+\delta(b,\sigma)\operatorname{tr}\rho(b,\sigma)
\quad\text{for all 48 elements}.
\]
The proof is an exhaustive finite calculation, not an extrapolation from examples. The program also groups elements into the ten signed-cycle conjugacy classes and checks constancy and sizes; its reproducible output is included.

**4. Representation and irreducibility.** The three-dimensional signed geometric representation \(\rho\) is absolutely irreducible under \(\mathbb F_2^3\rtimes S_3\): the translation subgroup acts by three distinct one-coordinate sign characters, while coordinate permutations transitively permute their eigenspaces. Twisting by the one-dimensional \(\delta\) preserves irreducibility. The character equality above and semisimplicity in characteristic zero determine the stated module isomorphism. The two constituents cannot be isomorphic because their dimensions are different. An independent character-inner-product check gives norms one for each constituent, mutual inner product zero, and norm two for their sum.

**5. Quotients.** For each finite subgroup \(H\le G\), rational cohomology of the ordinary quotient \(|K|/H\) identifies with the \(H\)-invariant rational cohomology of \(|K|\) (finite-group averaging/transfer). Thus its only possible nonzero reduced rational cohomology is in degree two, with dimension \(|H|^{-1}\sum_{h\in H}\chi(h)\). Applying the character gives respectively the dimensions \(3,1,1,0,0\) for the five stated subgroups, as checked independently by explicit sums in the verifier. The claimed ring-level consequences follow because the only positive cohomology degree is two, so all positive-degree products vanish.

## Verification

Run `python3 verify_cube_matching.py` with a Python 3 standard-library interpreter. It performs complete face and boundary enumeration, checks all automorphisms and all signed Lefschetz identities, verifies conjugacy-class uniformity, tests irreducible-character inner products, and computes invariant dimensions for all five subgroups. The expected final line is `Q3_MATCHING_EQUIVARIANT_PASS`. An exact execution transcript is provided in `verification_output.txt`; neither the transcript nor a few sample cases substitute for the definitions and complete loops in the program.

## Relationship to prior work

Jonsson's *Simplicial Complexes of Graphs* (first publicly issued in November 2007) develops topological methods for graph matching complexes. A separate public result titled *The cube matching complex is a wedge of four two-spheres* already establishes the **nonequivariant homotopy type** \(K\simeq\bigvee^4 S^2\); neither that homotopy type nor the ordinary Betti number four is new here. The finding is specifically the **complete 48-element rational symmetry module and the five contrasting quotient cohomology calculations**.

A related published result about the cube's three-cut complex has an entirely different face condition and nonzero homology degrees. Its four-dimensional module has character \(\varepsilon(g)\#\operatorname{Fix}_{\mathcal D}(g)\) on four body diagonals; at central inversion this equals \(-4\), whereas the matching-complex degree-two character here is \(+2\). Thus neither the object nor the representation is equivalent to the present one. Likewise, the octahedral *graph* matching complex has eleven-dimensional first homology and is not the cube-graph matching complex.

Agarwal–Basak (2026), Sections 3–5 and the future-directions section, study the ordinary independence complex and **perfect-matching subcomplex** of circular ladder graphs, including the cube \(C_4\square K_2\); the paper explicitly distinguishes the full ordinary matching complex from that proper subcomplex and does not supply this module. Classical work on complete-graph and chessboard matching complexes also concerns different underlying graphs. Indexed summaries of the most directly related cube result were available, but its complete text could not be inspected; this limitation leaves a residual overlap risk.

## Limitations

The theorem applies to the one three-dimensional cube and rational coefficients; it does not classify analogous modules for all hypercubes, integral representation lattices, quotient torsion, or equivariant homotopy types. The exact matching-complex historical record was compared through a public indexed summary but not full text; publication priority requires checking that complete record and any unindexed literature. The computations were reproduced in this package, but no independent mathematical audit has been performed.

## References

1. J. Jonsson, *Simplicial Complexes of Graphs*, Lecture Notes in Mathematics 1928, Springer, print publication 15 November 2007; DOI: https://doi.org/10.1007/978-3-540-75859-4 .
2. *The cube matching complex is a wedge of four two-spheres*, public mathematical research record (11 October 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-cube-matching-complex-is-bigvee-4-s-2--79d70fe8b67e .
3. *Automorphism-module structure of the cube three-cut complex*, public mathematical research record (11 October 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-automorphism-module-structure-of-the-cube-three-cut-complex--7e5f41a11a8d .
4. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601v2 (14 September 2026), https://arxiv.org/html/2608.30601v2 .
5. A. Björner, L. Lovász, S. T. Vrećica and R. T. Živaljević, *Chessboard Complexes and Matching Complexes*, J. London Math. Soc. 49 (1994), 25–39; DOI: https://doi.org/10.1112/jlms/49.1.25 .
