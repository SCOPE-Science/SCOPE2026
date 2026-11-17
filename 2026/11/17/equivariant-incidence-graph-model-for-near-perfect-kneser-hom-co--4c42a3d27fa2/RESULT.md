# Equivariant incidence-graph model for near-perfect Kneser Hom complexes

## Finding
For every integer \(r\geq2\), let \(X_r=\operatorname{Hom}(K_r,\mathrm{KG}(2r+1,2))\) be the graph-homomorphism polyhedral complex and \(G_r=S_{2r+1}\times S_r\), acting by permutations of ground points and of source colors, respectively. Define three finite \(G_r\)-sets:

* \(\mathcal V_r\): labeled ordered \(r\)-tuples of pairwise disjoint two-element subsets of \([2r+1]\), with one unused point;
* \(\mathcal T_r\): an exceptional source color carrying a three-element ground support, together with a two-element support for every other source color, all disjoint;
* \(\mathcal I_r\): incident pairs \((v,t)\) in which the ordered pairs of \(v\) agree with the support blocks of \(t\) away from its exceptional color and choose one of the three two-element subsets of the exceptional triple.

**Claim.** There is a \(G_r\)-equivariant strong deformation retraction of \(X_r\) onto the bipartite incidence graph \(\Gamma_r\) whose node sets are \(\mathcal V_r\) and \(\mathcal T_r\) and whose edge set is \(\mathcal I_r\). The graph is connected. Consequently the complete integral \(G_r\)-homology representation is given by the following explicit exact sequence of permutation lattices:

\[
0\longrightarrow H_1(X_r;\mathbb Z)
\longrightarrow\mathbb Z[\mathcal I_r]
\xrightarrow{\partial}\mathbb Z[\mathcal V_r]\oplus\mathbb Z[\mathcal T_r]
\xrightarrow{\epsilon}\mathbb Z\longrightarrow0,
\]
where \(\partial(v,t)=t-v\) and \(\epsilon\) sends every node to \(1\). All higher homology vanishes, and \(H_1\) is free abelian.

For every \(g\in G_r\), this also gives the **complete rational character** without any choice of irreducible basis:
\[
\operatorname{tr}\bigl(g\mid H_1(X_r;\mathbb Q)\bigr)
=1+|\mathcal I_r^g|-|\mathcal V_r^g|-|\mathcal T_r^g|.
\]
Here fixed points are taken in the explicitly defined finite sets, so the formula is valid for every conjugacy class and every \(r\geq2\).

Put \(q_r=(2r-3)(2r+1)!!/3\), an integer. For the source-color subgroup \(S_r\) the rational representation and quotient are
\[
H_1(X_r;\mathbb Q)|_{S_r}\cong
\mathbb Q\oplus\mathbb Q[S_r]^{\oplus q_r},
\qquad X_r/S_r\simeq\bigvee^{q_r+1}S^1.
\]
In contrast, both \(X_r/S_{2r+1}\) and \(X_r/G_r\) are **contractible**. In particular, \(H_1(X_r;\mathbb Q)^{S_{2r+1}}=0\).

The node and incidence counts are
\[
|\mathcal V_r|=\frac{(2r+1)!}{2^r},\quad
|\mathcal T_r|=\frac{r(2r+1)!}{3!2^{r-1}},\quad
|\mathcal I_r|=3|\mathcal T_r|,
\]
so the known nonequivariant wedge-of-circles type has rank
\[
\beta_1(X_r)=1+\frac{(2r-3)(2r+1)!}{3\,2^r}.
\]
The nonequivariant wedge assertion falls under Osztényi's earlier general theorem; the **new claim is the explicit simultaneous equivariant graph model, integral module, source-color character, and contrasting quotient types**.

## Assumptions and scope
Write \(\mathrm{KG}(n,2)\) for the simple graph whose vertices are two-element subsets of \([n]\), adjacent exactly when disjoint. A cell of \(\operatorname{Hom}(K_r,\mathrm{KG}(n,2))\) assigns to each source vertex a nonempty collection of two-subsets, with every choice in one color disjoint from every choice in another. The cell is the product of simplices on those collections, in the usual Babson–Kozlov convention. No extra structures or orientation hypotheses are imposed. The domain is **every integer \(r\ge2\)** with **exactly \(n=2r+1\)** ground points; the conclusion makes no assertion for other \(n\), for higher-uniformity Kneser graphs, or for generalized multihomomorphisms with altered adjacency.

## Proof
**1. Classification of cells.** Given a multihomomorphism cell, let \(U_i\) be the union of the ground-point pairs in source color \(i\). The cross-disjointness axiom makes all \(U_i\) pairwise disjoint, and every \(|U_i|\ge2\). Since there are \(2r+1\) points, either all supports have size two, or exactly one has size three and the others have size two. In the first case every color contains precisely one two-subset, yielding a node in \(\mathcal V_r\). In the second case the three possible pairs within the unique three-point support form all possible vertices of a two-simplex, and the remaining colors are fixed. Therefore the maximal cells are precisely the \(\mathcal T_r\)-indexed triangles. Every triangle has three distinct corners, and every one-cell belongs to precisely one triangle, because its exceptional color, three-point union, and other pairs are uniquely determined. Distinct triangles meet only at zero-cells.

**2. Equivariant collapse.** Insert the barycenter into each maximal triangle and cone its boundary to that barycenter. Collapse the three subtriangles, each along its unique outer boundary edge. These disjoint free-face pairs can be collapsed simultaneously in a manner invariant under all permutations of the three corners. Since triangles have no shared edges, the construction is compatible across the whole complex and is \(G_r\)-equivariant. What remains from each original triangle is the three-spoked tree joining its barycenter to its corners, exactly the incidence graph \(\Gamma_r\). Thus the collapse is an equivariant strong deformation retraction.

**3. Connectivity.** At a node \(v\in\mathcal V_r\), replacing one point of one colored pair with the unique unused point yields another node; the two nodes are corners of a common triangle. Such operations are the transpositions of the unused coordinate with each other coordinate. They generate the full symmetric group on the \(2r+1\) point positions. The symmetric group is transitive on labeled ordered near-perfect pairings, hence all nodes of \(\mathcal V_r\) lie in one component; triangle centers attach to them. This proves connectivity.

**4. Integral module and character.** Give each spoke the orientation from its \(\mathcal V_r\)-node to its \(\mathcal T_r\)-node. The graph's cellular boundary is \(\partial(v,t)=t-v\), preserved by \(G_r\) because the action never swaps the two node types. Connectivity gives \(\operatorname{im}\partial=\ker\epsilon\), proving the integral exact sequence and hence the full \(\mathbb Z[G_r]\)-lattice description. Taking traces after tensoring with \(\mathbb Q\) proves the fixed-point character formula. Counting ordered pair supports and exceptional triple supports gives the displayed \(V,T,I\) formulas and the Betti number.

**5. Orbit spaces.** No nonidentity permutation of source colors fixes any cell: every color has a nonempty ground support disjoint from all other color supports, so these supports cannot be permuted nontrivially while remaining equal. Thus \(S_r\) acts freely on the incidence graph, yielding \(V/r!+T/r!\) nodes and \(I/r!\) edges. Its quotient is connected and has first Betti number \(1+(2T-V)/r!=q_r+1\), hence is a wedge of that many circles. On the other hand, \(S_{2r+1}\) is transitive on \(\mathcal V_r\); its \(\mathcal T_r\)-orbits and \(\mathcal I_r\)-orbits are each indexed by the exceptional color. The quotient incidence graph is therefore a star with \(r\) leaves, hence a tree. Allowing source-color permutations merges those leaves, and the full quotient is a single edge. Equivariant retraction transfers these orbit-space conclusions to \(X_r\). Finally the \(S_r\)-character is \(\beta_1\) at the identity and \(1\) at each nonidentity element, because every permutation set in the exact sequence is free as an \(S_r\)-set. Over \(\mathbb Q\) this is the character of one trivial representation plus \(q_r\) copies of the regular representation, proving the asserted decomposition.

## Verification
Run `python3 verify_nearperfect_hom.py`. This program independently enumerates all zero-cells and maximal triangles, builds the exact incidence graph and checks its connectivity, unique edge incidence, Euler rank, the color-quotient orbit counts, and preservation under generators of both permutation groups. The enumerated cases are \(r=2,3,4\), producing respective first Betti numbers \(11,631,37801\) and color-quotient Betti numbers \(6,106,1576\). The uniform theorem is proved above; finite tests are cross-checks only. The exact program and its output are supplied alongside this document.

## Relationship to prior work
Babson and Kozlov defined graph Hom polyhedral complexes and proved results for complete-graph targets. Osztényi's Theorem 4 already establishes that \(\operatorname{Hom}(K_r,\mathrm{KG}(m,2))\) is a wedge of \((m-2r)\)-spheres for \(m\ge2r\); setting \(m=2r+1\) **covers the nonequivariant sphere dimension**, so neither the existence of a wedge of circles nor its low-rank instances is claimed as original. An independently recorded uniform character computation for the ordinary Kneser neighborhood complex can already imply the \(r=2\) target-permutation **rational** character, using its classical \(\operatorname{Hom}(K_2,-)\) equivalence. Neither that ground-action special case nor the known non-equivariant wedge classification is new. The newly asserted results concern the natural simultaneous \(S_{2r+1}\times S_r\) action across all \(r\), a canonical equivariant incidence graph, its integral permutation-kernel lattice, and the non-equivalent quotients by the two acting factors. Schultz's results concern principally \(\operatorname{Hom}(K_2,\mathrm{SG}(n,k))\) for **stable** Kneser graphs with dihedral symmetry and do not calculate these full-group modules. No stronger or equivalent indexed treatment of the asserted equivariant statements was identified; this is not proof of publication priority.

## Limitations
The exact permutation-kernel description does not provide a Specht-irrep decomposition upon restriction to every \(S_{2r+1}\) at each \(r\). No assertion is made about integral homology of Borel homotopy quotients, about parameters outside \(2r+1\), or about all Kneser graphs. The computations exhaust only the three stated finite cases; they are not an infinite proof. Unindexed literature might contain equivalent equivariant results. No independent mathematical audit has been performed.

## References
1. E. Babson and D. N. Kozlov, *Complexes of graph homomorphisms*, first public arXiv posting 2003-10-05, arXiv:math/0310056, Definition 1.2 and Section 4.
2. J. Osztényi, *The homotopy type of complexes of homomorphisms from a complete graph to a Kneser graph*, Acta Sci. Math. (Szeged), 76 (2010), 713–722, DOI:10.1007/BF03592970, especially Theorem 4.
3. C. Schultz, *The equivariant topology of stable Kneser graphs*, arXiv:1003.5688, first public 2010-03-29; distinct stable-target and \(K_2\) symmetry setting.
