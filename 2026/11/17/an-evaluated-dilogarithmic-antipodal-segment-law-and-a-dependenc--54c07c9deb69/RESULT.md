# An evaluated dilogarithmic antipodal-segment law and a dependence reversal for random cyclic triangles

## Finding
Let \(V_1,V_2,V_3\) be independent, arclength-uniform points on the unit circle, and let \(T=\operatorname{conv}\{V_1,V_2,V_3\}\). For \(0\le r\le1\), put \(a_r=(r,0)\), \(b_r=(-r,0)\), and \(J(r)=\Pr\{a_r,b_r\in T\}\). The joint containment event is equivalently \([-r,r]\times\{0\}\subseteq T\).

The complete joint law is the evaluated dilogarithmic expression
\[
J(r)=\frac14+\frac6{\pi^2}\operatorname{Li}_2(-r)-\frac3{\pi^2}\operatorname{Li}_2(-r^2).
\]
Here \(\operatorname{Li}_2(z)=\sum_{n\ge1}z^n/n^2\) for \(|z|\le1\). Thus \(J(0)=1/4\), \(J(1)=0\), and \(J\) is strictly decreasing on \((0,1)\). The sharp limits are
\[
J(r)=\frac14-\frac6{\pi^2}r+O(r^2)\quad(r\downarrow0),\qquad
J(r)\sim\frac3{2\pi^2}(1-r)^2\quad(r\uparrow1).
\]

For the single-point indicator \(A_r={\bf1}_{\{a_r\in T\}}\) and its antipodal partner \(B_r={\bf1}_{\{b_r\in T\}}\), the previously known marginal is
\[
p(r)=\Pr(A_r=1)=\Pr(B_r=1)=\frac14-\frac3{2\pi^2}\operatorname{Li}_2(r^2).
\]
Their covariance \(J(r)-p(r)^2\) is \(3/16>0\) at \(r=0\), but is strictly negative for all \(r\) sufficiently close to \(1\), hence changes sign at least once in \((0,1)\). More precisely, with \(\delta=1-r\),
\[
p(r)\sim\frac3{\pi^2}\delta\log(1/\delta),\qquad
\frac{J(r)}{p(r)^2}\sim\frac{\pi^2}{6\log^2(1/\delta)}\to0.
\]
No uniqueness of the covariance zero is asserted. As an equivalent geometric consequence, the largest centered horizontal half-segment contained in \(T\), set to zero if the origin is outside \(T\), has atom \(3/4\) at zero and survival function \(J(r)\) for \(0<r\le1\).

## Assumptions and scope
The randomness is exactly three *independent* vertices uniform by angle/arclength on one Euclidean circle, not points uniform in the disk, random lines, or separate independent triangles at the two targets. Equalities at tangent or degeneracy configurations are probability zero. Formula and limits hold for the entire closed radius interval and for the specified antipodal segment only. The primary field is stochastic geometry (MSC2020 52A22).

## Proof
Write the upper-half-plane vertex (if unique) as \(U=(\cos\phi,\sin\phi)\), \(0<\phi<\pi\), and the two lower-half-plane vertices as \(L_j=(\cos\psi_j,-\sin\psi_j)\), \(0<\psi_j<\pi\). Configurations with two points in one open half-plane and one in the other have total probability \(3/4\). Interchanging the halves is a reflection, so fix the unique upper vertex. Conditional on this arrangement, \(\phi,\psi_1,\psi_2\) are independent \(\operatorname{Unif}(0,\pi)\).

The chord \(UL_j\) meets the horizontal axis at abscissa
\[
x(\phi,\psi_j)=\frac{\sin(\phi+\psi_j)}{\sin\phi+\sin\psi_j}.
\]
For fixed \(\phi\), its derivative with respect to \(\psi\) is
\[
\frac{\sin\phi\,[\cos(\phi+\psi)-1]}{(\sin\phi+\sin\psi)^2}<0
\]
for almost every interior parameter; its boundary values are \(1\) and \(-1\). Therefore \([-r,r]\) lies inside the triangle exactly when the two chord-intercepts straddle both endpoints. Set \(q=(1-r)/(1+r)\). Directly solving \(x(\phi,\psi)=r\) and \(x(\phi,\psi)=-r\) using half-angles yields the two admissible angular tail lengths
\[
\psi_+(\phi)=2\arctan\!\left(q\cot\frac\phi2\right),\qquad
\pi-\psi_-(\phi)=2\arctan\!\left(q\tan\frac\phi2\right).
\]
There are two possible assignments of the two independent lower vertices to the two tails, and the events are disjoint except on null sets. Averaging their product, then accounting for the \(3/4\) arrangement probability and writing \(t=\phi/2\), gives the exact elementary integral
\[
J(r)=\frac{12}{\pi^3}\int_0^{\pi/2}
\arctan(q\tan t)\,\arctan(q\cot t)\,dt. \tag{1}
\]

For \(0\le r<1\), the factorization
\[
\cos t+iq\sin t=\frac{1+q}{2}e^{it}(1+r e^{-2it})
\]
and the absolutely convergent logarithm series give
\[
\arctan(q\tan t)=t+\sum_{n\ge1}\frac{(-1)^nr^n}{n}\sin(2nt),
\]
\[
\arctan(q\cot t)=\frac\pi2-t-\sum_{n\ge1}\frac{r^n}{n}\sin(2nt).
\]
Uniform absolute convergence on the closed interval for every fixed \(r<1\) justifies termwise multiplication and integration. The needed integrals are
\[
\int_0^{\pi/2}t(\pi/2-t)\,dt=\frac{\pi^3}{48},\quad
\int_0^{\pi/2}t\sin(2nt)\,dt=\frac{\pi(-1)^{n+1}}{4n},
\]
\[
\int_0^{\pi/2}(\pi/2-t)\sin(2nt)\,dt=\frac\pi{4n},\quad
\int_0^{\pi/2}\sin(2nt)\sin(2mt)\,dt=\frac\pi4\mathbf1_{m=n}.
\]
Consequently the integral in (1) equals
\[
\frac{\pi^3}{48}+\frac\pi2\operatorname{Li}_2(-r)-\frac\pi4\operatorname{Li}_2(-r^2),
\]
which proves the asserted closed form for \(r<1\). Continuity also proves the endpoint \(r=1\).

Differentiate using \((\operatorname{Li}_2(z))'=-\log(1-z)/z\) to obtain
\[
J'(r)=\frac6{\pi^2r}\log\frac{1+r^2}{1+r}<0\quad(0<r<1).
\]
As \(r\uparrow1\), \(J'(r)=-3(1-r)/\pi^2+O((1-r)^2)\); since \(J(1)=0\), integration yields \(J(r)=3(1-r)^2/(2\pi^2)+O((1-r)^3)\). Taylor expansion at \(r=0\) gives the other endpoint.

The cited single-point law has \(p(r)=1/4-3\operatorname{Li}_2(r^2)/(2\pi^2)\). Its derivative is \(p'(r)=3\log(1-r^2)/(\pi^2 r)\), which integrates near \(r=1\) to \(p(r)\sim3(1-r)\log(1/(1-r))/\pi^2\). This plus the joint expansion proves the ratio and the negative covariance near one. At zero the two indicators coincide with probability \(1/4\), so covariance is \(1/4-(1/4)^2=3/16\). Continuity proves at least one sign change. Finally the half-segment survival identity is direct from convexity and the definition of the largest contained centered segment.

## Verification
The included `checker.py` independently integrates (1), evaluates the dilogarithms, and uses independently generated Cartesian vertices and signed-area half-plane tests for \(800000\) triangles at three radii. It also checks the quadratic endpoint coefficient and opposite covariance signs. Run `python checker.py` after installing packages from `requirements.txt`. Finite sampling and quadrature support, but do not prove, the exact Fourier identity or asymptotic limits; these are proved above.

## Relationship to prior work
Wendel (1962) established the classical centered inclusion probability \(1/4\), and Kabluchko–Vysotsky–Zaporozhets (2015) revisited related convex-hull absorption identities. The 2019 Mathematics@CUHK treatment of inscribed-triangle containment **already gives a general four-double-integral formula for any interior segment**. Hence the existence of an integral for segment coverage, and even general segment coverage itself, are *prior art*, not claimed here. The contribution is the fully evaluated dilogarithmic simplification in the antipodal one-parameter geometry, its sharp quadratic boundary law, and the correlated-versus-anticorrelated two-site containment effect. The single-point marginal, first obtained by Jeremy Tan Jie Rui (2018) and reproved by Ismailov (2026), is also prior art. These references and the related archived geometric probability literature were compared by mathematical implication, not by title alone.

## Limitations
No claim is made of priority over unindexed work or over possible earlier evaluations hidden in the 2019 general segment integrals. The exact single-point dilogarithm is not new. No uniqueness or closed form for the radius of covariance sign reversal is proved. The statements are limited to three independent circle-uniform vertices, a unit circle (or its similarity images), and two exactly antipodal target points. Self-review does not constitute an independent audit.

## References
1. J. G. Wendel, “A Problem in Geometric Probability,” *Mathematica Scandinavica* **11** (1962), 109–111, DOI:10.7146/math.scand.a-10655. https://journals.msp.org/mscand/article/view/2688
2. Z. Kabluchko, V. Vysotsky, D. Zaporozhets, “Convex hulls of random walks, hyperplane arrangements, and Weyl chambers,” arXiv:1510.04073 (first submitted 2015-10-14). https://arxiv.org/abs/1510.04073
3. KKK, “Probability that a random inscribed triangle contains another circle,” Mathematics@CUHK, 2019-08-26, especially §5 (arbitrary segment). https://cuhkmath.wordpress.com/2019/08/26/probability-that-a-random-inscribed-triangle-contains-another-circle/
4. A. Ismailov, “With what probability does an inscribed triangle contain a given point?,” arXiv:2601.02929 (2026), credits Jeremy Tan Jie Rui (2018) for the single-point formula. https://arxiv.org/abs/2601.02929
