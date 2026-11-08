# Gaussian proximity and sharp observable escape times near a planar invariant line

## Finding
For the smooth planar system
\[\dot x=-xy,\qquad \dot y=x-1\]
consider the observable \(v(x,y)=x\), whose speed is \(|\dot v|=|xy|\). Fix \(\eta\in\mathbb R\) and a positive threshold \(s\). Starting from \((x(0),y(0))=(\varepsilon,\eta)\), define the **first observable-speed exit**
\[\tau_s(\varepsilon,\eta)=\inf\{t\ge0:|\dot x(t)|>s\}.\]
Write \(L=\log(1/\varepsilon)\). For every fixed \(s>0\) and \(\eta\in\mathbb R\), as \(\varepsilon\downarrow0\),
\[\boxed{\tau_s(\varepsilon,\eta)=\eta+\sqrt{2L}+\frac{\eta^2+2\log s-\log(2L)}{2\sqrt{2L}}+O_{s,\eta}\!\left(\frac{(\log L)^2}{L^{3/2}}\right).}\]
The error is uniform when the threshold ranges in a compact positive interval and the initial vertical coordinate ranges in a compact interval. In particular, the slowness residence time diverges as \(\sqrt{2\log(1/\varepsilon)}\), not as the logarithm of inverse initial distance.

There is an equivalent, quantitative necessary proximity for an escape time \(\tau_s\). With \(Q=\tau_s-\eta\to\infty\),
\[\boxed{\varepsilon=\frac{s\,e^{\eta^2/2}}{Q}\exp(-Q^2/2)\bigl(1+O_{s,\eta}(Q^{-2})\bigr).}\]
Thus obtaining a prescribed long residence time requires **Gaussian-in-time closeness** to the invariant line \(x=0\), with a definite reciprocal-time prefactor.

## Assumptions and scope
The time variable is the original, unrescaled physical time. The system is defined on the half-plane \(x>0\), with a smooth extension to the invariant line \(x=0\). The speed threshold \(s\) is strictly positive and fixed as \(\varepsilon\downarrow0\). The vertical datum \(\eta\) is fixed, or varies in a fixed compact interval. The first-exit definition uses a *strict* inequality; by continuity its value is the first equality time. For sufficiently small \(\varepsilon\), the initial speed \(\varepsilon|\eta|\) is below \(s\).

## Proof
**1. First integral and location of the exit.** The smooth conserved energy for \(x>0\) is
\[H(x,y)=x-\log x+\frac{y^2}{2},\qquad \frac{dH}{dt}=0.\]
Initially \(H_\varepsilon=\varepsilon+L+\eta^2/2\). For all small enough \(\varepsilon\), the solution descends in \(y\) while \(x<1\). On the portion \(y>0\), \(xy\) is strictly decreasing because
\[\frac{d(xy)}{dt}=x(x-1-y^2)<0.\]
On the portion \(y<0\), the positive quantity \(-xy\) increases strictly, since
\[\frac{d(-xy)}{dt}=x(1+y^2-x)>0.\]
The energy level contains a small-\(x\) branch extending to negative values of \(y\), and this branch crosses \(-xy=s\) at a unique first exit for all sufficiently small \(\varepsilon\). Let \(y=-z<0\) and \(x=s/z<1\) there. Energy conservation gives the exact large-root equation
\[\frac{z^2}{2}+\log z+\frac{s}{z}=L+\frac{\eta^2}{2}+\log s+\varepsilon.\tag{1}\]
The large solution is unique for large \(L\): the left side is strictly increasing for \(z\) sufficiently large, and \(z\sim\sqrt{2L}\). The small-\(x\) branch stays below \(1\) until exit, establishing that this root corresponds to the *first* crossing.

**2. Exact time integral and boundary layer.** On the relevant energy branch, \(x\) is the unique solution in \((0,1)\) of
\[X(u)e^{-X(u)}=\exp(-H_\varepsilon+u^2/2),\quad
X(u)=-W_0\!\left(-e^{-H_\varepsilon+u^2/2}\right),\]
where \(W_0\) is the principal real Lambert branch. From \(\dot y=X(y)-1\), the exact first exit time is
\[\tau_s=\int_{-z}^{\eta}\frac{du}{1-X(u)}=z+\eta+\int_{-z}^{\eta}\frac{X(u)}{1-X(u)}\,du.\tag{2}\]
Equation (1) makes the integrand amenable to direct asymptotics: for \(-z\le u\le\eta\),
\[X(u)e^{-X(u)}=\frac{s}{z}e^{-s/z}\exp\!\left(\frac{u^2-z^2}{2}\right).\tag{3}\]
Uniformly for bounded \(s,\eta\) in the stated ranges, the only material contribution to the integral in (2) comes from the layer \(u=-z+r/z\), with \(r=O(1)\). There \(X(u)=(s/z)e^{-r}(1+O((1+r)^2/z))\) on bounded \(r\)-intervals. The transformed integrand admits a uniform integrable exponential majorant, for example after splitting at \(u=-z/2\); the remainder near bounded positive \(u\) is exponentially small in \(z^2\). It follows, including the quadratic correction from \(1/(1-X)\), that
\[\int_{-z}^{\eta}\frac{X(u)}{1-X(u)}\,du=\frac{s}{z^2}+O_{s,\eta}(z^{-3}).\tag{4}\]
This explicitly computes the physical-time retardation relative to the approximate speed \(\dot y=-1\).

**3. Matching the endpoint and time expansions.** Put \(R=\sqrt{2L}\). Expanding the unique large root of (1) yields
\[z=R+\frac{\eta^2+2\log s-2\log R}{2R}-\frac{s}{R^2}
+O_{s,\eta}\!\left(\frac{(\log R)^2}{R^3}\right).\tag{5}\]
Substituting (5) into (2)–(4), the term \(-s/R^2\) in the endpoint location *cancels* the leading physical-time correction \(+s/z^2\). This nontrivial cancellation gives the displayed escape-time law with error \(O((\log L)^2/L^{3/2})\).

**4. Gaussian inversion.** From (2)–(4), \(Q=\tau_s-\eta=z+s/z^2+O(z^{-3})\), so \(z=Q-s/Q^2+O(Q^{-3})\). Rewriting (1),
\[L=\frac{z^2}{2}+\log z+\frac{s}{z}-\frac{\eta^2}{2}-\log s-\varepsilon
=\frac{Q^2}{2}+\log Q-\frac{\eta^2}{2}-\log s+O_{s,\eta}(Q^{-2}).\]
The two terms of order \(Q^{-1}\) cancel once again. Exponentiation yields the stated Gaussian proximity law.

## Verification
The standalone `VERIFY_NUMERIC.py` integrates the transformed ODE in logarithmic \(x\)-coordinates, detects the first threshold crossing, and checks the independent energy root, time asymptotic, boundary-layer correction, and inverted proximity law. It verifies 24 parameter combinations with \(\eta\in\{-1,0,2\}\), \(s\in\{1/4,1\}\), \(L\in\{15,30,60,100\}\), and independently checks one time integral by direct quadrature. A successful execution prints `VERIFY_OK ODE_first_exits=24 root_conditions=24 Gaussian_log_inverse=24 independent_time_quadrature=1`. These finite calculations corroborate the asymptotic proof but do not establish its infinite-parameter conclusion by enumeration.

For orientation, at \(\eta=0\), \(s=1\), and \(L=100\), direct integration gives \(\tau_s\approx13.954565\), whereas the displayed asymptotic gives \(13.954812\).

## Relationship to prior work
Pasion and Magpantay's 2026 analysis introduces nonequilibrium transient centers and includes this precise planar flow as an example with observable \(x\). Its qualitative finite-exit criteria do not give the first-exit time, the logarithmic correction, or the necessary initial-distance law. Liu, Magpantay and Abdella's 2023 treatment discusses the same dynamical example and first integral, but classifies transient centers rather than establishing the quantified speed-threshold escape asymptotic. The related 2022 paper by Liu and Magpantay establishes a more general framework for transients; a complete comparison to that original text is limited by access. Standard conservative planar orbit-period estimates concern an entire energy-level circuit, not the first observable-speed crossing considered here. The derivation relies on elementary energy reduction followed by a boundary-layer estimate; neither the conserved integral nor the general notion of slow transients is claimed as new.

## Limitations
The result applies to this specific smooth integrable ODE, fixed positive observable-speed thresholds, and initial data approaching the invariant line with fixed/bounded \(\eta\). It does not apply automatically to general transient centers, arbitrary observables, stochastic perturbations, perturbations of the vector field, or varying thresholds that tend to zero. The stated error bounds are asymptotic, not uniform for arbitrarily large \(|\eta|\) or arbitrarily small \(s\). Independent validation and complete historical-priority certification have not been performed.

## References
1. A. Pasion and F. Magpantay, *Nonequilibrium Transient Centers in Continuous-Time Systems*, arXiv:2610.41930v1, first publicly submitted 2026-10-30. https://arxiv.org/abs/2610.41930.
2. A. Liu, F. M. G. Magpantay and K. Abdella, *A framework for long-lasting, slowly varying transient dynamics*, Mathematical Biosciences and Engineering 20 (2023), 12130–12153. DOI: 10.3934/mbe.2023540. https://doi.org/10.3934/mbe.2023540.
3. A. Liu and F. M. G. Magpantay, *A Quantification of Long Transient Dynamics*, SIAM Journal on Applied Mathematics 82 (2022), 381–407. DOI: 10.1137/20M1367131. https://doi.org/10.1137/20M1367131.
