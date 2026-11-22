# Three Fourier-mean area phases and universal polygonal facet horns

## Finding
Let \(P\subset\mathbb R^2\) be **any** full-dimensional compact convex polygon of area \(A\). In the Fourier convention \(\widehat{\mathbf1_P}(\xi)=\int_Pe^{-i\langle\xi,x\rangle}\,dx\), define the extended radial function, for every \(p>0\) and \(u\in S^1\), by
\[
\rho_p(u)^p=\frac{p}{A}\int_0^\infty |\widehat{\mathbf1_P}(ru)|^2r^{p-1}\,dr.
\]
The associated star set \(F_pP=\{ru:u\in S^1,\ 0\le r\le\rho_p(u)\}\), allowing infinite radii, has **exactly three area/compactness phases**:
\[
\boxed{\begin{array}{ll}0<p<2:&F_pP\text{ is compact};\\ 2\le p<4:&F_pP\text{ is unbounded and has finite, positive area};\\ p\ge4:&F_pP=\mathbb R^2.\end{array}}
\]
The finite-area statement at \(p=2\), including \(\operatorname{Area}(F_2P)=4\pi^2\), is **already known** for arbitrary convex bodies and is included here only to identify the full phase boundary; the additional new geometric classification concerns \(2<p<4\), its sharp facet-horn asymptotics, and the all-direction endpoint \(p=4\).

For any edge-normal unit vector \(n\), let \(t\) be a perpendicular unit tangent, and let \(\mathcal E(n)\) be the one or two edges of \(P\) parallel to \(t\), with lengths \(\ell_E>0\). For fixed \(2<p<4\), as \(\theta\to0\),
\[
\boxed{\rho_p(n\cos\theta+t\sin\theta)^p\sim \frac{p\pi\sum_{E\in\mathcal E(n)}\ell_E^{4-p}}{A\Gamma(5-p)\sin(\pi(4-p)/2)}\,|\theta|^{2-p}.}
\]
At \(p=2\) the corresponding sharp law is
\[
\rho_2(n\cos\theta+t\sin\theta)^2=\frac{2}{A}\left(\sum_{E\in\mathcal E(n)}\ell_E^2\right)\log(1/|\theta|)+O_P(1).
\]
Thus each unbounded facet-normal ray sits inside a quantitative power horn, or a logarithmic horn at the endpoint. The power exponent for radial-square area is \(2(p-2)/p<1\), so every horn contributes finite area exactly throughout the open interval \(2<p<4\).

There is also an exact *finite* formula away from edge normals. Set \(g_u(s)=\mathcal H^1(P\cap\{x:\langle u,x\rangle=s\})\), and list the distinct projected-vertex abscissae \(s_1<\cdots<s_N\). For \(u\) not normal to an edge, this is a continuous compactly supported piecewise-affine function. Define the jumps \(c_j=g_u'(s_j+)-g_u'(s_j-)\). For \(2<p<4\),
\[
\boxed{\rho_p(u)^p=-\frac{p\pi}{2A\Gamma(5-p)\sin(\pi(4-p)/2)}\sum_{j,k=1}^Nc_jc_k|s_j-s_k|^{4-p}.}
\]
For \(p=2\) its logarithmic limit is \(\rho_2(u)^2=A^{-1}\sum_{j,k}c_jc_k(s_j-s_k)^2\log|s_j-s_k|\), with \(0\log0=0\). Finally, in every non-edge-normal direction,
\[
\boxed{\lim_{p\uparrow4}(4-p)\rho_p(u)^p=\frac4A\sum_{j=1}^Nc_j^2>0,}
\]
so \(p=4\) is the exact global ray-divergence threshold. The jump coefficients are grouped at coincident projected vertices; the formulas make no generic-position assumption beyond excluding edge normals.

## Assumptions and scope
The polygon is a convex body in the Euclidean plane with finitely many nonzero-length edges and positive area. Adjacent collinear edges are merged. All radial integrals are understood as extended nonnegative integrals. Polygon vertices may have coincident projection abscissae, and opposing edges may be parallel with unequal lengths. Angles are measured in radians. The strict inequality \(2<p<4\) is essential for the fractional-distance identity. The Fourier transform uses no \(2\pi\) factor in the exponential. All statements are invariant under Euclidean rigid motions and behave correctly under scaling.

## Proof
**1. Projections and ray finiteness.** The Fourier slice identity is \(\widehat{\mathbf1_P}(ru)=\int_{\mathbb R}g_u(s)e^{-irs}\,ds\). Away from edge normals, each intersection endpoint varies affinely in the level \(s\) between consecutive projected vertex levels, so \(g_u\) is continuous, piecewise affine and compactly supported. Its distributional second derivative is \(g_u''=\sum_jc_j\delta_{s_j}\), giving for \(r\ne0\)
\[
\widehat{\mathbf1_P}(ru)=-r^{-2}\sum_jc_je^{-irs_j}.
\]
The sign does not matter below. Compact support and continuity imply \(\sum c_j=\sum c_js_j=0\). The finite trigonometric polynomial \(h_u(r)=\sum c_je^{-irs_j}\) is nonzero (otherwise \(g_u\equiv0\)), and \(R^{-1}\int_0^R|h_u(r)|^2dr\to\sum c_j^2>0\). Therefore \(\int_1^\infty|h_u(r)|^2r^{p-5}dr\) converges precisely when \(p<4\). At \(p=4\) it diverges logarithmically with coefficient \(\sum c_j^2\), and above it diverges polynomially by averaging. This proves the nonnormal ray criterion, including the asserted \(p\uparrow4\) residue (by the Abelian weighted mean theorem). For \(u\) normal to an edge, \(g_u\) has a nonzero jump at each projected support edge, hence \(\widehat{\mathbf1_P}(ru)=r^{-1}\) times a nonzero finite sum of distinct oscillatory frequencies, plus \(O(r^{-2})\). Its positive mean square makes the integral infinite exactly for \(p\ge2\). Standard bounded-variation integration by parts gives uniform \(|\widehat{\mathbf1_P}(ru)|\le C_P/r\) across all \(u\), so \(\rho_p\) is bounded and continuous when \(0<p<2\). Hence \(F_pP\) is compact in this range, unbounded for \(p\ge2\), and the whole plane for \(p\ge4\).

**2. Exact projected-vertex energy.** Put \(\alpha=4-p\in(0,2)\) and use
\[
\int_0^\infty(1-\cos(rs))r^{-1-\alpha}\,dr=\frac{\pi|s|^\alpha}{2\Gamma(1+\alpha)\sin(\pi\alpha/2)}.
\]
Because \(\sum c_j=0\), expansion of the square \(|h_u|^2\) as \(-\sum_{j,k}c_jc_k(1-\cos(r(s_j-s_k)))\) proves the displayed exact finite formula. Strict positivity follows because this equals the integral of a nonzero squared Fourier transform. Sending \(\alpha\uparrow2\), the leading apparent pole cancels since \(\sum c_jc_k(s_j-s_k)^2=-2(\sum c_js_j)^2=0\); its finite remainder is the displayed logarithmic expression.

**3. The facet-normal boundary layer.** Fix \(n\), let \(u_\theta=n\cos\theta+t\sin\theta\), and write each edge \(E\) using its midpoint \(m_E\), length \(\ell_E\), unit tangent \(t_E\), and outer unit normal \(n_E\). The divergence theorem gives exactly
\[
\widehat{\mathbf1_P}(ru_\theta)=\frac{-1}{ir}\sum_E (u_\theta\cdot n_E)\ell_E\,e^{-ir\langle u_\theta,m_E\rangle}\operatorname{sinc}\left(\frac{r\ell_E\langle u_\theta,t_E\rangle}{2}\right).
\]
For \(|\theta|\) sufficiently small, all edges not parallel to \(t\) contribute together \(O_P(r^{-2})\), uniformly for \(r\ge1\). Each parallel edge contributes a leading term of magnitude \(\ell_E r^{-1}|\operatorname{sinc}(r\ell_E\sin\theta/2)|\); its phase has a midpoint projection converging to the corresponding supporting line. Distinct parallel supporting edges have nonzero, distinct limiting midpoint projections. On multiplying the radial energy by \(|\theta|^{p-2}\) and substituting \(q=r|\theta|\), the cross-terms between these distinct parallel edges vanish by the Riemann--Lebesgue lemma; the remaining cross-terms with the \(O(r^{-2})\) remainder are \(o(|\theta|^{2-p})\) by splitting at \(r=1/|\theta|\) and using \(\min(r^{-1},|\theta|^{-1}r^{-2})\) for each special-edge term. The diagonal special-edge energy gives
\[
\lim_{\theta\to0}|\theta|^{p-2}\int_0^\infty|\widehat{\mathbf1_P}(ru_\theta)|^2r^{p-1}dr
=\sum_{E\in\mathcal E(n)}\ell_E^{4-p}\frac{\pi}{\Gamma(5-p)\sin(\pi(4-p)/2)},
\]
by the same fractional cosine integral. At \(p=2\), split the radial range into \(r\in[1,1/|\theta|]\) and its complement. The diagonal special-edge contributions are \(\ell_E^2\log(1/|\theta|)+O_P(1)\); oscillatory separated-edge cross terms and nonspecial-edge terms contribute \(O_P(1)\). This establishes both horn formulas.

**4. Finite-area phase.** There are finitely many edge-normal directions. On their complementary closed angular arcs the radial function is finite and continuous for \(p<4\), by the exact projected-vertex representation or uniform \(r^{-2}\) Fourier decay. The sharp horns imply \(\rho_2(u_\theta)^2=O(1+|\log|\theta||)\), and, for \(2<p<4\), \(\rho_p(u_\theta)^2=O(|\theta|^{-2(p-2)/p})\). Since the latter exponent is strictly below one, \(\frac12\int_{S^1}\rho_p^2\,du<\infty\). Nonempty interior and positive area are immediate from \(\rho_p>0\). This proves the asserted phase classification.

## Verification
The independent script `verify.py` constructs projected chord-length knots and second-derivative jumps by intersecting polygon edges with level lines; it evaluates the finite fractional-energy formula without using the boundary-edge transform argument. It tests two unrelated polygon geometries (square and right triangle), including coincident projected vertices, against separate closed-form oscillatory integrals for \(p=3\), the logarithmic \(p=2\) square value, and facet-horn coefficients in both examples. Numeric tests are consistency checks only, not substitutes for the general proof.

## Relationship to prior work
Langharst, Manui and Zvavitch (2026) introduce Fourier mean bodies, prove the **already known** universal finite-volume identity at \(p=2\) (Proposition 6), and establish noncompactness for the square at \(p\ge2\). Their paper does not give this entire polygonal three-phase classification above \(p=2\), or its explicit facet-normal horn laws. The previously published classification of cubic Fourier-mean directional residues gives complete coordinate-support thresholds for cubes, and includes the square's generic ray threshold as a special case, but not a result for every convex polygon or finite area throughout \(2<p<4\). A separate quartic-disk finding gives a three-phase structure for one *smooth* body with different critical exponents. Wuttke (2017) derives general polygon Fourier transforms, which are used here as established groundwork, rather than claimed as new. The independent universal polygonal \(1<p<2\) facet cusp/nonconvexity statement is earlier work and is not a component of the new claim. None of the compared statements yields the asserted **full all-polygon area phase, facet horn coefficient, and exact generic projected-vertex energy** as an existing cited conclusion.

## Limitations
The classification is planar, polygonal, and convex. It does not describe polygons with fractal boundaries, smooth ovals, general higher-dimensional polytopes, or \(p\le0\). The exact facet asymptotics are pointwise for each fixed \(p\), not uniform as \(p\to4\). The value \(\operatorname{Area}(F_2P)=4\pi^2\) and the known square noncompactness result are prior art, not originality claims. Standard Fourier and fractional-kernel identities are used without novelty claims. Historical priority remains provisional; no independent external mathematical audit has been performed.

## References
1. D. Langharst, A. Manui and A. Zvavitch, *On the Fourier Mean Bodies of a Convex Body*, arXiv:2601.20117v1, first public 2026-01-27, Sections 1.3.1 and 5, https://arxiv.org/html/2601.20117v1.
2. J. Wuttke, *Form factor (Fourier shape transform) of polygon and polyhedron*, arXiv:1703.00255v1, first public 2017-03-01, Sections 2--3, https://arxiv.org/html/1703.00255v1.
3. L. Brandolini, M. Rigoli and G. Travaglini, *Average decay of Fourier transforms and geometry of convex sets*, Rev. Mat. Iberoamericana 14 (1998), 519--560, DOI 10.4171/RMI/244, comparison of average decay rather than the presently stated Fourier-mean directional integral.
4. *Coordinate-stratified divergence and sharp resonance residues of Fourier mean bodies of cubes*, publicly archived mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-coordinate-stratified-divergence-and-sharp-resonance-residues-of--a7d140566df1.
5. *Three Fourier-mean phases and an exact logarithmic horn constant for the quartic disk*, publicly archived mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-three-fourier-mean-phases-and-an-exact-logarithmic-horn-constant--9e341c4e60ef.
