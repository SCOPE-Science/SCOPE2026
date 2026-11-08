# Late spatial switching for inhomogeneous diffusion exit odds and its third-mode correction

## Finding

Consider a regular one-dimensional diffusion killed at two endpoints. The exact-time upper-versus-lower exit odds have a spatially nonincreasing logarithmic time derivative, for **every** positive time. At sufficiently late times this derivative has exactly one zero. That zero converges to the unique interior node of the second Dirichlet eigenfunction; its first displacement from that node is controlled by the third eigenvalue and the boundary spectral fluxes.

Precisely, let \(f_0(t,x)\) and \(f_a(t,x)\) be the joint densities for exiting at time \(t>0\) through the lower and upper endpoints. Put

\[
D(t,x)=\partial_t\log\frac{f_a(t,x)}{f_0(t,x)}.
\]

For every \(t>0\), the map \(x\mapsto D(t,x)\) is nonincreasing on \((0,a)\). In fact, for \(0<x<y<a\) and \(0<s<t\),

\[
f_0(s,x)f_0(t,y)\ge f_0(t,x)f_0(s,y),\qquad
f_a(s,y)f_a(t,x)\ge f_a(t,y)f_a(s,x).
\]

Choose the first three eigenfunctions \(\phi_j\) of the killed generator as specified below, and denote their eigenvalues by \(\lambda_1<\lambda_2<\lambda_3\). Define

\[
 c_{j,0}=\frac{\phi_j'(0)}{s'(0)},\quad
 c_{j,a}=-\frac{\phi_j'(a)}{s'(a)},\quad
 K_j=(\lambda_j-\lambda_1)
 \left(\frac{c_{j,0}}{c_{1,0}}-\frac{c_{j,a}}{c_{1,a}}\right)
 \quad (j=2,3).
\]

Here \(s'\) is the positive scale density, not a derivative in time. Orient \(\phi_1>0\) and \(\phi_2\) positive near zero, so \(K_2>0\). Let \(x_\star\) be the unique zero of \(\phi_2\). There is \(t_0<\infty\) such that for all \(t\ge t_0\), \(D(t,\cdot)\) has exactly one zero \(x_t\), and

\[
 \boxed{\displaystyle
 x_t=x_\star-
 \frac{K_3\phi_3(x_\star)}{K_2\phi_2'(x_\star)}
 e^{-(\lambda_3-\lambda_2)t}
 +o\bigl(e^{-(\lambda_3-\lambda_2)t}\bigr).}
\]

This includes the case where the displayed coefficient vanishes, in which case the remainder is genuinely little-oh; no assertion of a nonzero leading displacement is then made. At each fixed \(x\ne x_\star\), the late-time sign of \(D(t,x)\) is the sign of \(\phi_2(x)\).

## Assumptions and scope

Fix \(a>0\). Let the diffusion solve

\[
 dX_t=b(X_t)\,dt+\sigma(X_t)\,dW_t
\]

in \((0,a)\) and be absorbed at the first hit of either endpoint. Assume \(b,\sigma\in C^4([0,a])\) and \(\inf_{[0,a]}\sigma>0\). All statements concern each such fixed regular diffusion, initial point \(x\in(0,a)\), and actual elapsed time \(t>0\). Write \(A=\sigma^2/2\) and define the scale density and speed density by

\[
 s'(x)=\exp\left(-\int_0^x\frac{b(u)}{A(u)}\,du\right),\qquad
 m(x)=\frac1{A(x)s'(x)}.
\]

Then \(L=A\partial_{xx}+b\partial_x=(1/m)\partial_x[(1/s')\partial_x]\), with Dirichlet boundaries. Let \(-L\phi_j=\lambda_j\phi_j\) and normalize \(\int_0^a\phi_j\phi_k m\,dx=\delta_{jk}\). The spectrum is positive, discrete and simple. Sturm oscillation gives a single simple zero for \(\phi_2\) and no zeros for \(\phi_1\). The third eigenfunction need not be symmetric. No uniform estimates over arbitrary families of coefficients are asserted.

## Proof

**1. Strict two-time inequalities from path swapping.** Start two independent, identically governed absorbed diffusions at \(x<y\). Select two disjoint small exit-time intervals with the first lying before the second. On the event that the process from \(y\) exits at zero in the first interval while the process from \(x\) exits at zero in the second, continuity forces their paths to meet before the first exit. At their first meeting, interchange their future paths. The strong Markov property and independence make this path-tail interchange measure-preserving, and it is injective into the event with the two exit times reversed. It follows by shrinking the two intervals and using smooth positivity of the exit-time densities that

\[
 f_0(s,x)f_0(t,y)\ge f_0(t,x)f_0(s,y),\quad s<t.
\]

Reflect the spatial order for upper exits to obtain the second displayed inequality. Notice that an unconditioned, synchronous discrete walk need not enjoy this path-crossing argument; continuity and independent diffusion increments are essential.

**2. Spatial switching at every time.** Divide the inequalities by the positive factors. For \(s<t\), the quotient \(f_0(t,z)/f_0(s,z)\) is nondecreasing in \(z\), whereas \(f_a(t,z)/f_a(s,z)\) is nonincreasing. Letting \(s\uparrow t\), the smooth time logarithmic derivative of the lower channel is spatially nondecreasing and that of the upper channel is nonincreasing. Their difference \(D(t,\cdot)\) is therefore nonincreasing. This does not claim a single temporal sign reversal at any fixed starting point.

**3. Flux spectral expansion.** The Dirichlet transition density relative to speed measure is

\[
 p(t,x,y)=\sum_{j\ge1}e^{-\lambda_jt}\phi_j(x)\phi_j(y).
\]

The absorbing boundary currents give, for \(e\in\{0,a\}\),

\[
 f_e(t,x)=\sum_{j\ge1}c_{j,e}\phi_j(x)e^{-\lambda_jt}.
\]

At every positive time the series, its time derivative, and the needed interior spatial derivatives converge locally uniformly (standard regular Sturm–Liouville heat-kernel estimates). Positivity of \(\phi_1\) implies \(c_{1,0},c_{1,a}>0\). With \(\phi_2\) positive near zero, the Hopf boundary signs imply \(c_{2,0}>0>c_{2,a}\), hence \(K_2>0\).

**4. Late spatial switch.** Set \(\Delta_j=\lambda_j-\lambda_1\). Expanding the logarithms of the positive boundary densities yields, locally in \(C^1\) over interior \(x\)-intervals,

\[
 D(t,x)=K_2\frac{\phi_2(x)}{\phi_1(x)}e^{-\Delta_2t}+o(e^{-\Delta_2t}).
\]

The simple node \(x_\star\) of \(\phi_2\) has \(\phi_2'(x_\star)<0\). For sufficiently large \(t\), \(D\) has opposite signs on either side of a small neighborhood of \(x_\star\) and a strictly negative spatial derivative within that neighborhood. Spatial nonincrease from Step 2 excludes any additional zero outside it. Thus a unique \(x_t\) exists and \(x_t\to x_\star\).

**5. Quantified switch displacement.** At the node, the second-mode contribution to both channel densities vanishes exactly. Consequently,

\[
 D(t,x_\star)=K_3\frac{\phi_3(x_\star)}{\phi_1(x_\star)}e^{-\Delta_3t}
 +o(e^{-\Delta_3t}),
\]

while

\[
 \partial_xD(t,x_\star)=K_2\frac{\phi_2'(x_\star)}{\phi_1(x_\star)}e^{-\Delta_2t}
 +o(e^{-\Delta_2t}).
\]

The mean-value theorem at the unique zero first gives \(|x_t-x_\star|=O(e^{-(\Delta_3-\Delta_2)t})\), since the derivative is uniformly comparable to the displayed leading term near the node. A second application and continuity of the normalized derivative give the boxed expansion. Nonlinear second-mode terms do not introduce an earlier correction at the node because they carry a factor \(\phi_2(x_\star)=0\).

## Verification

The independent standalone script `verify.py` checks exact rational same-parity finite-chain two-time determinant inequalities (a lattice control), then numerically diagonalizes several reversible tridiagonal approximations of the nonsymmetric diffusion \(dX_t=2X_t^2dt+dW_t\) on \((0,1)\). It checks numerical spatial nonincrease of \(D\), the uniqueness of a late switching zero on the mesh, and consistency of the predicted third-mode displacement against directly computed boundary currents. Run `python verify.py` with NumPy and SciPy installed. Its finite calculations cannot prove the continuum assertions, which rest on the preceding path-swap and Sturm–Liouville arguments.

## Relationship to prior work

Newton and Vega Coso (2026, arXiv:2611.01756, Sections 7, 9, 10.3) prove finite birth–death switching and constant-coefficient drifted Brownian results and explicitly propose the general-diffusion switching point at the second Dirichlet eigenfunction node as an open problem. The theorem above establishes that proposed result for uniformly elliptic smooth inhomogeneous coefficients and additionally identifies the third-eigenmode exponential displacement of the moving zero. Classical Karlin–McGregor total positivity underlies related first-passage comparisons; Evans and Williams (1998) establish variation-diminishing properties of diffusion transition operators. None of these inspected accessible statements supplies the displayed general-diffusion switch displacement formula. This is a literature-relative, not a definitive historical-priority, assessment.

## Limitations

The exit-time densities refer to an absorbing, time-homogeneous, scalar, uniformly elliptic diffusion on a compact interval. The statement does not cover degenerate endpoints, jumps, nonlocal resets, or higher-dimensional diffusions. It does not assert that each fixed point undergoes only one temporal reversal, nor a global-in-time unique switch. If the third-mode coefficient vanishes, a higher-mode calculation is required to find the first nonzero displacement. Classical early literature on total positivity could contain related implicit statements; a full historical-priority determination remains open. No independent validation has been performed.

## References

1. T. Newton and J. A. Vega Coso, *Stochastic Orders of the Exit Pair and the Monotone Response to Resetting*, arXiv:2611.01756 (first public version 2026-11-01), https://arxiv.org/html/2611.01756v1 ; Sections 7, 9, 10.3.
2. S. Karlin and J. McGregor, *Classical Diffusion Processes and Total Positivity* (Stanford technical report, 1960), https://statistics.stanford.edu/technical-reports/classical-diffusion-processes-and-total-positivity .
3. S. N. Evans and R. J. Williams, *Transition Operators of Diffusions Reduce Zero-Crossing*, technical report 507 (1998), https://live-statistics.pantheon.berkeley.edu/sites/default/files/tech-reports/507.pdf .
