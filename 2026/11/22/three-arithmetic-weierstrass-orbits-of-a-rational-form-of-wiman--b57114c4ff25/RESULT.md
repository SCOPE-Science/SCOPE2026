# Three arithmetic Weierstrass orbits of a rational form of Wiman’s \(W^{160}\)

## Finding
Let \(C/\mathbb Q\subset\mathbb P^4\) be the smooth complete intersection of the three quadrics
\[
\begin{aligned}
X_0^2+2X_1X_4+2X_2X_3&=0,\\
X_2^2+2X_0X_4+2X_1X_3&=0,\\
X_4^2+2X_0X_3+2X_1X_2&=0.
\end{aligned}
\]
Its reduced canonical Weierstrass scheme consists of **exactly three closed points over \(\mathbb Q\), of residue degrees \(8,16,16\)**. Each of the forty geometric points has canonical vanishing sequence \((0,1,2,4,6)\), hence Weierstrass weight three. Their common splitting field is the degree-sixteen Galois extension
\[
E=\mathbb Q\bigl(\zeta_5,i,\sqrt{(1+\sqrt5)/2}\bigr).
\]
The degree-eight closed point lies over the rational fifth root of unity; the two degree-sixteen closed points lie over the four primitive fifth roots. Thus none of the Weierstrass points is rational over \(\mathbb Q\).

## Assumptions and scope
All assertions concern this literal rational canonical curve in characteristic zero. Let \(\zeta=\zeta_5\) be a primitive fifth root of unity, \(K=\mathbb Q(\zeta)\), \(\varphi=1+\zeta+\zeta^{-1}=(1+\sqrt5)/2\), and \(s^2=\varphi\). Here \(i^2=-1\). The phrase splitting field means the smallest field over which all geometric support points of the reduced canonical Weierstrass divisor are rational. The scheme is reduced because the forty points are distinct in characteristic zero. No statement about reductions at positive-characteristic primes or arbitrary Humbert curves is intended.

## Proof
**1. Diagonalization and smoothness.** Set \(v_j=\sum_{r=0}^4X_r\zeta^{jr}\), where \(j\) ranges over \(\mathbb Z/5\mathbb Z\). Orthogonality of fifth roots transforms the three equations into
\[
\sum_{j=0}^4\zeta^{kj}v_j^2=0\qquad(k=0,1,2).
\]
Their solution space in the five squares is two-dimensional. There are quadratic forms \(A,B\) with rational coefficients in the \(X_r\) such that
\[
v_j^2=\zeta^j(A+B\zeta^j).
\]
Indeed \(A=\tfrac15\sum_j\zeta^{-j}v_j^2\), \(B=\tfrac15\sum_j\zeta^{-2j}v_j^2\), and both are integral quadratic convolution forms in the rational \(X_r\). The map \([A:B]:C\to\mathbb P^1\) has degree sixteen: away from five branch values, there are \(2^5/2=16\) projective sign choices. Its five branch values are \(A+B\zeta^a=0\), one for each \(a\in\mathbb Z/5\mathbb Z\); each has eight distinct points, characterized by \(v_a=0\). The cover is geometrically connected, since four independent square classes of ratios of five distinct linear factors give a degree-sixteen Kummer extension of \(\overline{\mathbb Q}(A/B)\). A point has at least four nonzero diagonal coordinates, so the Jacobian matrix of the three diagonal quadrics has rank three (any three columns of the Vandermonde matrix are independent). Thus \(C\) is smooth and connected. As a smooth \((2,2,2)\) complete intersection in \(\mathbb P^4\), its genus is five and \(\omega_C\cong\mathcal O_C(1)\).

**2. The complete Weierstrass divisor.** Work at one of the eight points above the branch value indexed by \(a\). After an analytic choice of a nonzero projective scale, take a local parameter \(u\) with \(t-\zeta^a=u^2\), where \(t=-A/B\). The coordinate \(v_a\) is odd of order one in \(u\); the other four coordinates are even functions, proportional to \(\sqrt{\zeta^j(\zeta^j-t)}\) for \(j\ne a\). Their first four jets in \(t\), of orders zero through three, give a nonsingular matrix: apart from nonzero row and column factors, it is the Vandermonde matrix in the four pairwise distinct numbers \((\zeta^j-\zeta^a)^{-1}\). Consequently the four even canonical sections have vanishing orders \(0,2,4,6\), while \(v_a\) gives the independent order one. The canonical sequence is \((0,1,2,4,6)\); the weight is \(3\). All forty branch points therefore contribute \(40\cdot3=120\), exactly the total canonical Weierstrass weight \(g^3-g=120\) for genus five. No other points are Weierstrass.

**3. Radical coordinates and a degree-sixteen splitting field.** Above the branch value indexed by \(a\), put \(A=-B\zeta^a\). Since \(B\ne0\), the nonzero diagonal coordinates satisfy
\[
v_j^2=B\,w_j(a),\qquad w_j(a)=\zeta^j(\zeta^j-\zeta^a),\quad j\ne a.
\]
At \(a=0\), divide the four nonzero coordinates by \(v_1\). The ratios of squares satisfy
\[
\frac{w_2(0)}{w_1(0)}=-\zeta^4\varphi,\qquad
\frac{w_3(0)}{w_1(0)}=\zeta^3\varphi,\qquad
\frac{w_4(0)}{w_1(0)}=-\zeta^2.
\]
Thus the eight normalized points have
\[
\left(\frac{v_2}{v_1},\frac{v_3}{v_1},\frac{v_4}{v_1}\right)
=\left(\epsilon_2 i\zeta^2s,\ \epsilon_3\zeta^4s,\ \epsilon_4 i\zeta\right),
\quad \epsilon_j\in\{1,-1\}.
\]
For any \(a\), the identity \(w_{a+j}(a)=\zeta^{2a}w_j(0)\), with subscripts modulo five, gives identical ratios after relabeling the coordinates. Fourier inversion \(X_r=\tfrac15\sum_j\zeta^{-jr}v_j\) therefore puts **all forty** points in \(E=K(i,s)\).

The field \(K\) has degree four. It does not contain \(i\), and \(K(i)=\mathbb Q(\zeta_{20})\) is an abelian Galois extension of \(\mathbb Q\). The number \(s\) satisfies the irreducible quartic \(U^4-U^2-1\); this polynomial has two real and two nonreal roots, so \(\mathbb Q(s)\) is not Galois over \(\mathbb Q\). It cannot be a subfield of the abelian extension \(K(i)\), all of whose subfields are Galois over \(\mathbb Q\). Hence \([E:K]=4\) and \([E:\mathbb Q]=16\). Moreover \(E/\mathbb Q\) is Galois: the conjugate of \(\varphi\) under \(\zeta\mapsto\zeta^2\) is \(-1/\varphi\), whose square root is \(i/s\), already in \(E\).

**4. Exact Galois-orbit lengths.** Over \(K\), the two independent sign changes \(i\mapsto-i\) and \(s\mapsto-s\) act on the three signs \((\epsilon_2,\epsilon_3,\epsilon_4)\) by flipping the pairs \((2,4)\) and \((2,3)\). Their action is free and has two orbits of four points in each branch fiber, distinguished by the product of the three signs.

For a branch index \(a\), the polynomial identity
\[
\prod_{j\ne a}w_j(a)=5\zeta^{-2a}
\]
yields a scale-invariant sign
\[
\delta_a(P)=\frac{\prod_{j\ne a}v_j(P)}{B(P)^2\sqrt5\,\zeta^{-a}}\in\{1,-1\}.
\]
The chosen \(\sqrt5=1+2(\zeta+\zeta^{-1})\) lies in \(K\). The automorphism \(\sigma_k:\zeta\mapsto\zeta^k\), for \(k\in(\mathbb Z/5\mathbb Z)^\times\), sends \(a\) to \(ka\) and multiplies \(\delta\) by the quadratic character \(\chi(k)\in\{1,-1\}\) of \(k\) modulo five. In particular, at \(a=0\), \(\sigma_2\) exchanges the two four-point orbits. Hence all eight points above the rational branch value form **one** Galois orbit.

For \(a\ne0\), the base value \(\zeta^a\) generates \(K\). Any Galois element fixing a point above it must fix \(K\), but \(\operatorname{Gal}(E/K)\) acts freely on all eight points in that fiber. Thus each of the thirty-two points above primitive fifth roots has a full degree-sixteen orbit. There are exactly two such orbits. Their residue fields equal \(E\), since \(E/\mathbb Q\) itself has degree sixteen. This also proves that \(E\) is the **minimal** common splitting field.

## Verification
The accompanying standard-library script `verify_cyclotomic.py` implements exact integer arithmetic in \(\mathbb Z[\zeta]/(1+\zeta+\zeta^2+\zeta^3+\zeta^4)\). Run `python3 verify_cyclotomic.py`. It checks the three rational trace quadrics, the identity \(\varphi^2=\varphi+1\), the five branch-product identities, the relabeling identities, the three radical-square identities, and the two four-point sign-action orbits. It returns `HUMBERT_FIVE_EXACT_IDENTITIES_OK`. The proof of geometric smoothness, Weierstrass completeness, field degree, and Galois orbit transitivity is the argument above, not a finite computational extrapolation.

## Relationship to prior work
The curve is a rational Fourier-descended form of Wiman’s classical genus-five curve \(W^{160}\). Edge (1969), §§2,4,6–9, explicitly gives Wiman’s fifth-root diagonal quadrics (up to a coordinate rescaling), identifies the five Weierstrass octads, and studies the automorphism group of order 160, tangent projections, and plane sextic adjoints. These **geometric objects, equations, and forty weight-three points are not claimed as new**. Explicitly, multiplying Wiman’s diagonal coordinate with index \(j\) by \(\zeta^{2j}\) shifts the exponent set \(\{0,1,4\}\) to the consecutive-character set \(\{0,1,2\}\); the displayed rational model is its inverse Fourier descent. The 2014 work of Hidalgo and Leyton-Álvarez gives the general hyperosculating framework and weight bounds; Kato (2015) also records the forty type-I points. The contribution is the exact **arithmetic** closed-point degrees \((8,16,16)\) for the displayed \(\mathbb Q\)-form, and its minimal degree-sixteen splitting field. Edge's explicit octad formulas over complex fifth roots alone do not determine which coordinate ratios define the rational Weil-descent and its resulting \(\mathbb Q\)-Galois orbits; the cyclotomic quadratic-character action provides that comparison.

## Limitations
The result applies to one explicit rational model, not every Humbert curve; different rational twists of the same geometric curve can have different arithmetic orbits. The weight computation is characteristic zero, and no claim is made about bad reductions or independent external validation. The 1969 Edge paper has been inspected in its complete accessible text; the earlier Edge 1951 paper was available only by extract, so a previously unlocated rational-descent computation remains a priority risk.

## References
1. R. A. Hidalgo and M. Leyton-Álvarez, *The hyperosculating points of the generalized Fermat curves*, arXiv:1409.6258v1 (first posted 2014-09-22), https://arxiv.org/abs/1409.6258.
2. T. Kato, *A curve of genus 5 having 24 Weierstrass points of weight 5*, Hokkaido Mathematical Journal 44 (2015), 165–173, https://www.math.sci.hokudai.ac.jp/hmj/page/44-2/pdf/HMJ44_165-173.pdf.
3. W. L. Edge, *Humbert's plane sextics of genus 5*, Mathematical Proceedings of the Cambridge Philosophical Society 47 (1951), 483–495, https://doi.org/10.1017/S030500410002689X.
4. R. A. Hidalgo, A. Kontogeorgis, M. Leyton-Álvarez and P. Paramantzoglou, *Automorphisms of the Generalized Fermat curves*, arXiv:1409.3063 (2014), https://arxiv.org/abs/1409.3063.
5. W. L. Edge, *Three plane sextics and their automorphisms*, Canadian Journal of Mathematics 21 (1969), 1263–1278, §§2,4,6–9, https://doi.org/10.4153/CJM-1969-139-6.
