# A sharp Löwner-contact transition for Euclidean balls clipped by coaxial cylinders

## Finding

Consider the Euclidean ball intersected with a coaxial circular cylinder:
\[
K_{d,s}=\{(z,y)\in\mathbb R\times\mathbb R^{d-1}:z^2+\|y\|^2\le1,\ \|y\|\le s\},\qquad d\ge3,\ 0<s\le1.
\]
Its unique **unrestricted** minimum-volume enclosing (Löwner) ellipsoid has a sharp transition at
\[s_* = \sqrt{\frac{d-1}{d}}.\]
For \(0<s<s_*\) the ellipsoid is
\[
E_{d,s}=\left\{(z,y):\frac{z^2}{d(1-s^2)}+\frac{(d-1)\|y\|^2}{ds^2}\le1}\right\};
\]
for \(s_*\le s\le1\) it is the unit ball. Denoting the volume of the unit \(d\)-ball by \(\kappa_d\), the normalized enclosing volume is exactly
\[
F_d(s)=\frac{\operatorname{vol}_d(E_{d,s})}{\kappa_d}=
\begin{cases}
\dfrac{d^{d/2}s^{d-1}\sqrt{1-s^2}}{(d-1)^{(d-1)/2}},&0<s<s_*,\\[4pt]
1,&s_*\le s\le1.
\end{cases}
\]
At the threshold, \(F_d\) is \(C^1\) but not \(C^2\), and
\[
F_d''(s_*^-)-F_d''(s_*^+)=-2d^2.
\]
For \(s<s_*\), exactly the two rim spheres \(z=\pm\sqrt{1-s^2},\ \|y\|=s\) touch the ellipsoid; at and above the threshold all the spherical cap points \(z^2+\|y\|^2=1,\ |z|\ge\sqrt{1-s^2}\) touch the round ball. This is also the enclosing-ellipsoid law for the convex hull of the two opposite unit-sphere caps.

## Assumptions and scope

The integer dimension \(d\ge3\) is fixed. The cylinder has transverse radius \(s\in(0,1]\) and is coaxial with the first coordinate of the unit Euclidean ball. Enclosing ellipsoids are allowed to be arbitrarily oriented and translated. The body is full-dimensional when \(s>0\). The degenerate limit \(s=0\) is excluded, and no probability measure is assumed.

## Proof

**1. Symmetry reduces the unrestricted problem.** The minimum-volume enclosing ellipsoid of a full-dimensional compact convex body exists and is unique (the classical Löwner theorem). Reflection in \(z\) and all orthogonal transformations of the \(y\)-coordinates preserve \(K_{d,s}\). Hence uniqueness forces its center to be the origin and its equation to be \(xz^2+u\|y\|^2\le1\) with \(x,u>0\). This conclusion is about *all* ellipsoids, not a prior restriction to symmetric candidates.

**2. Exact containment constraints.** Put \(c=\sqrt{1-s^2}\). On \(|z|\le c\), the maximal permissible \(\|y\|\) is \(s\); on \(c\le|z|\le1\), it is \(\sqrt{1-z^2}\). On each of these two ranges, the maximum of \(xz^2+u\|y\|^2\), at fixed \(z^2\), is affine in \(z^2\). Its maximum is therefore attained at either \(|z|=c\) or \(|z|=1\). Thus \(K_{d,s}\subset E\) holds **if and only if**
\[x\le1,\qquad c^2x+s^2u\le1.\]

**3. Optimization.** The ellipsoid volume is \(\kappa_d x^{-1/2}u^{-(d-1)/2}\). Minimizing volume is equivalent to maximizing the strictly concave function \(\log x+(d-1)\log u\) on the two linear constraints. Since increasing \(u\) improves the objective, its optimum satisfies \(u=(1-c^2x)/s^2\). Without \(x\le1\), differentiation yields uniquely
\[x_0=\frac1{dc^2},\qquad u_0=\frac{d-1}{ds^2}.\]
If \(c^2>1/d\), this optimum is feasible and gives the displayed spheroid. If \(c^2\le1/d\), the constrained optimum is at \(x=1\), giving \(u=1\). The equality case agrees on both branches.

**4. Global contact and isotropic certificate.** If \(s<s_*\), equality in the radial support bound holds precisely on the two rim spheres. Under the ellipsoid's affine normalization their points become
\[\left(\pm\frac1{\sqrt d},\ \sqrt{\frac{d-1}d}\,\omega\right),\qquad \omega\in S^{d-2}.\]
Choose the two signs equally often and \(\omega\) uniformly. The mean is zero and the second-moment matrix is \(I_d/d\), the classical isotropic Löwner contact certificate. For \(s\ge s_*\), the same normalized contact latitudes belong to the spherical caps of \(K_{d,s}\); thus they certify the unit ball. Because every cap point lies on its boundary, the whole pair of caps is its contact set. This also independently checks the global minimality and the stated contact sets.

**5. Sharp differentiability.** The positive semiaxes in the nonround regime are \(\sqrt d\,c\) and \(\sqrt{d/(d-1)}s\) (multiplicity \(d-1\)), giving \(F_d\). For the nonround branch,
\[\frac{d}{ds}\log F_d(s)=\frac{d-1}s-\frac{s}{1-s^2},\qquad \frac{d^2}{ds^2}\log F_d(s)=-\frac{d-1}{s^2}-\frac{1+s^2}{(1-s^2)^2}.\]
At \(s_*\), \(F_d=1\) and the first logarithmic derivative vanishes; the second is \(-2d^2\). The round branch is the constant one. This proves the asserted exact second-derivative jump and completes the proof.

## Verification

A standalone checker `CHECK.py` independently maximizes the reduced log-determinant objective on a dense positive grid for several dimensions and parameters, checks the seam/tip containment inequalities, the predicted transition, and the normalized isotropic contact moments. The checker samples a finite grid and therefore does not replace the analytic proof above. The volume and regularity formulas follow by direct differentiation without empirical inference.

## Relationship to prior work

Todd (1982) proved minimum-volume ellipsoid formulas for one- and two-sided *linear-hyperplane cuts* of an ellipsoid. The present body is instead intersected with a **round cylinder of transverse dimension \(d-1\ge2\)**, not a slab; the Todd formulas cannot be substituted without changing the feasible body. General uniqueness and contact-certificate principles are classical and not claimed as new. Related published calculations for intersections of two unbounded orthogonal cylinders and for balls intersected with mutually orthogonal slabs concern different constraint classes. The claimed contribution is the complete formula and sharp contact/differentiability transition for the ball--coaxial-cylinder family, not the general Löwner method.

## Limitations

The theorem concerns the Euclidean unit ball with a *coaxial round* cylinder; it does not classify oblique, elliptic-cylinder, or general quadratic intersections. It excludes the lower-dimensional case \(d=2\), where a cylinder constraint is a linear slab and existing one/two-sided cut results apply. Historical priority may be affected by specialized convex-optimization references not retrieved in the present comparison. Independent external mathematical validation has not been performed.

## References

- M. J. Todd, *On Minimum Volume Ellipsoids Containing Part of a Given Ellipsoid*, Mathematics of Operations Research 7(2), 253--261 (1982), DOI: 10.1287/moor.7.2.253. Earliest verified publication May 1, 1982; primary historical MSC 52A40. Full accessible author-uploaded text: https://www.researchgate.net/publication/242929698_On_Minimum_Volume_Ellipsoids_Containing_Part_of_a_Given_Ellipsoid .
- Classical Löwner uniqueness/isotropic contact criterion, as used in the general enclosing-ellipsoid literature; the specialized cylindrical calculation and threshold are established directly above.
