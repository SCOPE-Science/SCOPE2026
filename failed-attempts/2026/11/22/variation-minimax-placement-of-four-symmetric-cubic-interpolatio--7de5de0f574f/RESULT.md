# Variation-minimax placement of four symmetric cubic interpolation nodes

## Finding
For \(0<a<1\), let \(I_a:\mathbb R^4\to\mathbb P_3\) interpolate data \(y=(y_0,y_1,y_2,y_3)\) at the ordered nodes \((-1,-a,a,1)\). Define the nodal and output variations by
\[
V_d(y)=\sum_{j=1}^3|y_j-y_{j-1}|,\qquad V_c(p)=\int_{-1}^1|p'(x)|\,dx.
\]
Then the *exact, attained* operator seminorm for every \(0<a<1\) is
\[
\boxed{\sup_{V_d(y)>0}\frac{V_c(I_a y)}{V_d(y)}=\max\{A(a),B(a)\}},
\]
where
\[
A(a)=1+\frac{4(1+3a^2)^{3/2}}{27(1-a^2)},\qquad
B(a)=\frac{4(1+a+a^2)^{3/2}}{3\sqrt3\,a(1+a)}-1.
\]
The branch \(A\) is attained by a terminal step in the nodal data and its reflection; \(B\) is attained by a central step. The two branches are respectively strictly increasing and strictly decreasing on \((0,1)\). Consequently there is a **unique variation-optimal symmetric grid** with
\[
\boxed{A(a_*)=B(a_*),\quad 0.48013692628<a_*<0.48013692629},
\]
and sharp optimal gain
\[
\boxed{1.4235939250<\inf_{0<a<1}\|I_a\|_{V_d\to V_c}<1.4235939251}.
\]
For comparison, the four equally spaced nodes correspond to \(a=1/3\), giving gain approximately \(2.0068508881\), and the four Chebyshev–Lobatto nodes correspond to \(a=1/2\), giving approximately \(1.4572903501\). Thus symmetric node designs optimal for other interpolation objectives need not optimize total variation.

## Assumptions and scope
All data are real, without monotonicity, positivity, or smoothness assumptions. The output variation is the integral of the absolute classical derivative on the *whole* interval, not the discrete variation at the interpolation nodes or the maximum pointwise range escape. Denominators are nonzero since \(0<a<1\). Constants are in the null space of both variations, so the quotient is taken only over \(V_d(y)>0\). The optimization is over exactly the symmetric family with both endpoints fixed. Affine changes of independent variable leave the dimensionless gain invariant. No assertion of optimality among asymmetric four-node systems is made.

## Proof
Write \(d_k=y_k-y_{k-1}\), \(k=1,2,3\), and let \(S_{k,a}=I_a(\mathbf1_{\{j\ge k\}})\) be the interpolant of the corresponding nodal step. Polynomial interpolation reproduces constants, giving
\[
I_a y=y_0+\sum_{k=1}^3 d_kS_{k,a}.
\]
By the triangle inequality for \(\int|p'|\),
\[
V_c(I_a y)\le\sum_{k=1}^3|d_k|V_c(S_{k,a})
\le\bigl(\max_kV_c(S_{k,a})\bigr)V_d(y).
\]
Choosing one unit step as input gives equality for whichever index maximizes the three step variations. Thus the entire operator seminorm reduces *exactly* to three step responses, not to a sample-based bound.

For the terminal step define
\[
T_a(x)=S_{3,a}(x)=\frac{(x+1)(x^2-a^2)}{2(1-a^2)}.
\]
Reflection yields \(S_{1,a}(x)=1-T_a(-x)\), so the first and third steps have the same variation. The derivative
\[
S'_{1,a}(x)=\frac{3x^2-2x-a^2}{2(1-a^2)}
\]
changes sign at \(r_\pm=(1\pm\sqrt{1+3a^2})/3\), both strictly inside \((-1,1)\). It is positive outside \((r_-,r_+)\) and negative inside. Since \(S_{1,a}(-1)=0\) and \(S_{1,a}(1)=1\), the total variation is
\[
V_c(S_{1,a})=1+2\bigl(S_{1,a}(r_-)-S_{1,a}(r_+)\bigr)
=1+\frac{4(1+3a^2)^{3/2}}{27(1-a^2)}=A(a).
\]
The second identity follows from integrating the quadratic derivative over its two roots, and is valid throughout \(0<a<1\).

For the central step, with \(q=1+a+a^2\), direct interpolation and reflection give
\[
S_{2,a}(x)=\frac12+\frac{x(q-x^2)}{2a(1+a)},\qquad
S'_{2,a}(x)=\frac{q-3x^2}{2a(1+a)}.
\]
Its turning points are \(\pm t\), \(t=\sqrt{q/3}\in(0,1)\). The derivative is positive between them and negative outside. Therefore
\[
V_c(S_{2,a})=2\bigl(S_{2,a}(t)-S_{2,a}(-t)\bigr)-1
=\frac{4q^{3/2}}{3\sqrt3\,a(1+a)}-1=B(a).
\]
This proves the claimed formula and all its sharpness statements.

The function \(A(a)\) is strictly increasing because its positive numerator increases and denominator decreases. For \(B(a)+1>0\), logarithmic differentiation yields
\[
\frac{d}{da}\log(B(a)+1)
=\frac{(1+2a)(a^2+a-2)}{2a(1+a)(1+a+a^2)}<0
\quad(0<a<1).
\]
Moreover, \(B(a)\to\infty\) as \(a\downarrow0\) while \(A(a)\to31/27\); and \(A(a)\to\infty\) as \(a\uparrow1\) while \(B(a)\to1\). Thus \(A=B\) has exactly one solution. The envelope \(\max(A,B)\) strictly decreases to that crossing and strictly increases thereafter. The strict rational enclosures above are verified by integer square-root bounds in the accompanying checker; they are not assumptions in the uniqueness proof.

## Verification
The standalone `verify.py` reconstructs the four cardinal polynomials, verifies their partition of unity and all three step formulas, checks the critical-point and variation identities symbolically, and verifies the logarithmic derivative identity. Integer arithmetic with rational lower and upper bounds for square roots certifies opposite signs of \(A-B\) at \(48013692628/10^{11}\) and \(48013692629/10^{11}\), and encloses the optimal gain between the two stated decimal rationals. It also makes exact comparisons with the equally spaced and Chebyshev–Lobatto grids. A separate direct polynomial integration test on 4,000 deterministic random instances checks the norm inequality numerically. No finite experiment substitutes for the all-data or unique-global-minimum arguments.

Run `python verify.py` with Python 3.10+, SymPy, and NumPy. The checker is self-contained apart from those declared packages.

## Relationship to prior work
Berrut and Trefethen (2004) describe classical and barycentric Lagrange interpolation and emphasize numerical stability and Chebyshev nodes. Gunzburger and Teckentrup (arXiv:1407.3291v1) optimize the *uniform* Lebesgue constant, not variation of an interpolating polynomial relative to variation of its nodal data. Prestin (1993) investigates convergence and weighted \(L^p\) error for interpolation of bounded-variation functions at Jacobi abscissas; the accessible portions do not give the present finite symmetric-grid seminorm or node minimax.

A published full-interval four-node result for exactly the same symmetric grids computes the worst *pointwise range excursion* for nondecreasing bounded data, with optimizer approximately \(0.4458209225\). Its proof supplies step polynomials also used here, but its range bound cannot determine the variation: variation counts all excursions and turning points, including a positive lobe that the range-defect objective ignores. The exact function \(\max(A,B)\) and its different minimax parameter are not statements or mathematical consequences of its range-defect bound alone. A separate published equispaced four-node result concerns pointwise excursion only over the central cell. The close shared algebra is a historical-priority risk and is acknowledged; no exclusivity or independent novelty certification is claimed.

## Limitations
The classification is limited to real, symmetric, endpoint-fixed four-node cubic interpolation. It does not determine the unrestricted asymmetric four-node optimum, variation on proper subintervals, higher polynomial degrees, or perturbations of knot positions. The proof concerns the seminorm of interpolated signals, not uniform interpolation error, floating-point sensitivity, or variation of a series of interpolants. Searches and accessible documents do not rule out an unindexed equivalent formula or an older small-degree table. Independent mathematical validation has not been performed.

## References
1. J.-P. Berrut and L. N. Trefethen, *Barycentric Lagrange Interpolation*, SIAM Review **46** (2004), 501–517. DOI: 10.1137/S0036144502417715; full text: https://people.maths.ox.ac.uk/trefethen/barycentric.pdf (first electronic publication 2004-07-30).
2. M. Gunzburger and A. L. Teckentrup, *Optimal Point Sets for Total Degree Polynomial Interpolation in Moderate Dimensions*, arXiv:1407.3291v1 (2014-07-11), https://arxiv.org/abs/1407.3291.
3. J. Prestin, *Lagrange interpolation for functions of bounded variation*, Acta Mathematica Hungarica **62** (1993), 1–13, DOI: 10.1007/BF01874212 (full text not independently inspected).
4. *Optimal symmetric four-node cubic interpolation for monotone range control*, publicly accessible research finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-optimal-symmetric-four-node-cubic-interpolation-for-monotone-ran--7f9a4d5c7ee7.
5. *Sharp monotone range defect of uniform four-point cubic Lagrange interpolation*, publicly accessible research finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-monotone-range-defect-of-uniform-four-point-cubic-lagrange--1fad48a6c445.
