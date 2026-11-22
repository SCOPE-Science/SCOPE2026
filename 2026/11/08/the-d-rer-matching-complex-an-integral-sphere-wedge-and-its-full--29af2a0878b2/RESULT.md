# The rational dihedral homology character of the Dürer matching complex

## Finding
Let \(G=GP(6,2)\) be the Dürer graph, with vertices \(u_i,v_i\), \(i\in\mathbb Z/6\mathbb Z\), and edges \(\{u_i,u_{i+1}\}\), \(\{u_i,v_i\}\), and \(\{v_i,v_{i+2}\}\). Its ordinary matching complex \(K=\mathcal M(G)\) has graph edges as simplicial vertices and pairwise disjoint edge sets as simplices. The known integral homotopy equivalence \(K\simeq\bigvee^{22}S^3\) was already established in the October 18, 2026 calculation cited below. The finding here is the **complete rational homology character** of its natural full dihedral action.

Under \(r(u_i)=u_{i+1}\), \(r(v_i)=v_{i+1}\), \(s(u_i)=u_{-i}\), and \(s(v_i)=v_{-i}\), the full graph automorphism group is \(D_6=\langle r,s:r^6=s^2=1,srs=r^{-1}\rangle\). Its action on \(\widetilde H_3(K;\mathbb Q)\) has character
\[
(\chi(1),\chi(r),\chi(r^2),\chi(r^3),\chi(r^4),\chi(r^5))
=(22,0,-2,6,-2,0),\qquad
\chi(r^ks)=0\quad(0\le k<6).
\]
Let \(\lambda_{a,b}\) be the one-dimensional rational representation \(r\mapsto a\), \(s\mapsto b\), for \(a,b\in\{\pm1\}\), and \(V_j\) the rational two-dimensional irreducible representation with rotation trace \(2\cos(2\pi jk/6)\) at \(r^k\) and reflection trace zero, for \(j=1,2\). Then
\[
\widetilde H_3(K;\mathbb Q)\cong
2\lambda_{1,1}\oplus2\lambda_{1,-1}\oplus
\lambda_{-1,1}\oplus\lambda_{-1,-1}\oplus3V_1\oplus5V_2.
\]
Consequently the globally fixed rational third-homology subspace is **two-dimensional**; the half-turn has trace \(6\), and all six reflections have trace zero.

## Scope and proof
The statement concerns one fixed 12-vertex, 18-edge simple graph and the **ordinary** matching complex, not its perfect-matching-extendability or induced-matching complex. The homotopy conclusion is cited as established prior art; the character and representation decomposition are the results singled out here. No integral \(\mathbb Z[D_6]\)-lattice identification or equivariant homotopy splitting is claimed.

**Full symmetry group.** The six inner vertices lie in the two inner triangles, while the six outer vertices lie on an induced six-cycle and on no triangle. Therefore every automorphism preserves the two layers, restricts to an automorphism of the outer cycle, and uniquely determines the image of each inner vertex through its spoke. All six rotations and six reflections extend, giving exactly \(D_6\).

**Chain-level trace.** There are \(1037\) nonempty matchings. Their counts by simplex dimension \(0,1,2,3,4,5\) are
\[
(18,117,334,402,156,10).
\]
For each \(g\in D_6\), let \(g_E\) be the induced permutation of the graph's eighteen edges. The simplicial Lefschetz number is the exact integer
\[
L(g)=\sum_{\substack{\varnothing\ne\sigma\in K\\g_E(\sigma)=\sigma}}
(-1)^{|\sigma|-1}\operatorname{sgn}(g_E|_\sigma).
\]
Here the sign is the permutation sign on the ordered edge indices within each invariant simplex. A direct exhaustive enumeration of the finite simplicial complex and all twelve symmetries gives
\[
(L(1),L(r),L(r^2),L(r^3),L(r^4),L(r^5))=(-21,1,3,-5,3,1),
\quad L(r^ks)=1\ (0\le k<6).
\]
The cited integral wedge equivalence implies \(H_0(K;\mathbb Q)\cong\mathbb Q\), \(\widetilde H_3(K;\mathbb Q)\cong\mathbb Q^{22}\), and all other reduced rational homology vanishes. By the Lefschetz trace formula \(L(g)=1-\chi(g)\), yielding the displayed character.

**Representation multiplicities.** For a one-dimensional character \(\lambda_{a,b}\), its multiplicity in \(H_3\) is
\[
\frac1{12}\sum_{k=0}^5\bigl(\chi(r^k)a^k+\chi(r^ks)a^kb\bigr)
=\frac{22-2a^2+6a^3-2a^4}{12}
=\begin{cases}2,&a=1,\\1,&a=-1.\end{cases}
\]
For \(V_1,V_2\), the respective character inner products are \(3,5\). These nonnegative integer multiplicities account for all \(22\) dimensions. The trivial constituent \(\lambda_{1,1}\) occurs twice, proving the invariant-dimension statement.

**Independent verification of the homotopy premise.** The integral homotopy type does not follow merely from rational Betti numbers. As a secondary reproduction, lexicographically enumerate the 18 edges and greedily pair each remaining simplex missing edge \(j\) with its still-unpaired compatible coface containing it. The 18 phase sizes are
`[204,103,54,26,14,45,23,10,7,0,11,0,0,0,5,2,1,1]`.
The resulting \(506\) pairs form an acyclic partial matching on the \(1037\) nonempty simplices, verified by sorting all \(3684\) directed codimension-one incidences. Its critical cells are one vertex, 23 three-cells, and one four-cell. Exact integral cancellation through \(506\) signed unit pivots gives the four-cell a primitive boundary with two coefficients \(+1\). The associated CW model is \(\bigvee^{23}S^3\) with a four-cell attached by a primitive element of \(\pi_3(\bigvee^{23}S^3)=\mathbb Z^{23}\), hence is homotopy equivalent to \(\bigvee^{22}S^3\). This is a second proof of an **already published** premise, not a new sphere-wedge theorem.

## Verification and limitations
The frozen package's `verify.py` and `rank_independent.py` specify reproducible finite checks. For the character, only the exact simplicial face list, the induced edge permutations, and oriented fixed-face signs are needed. Exhaustion of all \(1037\) nonempty simplices and all \(12\) group elements proves the character for this fixed graph; it is not extrapolation to other graphs. An independently authored check reproduces the full character, representation multiplicities, acyclic Morse data, and primitive integral attaching vector. Other graph families and integral representation-lattice structures remain outside scope.

## Relationship to prior work
The integral \(22\)-sphere homotopy classification for precisely this ordinary Dürer matching complex was already published on **October 18, 2026**, in *Shortest octahedral carriers and integral orbit obstructions in the Dürer matching complex*. That result also classifies \(93\) octahedral carriers and their eleven \(D_6\)-orbits, as well as integral orbit-lattice obstructions. Those are **prior results**, and neither the homotopy type nor the lattice facts are presented here as new. The earlier statement does not give the twelve orientation-sensitive homology traces or their six-constituent rational character decomposition; carrier orbit sizes and lattice ranks alone do not determine these signed traces.

Marietti–Testa's matching-complex sphere-wedge result applies to forests, and Bayer–Jelić Milutinović–Vega's to outerplanar graphs; the Dürer graph is cubic and not outerplanar. Bayer–Goeckner–Jelić Milutinović classify matching complexes that are homology manifolds, unlike this nonpure matching complex. The November 17, 2026 paper of Youngsoo Kim concerns **vertex-independence** of \(GP(n,2)\), and perfect-matching complexes of antiprism graphs, not the ordinary Dürer matching complex's dihedral homology character. Forman's discrete Morse theorem and the simplicial Lefschetz formula supply methods, not the evaluated character. Older unindexed equivariant calculations remain a priority risk; the statement does not claim exhaustive historical novelty.

## References
1. *Shortest octahedral carriers and integral orbit obstructions in the Dürer matching complex*, publication dated October 18, 2026, https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-shortest-octahedral-carriers-and-integral-orbit-obstructions-in--2058dcbfce11/RESULT.md.
2. M. Marietti and D. Testa, *A Simple Uniform Approach to Complexes Arising from Forests*, arXiv:0705.1461, §4.4.
3. M. Bayer, M. Jelić Milutinović and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601v2, Theorem 2 and Proposition 4.
4. M. Bayer, B. Goeckner and M. Jelić Milutinović, *Manifold Matching Complexes*, arXiv:1906.03328.
5. Y. Kim, *Perfect matching complexes of antiprism graphs and independence complexes of generalized Petersen graphs GP(n,2)*, arXiv:2611.22021v1 (November 17, 2026).
6. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
