# Affine isotropic ordering for two rotated regular polygons and a three-rotation majorization obstruction

## Finding
Fix an integer \(n\ge3\) and a centered regular \(n\)-gon \(P_n\) with inradius one. Put \(\alpha=2\pi/n\). For any integer \(k\ge2\), consider phase gaps \(g_i\ge0\) satisfying \(\sum_{i=1}^k g_i=\alpha\), and rotate copies of \(P_n\) through phases \(0,g_1,g_1+g_2,\ldots,g_1+\cdots+g_{k-1}\). Define their intersection \(K(g)\), and let \(X_g\) be uniform by area in \(K(g)\). The affine isotropic invariant is
\[
I_n(g)=\frac{\det\operatorname{Cov}(X_g)}{\operatorname{area}(K(g))^2}.
\]
Write \(S_1(g)=\sum_i\tan(g_i/2)\) and \(S_3(g)=\sum_i\tan^3(g_i/2)\). Its exact profile is
\[
\boxed{I_n(g)=\frac{(3S_1(g)+S_3(g))^2}{144n^2S_1(g)^4}.}\tag{1}
\]

**Two rotations: complete strict ordering.** If \(k=2\), write \(g=(\theta,\alpha-\theta)\), with \(0\le\theta\le\alpha/2\). Then
\[
\boxed{I_n(g)=\frac1{16n^2}\left[\cot\frac\alpha2+\frac13\left(\tan\frac\theta2+\tan\frac{\alpha-\theta}2\right)\right]^2,}\tag{2}
\]
which is strictly decreasing in \(\theta\) on the whole open interval \((0,\alpha/2)\). The largest value is that of the regular \(n\)-gon, attained only when both copies coincide modulo their \(n\)-fold symmetry; the smallest value is that of the regular \(2n\)-gon, attained only at a half-step relative rotation.

**Three rotations: the majorization obstruction.** For every fixed \(n\ge3\), let
\[
 g_\varepsilon=(\alpha-2\varepsilon,3\varepsilon/2,\varepsilon/2),\qquad
 h_\varepsilon=(\alpha-2\varepsilon,\varepsilon,\varepsilon).
\]
For all sufficiently small positive \(\varepsilon\), both are genuine positive three-gap lists, and \(g_\varepsilon\) strictly majorizes \(h_\varepsilon\). Nevertheless
\[
\boxed{I_n(g_\varepsilon)-I_n(h_\varepsilon)
=-\frac{\tan^2(\pi/n)+3}{576n^2\tan(\pi/n)}\,\varepsilon^3
+O_n(\varepsilon^4)<0.}\tag{3}
\]
Hence the natural strict Schur-convex continuation of (2) fails for every regular polygon order already at three rotations. The same obstruction extends to any fixed \(k>3\) when coincident rotations (zero gaps) are allowed, and by continuity to nearby all-positive \(k\)-gap vectors. No general majorization order in the opposite direction is asserted.

## Assumptions and scope
All Euclidean geometry is planar. A phase is understood modulo \(\alpha=2\pi/n\), the rotational period of the starting polygon. The prescribed gaps are a cyclic partition of that period. The intersection contains the unit disk and is full-dimensional, also when some phases coincide. The covariance is taken about the mean of the uniform-area probability measure, not about an arbitrarily chosen point. The squared affine isotropic constant is defined here explicitly as the positive fourth-power quantity \(I_n\), and its invariance under invertible affine coordinate changes follows from the determinant transformation rules for covariance and area. In (3) the smallness threshold may depend on fixed \(n\); there is no claim of a uniform threshold over all polygon orders. Majorization is standard descending-partial-sum majorization for vectors with the same total sum. Strict majorization means majorization without permutation equivalence. The \(O_n\) remainder is valid with \(n\) fixed and real \(\varepsilon\downarrow0\).

## Proof
**1. The circular normal fan and its area moment.** Since each copy of \(P_n\) is the intersection of half-planes \(x\cdot u\le1\) at its side normals, the union of all side-normal sets consists of \(n\) repeated copies of the cyclic gap pattern \(g\). For a polar ray through angle \(\phi\), the active tangent line is the one whose normal is closest in angular distance. In the fan between two consecutive distinct normals separated by a gap \(g_i\), the boundary radius is \(\rho(\phi)=\sec t\) on either half-fan, where \(t\in[0,g_i/2]\). This remains valid in the limit of a zero gap. Every gap is at most \(2\pi/3\), so no tangent singularity occurs. Hence the exact area \(A\) and the polar second moment \(J=\int_{K(g)}\|x\|^2\,dx\) are
\[
\begin{aligned}
A&=n\sum_i\int_0^{g_i/2}\sec^2 t\,dt=nS_1,\\
J&=\frac n2\sum_i\int_0^{g_i/2}\sec^4 t\,dt
=\frac n2\left(S_1+\frac{S_3}{3}\right).
\end{aligned}\tag{4}
\]
Here \(\int\sec^4t\,dt=\tan t+\tan^3t/3\). The factor \(1/2\) in \(J\) comes from the polar radial integration \(\int_0^\rho r^3dr=\rho^4/4\) and two symmetrical half-fans.

**2. Covariance normalization.** The body is invariant under rotation by \(2\pi/n\), with \(n\ge3\), so its centroid is zero and its symmetric covariance matrix commutes with a planar rotation other than a half-turn. Such a symmetric matrix must be a scalar multiple of the identity. Its trace equals \(J/A\); therefore \(\operatorname{Cov}(X_g)=J/(2A)\,\mathrm{Id}\). Consequently \(I_n(g)=J^2/(4A^4)\), and substituting (4) proves (1), with every factor retained.

**3. All two-rotation phases.** Put \(a=\tan(\theta/2)\), \(b=\tan((\alpha-\theta)/2)\), \(S=a+b\). Their angles add to \(\alpha/2\), so the tangent addition rule gives \(ab=1-S/\tan(\alpha/2)\). Since \(a^3+b^3=S^3-3abS\), the positive square root of (1), multiplied by \(4n\), reduces to
\[
\frac{3S+a^3+b^3}{3S^2}=\cot(\alpha/2)+S/3.
\]
This proves (2). The derivative of \(S\) with respect to \(\theta\) equals \(\tfrac12(\sec^2(\theta/2)-\sec^2((\alpha-\theta)/2))\), which is strictly negative for \(0\le\theta<\alpha/2\), because all arguments are nonnegative and the second is larger. The bracket in (2) is positive, so \(I_n\) decreases strictly. At \(\theta=0\) the intersection is \(P_n\); at \(\theta=\alpha/2\) its normal rays form a regular \(2n\)-gon. The endpoint values are exactly
\[
I_n(0,\alpha)=\frac{(\cot(\pi/n)+\tan(\pi/n)/3)^2}{16n^2},\quad
I_n(\alpha/2,\alpha/2)=\frac{(\cot(\pi/(2n))+\tan(\pi/(2n))/3)^2}{64n^2}.
\tag{5}
\]

**4. The genuinely three-rotation sign reversal.** Set \(T=\tan(\alpha/2)>0\), and for fixed \(q\in[0,1/2]\) and small \(\varepsilon>0\) put
\[
g(q,\varepsilon)=(\alpha-2\varepsilon,(1+q)\varepsilon,(1-q)\varepsilon).
\]
Write \(F(g)=(3S_1(g)+S_3(g))/(3S_1(g)^2)\), so \(I_n(g)=F(g)^2/(16n^2)\). Elementary Taylor expansion at \(\varepsilon=0\), using \(\tan(\alpha/2-\varepsilon)=(T-\tan\varepsilon)/(1+T\tan\varepsilon)\), yields
\[
\begin{aligned}
F(g(q,\varepsilon))={}&\frac{T^2+3}{3T}-\frac{T^2}{3}\varepsilon
+\frac{T(T^2+1)}3\varepsilon^2\\
&-\frac{6T^4+8T^2-3+3q^2}{18}\varepsilon^3
+O_n(\varepsilon^4).\tag{6}
\end{aligned}
\]
The remainder is uniform over \(q\in[0,1/2]\) for fixed \(n\): the tangent functions and the nonzero denominator \(S_1\) are analytic in a neighborhood of the compact parameter set. To check the decisive coefficient without suppressing a cancellation, the \(q^2\varepsilon^3\) contribution to \(S_1\) is \(q^2\varepsilon^3/4\), while that to \(S_3\) is \(3q^2\varepsilon^3/4\). At \(\varepsilon=0\), \(S_1=T\) and \(S_3=T^3\), and \(\partial F/\partial S_1=-1/T^2-2/3\), \(\partial F/\partial S_3=1/(3T^2)\). Their combined contribution to \(F\) is therefore \(-q^2\varepsilon^3/6\), as in (6).

For \(q=1/2\) versus \(q=0\), equation (6) gives \(F(g(1/2,\varepsilon))-F(g(0,\varepsilon))=-\varepsilon^3/24+O_n(\varepsilon^4)\). Squaring, using the positive common leading value \(F_0=(T^2+3)/(3T)\), gives
\[
I_n(g(1/2,\varepsilon))-I_n(g(0,\varepsilon))
=-\frac{F_0}{192n^2}\varepsilon^3+O_n(\varepsilon^4),
\]
which is precisely (3). For all sufficiently small \(\varepsilon>0\), the first coordinate \(\alpha-2\varepsilon\) is greater than either small coordinate. The first descending partial sums of the two vectors coincide, while the sum of their two largest coordinates is larger by \(\varepsilon/2\) for \(g_\varepsilon\). Thus \(g_\varepsilon\) strictly majorizes \(h_\varepsilon\), and the strict negative sign proves the claimed obstruction. This is a continuous-parameter proof; finite numerical checks do not establish it.

## Verification
Run the enclosed `check_geometry.py` with Python 3 using only the standard library. The checker separately constructs the intersection polygon from its half-planes by clipping, computes area and raw second moments by shoelace/edge-integral formulas, and checks the analytic area, moment and isotropic profiles. It tests six polygon orders, two, three and four rotations, and eleven distinct positive gap samples for each order and rotation count. It then checks eleven angles for the strict two-rotation profile for each order, and checks the three-rotation counter-order and cubic coefficient at three small parameters per order. The reproducible execution returned `PASS 1140 independent numerical geometry and algebraic-profile checks`. The quantified theorem is proved analytically in Steps 1–4, not extrapolated from samples. The code includes only standard-library dependencies and fixed deterministic test inputs.

## Relationship to prior work
The tangent-half-gap area formula is elementary and known. The published result *Radial-distance laws classify tangential polygons up to cyclic ordering* gives a complete radial-distance distribution for arbitrary tangential polygons, from which the moments in (4) are recoverable. Thus (1) is a convenient specialization and normalization and is **not** claimed as an independently new moment identity. The published result *Independent Gumbel and Gaussian errors for randomly rotated regular polygons* also employs the same exact circular-gap area sum, but optimizes asymptotic random area and Hausdorff fluctuations rather than normalized inertia.

The closest result on the **same deterministic polygon family** is *Strict angular-gap majorization of Mahler products for rotational polygon intersections* (2026-11-01). It proves that the Mahler product is strictly Schur-**concave** in all the rotation gaps. Its product uses the sum of tangents and the sum of sines, not the covariance moment \(S_3\) divided by the fourth power of area. The present structural claim is different: the isotropic invariant is strictly Schur-convex on the two-gap simplex, yet a specific balancing operation reverses the expected Schur-convex inequality on the three-gap simplex. The previous Mahler theorem does not imply either signed isotropic comparison: distinct affine invariants have no known identity transforming one into the other here.

Kweon and Zhu, *Maximum Overlap Area of Several Convex Polygons Under Translations* (first public 2023-07-01), study translations to maximize intersection **area**, not the normalized covariance of concentric regular-polygon intersections as functions of angular gaps. O'Rourke and Zaimi (2015) classify the **number of edges** of intersections of rotating regular polygons, a combinatorial observable. A published exact rotational area law for regular polygons of unequal orders also concerns area rather than inertia and assumes unequal polygon orders; those assertions do not determine (2) or (3).

## Limitations
The strong comparison (2) requires two copies of one regular polygon at a common center and common inradius. At three copies, (3) is a rigorous local counterexample to a proposed global majorization property, not a full characterization of all triples, not a statement that the isotropic invariant is Schur-concave, and not an optimization result over arbitrary convex bodies. The all-gap identity (1) follows from known moment geometry, while the claimed additional content is the sharp two-copy ordering and the three-copy failure mechanism. Exact older equivalent analyses in unindexed geometric-inertia literature cannot be ruled out. No independent scientific audit has been performed.

## References
1. H. J. Kweon and H. Zhu, *Maximum Overlap Area of Several Convex Polygons Under Translations*, arXiv:2307.00409v1, first public 2023-07-01. https://arxiv.org/abs/2307.00409
2. *Strict angular-gap majorization of Mahler products for rotational polygon intersections*, published mathematical result (2026-11-01), https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-strict-angular-gap-majorization-of-mahler-products-for-rotationa--073641383518/RESULT.md
3. *Radial-distance laws classify tangential polygons up to cyclic ordering*, published mathematical result (2026-11-01), https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-radial-distance-laws-classify-tangential-polygons-up-to-cyclic-o--682fa94d6003/RESULT.md
4. *Independent Gumbel and Gaussian errors for randomly rotated regular polygons*, published mathematical result (2026-10-25), https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-independent-gumbel-and-gaussian-errors-for-randomly-rotated-regu--ed3ca8970379/RESULT.md
5. J. O'Rourke and G. Zaimi, *Intersection of rotating regular polygons*, MathOverflow question and answer (2015-10-17). https://mathoverflow.net/questions/221120/intersection-of-rotating-regular-polygons
6. *Universal convex-gap rigidity and the exact rotational overlap law of unequal regular tangential polygons*, published mathematical result (2026-10-18), https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-universal-convex-gap-rigidity-and-the-exact-rotational-overlap-l--ed975dc47a69/RESULT.md
