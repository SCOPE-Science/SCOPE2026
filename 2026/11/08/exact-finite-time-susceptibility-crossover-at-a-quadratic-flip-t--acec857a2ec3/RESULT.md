# Exact finite-time susceptibility crossover at a quadratic flip threshold

## Finding

For the canonical quadratic period-doubling map \(f_{\mu,Q}(x)=-(1+\mu)x+Qx^2\), the critical finite-time susceptibility has a universal **entire crossover profile**, including its normalization and the positive-side peak displacement, rather than only a scaling exponent. Specifically, if \(Q>0\), \(0<Qx_0<1/4\), and \(x_{j+1}=f_{\mu,Q}(x_j)\), define
\[
\chi_N(\mu)=\sum_{j=1}^{N}\bigl(\partial_\mu x_j(\mu)\bigr)^2,
\]
with the initial condition independent of \(\mu\). For each real \(z\), as \(N\to\infty\) with \(\mu=z/N\),
\[
\lim_{N\to\infty}\frac{\chi_N(z/N)}{N^2}
=\frac{\mathcal S(z)}{Q^2},\qquad
\mathcal S(z)=\int_0^1\left[\frac{\partial}{\partial z}\sqrt{\frac{z}{1-e^{-2zt}}}\right]^2dt.
\]
The formula is interpreted continuously at \(z=0\), and convergence is uniform for \(z\) in compact real intervals. The shape satisfies \(\mathcal S(0)=1/16\), \(\mathcal S'(0)=1/72>0\), and \(\mathcal S(z)\to0\) as \(z\to+\infty\). In particular the positive-side limiting susceptibility attains its maximum at a strictly positive rescaled bifurcation parameter (no uniqueness of the maximizer is asserted).

A second exact consequence at the critical parameter \(\mu=0\), for the finite-time Lyapunov exponent \(\lambda_N=N^{-1}\sum_{j=0}^{N-1}\log|f'_{0,Q}(x_j)|\), is
\[
\lim_{N\to\infty}\frac{N\lambda_N}{\log N}=-\frac32.
\]
These are analytic limits in the original one-step clock, not numerical scaling fits.

## Assumptions and scope

The coefficient \(Q\) is fixed and strictly positive, the initial condition satisfies \(0<Qx_0<1/4\) and is independent of the bifurcation parameter, and \(z\in\mathbb R\) remains fixed while \(N\to\infty\). The parameter derivative in \(\chi_N\) is taken at a fixed \(N\) before setting \(\mu=z/N\). The Lyapunov conclusion concerns exactly \(\mu=0\). These are deterministic scalar map statements.

## Proof

**1. Exact two-step reduction and a uniform entrance estimate.** Rescale \(u_j=Qx_j\). The recurrence becomes \(u_{j+1}=-(1+\mu)u_j+u_j^2\), so for \(v_m=u_{2m}>0\) its exact two-step map is
\[
 v_{m+1}=v_m R(v_m,\mu),\quad
 R(v,\mu)=(1+\mu)^2+\mu(1+\mu)v-2(1+\mu)v^2+v^3.
\]
Fix \(K>0\). For all sufficiently large \(N\), all \(|z|\le K\), and \(\mu=z/N\), the interval \((0,u_0]\) is invariant under this positive increasing two-step map. Indeed the map and its derivative are positive there for small \(|\mu|\); its value at \(u_0\) is strictly less than \(u_0\) for large \(N\), since \(R(u_0,0)=1-2u_0^2+u_0^3<1\). Thus all \(v_m\) are positive and bounded by \(u_0\), and the odd points have the opposite sign.

Put \(S_m=v_m^{-2}\). Expanding the exact rational identity \(S_{m+1}=S_m R(S_m^{-1/2},\mu)^{-2}\) yields
\[
 S_{m+1}=S_m+4-4\mu S_m+E(S_m,\mu),
\]
where, on this invariant interval, a constant independent of \(N,z,m\) bounds the remainder as
\[
 |E(S,\mu)|\le C\bigl(S^{-1/2}+|\mu|S^{1/2}+S^{-1}+|\mu|+\mu^2S\bigr).
\]
An elementary comparison of the exact identity with the affine recurrences \(S\mapsto(1\pm C_K/N)S+c\) gives
\[
 c_K(m+1)\le S_m\le C_K(m+1)\quad(0\le m\le N/2+1).
\]
For clarity, the lower estimate uses the positive constant term from \(4+E(S,0)\), since \(u_0<1/4\); the upper estimate uses its boundedness, and the \(O(1/N)S\) coefficient. Discrete Gronwall closes both bounds on this finite window. Consequently
\[
 \sup_{m\le N/2}\Big|\sum_{j<m}E(S_j,z/N)\Big|=O_K(\sqrt N).
\]
The estimates and subsequent derivatives may depend on the fixed \(u_0\) but are uniform for \(z\) in compact intervals.

**2. Derivative-controlled crossover, not differentiation of an unverified limit.** Since \(S_0=u_0^{-2}\) is independent of \(z\), differentiation of the *exact* recurrence gives
\[
 \partial_z S_{m+1}=(1-4z/N)\partial_z S_m-4S_m/N
 +\partial_z E(S_m,z/N).
\]
Direct differentiation of the rational formula for \(E\), together with \(S_m\asymp_K m+1\), proves by induction
\[
 |\partial_z S_m|\le C_K(m+1)^2/N,
 \qquad\sum_{m<N/2}|\partial_z E(S_m,z/N)|=O_K(\sqrt N).
\]
Indeed differentiating the displayed remainder produces terms bounded by \(C_K((m+1)^{1/2}/N+(m+1)^{-3/2}|\partial_zS_m|+N^{-2}(m+1))\); their sum is \(O_K(\sqrt N)\) under the induction estimate. The estimates remain valid at \(z=0\) because the exact recurrence is polynomial/rational and smooth there.

Define \(H_{m,N}(z)=S_m/N\) and \(t_m=2m/N\). The two recurrences, divided by \(N\), now constitute an Euler approximation **together with its differentiated variational equation**, with cumulative errors \(O_K(N^{-1/2})\). Thus uniformly for \(t_m\in[0,1]\) and \(|z|\le K\),
\[
 H_{m,N}(z)\longrightarrow H(z,t_m),\quad
 \partial_zH_{m,N}(z)\longrightarrow\partial_zH(z,t_m),
\]
where \(\partial_tH=2-2zH\), \(H(z,0)=0\), so
\[
 H(z,t)=\begin{cases}(1-e^{-2zt})/z,&z\ne0,\\2t,&z=0.\end{cases}
\]
For each fixed \(\delta>0\), the preceding convergence and positivity give uniform \(C^1\)-convergence for \(t_m\in[\delta,1]\) of
\[
 \sqrt N\,u_{2m}=H_{m,N}^{-1/2}\longrightarrow V(z,t_m)=H(z,t_m)^{-1/2}.
\]
Because \(\partial_\mu u_{2m}/\sqrt N=\partial_z(\sqrt N\,u_{2m})\), the positive even-time sensitivity divided by \(\sqrt N\) tends to \(\partial_zV\). The odd-time recurrence implies \(\partial_\mu u_{2m+1}=-(1+\mu-2u_{2m})\partial_\mu u_{2m}-u_{2m}\), giving the same squared limit.

The delicate initial layer is controlled rather than discarded: the comparison bounds on \(H_{m,N}\) and \(\partial_zH_{m,N}\) give \(|\partial_\mu u_{2m}|^2\le C_K(m+1)\), also for odd times, uniformly up to time \(N\). Consequently the fraction of \(\chi_N/N^2\) coming from \(j\le\delta N\) is at most \(C_K\delta^2+o(1)\). On \([\delta,1]\), Riemann sums converge uniformly to the integral of \((\partial_zV)^2\). Letting \(\delta\downarrow0\) proves the claimed compact-uniform susceptibility limit, including its precise normalization \(Q^{-2}\).

**3. Center value and the positive-side displacement.** At small \(z\), direct Taylor expansion (uniform on \([0,1]\) after the removable endpoint is resolved) yields
\[
 V(z,t)=(2t)^{-1/2}\left(1+\frac{zt}{2}+\frac{z^2t^2}{24}+O(z^3t^3)\right).
\]
Therefore
\[
 [\partial_z V(z,t)]^2=\frac t8+\frac{zt^2}{24}+O(z^2t^3),
\]
so \(\mathcal S(0)=\int_0^1t/8\,dt=1/16\) and \(\mathcal S'(0)=\int_0^1t^2/24\,dt=1/72\). For large positive \(z\), split the integral at \(t=z^{-1}\): the short part is \(O(z^{-2})\), while for the remainder \(\partial_zV=(2\sqrt z)^{-1}+O(\sqrt z\,t e^{-2zt})\); thus \(\mathcal S(z)=1/(4z)+O(z^{-2})\). Continuity, positive derivative at zero, and decay at infinity ensure at least one interior maximum on the positive half-line, without asserting uniqueness.

**4. Exact Lyapunov logarithmic coefficient.** At \(\mu=0\), \(v_{m+1}=v_m(1-2v_m^2+v_m^3)\) and the inverse-square recurrence gives \(S_m=4m+O(\sqrt m)\). The exact two-step derivative is \((f_0^2)'(v)=1-6v^2+4v^3\). Hence
\[
 \log|(f_0^2)'(v_m)|=-\frac{3}{2m}+O(m^{-3/2})
\]
for large \(m\). Summation gives \(\log |(f_0^{2M})'(u_0)|=-(3/2)\log M+O(1)\). The additional odd iterate changes the log by \(O(1)\), proving the limit for all \(N\), and linear rescaling by \(Q\) leaves the derivative multiplier unchanged.

## Verification

The standalone `verify.py` uses symbolic polynomial expansion to check the exact two-step map and its derivative and tests the critical constants and the crossover integral against independently differentiated finite trajectories. It also checks the small-parameter slope \(1/72\). Finite trajectory calculations illustrate convergence but do not replace the bounds above. Run `python verify.py` with Python 3, SymPy and mpmath installed.

## Relationship to prior work

Martin, Tang and Chialvo introduce the canonical period-doubling map and the finite-time susceptibility observable. Their 2025 preprint derives the **exponent** \(\chi_N\sim N^2\) for a quadratic flip, gives a state crossover function, and presents numerical susceptibility collapse; it does not give a parameter-differentiable full response profile, the exact integral normalization \(1/(16Q^2)\), the right-side slope, or the coefficient \(-3/2\) of the critical Lyapunov logarithm. Our result concerns precisely those additional quantitative assertions, **not** the invention of susceptibility or the observation of an exponent. Corral's earlier finite-time theory supplies state scaling for nonoscillatory bifurcations; that does not directly determine this two-step susceptibility with verified sensitivity convergence. General parabolic-map normal forms are background, not claimed as novel.

## Limitations

The result concerns the exact polynomial normal form with fixed \(Q>0\) and a small, positive, parameter-independent initial condition; it does not automatically transfer unchanged to logistic or Chialvo parameters with moving equilibria and different parameter observables. The location or uniqueness of a global susceptibility peak over all real \(z\) is not proved. No independent scientific validation or exhaustive historical priority guarantee is claimed.

## References

1. D. A. Martin, Q.-Y. Tang, and D. R. Chialvo, *Finite-time scaling on low-dimensional map bifurcations*, first posted 2025-05-30, arXiv:2505.24673v1; https://arxiv.org/abs/2505.24673.
2. Á. Corral, *Universal finite-time scaling in the transcritical, saddle-node, and pitchfork discrete and continuous bifurcations*, arXiv:2405.19947v1 (2024); https://arxiv.org/abs/2405.19947.
