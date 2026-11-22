# An explicit three-node Gaussian rule and a sharp knot-crossing law for two-element \(C^1\) cubic splines

## Finding

For every real \(0<s<1\), let \(\mathcal S_s\) be the six-dimensional real space of functions on \([0,1]\) that are cubic polynomials on each of \([0,s]\) and \([s,1]\), with the function and its first derivative continuous at \(s\). Lebesgue integration on \(\mathcal S_s\) has exactly one **positive, three-distinct-node** quadrature rule whose nodes lie in \([0,1]\), up to permutation. No positive rule with fewer nodes is exact. The nodes and weights have an explicit formula for every nonsymmetric knot position, rather than requiring numerical continuation.

Write \(a=\min\{s,1-s\}\), so \(0<a\le1/2\), and set
\[
q(a)=12a^3-48a^2+64a-27,\qquad
u(a)=\frac{3a^4-6a^3-16a^2+48a-27}{q(a)},\qquad
v(a)=\frac{3a^4-16a^3+24a^2-9}{2q(a)}.
\]
Let \(r_2<r_3\) be the two roots of \(z^2-\nu(a)z+v(a)=0\), and define
\[
M_k(a)=\frac{1}{k+1}-\frac{16a}{27}\left(\frac a4\right)^k\quad(k=0,1,2,3),
\]
\[
\begin{aligned}
\xi_1&=a/4,& \omega_1&=16a/27,\\
\xi_2&=r_2,& \omega_2&=\frac{M_0r_3-M_1}{r_3-r_2},\\
\xi_3&=r_3,& \omega_3&=\frac{M_1-M_0r_2}{r_3-r_2}.
\end{aligned}
\]
For \(s\le1/2\), the unique rule is \((x_i,w_i)=(\xi_i,\omega_i)\). For \(s>1/2\), reflect the rule for \(a=1-s\): \(x_i=1-\xi_{4-i}\), \(w_i=\omega_{4-i}\). These formulas always have strictly positive weights and
\(0<x_1<x_2<x_3<1\).
For \(s<1/2\), one node is in \((0,s)\) and two in \((s,1)\); for \(s>1/2\) the pattern reverses. At \(s=1/2\) the rule is
\[
(x_1,x_2,x_3)=(1/8,1/2,7/8),\quad(w_1,w_2,w_3)=(8/27,11/27,8/27).
\]
Thus a quadrature node lies **exactly at the interior knot if and only if the knot is central**.

The middle-node position \(x_2(s)\) is analytic on each side of \(s=1/2\), belongs to \(C^1(0,1)\), but is not twice differentiable at the crossing:
\[
 x_2'(1/2)=\frac8{11},\qquad
 \lim_{s\uparrow1/2}x_2''(s)=\frac{96}{121},\qquad
 \lim_{s\downarrow1/2}x_2''(s)=-\frac{96}{121}.
\]
The explicit non-\(C^2\) crossing occurs despite continuous first derivatives of all nodes and weights.

## Assumptions and scope

The integral is \(I(f)=\int_0^1 f(x)\,dx\), not a weighted or probabilistic integral. Nodes are distinct and constrained to \([0,1]\); weights are strictly positive. The spline degree is at most three, and only \(C^1\) continuity is required across the one moving knot. The theorem is global for every \(0<s<1\); no claim is made for additional knots, different smoothness, negative-weight rules, or integration measures other than Lebesgue measure.

## Proof

**Basis and exactness.** Every member of \(\mathcal S_s\) is uniquely representable as
\[
f(x)=p(x)+A(x-s)_+^2+B(x-s)_+^3,\qquad \deg p\le3.
\]
Equivalently one may use \((s-x)_+^2,(s-x)_+^3\) in place of the right-truncated powers, since their differences are polynomials of degrees two and three. Thus six scalar moment equations completely certify exactness.

**Forcing the single node.** The two nonnegative splines \((s-x)_+^2\) and \((x-s)_+^2\) have positive integrals. Every positive exact rule therefore has a node strictly on each side. If there is exactly one left node \(y\) of weight \(h\), exactness for the two left-truncated powers gives
\[
h(s-y)^2=s^3/3,\quad h(s-y)^3=s^4/4,
\]
so necessarily \(y=s/4\), \(h=16s/27\). The right-hand analogue, for a single right node, forces \(y=(s+3)/4\), \(h=16(1-s)/27\). If only two positive nodes were used, there would be one on each side, and their forced weights would sum to \(16/27\), contradicting exactness on constants. Therefore three positive nodes are minimal.

**Two right nodes when \(s\le1/2\).** Fix the unique left node and weight above. The four residual polynomial moments of the two right nodes are \(M_0,M_1,M_2,M_3\). The unique monic quadratic orthogonal to both \(1\) and \(x\) for these moments is \(P(z)=z^2-\nu(s)z+v(s)\), as direct substitution verifies:
\[
M_2-\nu M_1+vM_0=M_3-\nu M_2+vM_1=0.
\]
Its coefficients are those in the Finding, and
\[
M_0M_2-M_1^2=-q(s)/324,
\]
\[
\nu^2-4v=\frac{9(1-s)^4}{q(s)^2}
(s^4-8s^3+30s^2-52s+27).
\]
For \(0<s\le1/2\), \(q'(s)=4(3s-4)^2>0\) and \(q(1/2)=-11/2\), hence \(q(s)<0\). The quartic in the discriminant becomes \(y^4+4y^3+12y^2+12y-2>0\) for \(y=1-s\ge1/2\). Thus there are two distinct real roots. To locate them, use
\[
 P(s)=\frac{9(1-s)^4(2s-1)}{2q(s)}\ge0,\qquad
 P(1)=-\frac{(1-s)^2(3s^2-14s+9)}{2q(s)}>0,
\]
\[
 M_1-sM_0=\frac{(2s-3)(4s-3)}{18}>0,
 \qquad M_0-M_1=\frac{8s^2-32s+27}{54}>0.
\]
The mean \(M_1/M_0\) lies strictly between the two roots since
\(P(M_1/M_0)=-(M_0M_2-M_1^2)/M_0^2<0\).
These signs imply \(s<r_2<r_3<1\) for \(s<1/2\); at \(s=1/2\), \(r_2=s\). The two weights displayed above are positive because the residual mean lies between the roots. By construction, the rule integrates polynomials through degree three. Its left-truncated moments are correct because
\[
\frac{16s}{27}\left(s-\frac s4\right)^k=\frac{s^{k+1}}{k+1}\quad(k=2,3).
\]
Consequently the six-dimensional spline space is integrated exactly.

**Uniqueness and the opposite node pattern.** Any positive three-node rule without a node at \(s\) has either one left and two right nodes, or two left and one right. In the first pattern the forced left node and the two residual Gaussian moments uniquely determine everything. To eliminate the second pattern for \(s<1/2\), reflect the interval and set \(t=1-s>1/2\). It would require two positive residual nodes strictly to the right of \(t\), after removing the forced left node at \(t/4\). But if \(q(t)\ge0\), then \(M_0M_2-M_1^2=-q(t)/324\le0\), impossible for two distinct positive-weight nodes. If \(q(t)<0\), the uniquely determined residual quadratic has \(P(t)<0\), so its roots straddle \(t\), again impossible. A knot-locked rule with one node on each side must have the two forced outer nodes and weights; the middle weight is \(11/27\), and its first moment is \((s+4)/9\). Matching \(1/2\) forces \(s=1/2\). At that value the displayed symmetric rule is the unique positive three-node rule. Reflection covers \(s>1/2\).

**Crossing regularity.** On \(s<1/2\), the middle node is the smaller root \(x_2(s)=(\nu(s)-\sqrt{\nu(s)^2-4v(s)})/2\). Exact differentiation at the symmetric point gives \(x_2(1/2^-)=1/2\), \(x_2'(1/2^-)=8/11\), and \(x_2''(1/2^-)=96/121\). Reflection gives \(x_2(s)=1-x_2(1-s)\) for \(s>1/2\), hence the first derivative agrees and the one-sided second derivative changes sign. The common first-derivative vector of nodes and weights, in the ordered coordinates \(x_1,x_2,x_3,w_1,w_2,w_3\), is \((1/4,8/11,1/4,16/27,0,-16/27)\) from either side. This proves the stated \(C^1\) regularity and the non-\(C^2\) claim.

## Verification

The standalone `verify.py` checks the residual-moment identities, quadratic discriminant, endpoint inequalities in symbolic factored form, exact midpoint rule, both derivatives, and numerical moment reconstruction at 100 rational knot positions using 40-digit arithmetic (1,130 assertions). It uses Python 3 with SymPy and runs as `python verify.py` alongside this file. The sign arguments, global uniqueness, and minimality are proved above for the continuum; the finite tests alone do not establish any universal claim.

## Relationship to prior work

Ait-Haddou, Bartoň and Calo (arXiv:1410.7196, first posted 27 October 2014) explicitly constructed optimal quadrature for **symmetrically stretched** \(C^1\) cubic knot sequences and supplied the central-knot rule within their symmetric family. Their symmetric theorem neither covers arbitrary nonsymmetric single-knot positions nor states the formulas or uniqueness and crossing regularity established here. Bartoň and Calo (arXiv:1505.04391, first posted 17 May 2015) described a numerical polynomial-homotopy method for deforming spline knot vectors, including nonuniform configurations and changing node patterns. That computational framework supports existence and continuous path following but does not state this explicit global one-knot rule or the precise failure of twice differentiability at its node–knot crossing. Micchelli–Pinkus existence and node-count theory, credited in both sources, predates these works; the three-node minimality here is an independent elementary verification, not a novelty claim about the general node-count principle.

## Limitations

The closed formula and uniqueness are restricted to **one interior knot and three strictly positive quadrature weights**. This does not prove that numerical homotopy is unstable, that its solutions are never \(C^2\) for other spline spaces, or that arbitrary-knot multi-element rules admit analogous formulas. The knot-crossing derivative is a regularity observation, not an algorithmic error estimate. Exhaustive bibliographic priority cannot be established by indexed search; older spline-quadrature tables or unpublished formulae could contain equivalent special cases. No independent mathematical audit has been performed.

## References

1. R. Ait-Haddou, M. Bartoň, V. M. Calo, *Explicit Gaussian quadrature rules for cubic splines with non-uniform knot sequences*, arXiv:1410.7196, first version 27 October 2014. https://arxiv.org/abs/1410.7196
2. M. Bartoň, V. M. Calo, *Gaussian quadrature for splines via homotopy continuation: rules for \(C^2\) cubic splines*, arXiv:1505.04391, first version 17 May 2015. https://arxiv.org/abs/1505.04391
3. C. A. Micchelli and A. Pinkus, work on Gaussian quadrature for spline spaces, as cited and discussed in References 1–2; consulted through those papers rather than through an independently retrieved full text.
