# Quartic onset of coverage by four random spherical caps

## Finding
Let \(U_1,U_2,U_3,U_4\) be independent uniform points on the unit two-sphere \(S^2\). For an angular radius \(w\), place a closed spherical cap of radius \(w\) at each point, and denote by \(p(w)\) the probability that these four caps cover all of \(S^2\). Put \(w_0=\arccos(1/3)\), the optimal four-cap covering radius. Then
\[
 p(w)=0\quad(w\le w_0),\qquad
 \lim_{\varepsilon\downarrow0}\frac{p(w_0+\varepsilon)}{\varepsilon^4}=\frac{16\sqrt3}{\pi}.
\]
Equivalently, for \(\delta=1/3-\cos w\downarrow0\),
\[
 p(w)=\frac{81\sqrt3}{4\pi}\,\delta^4+o(\delta^4).
\]
The asymptotic is a fixed-sample small-excess law, not a large-number-of-caps or high-dimensional limit. Angular excess is measured in radians.

## Assumptions and scope
The four centers are ordered/labeled, independently sampled using normalized surface area \(d\sigma/(4\pi)\). The caps are equal and geodesic; the radius is strictly below \(\pi/2\) in the asymptotic regime. The probability includes both mirror-image orientation classes of labeled regular tetrahedra. The result describes the first-order nonzero term as the radius decreases to its sharp tetrahedral covering threshold; it does not give the complete distribution away from the threshold.

Write \(K=\operatorname{conv}(U_1,U_2,U_3,U_4)\). By the support-function criterion, the caps cover precisely when
\[
 h_K(y)=\max_i y\cdot U_i\ge\cos w\quad\text{for every }y\in S^2,
\]
which for positive \(\cos w\) is equivalent to \(B_{\cos w}(0)\subset K\). If the origin lies inside this tetrahedron, and \(h_i>0\) are the distances from the origin to its four facet planes, this is equivalent to \(\min_i h_i\ge\cos w\). The simplex Euler inequality \(R\ge3r\), applied to a tetrahedron with circumradius \(R=1\) and inradius \(r\), shows that \(\min_i h_i\le1/3\); equality forces a regular tetrahedron. Conversely, a regular tetrahedron on \(S^2\) has all four facet distances \(1/3\). Thus no covering is possible below \(w_0\), and the equality set consists of exactly two rotation orbits of *ordered* regular tetrahedra (the two chiralities).

## Proof
### 1. A smooth coordinate chart at the tetrahedral optimizers
Use the four ideal vertices
\[
 v_1=(1,1,1)/\sqrt3,\quad v_2=(1,-1,-1)/\sqrt3,\quad
 v_3=(-1,1,-1)/\sqrt3,\quad v_4=(-1,-1,1)/\sqrt3.
\]
For a small real symmetric trace-free matrix
\[
 A=\begin{pmatrix}a&p&q\\p&b&r\\q&r&-a-b\end{pmatrix},
\]
define \(u_i(A)=(I+A)v_i/\lVert(I+A)v_i\rVert\). Allow in addition a common rotation \(G\in SO(3)\). The map \((G,A)\mapsto(Gu_1(A),\ldots,Gu_4(A))\) has invertible derivative at every \((G,0)\), as verified below by its positive-definite Gram matrix. It is therefore a local diffeomorphism onto all eight-dimensional configurations near the chosen ordered regular-tetrahedron orbit. Its reflected analogue covers the second orbit.

Write \(c=-a-b\), \(Q=a^2+b^2+c^2\), \(T=(p,q,r)\). Let
\[
 L_1=p+q+r,\quad L_2=-p-q+r,\quad
 L_3=-p+q-r,\quad L_4=p-q-r.
\]
For the facet opposite vertex \(u_i(A)\), denote the outward unit normal by \(n_i(A)\) and its signed distance from the origin by \(h_i(A)\). These are analytic near \(A=0\), and \(h_i(0)=1/3\). Their uniform local expansion is
\[
 h_i(A)=\frac13+\frac8{27}L_i-\frac29Q
 +O\!\left(Q^{3/2}+\sqrt Q\,\lVert T\rVert+\lVert T\rVert^2\right).
\tag{1}
\]
To calculate the linear term, differentiate \(n_i\cdot u_j=h_i\) for the three indices \(j\ne i\). Using \(\sum_i v_i=0\), \(v_i\cdot v_j=-1/3\), and \(\sum_i v_iv_i^{\mathsf T}=(4/3)I\), one finds \(h_i'(0)=(4/9)v_i^{\mathsf T}Av_i=(8/27)L_i\). Pure diagonal perturbations give a tetrahedron with vertices \((\pm x,\pm y,\pm z)\), where the sign product is positive and
\[
 (x,y,z)=\frac{(1+a,1+b,1+c)}{\sqrt{3+Q}}.
\]
Each facet then has the same distance \((x^{-2}+y^{-2}+z^{-2})^{-1/2}=1/3-(2/9)Q+O(Q^{3/2})\). Taylor's theorem establishes the remainder in (1).

### 2. Anisotropic localization
Put \(\delta=1/3-\cos w>0\). Because \(\sum_iL_i=0\) and the four vectors giving \(L_i\) span \(\mathbb R^3\), there is an absolute constant \(c_0>0\) such that \(\min_i L_i\le-c_0\lVert T\rVert\). Equation (1) and absorption of its remainder in a sufficiently small fixed neighborhood show that
\[
 \frac13-\min_i h_i(A)\ge c_1(\lVert T\rVert+Q)
\]
for some \(c_1>0\). Compactness and the uniqueness of the global optimizers imply that every configuration satisfying \(\min_i h_i\ge1/3-\delta\) lies in the union of these neighborhoods for sufficiently small \(\delta\). Hence the entire event satisfies
\[
 T=O(\delta),\qquad (a,b,c)=O(\sqrt\delta),
\]
uniformly over the event. On this anisotropic scale, the remainder in (1) is \(O(\delta^{3/2})\). The rescaled feasible sets converge, except on their measure-zero boundaries, to
\[
 L_i\ge-\frac{27}{8}\left(\delta-\frac29Q\right),\qquad i=1,2,3,4.
\tag{2}
\]
The quantitative localization above permits dominated convergence of their rescaled Lebesgue volumes.

### 3. Five-dimensional local volume
For a fixed diagonal pair with \(Q\le(9/2)\delta\), the inequalities in (2) cut out a tetrahedron in the \((p,q,r)\)-variables. Its vertices are \((27/8)(\delta-(2/9)Q)\) times the four sign vectors \((1,1,1),(-1,-1,1),(-1,1,-1),(1,-1,-1)\). Its volume is
\[
 \frac83\left(\frac{27}{8}\right)^3\left(\delta-\frac29Q\right)^3.
\]
Since \(Q=2(a^2+ab+b^2)\), the area element in orthonormal coordinates on the trace-free diagonal plane is \(\sqrt3\,da\,db\). Consequently the leading Euclidean five-volume in \((a,b,p,q,r)\) is
\[
 V_\delta\sim\frac83\left(\frac{27}{8}\right)^3
 \frac{\pi}{4(2/9)\sqrt3}\,\delta^4
 =\frac{19683\sqrt3\pi}{512}\,\delta^4.
\tag{3}
\]
This displays the reason for the fourth power: three transverse coordinates have scale \(\delta\), while two have scale \(\sqrt\delta\).

### 4. Surface-measure Jacobian and the two chiralities
The tangent variation of a center is
\[
 \dot u_i=(A+\Omega)v_i-(v_i^{\mathsf T}Av_i)v_i,
\]
where \(\Omega x=\omega\times x\) is a common infinitesimal rotation. Direct summation over the four vertices gives the product-sphere Riemannian metric at the ideal tetrahedron:
\[
 \sum_i\lVert\dot u_i\rVert^2
 =\frac43Q+\frac89(p^2+q^2+r^2)+\frac83\lVert\omega\rVert^2.
\]
In the independent coordinates \((a,b,p,q,r,\omega_1,\omega_2,\omega_3)\), its positive square-root determinant is
\[
 J=\frac{2048}{243}.
\tag{4}
\]
With \(\omega\) parametrizing infinitesimal rotations by their axis-angle vectors, the corresponding invariant volume of \(SO(3)\) equals \(8\pi^2\). There are exactly two disjoint regular-tetrahedron rotation orbits for ordered labels. Dividing by the product surface area \((4\pi)^4\), equations (3) and (4) give
\[
 p(w)\sim \frac{2(8\pi^2)}{(4\pi)^4}\,
 \frac{2048}{243}\,
 \frac{19683\sqrt3\pi}{512}\,\delta^4
 =\frac{81\sqrt3}{4\pi}\,\delta^4.
\]
Finally, \(\delta=\sin(w_0)(w-w_0)+O((w-w_0)^2)\) and \(\sin w_0=2\sqrt2/3\); therefore the coefficient of \((w-w_0)^4\) is \(16\sqrt3/\pi\), as claimed. \(\square\)

## Verification
The included `check.py` constructs facet normals directly from the four perturbed sphere points, checks the independent Jacobian calculation by an eight-dimensional Gram determinant, verifies the predicted first- and second-order facet-distance coefficients, and estimates the rescaled event volume with a fixed-seed scrambled Sobol cubature. The checker uses the actual geometric face planes, not a reimplementation of the asymptotic inequalities as its event test. Its limiting-volume ratios approach one as the cap radius approaches \(w_0\). Finite numerics test the calculation but the argument above is analytic: the near-optimizer localization, Taylor expansion, and dominated convergence establish the infinite limiting statement.

## Relationship to prior work
Finch (2015, arXiv:1502.06931) studies precisely the four-random-cap coverage probability below a hemisphere, gives bounds for considerably larger radii, and explains that an exact complete probability expression is unknown. This finding supplies only the *sharp small-excess asymptotic*, not the missing full distribution. Bürgisser, Cucker and Lotz (2007 preprint; 2010 journal) study general random spherical coverage and its conditioning duality, with exact formulas for cap radii at least a hemisphere and bounds below a hemisphere; their stated formula does not determine this tetrahedral lower endpoint. Milne (2014) gives a derivation of the Grace–Danielsson inequality used to anchor the sharp tetrahedral rigidity. More recent general finite-sample and large-sample coverage literature concerns different regimes. The local anisotropic tetrahedral measure calculation and exact onset coefficient are the distinguishing claims.

## Limitations
The four centers must be independent and surface-uniform, the caps equal, and the ambient sphere \(S^2\). This is a one-sided local asymptotic as \(w\downarrow w_0\); no exact global cumulative distribution, explicit uniform error constant, or extension to arbitrary numbers of caps is claimed. The novelty assessment is based on searched and inspected sources, not a comprehensive historical certificate; equivalent unpublished or unindexed results may exist. There has been no independent mathematical audit.

## References
1. S. R. Finch, *Covering a Sphere with Four Random Circular Caps*, arXiv:1502.06931 (first public version 2015-02-24), https://arxiv.org/abs/1502.06931.
2. P. Bürgisser, F. Cucker and M. Lotz, *Coverage processes on spheres and condition numbers for linear programming*, arXiv:0712.2816 (first public version 2007-12-17), *Annals of Probability* 38 (2010), 570–604, https://arxiv.org/abs/0712.2816.
3. A. Milne, *The Euler and Grace-Danielsson inequalities for nested triangles and tetrahedra*, arXiv:1404.0525 (first public version 2014-04-02), https://arxiv.org/abs/1404.0525.
