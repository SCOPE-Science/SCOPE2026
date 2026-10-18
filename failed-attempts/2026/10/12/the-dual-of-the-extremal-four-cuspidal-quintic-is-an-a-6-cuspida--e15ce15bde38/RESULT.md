# The dual of the extremal four-cuspidal quintic is an \(A_6\)-cuspidal quartic

## Finding
Let \(Q_4\subset\mathbb P^2_{\mathbb C}\) be the unique four-cuspidal quintic of Koras--Palka, with normalization map
\[
[s:t]\longmapsto [s^4t:s^2t^3-s^5:t^5+2s^3t^2].
\]
Its projective dual \(Q_4^\vee\subset(\mathbb P^2)^\vee\) is the irreducible rational quartic with normalization
\[
[s:t]\longmapsto [t(4s^3-t^3):2s^2t^2:-s^4]
\]
and equation
\[
(B^2-4AC)^2+128BC^3=0.
\]
The quartic has exactly one singular point, \([1:0:0]\), and its unique branch there has Puiseux pair \((2,7)\), hence analytic type \(A_6\). The dual normalization map is injective. Consequently no line is tangent to \(Q_4\) at two distinct normalization points. In addition, \(Q_4\) has no flex at a smooth point. The three \(A_2\)-cusp tangents of \(Q_4\) map to smooth points of the dual, whereas the tangent at its \(A_6\) cusp maps to the unique \(A_6\) cusp of the dual.

## Assumptions and scope
Everything is over \(\mathbb C\). The source proves that a rational cuspidal plane curve with four cusps is unique up to projective equivalence and gives the displayed degree-five parametrization. Its explicit model has one cusp of type \(A_6\) and three cusps of type \(A_2\). The claim concerns the projective dual and tangent-line geometry of that unique projective class. “Tangent at a normalization point” includes the limiting tangent of a cusp branch. The statement does not classify duals of arbitrary rational cuspidal quintics.

## Proof
On the affine chart \(t=1\), write
\[
P(u)=(u^4,\;u^2-u^5,\;1+2u^3).
\]
The tangent line is represented by the cross product \(P(u)\times P'(u)\). Exact factorization gives
\[
P\times P'=u(u^3+2)\bigl(4u^3-1,\;2u^2,\;-u^4\bigr).
\]
The common factor vanishes precisely at cusp parameters and is removed when the Gauss map is extended across the normalization. Hence the extended dual map is
\[
Q(u)=[4u^3-1:2u^2:-u^4],
\]
which homogenizes to the map in the finding.

Put \(Q(u)=[A:B:C]\). Then
\[
B^2-4AC=16u^7,\qquad BC=-2u^6,
\]
so \(Q(u)\) satisfies
\[
F(A,B,C):=(B^2-4AC)^2+128BC^3=0.
\]
On the dense open set \(BC\ne0\), the parameter is recovered by
\[
u=-\frac{B^2-4AC}{8BC}.
\]
Thus the map is birational. The homogeneous coordinate forms have degree four and no common factor, so the image has degree four; since its closure is irreducible and lies on the quartic \(F=0\), it is exactly \(Q_4^\vee\).

The partial derivatives are
\[
F_A=8C(4AC-B^2),
\]
\[
F_B=-4(4ABC-B^3-32C^3),
\]
\[
F_C=8(4A^2C-AB^2+48BC^2).
\]
If \(C=0\) and all three partials vanish, then \(F_B=4B^3\), so \(B=0\) and the projective point is \([1:0:0]\). If \(C\ne0\), then \(F_A=0\) forces \(B^2=4AC\), after which \(F_B=128C^3\ne0\). Hence \([1:0:0]\) is the only singular point.

Near its unique preimage \(u=0\), work in the chart \(A=1\). With \(b=B/A\) and \(c=C/A\), set \(v=c-b^2/4\). Then
\[
b=-2u^2+O(u^5),\qquad v=-4u^7+O(u^{10}).
\]
Therefore the branch has characteristic exponents \(2\) and \(7\), equivalently Puiseux pair \((2,7)\), so it is an \(A_6\) cusp. This agrees with the standard rational-quartic classification, where the multiplicity sequence \((2:2:2:1)\) is the \(A_6\)-cusp and has \(\delta=3\). Since a plane quartic has arithmetic genus three, this single cusp also exhausts the genus defect.

The dual map is globally injective. Away from \(BC=0\), the displayed inverse recovers \(u\). The only parameters with \(BC=0\) are \(s=0\) and \(t=0\), mapping respectively to \([1:0:0]\) and \([0:0:1]\), with singleton fibers. Hence two distinct normalization points of \(Q_4\) never determine the same tangent line.

Finally, the projective Wronskian of the original parametrization is represented on \(t=1\) by
\[
\det(P,P',P'')=-4u^3(u^3+2)^2.
\]
Homogeneously it is \(-4s^3(s^3+2t^3)^2\), which is nonzero at \(t=0\). Its zero set is therefore exactly the parameter of the \(A_6\) cusp and the three parameters of the \(A_2\) cusps. There is no smooth flex. Since the dual singular locus consists only of the image of the \(A_6\)-cusp parameter, the three \(A_2\)-cusp tangent points are smooth on \(Q_4^\vee\).

## Verification
The accompanying `verify.py` performs exact symbolic checks of the tangent cross product, the dual equation, the birational inverse identity, the three partial derivatives, the local \((2,7)\) orders, and both Wronskians. These checks use exact polynomial arithmetic; they are not numerical sampling. The global conclusions about singularities and tangent fibers follow from the explicit case split and inverse formula above, not from finite enumeration.

## Relationship to prior work
Koras--Palka prove the sharp four-cusp bound, uniqueness of the extremal quintic up to projective equivalence, and the displayed parametrization. Their result supplies the object and its cusp types but does not state the dual quartic equation or the complete tangent-line consequences proved here. Cox--Kustin--Polini--Ulrich classify singularity configurations of rational plane quartics and identify the one-branch multiplicity sequence \((2:2:2:1)\) as an \(A_6\) cusp; that general classification does not identify the dual of the Koras--Palka quintic with this stratum.

A targeted comparison also considered formulations in terms of Gauss maps, bitangents, flexes, projective duals, and the exact dual equation. The closest indexed result on the same quintic concerns its projective automorphism group \(C_3\); that symmetry statement neither implies the displayed dual equation nor records the injectivity and flex assertions.

## Limitations
The finding is an exact statement for the unique extremal four-cuspidal quintic. It does not assert that every rational quartic with an \(A_6\) cusp arises as a dual of a four-cuspidal quintic, nor does it classify tangent geometry for other cuspidal quintics. The originality comparison cannot exclude an older classical source using substantially different terminology for the same specific duality computation.

## References
1. M. Koras and K. Palka, *Complex planar curves homeomorphic to a line have at most four singular points*, arXiv:1905.11376v1, 2019.
2. D. Cox, A. R. Kustin, C. Polini, and B. Ulrich, *A study of singularities on rational curves via syzygies*, arXiv:1102.5072, 2011.
