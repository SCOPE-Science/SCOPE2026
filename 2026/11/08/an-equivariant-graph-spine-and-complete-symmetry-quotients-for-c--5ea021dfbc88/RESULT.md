# An equivariant graph spine and complete symmetry quotients for categorical complete-graph independence complexes

## Finding

Let \(m,n\ge2\) be integers, \(G_{m,n}=K_m\times K_n\) the **categorical** graph product (vertices \((i,j)\), with two vertices adjacent precisely when both coordinates differ), and \(X_{m,n}=|\operatorname{Ind}(G_{m,n})|\). Put \(\Gamma_{m,n}=S_m\times S_n\), enlarged by coordinate interchange \(\tau(i,j)=(j,i)\) when \(m=n\). The following classification holds simultaneously for all indicated parameters.

**Equivariant spine.** There is an explicit \(\Gamma_{m,n}\)-equivariant strong deformation retraction with a piecewise-linear terminal map of \(X_{m,n}\) onto the barycentric subdivision \(T_{m,n}\) of the complete bipartite graph \(K_{m,n}\). The spine has row-center vertices \(r_i\), column-center vertices \(c_j\), original grid vertices \(v_{ij}\), and exactly the edges \(r_i v_{ij}\) and \(v_{ij}c_j\). In the balanced case, coordinate interchange exchanges \(r_i\) with \(c_i\) and sends \(v_{ij}\) to \(v_{ji}\).

**Every subgroup quotient.** For each subgroup \(H\le\Gamma_{m,n}\), including subgroups with coordinate interchange in the balanced case, let \(o_V(H)\) and \(o_E(H)\) be its numbers of orbits on the vertices and edges of the explicit graph \(T_{m,n}\). Then

\[
X_{m,n}/H\simeq\bigvee^{o_E(H)-o_V(H)+1}S^1,
\qquad \pi_1(X_{m,n}/H)\cong F_{o_E(H)-o_V(H)+1}.
\]

Here a wedge of zero circles means a point, and \(F_b\) is the free group of rank \(b\). There is **no integral homology torsion** in any such quotient.

For \(H\le S_m\times S_n\), write \(a_H,b_H,z_H\) for the numbers of orbits on row labels, column labels, and ordered grid positions, respectively. The same rank reduces to

\[
 b(H)=z_H-a_H-b_H+1.
\]

In particular, for any transitive \(H\le S_n\) acting diagonally on row and column labels, if \(r(H)\) is its permutation rank (number of orbits on ordered pairs of labels), then

\[
 X_{n,n}/H\simeq\bigvee^{r(H)-1}S^1.
\]

The diagonal action of \(S_n\) yields one circle for \(n\ge2\); that of a regular cyclic group gives \(n-1\) circles. The full coordinate-independent group \(S_m\times S_n\) has contractible quotient. For the coordinate-swap involution alone,

\[
X_{n,n}/\langle\tau\rangle\simeq
\bigvee^{\binom{n-1}{2}} S^1.
\]

**Every subgroup fixed space.** If \(H\le S_m\times S_n\), let \(f_H,g_H\) be the numbers of row and column labels fixed individually by every element of \(H\). If both numbers are positive, \(X_{m,n}^H\simeq |K_{f_H,g_H}|\); if exactly one is positive, the fixed space is homotopy equivalent to that many isolated points; if both are zero it is empty. If \(m=n\) and \(H\) contains a coordinate-interchanging element, its fixed space is homotopy equivalent to the discrete set of grid positions fixed individually by all elements of \(H\). In particular,

\[
X_{n,n}^{\langle\tau\rangle}\simeq\coprod_{i=1}^{n}\{\mathrm{point}\}.
\]

The given descriptions are stronger than mere Betti numbers: the strong deformation retraction identifies the actual homotopy type of every quotient and fixed space.

**Integral symmetry representation.** With \(U_d=\ker(\mathbb Z^d\xrightarrow{\varepsilon}\mathbb Z)\) the integral augmentation lattice, there is a natural isomorphism

\[
\widetilde H_1(X_{m,n};\mathbb Z)\cong_{\mathbb Z[S_m\times S_n]}U_m\otimes_{\mathbb Z}U_n,
\]

and all other reduced integral homology groups vanish. For \(m=n\), the coordinate interchange acts as **minus tensor flip** \(u\otimes v\mapsto-v\otimes u\). The complete rational trace is \((f(\pi)-1)(f(\sigma)-1)\) for \((\pi,\sigma)\in S_m\times S_n\), and \(1-f(\pi\sigma)\) for \((\pi,\sigma)\tau\) in the balanced group, where \(f(\rho)\) is the number of fixed labels of a permutation \(\rho\).

## Assumptions and scope

All graphs are finite and simple; the categorical product is **not** the Cartesian product. The independence complex contains every set of pairwise nonadjacent grid vertices, including the empty face; geometric realizations use the ordinary finite simplicial-complex topology. The assertions require \(m,n\ge2\). If \(m\ne n\), only the side-preserving action \(S_m\times S_n\) is asserted. If \(m=n\), the described action of \((S_n\times S_n)\rtimes C_2\) includes every choice of row relabeling, column relabeling, and their interchange. All fixed spaces mean fixed **geometric points**, not merely the subcomplex on pointwise-fixed original vertices.

## Proof

**1. Identify all faces.** Any two grid vertices with different first and second coordinates are adjacent in \(G_{m,n}\). Consequently a nonempty independent set with two distinct column indices has a common row index; a set with two distinct row indices has a common column index. Thus the maximal faces of \(\operatorname{Ind}(G_{m,n})\) are precisely the \(m\) full row simplices \(R_i\cong\Delta^{n-1}\) and the \(n\) full column simplices \(C_j\cong\Delta^{m-1}\). Different row simplices are disjoint, as are different column simplices, and \(R_i\cap C_j=\{v_{ij}\}\). This is an exact combinatorial statement, including the \(m=n=2\) boundary.

**2. A symmetric explicit simplex retraction.** In a simplex with \(d\ge2\) barycentric coordinates \(x_1,\ldots,x_d\), let \(a\) be the largest coordinate, \(b\) the second largest, \(t=a-b\), and \(u=(1/d,\ldots,1/d)\). If the maximum is unique at index \(j\), define

\[
R_d(x)=(1-t)u+t e_j.
\]

If the maximum is tied, define \(R_d(x)=u\), which agrees with the same expression because \(t=0\). The order statistics \(a,b\) are continuous, so \(R_d\) is continuous even across ties; it is piecewise linear on the finite polyhedral subdivision determined by coordinate ordering. Permuting coordinates commutes with \(R_d\). Its image is the star-shaped tree \(\bigcup_j[u,e_j]\). For a point \(x=(1-s)u+s e_j\) in that tree, its largest-minus-second-largest difference is exactly \(s\), so \(R_d(x)=x\). In particular all original simplex vertices are fixed. The straight-line homotopy \((1-q)x+qR_d(x)\), for \(0\le q\le1\), remains in the simplex and fixes this tree pointwise.

Apply this formula separately to every maximal row and column simplex. By Step 1 any two distinct such simplices intersect only at an original grid vertex, which is fixed by both formulas. Hence the maps and homotopies glue uniquely into a continuous strong deformation retraction of the full complex. Every row-label permutation, column-label permutation and, when balanced, coordinate swap carries one simplex to another while permuting its coordinates; symmetry of the formula makes the retraction equivariant. Its image is precisely the displayed graph \(T_{m,n}\), homeomorphic to a subdivision of \(K_{m,n}\).

**3. Quotients of every subgroup.** Equivariance implies that the homotopy in Step 2 descends to a strong deformation retraction \(X_{m,n}/H\searrow T_{m,n}/H\). Every edge of \(T_{m,n}\) has one endpoint a row/column center and one endpoint an original grid vertex. These two types are invariant under every element of \(\Gamma_{m,n}\), including coordinate swaps. Therefore no element sends an edge to itself while reversing its endpoints: the action has **no edge inversions**. Its topological quotient is the ordinary finite graph with one vertex and one edge per corresponding orbit. Since \(T_{m,n}\) is connected, the quotient graph is connected. Its first Betti number and free fundamental-group rank are \(o_E(H)-o_V(H)+1\); it has the homotopy type of a wedge of precisely that many circles, with torsion-free integral homology.

When \(H\le S_m\times S_n\), a grid-vertex orbit corresponds to an orbit on ordered pairs \((i,j)\), while center-vertex orbits correspond to row and column orbits. Every original edge of \(K_{m,n}\) becomes two subdivided edges with exactly the same orbit count on each half. Therefore \(o_V=a_H+b_H+z_H\) and \(o_E=2z_H\), giving \(b(H)=z_H-a_H-b_H+1\). For diagonal transitive \(H\) the two center-orbit counts are one and the pair-orbit count is the permutation rank, yielding \(r(H)-1\). The full symmetric group has two orbitals on ordered pairs (diagonal/off-diagonal) and a regular cyclic group has \(n\) orbitals (differences), proving the stated examples. The independent-coordinate group has one grid orbit and two center orbits, yielding rank zero.

For \(\langle\tau\rangle\), the row and column centers form \(n\) orbits, grid vertices form \(n(n+1)/2\) orbits (unordered pairs), and subdivided edges form \(n^2\) orbits, so the cycle rank is \(n^2-n-n(n+1)/2+1=\binom{n-1}{2}\), including zero at \(n=2\).

**4. Fixed spaces of every subgroup.** Equivariance also restricts the same strong deformation retraction to \(X_{m,n}^H\searrow T_{m,n}^H\). Because there are no edge inversions, the fixed set of the graph is exactly its subgraph spanned by its pointwise-fixed vertices and pointwise-fixed edges. For side-preserving \(H\), the fixed row centers are labeled by the \(f_H\) common fixed row labels, the fixed column centers by the \(g_H\) fixed column labels, and the fixed grid vertices by pairs of those labels. They form a subdivision of \(K_{f_H,g_H}\) when both parameters are positive, or the asserted isolated centers otherwise. If \(H\) has a swapping element, no row or column center can be fixed by all \(H\) (a swapping element always exchanges center types). Therefore only the grid positions fixed by all of \(H\) remain, with no edges. For the pure swap, exactly \((i,i)\) are fixed, giving \(n\) isolated points.

**5. Integral module and trace.** Orient each unsubdivided edge of \(K_{m,n}\) from its row vertex to its column vertex. Integral cycles are exactly matrices \((z_{ij})\in\mathbb Z^{m\times n}\) with every row sum and every column sum zero. The natural inclusion \(U_m\otimes U_n\hookrightarrow\mathbb Z^m\otimes\mathbb Z^n\) identifies its image with this kernel: the elementary rectangles \((e_i-e_m)\otimes(e_j-e_n)\), for \(i<m\), \(j<n\), form an integral basis. Row and column permutations act on this lattice by the obvious tensor permutations. Under coordinate swap the oriented edge from row \(i\) to column \(j\) goes to the edge from column \(i\) to row \(j\), which reverses its orientation. Thus the integral action is \(-\mathrm{flip}\). The trace of a permutation on \(U_d\otimes\mathbb Q\) is \(f(\pi)-1\). For balanced swapped elements, the elementary identity \(\operatorname{tr}((A\otimes B)\mathrm{flip})=\operatorname{tr}(AB)\) yields \(-[f(\pi\sigma)-1]\). This proves the complete rational character and the remaining homology statement.

## Verification

The accompanying `verify.py` is standalone Python 3 code using only the standard library. It reconstructs independently all independent sets by the pairwise graph adjacency definition for grid sizes two through four, calculates their reduced Betti numbers, enumerates representative subgroups including simultaneous permutations and coordinate swap, and compares quotient homology calculated directly on the barycentric subdivision with the predicted orbit graph ranks. It checks the simplex retraction's exact idempotence, permutation symmetry and restriction to the star tree using rational arithmetic, and compares swap-character formulas against direct signed graph-edge Lefschetz traces for all label permutations through size six. The exact captured result is in `verify_output.txt`:

`ALL_VERIFY_OK cases= 60 independence_faces= 369 barycentric_quotient_cells= 7038 local_retraction_checks= 104384 swap_character_checks= 872`

These finite checks are corroboration. The proof in Steps 1–5 supplies the unrestricted parameter and subgroup arguments; the computations are not claimed as exhaustive in larger sizes or as independent validation.

## Relationship to prior work

Goyal, Shukla and Singh (arXiv:1905.06926, Proposition 3.2 in the accessible preprint) proved the **ordinary** homotopy equivalence \(\operatorname{Ind}(K_m\times K_n)\simeq\bigvee^{(m-1)(n-1)}S^1\); that sphere count is explicitly not claimed as new. Their paper on line-graph clique complexes (arXiv:2009.12130, Lemma 3.2, Corollary 3.3 and Proposition 3.8) also obtains this ordinary type, via the equivalence to \(\operatorname{Cl}(L(K_{m,n}))\) and the ordinary nerve theorem. This stronger **nonequivariant prior coverage** was checked directly and is not ignored. The 2026 Mycielskian work of Carnero Bravo (arXiv:2601.13432, Corollary 8, first posted 2026-01-19) uses the same ordinary complex as a homotopy-theoretic input.

The present claim concerns something these prior statements do **not determine**: one concrete symmetry-commuting strong deformation retraction, the actual homotopy types and free fundamental groups of **every** symmetry-subgroup quotient (including the swap group), the complete subgroup fixed-space classification, and integral symmetry operators. An arbitrary nonequivariant equivalence cannot be passed through arbitrary fixed-point or orbit-space functors. These are naturally motivated refinements of the known ordinary result. A standard equivariant nerve argument might give another route to an equivariant equivalence, so a not-yet-indexed formulation remains a genuine originality risk; no exclusivity or independent verification is asserted.

## Limitations

The result concerns two complete-graph factors and their natural coordinate symmetry groups, not arbitrary graph products or arbitrary actions on an unrelated graph. The proof does not classify higher-dimensional generalized Mycielskian complexes. It gives homotopy equivalences of quotients, not canonical equivalences preserving additional metric data. No systematic independent external audit has been performed.

## References

1. S. Goyal, S. Shukla and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926 (first posted 2019-05-16), Proposition 3.2; later published in *Contributions to Discrete Mathematics* 16 (2021).
2. S. Goyal, S. Shukla and A. Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130 (first posted 2020-09-25), Lemma 3.2, Corollary 3.3 and Proposition 3.8.
3. A. Carnero Bravo, *Independence complexes of generalized Mycielskian graphs*, arXiv:2601.13432 (first posted 2026-01-19), Corollary 8.
4. O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401 (first posted 2023-07-23), broader categorical-product context (different graph families).
