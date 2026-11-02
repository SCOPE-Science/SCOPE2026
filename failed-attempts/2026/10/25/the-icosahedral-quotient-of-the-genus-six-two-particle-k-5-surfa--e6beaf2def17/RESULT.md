# The icosahedral quotient of the genus-six two-particle \(K_5\) surface

## Finding
Let \(G=K_5\) be the complete graph on five labeled vertices. The ordered deleted-product cubical complex \(X=D_2^{\mathrm{ord}}(G)\) is the subcomplex of \(G\times G\) having cells \(\sigma\times\tau\) with disjoint closed graph cells. The even vertex permutations form \(A_5\), acting diagonally on \(X\). This action preserves orientation. Its quotient has underlying topological space \(S^2\) and exactly four branch points, with ramification indices
\[
(2,2,2,3).
\]
In detail, every nonidentity double transposition fixes six points of \(X\); every three-cycle fixes two; every five-cycle fixes none. The branch locus consists of exactly three orbits of size \(30\) (order-two stabilizers) and one orbit of size \(20\) (order-three stabilizers). Thus the quotient orbifold has signature \((0;2,2,2,3)\).

For clarity on the symmetry, the full vertex-permutation group \(S_5\) acts on the primitive orientation class by \(\operatorname{sgn}\). The independent involution exchanging particle labels acts by \(-1\). The known nonequivariant genus-six surface classification is not claimed as new.

## Assumptions and scope
All graph edges have the usual closed-cell topology. For each oriented edge \(e=\{a,b\}\) with \(a<b\), use the orientation \(a\to b\); orient the square \(e\times f\) by the first particle's edge followed by the second's. The graph automorphism group is \(S_5\), and \(A_5\) is its even subgroup of order \(60\). The quotient statement refers to the compact Abrams deleted-product *cubical surface*, not to a claim that the full open space of distinct graph points is itself a closed surface. The latter is equivariantly homotopy equivalent to \(X\) via the standard configuration-space retraction. The orbifold structure is that of the finite orientation-preserving action on \(X\).

## Proof
**1. The surface and its fundamental cycle.** Its cubical cell numbers are \((20,60,30)\) in dimensions zero through two, giving Euler characteristic \(-10\). The one-skeleton is connected; each of the sixty one-cells lies in exactly two distinct squares, and each vertex link is a circular graph. Therefore \(X\) is a closed connected surface. For disjoint ordered edges \(e=(a,b)\), \(f=(c,d)\), let \(r\) be the unique vertex outside their four endpoints and let \(\epsilon(a,b,c,d,r)\) be the sign of the displayed permutation of the five vertex labels, relative to increasing order. Then
\[
z=\sum_{e\cap f=\varnothing}\epsilon(a,b,c,d,r)[e\times f]
\]
is a cellular two-cycle: along every codimension-one face, the two incident squares appear with opposite signed coefficients. Every coefficient is \(\pm1\), so \(z\) is primitive. Since \(X\) has no cells above dimension two and its square-incidence adjacency is connected, every two-cycle is an integral multiple of \(z\). Thus \(H_2(X;\mathbb Z)=\mathbb Z[z]\), and \(X\) is orientable of genus \(6\). This surface type was already known.

**2. Orientation character.** An element \(g\in S_5\) permutes five labels. Its action on the oriented square corresponding to disjoint ordered edges introduces the respective two edge-orientation signs. The five-label alternating symbol introduces the reciprocal edge-orientation signs and the global factor \(\operatorname{sgn}(g)\). Therefore \(g_*z=\operatorname{sgn}(g)z\). Exchanging the two coordinate factors reverses square orientation, whereas switching the two ordered blocks of two labels in the alternating symbol is even. Hence particle exchange sends \(z\mapsto-z\). In particular, every element of \(A_5\) preserves the surface orientation.

**3. Fixed-point counts.** For any graph automorphism \(g\), the known coordinate-projection isomorphism \(H_1(X;\mathbb Q)\simeq H_1(G;\mathbb Q)\oplus H_1(G;\mathbb Q)\) is diagonal-equivariant. The graph-cycle trace is computed from the one-dimensional cellular Lefschetz identity:
\[
\operatorname{tr}(g_*\mid H_1(G;\mathbb Q))=1-\#\operatorname{Fix}_V(g)+\operatorname{tr}(g\mid C_1(G;\mathbb Q)),
\]
where an individually fixed edge contributes \(+1\) or \(-1\) depending on whether its endpoints are preserved or exchanged. For a double transposition, a three-cycle, and a five-cycle the resulting graph-cycle traces are, respectively, \(-2,0,1\). Because \(g\in A_5\) acts trivially on \(H_2(X;\mathbb Q)\), its Lefschetz number on \(X\) is
\[
L(g)=2-2\operatorname{tr}(g_*\mid H_1(G;\mathbb Q))=6,2,0
\]
in the three cases. A nonidentity, orientation-preserving finite-order PL homeomorphism of a closed oriented surface has only isolated fixed points, each of local index \(+1\). Thus the Lefschetz numbers are exactly the fixed-point counts stated above.

**4. Stabilizers and quotient.** Stabilizers of points in a faithful orientation-preserving finite surface action are cyclic: locally, they embed in the planar rotation group. The only element orders in \(A_5\) are \(1,2,3,5\); elements of order five fix no point. Hence each nontrivial stabilizer has order two or three. There are fifteen involutions, each fixing six points, so there are \(90\) points of stabilizer order two, forming \(90/30=3\) orbits. There are twenty three-cycles, each fixing two points, and each point with stabilizer order three is counted twice; hence there are \(40/2=20\) such points, forming one orbit. If \(h\) is the genus of the quotient, Riemann–Hurwitz gives
\[
-10=60\left(2-2h-3\left(1-\frac12\right)-\left(1-\frac13\right)\right)
=-10-120h.
\]
Thus \(h=0\), and the entire orbifold signature follows.

## Verification
The standalone `check_k5.py` reconstructs all \(20\) vertices, \(60\) oriented edges and \(30\) squares, verifies consecutive cellular boundaries, circular vertex links and the connected square-adjacency structure. It constructs the primitive orientation cycle and checks the signed cellular action of all \(120\) vertex permutations and both particle-label choices (\(240\) actions). It also checks the Lefschetz traces and the three fixed-point counts, branch-orbit multiplicities, and exact rational Riemann–Hurwitz equality. Running `python3 check_k5.py` prints four `PASS`/summary lines. The universal fixed-point assertion uses the standard theorem on finite-order orientation-preserving surface homeomorphisms, not finite-size extrapolation.

## Relationship to prior work
Barnett and Farber already established the orientable genus-six model of the ordered two-particle configuration of \(K_5\), its Betti numbers, the coordinate-projection homology description and an explicit integral top class in the intersection pairing. Those properties are background, **not** new findings here. The present result identifies the full \(A_5\)-quotient as a branched sphere, giving every stabilizer order, all branch-orbit sizes and the exact orbifold signature. Those orbit and quotient statements do not appear in the inspected treatment of the \(K_5\) example. The general graph-configuration literature provides the cubical framework; it does not by itself tabulate this quotient. Similar genus-six \(A_5\)-actions elsewhere do not automatically identify the action induced by graph-label permutations.

## Limitations
The result concerns this specific compact two-particle deleted product and its natural \(A_5\)-action. It does not classify all actions of \(A_5\) on genus-six surfaces, their complex-analytic structures, or quotient orbifolds for other graph configurations. The conclusion is compatible with, and uses, previously established nonequivariant topology. An equivalent calculation in uncatalogued literature remains possible. Only a self-review has been performed; there is no independent validation.

## References
1. Kathryn Barnett and Michael Farber, *Topology of configuration space of two particles on a graph, I*, arXiv:0903.2180v1, 12 March 2009, especially §§1 and 4.1. https://arxiv.org/abs/0903.2180
2. Byung Hee An, Gabriel C. Drummond-Cole, and Ben Knudsen, *Subdivisional spaces and graph braid groups*, arXiv:1708.02351v1, 8 August 2017. https://arxiv.org/abs/1708.02351
3. Daniel Berlyne, *Graph of groups decompositions of graph braid groups*, arXiv:2209.03860v1, 8 September 2022. https://arxiv.org/abs/2209.03860
4. Standard surface Lefschetz index theorem and Riemann–Hurwitz formula for finite orientation-preserving surface actions.
