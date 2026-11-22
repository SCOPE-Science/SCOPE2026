# A fractional short-chord cusp law for the Euclidean astroid

## Finding

Let \(C\) be the unit astroid \(\{(x,y):|x|^{2/3}+|y|^{2/3}=1\}\), endowed with one-dimensional Euclidean arclength. Choose \(X,Y\) independently and uniformly by normalized arclength. Let \(D=\|X-Y\|_2\), and let \(S\) be the shorter **intrinsic arclength** between the two points along \(C\). Write \(B(r,s)=\Gamma(r)\Gamma(s)/\Gamma(r+s)\). Then as \(\varepsilon\downarrow0\),

\[
\boxed{\Pr(D\le\varepsilon)=\frac{\varepsilon}{3}+C_{\rm cusp}\,\varepsilon^{5/3}+o(\varepsilon^{5/3}),\qquad
C_{\rm cusp}=\frac{2^{1/3}}9 B\left(\frac13,\frac32\right)
=0.35332775005709\ldots.}
\]

The fractional term consists of pairs that are closer in ambient Euclidean distance than in intrinsic arclength. More precisely, with \(E_\varepsilon=\{D\le\varepsilon<S\}\),
\[
\Pr(E_\varepsilon)\sim C_{\rm cusp}\,\varepsilon^{5/3}.
\]
On \(E_\varepsilon\), with probability tending to one, the points lie on opposite local branches of one of the four cusps. The cusp label tends to uniform on four choices, and the ordered branch orientation tends to an independent fair bit. Write \(a,b\) for the positive intrinsic arclength depths of \(X,Y\) from this cusp, respectively, and put
\[
 c=(2/3)^{3/2},\quad u_*=3/2^{5/3},\quad U_\varepsilon=a/\varepsilon^{2/3},\quad V_\varepsilon=(b-a)/\varepsilon.
\]
Conditionally on \(E_\varepsilon\), \((U_\varepsilon,V_\varepsilon)\) converges **in total variation** to the uniform area distribution on
\[
 \boxed{\mathcal R=\{(u,v):u>0,\ v^2+4c^2u^3<1\}.}
\]
In particular, the transformed limiting coordinates
\[
 W=(U/u_*)^3,\qquad Z=V/\sqrt{1-W}
\]
are independent, with \(W\sim\operatorname{Beta}(1/3,3/2)\) and \(Z\sim\operatorname{Unif}(-1,1)\). All indicated discrete marks are independent of \((W,Z)\). This joint law is part of the finding, not an inference from a fitted scalar tail.

## Assumptions and scope

The curve is the complete simple closed *unit* astroid, not its filled-in planar region. The sampling measure is normalized Euclidean arclength on that curve; it is not uniform angle, invariant random-line sampling, or area sampling. The two points are independent. The distance \(D\) is an ambient Euclidean straight-line distance; \(S\) is the shortest of the two possible arclength distances along the closed curve. The limit fixes the astroid and sends \(\varepsilon>0\) to zero. Changing the astroid scale by \(A>0\) replaces \(\varepsilon\) by \(\varepsilon/A\). The zero-probability events of sampling a cusp itself or ties in shortest arclength may be ignored.

## Proof

**1. Exact arclength coordinates and leading intrinsic term.** In the first quadrant the parameterization \((\cos^3t,\sin^3t)\), \(0\le t\le\pi/2\), has speed \(3\sin t\cos t\). Measured from \((1,0)\), arclength is \(s=(3/2)\sin^2t\), giving the *exact* unit-speed quadrant chart
\[
 \gamma(s)=\left(f(s),c s^{3/2}\right),\quad f(s)=(1-2s/3)^{3/2},\quad c=(2/3)^{3/2},\quad 0\le s\le3/2.
\]
The four congruent quadrants each have length \(3/2\), so total length is \(L=6\). For two independent uniform arclength points on any length-\(L\) closed loop, the shorter circular arclength \(S\) has \(\Pr(S\le\varepsilon)=2\varepsilon/L=\varepsilon/3\), exactly for \(0<\varepsilon<L/2\). Always \(D\le S\), so the displayed probability splits *exactly* as
\[
 \Pr(D\le\varepsilon)=\varepsilon/3+\Pr(D\le\varepsilon<S).
\]

**2. Non-cusp corrections are smaller.** The Euclidean astroid is a simple compact curve, and two points with small Euclidean separation must either be close in arclength within one smooth quadrant or lie near the common cusp of two adjacent quadrants. On a single quadrant the unit tangent rotates monotonically through a total angle \(\pi/2\). Write \(\theta(s)\) for the **nondecreasing absolute turning angle**, namely the negative of the usual oriented tangent-angle argument up to an additive constant. For two points with arclength difference \(h\), Euclidean separation is at least \(h\cos(\Delta\theta/2)\), where \(\Delta\theta\in[0,\pi/2]\) is the tangent-angle increment. Thus \(D\le\varepsilon\) forces \(h\le\sqrt2\varepsilon\). For those pairs having additionally \(h>\varepsilon\),
\[
 h-\varepsilon\le h-D\le h\bigl(1-\cos(\Delta\theta/2)\bigr)
 \le C\varepsilon\,[\theta(s+\sqrt2\varepsilon)-\theta(s)]^2,
\]
with the tangent angle extended constantly beyond quadrant endpoints. Since \(\theta\) is monotone with total variation \(\pi/2\), writing \(Q(s)=\theta(s+\sqrt2\varepsilon)-\theta(s)\) gives
\[
 \int Q(s)^2ds\le(\pi/2)\int Q(s)ds\le(\pi/2)^2\sqrt2\varepsilon.
\]
For fixed first arclength \(s\), the admissible positive differences \(h>\varepsilon\) therefore occupy length at most \(C\varepsilon Q(s)^2\). Integrating over the first point, then accounting for both orders, proves that all same-quadrant excess pairs have unnormalized product-arclength measure \(O(\varepsilon^2)\). Pairs from nonadjacent quadrants or away from common cusp neighborhoods are uniformly separated, by compactness and injectivity. Hence the leading excess of order \(\varepsilon^{5/3}\) must come from opposite branches at one cusp.

**3. Opposite-branch geometry.** At \((1,0)\), coordinates on the two adjacent branches at depths \(a,b\ge0\) are \((f(a),c a^{3/2})\) and \((f(b),-c b^{3/2})\). Their squared distance is **exactly**
\[
 d(a,b)^2=[f(a)-f(b)]^2+c^2(a^{3/2}+b^{3/2})^2.
\]
The condition \(d(a,b)\le\varepsilon\) forces \(a,b=O(\varepsilon^{2/3})\) from the second term, and \(|b-a|=O(\varepsilon)\) because \(f'(s)=-\sqrt{1-2s/3}\) stays uniformly away from zero near \(0\). Substitute \(a=\varepsilon^{2/3}u\), \(b=a+\varepsilon v\), whose Jacobian is \(\varepsilon^{5/3}\). On every compact set of the rescaled variables, the exact identity and \(f'(0)=-1\) yield
\[
 \frac{d(a,b)^2}{\varepsilon^2}\longrightarrow v^2+4c^2u^3.
\]
The preceding bounds confine all rescaled admissible \((u,v)\) to one fixed bounded rectangle, and the boundary of \(\mathcal R\) has zero Lebesgue measure. Dominated convergence therefore gives the **entire** opposite-branch area, for one ordered orientation, as
\[
 \iint\mathbf1_{\{d(a,b)\le\varepsilon\}}\,da\,db
 = I\,\varepsilon^{5/3}+o(\varepsilon^{5/3}),\qquad
 I=\int_0^{u_*}2\sqrt{1-4c^2u^3}\,du.
\]
Here \(4c^2u_*^3=1\), so with \(w=(u/u_*)^3\),
\[
 I=\frac{2u_*}{3}B(1/3,3/2)=2^{-2/3}B(1/3,3/2).
\]
There are four congruent cusps and two ordered choices for which adjacent branch contains \(X\), giving eight equal contributions. In each, the intrinsic-nearby subregion \(a+b\le\varepsilon\) has area at most \(\varepsilon^2/2\), hence negligible compared with \(\varepsilon^{5/3}\). Dividing the eight contributions by \(L^2=36\), and combining with step 2, proves
\[
 \Pr(E_\varepsilon)\sim\frac{8I}{36}\varepsilon^{5/3}
 =\frac{2^{1/3}}9 B(1/3,3/2)\varepsilon^{5/3}.
\]

**4. Marked conditional law and independence.** Insert an arbitrary bounded measurable test function of \((u,v)\) into the rescaled integrals of step 3. The indicator functions of the exact regions converge in \(L^1(du\,dv)\) to \(\mathbf1_{\mathcal R}\) by dominated convergence on their common bounded support. After normalization by the positive area \(I\), the densities converge in \(L^1\), which is total variation convergence. Same-quadrant contributions vanish conditionally because \(O(\varepsilon^2)/\varepsilon^{5/3}\to0\). The eight geometrically congruent cusp-orientation contributions yield independent uniform discrete labels. In the limiting region the \(u\)-marginal has density \(2\sqrt{1-(u/u_*)^3}/I\); substitution \(W=(u/u_*)^3\) gives precisely \(\operatorname{Beta}(1/3,3/2)\). Given \(W\), the variable \(V\) is uniform between \(\pm\sqrt{1-W}\). Thus \(Z=V/\sqrt{1-W}\) is independent uniform on \((-1,1)\). Total variation convergence of the transformed marks follows by contraction under measurable maps, after ignoring null boundary sets.

## Verification

The companion `verify.py` reconstructs the *finite-radius* cross-branch geometry from the exact arclength parameterization; it does not substitute the limiting parabolic region into the numerical test. It independently minimizes squared distance in the second branch, finds the two exact threshold roots by bisection, and integrates the resulting interval widths by composite Simpson quadrature. It checks the symbolic beta normalization, the limiting independent-mark moments, and monotone convergence of four finite-radius normalized coefficients to the predicted constant. Run `python3 verify.py` using only the Python standard library. Its successful final line is `ALL_CHECKS_PASSED`. The accompanying numerical calculations check consistency at selected radii; the infinite-dimensional limit and asymptotic equivalences are proved by the localization and dominated-convergence arguments above, not by extrapolating numerical samples.

## Relationship to prior work

The geometric model and the sampling law matter. Bäsel (2012, full HTML inspected, Sections 1 and 4) derives Euclidean distances of two **interior-area-uniform points** in a regular polygon, using the *invariant random-line* chord distribution. The present points instead lie on the **arclength boundary of a cusped nonconvex curve**, and the theorem concerns its fractional *near-zero* Euclidean pair-distance correction and marked cusp localization. These results do not imply one another. Gille (2005) derives invariant-line chord distributions for a wedge and quadratic rod, not independent arclength endpoints. García-Pelayo (2015) studies affine-invariant random-line chords of convex and concave polygons, not cusp-to-cusp point-pair distance on a smooth-quadrant astroid. Only the latter two sources' abstracts and bibliographic material were examined, so no assertion about their complete contents is made. Historical priority remains provisional.

Related published arclength-boundary ellipse results analyze **near-diameter** chord tails of a smooth convex curve. Their opposite extreme and smooth-curvature hypotheses do not cover the short-distance excess of the semicubical cusp considered here. Similarly, published smooth-curve chord-midpoint boundary-layer laws concern distance of the chord **midpoint to a boundary** and require positive curvature, rather than the distance of the two endpoints from each other. The elementary beta-function evaluation, classical astroid parameterization, and intrinsic short-arc baseline are not claimed as novel. The mathematical difference is the fractional \(5/3\) correction arising from two tangent branches with local separation of order \(s^{3/2}\), along with its full conditional marked geometry.

## Limitations

The result is for the fixed unit four-cusped astroid and independent arclength samples only; it does not claim a uniform law for a family of rounded astroids or all singular plane curves. The \(o(\varepsilon^{5/3})\) is not furnished with an explicit effective error constant or a further asymptotic term. The conditional law applies to the excess event \(D\le\varepsilon<S\), not to all short chords, whose leading population consists of neighboring arclength points. An unindexed equivalent cusp-correlation theorem could affect historical originality; independent mathematical assessment has not been carried out.

## References

1. W. Gille, *Analysis of the Chord Length Distribution Along an Edge: The Wedge Case and the Quadratic Rod Case*, Journal of Mathematics and Statistics **1** (2005), 106–112, first published 2005-06-30. DOI: 10.3844/jmssp.2005.106.112. https://doi.org/10.3844/jmssp.2005.106.112
2. U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707v1, first posted 2012-04-12; full HTML v2 inspected. https://arxiv.org/html/1204.2707v2
3. R. A. García-Pelayo Novo, *Computation of the multi-chord distribution of convex and concave polygons*, Applied Mathematical Sciences **9** (2015), 4669–4708. DOI: 10.12988/ams.2015.54364. https://oa.upm.es/44786/
4. *Astroid*, MacTutor History of Mathematics (classical parameterization, four cusps and perimeter). https://mathshistory.st-andrews.ac.uk/Curves/Astroid/
