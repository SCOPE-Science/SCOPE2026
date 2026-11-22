# Five integral Frobenius Picard tori of the resolved \(B_3\) reflection arrangement

## Finding
Let \(k=\mathbb F_q\) be a finite field of characteristic greater than three. In \(\mathbb P^2_k\) consider the nine-line Coxeter arrangement
\[
A=V\!\bigl(xyz(x-y)(x+y)(x-z)(x+z)(y-z)(y+z)\bigr).
\]
Blow up the seven geometric intersection points of multiplicity at least three, and let \(D\) be the reduced union of the nine strict transforms and the seven exceptional curves. This is a geometrically connected **stable nodal curve** with sixteen rational components, thirty ordinary nodes, and arithmetic genus fifteen. The projective signed-coordinate permutation group \(G\cong S_4\) of order twenty-four preserves \(D\). For each conjugacy class of \(G\), let \(D_g/k\) be the finite-field form obtained by descent using the specified Frobenius action \(g\), and set \(T_g=\operatorname{Pic}^0(D_g/k)\).

Write \(R_d=\operatorname{Res}_{\mathbb F_{q^d}/k}\mathbb G_m\), and write \(N_2=\ker(R_2\xrightarrow{\operatorname{Norm}}\mathbb G_m)\). Here \(C_m\) is a cyclic abstract group of order \(m\). The **complete integral** classifications are:

| Conjugacy type in \(S_4\) | Class size | \(T_g\) as a \(k\)-torus | Abstract finite abelian group \(T_g(k)\) | \(\#D_g(k)\) |
| --- | ---: | --- | --- | --- |
| \(1^4\) | 1 | \(\mathbb G_m^{15}\) | \(C_{q-1}^{15}\) | \(16q-14\) |
| \(2^2\) | 3 | \(\mathbb G_m^3\times R_2^6\) | \(C_{q-1}^3\times C_{q^2-1}^6\) | \(8q-2\) |
| \(2\,1^2\) | 6 | \(\mathbb G_m\times R_2^7\) | \(C_{q-1}\times C_{q^2-1}^7\) | \(6q\) |
| \(4\) | 6 | \(R_4^3\times R_2\times N_2\) | \(C_{q^4-1}^3\times C_{q^2-1}\times C_{q+1}\) | \(2q+2\) |
| \(3\,1\) | 8 | \(R_3^5\) | \(C_{q^3-1}^5\) | \(q+1\) |

These are isomorphisms of algebraic tori over \(k\), **not merely isogenies or group-order identities**. The order-four case contains an intrinsically anisotropic quadratic norm-one factor. In particular all five Frobenius conjugacy types yield distinct integral torus isomorphism classes.

The complete Hasse–Weil zeta functions, encompassing **every** extension field of \(k\), are respectively
\[
\begin{array}{c|l}
1^4 & \displaystyle\frac{(1-t)^{14}}{(1-qt)^{16}}\\[3pt]
2^2 & \displaystyle\frac{(1-t)^2(1-t^2)^6}{(1-qt)^8(1-q^2t^2)^4}\\[3pt]
2\,1^2 & \displaystyle\frac{(1-t^2)^7}{(1-qt)^6(1-q^2t^2)^5}\\[3pt]
4 & \displaystyle\frac{(1-t^2)^2(1-t^4)^3}{(1-t)^2(1-qt)^2(1-q^2t^2)^3(1-q^4t^4)^2}\\[3pt]
3\,1 & \displaystyle\frac{(1-t^3)^5}{(1-t)(1-qt)(1-q^3t^3)^5}.
\end{array}
\]

## Assumptions and scope
Work in characteristic \(p>3\), where the indicated nine geometric lines are distinct and have the stated integral incidence. All intersections and components in the construction are understood geometrically over \(\bar{k}\). There are six ordinary double points, four ordinary triple points, and three ordinary quadruple points in the original plane arrangement. Blow up the last seven points once each; the ordinary double intersections remain ordinary nodes. The strict transforms are embedded copies of \(\mathbb P^1\), as are the exceptional curves. Each geometric rational component has at least three nodal markings, so \(D\) is stable.

A signed permutation matrix acts on homogeneous coordinates and therefore on the arrangement and its blowup. The common scalar \(-I\) acts trivially on projective space, giving precisely the specified twenty-four-element projective group \(G\). Its action on the four long diagonal axes identifies \(G\) with \(S_4\). The theorem concerns forms descended by elements of **this group**, not all possible abstract or embedded forms of \(D\). Such a form exists over every \(k\) in scope: the group is defined over \(k\), and a chosen finite-order element defines a continuous finite-Galois descent cocycle. The identity component \(\operatorname{Pic}^0\) denotes multidegree-zero line bundles, not the full possibly disconnected Picard functor.

## Proof
**1. Incidence and stable curve.** The nine line-normal triples are
\[
(1,0,0),(0,1,0),(0,0,1),
(1,-1,0),(1,1,0),(1,0,-1),(1,0,1),(0,1,-1),(0,1,1).
\]
For each pair, take its cross product and normalize the first nonzero coordinate to be positive. Exhaustive exact integer cross products yield thirteen distinct projective intersections: six have two incident lines, four have three, and three have four. This exhausts all \(\binom92=36\) pairs because \(6+4\binom32+3\binom42=36\). Over any \(p>3\) this incidence remains unchanged: all normalized coordinates have entries in \(\{0,\pm1\}\), and direct substitution shows distinctness and transversality in the indicated characteristics. Blowing up the seven higher intersections produces, at each former point of multiplicity \(m\), one exceptional rational curve meeting the \(m\) strict transforms transversely at \(m\) distinct nodes. The six original ordinary nodes remain. Hence the graph \(\Gamma\) has
\[
|V|=9+7=16,\qquad |E|=4\cdot3+3\cdot4+6=30,
\qquad b_1(\Gamma)=30-16+1=15.
\]
The graph is connected and its sixteen vertices all have degree three or four, so the curve is stable and \(p_a(D)=15\).

**2. Integral Picard character lattice.** Since every normalized component has genus zero, the normalization exact sequence for units identifies the Galois character lattice of \(\operatorname{Pic}^0(D_g/k)\) with the **integral** graph cycle lattice \(H_1(\Gamma,\mathbb Z)\). This is the kernel, not merely the rational kernel, of the signed incidence boundary \(\mathbb Z^{E}\to\mathbb Z^{V}\). The rank is fifteen by the preceding count. A rooted spanning tree supplies fifteen fundamental cycles, giving an integral basis without denominators. The signs under Frobenius are those induced by the orientations of graph edges.

**3. Exact integral Frobenius normal forms.** For the five class representatives, act on line normals by respectively the identity, the coordinate sign change \((x,y,z)\mapsto(x,y,-z)\), the swap \((x,y,z)\mapsto(x,z,y)\), the signed swap \((x,y,z)\mapsto(x,z,-y)\), and the rotation \((x,y,z)\mapsto(y,z,x)\). They have class sizes \(1,3,6,6,8\) and orders \(1,2,2,4,3\). The program `verify_b3_tori.py` constructs all twenty-four projective signed permutations, checks their five complete conjugacy classes, fixes a canonical breadth-first spanning tree, and constructs their exact \(15\)-by-\(15\) cycle matrices \(F\).

For each representative the program builds a fifteen-column integral matrix \(W\) from explicit seeds in the fundamental-cycle basis. A cyclic block of length \(d\) contributes \(v,Fv,\ldots,F^{d-1}v\), with the wrap-around relation \(F^dv=v\); a negative block is a single primitive vector with \(Fv=-v\). The certificate seeds are encoded directly in the program as the `SEEDS` table. Their normal forms, **with determinant \(\pm1\)**, give
\[
H_1(\Gamma,\mathbb Z)\cong
\begin{cases}
\mathbb Z^{15},&1^4,\\
\mathbb Z^3\oplus\mathbb Z[C_2]^6,&2^2,\\
\mathbb Z\oplus\mathbb Z[C_2]^7,&2\,1^2,\\
\mathbb Z[C_4]^3\oplus\mathbb Z[C_2]\oplus\mathbb Z_{-},&4,\\
\mathbb Z[C_3]^5,&3\,1.
\end{cases}
\]
Here \(\mathbb Z_{-}\) means the primitive rank-one sign module and \(\mathbb Z[C_d]\) the regular rank-\(d\) permutation module. In the order-four case, for example, the columns constructed from seeds \(e_1\), \(e_2+e_9\), \(e_{12}+e_{13}\), \(e_2\), and \(e_{14}\) have exact determinant one and exhibit blocks of lengths four, four, four, two, and one (negative), respectively. A regular module gives the torus \(R_d\), and \(\mathbb Z_{-}\) gives \(N_2\). This proves all five integral torus isomorphisms. Taking rational points gives the displayed **abstract finite abelian groups**, since \(R_d(k)=\mathbb F_{q^d}^{\times}\) and \(N_2(k)\) has order \(q+1\) and is cyclic.

**4. Zeta functions.** Denote by \(v_d\), \(e_d\), and \(f_d\) the number of Frobenius orbits of length \(d\) on the sixteen components, thirty nodes, and sixty normalization branches, respectively. Direct exact group enumeration gives:

| Conjugacy type | Nonzero \(v_d\) | Nonzero \(e_d\) | Nonzero \(f_d\) |
| --- | --- | --- | --- |
| \(1^4\) | \(v_1=16\) | \(e_1=30\) | \(f_1=60\) |
| \(2^2\) | \(v_1=8,v_2=4\) | \(e_1=10,e_2=10\) | \(f_1=20,f_2=20\) |
| \(2\,1^2\) | \(v_1=6,v_2=5\) | \(e_1=6,e_2=12\) | \(f_1=12,f_2=24\) |
| \(4\) | \(v_1=2,v_2=3,v_4=2\) | \(e_2=5,e_4=5\) | \(f_2=10,f_4=10\) |
| \(3\,1\) | \(v_1=1,v_3=5\) | \(e_3=10\) | \(f_3=20\) |

No graph edge is reversed by any specified group element, and therefore \(f_d=2e_d\) for each length. Normalization gives, for every \(r\ge1\),
\[
\#D_g(\mathbb F_{q^r})=(q^r+1)\#\operatorname{Fix}(g^r\mid V)-
\#\operatorname{Fix}(g^r\mid\text{branches})+
\#\operatorname{Fix}(g^r\mid E).
\]
Taking exponential generating functions yields the exact zeta product
\[
Z(D_g/k,t)=\prod_{d\ge1}\frac{(1-t^d)^{e_d-v_d}}{(1-q^dt^d)^{v_d}},
\]
which simplifies to the five displayed rational functions and their rational-point counts. This is an identity for every extension degree, not a finite-field interpolation.

## Verification
Execute `python3 verify_b3_tori.py` from the directory containing the file; it uses only the Python standard library. Its successful final line is `B3_RESOLVED_FROBENIUS_INTEGRAL_PICARD_TORI_OK`. It reconstructs all thirty-six line pairs, the complete stable graph, all twenty-four signed projective symmetries and five actual conjugacy classes, signed edge actions and fundamental cycles, all orbit counts, and the exact integral change-of-basis certificates by fraction-free determinant computation. The certificate matrices are recreated from the supplied seed table rather than imported from saved computations. The recorded verification output is `verify_output.txt`. The general algebraic steps (descent, normalization and Picard identification) are proved separately above, rather than inferred from finite tests.

## Relationship to prior work
The nine-line projectivized \(B_3\) Coxeter arrangement is classical; Ehrenborg–Klivans–Reading treat three-dimensional Coxeter arrangements (arXiv:1501.05991v1), while Bauer–Malara–Szemberg–Szpond explicitly give its nine-line polynomial and study the **dual point configuration's unexpected quartic** (arXiv:1804.03610). Neither subject is the arithmetic classification of this resolved boundary. Geisser's *The affine part of the Picard scheme* (arXiv:0704.0479v1, Theorem 1) provides the general torus–integral-cohomology foundation, and Casalaina-Martin–Kass–Viviani (arXiv:1107.4166v1) develop nodal dual-graph Jacobian techniques; their general theories do not evaluate the five specified \(B_3\) cycle-lattice modules. Closely relevant accessible prior calculations include five integral Heawood-graph Picard tori and fifteen-line Igusa-boundary twists. The former uses a different fourteen-vertex incidence graph, and the latter evaluates one of eleven integral classes for a different curve. A separate Fermat–Ceva divisor calculation covers exponent \(n\ge3\), without the three coordinate axes or the \(B_3\) projective \(S_4\) twists. None of those results implies the present complete five-class integral decomposition or its zeta table. An equivalent specialist calculation in unindexed historical representation or arrangement literature has not been excluded.

## Limitations
Only characteristic greater than three and the five twists from the specified projective signed-permutation group are asserted. This does not classify all forms under possible additional abstract automorphisms. \(T_g\) is the connected Picard torus of a **reducible nodal curve**, not an abelian variety or the Picard group of the blown-up surface. The result does not classify the Néron component group of arbitrary smoothings, nor does the finite certificate independently authenticate the general algebraic geometry. Historical originality remains subject to specialist verification; no independent mathematical audit has been performed.

## References
1. T. Geisser, *The affine part of the Picard scheme*, arXiv:0704.0479v1, first public 2007-04-04, especially Theorem 1, https://arxiv.org/abs/0704.0479.
2. S. Casalaina-Martin, J. L. Kass, F. Viviani, *The Local Structure of Compactified Jacobians*, arXiv:1107.4166v1, first public 2011-07-21, https://arxiv.org/abs/1107.4166.
3. R. Ehrenborg, C. Klivans, N. Reading, *Coxeter arrangements in three dimensions*, arXiv:1501.05991v1, first public 2015-01-24, https://arxiv.org/abs/1501.05991.
4. T. Bauer, G. Malara, T. Szemberg, J. Szpond, *Quartic unexpected curves and surfaces*, arXiv:1804.03610, 2018, https://arxiv.org/abs/1804.03610.
