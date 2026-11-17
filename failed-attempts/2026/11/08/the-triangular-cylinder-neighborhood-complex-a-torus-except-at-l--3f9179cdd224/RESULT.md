# The triangular-cylinder neighborhood complex: a torus except at length four

## Finding
For every integer \(n\ge3\), let \(G_n=C_3\square C_n\) be the Cartesian product of cycles, where \(C_3=K_3\). Define its **open** Lovász neighborhood complex \(\mathcal N(G_n)\) to comprise all nonempty vertex sets lying in the open neighborhood of some vertex, together with the empty face. Then
\[
\mathcal N(C_3\square C_n)\simeq
\begin{cases}
S^1\vee\bigvee^6 S^2,& n=4,\\
S^1\times S^1,& n=3\text{ or }n\ge5.
\end{cases}
\]
For all \(n\ge3\), there are exactly \(6n\) explicit elementary simplicial collapses from the original three-dimensional complex to a two-dimensional core. Outside the exceptional length four, this core is itself a triangulated orientable torus. In particular the noncyclic Cartesian-product cases with \(3\mid n\), not covered by the standard four-regular circulant theorem, have torus homotopy type.

## Assumptions and scope
The vertex set is \(\mathbb Z/3\mathbb Z\times\mathbb Z/n\mathbb Z\). Two vertices are adjacent if one coordinate agrees and the other differs by \(\pm1\) in its cyclic group. For a vertex \(v=(a,b)\), write
\[
E=(a+1,b),\quad W=(a-1,b),\quad U=(a,b+1),\quad D=(a,b-1),
\]
where coordinates are reduced modulo \(3\) and \(n\), respectively. Its open neighborhood is the four-element set \(Q_v=\{E,W,U,D\}\). The complex is the union of all \(\Delta(Q_v)\). The result is **nonequivariant**, uses the standard geometric realization of the abstract simplicial complex, and applies to every integer \(n\ge3\), including the two small boundaries \(n=3,4\).

## Proof
**1. A uniform sequence of genuine elementary collapses.** The horizontal pair \(P_v=\{E,W\}\) has exactly one common graph neighbor, namely \(v\). Indeed, the two distinct other vertices of the \(C_3\)-layer have \(v\) as their unique common neighbor within that layer, while neighbors outside the layer preserve their distinct first coordinates. Consequently every face of \(\mathcal N(G_n)\) containing \(P_v\) lies in the unique tetrahedron \(Q_v\). Different vertices \(v\) give distinct pairs \(P_v\) and hence disjoint face sets for the collapses below.

First collapse the free triangle–tetrahedron pair \((\{E,W,U\},Q_v)\) for each \(v\); then collapse the free edge–triangle pair \((\{E,W\},\{E,W,D\})\) for each \(v\). The second pair is free because its only remaining possible coface was the displayed triangle. Each operation removes exactly its two listed simplices, and no operation can spoil freeness for a different center. This gives \(2(3n)=6n\) elementary collapses, leaving the two-dimensional complex \(T_n\) with exactly the triangles
\[
\{E,U,D\},\qquad\{W,U,D\},\qquad v\in\mathbb Z_3\times\mathbb Z_n,
\]
and all their faces. The \(6n\) displayed triangles are distinct for every \(n\ge3\). The vertex and triangle counts are \(f_0=3n\) and \(f_2=6n\); its edge count is \(f_1=9n\) when \(n\ne4\), and \(f_1=30\) when \(n=4\).

**2. All lengths other than four yield a torus, not just torus homology.** At any vertex \((a,b)\) of \(T_n\), the six triangles incident there have a link consisting of the consecutive edges
\[
(a-1,b+1)\!\! -\!\! (a-1,b-1)\!\! -\!\! (a,b-2)\!\! -\!\! (a+1,b-1)\!\! -\!\! (a+1,b+1)\!\! -\!\! (a,b+2)\!\! -\!\! (a-1,b+1).
\]
For \(n=3\) and every \(n\ge5\) these six vertices are pairwise distinct. Every vertex link is therefore a simple six-cycle, proving that \(T_n\) is a closed triangulated surface. Its triangles and edges are connected: the diagonal edges \((a,b)\)--\((a+1,b+1)\) and \((a,b)\)--\((a+1,b-1)\) generate the whole group \(\mathbb Z_3\times\mathbb Z_n\), because their sum gives \((2,0)\), which generates the first cyclic factor, and then gives \((0,1)\).

To check orientability globally, lift the triangular core to the infinite square grid. At each lattice point, draw the diamond with corners one unit to the east, west, north and south, triangulated along its north–south diagonal. Diamonds centered at each fixed parity of the coordinate sum tile a copy of the oriented plane, and diamonds of opposite center parity tile a second disjoint plane. Translation by the period lattice \(L=\langle(3,0),(0,n)\rangle\) acts by orientation-preserving translations and interchanges these planes whenever the period has odd coordinate sum. The period \((3,0)\) is odd, so the quotient is one oriented torus, namely the quotient of one plane by the parity-even sublattice of \(L\). The explicit six-cycle links above ensure this quotient gives precisely the abstract complex even for the short period \(3\), rather than a nonsimplicial identification. Alternatively, the standard orientation propagation across adjacent triangles gives an orientation on \(T_n\). Since
\[\chi(T_n)=3n-9n+6n=0,\]
the connected closed orientable surface is a torus. This proves all cases \(n=3\) and \(n\ge5\).

**3. At length four the core is a circle with six two-spheres.** For \(n=4\), the two would-be distinct link vertices \((a,b-2)\) and \((a,b+2)\) coincide. Thus the preceding manifold argument is inapplicable. Instead an explicit complete two-dimensional CW cancellation proves the homotopy type. Label \((a,b)\) by \(4a+b\), for \(0\le a<3\), \(0\le b<4\). The core has twelve vertices, thirty edges, twenty-four triangles. Sort its edges lexicographically and use Kruskal's algorithm in that order to select a spanning tree. Contracting this tree gives one vertex, nineteen oriented one-cells \(g_1,\ldots,g_{19}\) (the non-tree edges in increasing lexicographic order), and twenty-four triangular two-cell relators. Each ascending-oriented triangle \((u,v,w)\) has attaching word \((uv)(vw)(uw)^{-1}\), with each tree edge omitted.

An explicit sequence of eighteen elementary one-cell/two-cell eliminations uses the generators, in order,
\[
11,19,9,18,1,2,3,4,5,6,7,8,14,10,15,12,13,16.
\]
At every step one selected cyclically reduced triangle relator contains the eliminated generator exactly once, so it determines a homotopy-preserving CW cancellation. All eliminated generators map to the trivial word except
\[
g_{10}\mapsto g_{15},\quad g_{12}\mapsto g_{16},\quad g_{13}\mapsto g_{17},\quad g_{16}\mapsto g_{17}.
\]
After cyclic reduction and substitution, exactly six empty relators and one generator \(g_{17}\) remain. The resulting CW complex is a circle with six two-cells attached by nullhomotopic maps. It has homotopy type \(S^1\vee\bigvee^6S^2\). The accompanying exact verifier regenerates the spanning tree, relators and all eighteen legal cancellations rather than treating the displayed output as an unverified assertion.

## Verification
The standalone Python 3 script `verify.py` uses only the standard library. It reconstructs the open neighborhoods and complete original simplicial face sets from adjacency for every integer \(3\le n\le18\), checks each of the \(6n\) elementary free-face collapses individually and compares the exact surviving core with the displayed triangle formula. For \(n\ne4\) it checks all vertex links, edge degrees, connectedness, orientation propagation, Euler characteristic, and independent mod-two boundary ranks. For \(n=4\), it constructs the lexicographic spanning-tree presentation and checks the eighteen one-relator eliminations and all six empty residual relators. The recorded output is in `verification_output.txt`. These finite checks support the proof but do not establish its infinite quantifier independently.

## Relationship to prior work
Matsushita's general study of open-neighborhood fundamental groups [1] provides the fundamental-group framework but does not classify this one-parameter family. Shukla's primary full text [2, Theorems 2.2–2.6] already classifies open neighborhoods for connected four-regular **circulant** graphs. The products \(C_3\square C_n\) with \(\gcd(3,n)=1\) admit cyclic descriptions and overlap that theorem; in particular its garland-of-two-spheres case applies at \(n=4\). These overlapping conclusions are not claimed as independently new. For \(3\mid n\) the natural group of translations \(\mathbb Z_3\times\mathbb Z_n\) is noncyclic, and the circulant theorem does not automatically apply; this statement extends the classification uniformly to those noncyclic products and supplies explicit collapses throughout.

A later published exact toroidal-grid collapse theorem [3] applies to square-lattice quotients with minimum nonzero Manhattan-period length at least five. Its hypotheses exclude the present period-three family, and its proof does not settle the exceptional four-cycle. A published theorem on \(K_m\square C_n\) [4] requires \(m\ge4\) and \(n\ge5\); our first factor is \(K_3\), so that theorem does not imply this result. An open-neighborhood calculation for rook graphs [5] concerns integral homology only in degrees at least three and a relative cofiber, not this homotopy type. The closed-neighborhood calculations in [6] define a different simplicial complex. No inspected source was found to imply this full all-parameter assertion, particularly its \(3\mid n\) cases; unindexed equivalent results remain possible.

## Limitations
This concerns only products with a triangular first factor; arbitrary lattice quotients of shortest period three and other small-period products are not classified. The equivalences are nonequivariant and no persistence filtration is claimed. The conclusions for cyclic products overlap existing work and are included only to make the family classification complete. The exact small-instance verifier is corroborative rather than an infinite proof. Literature priority is subject to independent checking.

## References
[1] T. Matsushita, *Fundamental groups of neighborhood complexes*, first public arXiv posting 2012-10-10, arXiv:1210.2803, https://arxiv.org/abs/1210.2803 .
[2] S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, first public posting 2018-02-13, arXiv:1802.04526v2, especially Theorems 2.2–2.6, https://arxiv.org/html/1802.04526v2 .
[3] *Toroidal grid neighborhood complexes collapse to one or two tori*, public mathematical result dated 2026-10-11; exact hypothesis on shortest periods and explicit two-pair local collapse inspected.
[4] *Mixed-dimensional neighborhood homotopy of complete-graph cycle products*, public mathematical result dated 2026-10-11; its assumptions require the clique factor of order at least four.
[5] *Row–column boundary spheres control higher neighborhood homology of rook graphs*, public mathematical result dated 2026-10-11; its conclusion determines relative and higher homology but not the full homotopy type.
[6] T. Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608, 2025-11-16, https://arxiv.org/abs/2511.12608 .
