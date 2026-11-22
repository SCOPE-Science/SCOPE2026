# Integral Picard tori and zeta functions of Cayley's nine-line divisor

## Finding

Let \(k=\mathbb F_q\) have characteristic greater than three. Consider Cayley's cubic surface
\[
 S:\quad X_0X_1X_2+X_0X_1X_3+X_0X_2X_3+X_1X_2X_3=0
\]
and its reduced divisor \(D\) consisting of all nine geometric lines. For each \(k\)-form \((S_\sigma,D_\sigma)\) obtained by the coordinate-permutation action of \(S_4\), with Frobenius permutation \(\sigma\), the connected generalized Picard scheme of \(D_\sigma\) is a nine-dimensional algebraic torus. Its **integral** character lattice is the cycle lattice of the explicitly defined \(22\)-vertex, \(30\)-edge branch-incidence graph \(\Gamma\), with Frobenius acting by \(\sigma\). In particular, this is an integral classification, not merely a rational representation or isogeny statement.

There are five conjugacy types, with the following complete Frobenius data. In the table, \(L,P,B\) denote the geometric components, singular points, and normalization branches, respectively. An entry such as \(1^3 2^3\) describes three Frobenius fixed points and three two-cycles. The column \(\chi_\sigma(t)\) is the characteristic polynomial of Frobenius acting on \(H_1(\Gamma,\mathbb Z)\); the last column counts \(k\)-rational points of the connected Picard torus.

| \(\sigma\) cycle type | \(L\) orbits | \(P\) orbits | \(B\) orbits | \(\#D_\sigma(k)\) | \(\chi_\sigma(t)\) | \(\#\operatorname{Pic}^0(D_\sigma)(k)\) |
|---|---|---|---|---|---|---|
| \(1^4\) | \(1^9\) | \(1^{13}\) | \(1^{30}\) | \(9q-8\) | \((t-1)^9\) | \((q-1)^9\) |
| \(2\,1^2\) | \(1^3 2^3\) | \(1^5 2^4\) | \(1^6 2^{12}\) | \(3q+2\) | \((t-1)^4(t+1)^5\) | \((q-1)^4(q+1)^5\) |
| \(2^2\) | \(1^5 2^2\) | \(1^5 2^4\) | \(1^{10}2^{10}\) | \(5q\) | \((t-1)^5(t+1)^4\) | \((q-1)^5(q+1)^4\) |
| \(3\,1\) | \(3^3\) | \(1\,3^4\) | \(3^{10}\) | \(1\) | \((t^3-1)^3\) | \((q^3-1)^3\) |
| \(4\) | \(1\,2^2 4\) | \(1\,2^2 4^2\) | \(2^5 4^5\) | \(q+2\) | \((t-1)^2(t+1)^3(t^2+1)^2\) | \((q+1)(q^4-1)^2\) |

The full extension-field point counts are, for every integer \(m\ge1\),
\[
 \#D_\sigma(\mathbb F_{q^m})=(q^m+1)\#L^{\sigma^m}-\#B^{\sigma^m}+\#P^{\sigma^m}.
\]
Their Hasse–Weil zeta functions are determined exactly by the orbit product
\[
 Z(D_\sigma,T)=
 \frac{\prod_{O\subset B/\langle\sigma\rangle}(1-T^{|O|})}
 {\displaystyle\prod_{O\subset L/\langle\sigma\rangle}(1-T^{|O|})(1-q^{|O|}T^{|O|})\;
 \prod_{O\subset P/\langle\sigma\rangle}(1-T^{|O|})}.
\]
The integral character description yields the finite group, not only its order: if \(F_\sigma\) is the explicit nine-by-nine integral Frobenius matrix constructed from the graph in the attached checker, then
\[
 \operatorname{Pic}^0(D_\sigma)(\mathbb F_q)\simeq
 \operatorname{coker}(qI_9-F_\sigma)
\]
as a finite abelian group (the abstract group is insensitive to replacing Frobenius by its inverse).

## Assumptions and scope

All curves are reduced. The cubic and its nine-line boundary are defined by the displayed integral coordinates. A twist here means simultaneous descent of the pair \((S,D)\) through an \(S_4\) permutation of the four coordinates, rather than an arbitrary form of the cubic. The field has characteristic \(p>3\). Each geometric component of \(D\) is \(\mathbb P^1\). The connected Picard scheme is taken in the usual fppf sense. We do not assert that every abstract automorphism of the pair is covered by \(S_4\), only that all coordinate-permutation twists are classified by the five conjugacy classes.

Write \(I=\{0,1,2,3\}\). For every two-element subset \(e=\{i,j\}\), the edge line \(E_e\) has the other two coordinates zero. For each perfect matching \(M=\{e,e^c\}\) of \(I\), the diagonal line \(Q_M\) has equations \(\sum_{i\in e}X_i=\sum_{i\in e^c}X_i=0\). The six \(E_e\) and three \(Q_M\) are the nine distinct lines.

## Proof

**Geometric singularities and the incidence graph.** The six edges pass through the four coordinate vertices \(N_i=[0:\cdots:1:\cdots:0]\), three at each vertex. Their pairwise intersections are exclusively these vertices. Each edge \(E_e\) meets its unique diagonal \(Q_{\{e,e^c\}}\) at the point \(P_e\), represented on that edge by \(X_i=-X_j\) with all other coordinates zero. Each pair of distinct diagonals meets at one point; label this \(R_M\), where \(M\) is the omitted third matching. Each such point has two incident diagonals. Direct substitution in the three line equations shows that all six \(P_e\), all three \(R_M\), and the four \(N_i\) are distinct, and that the other pairs are disjoint. This exhausts line intersections. The completed local ring of \(D\) at \(N_i\) is \(\bar k[[u,v,w]]/(uv,uw,vw)\), an ordinary transverse three-axis singularity (normalization defect \(2\)); at every \(P_e,R_M\), it is \(\bar k[[u,v]]/(uv)\), with normalization defect \(1\). Both types are seminormal. Thus \(D\) has precisely four triple-axis points and nine ordinary nodes.

Construct \(\Gamma\) with one vertex for each of the nine components, one vertex for each of the thirteen singular points, and one edge for every incident component branch. Each \(E_e\) contributes two branches at coordinate vertices and one at \(P_e\); each \(Q_M\) contributes two at the relevant \(P_e\) and two at the relevant \(R_{M'}\). Thus \(\Gamma\) has \(22\) vertices and \(30\) edges and is connected. Its cycle rank is \(30-22+1=9\). Its full combinatorial definition is included in `verify_cayley_boundary.py`.

**Generalized Jacobian and integral Frobenius action.** The normalization \(\nu:\bigsqcup_{L}\mathbb P^1\to D\) has split geometrically rational components and seminormal singularities. The normalization units sequence and the torus-valued gluing parameters at each singular point yield an exact sequence of algebraic tori over \(\bar k\), whose character cochain complex is the signed incidence complex of \(\Gamma\). Since each component has vanishing connected Picard variety, this gives canonically
\[
 X^*(\operatorname{Pic}^0(D_{\bar k}))\cong H_1(\Gamma,\mathbb Z),\qquad
 0\longrightarrow H_1(\Gamma,\mathbb Z)\longrightarrow\mathbb Z[B]
 \xrightarrow{\partial}\mathbb Z[L]\oplus\mathbb Z[P]
 \xrightarrow{\varepsilon}\mathbb Z\longrightarrow0.
\]
Orient the edges from component vertices to singular vertices. Each coordinate permutation preserves this orientation, acts by permutations on each of the three finite sets, and acts on the integral kernel. This proves the integral \(S_4\)-equivariant presentation and its descent to all the stated twists. In particular \(\operatorname{Pic}^0\) has no unipotent part; the graph gives the full connected group, not just a torus quotient.

**Frobenius computation.** Fix a spanning tree of \(\Gamma\). Each of its nine chords determines an integral fundamental cycle, and those cycles form a \(\mathbb Z\)-basis of \(H_1\). Expressing the permutation image of each fundamental cycle in this basis produces the exact integral matrix \(F_\sigma\). This requires only additions and subtractions of integers. The attached standalone checker constructs that basis for all five representative permutations, verifies preservation of the full edge chain, and computes the five characteristic polynomials as shown. For any nine-dimensional torus with integral character matrix \(F_\sigma\), the rational-point group is abstractly \(\mathbb Z^9/(qI_9-F_\sigma)\mathbb Z^9\). The determinant gives its order and factors as in the table; no conclusion about a Smith normal form is inferred from the characteristic polynomial alone.

**All extension counts and zeta functions.** A component defined over \(\mathbb F_{q^m}\) contributes \(q^m+1\) normalization points; components that are not individually fixed contribute none over that field. At each singular point fixed by \(\sigma^m\), normalization has exactly as many rational preimages as fixed incident branches, and there is one point of \(D\) itself. This proves the displayed point-count identity. Exponentiating the series \(\sum_{m\ge1}\#D(\mathbb F_{q^m})T^m/m\) and using Frobenius orbit factors gives the zeta product formula. The orbit counts in the table are obtained by exact finite permutations of the specified finite sets \(L,P,B\); their weighted sizes independently equal \(9,13,30\). In particular, for a three-cycle twist the unique fixed singular point is one coordinate vertex, but no component or branch is fixed: its divisor has exactly one rational point.

## Verification

Run `python3 verify_cayley_boundary.py` under Python 3 with no third-party dependencies. It reconstructs all nine lines, thirteen singularity labels and thirty branches, builds the connected graph and its integer cycle basis, computes five integral Frobenius matrices, verifies every stated orbit profile and Frobenius characteristic polynomial, and checks the split-model projective point counts by **complete** enumeration over \(\mathbb F_5,\mathbb F_7,\mathbb F_{11}\). The recorded output is in `verification_output.txt` and ends with `CAYLEY_BOUNDARY_INTEGRAL_FROBENIUS_AND_ZETA_OK`. The all-characteristic assertions follow from the coordinate and normalization arguments, not from three numerical tests.

## Relationship to prior work

Heath-Brown (first publicly posted October 21, 2002) describes Cayley's four nodes and nine geometric lines as part of a study of rational-point heights. Hassett's account of rational surfaces over nonclosed fields describes the same geometric configuration; Amram–Dettweiler–Friedman–Teicher analyze a different topological invariant of the Cayley singularity complement. A published calculation of the **relative Hilbert scheme of lines** of the four-nodal Cayley cubic determines its nine-point support and nonreduced integral multiplicities, but concerns neither the reduced union's generalized Jacobian nor Frobenius and normalization-gluing zeta data. The present claim is the exact integral Frobenius/Picard classification and all-extension arithmetic for this reduced nine-line divisor. Geometric nine-line enumeration and standard normalization theory are acknowledged as prior knowledge.

## Limitations

The classification concerns only characteristic \(p>3\) coordinate-permutation twists of the specified pair. It does not classify other possible twists, the singular surface's Picard scheme, or integral Hilbert-scheme nilpotents. The group of rational points is given by a fully explicit integral matrix cokernel; separate invariant-factor decompositions for every symbolic \(q\) are not claimed. The novelty assessment compares accessible literature and published results and is not a guarantee against older or differently worded calculations. Independent review has not been performed.

## References

1. D. R. Heath-Brown, *The Density of Rational Points on Cayley's Cubic Surface*, arXiv:math/0210333, first publicly posted 21 October 2002. https://arxiv.org/abs/math/0210333.
2. B. Hassett, *Rational Surfaces over Nonclosed Fields*, Clay Mathematics Proceedings **8** (2009), §4.1. https://www.claymath.org/wp-content/uploads/2022/03/cmip08c.pdf.
3. M. Amram, M. Dettweiler, M. Friedman, M. Teicher, *The Fundamental Group for the Complement of Cayley's Singularities*, arXiv:0803.3005, posted 20 March 2008. https://arxiv.org/abs/0803.3005.
4. *The integral 27-line Hilbert scheme of the four-nodal Cayley cubic*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-integral-27-line-hilbert-scheme-of-the-four-nodal-cayley-cub--2f8fc2a76c51.
