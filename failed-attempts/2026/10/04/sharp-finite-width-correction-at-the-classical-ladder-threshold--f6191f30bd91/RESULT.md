# Sharp finite-width correction at the classical ladder threshold
## Finding
Let \(a,b>0\), and for \(0\le d\le \min\{a,b\}\) define
\[
n(a,b,d)=\inf_{0<t<\pi/2}\frac{a\sin t+b\cos t-d}{\sin t\cos t}.
\]
Put \(L=(a^{2/3}+b^{2/3})^{3/2}\) and \(\kappa=(ab)^{1/3}/(a^{2/3}+b^{2/3})\). Then \(d\mapsto n(a,b,d)\) is concave and
\[
n(a,b,d)\le L-\frac{d}{\kappa}\qquad(0\le d\le\min\{a,b\}).
\]
If \(a\ne b\), the inequality is strict for every \(d>0\); if \(a=b\), equality holds throughout the interval. Moreover, as \(d\downarrow0\),
\[
n(a,b,d)=L-\frac{d}{\kappa}-\frac{(a^{2/3}-b^{2/3})^2\sqrt{a^{2/3}+b^{2/3}}}{6(ab)^{4/3}}d^2+O(d^3).
\]
For all sufficiently small \(d>0\), this \(n(a,b,d)\) is exactly the largest possible long side of a rectangle of short side \(d\) that can move around each of the three ladder-limited corridors \(\mathcal C_{03},\mathcal C_{11},\mathcal C_{13}\) of Mushkarov--Nikolov. Thus the classical zero-width ladder length has a sharp finite-width linear loss, while corridor anisotropy contributes a strictly negative quadratic correction, vanishing exactly when \(a=b\).

Equivalently, if \(A=a^{1/3}\), \(B=b^{1/3}\), and \(S=A^2+B^2\), then the first two finite-width losses are
\[
\frac{1}{\kappa}=\frac{S}{AB},\qquad
\frac{(A^2-B^2)^2\sqrt S}{6A^4B^4}.
\]
The quadratic coefficient is zero exactly in the symmetric corridor and is positive otherwise.

## Assumptions and scope
The corridor widths satisfy \(a,b>0\). The short side satisfies \(0\le d\le\min\{a,b\}\). The function \(n(a,b,d)\) is the tangent-segment functional introduced in the 2026 classification of moving rectangles. The assertion that \(n(a,b,d)\) is the exact maximum long side is only claimed for sufficiently small positive \(d\), where \(n(a,b,d)>\max\{a,b\}\) and \(d<h=ab/\sqrt{a^2+b^2}\); in that regime the classification theorem reduces in all three ladder-limited corridors to the single condition \(c\le n(a,b,d)\).

No claim is made for the other five corridor types, for nonrectangular sofas, or for arbitrary finite widths beyond the displayed global bound on \(n\).

## Proof
Write
\[
G(t)=\frac{a}{\cos t}+\frac{b}{\sin t},\qquad
H(t)=\frac{1}{\sin t\cos t},
\]
so that
\[
n(a,b,d)=\inf_{0<t<\pi/2}\bigl(G(t)-dH(t)\bigr).
\]
For each fixed \(t\), the displayed expression is affine in \(d\). The infimum of affine functions is concave, proving concavity of \(d\mapsto n(a,b,d)\).

At \(d=0\), the classical ladder minimizer is unique and satisfies
\[
\tan t_0=(b/a)^{1/3}.
\]
If \(A=a^{1/3}\), \(B=b^{1/3}\), and \(S=A^2+B^2\), then
\[
\sin t_0=\frac{B}{\sqrt S},\qquad
\cos t_0=\frac{A}{\sqrt S},\qquad
G(t_0)=S^{3/2}=L,
\]
and
\[
H(t_0)=\frac{S}{AB}=\frac1\kappa.
\]
Evaluating the infimum at \(t_0\) gives the global tangent bound
\[
n(a,b,d)\le G(t_0)-dH(t_0)=L-\frac d\kappa.
\]
If \(a\ne b\), then \(H'(t_0)\ne0\), while \(G'(t_0)=0\). Hence for every \(d>0\), the point \(t_0\) is not stationary for \(G-dH\), so the bound is strict. When \(a=b\), the source's exact symmetric formula gives \(n(a,a,d)=2\sqrt2\,a-2d\), which is exactly the tangent line.

For the second-order term, the zero-width minimizer is nondegenerate. Direct differentiation at \(t_0\) gives
\[
G''(t_0)=3S^{3/2},\qquad
H'(t_0)=-\frac{(A^2-B^2)S}{A^2B^2}.
\]
The implicit-function theorem therefore supplies a smooth minimizing branch \(t(d)\) for small \(d\). Since the objective is affine in \(d\), the envelope identity and the stationarity equation give
\[
n''(0)=-\frac{H'(t_0)^2}{G''(t_0)}
=-\frac{(A^2-B^2)^2\sqrt S}{3A^4B^4}.
\]
Taylor's theorem yields
\[
n(a,b,d)=L-\frac{S}{AB}d-\frac{(A^2-B^2)^2\sqrt S}{6A^4B^4}d^2+O(d^3),
\]
which is the asserted expression in \(a,b\).

Finally, the 2026 classification uses \(m(a,b,c)=\min_t(a\sin t+b\cos t-c\sin t\cos t)\). For \(d\le\min\{a,b\}\),
\[
d\le m(a,b,c)
\quad\Longleftrightarrow\quad
c\le\inf_{0<t<\pi/2}\frac{a\sin t+b\cos t-d}{\sin t\cos t}
=n(a,b,d).
\]
Because \(n(a,b,0)=L>\max\{a,b\}\) and \(d<h\) for all sufficiently small \(d>0\), Theorem 1 of the source makes this condition precisely the feasibility frontier for \(\mathcal C_{03}\), \(\mathcal C_{11}\), and \(\mathcal C_{13}\).

## Verification
The accompanying `verify.py` symbolically checks the ladder minimizer identities, the tangent coefficient, and the exact second derivative
\[
n''(0)=-\frac{(a^{2/3}-b^{2/3})^2\sqrt{a^{2/3}+b^{2/3}}}{3(ab)^{4/3}}.
\]
It replays with `VERIFY_OK`. The infinite statement does not depend on finite sampling: concavity follows from an infimum of affine functions, strictness follows from a nonzero derivative at the tangent orientation, and the expansion follows from the nondegenerate implicit minimizer.

## Relationship to prior work
Mushkarov and Nikolov give a complete rectangle-feasibility classification for eight planar corridors, define both \(m(a,b,c)\) and its inverse tangent-segment functional \(n(a,b,d)\), recover the classical zero-width ladder length \(L\), and record the exact symmetric formula. They do not state the global tangent inequality, its strict anisotropic equality classification, or the two-term finite-width expansion above. Their paper also notes that older work determines the longest L-corridor rectangle of prescribed width through a sextic equation.

Boute's 2004 geometric treatment gives such a sextic relation for the standard corner and identifies the zero-width ladder extremal orientation, but the inspected text does not state a finite-width endpoint tangent law or quadratic asymptotic. Moretti's 2002 paper is the earlier calculus treatment cited by both Boute and the 2026 source; only bibliographic/abstract material was available in the bounded search. Kalman's 2007 paper concerns the zero-width ladder problem and therefore does not determine the positive-width correction.

## Limitations
The expansion is local as \(d\downarrow0\), although the tangent upper bound for \(n(a,b,d)\) is global over \(0\le d\le\min\{a,b\}\). The theorem concerns rectangles and the three ladder-limited planar corridor types only. It does not address optimal nonrectangular moving sofas, spatial boxes, or a uniform remainder constant. The older sextic equations implicitly encode the same finite-width frontier, so an unindexed prior derivation of these explicit coefficients remains a residual originality risk.

## References
1. O. Mushkarov and N. Nikolov, *Moving rectangular sofas in planar and spatial corridors*, arXiv:2604.01174v1, 2026.
2. R. T. Boute, *Moving a Rectangle around a Corner—Geometrically*, American Mathematical Monthly 111 (2004), 435–437, DOI 10.2307/4145272.
3. C. Moretti, *Moving a Couch Around a Corner*, College Mathematics Journal 33 (2002), 196–200, DOI 10.1080/07468342.2002.11921940.
4. D. Kalman, *Solving the Ladder Problem on the Back of an Envelope*, Mathematics Magazine 80 (2007), 163–182, DOI 10.1080/0025570X.2007.11953477.
