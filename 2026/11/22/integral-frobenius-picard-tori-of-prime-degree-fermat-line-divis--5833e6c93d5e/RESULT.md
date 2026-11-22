# Integral Frobenius Picard tori of prime-degree Fermat line divisors

## Finding
Fix an odd prime \(\ell\ge5\) and a finite field \(k=\mathbb F_q\) of characteristic \(p>\ell\). On the smooth Fermat surface
\[
X_\ell:\qquad X_0^\ell+X_1^\ell+X_2^\ell+X_3^\ell=0\subset\mathbb P_k^3,
\]
let \(B_\ell\) be the reduced union of its \(3\ell^2\) standard coordinate-pairing lines. Let \(J=\operatorname{Pic}^0_{B_\ell/k}\) denote the connected Picard group scheme of this reduced singular curve. Put
\[
d=\operatorname{ord}_{\ell}(q),\qquad R=3\ell^3+3\ell^2-6\ell,\qquad u=3\ell(\ell-1)(\ell-2).
\]
Then \(d\mid\ell-1\), hence \(d\mid R\), and:

1. The smooth connected unipotent radical of \(J\) is the split vector group \(U\cong\mathbb G_a^u\). The torus quotient, as an *actual integral algebraic-group isomorphism* over \(k\), is
\[
\boxed{J/U\cong\mathbb G_m\times\Bigl(\operatorname{Res}_{\mathbb F_{q^d}/\mathbb F_q}\mathbb G_m\Bigr)^{R/d}.}
\]
Here \(d=1\) is allowed and \(\operatorname{Res}_{k/k}\mathbb G_m=\mathbb G_m\), yielding \(\mathbb G_m^{R+1}\).
2. If \(C_n\) denotes an abstract cyclic group of order \(n\), there is a (noncanonical) finite-group isomorphism
\[
\boxed{J(k)\cong(k,+)^u\times C_{q-1}\times C_{q^d-1}^{R/d}.}
\]
In particular, \(\#J(k)=q^u(q-1)(q^d-1)^{R/d}\).
3. The curve \(B_\ell\) has arithmetic genus \(6\ell^3-6\ell^2+1\). In degree five it has genus \(601\), unipotent dimension \(180\), and torus types
\[
\begin{array}{c|c}
d&J/U\\\hline
1&\mathbb G_m^{421}\\
2&\mathbb G_m\times (\operatorname{Res}_{\mathbb F_{q^2}/k}\mathbb G_m)^{210}\\
4&\mathbb G_m\times (\operatorname{Res}_{\mathbb F_{q^4}/k}\mathbb G_m)^{105}.
\end{array}
\]

The geometry of the line arrangement and its point-count and zeta formulas were available previously; the classification asserted here is the **integral arithmetic Picard torus and rational-point group**, for all prime degrees and every possible Frobenius order.

## Assumptions and scope
The degree \(\ell\) is an odd prime at least five, and the characteristic \(p\) is strictly greater than \(\ell\). The divisor comprises the standard lines only; equality with the total geometric line locus is not needed. For each of the three partitions of four coordinates into two unordered pairs, and each \((a,b)\in(\mathbb Z/\ell)^2\), define the corresponding line by equating coordinates in the two pairs with factors \(-\zeta^a\) and \(-\zeta^b\), where \(\zeta\) is a primitive \(\ell\)-th root of unity. Since \(\ell\) is odd, both factors have \(\ell\)-th power \(-1\). All Picard group schemes refer to the reduced singular curve, not the surface Picard scheme. \(J/U\) is the maximal torus quotient; no canonical splitting of \(J\) as a product of algebraic groups is asserted. Rational-point group isomorphisms are abstract and noncanonical.

## Proof
**1. Geometry and the local Picard contribution.** The standard lines are indexed by three pairing families and two root labels per line. The established exact incidence description [2] shows that their reduced union has \(6\ell\) ordinary \(\ell\)-fold points (two roots-per-coordinate classes in each pairing family), \(3\ell^3\) ordinary nodes from intersections of distinct pairing families, and no other singularities. Each high-multiplicity point has \(\ell\) branches and each node has two. The normalization is the disjoint union of \(3\ell^2\) projective lines. The configuration is connected: within each family, lines with common first or second parameter meet, so each family is connected; distinct families have \(\ell^3\) cross intersections. These statements follow directly from the displayed line equations (or from [2, Proof, Steps 1--4]).

For an ordinary \(m\)-fold planar point, the local normalization-unit quotient has torus dimension \(m-1\) and unipotent dimension \(\binom{m-1}{2}\). Thus the global unipotent radical has dimension \(6\ell\binom{\ell-1}{2}=u\). Since the conductor exponents on a branch are at most \(\ell-1<p\), truncated logarithms identify the principal-unit quotients with vector groups, compatibly with Frobenius. Over a perfect finite field every smooth connected commutative unipotent quotient arising here is split, so \(U\cong\mathbb G_a^u\). Every normalization component has genus zero, so no abelian-variety quotient occurs.

**2. The normalization-incidence graph and its integral cycle lattice.** Let \(\Gamma\) be the bipartite graph having one vertex for each geometric component and one for each geometric singular point, with one edge per branch above that singular point. All edges are oriented from the component vertex to the singular vertex, so Frobenius preserves the edge orientations. Counting gives
\[
\#V=3\ell^2+6\ell+3\ell^3,\qquad \#E=6\ell^2+6\ell^3,
\]
and hence
\[
b_1(\Gamma)=\#E-\#V+1=R+1.
\]
The normalization sequence for multiplicative units, followed by scalar trivializations on the components, identifies the integral character lattice of the torus quotient of \(J\) with \(H_1(\Gamma,\mathbb Z)\) or its integral dual. The permutation-module type obtained below is self-dual, so this convention makes no difference to the isomorphism asserted.

**3. Exact Frobenius action and fixed subgraph.** Put \(a^\ell=-1\) in the form \(a=-\zeta^i\), with \(i\in\mathbb Z/\ell\). Frobenius sends every label \(i\) to \(qi\). If \(d=1\), it acts trivially on every component, point and branch, and the torus is split of rank \(R+1\).

Assume \(d>1\). Since \(\ell\) is prime, any nonzero label, or nonzero tuple of labels, has orbit length exactly \(d\). The fixed part of \(\Gamma\) consists of precisely three lines with parameter pair \((0,0)\), six high-multiplicity points with parameter \(0\), and three cross-family nodes with all root labels \(0\). These twelve fixed vertices have twelve fixed branches. The six high-multiplicity points are leaves, while the three lines and three nodes form a cycle of length six; thus the fixed subgraph is connected and has first Betti number one. Every other vertex and edge has orbit length exactly \(d\).

**4. Equivariant spanning tree and *integral* module decomposition.** First select a spanning tree of the connected fixed subgraph (delete one edge of its hexagon). Contract each Frobenius orbit of the remaining vertices to obtain a quotient graph rooted at the fixed subgraph. Since \(\Gamma\) is connected, choose a rooted spanning tree in this quotient. Build a tree upstairs inductively: for each free vertex-orbit newly reached, add the entire orbit of one edge joining it to an already reached orbit. This adds exactly \(d\) new vertices along \(d\) edges, without introducing a cycle. Together with the fixed subtree it constructs a connected Frobenius-invariant spanning tree \(\mathcal T\subset\Gamma\). The construction does not use a rational change of basis: it is an honest tree in the original graph.

For any graph, the edges outside a spanning tree give a \(\mathbb Z\)-basis of its first integral homology by their oriented fundamental cycles. Because \(\mathcal T\) and the chosen orientations are Frobenius-invariant, Frobenius simply permutes these cycles as it permutes their non-tree edges. There is exactly one fixed non-tree edge (the deleted fixed hexagon edge); every other non-tree edge is in an orbit of length \(d\). Counting ranks gives precisely \(R/d\) such orbits. Therefore, as a lattice with Frobenius action,
\[
\boxed{H_1(\Gamma,\mathbb Z)\cong \mathbb Z\oplus\mathbb Z[C_d]^{R/d}.}
\]
The integral group-ring lattice \(\mathbb Z[C_d]\) is the character module of \(\operatorname{Res}_{\mathbb F_{q^d}/k}\mathbb G_m\); the fixed rank-one summand is that of \(\mathbb G_m\). This proves the asserted torus isomorphism, **not merely an isogeny or an identity of zeta functions**.

**5. Rational points and genus.** The fppf extension \(1\to U\to J\to J/U\to1\) yields an exact sequence on rational points, because \(H^1(k,U)=0\) by Lang's theorem. The \(p\)-group \(U(k)=(k,+)^u\) has order \(q^u\), while \(\mathbb G_m(k)\) and \(\operatorname{Res}_{\mathbb F_{q^d}/k}\mathbb G_m(k)\) are cyclic of orders \(q-1\) and \(q^d-1\), both coprime to \(p\). Since \(J(k)\) is abelian, its primary decomposition proves the stated group isomorphism, without claiming a canonical algebraic-group splitting.

At an ordinary \(\ell\)-fold point the delta invariant is \(\binom\ell2\); at a node it is one. From the normalization formula
\[
p_a(B_\ell)=6\ell\binom\ell2+3\ell^3-3\ell^2+1=6\ell^3-6\ell^2+1.
\]
Independently, \(\dim J=(R+1)+u=6\ell^3-6\ell^2+1\). This agrees with adjunction on the degree-\(\ell\) surface: every line has self-intersection \(2-\ell\), the sum of pairwise intersections gives \(B_\ell^2=9\ell^3\), and \(K_{X_\ell}\cdot B_\ell=3\ell^2(\ell-4)\).

## Verification
The standalone program `verify_frob.py` constructs the component/branch graph with explicit algebraic label equations and all Frobenius edge permutations. For prime degrees \(\ell=5,7,11,13\) it tests representatives of several Frobenius orders, verifies the cardinalities, fixed subgraph and exact stabilizers, *builds the invariant spanning tree*, and checks its acyclicity, connectedness, and Frobenius invariance by an independent union-find implementation. It then counts the fixed and free non-tree edge-orbits. The script ends with `FERMAT_INTEGRAL_PICARD_TORI_VERIFIED`.

The separate `geometry_check.py` derives all seventy-five standard degree-five lines over \(\mathbb F_{11}\), intersects all their pairs by exact finite-field linear algebra, and independently checks precisely \(375\) nodes and \(30\) fivefold points, as well as all three cross-family label formulas. Its final message is `FERMAT_GEOMETRY_VERIFIED`. These finite examples corroborate the exact graph description but do not replace Steps 1--5, which prove the asserted infinite family of integral isomorphisms.

## Relationship to prior work
Schütt--Shioda--van Luijk [1], first available in 2008, give the standard \(3\ell^2\) lines of Fermat surfaces and study their classes in the surface Néron--Severi group; their full-text line parametrization and conclusions concern a **different Picard object** from the connected Picard group scheme of the *singular curve* \(B_\ell\). The previously published normalization and motivic formula [2] already determines its ordinary multiple points, nodes, all-extension rational-point counts and zeta function for every admissible degree; none of those data is claimed to be new. Its theorem and proof do not specify the integral Frobenius character lattice or the isomorphism type of the associated algebraic torus. The earlier integral quartic line-divisor torus theorem [3] treats the even-degree \(48\)-line divisor, whereas the independent odd-degree Ceva plane arrangement [4] has different incidence and Frobenius action. Neither implies the present all-prime-degree, all-Frobenius-order integral torus classification merely by comparing numerical invariants. General normalization and graph-cycle tools are classical; the new evaluated element is the invariant spanning tree establishing an integral induced-module decomposition in this family.

## Limitations
The theorem applies to odd prime degrees and \(p>\ell\). Composite or even degrees, bad characteristics and nonstandard additional Fermat-surface lines are not covered. It describes the connected generalized Jacobian of a singular curve, not the smooth-surface Picard or Néron--Severi group, and makes no novel claim about its already determined motivic class, zeta function or rational-point count. The quotient torus and the abstract rational-point group are classified; a canonical splitting of the whole Picard scheme as an algebraic group is not asserted. Earlier unindexed integral calculations may exist, and no independent mathematical validation has been performed.

## References
1. M. Schütt, T. Shioda and R. van Luijk, *Lines on Fermat surfaces*, arXiv:0812.2377, first public version 2008-12-12, particularly Section 3 and its three standard line families; https://arxiv.org/abs/0812.2377.
2. *A motivic normalization formula for the standard-line divisor on Fermat surfaces*, complete published mathematical record and proof: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-motivic-normalization-formula-for-the-standard-line-divisor-on--66e299b5c5f2.
3. *The genus-289 Fermat quartic line divisor: integral torus and point-free arithmetic*, complete published mathematical record and proof: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-genus-289-fermat-quartic-line-divisor-integral-torus-and-poi--0ec6abf1f810.
4. *Integral Frobenius tori and zeta functions of odd-degree Ceva divisors*, complete published mathematical record and proof: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-integral-frobenius-tori-and-zeta-functions-of-odd-degree-ceva-di--daef787a6781.
