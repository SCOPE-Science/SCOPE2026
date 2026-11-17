# Two-term near-diameter tails and universal endpoint laws for convex polytopes

## Finding

**Theorem.** Fix an integer \(d\ge2\) and a full-dimensional compact convex polytope \(P\subset\mathbb R^d\). Let \(V=\operatorname{vol}_d(P)>0\), \(D=\operatorname{diam}(P)>0\), and let \(X,Y\) be independent points uniform with respect to volume in \(P\). Write \(\mathcal E\) for the finite set of **ordered** pairs \((a,b)\) of vertices of \(P\) with \(\|b-a\|=D\). For \((a,b)\in\mathcal E\), define \(e=(b-a)/D\), vertex tangent cones \(C_a=\operatorname{cone}(P-a)\) and \(C_b=\operatorname{cone}(P-b)\), and the strictly positive linear function on their product
\[
L_{ab}(u,v)=e\mathbin{\cdot}u-e\mathbin{\cdot}v.
\]
Set
\[
c_a(e)=\operatorname{vol}_d\{u\in C_a:e\mathbin{\cdot}u<1\},\qquad
c_b(-e)=\operatorname{vol}_d\{v\in C_b:-e\mathbin{\cdot}v<1\},
\]
\[
k_{ab}=\frac{(d!)^2}{(2d)!}c_a(e)c_b(-e).
\]
Let \(\mu_{ab}\) be the probability measure on the compact cone slice
\[
S_{ab}=\{(u,v)\in C_a\times C_b:L_{ab}(u,v)=1\}
\]
proportional to \((2d-1)\)-dimensional Hausdorff measure (equivalently to coarea measure, because the gradient of \(L_{ab}\) is constant). Put
\[
m_{ab}=\int_{S_{ab}}\left[\|v-u\|^2-1\right]d\mu_{ab}(u,v)
=\int_{S_{ab}}\|\bigl(v-u\bigr)-\bigl(e\mathbin{\cdot}(v-u)\bigr)e\|^2d\mu_{ab}.
\]
Then \(k_{ab}>0\), \(m_{ab}>0\), and, as \(\varepsilon\downarrow0\),
\[
\boxed{\Pr\bigl(\|X-Y\|>D-\varepsilon\bigr)
=\frac{\varepsilon^{2d}}{V^2}\sum_{(a,b)\in\mathcal E}k_{ab}
+\frac{d\varepsilon^{2d+1}}{DV^2}\sum_{(a,b)\in\mathcal E}k_{ab}m_{ab}
+O_P(\varepsilon^{2d+2}).}
\]
Both displayed coefficients are strictly positive for every \(d\ge2\).

The event in this theorem localizes the ordered pair \((X,Y)\) to small neighborhoods of the ordered vertex pairs in \(\mathcal E\). Conditional on that event, the selected pair \((a,b)\) has limiting probability \(k_{ab}/\sum_{\mathcal E}k_{ab}\). Given its selection, the rescaled displacements \(U=(X-a)/\varepsilon\), \(W=(Y-b)/\varepsilon\) converge **in total variation** to normalized Lebesgue measure on the bounded set
\[
\Omega_{ab}=\{(u,v)\in C_a\times C_b:L_{ab}(u,v)<1\}.
\]
In this limit the three-vector
\[
\bigl(e\mathbin{\cdot}U,-e\mathbin{\cdot}W,1-L_{ab}(U,W)\bigr)
\]
has distribution \(\operatorname{Dirichlet}(d,d,1)\), and the normalized distance deficit \((D-\|X-Y\|)/\varepsilon\) converges to \(\operatorname{Beta}(2d,1)\). If both vertex cones are **simple** (each has exactly \(d\) extreme rays), express each displacement in ray generators normalized to unit positive depth; then its \(2d\) nonnegative ray coefficients together with the remaining depth converge to \(\operatorname{Dirichlet}(1,\ldots,1)\), with exactly \(2d+1\) parameters.

**Box corollary.** For \(B=\prod_{i=1}^d[0,a_i]\) with \(a_i>0\), write \(V=\prod_i a_i\) and \(D=(\sum_i a_i^2)^{1/2}\). Then
\[
\boxed{\Pr(\|X-Y\|>D-\varepsilon)
=\frac{2^dD^{2d}}{(2d)!V^4}\varepsilon^{2d}
\left[1+\left(\frac{3D}{2d+1}\sum_{i=1}^d\frac1{a_i^2}-\frac dD\right)\varepsilon+O_B(\varepsilon^2)\right].}
\]
Among all such boxes with fixed volume \(V\), the leading coefficient is at least \(2^dd^d/((2d)!V^2)\), with equality **only** for a cube. This is a fixed-volume optimization of the *leading probability coefficient*, not a stochastic ordering of the entire distributions.

## Assumptions and scope

All distances are Euclidean, not geodesic or Minkowski-gauge distances. All dimensions \(d\ge2\) are fixed. The polytope may be non-simple and have any finite number of diametral vertex pairs. The two sampled points are independent and area/volume-uniform, not boundary-uniform. The order of the pair matters in the coefficients and mixture (each unordered diametral pair occurs twice). Every \(O_P\) constant can depend on the fixed polytope and its dimension; no uniformity over degenerating families of polytopes is asserted. The transverse moment uses the specific normalization \(L_{ab}=1\). In the conditional statement, vertex-pair selection means selection of the unique disjoint pair of sufficiently small neighborhoods on which the rare event lies; the limiting law does not depend on the particular neighborhoods.

## Proof

**1. The only maximizing point pairs are vertex pairs and the cone slices are compact.** A maximizing pair \((x,y)\in P^2\) has \(\|x-y\|=D\). If \(x\) were a nontrivial convex combination of two distinct points of \(P\), strict convexity of the Euclidean norm would force the two vectors from \(y\) to those points to coincide when equality with the diameter holds. Thus \(x\) must be a vertex; similarly \(y\) must be a vertex. There are finitely many maximizing ordered pairs, precisely \(\mathcal E\).

Fix one such pair. Every nonzero \(u\in C_a\) has \(e\mathbin{\cdot}u>0\). Indeed, for some \(\delta>0\), \(a+tu\in P\) when \(0<t<\delta\), and
\[
\|b-a-tu\|^2=D^2-2Dt(e\mathbin{\cdot}u)+t^2\|u\|^2\le D^2.
\]
If \(e\mathbin{\cdot}u\le0\), this is impossible. Likewise \(-e\mathbin{\cdot}v>0\) for every nonzero \(v\in C_b\). Compactness of the unit-direction sections of these closed polyhedral cones gives positive lower bounds, hence \(L_{ab}(u,v)\ge\eta_{ab}(\|u\|+\|v\|)\) for some \(\eta_{ab}>0\). In particular, the cone truncated by \(L_{ab}\le1\) and the slice \(S_{ab}\) are compact with finite positive volumes/areas.

By compactness and the finite maximizing set, sufficiently small distance deficits force \((X,Y)\) into mutually disjoint vertex-pair neighborhoods. In each, the polytope coincides **exactly** with its tangent cone translated from the vertex; this follows from its finite defining halfspaces, since constraints inactive at a vertex remain inactive nearby. Write \(X=a+\varepsilon u\), \(Y=b+\varepsilon v\). The exact square-distance inequality is
\[
\|De+\varepsilon(v-u)\|^2>(D-\varepsilon)^2
\quad\Longleftrightarrow\quad
L_{ab}(u,v)<1+\frac{\varepsilon}{2D}\bigl(\|v-u\|^2-1\bigr).
\]
The bound from the previous paragraph makes the rescaled domain uniformly bounded for small \(\varepsilon\); alternatively, the distance deficit is bounded below by a positive multiple of \(\|X-a\|+\|Y-b\|\) on sufficiently small vertex neighborhoods, by differentiability and positivity of \(L_{ab}\). Thus no remote portions of the cones enter the local calculation.

**2. Leading cone volume.** Define \(A_a(t)=\operatorname{vol}_d\{u\in C_a:e\mathbin{\cdot}u<t\}=c_a(e)t^d\), with the analogous relation for \(b\). Fubini and the beta integral give
\[
\operatorname{vol}_{2d}\Omega_{ab}
=\int_{0}^{1}d\,c_a(e)t^{d-1}\,c_b(-e)(1-t)^d\,dt
=\frac{(d!)^2}{(2d)!}c_a(e)c_b(-e)=k_{ab}.
\]
Under uniform measure on \(\Omega_{ab}\), the pair of endpoint depths \((e\mathbin{\cdot}u,-e\mathbin{\cdot}v)\) has density proportional to \(t^{d-1}s^{d-1}\) on \(t,s\ge0\), \(t+s\le1\), proving the \(\operatorname{Dirichlet}(d,d,1)\) assertion. For simple cones, choose positive-depth-one extreme-ray generators. Their \(2d\) coefficients give linear coordinates with a constant nonzero Jacobian on the standard \(2d\)-simplex, proving the finer Dirichlet assertion.

**3. First curvature correction.** For the fixed ordered pair, use rays \((u,v)=t\omega\), where \(\omega\in S_{ab}\), \(t\ge0\). The Euclidean cone-volume element disintegrates into \(t^{2d-1}dt\) times coarea measure on the slice, up to a constant that cancels on normalization. Since \(L_{ab}(\omega)=1\), its rare-event radial boundary solves
\[
t<1+\frac{\varepsilon}{2D}(t^2\|\omega_v-\omega_u\|^2-1).
\]
The implicit-function theorem, uniformly over the compact slice, gives a unique boundary
\[
t_\varepsilon(\omega)=1+\frac{\varepsilon}{2D}\bigl(\|\omega_v-\omega_u\|^2-1\bigr)+O_P(\varepsilon^2).
\]
Therefore the volume of this rare-event region, after dividing by \(\varepsilon^{2d}\), is
\[
\frac{k_{ab}}{1}\int_{S_{ab}}t_\varepsilon(\omega)^{2d}d\mu_{ab}(\omega)
=k_{ab}\left[1+\frac{d\varepsilon}{D}m_{ab}+O_P(\varepsilon^2)\right].
\]
Here \(e\mathbin{\cdot}(\omega_v-\omega_u)=-1\), so the expression defining \(m_{ab}\) is the squared transverse component of \(\omega_v-\omega_u\) and is nonnegative. It is strictly positive on a relatively open subset of the slice for \(d\ge2\) because both product cones are full-dimensional. Summing disjoint ordered pairs and dividing by \(V^2\) proves the claimed two-term expansion and positivity.

**4. Conditional convergence.** The exact rescaled rare-event sets differ in \(2d\)-volume by \(O_P(\varepsilon)\) from \(\Omega_{ab}\), as seen from their uniformly \(O(\varepsilon)\) displaced radial boundaries. Their normalized uniform densities therefore converge in total variation with error \(O_P(\varepsilon)\). The same volume estimates give pair probabilities proportional to \(k_{ab}+O_P(\varepsilon)\). The radial depth \(T=L_{ab}(U,W)\) under uniform measure on \(\Omega_{ab}\) satisfies \(\Pr(T\le t)=t^{2d}\) for \(0\le t\le1\), i.e. \(T\sim\operatorname{Beta}(2d,1)\). The square-distance expansion gives \((D-\|X-Y\|)/\varepsilon=T+O_P(\varepsilon)\) on the bounded region, proving the normalized-deficit law.

**5. Explicit orthotopes.** At every ordered opposite-vertex pair of \(B\), all tangent-cone rays are coordinate rays. Their depth coefficients are \(a_i/D\); hence each endpoint truncated cone volume is \(c_a(e)=D^d/(d!V)\), and there are exactly \(2^d\) ordered opposite pairs. The first coefficient follows. For a slice point, the \(2d\) normalized ray depths have the uniform simplex-slice distribution; their two depths in coordinate \(i\) sum to a variable \(T_i\), with \((T_1,\ldots,T_d)\sim\operatorname{Dirichlet}(2,\ldots,2)\). Consequently \(\mathbb E T_i^2=6/(2d(2d+1))=3/[d(2d+1)]\), and
\[
m_{ab}=D^2\sum_{i=1}^d\frac{\mathbb E T_i^2}{a_i^2}-1
=\frac{3D^2}{d(2d+1)}\sum_{i=1}^d a_i^{-2}-1.
\]
Substitution gives the box expansion. Finally, \(D^2=\sum_i a_i^2\ge d(\prod_i a_i^2)^{1/d}=dV^{2/d}\) with equality only when all sides are equal. This proves the sharp fixed-volume leading-coefficient minimum.

## Verification

A standalone reproducible script `check_diameter_cone.py` numerically compares the two-term orthotope prediction with an independently integrated exact rectangle-distance tail, independent conditional-simplex importance samples for rectangles and dimension-three/four cubes, and direct tangent-cone calculations for two triangles. It uses NumPy and SciPy and is run with `python check_diameter_cone.py` after installation of the dependencies in `requirements.txt`. Its deterministic completion marker is `POLYTOPE_DIAMETRAL_CONE_TWO_TERM_DIRICHLET_CHECKS_OK`. The exact-square-distance reduction and analytic beta/Dirichlet integrals are the proof; numerical tests are corroboration only, not exhaustive or independent validation.

## Relationship to prior work

Tong, Ahmadi and Pan (2013, arXiv:1312.2498) derive the marginal distribution of distance between two interior-uniform points in arbitrary triangles and related regions. Tong and Pan (2016, arXiv:1602.03407) give an algorithmic approach to marginal pair-distance distributions in arbitrary polygons; those formulas may also imply polygon-specific endpoint coefficients after expansion. The present theorem does **not** claim that the marginal polygon distance distribution itself is unknown. It treats all dimensions, expresses the first *two* endpoint coefficients directly through diametral vertex tangent cones, and determines the **conditional positions of the two extremal endpoints**, including universal Dirichlet laws and explicit box coefficients.

Jammalamadaka and Janson (2012, arXiv:1211.0822) study maximum pairwise distances among an increasing number of sampled spherically symmetric vectors. Their extreme-value problem differs from this fixed-two-point, bounded, possibly anisotropic polytope law. Earlier work on sample diameters such as Appel–Najim–Russo (2002) is also relevant. An earlier general theorem about local polyhedral extremes or a sufficiently comprehensive pair-distance formula might subsume a marginal portion; detailed historical priority requires further verification. Two close published research records concern short pair distances in polygons and difference-body *gauge* distances, neither the Euclidean near-diameter conditional endpoint law.

## Limitations

This is a self-contained mathematical derivation, not an externally audited publication. It assumes fixed polytope geometry and Euclidean norm, not smooth bodies, noncompact regions, degenerate polytopes, or a dimension varying with the deficit. The leading and next-order coefficients are given through finite-dimensional cone measures rather than elementary closed expressions for arbitrary nonsimple polytopes. The formula for the complete distance distribution is not asserted. Older marginal polygon-distance formulas may imply special cases of the marginal asymptotic; the joint conditional endpoint law and all-dimensional cone formulation are the intended distinction. Relevant inaccessible full texts, especially the 2016 arbitrary-polygon paper and earlier sample-diameter articles, leave a residual historical-priority risk. Independent mathematical validation has not been performed.

## References

1. S. R. Jammalamadaka and S. Janson, *Asymptotic distribution of the maximum interpoint distance in a sample of random vectors with a spherically symmetric distribution*, arXiv:1211.0822, first public posting 2012-11-05.
2. F. Tong, M. Ahmadi, and J. Pan, *Random Distances Associated with Arbitrary Triangles: A Systematic Approach between Two Random Points*, arXiv:1312.2498, first public posting 2013-11-29.
3. F. Tong and J. Pan, *Random Distances Associated with Arbitrary Polygons: An Algorithmic Approach between Two Random Points*, arXiv:1602.03407, first public posting 2016-01-21.
4. M. J. Appel, C. A. Najim, and R. P. Russo, *Limit laws for the diameter of a random point set*, Advances in Applied Probability **34** (2002), 1–10, doi:10.1239/aap/1019160946.
