# A three-contact screening principle and the sharp minimum-disk transition of catenary arches

## Finding
Let \(a>0\) and let \(f:[-a,a]\to\mathbb R\) be even and continuously differentiable, with \(f(0)=0\) and \(f'(t)>0\) for \(0<t\le a\). Suppose
\[
H_f(t)=f(t)+\frac{t}{f'(t)}
\]
is nondecreasing on \((0,a]\). Then the unique smallest Euclidean disk containing the *entire continuous curve* \(\Gamma_{f,a}=\{(t,f(t)):-a\le t\le a\}\) is already the smallest enclosing disk of the three distinguished points \((0,0)\) and \((\pm a,f(a))\). Thus any finite sample containing these three points has exactly the same smallest enclosing disk as the continuous curve.

Writing \(d=f(a)>0\), the disk has center \((0,z)\), radius \(R\), and exact formula
\[
(z,R)=\begin{cases}
(d,a),&d\le a,\\
\left(\dfrac{a^2+d^2}{2d},\dfrac{a^2+d^2}{2d}\right),&d>a.
\end{cases}
\]
If \(H_f\) is strictly increasing, the only touching curve points are the two endpoints when \(d<a\), and the two endpoints plus the midpoint when \(d\ge a\).

In particular, for the natural hanging-chain catenary arch \(\Gamma_a=\{(t,\cosh t):|t|\le a\}\), there is a *unique* positive \(a_0\) satisfying
\[
\cosh a_0-1=a_0,\qquad a_0=1.61613751377431\ldots.
\]
Its minimum enclosing radius \(R(a)\) equals \(a\) for \(0<a\le a_0\), while for \(a>a_0\), with \(d(a)=\cosh a-1\),
\[
R(a)=\frac{a^2+d(a)^2}{2d(a)}.
\]
The disk has exactly two contacts below \(a_0\), and three at and above it. Its radius is continuously differentiable but not twice differentiable at the transition, with sharp positive onset
\[
R(a)-a=\frac{(\sinh a_0-1)^2}{2a_0}(a-a_0)^2+o((a-a_0)^2)
\quad(a\downarrow a_0\text{ from above}).
\]
The coefficient is \(0.62161467161233\ldots\), and the right-minus-left second derivative is twice this coefficient.

This screening condition has a sharp power-arch boundary: for \(f(t)=|t|^q\), \(1<q\le2\), it holds at every positive span; for every \(q>2\), at span \(a=1\) the three-point disk fails to contain the curve. This last assertion is a counterexample to extending the screening conclusion to arbitrary symmetric convex arches without a shape hypothesis.

## Assumptions and scope
All disks are **closed Euclidean** disks. The entire continuous graph is considered, not merely a polygonal sampling. The general screening theorem assumes only even \(C^1\) regularity and the displayed monotonicity on the positive half-interval, not global convexity of the graph beyond the stated positive derivative. The catenary normalization has generating scale one; translating its height or uniformly scaling both coordinates translates or scales the disk correspondingly. The power-arch boundary uses \(q>1\), so \(|t|^q\) is \(C^1\) at the origin.

## Proof
**1. Restriction to axis centers.** Because the compact curve is invariant under \((x,y)\mapsto(-x,y)\), the center of its unique smallest enclosing disk lies on the vertical axis. Existence follows by compactness and coercivity of the maximal-distance function. If two distinct radius-minimizing centers existed, their midpoint would enclose all curve points in a disk of strictly smaller squared radius by the parallelogram identity. Reflection therefore forces the unique center to have first coordinate zero.

**2. Endpoint screening.** The normal to the graph at \(t,f(t)\) intersects the vertical axis at height \(H_f(t)\), so the hypothesis has the geometric meaning that these normal-axis intercept heights do not decrease as one travels outward. For an arbitrary axis center \((0,z)\) and \(t\in(0,a]\), define
\[
F_z(t)=t^2+(f(t)-z)^2.
\]
Differentiation gives the exact identity
\[
F_z'(t)=2f'(t)\bigl(H_f(t)-z\bigr).
\]
Since \(f'(t)>0\) and \(H_f\) is nondecreasing, the derivative can change sign only from negative to positive, never from positive to negative. Thus \(F_z\) achieves its maximum on \([0,a]\) at \(0\) or \(a\), for every real \(z\). By evenness the same holds on the negative half. If \(H_f\) is strictly increasing, every interior point has strictly smaller squared distance than the maximum at the two endpoint types; an interior local minimum may occur but not a maximum. Consequently the curve and the distinguished three-point set have identical axis-center enclosing-radius functions; axis symmetry and uniqueness give identical global minimum disks.

**3. Optimization of the three points.** Set \(d=f(a)\). The squared radius for the axis center \((0,z)\) is
\[
\Phi(z)=\max\{z^2,\ a^2+(d-z)^2\}.
\]
Two endpoints are distance \(2a\) apart, so every disk has radius at least \(a\). If \(d\le a\), choose \(z=d\); its radius is exactly \(a\) and it contains the midpoint. If \(d>a\), the unique minimizer of \(\Phi\) is the positive crossing \(z=(a^2+d^2)/(2d)\in(0,d)\), at which the midpoint and both endpoints are equidistant, giving \(R=z\). Any smaller \(z\) has larger endpoint distance, and any larger \(z\) has larger midpoint distance; hence the minimum is global and unique. The strict screening observation gives the asserted contact counts, including three contacts at \(d=a\).

**4. Catenary verification.** Translate \(y=\cosh t\) down by one, so \(f(t)=\cosh t-1\). Then \(f'(t)=\sinh t>0\) and
\[
H_f(t)=\cosh t-1+\frac{t}{\sinh t}.
\]
The derivative has the sign of
\[
B(t)=\sinh^3t+\sinh t-t\cosh t.
\]
Here \(B(0)=0\), while
\[
B'(t)=\sinh t\bigl(3\sinh t\cosh t-t\bigr)>0
\]
for every \(t>0\), because \(\sinh t\cosh t>t\). Thus \(H_f\) is strictly increasing for every positive span. The function \(g(a)=\cosh a-1-a\) is negative for sufficiently small positive \(a\), strictly convex, and tends to \(+\infty\), so it has exactly one positive root \(a_0\). Applying Step 3 gives the piecewise formula and contacts. (For the unshifted catenary, increase the stated center height by one.)

**5. Sharp transition.** On the three-contact branch, the exact identity
\[
R(a)-a=\frac{(d(a)-a)^2}{2d(a)}
\]
holds, while the difference is zero on the two-contact branch. Since \(d(a_0)=a_0\) and \(d'(a_0)=\sinh a_0>1\), Taylor expansion proves the displayed positive quadratic onset and hence continuity of the first derivative and a jump of \((\sinh a_0-1)^2/a_0\) in the second derivative.

**6. A sharp boundary of the screening class.** For \(f(t)=|t|^q\) and \(1<q\le2\),
\[
H_f(t)=t^q+\frac1q t^{2-q},
\]
which increases strictly for all \(t>0\). Conversely, if \(q>2\) and \(a=1\), the three marked points are \((\pm1,1),(0,0)\), whose smallest enclosing disk is the unit disk centered at \((0,1)\). At any sufficiently small \(t>0\), its squared distance to \((t,t^q)\) is
\[
t^2+(1-t^q)^2=1+t^2-2t^q+t^{2q}>1.
\]
Therefore that three-point disk does not enclose the full arch. This establishes an exact quadratic-contact boundary for this natural power family without asserting that monotonicity is necessary for all other families.

## Verification
The accompanying standalone standard-library Python program `check.py` evaluates the actual analytic centers and radii. It passed 150,015 dense deterministic point-containment checks over 15 catenary spans, together with 20 power-arch span/exponent checks, the high-precision transition-root comparison and quartic boundary failures. These finite diagnostics do not prove the quantified statements; Steps 1–6 provide the infinite proof. Reproduce with `python3 check.py` (no external packages required).

## Relationship to prior work
The catenary parametrization is classical; Ebisu and Machigashira (first arXiv availability July 25, 2012) study discrete catenary approximations for minimal-surface construction, not minimum Euclidean covering disks. Welzl's and Skyum's finite-point minimum-disk algorithms supply the general computational context; they do not identify a three-point *exact support set for every point of a continuous transcendental arch*, nor this contact threshold. The result is consistent with but not implied by maximum-chord/diameter information, since a smallest enclosing disk need not be determined by a diametral pair. The claim of historical novelty remains provisional, as exhaustive older arc-coverage literature has not been established.

## Limitations
The screening condition is sufficient, not claimed necessary, and does not cover all convex graphs. The catenary theorem is for symmetric finite arches and their convex hulls, not asymmetric cutoffs, different metrics or general hanging chains with spatially varying weight. The coefficient is an asymptotic in the half-span of the arch, not a probabilistic limit. Numerical checks sample finitely many points; complete containment rests on the derivative proof. No independent mathematical review or historical-priority certification has been carried out.

## References
1. A. Ebisu and Y. Machigashira, *An approximation of a catenoid constructed from piecewise truncated conical minimal surfaces*, arXiv:1207.5920, first submitted 2012-07-25, https://arxiv.org/abs/1207.5920.
2. E. Welzl, *Smallest enclosing disks (balls and ellipsoids)*, LNCS 555 (1991), 359–370, https://doi.org/10.1007/BFB0038202.
3. S. Skyum, *A simple algorithm for computing the smallest enclosing circle*, Information Processing Letters 37 (1991), 121–125, https://doi.org/10.1016/0020-0190(91)90030-L.
