# Exact small-distance law on flat cone surfaces and Euclidean orbifold signature recovery

## Finding

Let \(S\) be a compact, connected, boundaryless Euclidean cone surface of total area \(A>0\), with finitely many conical points of total angles \(0<\alpha_j<2\pi\). Let \(X,Y\) be independent area-uniform points and \(F_S(r)=\Pr(d_S(X,Y)\le r)\), where \(d_S\) is **intrinsic geodesic distance**. Define
\[
K(\alpha)=\frac{\alpha}{8}\left[\cot\left(\frac\alpha2\right)+\left(\pi-\frac\alpha2\right)\csc^2\left(\frac\alpha2\right)\right].
\]
Then \(K(\alpha)>0\) for \(0<\alpha<2\pi\), and there is \(r_0(S)>0\) such that the following identity is **exact** for every \(0\le r<r_0(S)\):
\[
\boxed{F_S(r)=\frac{\pi r^2}{A}-\frac{r^4}{A^2}\sum_jK(\alpha_j).}
\]
For a smooth compact flat surface (no conical points), the sum is empty and the same formula holds. In particular, the two-point distance distribution determines both \(A\) and \(\sum_jK(\alpha_j)\).

For a compact **orientable Euclidean 2-orbifold without reflector boundary**, the distribution furthermore determines its entire cone-order signature. The five possible signatures, with \(B=\sum_j K(2\pi/m_j)\), are
\[
\begin{array}{c|c}
\text{signature}&B\\ \hline
\text{torus}&0\\
(2,2,2,2)&\pi^2/4\\
(3,3,3)&\pi(3\sqrt3+8\pi)/36\\
(2,4,4)&\pi(2\pi+1)/8\\
(2,3,6)&\pi(119\pi+30\sqrt3)/432
\end{array}
\]
These constants are strictly increasing in the displayed order. This distinguishes all signatures from only the quadratic and quartic coefficients of a single scalar distance distribution; it does **not** recover a general flat metric within a signature.

## Assumptions and scope

A Euclidean cone surface means a length surface locally isometric to the Euclidean plane away from finitely many points, and around each exceptional point to the metric cone \(C_{\alpha}\) with polar metric \(du^2+u^2d\psi^2\), \(\psi\in\mathbb R/\alpha\mathbb Z\). The surface is compact and has no boundary. All nontrivial cone angles in this theorem are below \(2\pi\). The area measure is the two-dimensional Hausdorff/flat area measure; cone points have measure zero. The random variables are independently sampled with normalized area measure, not by boundary arclength or any ambient Euclidean measure. The radius interval \([0,r_0(S))\) is allowed to depend on the surface.

The orientable orbifold corollary assumes the standard local models \(\mathbb R^2/C_m\), \(m\ge2\), without mirror or corner-reflector strata; at a cone point, \(\alpha=2\pi/m\). A torus is the zero-singularity case. Nonorientable and reflector orbifolds are not covered by the signature classification.

## Proof

**1. A cone-ball deficit.** Fix \(0<\alpha<2\pi\), put \(\phi=\alpha/2\in(0,\pi)\), and work on the infinite cone \(C_\alpha\). Two points at radial distances \(u,v\) whose shorter angular difference is \(\delta\in[-\phi,\phi]\) have squared intrinsic distance \(u^2+v^2-2uv\cos\delta\); this holds because \(|\delta|\le\phi<\pi\). For \(u,v>0\), let \(\beta_r(u,v)\in[0,\pi]\) be the angular radius for which this squared distance is at most \(r^2\): it is \(\pi\) when \(u+v\le r\), \(0\) when \(|u-v|\ge r\), and otherwise \(\arccos((u^2+v^2-r^2)/(2uv))\). Endpoint conventions do not affect integrals.

For an area ball centered at radius \(u\), the cone angular range has length \(2\min(\beta_r,\phi)\), whereas its Euclidean-plane counterpart has length \(2\beta_r\). Therefore
\[
\operatorname{area}_{C_\alpha} B_r(u)-\pi r^2
=-2\int_0^\infty v\,[\beta_r(u,v)-\phi]_+\,dv.
\]
The difference vanishes for sufficiently large \(u/r\): for example it vanishes for \(u/r>\max\{1,1/\sin\phi\}\). Thus its integral over the cone is finite. Fubini and the identity
\[
[\beta_r-\phi]_+=\int_\phi^\pi \mathbf1\{u^2+v^2-2uv\cos\theta<r^2\}\,d\theta
\]
give the total defect
\[
\Delta_\alpha(r):=\int_{C_\alpha}(\operatorname{area}B_r(x)-\pi r^2)\,dx
=-2\alpha r^4\int_\phi^\pi I(\theta)\,d\theta,
\]
where
\[
I(\theta)=\int_0^\infty\!\int_0^\infty uv\,\mathbf1\{u^2+v^2-2uv\cos\theta<1\}\,du\,dv.
\]
With \(v=tu\), the Jacobian and the radial integral yield
\[
I(\theta)=\frac14\int_0^\infty\frac{t\,dt}{(1+t^2-2t\cos\theta)^2}
=\frac{\sin\theta+(\pi-\theta)\cos\theta}{8\sin^3\theta}.
\]
The displayed expression extends continuously to \(\theta=\pi\) with value \(1/24\). An antiderivative gives
\[
\int_\phi^\pi I(\theta)\,d\theta
=\frac1{16}\left[\cot\phi+(\pi-\phi)\csc^2\phi\right].
\]
Consequently \(\Delta_\alpha(r)=-K(\alpha)r^4\). Positivity of \(K\) follows directly from the strictly positive defining double integral (for \(\alpha<2\pi\)), including angles for which \(\cot\phi<0\).

**2. From cones to a compact surface.** Choose pairwise disjoint cone neighborhoods with fixed positive radii around all exceptional points. By compactness and local Euclidean structure on their complement, a sufficiently small intrinsic ball is either Euclidean or is described exactly inside one cone chart. The cone calculation shows that its area differs from \(\pi r^2\) only if its center lies within a constant multiple of \(r\) of a cone point; these influence regions are disjoint for small \(r\). They can be integrated using the corresponding infinite cones without boundary effects or nonlocal shorter paths. For all \(0<r<r_0(S)\), therefore,
\[
\int_S\operatorname{area}(B_r(x))\,dx
=A\pi r^2-r^4\sum_jK(\alpha_j).
\]
Dividing by \(A^2\) proves the asserted probability identity. It also gives
\[
A=\lim_{r\downarrow0}\frac{\pi r^2}{F_S(r)},\qquad
\sum_jK(\alpha_j)=\lim_{r\downarrow0}\frac{A\pi r^2-A^2F_S(r)}{r^4}.
\]
These are exact limits of the measured scalar distribution, not assumptions of knowing the area or angles in advance.

**3. Orbifold signature classification and separation.** On an orientable compact flat 2-orbifold without reflectors, Gauss--Bonnet reads \(2-2g=\sum_j(1-1/m_j)\). With \(m_j\ge2\), either \(g=1\) and there are no cone points, or \(g=0\) and the only possible order multisets are \((2,2,2,2)\), \((3,3,3)\), \((2,4,4)\), and \((2,3,6)\). The latter follows by ordering the three possible orders and solving \(1/m_1+1/m_2+1/m_3=1\); for four points every order must be two. Substituting \(2\pi/m\) into \(K\) gives exactly the table in the Finding.

The differences of successive positive constants (after the torus) are respectively
\[
B_{333}-B_{2222}=\frac{\pi(3\sqrt3-\pi)}{36},\quad
B_{244}-B_{333}=\frac{\pi(2\pi+9-6\sqrt3)}{72},\quad
B_{236}-B_{244}=\frac{\pi(11\pi+30\sqrt3-54)}{432}.
\]
All are positive, using \(\pi<3\sqrt3\), \(\pi>3\) and \(3/2<\sqrt3<2\). Hence the scalar quartic coefficient distinguishes every allowed signature. This completes the proof.

## Verification

The standalone program `verify_flat_cone.py` checks \(K(2\pi/m)\) for \(m=2,3,4,6\) by two numerically independent methods: integrating the angular-gap formula, and directly integrating radial profiles of individual cone metric balls. It also checks several nonorbifold angles, the exact Euclidean two-disk convolution identity for a square pillowcase, and strict separation of the five signature constants. Run `python3 verify_flat_cone.py`; it uses only the Python standard library. Its successful final status is `FLAT_CONE_CHECK_OK angular=7 radial=4 pillowcase_convolutions=3 signatures=5`.

A separate elementary cross-check uses the square pillowcase \((\mathbb R^2/\mathbb Z^2)/\{\pm1\}\), of area \(A=1/2\) and four order-two points. For sufficiently small \(r\) (indeed \(r<1/4\)), a ball in the quotient lifts to the union of two radius-\(r\) disks. The integral of their planar overlap as the relative shift varies is \((\pi r^2)^2\) by convolution. This gives exactly \(F(r)=2\pi r^2-\pi^2r^4\), agreeing with four times \(K(\pi)=\pi^2/16\). Numerical tests are consistency checks, not a proof of the general identity.

## Relationship to prior work

Troyanov's 2007 account gives flat cone surface geometry, angle-curvature conventions, and Gauss--Bonnet; Sağlam's 2016 study provides local cone metrics and triangulation/geodesic context. Charitos--Papadoperakis--Tsapogas (2013) study global geodesics on these metric spaces. None of the inspected available full texts gives the area-averaged small geodesic-ball deficit above, its exact \(K(\alpha)\) coefficient, or reconstruction of Euclidean orbifold cone-order signatures from the two-point distance law.

Borzellino's earlier orbifold geometry work includes Bishop-type ball-volume comparison, which motivates comparison of local and global ball volumes, but the accessible abstract did not establish the explicit integrated flat-cone identity. The older smooth Bertrand--Diguet--Puiseux local curvature expansion also does not supply this finite-angle cone coefficient: for spherical orbifolds of the same Euler characteristic, the values \(B\) in the table differ. The new result is a direct finite-angle calculation and its inverse-geometric consequence, not a claim that defining cone models or Gauss--Bonnet is new.

## Limitations

This requires a compact **boundaryless** Euclidean cone surface with finitely many angles in \((0,2\pi)\). Larger cone angles, mirrors, boundary edges and arbitrary smooth curvature are outside the stated identity. It is local in radius and determines only the summed nonlinear cone-angle statistic on general cone surfaces, not the individual angles or the isometry class. The signature rigidity applies only to the five orientable, reflector-free compact Euclidean 2-orbifold types. Historical priority is not established exhaustively; in particular an earlier orbifold volume-comparison dissertation could not be inspected in full.

## References

1. M. Troyanov, *On the Moduli Space of Singular Euclidean Surfaces*, arXiv:math/0702666, first public version 22 February 2007, https://arxiv.org/abs/math/0702666 ; see sections 1.1 and 1.7 on area, Gauss--Bonnet and local cone geometry.
2. İ. Sağlam, *Complete Flat Cone Metrics on Punctured Surfaces*, arXiv:1602.04240, first public version 6 February 2016, https://arxiv.org/abs/1602.04240 ; see sections 2.1--2.3 on intrinsic length metrics and metric cones.
3. C. Charitos, I. Papadoperakis and G. Tsapogas, *The geometry of Euclidean surfaces with conical singularities*, arXiv:1306.1759, first public version 7 June 2013, https://arxiv.org/abs/1306.1759 ; see introduction and geodesic results.
4. J. E. Borzellino, *Riemannian Geometry of Orbifolds*, University of California, Los Angeles dissertation (1992), abstract/catalogue https://digitalcommons.calpoly.edu/math_fac/111/ ; full text not accessible in this review.
