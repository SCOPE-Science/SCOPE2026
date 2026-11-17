# An exact mean-deficit boundary layer for random hyperbolic cyclic triangles

## Finding

In the curvature-\(-1\) hyperbolic plane, sample three independent arclength-uniform points on a geodesic circle of radius \(R>0\). Let \(r_R\) be the inradius of their geodesic triangle and let
\[
r_*=\operatorname{arctanh}(1/2)=\tfrac12\log 3.
\]
Then the **mean incircle deficit** has the sharp, nonzero asymptotic
\[
\boxed{\lim_{R\to\infty}e^R\mathbb E(r_*-r_R)
=3-\frac{12}{\pi\sqrt3}\operatorname{arctanh}(1/\sqrt3)
=1.547846114742868\ldots.}
\]
The factor \(e^R\), rather than \(e^{2R}\), arises from angular near-collisions. An exact limiting description of those collisions is available under **deficit-weighted sampling**.

Let \(G_1,G_2,G_3\) be the successive positive angular gaps, in circular order, between the three sampled points, so \(G_1+G_2+G_3=2\pi\). Set \(J_R\) equal to the index of the smallest gap (ties have probability zero),
\[
X_R=e^R G_{J_R},\qquad B_R=G_{J_R+1},
\]
with cyclic indices. Define a new probability law on triangles by
\[
\mathbb Q_R(E)=\frac{\mathbb E[(r_*-r_R)\mathbf1_E]}{\mathbb E(r_*-r_R)}.
\]
For \(x>0\), put
\[
z(x)=\exp[-2\operatorname{arsinh}(x/4)],\quad
\delta(x)=\frac12\log\!\left(\frac{3(1+z(x))}{3-z(x)}\right),\quad
I=\int_0^\infty\delta(x)\,dx
=\pi-\frac4{\sqrt3}\operatorname{arctanh}(1/\sqrt3).
\]
Then **the joint law of \((J_R,X_R,B_R)\) under \(\mathbb Q_R\) converges in total variation** to mutually independent variables: a uniform index on \(\{1,2,3\}\), an \(X\) with density \(\delta(x)/I\) on \((0,\infty)\), and a uniform angle on \((0,2\pi)\). Equivalently, the limiting joint density with respect to counting measure on the indices and Lebesgue measure on \((x,b)\) is \(\delta(x)/(6\pi I)\).

## Assumptions and scope

Sampling is independent and uniform by *hyperbolic arclength* on one circle in the complete curvature-\(-1\) plane. The three vertices are almost surely distinct. The polygon is the geodesic triangle formed by its three unique minimizing segments. All limits send the common circumradius \(R\) to \(+\infty\); no simultaneous sample-size limit is involved. Deficit-weighting is a specified change of probability measure, not ordinary conditioning on an event.

## Proof

**1. Exact geometric identity.** For consecutive gaps \(g_1,g_2,g_3\) summing to \(2\pi\), the opposite geodesic side lengths satisfy the hyperbolic chord formula
\[
a_i=2\operatorname{arsinh}(\sinh R\sin(g_i/2)),\qquad s=(a_1+a_2+a_3)/2.
\]
The classical hyperbolic Staudtian inradius identity (see Horváth, Theorem 4.10) gives
\[
\tanh^2r_R=\frac{\sinh(s-a_1)\sinh(s-a_2)\sinh(s-a_3)}{\sinh s}.
\]
Define \(u_i=e^{-2(s-a_i)}\), each strictly between zero and one by the triangle inequalities. Elementary factorization yields
\[
4\tanh^2r_R=\frac{(1-u_1)(1-u_2)(1-u_3)}{1-u_1u_2u_3}.
\tag{1}
\]
Because the product of the three \((1-u_i)\) and \(u_1u_2u_3\) are probabilities of disjoint outcomes, their sum does not exceed one. Thus \(0<r_R<r_*\). For fixed strictly positive angular gaps, \(u_i\to0\), hence \(r_R\to r_*\).

**2. A uniform integrable envelope.** Put
\[
x_i=\sinh R\sin(g_i/2),\quad y_i=x_i+\sqrt{1+x_i^2},\quad m=\min_i x_i.
\]
Then \(u_i=(y_i/(y_jy_k))^2\). Since the three half-gaps are positive and sum to \(\pi\), their sines obey \(x_i\le x_j+x_k\). For \(x_j,x_k\ge m\),
\[
y_i\le1+2(x_j+x_k)\le4(1+(x_j+x_k)/2),
\]
while
\[
y_jy_k\ge(1+x_j)(1+x_k)
\ge(1+m)(1+(x_j+x_k)/2).
\]
Consequently \(u_i\le16/(1+m)^2\). Applying (1), the mean-value bound for \(\operatorname{arctanh}\) on \([0,1/2]\), and \(1-\prod_i(1-u_i)\le\sum_i u_i\), gives
\[
0\le r_*-r_R\le\frac{32}{(1+m)^2}.
\]
If \(g_{\min}=\min_i g_i\), the monotonicity/symmetry of sine implies \(\min_i\sin(g_i/2)\ge g_{\min}/\pi\). For \(R\ge1\), \(\sinh R\ge c e^R\), for an absolute \(c>0\). Hence, with another absolute constant \(C_0\),
\[
0\le r_*-r_R\le\frac{C_0}{(1+e^R g_{\min})^2}.
\tag{2}
\]
This bound controls the small-gap boundary layer and makes its scaled integral uniformly integrable. It also controls configurations in which two gaps shrink simultaneously.

**3. Boundary-layer profile.** Fix \(x>0\) and \(b\in(0,2\pi)\). In the gap chart
\[
(g_1,g_2,g_3)=(xe^{-R},b,2\pi-b-xe^{-R}),
\]
the first side length tends to \(2\operatorname{arsinh}(x/4)\), while the other two sides diverge and their difference tends to zero. In (1), this means \(u_1\to0\) and \(u_2,u_3\to z(x)\). Thus
\[
r_*-r_R\longrightarrow
r_*-\operatorname{arctanh}\!\big((1-z(x))/2\big)
=\delta(x).
\tag{3}
\]
The limit is independent of the remaining angle \(b\). The profile is positive, bounded near zero and is \(8/(3x^2)+O(x^{-4})\) as \(x\to\infty\), so \(I\in(0,\infty)\).

**4. Sharp expectation.** The cyclic gap vector is Dirichlet\((1,1,1)\) multiplied by \(2\pi\), with planar density \(1/(2\pi^2)\) on its open simplex. Partition by the smallest-gap index. Each of the three equal integrals admits the coordinates \(g_i=xe^{-R}\), \(g_{i+1}=b\), whose Jacobian is \(e^{-R}\). Its domain is \(0<x<(2\pi/3)e^R\) and \(xe^{-R}<b<2\pi-2xe^{-R}\). Equations (2)–(3) and dominated convergence yield
\[
\lim_{R\to\infty}e^R\mathbb E(r_*-r_R)
=\frac3{2\pi^2}\int_0^\infty\!\int_0^{2\pi}\delta(x)\,db\,dx
=\frac{3I}{\pi}.
\tag{4}
\]
To evaluate \(I\), substitute \(t=\exp[-\operatorname{arsinh}(x/4)]\). An integration by parts gives
\[
I=8\int_0^1\frac{1-t^2}{(1+t^2)(3-t^2)}dt
=4\int_0^1\left(\frac1{1+t^2}-\frac1{3-t^2}\right)dt
=\pi-\frac4{\sqrt3}\operatorname{arctanh}(1/\sqrt3).
\]
Substitution in (4) proves the displayed constant.

**5. The marked total-variation law.** On the same chart, the \(\mathbb Q_R\)-density of \((J_R,X_R,B_R)\) is
\[
\frac{e^{-R}(r_*-r_R)}{2\pi^2\,\mathbb E(r_*-r_R)}
\mathbf1_{\{xe^{-R}<b<2\pi-2xe^{-R}\}}.
\]
For each index and almost every \((x,b)\) it converges, using (3)–(4), to \(\delta(x)/(6\pi I)\). This limiting density integrates to one across all three indices. Scheffé's lemma proves convergence in total variation. Factorization yields the stated independence and normalized laws.

## Verification

The supplementary executable `check_inradius.py` uses two independent constructions of hyperbolic inradius: the Staudtian side-length identity and intersecting unit-spacelike geodesic normals in the hyperboloid model. It checks the collision chart numerically, evaluates \(I\) both directly and after substitution, and compares Monte Carlo scaled means with the exact coefficient. Run from this directory using `python check_inradius.py` with NumPy and SciPy installed. These computations corroborate but do not replace the analytic proof above.

## Relationship to prior work

The hyperbolic inradius identity is classical and is explicitly recorded in Horváth (2014, Theorem 4.10). Brody–Schettler (2014) study fixed-inradius hyperbolic triangle families and arithmetic curves, not random expanding circles. A previously recorded result for precisely this random-circle ensemble already supplies the almost-sure \(e^{2R}\)-rescaled deficit law, its heavy tail and marked large-deficit excursions; **none of those statements is claimed here**. Crucially, those distributional statements do not determine the mean, because the rescaled limit has infinite first moment. The present result derives a different \(e^{-R}\) expectation scale and identifies its angular boundary-layer contribution and its deficit-weighted configuration law. Separate research on the acuteness probability of random hyperbolic cyclic triangles addresses a different functional of the same ensemble.

## Limitations

The result is for three independent arclength-uniform vertices, fixed curvature \(-1\), and a common expanding geodesic circle. It does not provide a finite-radius error rate, a higher-moment asymptotic, or extensions to general negatively curved surfaces. The exact constant and total-variation limit are proved, but historical originality beyond inspected sources remains provisional. No independent mathematical audit has been performed.

## References

1. Ákos G. Horváth, *Hyperbolic plane geometry revisited*, first public arXiv version 2014-05-05, arXiv:1405.1068, Theorem 4.10 and the Staudtian formulas. https://arxiv.org/abs/1405.1068
2. Nicolas Brody and Jordan Schettler, *Rational Hyperbolic Triangles and a Quartic Model of Elliptic Curves*, first public arXiv version 2014-06-02, arXiv:1406.0467. https://arxiv.org/abs/1406.0467
