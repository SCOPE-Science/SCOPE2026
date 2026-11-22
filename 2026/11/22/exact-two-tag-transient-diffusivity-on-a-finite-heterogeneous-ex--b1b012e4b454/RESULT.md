# Exact two-tag transient diffusivity on a finite heterogeneous exclusion ring

## Finding

Two distinguishable symmetric exclusion walkers on the same finite ring have **equal long-time diffusivities**, but unequal, strictly decreasing transient instantaneous diffusivities. The relative *excess* instantaneous diffusivity is completely independent of observation time, and its exact ratio is the **square of the microscopic jump-rate ratio**. Furthermore, every finite-time mean-squared displacement is a positive sum of explicit odd reflecting-gap eigenmodes.

Let \(L\ge3\) and \(n=L-1\). Define \(q=a+b\), \(r_1=a\), \(r_2=b\), and
\[
D_* = \frac{n-1}{n}\frac{ab}{q},\qquad
\theta_m=\frac{m\pi}{2n},\qquad
\lambda_m=4q\sin^2\theta_m.
\]
The exact stationary-start squared displacement of either labeled walker \(i\) is, for every \(t\ge0\),
\[
\boxed{\mathbb E[X_i(t)^2]=2D_*t+\left(\frac{r_i}{q}\right)^2
\sum_{\substack{1\le m<n\\m\ \mathrm{odd}}}
\frac{\cos^2\theta_m}{n^2\sin^4\theta_m}(1-e^{-\lambda_m t}).}
\]
Its mean is zero. Consequently, with \(K_i(t)=\frac12\frac{d}{dt}\mathbb E[X_i(t)^2]\),
\[
\boxed{\ K_i(t)>D_*,\qquad K_i'(t)<0,\qquad
\frac{K_1(t)-D_*}{K_2(t)-D_*}=\left(\frac ab\right)^2\ }
\qquad(0\le t<\infty).
\]
The endpoints and finite-size intercept are
\[
K_i(0)=\frac{n-1}{n}r_i,\qquad
\lim_{t\to\infty}K_i(t)=D_*,\qquad
\lim_{t\to\infty}(\mathbb E[X_i(t)^2]-2D_*t)
=\left(\frac{r_i}{q}\right)^2\frac{n^2-1}{6}.
\]
For every strictly positive rate pair, the common slowest relaxation exponent is \(4q\sin^2(\pi/(2n))\). Thus the long-time common diffusion masks a persistent, exactly quantifiable difference in their finite-time approach.

## Assumptions and scope

The space is the cycle \(\mathbb Z/L\mathbb Z\), with integer \(L\ge3\). Exactly two *distinguishable* walkers occupy different sites. Independently, walker 1 attempts to hop by one site clockwise and anticlockwise at rate \(a>0\) **for each direction**, and walker 2 does likewise at rate \(b>0\) per direction. An attempted jump into the other walker is rejected. All rates are constant and time is continuous. Initial labeled positions are distributed uniformly over the \(L(L-1)\) ordered distinct-site pairs; this is the reversible stationary measure. Each \(X_i(t)\) counts all successful clockwise hops minus all successful counterclockwise hops after time zero; it is *unwrapped*, not a position modulo \(L\).

## Proof

**1. Reduction to the reflecting separation chain.** Let \(k\in\{1,\ldots,n\}\) be the clockwise gap from walker 1 to walker 2, modulo \(L\). From an interior gap, moves \(k\to k-1\) and \(k\to k+1\) each occur at combined rate \(q=a+b\). At \(k=1\), only \(k\to2\) is possible, and at \(k=n\), only \(k\to n-1\) is possible, in both cases with rate \(q\). Thus the gap generator is the symmetric reflecting matrix
\[
(Qf)(k)=q\mathbf1_{k>1}(f(k-1)-f(k))
+q\mathbf1_{k<n}(f(k+1)-f(k)).
\]
Its invariant distribution \(\pi(k)=1/n\) is uniform and the initial gap has this law. For the signed hopping displacement of walker \(i\), its local instantaneous drift is
\[
g_i(k)=s_i r_i(\mathbf1_{k=n}-\mathbf1_{k=1}),
\qquad s_1=1,\quad s_2=-1.
\]
The instantaneous squared-jump activity averaged under the invariant gap law is \(2r_i(n-1)/n\). The expected unwrapped displacement vanishes because \(\langle g_i,1\rangle_\pi=0\) and the gap remains stationary.

**2. An exact finite-gap Poisson corrector.** Put
\[
u_i(k)=s_i\frac{r_i}{q}\left(k-\frac{n+1}{2}\right).
\]
A direct check of the interior differences and both reflecting endpoints gives \(-Qu_i=g_i\), \(\langle u_i,1\rangle_\pi=0\). In particular,
\[
\langle g_i,u_i\rangle_\pi=
\frac{r_i^2(n-1)}{nq}.
\]
No continuum approximation is made.

**3. Exact second-moment evolution.** Write \(M_i(k,t)=\mathbb E[X_i(t)\mathbf1_{\{K_t=k\}}]\), with the stationary gap as initial state and \(X_i(0)=0\). The forward moment equations, keeping each signed hop, are
\[
\dot M_i=QM_i-\frac1n g_i,\qquad M_i(\cdot,0)=0.
\]
Indeed, the incoming signed-hop current at state \(k\) is \(-g_i(k)/n\), by reversibility and the antisymmetry of signed hops under edge reversal. Since \(-Qu_i=g_i\),
\[
M_i(k,t)=-\frac1n((I-e^{tQ})u_i)(k).
\]
The jump-generator identity \((X_i+\Delta X_i)^2-X_i^2=2X_i\Delta X_i+(\Delta X_i)^2\) therefore yields
\[
\begin{aligned}
\frac12\frac{d}{dt}\mathbb E[X_i(t)^2]
&=\frac{r_i(n-1)}n+\sum_{k=1}^{n}M_i(k,t)g_i(k)\\
&=\frac{r_i(n-1)}n-\langle g_i,u_i\rangle_\pi
  +\langle g_i,e^{tQ}u_i\rangle_\pi\\
&=D_*+\langle g_i,e^{tQ}u_i\rangle_\pi,
\end{aligned}
\]
where \(D_*=(n-1)ab/(nq)\), regardless of \(i\).

**4. Odd spectral modes and positive relaxation.** In \(L^2(\pi)\), the nonconstant orthonormal eigenfunctions of \(-Q\) are
\[
\phi_m(k)=\sqrt2\cos\!\left(\frac{m\pi(k-1/2)}n\right),
\quad\lambda_m=4q\sin^2\left(\frac{m\pi}{2n}\right),\quad1\le m<n.
\]
Since \(g_i\) is supported on the two reflecting ends with opposite signs, every even mode has zero overlap, while for odd \(m\),
\[
\left|\langle g_i,\phi_m\rangle_\pi\right|^2
=\frac{8r_i^2}{n^2}\cos^2\theta_m.
\]
Expand \(u_i=(-Q)^{-1}g_i\), substitute this eigenbasis into Step 3, and integrate from zero. The coefficient of \(1-e^{-\lambda_m t}\) is
\[
\frac{2\left|\langle g_i,\phi_m\rangle_\pi\right|^2}{\lambda_m^2}
=\left(\frac{r_i}{q}\right)^2\frac{\cos^2\theta_m}{n^2\sin^4\theta_m},
\]
proving the full formula. Every odd coefficient is strictly positive; in particular \(m=1\) exists for every \(n\ge2\). Differentiation proves strict decrease of \(K_i(t)\) and positive excess at each finite time. The only dependence on the tag label in the relaxation is the factor \(r_i^2\), so the squared-rate ratio follows identically at every lag.

**5. Exact infinite-time intercept.** The finite sum can be evaluated without trigonometric algebra. The spectral identity gives
\[
\lim_{t\to\infty}(\mathbb E[X_i(t)^2]-2D_*t)
=2\sum_{m=1}^{n-1}\frac{|\langle g_i,\phi_m\rangle_\pi|^2}{\lambda_m^2}
=2\langle u_i,u_i\rangle_\pi.
\]
The variance of the uniform integer \(k\in\{1,\ldots,n\}\) is \((n^2-1)/12\), hence this is \((r_i/q)^2(n^2-1)/6\). All statements follow for the entire parameter range, including \(L=3\) and equal hopping rates.

## Verification

Run `python checker.py` with Python 3, NumPy and SciPy. The checker constructs the full marked gap transition matrices directly from individual hopping events; an independent block-matrix exponential generates both tags' exact second moments without evaluating the spectral formula. It compares these results for ring lengths \(3\) through \(14\), distinct positive rate pairs, multiple finite times, and both tags. An exact-rational verification of the Poisson corrector covers ring lengths \(3\) through \(17\). It also tests the excess-diffusivity ratio and large-time intercept. A complete run passes **564 checks**. These computations are corroboration; Steps 1–5 prove the infinite family of claims.

## Relationship to prior work

Mason, Jack and Bruna [1] study the unequal-species exclusion model and its cross-diffusion coefficients in **dimensions at least two** and in dilute/macroscopic regimes. Their paper expressly distinguishes the nonpassing one-dimensional case. It motivates the present exact finite-particle one-dimensional analysis, but does not yield an all-time finite-ring tagged spectrum.

Ambjörnsson and coauthors [2] derive all-time propagators for two *continuum* hard-core Brownian particles on an **infinite line**, with simulations using a reflecting finite interval. Their exact propagators do not give the finite *periodic lattice* tagged dispersion or its all-time squared-rate relation.

Mallmin, du Buisson and Touchette [3] establish the collective long-time current large deviations of heterogeneous reflected Brownian particles on a **continuum ring**. Their harmonic-mean effective diffusivity is consistent with the long-time structural form here, but their continuum setting lacks the finite-lattice occupancy factor and the tagged transient spectrum. Gupta and coauthors [4] address finite-size tagged correlations for **asymmetric** (driven) homogeneous exclusion on a ring, including oscillatory effects, a distinct stochastic generator and observable classification.

The spectral result above is derived from a reversible finite-state lattice gap chain, with explicit positive relaxation modes and simultaneous two-tag comparison. No general novelty or priority theorem is inferred merely from failed literature searches.

## Limitations

This is an exact two-particle, finite-ring, stationary-start, continuous-time lattice result. It does not assert the same formula for three or more particles, open boundaries, driven hopping, initial nonstationary gaps, or continuous Brownian motion. The positivity and rate-ratio statements concern instantaneous *excess* diffusivity relative to the common asymptote, not a ratio of the entire instantaneous diffusivities. The right-hand ratio is undefined only in the infinite-time limit where both excesses vanish; the ratio has the stated finite positive constant for every finite time. No complete survey of unpublished or unindexed literature is possible, so priority remains qualified.

## References

[1] J. Mason, R. L. Jack and M. Bruna, *Macroscopic behaviour in a two-species exclusion process via the method of matched asymptotics*, first posted 2 March 2022, arXiv:2203.01038. https://arxiv.org/abs/2203.01038

[2] T. Ambjörnsson, L. Lizana, M. A. Lomholt and R. J. Silbey, *Single-file dynamics with different diffusion constants*, arXiv:0803.2485. https://arxiv.org/html/0803.2485v2

[3] E. Mallmin, J. du Buisson and H. Touchette, *Large deviations of currents in diffusions with reflective boundaries*, arXiv:2102.04846. https://arxiv.org/abs/2102.04846

[4] S. Gupta, S. N. Majumdar, C. Godrèche and M. Barma, *Tagged Particle Correlations in the Asymmetric Simple Exclusion Process: Finite Size Effects*, arXiv:cond-mat/0703464. https://arxiv.org/abs/cond-mat/0703464
