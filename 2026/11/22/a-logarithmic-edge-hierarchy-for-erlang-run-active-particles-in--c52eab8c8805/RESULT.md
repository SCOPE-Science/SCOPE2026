# A logarithmic edge hierarchy for Erlang-run active particles in a harmonic trap

## Finding
Consider a one-dimensional, athermal, harmonically confined particle with dimensionless position \(X\in[-1,1]\) and dynamics
\[
\dot X(t)=-\kappa X(t)+\kappa\sigma(t),\qquad \kappa>0,
\]
where \(\sigma(t)\in\{-1,+1\}\) flips sign after independent \(\operatorname{Gamma}(m,\lambda)\) run durations, with integer shape \(m\geq2\) and rate \(\lambda>0\). A Gamma shape/rate convention is used: each run is the sum of \(m\) independent exponential waiting times of rate \(\lambda\). Set \(\beta=\lambda/\kappa\). In the unique stationary law, there is a finite positive constant \(C_{m,\beta}\) such that
\[
\boxed{\lim_{\varepsilon\downarrow0}\frac{\mathbb P(X>1-\varepsilon)}{\varepsilon^{\beta}[\log(1/\varepsilon)]^{m-1}}
=C_{m,\beta}:=\frac{\beta^{m-1}}{2m(m-1)!}\,\mathbb E[Z^{-\beta}]\in(0,\infty).}
\]
Here \(Z\in(0,2)\) is uniquely characterized by the stationary perpetuity
\[
Z\stackrel{d}{=}2(1-B)+BCZ',\qquad
B=e^{-\kappa T_-},\quad C=e^{-\kappa T_+},
\]
where \(T_-\) and \(T_+\) are independent \(\operatorname{Gamma}(m,\lambda)\), and \(Z'\) is an independent copy of \(Z\). Symmetry gives the same probability at the left edge.

For any fixed mean run duration \(\tau>0\), taking \(\lambda=m/\tau\) implies a strict asymptotic hierarchy: if \(2\leq m<n\) are integers, then
\[
\lim_{\varepsilon\downarrow0}
\frac{\mathbb P_{n}(X>1-\varepsilon)}{\mathbb P_{m}(X>1-\varepsilon)}=0.
\]
Consequently an Erlang phase count is detectable in rare wall-adjacent occupancy even if the mean run time and propulsion/trap parameters are fixed. The shape \(m=1\) gives the classical exponential-run edge power without the logarithmic multiplier and is a consistency boundary, not a novelty claim.

## Assumptions and scope
All runs are independent, have the same integer Gamma shape \(m\geq2\) and rate \(\lambda>0\), and force a reversal of orientation. The trap relaxation \(\kappa\) is positive and no translational Brownian noise is present. The stationary law is taken after the alternating renewal process has reached its equilibrium-age distribution. A physical model \(\dot x=-\kappa x+v\sigma\) with \(v>0\) is converted to the stated model by \(X=\kappa x/v\); its support is \([-v/\kappa,v/\kappa]\). The theorem concerns fixed \(m,\kappa,\lambda\) followed by the edge limit; no simultaneous limit in shape or rate is claimed.

## Proof
**1. Stationary starting position.** At the start of a positive run define its right-edge deficit \(Z=1-Y\), where \(Y\) is the position. During a positive run of duration \(T_+\), the deficit contracts to \(CZ\), with \(C=e^{-\kappa T_+}\). During the following negative run of duration \(T_-\), its value at the next positive start is
\[
Z_{\mathrm{next}}=2(1-B)+BCZ,\qquad B=e^{-\kappa T_-}.
\]
The independent positive inter-run times make this a strict iterated random affine contraction. Since \(0<BC<1\), \(\mathbb E|\log(BC)|=2m\kappa/\lambda<\infty\) and \(\mathbb E\log(BC)<0\), iteration from any \(Z\in[0,2]\) converges to one law. Its stationary solution is in \((0,2)\), and the alternating renewal process (finite mean run durations) supplies a unique invariant time-stationary law.

**2. Critical inverse entrance moment.** We prove \(\mathbb E Z^{-\beta}<\infty\), rather than assuming it. Write \(U=2(1-B)>0\) and \(V=BCZ'>0\). For \(0<q<p\),
\[
(U+V)^{-p}\leq U^{-(p-q)}V^{-q}.
\]
Hence, when \(p-q<m\), \(q<\beta\), and \(\mathbb E(Z')^{-q}<\infty\), independence yields
\[
\mathbb E Z^{-p}\leq
2^{-(p-q)}\mathbb E[(1-B)^{-(p-q)}B^{-q}]
\mathbb E[C^{-q}]\,\mathbb E[(Z')^{-q}]<\infty.
\]
Indeed, \(1-B\) has lower-tail order \(t^m\) near zero, while \(\mathbb E B^{-q}=\mathbb E C^{-q}=(\lambda/(\lambda-q\kappa))^m<\infty\) for \(q<\beta\). The mixed expectation is finite at both endpoints. Initially, \(Z\geq2(1-B)\) gives all inverse moments of orders \(p<m\). A finite sequence of increments smaller than \(m\), each intermediate exponent strictly less than \(\beta\), reaches \(p=\beta\); the displayed inequality then proves the required critical moment.

**3. Equilibrium run age and positive orientation.** Let \(S(t)=\mathbb P(T_+>t)\), and let \(A\) be the age of the currently observed run under equilibrium time sampling, conditional on its sign being positive. Its survivor function is
\[
H(t)=\mathbb P(A>t)=\frac{1}{\mathbb ET_+}\int_t^\infty S(u)\,du
=\frac{e^{-\lambda t}}{m}\sum_{j=0}^{m-1}\frac{(m-j)(\lambda t)^j}{j!}.
\]
The entrance gap \(Z\) is independent of the current run and hence of its equilibrium age. Moreover \(\mathbb P(\sigma=+1)=1/2\). Within a positive run, \(1-X=Ze^{-\kappa A}\). Therefore, for \(0<\varepsilon<1\), the *exact* positive-orientation contribution is
\[
P_+(\varepsilon)=\frac12\mathbb E\left[
\mathbf 1_{\{Z\leq\varepsilon\}}+
\mathbf 1_{\{Z>\varepsilon\}}
H\left(\frac{\log(Z/\varepsilon)}{\kappa}\right)\right].
\]
The highest term in the age-survival polynomial gives, for each fixed \(Z>0\),
\[
\frac{H(\kappa^{-1}\log(Z/\varepsilon))}
{\varepsilon^\beta[\log(1/\varepsilon)]^{m-1}}
\longrightarrow\frac{\beta^{m-1}}{m(m-1)!}Z^{-\beta}.
\]
For \(Z>\varepsilon\), the normalized integrand is bounded by a constant times \(Z^{-\beta}\), using \(Z\leq2\) and \(\log(Z/\varepsilon)\leq\log(2/\varepsilon)\). Dominated convergence applies by step 2. Also
\[
\mathbb P(Z\leq\varepsilon)\leq
\varepsilon^\beta\mathbb E[Z^{-\beta}\mathbf1_{\{Z\leq\varepsilon\}}]
=o(\varepsilon^\beta).
\]
We conclude \(P_+(\varepsilon)\sim C_{m,\beta}\varepsilon^\beta[\log(1/\varepsilon)]^{m-1}\).

**4. Negative orientation cannot dominate.** At the start of a negative run the deficit from the right edge is \(W=CZ\), where the completed positive run has independent Gamma duration. Its small-ball probability satisfies
\[
\mathbb P(W\leq\varepsilon)
\sim \frac{\beta^{m-1}}{(m-1)!}\mathbb E[Z^{-\beta}]\,
\varepsilon^\beta[\log(1/\varepsilon)]^{m-1},
\]
by the same dominated-convergence argument with the ordinary (not equilibrium-age) Gamma survival function. At equilibrium time sampling within a negative run, the deficit is
\[
1-X=2(1-e^{-\kappa A})+We^{-\kappa A}.
\]
The event \(X>1-\varepsilon\) forces \(A=O(\varepsilon)\) and \(W\leq2\varepsilon\). Since this age is independent of \(W\) and has a bounded density near zero, the probability from negative orientation is
\[
P_-(\varepsilon)=O(\varepsilon^{\beta+1}[\log(1/\varepsilon)]^{m-1})=o(P_+(\varepsilon)).
\]
Combining both orientations proves the boxed asymptotic. Reflection symmetry proves its left-edge counterpart.

**5. Fixed-mean hierarchy.** For a common mean \(\tau=m/\lambda\), the boundary exponent equals \(\beta_m=m/(\kappa\tau)\). Consequently, for any integers \(2\leq m<n\), the ratio of the two edge tails equals a positive finite constant times
\[
\varepsilon^{(n-m)/(\kappa\tau)}[\log(1/\varepsilon)]^{n-m}(1+o(1))\longrightarrow0.
\]
This establishes the strict ordering without assuming a closed form for the entrance negative moment.

## Verification
The standalone file `check.py` verifies the integrated Erlang-age polynomial and derivative identity; samples the affine perpetuity with an independent update scheme; compares its exact first moment to the sampled first moment; compares one stationary second moment to an independently assembled phase-generator calculation; and checks the predicted approach of scaled boundary tails at three parameter sets. The packaged checker reports 98 passing finite checks. Simulations assess the algebra and normalization, not the infinite-limit proof, which is steps 1–5. The entrance negative moment is defined exactly by the invariant perpetuity, not claimed to have a simpler elementary expression.

## Relationship to prior work
Farago and Smith [1] formulate the general non-Markovian run-and-tumble confinement problem, derive stationary-current integral equations, and evaluate exponential, semi-Gaussian and half-Student running-time examples. Their full text discusses edge behavior and local switching rates, but does not provide the Erlang-shape sharp logarithmic factor, positive perpetuity-moment prefactor, or same-mean shape hierarchy proved here. Guéneau, Majumdar and Schehr [2] develop the affine-recursion method for harmonic active dynamics, concentrating on periodic and Poisson forcing. The 2026 exact dimensional RTP solution [3] assumes exponentially distributed intervals in its generalized-velocity recursion and therefore does not include non-exponential Erlang renewals. Sun, Ye and Podgornik [5] explicitly use exponential run and finite-rest intervals with a zero-propulsion rest state; their exactly solved three-state process differs from the non-exponential, always-moving, reversing Erlang-run model here. The Markovian exponential-run beta stationary law is classical; the \(m=1\) consistency case is not presented as new. Existing published mathematical findings on power-law (heavy-tailed) alternating runs yield a different slowly varying logarithmic-edge regime and neither logically implies the exponentially decaying Erlang-tail result nor its coefficient.

## Limitations
The theorem does not establish the full stationary density in elementary closed form, a uniform-in-shape asymptotic, or an analogous result under thermal diffusion. The leading prefactor involves an exact finite negative moment of the stationary entrance-gap perpetuity; numerical evaluation of that moment is approximate. The available comparisons cannot establish worldwide publication priority, particularly in specialized phase-type and renewal-driven switching literature. The result holds for sign reversal, not arbitrary redraw of velocity direction at renewal.

## References
[1] O. Farago and N. R. Smith, “Confined run and tumble particles with non-Markovian tumbling statistics,” first public version 2024-01-03, arXiv:2401.01576, https://arxiv.org/abs/2401.01576.

[2] M. Guéneau, S. N. Majumdar and G. Schehr, “Active particle in a harmonic trap driven by a resetting noise: an approach via Kesten variables,” first public version 2023-06-15, arXiv:2306.09453, https://arxiv.org/abs/2306.09453.

[3] M. Guéneau, S. N. Majumdar and G. Schehr, “Exact stationary state of a \(d\)-dimensional run-and-tumble particle in a harmonic potential,” first public version 2026-02-09, arXiv:2602.08436, https://arxiv.org/abs/2602.08436.

[4] R. Garcia-Millan and G. Pruessner, “Run-and-tumble motion in a harmonic potential: field theory and entropy production,” J. Stat. Mech. (2021) 063203, https://doi.org/10.1088/1742-5468/ac014d.

[5] A. Sun, F. Ye and R. Podgornik, “Exact moments for a run and tumble particle with a finite tumble time in a harmonic trap,” first public version 2024-09-01, arXiv:2409.00578, https://arxiv.org/abs/2409.00578.
