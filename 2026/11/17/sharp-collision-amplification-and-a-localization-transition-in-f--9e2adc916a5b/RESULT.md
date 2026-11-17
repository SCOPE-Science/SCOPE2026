# Sharp collision amplification and a localization transition in four-site quadratic midpoint-knot splines

## Finding
For each fixed real \(R>1\), and \(0<\varepsilon<1\), let \(I_{\varepsilon,R}:\mathbb R^4\to C[0,R]\) interpolate arbitrary values at the four data sites \(0,\varepsilon,1,R\) by a continuously differentiable, degree-at-most-two spline with the sole interior knot \(\kappa_\varepsilon=(1+\varepsilon)/2\). Give the data \(\mathbb R^4\) the maximum norm and the spline the uniform norm, and set \(\Lambda(\varepsilon,R)=\|I_{\varepsilon,R}\|\).

As the first two data sites merge, the entire scaled interpolation operator converges in norm to a **rank-one collision operator**:
\[
\lim_{\varepsilon\downarrow0}\sup_{\|y\|_\infty\le1}
\left\|\varepsilon I_{\varepsilon,R}y-(y_2-y_1)g_R\right\|_\infty=0,
\]
where
\[
g_R(t)=\begin{cases}
 t-\dfrac{4R-1}{3R-1}t^2,&0\le t\le\tfrac12,\\[3pt]
 \dfrac{(t-1)(t-R)}{3R-1},&\tfrac12\le t\le R.
\end{cases}
\]
Consequently the **exact leading operator-norm coefficient** is
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon\Lambda(\varepsilon,R)
=\max\left\{\frac{3R-1}{2(4R-1)},\ \frac{(R-1)^2}{2(3R-1)}\right\}.}
\]
There is a unique localization transition at \(R_*=2+\sqrt3\). For \(1<R<R_*\), every sequence of maximizers of the Lebesgue function has limit \(t=(3R-1)/(2(4R-1))\), inside the first spline piece. For \(R>R_*\), every such sequence tends to \(t=(1+R)/2\), inside the second piece. At \(R=R_*\), all limit points belong to these two distinct positions, and both locations maximize the limiting profile. The upper limits are attained by sign-opposed data at the colliding pair, with the other two data remaining uniformly bounded.

## Assumptions and scope
The parameter \(R>1\) is fixed as \(\varepsilon\downarrow0\). The interpolation space is the four-dimensional space of continuous \(C^1\) piecewise quadratics on the two intervals \([0,\kappa_\varepsilon]\) and \([\kappa_\varepsilon,R]\), with no additional interior knot, matching the quadratic midpoint not-a-knot scheme on four nodes. The statement concerns arbitrary bounded **real** nodal data; the same leading norm follows for complex data by the triangle inequality. It is a fixed-four-node collision limit, not a uniform-in-\(R\) estimate or a many-node theorem.

## Proof
Write the two pieces as \(P(t)=a_0+a_1t+a_2t^2\) and \(Q(t)=b_0+b_1t+b_2t^2\). The six conditions are \(P(0)=y_1\), \(P(\varepsilon)=y_2\), \(Q(1)=y_3\), \(Q(R)=y_4\), and equality of \(P,Q\) and of \(P',Q'\) at \(\kappa_\varepsilon\). Their coefficient matrix in \((a_0,a_1,a_2,b_0,b_1,b_2)\) has determinant
\[
\frac{\varepsilon(R-1)(\varepsilon-1)
\big(-R\varepsilon-3R+\varepsilon^2+2\varepsilon+1\big)}4.
\]
This determinant is nonzero when \(0<\varepsilon<1<R\): the final factor is strictly negative because \(\varepsilon^2+2\varepsilon+1-R(\varepsilon+3)<(\varepsilon+1)^2-(\varepsilon+3)<0\). (Alternatively use Schoenberg--Whitney unisolvence.)

Replace the second interpolation equation by \((P(\varepsilon)-P(0))/\varepsilon=(y_2-y_1)/\varepsilon\). The determinant of this transformed matrix has the nonzero limit \((R-1)(3R-1)/4\). Hence its inverse is continuous at \(\varepsilon=0\), and the coefficients of \(\varepsilon I_{\varepsilon,R}y\) tend uniformly for \(\|y\|_\infty\le1\) to those of the confluent interpolation problem with zero values at \(t=0,1,R\), and derivative \(y_2-y_1\) at \(t=0\). The moving knot tends to \(1/2\); coefficient convergence gives uniform convergence of the piecewise functions on the common domain. This proves the operator-norm convergence once the solution to the confluent problem is computed.

For derivative one, the left piece must be \(t+At^2\), and the right piece has the form \(C(t-1)(t-R)\). Matching the values and first derivatives at \(1/2\) gives \(A=-(4R-1)/(3R-1)\) and \(C=1/(3R-1)\). Thus the confluent solution is \(g_R\), and linearity supplies the factor \(y_2-y_1\). Since \(\sup_{\|y\|_\infty\le1}|y_2-y_1|=2\), the limiting norm is \(2\|g_R\|_\infty\).

On \([0,1/2]\), \(g_R\) is a strictly concave quadratic with its unique peak at \(u_R=(3R-1)/(2(4R-1))\) and height \(A_R=(3R-1)/(4(4R-1))\). On \([1/2,R]\), its maximum positive value occurs at \(1/2\) and is smaller than \(A_R\), while its unique negative trough occurs at \(v_R=(1+R)/2\), of magnitude \(B_R=(R-1)^2/(4(3R-1))\). Comparing \(A_R\) and \(B_R\), their difference has the sign of
\[
(3R-1)^2-(4R-1)(R-1)^2
=-2(2R-1)(R^2-4R+1).
\]
The sole crossing for \(R>1\) is \(2+\sqrt3\). Hence \(\|g_R\|_\infty=\max\{A_R,B_R\}\), giving the asserted sharp coefficient and the two norming regions. Finally, uniform convergence of the scaled Lebesgue functions to \(2|g_R|\) (from the convergence of each basis function) and compactness of \([0,R]\) imply the stated localization of every maximizing sequence.

## Verification
The standalone `checker.py` builds the six interpolation equations, solves for the four Lagrange functions, tests the nodal and \(C^1\) constraints, and compares \(\varepsilon\Lambda(\varepsilon,R)\) to the derived limit on meshes approaching collision on both sides of the transition. These finite computations are diagnostics, not the proof of the operator limit. For example \(R=2\) gives coefficient \(5/14\); \(R=4\) gives coefficient \(9/22\). Exact determinant and stationary-point formulas are derived above rather than inferred from the checker.

## Relationship to prior work
Greene (2026) establishes well-posedness and optimal cubic convergence of the midpoint-knot quadratic not-a-knot interpolant for smooth input on arbitrary meshes, and notes Powell's older non-uniform-boundedness observation for arbitrary nodal data. Those results motivate the collision problem but do not give the sharp leading Lebesgue constant or the threshold where the norming position moves between the spline pieces. Powell (1981) is a priority-risk source because its relevant chapters could not be inspected in full. No claim is made to the classical spline construction or to its smooth-data convergence theorem.

## Limitations
The theorem is a minimal four-site example with one collapsing adjacent pair and fixed outer-site ratio. It neither bounds the norm uniformly over arbitrary partitions nor supplies the next-order term in \(\varepsilon\). Its publication priority remains uncertain without complete access to Powell's detailed text and all earlier spline-instability work. The equality data statement is asymptotic; it does not classify all maximizers for positive \(\varepsilon\).

## References
- A. Greene, *Optimal Convergence of Quadratic Not-a-Knot Spline Interpolation on Arbitrary Partitions*, arXiv:2610.32044, initial submission 23 October 2026, https://arxiv.org/abs/2610.32044. Sections 1–4, especially Proposition 2.1 and Lemma 4.1.
- M. J. D. Powell, *Approximation Theory and Methods*, Cambridge University Press, 1981, especially Eq. (18.40) and §21.2 (cited in Greene 2026); full relevant text not inspected.
- L. L. Schumaker, *Spline Functions: Basic Theory*, 3rd ed., Cambridge University Press, 2007, Schoenberg–Whitney interpolation criterion (as cited in Greene 2026).
