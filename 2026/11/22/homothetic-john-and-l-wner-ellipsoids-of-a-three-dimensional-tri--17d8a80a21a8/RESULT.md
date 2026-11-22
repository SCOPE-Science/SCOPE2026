# Homothetic John and Löwner ellipsoids of a three-dimensional trigonometric orbitope

## Finding

Let
\[
K=\operatorname{conv}\{(\cos t,\sin t,\cos(2t)):0\le t\le2\pi\}\subset\mathbb R^3.
\]
The **unique, unrestricted** maximum-volume inscribed ellipsoid and minimum-volume containing ellipsoid are, respectively,
\[
E_{\mathrm J}=\left\{(x,y,z):\frac{x^2+y^2}{3/8}+\frac{z^2}{3/4}\le1\right\},\qquad
E_{\mathrm L}=\left\{(x,y,z):\frac{x^2+y^2}{3/2}+\frac{z^2}{3}\le1\right\}.
\]
In particular \(E_{\mathrm L}=2E_{\mathrm J}\), with dilation about their common origin. Their contact sets are each exactly four points, forming regular tetrahedra after transforming the corresponding ellipsoid into a unit Euclidean ball. The three volumes and the sharp affine ellipsoidal containment factor are
\[
\operatorname{vol}(K)=\pi,\quad
\operatorname{vol}(E_{\mathrm J})=\frac{\pi\sqrt3}{4},\quad
\operatorname{vol}(E_{\mathrm L})=2\pi\sqrt3,\quad
\inf_{E\subset K\subset\rho E}\rho=2,
\]
where the infimum ranges over **all** nondegenerate Euclidean ellipsoids \(E\), arbitrary centers, orientations and semiaxes, and \(\rho E\) means the homothety of \(E\) by \(\rho\) about its own center. The ratio of outer to inner ellipsoid volumes is exactly \(8\).

## Assumptions and scope

All ellipsoids are closed, nondegenerate and three-dimensional. Volume is ordinary three-dimensional Lebesgue measure. The support curve runs through one full period; the coordinate normalization is part of the theorem. No symmetry or centering is imposed on competitors. The body has nonempty interior; the known representation
\[
K=\{(x,y,z):2x^2-1\le z\le1-2y^2\}
\tag{1}
\]
is the left-hand quadratic-cylinder orbitope of Sanyal--Sottile--Sturmfels [1, Sec. 5, Figure 3]. In particular, the inequalities in (1) already imply \(x^2+y^2\le1\). This description is **prior work**, not a new assertion of priority.

## Proof

**Step 1 (exact solid and volume).** The convex-hull identity (1) is proved in [1]. An independent direct argument uses a random point \((X,Y)\) on the unit circle with means \(x,y\): \(z=2\mathbb E(X^2)-1\) ranges between \(2x^2-1\) and \(1-2y^2\). The lower endpoint is attained by measures supported at the two circle points with fixed first coordinate \(x\), and the upper endpoint by measures with fixed second coordinate \(y\); both are feasible whenever \(x^2+y^2\le1\). Their mixtures achieve every intermediate value while preserving both means. Hence (1). The vertical fiber over \((x,y)\) in the unit disk has length \(2(1-x^2-y^2)\), giving
\[
\operatorname{vol}(K)=\int_0^{2\pi}\int_0^1 2(1-r^2)r\,dr\,d\phi=\pi.
\]

**Step 2 (inscribed ellipsoid containment).** For a point of \(E_{\mathrm J}\),
\[
x^2\le\frac38-\frac{z^2}{2},\qquad y^2\le\frac38-\frac{z^2}{2}.
\]
Consequently, the exact nonnegative square identities give
\[
1+z-2x^2\ge(z+\tfrac12)^2\ge0,\qquad
1-z-2y^2\ge(z-\tfrac12)^2\ge0.
\]
Thus \(E_{\mathrm J}\subseteq K\). The equality/contact points are exactly
\[
(\pm\tfrac12,0,-\tfrac12),\qquad(0,\pm\tfrac12,\tfrac12).
\tag{2}
\]

**Step 3 (global John optimality, including translated/rotated ellipsoids).** Apply the diagonal map \(T_{\mathrm J}(x,y,z)=(x/\sqrt{3/8},y/\sqrt{3/8},z/\sqrt{3/4})\). The four points in (2) become
\[
(\pm\sqrt{2/3},0,-1/\sqrt3),\qquad(0,\pm\sqrt{2/3},1/\sqrt3).
\]
Write these unit vectors as \(u_i\), for \(i=1,\ldots,4\). Direct multiplication gives
\[
\sum_{i=1}^4u_i=0,\qquad\frac34\sum_{i=1}^4u_iu_i^{\mathsf T}=I_3,
\qquad u_i\cdot u_j=-\frac13\ (i\ne j).
\tag{3}
\]
All four are boundary contacts of \(T_{\mathrm J}K\) with the unit ball. The nonsymmetric version of John's contact theorem [2, Thm. 2] proves that this ball is the **unique** largest-volume ellipsoid inside \(T_{\mathrm J}K\); mapping back proves the first formula, globally.

**Step 4 (outer ellipsoid containment).** For every generating point \(\gamma(t)=(\cos t,\sin t,\cos2t)\),
\[
\frac{\cos^2t+\sin^2t}{3/2}+\frac{\cos^2(2t)}3
=\frac23+\frac13\cos^2(2t)\le1.
\]
Since the candidate outer ellipsoid is convex, \(K\subseteq E_{\mathrm L}\). Equality holds exactly at the four curve points
\[
(\pm1,0,1),\qquad(0,\pm1,-1).
\tag{4}
\]
The diagonal normalization \(T_{\mathrm L}(x,y,z)=(x/\sqrt{3/2},y/\sqrt{3/2},z/\sqrt3)\) takes (4) to
\[
(\pm\sqrt{2/3},0,1/\sqrt3),\qquad(0,\pm\sqrt{2/3},-1/\sqrt3).
\]
These four unit contact vectors again obey the two isotropic identities (3). The standard dual Löwner contact criterion [3, Sec. 2] therefore certifies the **unique** minimum-volume covering ellipsoid among all ellipsoids, irrespective of center or orientation.

**Step 5 (homothety and sharpness).** The two diagonal semiaxis-square triples are \((3/8,3/8,3/4)\) and \((3/2,3/2,3)\); the latter is four times the former, proving the exact factor-two homothety. The ellipsoid volume formula gives the two asserted volumes. If any ellipsoid \(E\) satisfies \(E\subseteq K\subseteq\rho E\), extremality implies
\[
\frac{\operatorname{vol}(E_{\mathrm L})}{\operatorname{vol}(E_{\mathrm J})}
\le \frac{\rho^3\operatorname{vol}(E)}{\operatorname{vol}(E_{\mathrm J})}
\le\rho^3.
\]
Since the left side is \(8\), necessarily \(\rho\ge2\); the displayed ellipsoids attain equality. This also proves the claimed sharp affine containment factor.

## Verification

The accompanying `verify.py` uses only Python's standard library. Run `python verify.py`. It replays exact rational square-completion identities at \(401\) rational heights for each inequality, the complete four-point affine isotropic moments and pairwise Gram matrices for both contact families, exact scaling identities, and \(10{,}001\) numerical generating-curve containment checks. The infinite assertions rest on the displayed symbolic inequalities and published contact criteria, **not** on finite samples. The volume integral and exact two-sided factor follow symbolically in the proof.

## Relationship to prior work

Sanyal, Sottile and Sturmfels [1, Section 5 and Figure 3] give the precise same trigonometric curve and already identify its hull as the intersection of the two parabolic cylinders. Therefore the body's description, its general orbitope setting and the availability of semidefinite methods are prior work. Gruber and Schuster [2] prove the general unrestricted John contact characterization, and standard duality yields the Löwner form [3]. What is determined here is the **specific pair of extremal ellipsoids**, the two distinct regular-tetrahedron contact quadruples, their unexpected exact homothety, and the resulting sharp factor-two ellipsoidal containment of this particular body. The inspected sections of [1] do not provide those optimization outputs, while [2] and [3] supply criteria, not the body's contact coordinates. published-finding corpus searches for the curve and its equivalent quadratic-cylinder representation found related but different convex bodies; these do not give the two exact ellipsoids here. The originality conclusion remains provisional pending broader historical review.

## Limitations

The result is particular to this three-coordinate projection of the first two Fourier harmonics; it does not assert the same homothetic property for all trigonometric orbitopes or for deformed generating curves. Historical-priority searches, even with a directly matching primary body source, cannot prove uniqueness in the literature. No independent audit has been performed.

## References

[1] R. Sanyal, F. Sottile and B. Sturmfels, *Orbitopes*, arXiv:0911.5436, first submitted 2009-11-28, Sec. 5, Corollary 5.3 and Figure 3. https://arxiv.org/abs/0911.5436 ; open manuscript https://franksottile.github.io/research/pdf/Orbitope.pdf .

[2] P. M. Gruber and F. E. Schuster, *An Arithmetic Proof of John's Ellipsoid Theorem*, arXiv:1207.7246, first submitted 2012-07-31, Theorem 2. https://arxiv.org/abs/1207.7246 .

[3] M. Henk, *Löwner--John Ellipsoids*, in *Optimization Stories*, Documenta Mathematica Extra Volume ISMP, 2012, pp. 95--106. https://doi.org/10.4171/DMS/6/15 .
