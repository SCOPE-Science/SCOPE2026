# A Dirichlet corner law for tiny random sections of orthotopes

## Finding

Let \(B=\prod_{i=1}^d[-a_i/2,a_i/2]\subset\mathbb R^d\), where \(d\ge2\) is an integer and every \(a_i>0\). Sample an affine hyperplane from the Euclidean-motion-invariant measure on unoriented hyperplanes, conditioned to intersect \(B\), and let \(X\) be its \((d-1)\)-dimensional intersection volume. Put \(\alpha=1/(d-1)\). Then, as \(t\downarrow0\),

\[
\Pr\{X\le t\}=\frac{\kappa_d}{\sum_{i=1}^d a_i}\,t^\alpha+o(t^\alpha),\qquad
\kappa_d=\frac{2((d-1)!)^\alpha\Gamma((d+1)/2)\Gamma(d/(2(d-1)))^d}{\pi^{(d-1)/2}\Gamma(d^2/(2(d-1)))}.
\]

Define the *contact vertex* as the unique box vertex exposed by the supporting hyperplane at the nearer endpoint of the sampled plane's admissible offset interval; an arbitrary convention on ties, a null event, does not affect the law. Conditional on \(X\le t\), the vector of squared unit-normal coordinates converges weakly to

\[
(U_1^2,\ldots,U_d^2)\ \Longrightarrow\ \operatorname{Dirichlet}\left(\frac d{2(d-1)},\ldots,\frac d{2(d-1)}\right).
\]

Jointly, the contact vertex becomes uniform over the \(2^d\) vertices and is independent of those squared coordinates; independently of both, \(X/t\) converges to \(\operatorname{Beta}(\alpha,1)\), with cumulative law \(\Pr\{X/t\le z\mid X\le t\}\to z^\alpha\) for \(0\le z\le1\). Conditional on the rare event, the section is simplicial with probability tending to one.

At fixed \(d\)-volume \(V=\prod a_i\), the leading coefficient is largest exactly when \(a_1=\cdots=a_d=V^{1/d}\), by strict arithmetic–geometric mean. At a prescribed \(\sum a_i\), the coefficient is identical for all shapes. For \(d=3\) and the unit cube, the coefficient is approximately \(0.487409686447428\); for \(d=2\) it is \(1/(a_1+a_2)\).

## Assumptions and scope

The hyperplane law is **not** the one obtained by first sampling a uniform direction and then uniformly choosing an offset along that direction: its density before conditioning is the product of spherical area measure and Lebesgue measure in the signed offset. Normalize an unoriented plane by using the hemisphere \(S^{d-1}_+=\{u\in S^{d-1}:u_d\ge0\}\), disregarding its null equator; with \(H(u,s)=\{x:\langle x,u\rangle=s\}\), the law is

\[
\Pr\{(u,s)\in E\}=\frac1Z\int_{S^{d-1}_+}\int_{-w(u)/2}^{w(u)/2}\mathbf1_E(u,s)\,ds\,d\sigma(u),
\quad w(u)=\sum_{i=1}^d a_i|u_i|,
\quad Z=\int_{S^{d-1}_+}w(u)\,d\sigma(u).
\]

The volume of a measure-zero tangent section is defined as zero. The reference to a contact vertex concerns the adjacent exposed supporting plane, not the actual intersection vertices. No claim of a finite-threshold identity for \(t>0\) is made.

## Proof

**1. Exact simplex near a generic supporting vertex.** Fix a direction with every \(u_i\ne0\). At either extremal offset the exposed face is a single vertex. Measure inward offset depth \(h\ge0\) from that support plane. After reflecting and translating individual coordinates, near that vertex the portion of the box is the orthant \(x_i\ge0\), while the section plane becomes \(\sum_i|u_i|x_i=h\). Whenever \(h<\min_i(a_i|u_i|)\), the section is exactly a simplex with intercepts \(h/|u_i|\). The volume of the cone cut off from the vertex is \(h^d/(d!\prod_i|u_i|)\). The cone's perpendicular height is \(h\), hence its base \((d-1)\)-volume is

\[
A(h,u)=\frac{h^{d-1}}{(d-1)!\prod_{i=1}^d|u_i|}.
\tag{1}
\]

For each fixed generic direction and all sufficiently small \(t\), precisely one small-section interval occurs near each of its two supporting vertices. Each has length

\[
h_t(u)=\left((d-1)!\,t\prod_{i=1}^d|u_i|\right)^\alpha.
\tag{2}
\]

Indeed, convexity and symmetry of the box imply that the section-volume power \(A(s,u)^\alpha\) is even and concave in \(s\), hence increases from either support endpoint toward the center. Therefore there is no additional interior small-section interval.

**2. Uniform domination for angular integration.** Let \(r=\tfrac12\min_i a_i>0\) and \(W=(\sum_i a_i^2)^{1/2}\). The centered ball \(rB_2^d\) lies inside \(B\), so every centered section has \((d-1)\)-volume at least \(\omega_{d-1}r^{d-1}\), with \(\omega_{d-1}\) the unit \((d-1)\)-ball volume. Brunn's concavity theorem says \(s\mapsto A(s,u)^\alpha\) is concave. If \(h\) is inward distance from a support plane on either half of the offset interval, concavity on the segment to the center gives

\[
A(h,u)^\alpha\ge\frac{2h}{w(u)}\omega_{d-1}^\alpha r\,.
\]

Thus \(A(h,u)\le t\) implies \(h\le Wt^\alpha/(2\omega_{d-1}^\alpha r)\), uniformly in \(u\). Hence the **total** admissible small-section offset length, divided by \(t^\alpha\), is bounded by a finite box-dependent constant. Combining this bound with (2), dominated convergence applies to the spherical area integral, despite the coordinate great circles on which the exposed face is not a vertex.

**3. Exact normalizations and the sharp constant.** Let \(T_t(u)\) denote the total offset length for which \(X\le t\). By Steps 1–2,

\[
\lim_{t\downarrow0}\frac{T_t(u)}{t^\alpha}=2((d-1)!)^\alpha\prod_i|u_i|^\alpha\quad\text{for almost all }u,
\]

and integration of both sides is justified. Standard sphere beta integrals give

\[
\int_{S^{d-1}_+}\prod_i|u_i|^\alpha\,d\sigma(u)=\frac{\Gamma((1+\alpha)/2)^d}{\Gamma(d(1+\alpha)/2)},
\qquad
\int_{S^{d-1}_+}|u_j|\,d\sigma(u)=\frac{\pi^{(d-1)/2}}{\Gamma((d+1)/2)}.
\]

The latter identity gives \(Z=\pi^{(d-1)/2}(\sum_i a_i)/\Gamma((d+1)/2)\). Divide the integrated first limit by \(Z\), substitute \((1+\alpha)/2=d/[2(d-1)]\), and obtain exactly the asserted \(\kappa_d\).

**4. Joint conditional marks.** The same dominated-convergence argument works with any bounded continuous test function of the normal, the endpoint sign, and \(A(h,u)/t\). For a generic fixed \(u\), (1)–(2) give the exact change of variables \(h=h_t(u)v\), \(0\le v\le1\), and \(A(h,u)/t=v^{d-1}\). Thus the conditional radial mark has distribution function \(z^\alpha\), independent of the normal. The two endpoint intervals have identical asymptotic lengths. Symmetry under sign changes of the normal and of the supporting side makes the contact vertex uniform on the box vertices, independent of the absolute normal coordinates. Finally, a uniform spherical normal has squared-coordinate distribution \(\operatorname{Dirichlet}(1/2,\ldots,1/2)\). Conditioning the rare event reweights its density by \(\prod_i|u_i|^\alpha=\prod_i(U_i^2)^{\alpha/2}\); therefore the squared-coordinate Dirichlet parameters become \((1+\alpha)/2=d/[2(d-1)]\). This establishes the joint weak convergence and independence. At each generic normal the section is a simplex throughout the sufficiently short endpoint intervals, and the dominated-convergence bound makes the nonsimplicial conditional fraction tend to zero.

**5. Shape extremality.** The constant \(\kappa_d\) depends only on dimension. For fixed \(\prod_i a_i=V\), the strict arithmetic–geometric mean inequality gives \(\sum_i a_i\ge dV^{1/d}\), with equality only for the cube. Invert this sum in the coefficient from Step 3. At fixed side-length sum the coefficient does not vary.

## Verification

A standalone script, `verify.py`, checks the closed gamma expression (including the planar limiting value), the side-length dependence, and the cube numerical coefficient for dimensions 2 through 8. For spatial boxes with side vectors \((1,1,1)\) and \((1,2,3)\), it separately computes the section-area distribution using the inclusion–exclusion formula for a box slice, quasi-Monte Carlo spherical quadrature, and bisection on the offset. It compares small-threshold cumulative probabilities to the theorem and checks weighted angular moments against the Dirichlet predictions in dimensions three and four. This computation supplements rather than establishes the infinite theorem, which follows from the proof above.

Reproduce with a recent Python 3 installation supplying NumPy, SciPy and mpmath: `python verify.py`. All thresholds, numerical tolerances and random seeds are in the script. The script outputs `PASS` on successful completion.

## Relationship to prior work

Van der Jagt, Jongbloed and Vittorietti (first public arXiv version May 4, 2023) introduce precisely the isotropic uniformly random hyperplane model used here and prove general absolute continuity of section-volume distributions, with simulations for the cube and other polytopes. Their Section 5 observes possible inverse-square-root behavior in three-dimensional section-area densities, but supplies no exact coefficient for orthotopes, no universal conditional Dirichlet direction law, and no fixed-volume box optimization. Their work is not claimed to be new here.

Paul (1981) reports computer-generated distributions of cross-sectional areas for polyhedra, including the cube, according to the accessible abstract; its complete text was not available for examination, so possible earlier equivalent endpoint computations remain a priority limitation. Coleman (1981) studies random *line* intercepts through three-dimensional boxes, not hyperplane *area* sections. Other work on central (offset-zero) cube sections, section *polygon types*, and projected shadow volumes concerns different random variables or sampling laws. The planar \(d=2\) chord-length situation is classical; the contribution here is the complete all-dimensional sharp coefficient and marked limit, particularly in \(d\ge3\).

## Limitations

The law is asymptotic as \(t\downarrow0\) at fixed dimension and fixed positive side lengths; no uniform bound over degenerating boxes or dimensions is claimed. It concerns isotropic **affine** sections conditioned on hitting a box, not a fixed central plane, a fixed uniform orientation, or independently sampled directions and offsets. The numerical verifier covers finitely many cases only. The 1981 full text and unindexed literature may contain historical overlap. Neither a general exact finite-threshold density nor an optimal error term is derived.

## References

1. T. van der Jagt, G. Jongbloed, M. Vittorietti, *Existence and approximation of densities of chord length- and cross section area distributions*, first public preprint May 4, 2023, https://arxiv.org/abs/2305.02864; *Image Analysis & Stereology* 42 (2023), 171–184, https://doi.org/10.5566/ias.2923.
2. J. L. Paul, *Distribution curves of sectional areas through some families of convex particles*, *Journal of Microscopy* 122 (1981), 165–172, https://doi.org/10.1111/j.1365-2818.1981.tb01255.x (abstract examined; full text unavailable).
3. R. Coleman, *Intercept lengths of random probes through boxes*, *Journal of Applied Probability* 18 (1981), 276–282, https://doi.org/10.2307/3213189 (abstract examined).
