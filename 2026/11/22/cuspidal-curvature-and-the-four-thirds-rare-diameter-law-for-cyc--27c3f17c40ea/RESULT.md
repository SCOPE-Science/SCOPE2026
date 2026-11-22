# Cuspidal curvature and the four-thirds rare-diameter law for cycloidal arches

## Finding
Let \(\Gamma\) be a compact, simple, rectifiable Euclidean plane arc of length \(L>0\) with two endpoint cusps forming its **unique unordered diametral pair**, of length \(D>0\). Suppose it is regular away from the endpoints and, after a Euclidean rigid motion placing its endpoints at \((0,0)\) and \((D,0)\), has smooth one-sided local parametrizations
\[
\gamma_L(t)=(a_Lt^3+O(t^4),\ b_Lt^2+O(t^3)),\qquad
\gamma_R(s)=(D-a_Rs^3+O(s^4),\ b_Rs^2+O(s^3))
\]
as \(t,s\downarrow0\), with \(a_L,a_R>0\) and \(b_Lb_R\ne0\). Let \(P,Q\) be independent arclength-uniform points on \(\Gamma\), and \(X=\|P-Q\|\). Then
\[
\Pr(D-X\le\varepsilon)
\sim C_\Gamma\varepsilon^{4/3},\qquad
C_\Gamma=\frac{8\Gamma(2/3)^2}{9L^2\Gamma(7/3)}
\frac{|b_Lb_R|}{(a_La_R)^{2/3}}.
\]
In terms of the absolute Euclidean cuspidal curvatures
\[
|\mu_i|=\frac{|\det(\gamma_i''(0),\gamma_i'''(0))|}
{\|\gamma_i''(0)\|^{5/2}}
=\frac{3a_i}{\sqrt2|b_i|^{3/2}},
\]
this is the intrinsic formula
\[
C_\Gamma=\frac8{9L^2}\left(\frac3{\sqrt2}\right)^{4/3}
\frac{\Gamma(2/3)^2}{\Gamma(7/3)}
|\mu_L\mu_R|^{-2/3}.
\]

Conditioned on \(D-X\le\varepsilon\), the two possible endpoint orders tend to independent equiprobable choices. Within either order, if \(t\) and \(s\) are the one-sided local cusp parameters of the sampled points, the three coordinates
\[
\left(\frac{a_Lt^3}{\varepsilon},\ \frac{a_Rs^3}{\varepsilon},\ 1-\frac{D-X}{\varepsilon}\right)
\]
converge jointly to \(\operatorname{Dirichlet}(2/3,2/3,1)\). In particular, the rescaled distance deficit converges to \(\operatorname{Beta}(4/3,1)\) and the fraction of its leading cubic deficit contributed by the left cusp converges to \(\operatorname{Beta}(2/3,2/3)\), independently.

For the complete one-arch cycloid traced by a circle of radius \(r>0\),
\[
\gamma_r(t)=r(t-\sin t,1-\cos t),\qquad 0\le t\le2\pi,
\]
the hypotheses hold, the unique diameter is \(D=2\pi r\), the total arclength is \(L=8r\), and \(|\mu_L|=|\mu_R|=r^{-1/2}\). Thus
\[
\boxed{\Pr(2\pi r-X\le\varepsilon)
\sim \frac{6^{4/3}\Gamma(2/3)^2}{288\Gamma(7/3)}
\left(\frac{\varepsilon}{r}\right)^{4/3}}
\]
with dimensionless numerical coefficient \(0.0583009007833961\ldots\). The limit is at fixed \(r>0\) as \(\varepsilon\downarrow0\).

## Assumptions and scope
A one-sided cusp parameter is smooth enough for the stated Taylor expansions and the arc is regular at interior points. The two endpoint positions must be the **only** pair on the arc at Euclidean distance \(D\); this global hypothesis cannot be inferred from local cusp geometry alone. The projections of the cubic terms onto the diameter are strictly inward (the positive \(a_i\)); this is a nondegeneracy condition. The tangent vectors of the endpoint cusps are perpendicular to the diameter (the quadratic terms are vertical). The arclength distribution gives each subarc probability proportional to its Euclidean length, not equal probability in the displayed local parameters.

The result is for Euclidean distances between independently chosen **boundary-arc points**. It is not a Euclidean-invariant random-line chord model, and it does not include samples from the area below a cycloid. \(\Gamma(z)\) in constants denotes Euler's gamma function; the symbol \(\Gamma\) without an argument denotes the geometric arc.

## Proof
**1. Unique global diameter of a full cycloid arch.** By scaling it suffices to take \(r=1\). For any \(t,s\in[0,2\pi]\), write \(d=|t-s|/2\in[0,\pi]\) and \(m=(t+s)/2\). The cosine difference formula gives the exact chord identity
\[
\|\gamma_1(t)-\gamma_1(s)\|^2
=4\{d^2+\sin^2d-2d\sin d\cos m\}.
\]
Since \(\sin d\ge0\) and \(\cos m\ge-1\), the distance is bounded by \(2(d+\sin d)\). The function \(d+\sin d\) is strictly increasing on \([0,\pi]\) (its derivative is \(1+\cos d>0\) for \(d<\pi\)) and equals \(\pi\) only at \(d=\pi\). Hence every chord has length at most \(2\pi\), with equality only when \(\{t,s\}=\{0,2\pi\}\).

**2. Uniform local diameter deficit.** For a general arc under the stated assumptions, place a point near the left cusp at \(\gamma_L(t)\) and one near the right cusp at \(\gamma_R(s)\). Their horizontal separation is \(D-a_Lt^3-a_Rs^3+O(t^4+s^4)\), and their vertical separation is \(O(t^2+s^2)\). Expanding the Euclidean square root around \((D,0)\) gives
\[
D-\|\gamma_L(t)-\gamma_R(s)\|
=a_Lt^3+a_Rs^3+O(t^4+s^4),
\]
uniformly as \(t,s\downarrow0\). The remainder is \(o(t^3+s^3)\), including along either coordinate axis. Because the diametral pair is globally unique, compactness excludes all pairs outside arbitrarily small neighborhoods of the two ordered cusp pairs from the event \(D-X\le\varepsilon\), once \(\varepsilon\) is small.

**3. Arclength Jacobians.** Differentiation of the local parametrizations yields
\[
d\ell_L=(2|b_L|t+O(t^2))\,dt,\qquad
d\ell_R=(2|b_R|s+O(s^2))\,ds.
\]
There are two ordered possibilities, each with product probability density \(L^{-2}d\ell_Ld\ell_R\). Hence the leading mass is
\[
\frac{8|b_Lb_R|}{L^2}
\int_{a_Lt^3+a_Rs^3\le\varepsilon}ts\,dt\,ds.
\]
In the change of variables \(u=a_Lt^3/\varepsilon\), \(v=a_Rs^3/\varepsilon\), the measure becomes
\[
\frac{8|b_Lb_R|}{9L^2}
(a_La_R)^{-2/3}\varepsilon^{4/3}
 u^{-1/3}v^{-1/3}\,du\,dv
\]
on \(u,v\ge0\), \(u+v\le1\). The Dirichlet beta integral is
\[
\int_{u+v\le1}u^{-1/3}v^{-1/3}\,du\,dv
=\frac{\Gamma(2/3)^2}{\Gamma(7/3)}.
\]
Uniform remainder bounds and dominated convergence justify replacing the exact event and exact arclength densities by these leading forms. This proves the stated coefficient and, after normalization, the joint Dirichlet limit. The identities for the beta marginals and the independent endpoint order follow from elementary Dirichlet aggregation and the symmetry of the two ordered events.

**4. Intrinsic normalization.** The cusp derivative vectors are \(\gamma_i''(0)=(0,2b_i)\), and their cubic derivatives have horizontal absolute component \(6a_i\). Consequently \(|\mu_i|=3a_i/(\sqrt2|b_i|^{3/2})\), so \(|b_i|a_i^{-2/3}=(3/\sqrt2)^{2/3}|\mu_i|^{-2/3}\). Substitution yields the intrinsic formula. In particular, the leading tail and total arclength jointly recover \(|\mu_L\mu_R|\) within this class, but not its two individual factors.

**5. Cycloid specialization.** The cycloid has expansions
\[
\gamma_r(t)=\left(\frac r6t^3+O(t^5),\frac r2t^2+O(t^4)\right),\quad
\gamma_r(2\pi-s)=\left(2\pi r-\frac r6s^3+O(s^5),\frac r2s^2+O(s^4)\right).
\]
Its arclength element is \(2r\sin(t/2)\,dt\) and integrates to \(8r\). The cusp coefficients are \(a_i=r/6\), \(b_i=r/2\), so \(|\mu_i|=r^{-1/2}\). Inserting these values in the general law gives the displayed \(r^{-4/3}\) coefficient. Step 1 supplies the otherwise indispensable global uniqueness hypothesis.

## Verification
The enclosed `check.py` evaluates the exact distance expression, verifies the two independently simplified gamma-function coefficients, and computes the finite-threshold probability by deterministic nested quadrature and scalar bracketing. Replaying with Python 3.13 and SciPy 1.17 produced ratios of direct probability to the claimed leading asymptotic of approximately \(1.0262350114\), \(1.0112603268\), and \(1.0050207385\) at \(\varepsilon=10^{-2},10^{-3},10^{-4}\), respectively. The directly integrated conditional first cubic-deficit mark was approximately \(0.286831903\) at \(10^{-4}\), approaching the Dirichlet prediction \(2/7\). A supplementary 20,100-pair grid test checks, but does not prove, the global diameter bound. The exact analytic argument, not a finite grid or floating-point computation, proves the infinite claims.

## Relationship to prior work
Shiba and Umehara (2011, first arXiv release February 22) developed Euclidean and affine normalized curvature at \(3/2\)-cusps and explicitly calculated the cycloid's cuspidal curvature in Example 2.4. Their Theorem 1.1 and example provide useful local geometry; the global diametral-pair classification, pairwise arclength chord tail, exact gamma coefficient, and conditional Dirichlet law are separate assertions. Apostol and Mnatsakanian (2009) established cycloidal area identities. Available bibliographic material for that paper addresses areas, not an arclength-uniform two-point distance tail, but its full article was not inspected and it remains a priority uncertainty. The random-chord literature on invariant lines in convex bodies, regular polygons and smooth convex boundaries uses other objects, sampling conventions or regularity assumptions. Indexed statements about gamma/Dirichlet chord tails of \(\ell_p\) balls concern Euclidean-invariant line chords, not independent arclength points on a two-cusp plane arc; neither implication nor equality of exponents is asserted.

## Limitations
No rate of convergence or two-term expansion is proved. The general theorem requires unique diametral cusps with inward nonzero cubic displacement perpendicular to a quadratic cusp tangent; if another pair is diametral, if an inward coefficient vanishes, or if a quadratic displacement has a longitudinal component, different laws may arise. The coefficient identifies only the product of absolute cuspidal curvatures at fixed total length. Other sampling laws (parameter-uniform, planar area-uniform, invariant-line chords) are excluded. Numerical decimal values are diagnostics, not rigorously enclosed intervals. Priority beyond the inspected works and indexed matches remains provisional, and independent mathematical review is not supplied.

## References
- S. Shiba and M. Umehara, *The behaviour of curvature functions at cusps and inflection points*, arXiv:1102.4478v1 (first public February 22, 2011), especially Theorem 1.1 and Example 2.4. https://arxiv.org/abs/1102.4478
- T. M. Apostol and M. A. Mnatsakanian, *New Insight into Cycloidal Areas*, American Mathematical Monthly 116 (2009), 598–611, DOI:10.4169/193009709X458573. https://authors.library.caltech.edu/records/7wxkh-b1h64
- D. Ren, *Random chord distributions and containment functions*, Advances in Applied Mathematics 2014, DOI:10.1016/j.aam.2014.05.003 (sampling-convention context, not used as an asserted theorem here). https://doi.org/10.1016/j.aam.2014.05.003
