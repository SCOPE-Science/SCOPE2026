# Sharp central-plane section extrema of the Steinmetz bicylinder

## Finding

Let \(K_R=\{(x,y,z)\in\mathbb R^3:x^2+z^2\le R^2,\ y^2+z^2\le R^2\}\), the intersection of two perpendicular radius-\(R\) circular cylinders, with \(R>0\). For a unit normal \(n\), put \(A_R(n)=\operatorname{area}(K_R\cap n^\perp)\), using Euclidean area in the section plane. Then the **sharp global range** is

\[
\boxed{\pi R^2\le A_R(n)\le\pi\sqrt2\,R^2.}
\]

The lower bound is attained **exactly** for normals along the two cylinder axes, \(n=\pm e_x\) and \(n=\pm e_y\). The upper bound is attained **exactly** for \(n=(\pm1,\pm1,0)/\sqrt2\). Thus the maximum/minimum central-section area ratio is precisely \(\sqrt2\), with all equality cases classified.

In fact the area is elementary for every plane. For a unit normal, set \(a=|n_x|\), \(b=|n_y|\), \(c=|n_z|\), and use the symmetry \(a\ge b\ge0\). Whenever \(a,b,c>0\),

\[
\boxed{\frac{A_R(n)}{R^2}=
\frac{(a+b)\arctan((a+b)/c)-(a-b)\arctan((a-b)/c)}{ab}.}
\]

The formula extends by continuity to the coordinate boundaries. In particular, at \(c=0\), \(A_R(n)/R^2=\pi/a\); at \(b=0<a\), \(A_R(n)/R^2=\frac2a[\arctan(a/c)+ac/(a^2+c^2)]\) for \(c>0\); and at \(a=b=0\), \(A_R(n)=4R^2\).

For every prescribed value of \(c=|n_z|<1\), the largest area among normals with that value of \(c\) is attained exactly when \(a=b\). Writing those normals proportionally to \((1,1,k)\), \(k\ge0\), their normalized section-area profile is

\[
\boxed{D(k)=2\sqrt{k^2+2}\arctan(2/k),\qquad D(0)=\pi\sqrt2,\quad D(+\infty)=4.}
\]

It decreases to one strict minimum and then increases: that minimum occurs at the unique \(k_*>0\) satisfying

\[
k_*(k_*^2+4)\arctan(2/k_*)=2(k_*^2+2).
\]

Numerically, \(k_*=1.320136713376677\ldots\) and \(D(k_*)=3.8203968413887655\ldots\). These decimals are descriptive, not used in the proof.

## Assumptions and scope

All sections are two-dimensional **central** sections by planes through the center of the *solid* (not its boundary surface). The two generating cylinders are infinite, congruent, perpendicular and share their center. Uniform radius scaling is exactly quadratic; it suffices to prove the assertions for \(R=1\). No claims are made for unequal radii, nonorthogonal cylinder axes, or affine-offset cutting planes.

## Proof

**1. Exact formula.** Scale to \(R=1\), and use the coordinate symmetries to assume \(a\ge b\ge0\), \(c\ge0\), \(a^2+b^2+c^2=1\). At height \(z\), the bicylinder has the square slice \([-r,r]^2\), where \(r=\sqrt{1-z^2}\). In the central cutting plane \(ax+by+cz=0\), the horizontal line intersects that square in a segment of length \(L(z)\). With \(p=\sqrt{a^2+b^2}\) and \(q=c|z|\), elementary clipping of two intervals gives, for \(a>b>0\),

\[
L(z)=\begin{cases}
2pr/a,&q\le r(a-b),\\
p\bigl(r(a+b)-q\bigr)/(ab),&r(a-b)<q<r(a+b),\\
0,&q\ge r(a+b).
\end{cases}
\]

The plane's area element is \(p^{-1}L(z)\,dz\): the vector in the plane corresponding to a unit vertical displacement has length \(1/p\) and is orthogonal to the horizontal chord. Therefore

\[
A_1(n)=\frac1p\int_{-1}^1 L(z)\,dz.
\]

The thresholds are \(z_\pm=(a\pm b)/\sqrt{c^2+(a\pm b)^2}\). Split the integral at \(z_-\) and \(z_+\), and use

\[
\int_0^t\sqrt{1-z^2}\,dz=\frac12(t\sqrt{1-t^2}+\arcsin t),\qquad
\arcsin z_\pm=\arctan((a\pm b)/c).
\]

The algebraic boundary contributions cancel, leaving the boxed elementary formula. Continuous limits give all boundary cases; direct sections yield the values at coordinate axes.

**2. Balancing the horizontal components.** For fixed \(0\le c<1\) put \(s=a^2+b^2=1-c^2\) and \(h_c(v)=\sqrt v\arctan(\sqrt v/c)\) for \(c>0\). Since \(v_\pm=(a\pm b)^2=s\pm2ab\), the exact formula rewrites as

\[
A_1(n)=4\cdot\frac{1}{v_+-v_-}\int_{v_-}^{v_+}h_c'(v)\,dv.
\]

Now

\[
h_c'(v)=\frac12\int_0^{1/c}\frac{dt}{1+vt^2}+\frac{c}{2(c^2+v)}.
\]

Each integrand is convex in \(v\ge0\), and the first integral is strictly convex. Consequently the average of \(h_c'\) over an interval centered at fixed \(s\) is strictly increasing with the interval radius \(2ab\). (For a differentiable convex function, the derivative of the centered interval mean with respect to its radius is nonnegative; it is positive for strictly convex functions.) Because \(ab\le s/2\), the unique maximizer at fixed \(c\) has \(a=b=\sqrt{s/2}\). For \(c=0\), the same argument applies with \(h_0'(v)=\pi/(4\sqrt v)\), strictly convex and integrable at zero. This proves the fixed-vertical-normal balancing claim, including strictness.

**3. Global maximum and one valley in the diagonal profile.** Substituting \(a=b=1/\sqrt{k^2+2}\), \(c=k/\sqrt{k^2+2}\) into the exact formula yields \(D(k)\). For \(k>0\), differentiation gives

\[
D'(k)=\frac{2g(k)}{\sqrt{k^2+2}(k^2+4)},\quad
g(k)=k(k^2+4)\arctan(2/k)-2(k^2+2).
\]

The derivative of \(g\) is

\[
g'(k)=(3k^2+4)\arctan(2/k)-6k>0.
\]

Indeed, for every \(x>0\), the elementary strict inequality \(\arctan x>3x/(x^2+3)\) follows by differentiating the difference: its derivative is \(4x^4/((1+x^2)(x^2+3)^2)>0\), and it vanishes at \(x=0\). Apply it at \(x=2/k\). Since \(g(0+)=-4\) and \(g(+\infty)=4/3\), \(g\) has exactly one zero. Hence \(D\) decreases and then increases, so its global supremum equals the greater endpoint value, \(\max\{\pi\sqrt2,4\}=\pi\sqrt2\), attained only at \(k=0\). Combined with Step 2, this proves the upper bound and equality classification.

**4. Global minimum.** The Euclidean unit ball lies inside \(K_1\) because \(x^2+z^2\le x^2+y^2+z^2\) and \(y^2+z^2\le x^2+y^2+z^2\). Every central section consequently contains a unit disk, so \(A_1(n)\ge\pi\). For the planes \(x=0\) and \(y=0\), the sections are exactly unit disks and equality holds. Conversely, if a central plane is neither of these coordinate planes, it contains directions with both \(x\ne0\) and \(y\ne0\). Along any such direction, the boundary radius of \(K_1\) is strictly greater than one, since \(\max(x^2,y^2)+z^2<1\) on the unit sphere. By continuity an open angular interval extends beyond the contained unit disk, implying strictly larger area. Scaling by \(R^2\) completes the proof. \(\square\)

## Verification

The reproducibility script `verify.py` uses an independently parametrized orthonormal basis of each section plane and integrates the radial area formula

\[
A_1(n)=\frac12\int_0^{2\pi}\frac{d\theta}{\max\{d_x(\theta)^2+d_z(\theta)^2,\ d_y(\theta)^2+d_z(\theta)^2\}}.
\]

It tests 154 deterministic normals, including exact boundary and near-degenerate configurations, against the closed formula, verifies the theoretical bounds at those instances, and locates the sole diagonal-profile stationary point using bisection. The observed maximum absolute quadrature discrepancy was \(1.5701\times10^{-7}\), versus the explicit check tolerance \(1.4\times10^{-5}\). The universal proof rests on the analytic arguments above, not on finite sampling or numerical root finding. Run `python3 verify.py` with the Python standard library.

## Relationship to prior work

The bicylinder's classical volume \(16R^3/3\) and surface area \(16R^2\) are well documented (for example, the cited Wolfram MathWorld treatment and Paul Bourke's historical geometric account). Dirksen's 2016 study proves maximal-section results for products of a Euclidean ball and a cube; the body studied here is instead the *intersection of two perpendicular circular cylinders*. Its area formula, exact globally sharp central-section bounds and four maximizing normals do not follow from those product-body results. The exact convexity-of-interval-means reduction is essential: assessing only the diagonal orientations would not establish a global optimum over all cutting planes. The 2015 Alsina–Nelsen solid-geometry volume includes both sections and bicylinders among its topics, but its relevant pages were not available for a decisive priority comparison.

## Limitations

The result concerns central planes of congruent perpendicular cylinders, not affine sections, unequal radii, or more than two cylinders. The same geometric argument has not been claimed to extend to those families. Searches and accessible primary texts did not reveal the identical extremal theorem; this is not a proof of historical novelty. In particular, inaccessible historical treatments of bicylinder sections could contain a comparable formula. The result has not received independent scientific validation.

## References

1. H. Dirksen, *Hyperplane Sections of Cylinders*, arXiv:1602.07854v1, first submitted 25 February 2016. https://arxiv.org/html/1602.07854v1
2. E. W. Weisstein, *Steinmetz Solid*, MathWorld. https://mathworld.wolfram.com/SteinmetzSolid.html
3. P. Bourke, *Intersecting Cylinders*, December 2003 (month recorded, exact public day not established). https://paulbourke.net/geometry/cylinders/
4. C. Alsina and R. B. Nelsen, *A Mathematical Space Odyssey: Solid Geometry in the 21st Century*, Mathematical Association of America, 2015 (limited preview, not a full-text novelty exclusion).
