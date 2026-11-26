# A product-form stationary law and exact shape optimum for cardinal-heading active particles in rectangular boxes

## Finding
Consider a single athermal particle confined by hard walls to a rectangular box in dimension \(d\geq2\). At any instant it propels along exactly **one** Cartesian axis; at independent Poisson times it redraws an axis and a fair sign. Although all coordinates are dynamically coupled through the exclusive choice of active axis, their **entire joint stationary positional measure factorizes**. In particular, all stationary spatial mixed cumulants vanish, and every face, edge, and corner mass is exactly calculable. The positional law does not depend on how often each axis is selected, provided every selection probability is positive.

More precisely, introduce \(\ell_i=2v_i/\gamma\) and the finite measures on \([0,L_i]\)
\[
\mu_i=\frac{dx_i+(\ell_i/2)(\delta_0+\delta_{L_i})}{L_i+\ell_i},\qquad
\nu_i^+=\frac{dx_i+\ell_i\delta_{L_i}}{L_i+\ell_i},\qquad
\nu_i^-=\frac{dx_i+\ell_i\delta_0}{L_i+\ell_i}.
\]
Here \(dx_i\) is Lebesgue measure on the open interval, and each displayed measure has total mass one. If \(H\in\{\pm e_1,\ldots,\pm e_d\}\) is the heading, the **unique stationary probability measure** is
\[
\boxed{\ \pi(dx,H=\pm e_i)=\frac{w_i}{2}\nu_i^\pm(dx_i)\bigotimes_{j\ne i}\mu_j(dx_j).\ }
\]
Consequently \(\pi_X=\bigotimes_{i=1}^d\mu_i\) regardless of the positive axis weights \(w_i\). Each prescribed collection of upper/lower walls, indexed by \(I\subseteq\{1,\ldots,d\}\), has simultaneous stationary mass \(\prod_{i\in I}\ell_i/[2(L_i+\ell_i)]\).

For \(N\) noninteracting copies of friction coefficient \(\zeta>0\), define \(D_i=w_iv_i^2/\gamma\), the free-space active diffusivity along axis \(i\), and \(V=\prod_iL_i\). The stationary propulsion force per unit area on either face normal to axis \(i\) is exactly
\[
\boxed{\ P_i=\frac{N\zeta D_i}{V}\frac{L_i}{L_i+\ell_i}.\ }
\]
For a quasistatic change of the box lengths at fixed \(v_i,\gamma,w_i,\zeta,N\), the mean mechanical expansion work \(\sum_iP_i(V/L_i)dL_i\) is the exact differential of
\[
\Phi(L)=N\zeta\sum_iD_i\log\!\left(\frac{L_i+\ell_i}{L_{\mathrm{ref}}}\right),
\]
where \(L_{\mathrm{ref}}>0\) is any reference length. At each prescribed positive volume \(V_0\), this potential has **exactly one** global minimizer, characterized by
\[
\frac{D_iL_i}{L_i+\ell_i}=\lambda,\qquad
L_i=\frac{\ell_i\lambda}{D_i-\lambda},\qquad
\prod_iL_i=V_0,\qquad 0<\lambda<\min_iD_i.
\]
These last statements are consequences of the same stationary product law, not independent findings.

## Assumptions and scope
Let \(d\geq2\) be an integer. Let all lengths \(L_i\), axis propulsion speeds \(v_i\), redraw rate \(\gamma\), and selection probabilities \(w_i\) be strictly positive, with \(\sum_iw_i=1\). The state is \((X,H)\) in \(\prod_i[0,L_i]\times\{\pm e_i\}_{i=1}^d\). At rate \(\gamma\), independent of the current state, the heading is redrawn from \(\Pr(H=+e_i)=\Pr(H=-e_i)=w_i/2\); redrawing the same heading is allowed. Between redraws, only \(X_i\) moves, with signed speed \(\pm v_i\), and its position is clipped to \([0,L_i]\), so an outward-pointing heading at a hard face holds the particle there until the heading changes. There is no translational thermal noise or particle interaction. The constant \(N\) pertains only to an independent ideal gas of copies, not an exclusion gas. Pressures are the mechanical forces from stalled outward propulsion divided by geometric face area. All stationary claims concern this specified discrete-cardinal heading law, not the continuously distributed orientation model.

## Proof
**1. Generator and boundary flux.** For a continuously differentiable family of test functions \(f_{i,\pm}(x)=f(x,\pm e_i)\), the Markov generator is
\[
\mathcal L f(x,\pm e_i)=b_{i,\pm}(x)\partial_if_{i,\pm}(x)
+\gamma\Big(\sum_{j=1}^d\frac{w_j}{2}[f_{j,+}(x)+f_{j,-}(x)]-f_{i,\pm}(x)\Big),
\]
where \(b_{i,+}\) equals \(v_i\) except at the upper wall where it is zero, and \(b_{i,-}\) equals \(-v_i\) except at the lower wall where it is zero. (The formula is interpreted through the deterministic clipped-flow generator on its standard differentiable core.) For each coordinate and each test \(g\), integrating the transport against the proposed \(\nu_i^\pm\) gives
\[
\int b_{i,+}g'\,d\nu_i^+=\frac{v_i[g(L_i)-g(0)]}{L_i+\ell_i},\qquad
\int b_{i,-}g'\,d\nu_i^-=\frac{-v_i[g(L_i)-g(0)]}{L_i+\ell_i}.
\]
The outward wall atom contributes no derivative. Independently,
\[
\gamma\int g\,d(\mu_i-\nu_i^\pm)
=\mp\frac{\gamma\ell_i}{2(L_i+\ell_i)}[g(L_i)-g(0)]
=\mp\frac{v_i[g(L_i)-g(0)]}{L_i+\ell_i}.
\]
Since the positional marginal of the proposed measure is \(\mu=\bigotimes_j\mu_j\), the incoming redraw term for heading \(\pm e_i\) is \(\gamma(w_i/2)\mu\); the outgoing term is \(\gamma(w_i/2)\nu_i^\pm\otimes_{j\ne i}\mu_j\). The displayed transport and redraw terms therefore cancel *for every heading-dependent test function*. This establishes weak stationarity of \(\pi\) including the singular wall and corner strata. Summing over headings gives the product positional law because \((\nu_i^++\nu_i^-)/2=\mu_i\) and \(\sum_iw_i=1\).

**2. Uniqueness.** In a fixed finite time, enforce a positive-probability event in which a redraw selects \(+e_1\), followed after longer than \(L_1/v_1\) by \(+e_2\), and so on through \(+e_d\), with each successive run longer than \(L_i/v_i\), and with no further redraw until the deterministic observation time. Choose small nonoverlapping event-time windows and sufficiently large gaps. The probability of this event is strictly positive and independent of the starting position or heading. On the event the final state is the single upper corner with final heading \(+e_d\), regardless of the starting state. Thus a fixed-time transition kernel satisfies a uniform minorization by a common point mass. The standard Doeblin contraction shows that the invariant distribution is unique (indeed convergence is uniformly geometric on a sufficiently long time grid).

**3. Wall probabilities and pressure.** For the right wall normal to coordinate \(i\), a propulsion force exists exactly on \(\{H=+e_i,X_i=L_i\}\), whose stationary probability is \((w_i/2)\ell_i/(L_i+\ell_i)\). Its microscopic outward force is \(\zeta v_i\). Multiplying by \(N\), dividing by face area \(V/L_i\), and using \(\ell_i=2v_i/\gamma\) gives the formula for \(P_i\). Left and right pressures are equal by sign symmetry. The unconfined velocity autocorrelation along axis \(i\) is \(w_iv_i^2e^{-\gamma t}\), so \(D_i=\int_0^\infty w_iv_i^2e^{-\gamma t}dt=w_iv_i^2/\gamma\), consistent with the stated normalization.

**4. Work and unique optimal shape.** Since \(P_iV/L_i=N\zeta D_i/(L_i+\ell_i)\), the work one-form is \(N\zeta\sum_iD_i\,d\log(L_i+\ell_i)=d\Phi\). Fix \(\prod_iL_i=V_0\) and set \(y_i=\log L_i\). The constraint becomes \(\sum_iy_i=\log V_0\), while the Hessian of \(\Phi/(N\zeta)\) in these coordinates is diagonal with entries \(D_i\ell_i e^{y_i}/(e^{y_i}+\ell_i)^2>0\). Restricted to the volume hyperplane, strict convexity holds; the objective grows without bound along every unbounded sequence there, because some coordinate must tend to \(+\infty\) when another tends to \(-\infty\). Therefore a unique global minimizer exists. A Lagrange multiplier yields \(D_iL_i/(L_i+\ell_i)=\lambda\). The product of \(\ell_i\lambda/(D_i-\lambda)\) increases continuously and strictly from zero to infinity as \(\lambda\uparrow\min_iD_i\), yielding exactly one solution for every \(V_0>0\).

## Verification
The accompanying standalone `verify.py` checks 80 distinct heading-dependent polynomial test-function generator identities exactly over rational numbers (dimensions two and three, all monomial exponents zero through three), checks both pressure normalizations, performs two independent event-driven long-run simulations with different orientation-selection weights, and numerically solves a three-dimensional fixed-volume stationarity system. Every program assertion passed on Python 3. The exact-rational generator tests illustrate the proof but do not replace the all-dimensional symbolic cancellation above; simulations are finite checks rather than infinite-time proofs. Run `python verify.py` using the standard library.

## Relationship to prior work
Li, Eichhorn and Dabelow (arXiv:2610.01287, first available October 1, 2026) derive a finite-box active ideal-gas law, exact for one-dimensional run-and-tumble motion, and approximate or numerical in higher dimensions with headings uniformly drawn from the continuum unit sphere. Their main text (Model, Steady-state solution, Ideal gas law, Thermodynamic processes) explicitly distinguishes independent AOUP coordinates from generally coupled multidimensional RTP coordinates. The result here concerns the separate, deliberately **discrete cardinal orientation law** (and zero thermal noise); the full higher-dimensional stationary position measure is exact and surprisingly factorized despite one-axis-at-a-time movement. It is neither an extension to the spherical-headings model nor a correction to that paper's results.

Frydel (arXiv:2410.06393) develops stationary slit distributions and wall forces for RTP orientations, including the familiar one-dimensional uniform bulk plus wall-atom law. That one-dimensional ingredient is prior mathematics. Product stationarity for a full rectangular box with exclusive axis choices and the arbitrary-weight invisibility are *not* the one-dimensional slit statement; they require checking the common-heading redraw generator across all coordinates. Published studies of sticky-wall fluctuations and confined four-heading longitudinal dispersion concern temporal covariance or diffusion in a slit rather than the full multidimensional box invariant law. The derivation itself is elementary once the invariant-measure ansatz is found; unindexed general random-scan product-invariance results may cover this specialization and are a priority for independent literature review.

## Limitations
The direction law is a finite set of coordinate-axis orientations, not an isotropic continuous-sphere law (even when weights are equal). The positions are independent at **one stationary time**; no claim is made of independent coordinate trajectories or of orientation-position independence. The model excludes translational thermal diffusion, soft walls, wall-induced turning, interactions, and non-Poisson residence times. Each \(w_i\) must be positive for uniqueness. Mechanical quasistatic work presumes slow shape changes at fixed microscopic parameters, and its exactness is not a claim of thermodynamic reversibility or total entropy-production neutrality. The unique-shape statement is for minimizing the specified work potential at fixed geometric volume, not optimizing power or arbitrary energetic functionals. Potential prior implicit coverage through general Markov process product-form theorems remains a publication-priority risk; independent external validation has not been performed.

## References
1. S. Li, R. Eichhorn, and L. Dabelow, *Ideal gas of active particles in a box*, arXiv:2610.01287 (first submitted 2026-10-01), https://arxiv.org/abs/2610.01287 . Relevant main-text sections: Model, Steady-state solution, Ideal gas law, Thermodynamic processes.
2. D. Frydel, *Run-and-tumble particles in slit geometry as a splitting probability problem*, arXiv:2410.06393 (first submitted 2024-10-08), https://arxiv.org/html/2410.06393v1 . Relevant sections: II, III, VI.
