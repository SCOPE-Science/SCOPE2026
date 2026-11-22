# Sharp two-moment tomography of three-dimensional equal-ball lens boundaries

## Finding

For every \(R>0\) and \(0\le a<1\), set
\[
L(R,a)=\{x\in\mathbb R^3:\|x-Rae_1\|_2\le R,\ \|x+Rae_1\|_2\le R\}.
\]
Let \(X,Y\) be independent and uniform with respect to normalized **Euclidean surface area on the entire boundary** \(\partial L(R,a)\). Define the ambient Euclidean chord length \(D=\|X-Y\|_2\), its even moments \(\mu=\mathbb E D^2\), \(\nu=\mathbb E D^4\), and \(\kappa=\nu/\mu^2\). Then
\[
\boxed{\mu=2R^2(1-a),\quad \nu=\frac43R^4(1-a)^2(4+a^2),\quad \kappa=\frac{4+a^2}{3}.}
\]
Consequently the complete feasible two-moment region is
\[
\boxed{\mu>0,\qquad \frac43\mu^2\le\nu<\frac53\mu^2.}
\]
Every feasible moment pair identifies **exactly one** such equal-ball lens up to Euclidean congruence, with explicit inverse
\[
\boxed{a=\sqrt{\frac{3\nu}{\mu^2}-4},\qquad R=\sqrt{\frac{\mu}{2(1-a)}}.}
\]
The lower ratio endpoint occurs only for a ball (\(a=0\)); the upper endpoint is not attained by any nondegenerate lens (\(a\uparrow1\) is a collapsed limit). For any two lenses with ratio observations \(\kappa_1,\kappa_2\), the normalized half-center separations obey
\[
\boxed{|a_1-a_2|\le\sqrt3\,|\kappa_1-\kappa_2|^{1/2}.}
\]
The constant \(\sqrt3\) is sharp and the exponent \(1/2\) cannot be improved in any uniform global bound. One even chord moment alone does not identify the two-parameter geometry.

This feasible moment region is exactly the region already found for uniformly sampled **single spherical-surface caps** (a distinct family); thus, without knowing which family generated the observations, two even chord moments cannot distinguish a lens boundary from a cap surface. This cross-family ambiguity does not contradict uniqueness within each family.

## Assumptions and scope

The ambient space is \(\mathbb R^3\). Generating balls have equal radius \(R>0\); their centers are separated by \(2Ra\), with \(0\le a<1\). The boundary is made of two spherical patches meeting along a circle of zero surface measure. The case \(a=0\) is a full sphere, with patches understood as a partition into opposite hemispheres. Samples are independent and uniform on the **full lens boundary** by area, not sampled from lens volume, a single cap, isotropic random lines, or intrinsic geodesic distance. The collapsed \(a=1\) configuration has no positive-area boundary and is excluded. Moments are exact expectations, not finite-sample estimates. Their values are invariant under common rigid motions.

## Proof

**1. Exact geometric surface law.** For \(a>0\), a point on the sphere centered at \(Ra e_1\) belongs to the lens boundary precisely if its first coordinate is nonpositive; equivalently, its spherical axial coordinate relative to this center is at most \(-a\). Reflection gives two equal-area spherical caps, each of area \(2\pi R^2(1-a)\). A boundary-area-uniform point therefore has the following exact representation, with independent \(\varepsilon\) uniform on \(\{-1,+1\}\), \(Z\) uniform on \([a,1]\), and \(\Phi\) uniform on \([0,2\pi)\):
\[
X=R\bigl(\varepsilon(Z-a),\sqrt{1-Z^2}\cos\Phi,\sqrt{1-Z^2}\sin\Phi\bigr).
\]
The same representation at \(a=0\) partitions the full spherical boundary into two equal hemispheres. Thus \(\mathbb E X=0\), and all mixed coordinate second moments vanish.

**2. Surface radial and covariance moments.** The unit-radius squared norm is
\[
\frac{\|X\|_2^2}{R^2}=(Z-a)^2+(1-Z^2)=1+a^2-2aZ.
\]
Integrating the polynomial density of the uniform \(Z\) yields
\[
\mathbb E\|X\|_2^2=R^2(1-a),\qquad
\mathbb E\|X\|_2^4=\frac{R^4(1-a)^2(3+a^2)}3.
\]
The covariance matrix is diagonal, with axial and transverse entries
\[
A=\frac{R^2(1-a)^2}3,\qquad
T=\frac{R^2(1-a)(2+a)}6,
\qquad\operatorname{Cov}(X)=\operatorname{diag}(A,T,T).
\]
In particular, \(\operatorname{tr}(\operatorname{Cov}(X)^2)=A^2+2T^2\).

**3. Independent-pair distance identity.** For independent centered identically distributed random vectors with finite fourth moments, expansion of \(\|X-Y\|_2^2=\|X\|_2^2+\|Y\|_2^2-2X\cdot Y\) gives
\[
\mathbb E\|X-Y\|_2^2=2\mathbb E\|X\|_2^2,
\]
\[
\mathbb E\|X-Y\|_2^4
=2\mathbb E\|X\|_2^4+2(\mathbb E\|X\|_2^2)^2
+4\operatorname{tr}(\operatorname{Cov}(X)^2).
\]
The mixed odd terms vanish by independence and centering; the squared inner product term is \(\mathbb E(X\cdot Y)^2=\operatorname{tr}(\operatorname{Cov}(X)^2)\). Substituting Step 2 proves the stated \(\mu\) and \(\nu\) identities exactly, not just asymptotically.

**4. Complete inverse and sharp stability.** Dividing the fourth moment by the square of the second gives \(\kappa=(4+a^2)/3\), which is a continuous strictly increasing bijection from \([0,1)\) onto \([4/3,5/3)\). For each \(\mu>0\) and \(\kappa\) in this interval, the displayed inversion provides a unique \(a\in[0,1)\) and \(R>0\), proving both necessity and sufficiency for all possible pairs. Varying \(a\) while adjusting \(R\) to keep \(\mu\) fixed proves one-moment nonidentifiability. Finally, for any \(a,b\ge0\),
\[
|\kappa(a)-\kappa(b)|=\frac{|a^2-b^2|}{3}
=\frac{|a-b|(a+b)}3\ge\frac{|a-b|^2}{3}.
\]
This proves the global stability bound. Equality holds whenever one separation is zero. For \(a\downarrow0\) and comparison with the sphere, \(\kappa(a)-\kappa(0)=a^2/3\) exactly, proving both sharpness and optimality of the exponent: no larger exponent can control a linearly changing separation from a quadratic moment-ratio change.

**5. Comparison to a single cap.** An independently published result for a spherical-surface cap establishes exactly the same feasible moment region. Since the lens result realizes every pair in that region, each pair has a cap realization as well as a lens realization. They are not congruent surfaces when \(a>0\): the lens boundary is made of two spherical patches with distinct centers, while the cap lies on one sphere. The complete-sphere endpoint is shared. This establishes the cross-family ambiguity as a direct consequence, without claiming the published single-cap result as new.

## Verification

The standalone `verify.py` (Python 3 with `sympy` and `numpy`) symbolically integrates the surface axial coordinate, confirms the exact radial moments and covariance eigenvalues, independently reconstructs the independent-pair chord moments, and checks all cancellations. It also independently samples both spherical patches by actual surface area at five nondegenerate/limiting configurations and checks 10 Monte Carlo moment estimates against analytic formulas. Run `python3 verify.py`; success prints `PASS: 17 symbolic identities / Monte Carlo comparisons; five independent parameter pairs`. Finite random checks are only diagnostics; the algebraic and integral argument in Steps 1–4 proves the full parameter range.

## Relationship to prior work

Drach and Tatarko (arXiv:2303.02294v1, 2023) study three-dimensional \(\lambda\)-convex lenses (intersections of congruent balls) and prove their extremal volume properties at fixed surface area. Their exact lens geometry supplies the natural object, but their results do not give the independent boundary-point chord moments or inverse identification.

A prior published mathematical result, *Two even Euclidean chord moments identify spherical caps, with optimal inverse exponents* (2026, identifier `589d8e6fc2c0`), covers points uniform on **one** spherical cap. Its full explicit formula has normalized ratio \(\frac43(1+((z+1)/(z+3))^2)\), a different parameter law. It establishes the same feasible wedge and therefore the cross-family ambiguity, but does not address the entire boundary of a two-ball intersection, including pairings between different supporting spheres.

*Sharp covariance anisotropy law for symmetric Euclidean ball lenses* (2026, identifier `dbb6d001c487`) samples points uniformly by **three-dimensional volume**, and thus its covariance identities do not apply to boundary-area sampling. *Two even chord moments identify spherical lunes, with sharp square-root angle stability* (2026, identifier `bdea9ec9027d`) concerns one connected patch of a single sphere, with a different feasible range. These full published claims were compared for logical implication rather than just names. The possibility of an unindexed classical boundary-lens moment calculation remains a priority uncertainty.

## Limitations

The conclusion is a deterministic exact-moment theorem within the equal-radius, three-dimensional lens family. It does not extend automatically to unequal generating balls, interior uniform sampling, higher-dimensional lenses, noisy observations or unrestricted convex bodies. The radius inverse is ill-conditioned as \(a\uparrow1\); no uniform stability for recovered \(R\) or statistical estimator is claimed. The sharp square-root bound controls normalized center separation, not physical distance without a scale estimate. The result does **not** identify the family of the source surface if caps and lens boundaries are both permitted. Originality is a literature comparison, not an independent certification.

## References

1. K. Drach and K. Tatarko, *Reverse isoperimetric problems under curvature constraints*, arXiv:2303.02294v1, first publicly posted 2023-03-04. https://arxiv.org/abs/2303.02294
2. *Two even Euclidean chord moments identify spherical caps, with optimal inverse exponents*, published mathematical record (2026), identifier `589d8e6fc2c0`. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-two-even-euclidean-chord-moments-identify-spherical-caps-with-op--589d8e6fc2c0
3. *Sharp covariance anisotropy law for symmetric Euclidean ball lenses*, published mathematical record (2026), identifier `dbb6d001c487`. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-covariance-anisotropy-law-for-symmetric-euclidean-ball-len--dbb6d001c487
4. *Two even chord moments identify spherical lunes, with sharp square-root angle stability*, published mathematical record (2026), identifier `bdea9ec9027d`. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-two-even-chord-moments-identify-spherical-lunes-with-sharp-squar--bdea9ec9027d
