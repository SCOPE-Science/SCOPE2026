# A cotangent-moment law and marked near-pole facets of random hemispherical polygons

## Finding

Fix an integer \(n\ge3\). Independently sample \(X_1,\ldots,X_n\) in the open northern unit hemisphere, each with azimuth \(\Phi_i\) uniform on \([0,2\pi)\) and independent colatitude \(R_i\in(0,\pi/2)\) of density \(g\). Assume \(\int_0^{\pi/2}g(r)\,dr=1\) and
\[
m=\int_0^{\pi/2}g(r)\cot r\,dr\in(0,\infty).
\]
Let \(N\) be the north pole and \(K_n\) the shortest-geodesic convex hull. On the event \(I_n=\{N\in\operatorname{int}K_n\}\) define \(D_n=d_{\mathbb S^2}(N,\partial K_n)\). Then
\[
\Pr(I_n)=1-\frac{n}{2^{n-1}},\qquad
\boxed{\lim_{\varepsilon\downarrow0}\frac{\Pr(I_n,\,D_n<\varepsilon)}{\varepsilon}
=\frac{n(n-1)}{2^{n-2}\pi}\,m.}
\]
In particular, uniform spherical-area sampling has \(g(r)=\sin r\) and \(m=1\). Independent uniform sampling under orthogonal projection to the equatorial disk has \(g(r)=2\sin r\cos r\), \(m=\pi/2\). Their leading small-clearance coefficients differ by exactly \(\pi/2\) for every fixed \(n\), and any two admissible axially symmetric densities having equal \(m\) give the same leading coefficient.

There is a joint conditional configuration law, rather than only a scalar asymptotic. On \(I_n\), almost surely the boundary edge nearest \(N\) has one unordered endpoint-label pair \(\{J_1,J_2\}\), with \(J_1<J_2\). Condition on \(I_n\cap\{D_n<\varepsilon\}\). As \(\varepsilon\downarrow0\), the ordered label pair becomes uniform on all \(\binom n2\) choices; its ordered endpoint colatitudes converge jointly in total variation to density
\[
\boxed{w(r,s)=\frac{g(r)g(s)(\cot r+\cot s)}{2m}},\qquad 0<r,s<\pi/2.
\]
Independently of these labels and colatitudes, the first endpoint azimuth tends to a uniform \([0,2\pi)\) mark, the sign of the near-antipodal angular deviation is a fair independent sign, and the rescaled pole clearance \(D_n/\varepsilon\) tends in total variation to \(\operatorname{Uniform}[0,1]\). The remaining \(n-2\) vertices are asymptotically independent with original colatitude density \(g\) and azimuth uniform on the *pole-side semicircle* specified by the sign. More explicitly, put \(\delta=\operatorname{wrap}(\Phi_{J_2}-\Phi_{J_1}-\pi)\in(-\pi,\pi]\). For \(\delta>0\), the remaining relative azimuths \(\operatorname{wrap}_{[0,2\pi)}(\Phi_k-\Phi_{J_1})\) are uniform in \((\pi,2\pi)\); for \(\delta<0\) they are uniform in \((0,\pi)\). The total-variation assertion concerns this fixed-dimensional marked-coordinate representation; it does not concern the unscaled, collapsing second azimuth.

For area-uniform sampling the endpoint density simplifies to \(w(r,s)=\frac12\sin(r+s)\). Thus the pole-clearance rare event selects systematically more polar endpoints than an ordinary independent pair, with a fully explicit shape bias.

## Assumptions and scope

The spherical domain is the closed northern hemisphere, but the radial density charges neither its pole nor its equator as atoms. Azimuths are independent uniform directions; the colatitude distribution is the same for all vertices, with measurable density \(g\) and finite positive cotangent moment \(m\). No continuity or boundedness of \(g\) is needed. Distances are spherical great-circle distances; the hull consists of shortest arcs entirely contained in the open hemisphere almost surely. Throughout \(n\) is fixed while \(\varepsilon\downarrow0\). The set \(I_n\) has positive probability for every \(n\ge3\). Boundary ties have probability zero. For the marked assertion, use the natural labelled colatitudes, relative azimuths, sign, and normalized clearance coordinates; the limit is interpreted as total variation of their joint laws.

## Proof

**1. Gnomonic geometry and inclusion.** The map \(X=(\sin r\cos\phi,\sin r\sin\phi,\cos r)\mapsto(\tan r\cos\phi,\tan r\sin\phi)\) sends shortest spherical geodesics to Euclidean segments and sends the pole to the planar origin. A geodesic-hull boundary edge is therefore exactly a Euclidean hull edge of the projected points. The north pole belongs to its interior iff the independent azimuths do not lie in any open semicircle. Almost surely, if all directions lie in a semicircle, that semicircle has a unique sample at its initial end. The disjoint anchor possibilities give \(\Pr(I_n^c)=n(1/2)^{n-1}\), proving the first formula. If a planar line lies at Euclidean distance \(\rho\) from the origin, the corresponding great circle lies at spherical pole distance \(\arctan\rho\). The closest spherical boundary point is on a hull edge, so these relations identify \(D_n\) with \(\arctan\) of the Euclidean origin-to-hull-boundary distance.

**2. Exact near-antipodal aperture.** Write \(a=\tan r\), \(b=\tan s\) for two projected radii and \(\tau=\tan\varepsilon\). If \(a,b>\tau\), the segment between two points at smaller angular separation \(\Delta\in[0,\pi]\) meets the closed disk of radius \(\tau\) if and only if
\[
\Delta\ge\arccos(\tau/a)+\arccos(\tau/b).
\]
This follows by drawing the two tangents from the endpoints to that disk: at equality the segment is tangent, and the segment is closer to the origin for larger separation. Equivalently, for the signed near-antipodal deviation \(\delta=\operatorname{wrap}(\Phi_j-\Phi_i-\pi)\),
\[
|\delta|\le H_\varepsilon(r,s)
=\arcsin(\tau\cot r)+\arcsin(\tau\cot s).
\]
For each fixed \(r,s>0\), \(H_\varepsilon/\varepsilon\to\cot r+\cot s\). For \(\tau\cot r,\tau\cot s\le1\), \(H_\varepsilon\le(\pi\tau/2)(\cot r+\cot s)\). Since the angular difference is uniform, the unconditioned candidate-pair event has probability \(\mathbb E[H_\varepsilon/\pi]\sim2m\varepsilon/\pi\). If either colatitude is at most \(\varepsilon\), then the event is negligible compared with \(\varepsilon\): indeed
\[
\Pr(R\le\varepsilon)\le\tan\varepsilon\int_0^\varepsilon g(r)\cot r\,dr=o(\varepsilon).
\]
Thus the angular approximation and dominated convergence are valid without assuming a bounded density.

**3. Exposed pole-side edges.** Fix distinct labels \(i<j\). As \(\delta\to0\), their projected endpoints become opposite vectors. Their line approaches a line through the origin. The remaining \(n-2\) projected points all lie on the same side as the origin exactly when their azimuths fall in the appropriate open pole-side semicircle, up to an event whose probability tends to zero for fixed remaining coordinates. The conditional probability of that configuration tends to \(2^{-(n-2)}\). At such a nondegenerate configuration the corresponding segment is an exposed hull edge and the origin lies strictly inside the hull on the near-pole side for all sufficiently small nonzero \(\delta\); its orthogonal projection is interior to that segment. Conversely any hull edge closer than \(\varepsilon\) must satisfy this near-antipodal condition unless one endpoint lies in the negligible \(r\le\varepsilon\) region. Hence one fixed unordered pair contributes
\[
\frac{\varepsilon}{\pi}\int\!\int g(r)g(s)(\cot r+\cot s)\,dr\,ds\;2^{-(n-2)}+o(\varepsilon)
=\frac{2m\varepsilon}{2^{n-2}\pi}+o(\varepsilon).
\]
Two different candidate pairs cannot contribute together at first order. With every radial coordinate truncated below by a fixed positive constant, the simultaneous near-antipodal constraints on two distinct azimuthal differences have probability \(O(\varepsilon^2)\), including when the pairs share a label. The omitted low-radial tails are \(o(\varepsilon)\) by the integrable cotangent bound. Letting the cutoff decrease after taking \(\varepsilon\downarrow0\) yields a total overlap of \(o(\varepsilon)\). Summing over \(\binom n2\) possible boundary edges proves the coefficient.

**4. Marked total-variation law.** In the chart with pair \(i<j\), first azimuth \(\Phi_i\), two colatitudes \((r,s)\), deviation sign \(\varsigma=\operatorname{sign}\delta\), and scaled clearance \(u=D_n/\varepsilon\), the exact signed-angle density is constant in \(\delta\). The Euclidean segment-distance formula has, for fixed \(r,s>0\) and small \(\delta\), the expansion
\[
D_n=\frac{|\delta|}{\cot r+\cot s}+o(|\delta|).
\]
Consequently the Jacobian of the change \(|\delta|\mapsto u\) tends to \(\varepsilon(\cot r+\cot s)\), uniformly on compact radial sets. The edge-support event tends almost everywhere to the condition that the other vertices lie in the selected semicircle. After division by the probability obtained in step 3, the limiting density factors into: the uniform unordered pair; \(w(r,s)\); the uniform anchor azimuth; an independent fair sign; \(\mathbf1_{0<u<1}\); and the product of \(n-2\) original radial densities times the uniform semicircle angular densities. The total limiting density integrates to one because \(\int\!\int w(r,s)\,dr\,ds=1\). Pointwise convergence on compact radial sets, the cotangent domination of step 2 and the \(o(\varepsilon)\) small-radial contribution give convergence in \(L^1\) of these marked densities. Equivalently, Scheffé's lemma yields convergence in total variation. Ignoring the remaining vertices yields the stated simpler joint marginals.

**5. Uniform-area specialization.** For \(g(r)=\sin r\), \(m=\int_0^{\pi/2}\cos r\,dr=1\), and \(g(r)g(s)(\cot r+\cot s)=\sin(r+s)\). For \(g(r)=2\sin r\cos r\), \(m=\int_0^{\pi/2}2\cos^2r\,dr=\pi/2\). Substitution supplies both explicit laws.

## Verification

The included `check.py` computes exact 3D great-circle edge distances from sampled points, checks which edges expose the northern pole, and tests the finite-\(n\) containment probabilities and first-order coefficients for \(n=3,4,5,6\). For independent area-uniform sampling and independent projected-disk-uniform sampling, numerical tests at thresholds \(0.009\) and \(0.018\) use one million independent samples per configuration, with an independent check of the rare-edge colatitude mean. The checker prints `POLE_CLEARANCE_COTANGENT_MARKED_LAW_DIAGNOSTIC_OK` when diagnostics pass. These simulations corroborate finite-scale consequences but cannot prove the asymptotic theorem; the analytic aperture estimate, radial domination and marked-density convergence above do so.

## Relationship to prior work

Wendel's center-containment formula gives \(\Pr(I_n)=1-n/2^{n-1}\) and is credited, not claimed as new. Bárány, Hug, Reitzner and Schneider, *Random points in halfspheres* (arXiv:1505.04672v1, 2015-05-18), analyze global hull face expectations, volume/surface area, and hemisphere approximation as \(n\to\infty\); their results do not provide this fixed-\(n\) pole-clearance derivative or marked edge law. Kabluchko's *Expected f-vector of the Poisson zero polytope and random convex hulls in the half-sphere* (2020) similarly treats f-vectors, random hulls and volume-like quantities, not the fixed-pole rare conditional distribution. Bürgisser, Cucker and Lotz (arXiv:0712.2816) study hemisphere-covering and feasibility condition numbers under a different full-sphere sampling model; their related notions do not state this axial cotangent-moment derivative.

A published marked Wendel-law result for smooth centrally symmetric curves treats the large-\(n\) **miss** event (the origin lies outside the hull) and its conditional Euclidean clearance. The present theorem instead conditions on center **inclusion** in an axially sampled spherical hemisphere at **fixed** \(n\) and resolves a small **inside-to-boundary** distance with its edge and colatitude marks. A published antipodal cap-transition result analyzes one pair's near-antipodal distance in higher-dimensional spherical caps; the two-point localization is related, but it does not imply the supporting-edge probability, fixed-pole condition, or full marked distribution here. No historical-priority claim is made beyond the specifically compared statements, and alternative terminology in older integral geometry remains a risk.

## Limitations

The result is two-dimensional in its spherical surface, requires independent uniform azimuths and a finite cotangent moment, and keeps \(n\) fixed. It does not describe a growing-\(n\) window, anisotropic azimuths, point-mass atoms, or hyperspherical polytopes. The origin-inclusion probability is classical. Total-variation convergence is for explicitly marked, rescaled local coordinates; unscaled singular geometry cannot have such convergence. Independent mathematical verification and exhaustive historical priority inspection are not claimed.

## References

1. J. G. Wendel, “A Problem in Geometric Probability,” *Mathematica Scandinavica* 11 (1962), 109–112, DOI: 10.7146/math.scand.a-10655, https://doi.org/10.7146/math.scand.a-10655.
2. I. Bárány, D. Hug, M. Reitzner and R. Schneider, “Random points in halfspheres,” arXiv:1505.04672v1, first made public 2015-05-18, https://arxiv.org/abs/1505.04672. Later *Random Structures & Algorithms* 50 (2017), 3–22.
3. Z. Kabluchko, “Expected f-vector of the Poisson zero polytope and random convex hulls in the half-sphere,” *Mathematika* (2020), DOI: 10.1112/mtk.12056, https://doi.org/10.1112/mtk.12056.
4. P. Bürgisser, F. Cucker and M. Lotz, “Coverage processes on spheres and condition numbers for linear programming,” arXiv:0712.2816, first posted 2007-12-18, https://arxiv.org/abs/0712.2816.
5. “Marked Wendel law and convex-order optimal sampling for random inscribed polygons,” publicly accessible result, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-marked-wendel-law-and-convex-order-optimal-sampling-for-random-i--6fc92189d743.
6. “A joint antipodal boundary-layer law across the hemispherical cap transition,” publicly accessible result, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-joint-antipodal-boundary-layer-law-across-the-hemispherical-ca--36d67459f871.
