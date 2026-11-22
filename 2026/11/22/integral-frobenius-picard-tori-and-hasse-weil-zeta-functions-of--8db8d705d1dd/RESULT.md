# Integral Frobenius Picard tori and Hasse–Weil zeta functions of the Hesse twelve-line divisor

## Finding

Define the homogeneous integral degree-twelve polynomial
\[
F(X,Y,Z)=XYZ\left((X^3+Y^3+Z^3)^3-27X^3Y^3Z^3\right).
\]
For every finite field \(k=\mathbb F_q\), let \(D_q\subset\mathbb P^2_k\) be the **reduced support** of \(V(F\bmod\operatorname{char}k)\). If the characteristic is different from three, this is the union of the twelve geometric lines in the four singular triangles of the Hesse cubic pencil. If the characteristic equals three, its reduced support consists of the four lines \(X=0\), \(Y=0\), \(Z=0\), and \(X+Y+Z=0\).

**Theorem (arithmetic divisor and connected Picard variety).** For every prime power \(q\), with \(\mathbb L=[\mathbb A^1_k]\) and, in the second case, \(E=\operatorname{Spec}\mathbb F_{q^2}\), the following hold.

1. The motivic class of the reduced divisor is
\[
[D_q]=\begin{cases}
12\mathbb L-27,&q\equiv1\pmod3,\\
4\mathbb L-1+(4\mathbb L-13)[E],&q\equiv2\pmod3,\\
4\mathbb L-2,&3\mid q.
\end{cases}
\]
The identity takes place in \(K_0(\operatorname{Var}_k)\), where \([E]\) is a genuine finite étale scheme class, not the integer two.

2. For every integer \(r\ge1\), setting \(Q=q^r\), the exact extension-field point count is
\[
\#D_q(\mathbb F_Q)=\begin{cases}
12Q-27,&q\equiv1\pmod3,\\
4Q-1,&q\equiv2\pmod3\text{ and }r\text{ odd},\\
12Q-27,&q\equiv2\pmod3\text{ and }r\text{ even},\\
4Q-2,&3\mid q.
\end{cases}
\]
Consequently its Hasse–Weil zeta function is
\[
Z(D_q,T)=\begin{cases}
\dfrac{(1-T)^{27}}{(1-qT)^{12}},&q\equiv1\pmod3,\\[4pt]
\dfrac{(1-T)(1-T^2)^{13}}{(1-qT)^4(1-q^2T^2)^4},&q\equiv2\pmod3,\\[4pt]
\dfrac{(1-T)^2}{(1-qT)^4},&3\mid q.
\end{cases}
\]
The divisor contains **every** rational point of the ambient projective plane if and only if \(q\in\{2,4,7\}\).

3. Let \(T_q\) be the maximal connected torus of \(\operatorname{Pic}^0_{D_q/k}\). Its exact **integral** isomorphism type is
\[
T_q\cong\begin{cases}
\mathbb G_m^{28},&q\equiv1\pmod3,\\
\mathbb G_m^3\times R^1_{\mathbb F_{q^2}/k}\mathbb G_m\times
(\operatorname{Res}_{\mathbb F_{q^2}/k}\mathbb G_m)^{12},&q\equiv2\pmod3,\\
\mathbb G_m^3,&3\mid q.
\end{cases}
\]
Here \(R^1\) denotes the kernel of the norm from the quadratic extension. For \(3\nmid q\), the connected unipotent part of \(\operatorname{Pic}^0\) has dimension \(27\), and in characteristic three it has dimension zero. Thus
\[
\#\operatorname{Pic}^0_{D_q/k}(k)=\begin{cases}
q^{27}(q-1)^{28},&q\equiv1\pmod3,\\
q^{27}(q-1)^3(q+1)(q^2-1)^{12},&q\equiv2\pmod3,\\
(q-1)^3,&3\mid q.
\end{cases}
\]
This asserts the isomorphism type of the maximal torus, not a splitting of the whole connected Picard group into its toric and unipotent parts.

## Assumptions and scope

All finite fields, including even characteristic, are included. The asserted divisor is the **reduced** support of the stated fixed integral polynomial. The geometrically twelve-line description and its ordinary nine quadruple points plus twelve nodes apply only in characteristic different from three. In characteristic three the *nonreduced* degree-twelve equation degenerates to \(XYZ(X+Y+Z)^9\), while the reduced divisor is four lines in general position. Zeta functions count closed points of this reduced support; they are unchanged by nilpotent thickenings, but the connected Picard statements are specifically about the reduced divisor.

The primary arithmetic splitting field of the twelve-line arrangement away from characteristic three is \(k(\omega)\), with \(\omega^2+\omega+1=0\). We do not consider arbitrary projective or Galois twists of the Hesse arrangement or arbitrary Hesse-pencil models. The class identity is for the scheme over \(k\), not merely the geometric incidence lattice.

## Proof

**1. The entire geometric incidence lattice is stable away from three.** Over \(\mathbb Z[\omega]\), write the twelve line coefficient triples as the three coordinate vectors and the nine vectors \((1,\omega^i,\omega^j)\), for \(i,j\in\{0,1,2\}\). Their product is \(F\): the nine noncoordinate factors multiply to \((X^3+Y^3+Z^3)^3-27X^3Y^3Z^3\). Their complete \(\binom{12}{3}=220\) determinant norm histogram, computed in the Eisenstein integers, is
\[
\begin{array}{c|rrrrr}
\operatorname{Norm}(\det)&0&1&3&9&27\\\hline
\text{number}&36&28&81&72&3.
\end{array}
\]
The standalone checker recomputes every determinant using \(\omega^2=-1-\omega\). Every nonzero determinant has norm a power of three, so no new triple concurrence can appear under reduction at any characteristic other than three. The nine Hesse base points have four incident lines each, accounting for all \(9\binom43=36\) identically vanishing triple determinants; the remaining \(\binom{12}{2}-9\binom42=12\) pairs produce distinct ordinary nodes. Pairwise distinctness of the twelve lines also follows from these explicit coefficients. There are exactly 21 singular points, 60 component-to-singular-point branches, and 12 geometrically rational normalization components \(\mathbb P^1\).

**2. Frobenius descent, including branches.** If \(q\equiv1\pmod3\), all cube roots of unity lie in \(k\); all twelve lines, nine quadruple points, twelve nodes, and sixty normalization branches are rational over \(k\). If \(q\equiv2\pmod3\), arithmetic Frobenius acts on coefficient vectors by \(\omega\mapsto\omega^2\). Its fixed-point census is: four fixed lines and four conjugate pairs of lines; three fixed quadruple points and three conjugate pairs; four fixed nodes and four conjugate pairs; and twelve fixed normalization branches and twenty-four conjugate pairs. The twelve fixed branches consist of two rational branches at each of the three rational quadruple points and at each of three rational coordinate-triangle nodes. The fourth rational node, where conjugate lines meet, has no rational normalization branch. This census is obtained from exact projective conjugation and the complete incidence graph, not inferred from a geometric point count. The computer-readable certificate independently verifies every fixed incidence flag.

**3. Motivic normalization identity.** Let \(\nu:\widetilde D\to D\) be normalization, and let \(S\) be the reduced singular-point scheme with \(\widetilde S=\nu^{-1}(S)_{\mathrm{red}}\). By scissors relations,
\[
[D]=[\widetilde D]-[\widetilde S]+[S].
\]
In the split case the three terms are \(12(\mathbb L+1)\), \(60\), and \(21\). In the nonsplit case they are respectively \((4+4[E])(\mathbb L+1)\), \(12+24[E]\), and \(7+7[E]\). Simplifying proves the two motivic formulas. In characteristic three the four distinct rational lines have six rational ordinary nodes, and \([D]=4(\mathbb L+1)-6=4\mathbb L-2\). These are identities in the Grothendieck ring, independent of point-count specialization.

**4. Extension fields and zeta functions.** Point counting is a ring homomorphism \(K_0(\operatorname{Var}_k)\to\mathbb Z\) for each extension \(\mathbb F_{q^r}\). If \(q\equiv2\pmod3\), \(\#E(\mathbb F_{q^r})=0\) for odd \(r\) and \(2\) for even \(r\). This gives the stated four-case point counts. Exponentiating \(\sum_{r\ge1}\#D(\mathbb F_{q^r})T^r/r\) gives all three rational zeta functions; equivalently, use \(Z(E,T)=(1-T^2)^{-1}\). Comparing with \(\#\mathbb P^2(\mathbb F_q)=q^2+q+1\), the point-complement sizes are \((q-4)(q-7)\), \((q-1)(q-2)\), and \(q^2-3q+3\), respectively. Their zeroes among permitted prime powers are exactly \(q=4,7,2\).

**5. The integral Frobenius character lattice.** Let \(\Gamma\) be the bipartite graph having one vertex for each geometric irreducible component and one for each geometric singular point, with an edge for each normalization branch above a singular point. The graph is connected, with \(12+21=33\) vertices and \(60\) edges; hence \(H_1(\Gamma,\mathbb Z)\cong\mathbb Z^{28}\). The normalization-of-units sequence identifies this cycle lattice, with its Galois action, as the character group \(X^*(T_q)\) of the maximal Picard torus (for ordinary multiple-point curve singularities, the remaining local unit quotient is unipotent). The corrected Geisser torus theorem [7] independently identifies the **cocharacter** lattice with the corresponding étale cohomology lattice; the present normalization-of-units description is of the **character** lattice, dual to that cocharacter statement. For the quadratic conjugation \(\sigma\), the trace on graph cycles is the alternating fixed-cell count
\[
\operatorname{tr}(\sigma\mid H_1)=12-(4+7)+1=2.
\]
The standalone checker builds an explicit integral fundamental-cycle basis from a spanning tree, constructs the resulting \(28\times28\) matrix \(A\), verifies \(A^2=I\), and computes
\[
\operatorname{rank}_{\mathbb F_2}(A-I)=12.
\]
By the integral normal form for involutions of a free abelian group, every such lattice is a sum of trivial rank-one, sign rank-one, and regular rank-two modules. If their multiplicities are \(a,b,c\), then \(a+b+2c=28\), \(a-b=2\), and \(c=\operatorname{rank}_{\mathbb F_2}(A-I)=12\). Therefore \((a,b,c)=(3,1,12)\). Translating those three integral modules into tori gives the stated decomposition. Importantly, the rational \(15\)-plus and \(13\)-minus eigen-dimensions alone would not determine these integral isomorphism classes.

**6. Unipotent dimensions and rational-point groups.** Each ordinary fourfold crossing has \(\delta=\binom42=6\) and four branches; of the six local gluing dimensions, three are toric and three unipotent. Each ordinary node contributes one toric dimension and no unipotent dimension. Thus the nine ordinary fourfold points contribute \(27\) unipotent dimensions and the maximal torus has dimension \(28\); their sum is \(55=(12-1)(12-2)/2\), the arithmetic genus of a connected plane degree-twelve curve. Over a finite (hence perfect) field, the smooth connected unipotent group has \(q^{27}\) points. The toric point counts follow from \(\#\mathbb G_m(k)=q-1\), \(\#R^1_{k_2/k}\mathbb G_m(k)=q+1\), and \(\#\operatorname{Res}_{k_2/k}\mathbb G_m(k)=q^2-1\). The finite-field exact sequence gives the displayed total connected Picard-point orders. In characteristic three, the reduced divisor has only six nodes; its four rational components yield torus rank three and no unipotent part.

## Verification

The standalone `verify.py` uses Python's standard library only. It exactly recomputes all 220 Eisenstein triple determinants and their norms; enumerates all 21 geometric crossings and 60 incidence flags; determines the Galois involution on lines, points, and branches; constructs the integral \(28\)-cycle basis and its involution matrix; checks the order-two relation, trace and rank modulo two; and independently enumerates every projective point over the ten small prime fields \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_{11},\mathbb F_{13},\mathbb F_{17},\mathbb F_{19},\mathbb F_{23},\mathbb F_{31}\). It prints `HESSE_ARITHMETIC_PICARD_TORUS_OK` only if all assertions succeed. The universal theorem uses the exact determinant and graph arguments, not a finite sample of primes. The arithmetic and motivic formulas are proved separately from the numerical tests.

## Relationship to prior work

Artebani and Dolgachev [1, Section 2] explicitly list the four triangular singular fibers, their twelve lines, and the twelve triangle vertices. Their classical geometric construction and incidence configuration are not claimed as new. Vallès [2] studies freeness and Jacobian ideals of divisors formed from singular pencil fibers; these are not finite-field zeta or integral Picard-torus calculations. The later work [3] studies the elliptic three-torsion representation and Hesse-pencil twists, not the Picard group of this singular twelve-line boundary. The published local-algebra study [4] explicitly establishes the nine ordinary fourfold points, twelve nodes and a characteristic-two Tjurina-socle jump for the very same divisor; that prior incidence and local Tjurina result is fully credited. The previously published triangular Fermat divisor study [5] gives motivic zeta formulas for different three-pencil configurations, not the four-triangle Hesse divisor or its integral Picard torus. The Hesse 57-line closure study [6] covers a larger distinct arrangement; its characteristic-seven finite-plane statement does not by itself determine the covering behavior of the twelve-line subarrangement.

The assessed contribution is the **joint exact descent** of this particular natural divisor: its finite étale normalization corrections in every characteristic, full zeta and ambient-plane-filling classification, and especially its integral \(\mathbb Z[C_2]\) torus decomposition. It is not a new abstract normalization identity, a rediscovery of the Hesse configuration, or a statement about arbitrary twists. No search can establish universal absence of equivalent earlier work.

## Limitations

The formula refers to the reduced support of a fixed integral plane model; in characteristic three it is not the connected Picard group of the nonreduced degree-twelve scheme. It does not assert that the connected Picard variety is a direct product of its unipotent subgroup and maximal torus, nor does it determine the detailed group law of the unipotent part. Only the quadratic Galois form defined by the displayed equation is classified. Priority over inaccessible or unindexed historical treatments remains provisional, and no independent mathematical validation has been performed.

## References

1. M. Artebani and I. Dolgachev, *The Hesse pencil of plane cubic curves*, first submitted 2006-11-19, arXiv:math/0611590, https://arxiv.org/abs/math/0611590 (especially Section 2, equations for the four triangles and their vertices).
2. J. Vallès, *Free divisors in a pencil of curves*, first submitted 2015-02-09, arXiv:1502.02416, https://arxiv.org/html/1502.02416v2.
3. A. S. I. Anema, J. Top and A. Tuijp, *Hesse Pencils and 3-Torsion Structures*, first submitted 2017-08-31, arXiv:1708.09745, https://arxiv.org/html/1708.09745v2.
4. *The characteristic-two Tjurina socle jump in the Hesse twelve-line arrangement*, published 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-characteristic-two-tjurina-socle-jump-in-the-hesse-twelve-li--815e8767b3d6 (full `RESULT.md` consulted).
5. *Arithmetic wall crossing in twisted triangular Fermat line divisors*, published 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-arithmetic-wall-crossing-in-twisted-triangular-fermat-line-divis--5105b8223fe7 (full `RESULT.md` consulted).
6. *Arithmetic reduction of the 57-line Hesse closure and its complete finite plane*, published 2026-10-13, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-arithmetic-reduction-of-the-57-line-hesse-closure-and-its-comple--878ed7fe45bf (full `RESULT.md` consulted).
7. T. Geisser, *The affine part of the Picard scheme*, Compositio Math. 145 (2009), 415–422, https://doi.org/10.1112/S0010437X08003710; **corrected author version** https://www2.rikkyo.ac.jp/web/geisser/picard_corrected.pdf (the torus/cocharacter theorem in its corrected form; the graph calculation here is explicit).
