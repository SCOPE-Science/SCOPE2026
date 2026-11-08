# Integral order-three homology lattices at the triple-saturation threshold of cycle powers

## Finding
For every integer \(m\ge2\), let \(G_m=C_{3m}^{m-1}\) denote the graph on \(\mathbb Z/(3m)\) in which distinct vertices are adjacent at cyclic distance at most \(m-1\). Let \(X_m=\operatorname{Ind}(G_m)\), and let \(g\) be the order-three simplicial automorphism \(i\mapsto i+m\) of \(X_m\). Define \(R=\mathbb Z[C_3]=\mathbb Z[g]/(g^3-1)\), \(N=1+g+g^2\), and \(S=R/(N)\cong\mathbb Z[\zeta_3]\), with \(g\) acting by multiplication by \(\zeta_3\) on \(S\). Then the complete integral \(C_3\)-homology module is

\[
\widetilde H_1(X_m;\mathbb Z)\cong R^{\binom{m-1}{2}}\oplus S^{m-1},\qquad
\widetilde H_j(X_m;\mathbb Z)=0\quad(j\ne1).
\]

In particular, the first Betti number is \((m-1)(3m-2)/2\). The order-three generator has rational trace \(1-m\), and the invariant subgroup has rank \(\binom{m-1}{2}\). The reduction modulo three has exactly \(\binom{m-1}{2}\) Jordan blocks of length three and \(m-1\) blocks of length two. This specifies an integral module rather than only a rank or rational character.

## Assumptions and scope
The power \(C_{3m}^{m-1}\) is the ordinary graph power in its shortest-path metric. An independent simplex contains vertices with pairwise circular separation at least \(m\). All statements hold for every integer \(m\ge2\), with integral simplicial chains carrying the indicated rotation. The module identification is noncanonical: it uses the residue-zero vertex orbit and selected edges as spanning-tree choices.

## Proof
**Simplices.** Every independent triple has three circular gaps at least \(m\) whose sum is \(3m\), so each gap equals \(m\). Consequently, its vertices are \(\{i,i+m,i+2m\}\), for exactly \(m\) values \(0\le i<m\). No four vertices are independent. Writing \(v_{i,t}=i+tm\) for \(0\le i<m\) and \(t\in\mathbb Z/3\), all one-simplices are the three edges in each exceptional triple and, for every \(0\le i<j<m\), precisely the three edges \(\{v_{i,t},v_{j,t+1}\}\) for \(t\in\mathbb Z/3\). For the latter assertion, the clockwise gap from \(v_{i,t}\) to \(v_{j,t+1}\) is \(m+j-i\), with opposite gap \(2m-j+i\), both at least \(m\). The alternative layer offsets have a gap less than \(m\). In particular, the one-skeleton is connected.

**Equivariant cellular presentation.** Orient the within-orbit edges from \(v_{i,t}\) to \(v_{i,t+1}\), and the between-orbit edges from \(v_{i,t}\) to \(v_{j,t+1}\) for \(i<j\). Rotation preserves these orientations. Denote their orbit generators by \(\ell_i\) and \(e_{ij}\); denote the vertex orbits by \(v_i\). The cellular chain groups and differentials are

\[
C_0\cong R^m,\quad C_1\cong R^{\binom m2}\oplus R^m,\quad C_2\cong\mathbb Z^m,\qquad
\partial e_{ij}=g v_j-v_i,\quad\partial\ell_i=(g-1)v_i,\quad\partial T_i=N\ell_i.
\]

Each two-cell is fixed by rotation with orientation preserved, hence its \(\mathbb Z\)-chain generator is a trivial \(C_3\)-module; its boundary is indeed \(\ell_i+g\ell_i+g^2\ell_i\). The \(m\) boundaries have disjoint supports and are \(\mathbb Z\)-independent. Thus \(\widetilde H_2=0\), and quotienting one-chains by their image gives
\[
C_1/\partial C_2\cong R^{\binom m2}\oplus S^m.
\]

**Exact elimination over the integral group ring.** For \(j=1,\ldots,m-1\), put \(b_j=g v_j-v_0\). The elements \(v_0,b_1,\ldots,b_{m-1}\) form an \(R\)-basis of \(C_0\) because \(g\) is a unit. The edges \(e_{0j}\) map to the respective \(b_j\), so these \(m-1\) source/target pairs cancel by integral \(R\)-linear row-column operations. The residual source is \(R^q\oplus S^m\), with \(q=\binom{m-1}{2}\), and its target is the free rank-one module \(R v_0\). After eliminating the \(b_j\) coordinates, the boundary is \((g-1)\phi\), where \(\phi:R^q\oplus S^m\to S\) is the well-defined \(R\)-linear map with coefficients \(g^{-1}\) on every remaining \(e_{ij}\), \(g^{-1}\) on \(\ell_j\) for \(j>0\), and \(1\) on \(\ell_0\). Here an element of \(S\) maps to \(R\) by multiplication by \(g-1\); this is well-defined because \((g-1)N=0\).

Multiplication by \(g-1\) embeds \(S=R/(N)\) into \(R\): if \((g-1)a=0\), comparison of the three coefficients of \(a\) shows \(a\in\mathbb Z N\). Thus the residual kernel is exactly \(\ker\phi\). Since \(\ell_0\) occurs with unit coefficient \(1\), the map \(\phi\) splits, and all other generators are freely adjusted by suitable multiples of \(\ell_0\). Therefore
\[
\ker\phi\cong R^q\oplus S^{m-1},
\]
proving the claimed integral \(C_3\)-module isomorphism. As the one-skeleton is connected and no chains exist in degrees above two, no other reduced integral homology occurs.

**Character and modular consequences.** As a free abelian group, \(R\) has rank three and \(S\) rank two, giving rank \(3q+2(m-1)=(m-1)(3m-2)/2\). The trace of \(g\) on \(R\) is zero and on \(S\) is \(-1\). A regular summand has one invariant generator, while \(S\) has none. Finally modulo three, the regular summand becomes a length-three unipotent Jordan block, whereas \(S\) becomes a length-two block: its annihilator \(N\) reduces to \((g-1)^2\), and \(g^3-1\) reduces to \((g-1)^3\).

## Verification
The attached standalone program `verify_integral_cyclic_triplets.py` independently enumerates every edge and triangle of the defined simplicial complex for \(2\le m\le8\); checks all integral chain identities and simplicial rotation actions; computes boundary ranks modulo two, three and five; and independently extracts the mod-three Jordan block ranks from the actual homology action. All tests pass. These finite checks test the chain presentation; the preceding integral group-ring elimination proves the arbitrary-parameter theorem.

## Relationship to prior work
Adamaszek's *Splittings of independence complexes and the powers of cycles* (first posted 2011-06-30, arXiv:1106.6250) treats the same underlying class of cycle-power independence complexes and establishes homotopy splitting results. Its Theorem 1.1 applies to the large-cycle regime \(n\ge5r+4\), whereas this finding is at the different parameter line \(n=3r+3\), and its subject is a rotation-equivariant **integral module**. The previously known nonequivariant framework and graph-power definitions are not presented as new. Related work on dihedral characters of cycle matching complexes, cut complexes of powers of cycles, and independence complexes of other graphs concerns different simplicial objects or different group actions. None of the inspected sources supplied the above exact \(R\)-plus-\(S\) decomposition. Absence from inspected literature does not establish publication priority.

## Limitations
The result describes only the order-three subgroup generated by rotation through one third of the cycle; it does not classify the action of the full cyclic or dihedral automorphism group or its equivariant homotopy type. The proof is for the exact triple-saturation line, not all graph powers. Equivalence to an unindexed earlier calculation cannot be ruled out. The finite script does not replace the uniform algebraic proof.

## References
1. M. Adamaszek, *Splittings of independence complexes and the powers of cycles*, arXiv:1106.6250 (first submitted 2011-06-30), https://arxiv.org/abs/1106.6250 and https://arxiv.org/html/1106.6250v4 .
2. D. Kozlov, investigations of independence complexes of paths and cycles, as cited in Adamaszek, Section 1. The parameter and topological scope comparisons use the full-text Section 6 of reference 1.
