# A Gaussian–Gumbel crossover and logistic bilateral cancellation in a shared switching-diffusivity gas

## Finding

A single environment modulating the diffusivity of many otherwise independent Brownian tracers produces a sharp finite-population transition between ordinary Gaussian extreme-value noise and collective environment noise. The critical switching rate is the **square of the logarithm of the number of tracers**. At the critical scale the two distant spatial fronts converge jointly to independent Gumbel variables plus the *same* Gaussian displacement. Their difference cancels that environmental displacement and retains the standard logistic law throughout the fast-mixing regime.

Fix \(T>0\) and two distinct numbers \(D_+>D_->0\). Write \(\bar D=(D_++D_-)/2\), \(\delta=(D_+-D_-)/2\), and \(A_0=\bar D T\). For every integer \(N\ge2\), let a common symmetric two-state Markov chain \(S_N(t)\in\{-1,1\}\), initially in its stationary symmetric law, flip at rate \(\lambda_N>0\). Independently, let \(W_i\), \(1\le i\le N\), be standard Brownian motions and define

\[
X_i(T)=\int_0^T\sqrt{2[\bar D+\delta S_N(s)]}\,dW_i(s).
\]

Let \(H_N=\max_i X_i(T)\) and \(J_N=-\min_i X_i(T)\) be the positive-direction and negative-direction front magnitudes. Define \(L_N=\log N\),

\[
u_N=\sqrt{2L_N}-\frac{\log L_N+\log(4\pi)}{2\sqrt{2L_N}},\qquad
b_N=\sqrt{\frac{A_0}{L_N}},\qquad
m_N=\sqrt{2A_0}\,u_N.
\]

Assume \(\lambda_N\to\infty\). The following jointly hold, where \(G_1,G_2\) are independent standard Gumbel random variables (distribution function \(e^{-e^{-x}}\)) and \(Z\sim N(0,1)\) is independent of them:

1. If \(\lambda_N/L_N^2\to\infty\), then
\[
\left(\frac{H_N-m_N}{b_N},\frac{J_N-m_N}{b_N}\right)
\ \Rightarrow\ (G_1,G_2).
\]
2. If \(\lambda_N/L_N^2\to c\in(0,\infty)\), put \(\sigma_c=\delta/(\bar D\sqrt{Tc})\). Then
\[
\boxed{\left(\frac{H_N-m_N}{b_N},\frac{J_N-m_N}{b_N}\right)
\ \Rightarrow\ (G_1+\sigma_c Z,G_2+\sigma_c Z).}
\]
Consequently, the limiting covariance of the centered, scaled fronts is \(\sigma_c^2\) and the variance of either front is \(\pi^2/6+\sigma_c^2\).
3. If \(\lambda_N/L_N^2\to0\), then
\[
\frac{\sqrt{\lambda_N}}{L_N}
\left(\frac{H_N-m_N}{b_N},\frac{J_N-m_N}{b_N}\right)
\ \Rightarrow\ \left(\frac{\delta}{\bar D\sqrt T}Z,\frac{\delta}{\bar D\sqrt T}Z\right).
\]
4. In **all three regimes**, without any assumption on the limiting ratio \(\lambda_N/L_N^2\) other than \(\lambda_N\to\infty\), the imbalance has the independent-of-clock limit
\[
\boxed{\frac{H_N-J_N}{b_N}\Rightarrow L_{\rm log},\qquad
\Pr(L_{\rm log}\le x)=\frac1{1+e^{-x}}.}
\]
At critical scaling the imbalance is also independent of the limiting environmental Gaussian variable. The normalized sum of the two front magnitudes instead converges to \(G_1+G_2+2\sigma_c Z\).

There is additionally a sharp variance competition, for any \(\lambda_N\to\infty\):
\[
\boxed{\operatorname{Var}(H_N)
=\frac{\pi^2\bar D T}{6\log N}+
\frac{\delta^2\log N}{\bar D\lambda_N}
+o\left(\frac1{\log N}+\frac{\log N}{\lambda_N}\right).}
\]
The same relation holds for \(J_N\). The first term is independent-particle extreme-value sampling; the second is common-environment variation. For finite \(\lambda_N\) not tending to infinity, no universal logistic limit in the stated deterministic normalization is claimed.

## Assumptions and scope

All processes are at the **same fixed observation time** \(T>0\), start at zero, and are conditionally independent given the *single common* diffusivity path. The two positive diffusivities are constant in \(N\), distinct, and symmetric switching is stationary at time zero. The flipping rate may depend on \(N\), but must tend to infinity in the asserted limits. No spatially varying force, individual environment, particle interaction, reset mechanism, or first-passage statistic is included. The fixed-time maximum is not the temporal maximum of an individual path.

## Proof

**Conditional Gaussian identity.** Define \(B_N=\int_0^T S_N(s)\,ds\) and \(A_N=A_0+\delta B_N\). Uniform ellipticity gives \(TD_-\le A_N\le TD_+\) almost surely. Conditional on the common environment, the Brownian stochastic integrals are independent centered normals with variance \(2A_N\). Thus, on an equivalent probability space,
\[
(H_N,J_N)=\sqrt{2A_N}\,(U_N,V_N),
\]
where \(U_N\) is the maximum and \(V_N\) is the negative minimum of \(N\) independent standard normals, jointly independent of \(A_N\). This identity also proves the exact finite-\(N\) conditional front law
\[
\Pr(H_N\le x,J_N\le y\mid A_N=a)
=\bigl[\Phi(x/\sqrt{2a})-\Phi(-y/\sqrt{2a})\bigr]_+^N.
\]

**Fast-switching central limit.** The two-state chain has covariance \(\mathbb E[S_N(s)S_N(t)]=e^{-2\lambda_N|t-s|}\). Direct integration gives
\[
\mathbb E B_N=0,\qquad
\operatorname{Var}(B_N)=\frac{T}{\lambda_N}-\frac{1-e^{-2\lambda_N T}}{2\lambda_N^2}.
\]
For completeness, the generator satisfies \(\mathcal Q s=-2\lambda_Ns\). The Dynkin martingale
\(M_N(t)=S_N(t)-S_N(0)+2\lambda_N\int_0^tS_N(s)ds\)
has jumps bounded by \(2\) and predictable quadratic variation \(4\lambda_Nt\). The martingale central limit theorem, or equivalently the explicit two-state characteristic function, gives
\[
\sqrt{\lambda_N}B_N\Rightarrow\sqrt T Z.
\]
The bounded endpoint correction \([S_N(T)-S_N(0)]/(2\sqrt{\lambda_N})\) disappears. This convergence is independent of the Gaussian sample extremes by construction.

**Joint Gaussian extremes.** Set \(a_N=(2L_N)^{-1/2}\). Standard Gaussian tail asymptotics give \(N[1-\Phi(u_N+a_Nx)]\to e^{-x}\). For fixed \(x,y\),
\[
\Pr\left(\frac{U_N-u_N}{a_N}\le x,\frac{V_N-u_N}{a_N}\le y\right)
=\bigl[\Phi(u_N+a_Nx)-\Phi(-u_N-a_Ny)\bigr]^N
\to e^{-e^{-x}-e^{-y}}.
\]
Hence \((G_N^+,G_N^-):=((U_N-u_N)/a_N,(V_N-u_N)/a_N)\Rightarrow(G_1,G_2)\), jointly with the independent telegraph central limit.

**Scale comparison and critical law.** Write \(R_N=\sqrt{A_N/A_0}\). The exact joint front identity is
\[
\left(\frac{H_N-m_N}{b_N},\frac{J_N-m_N}{b_N}\right)
=R_N(G_N^+,G_N^-)+\frac{u_N}{a_N}(R_N-1)(1,1).
\]
Since \(R_N-1=\delta B_N/(2A_0)+O_{\mathbb P}(B_N^2)\), \(u_N/a_N=2L_N+O(\log L_N)\), and \(B_N=O_{\mathbb P}(\lambda_N^{-1/2})\),
\[
\frac{u_N}{a_N}(R_N-1)=\frac{\delta L_N}{A_0}B_N+o_{\mathbb P}\left(1+\frac{L_N}{\sqrt{\lambda_N}}\right).
\]
This yields the fast, critical, and slow three cases under the stated normalizations. In the slow case the term containing \(G_N^\pm\) vanishes after multiplying by \(\sqrt{\lambda_N}/L_N\). At the critical scale \(L_NB_N\Rightarrow\sqrt{T/c}Z\), giving coefficient \(\delta/(\bar D\sqrt{Tc})\).

**Clock-free imbalance.** Subtract the two exact front identities; the common additive environment term cancels *before taking any limit*:
\[
\frac{H_N-J_N}{b_N}=R_N(G_N^+-G_N^-).
\]
Since \(R_N\to1\) in probability under \(\lambda_N\to\infty\), the limit is \(G_1-G_2\). If \(E_i=e^{-G_i}\), then \(E_1,E_2\) are independent unit-rate exponentials; \(G_1-G_2=\log(E_2/E_1)\) has the stated logistic distribution. Its independence of the Gaussian environmental limit follows from their joint independence before taking the limit.

**Variance law.** Independence gives an exact, finite-\(N\) decomposition with \(U_N\) as above:
\[
\operatorname{Var}(H_N)=2A_0\operatorname{Var}(U_N)
+2\operatorname{Var}(\sqrt{A_N})[\mathbb E U_N]^2.
\]
Gaussian extreme-value moment convergence gives \(\mathbb E U_N=u_N+O(a_N)\) and \(\operatorname{Var}(U_N)=\pi^2/(12L_N)+o(L_N^{-1})\). Since \(\lambda_N\to\infty\), the martingale fourth-moment bound (or the explicit telegraph moment generating function) implies \(\mathbb E B_N^4=O(\lambda_N^{-2})\); Taylor's formula on the compact uniformly elliptic interval and the exact variance above give
\[
\operatorname{Var}(\sqrt{A_N})=\frac{\delta^2}{4A_0}\operatorname{Var}(B_N)(1+o(1))
=\frac{\delta^2}{4\bar D\lambda_N}(1+o(1)).
\]
Substitution yields the displayed sharp two-term variance asymptotic. This verifies that the threshold separating the two variances is \(\lambda_N\asymp(\log N)^2\), and not merely a sufficient growth condition.

## Verification

The accompanying `checker.py` constructs exact two-state paths using Poisson flip counts and sorted uniform jump times, checks their integrated covariance against an independent quadrature, samples conditional Gaussian extrema by an exact inverse-normal transform, and tests the finite-\(N\) bilateral logistic cancellation. On the recorded run the checker passed 71 assertion groups. It tests finite parameter values; none of the infinite-volume conclusions is inferred from these numerical comparisons. The displayed analytic argument supplies the infinite-\(N\) proof.

Run `python checker.py` with NumPy and SciPy. The code contains no external data files or network dependencies.

## Relationship to prior work

Hass, Carroll-Godfrey, Corwin and Corwin (first public version 2022-05-04) establish extreme-particle/environment fluctuation separation for random walks in a **space-time random drift field** and explicitly propose continuum particles with a common random diffusivity field as a further testing ground. Hass, Drillick and the Corwins (2024) develop extreme-diffusion variance laws for random walks in random environments, not the present globally uniform **temporally switching volatility** or a joint Gaussian–Gumbel window. The variance decomposition alone is a law-of-total-variance fact and is not claimed as novel. Uchida, Washizu and Miyoshi (2023) study single-particle stochastic-diffusivity propagators and Gaussianization; single-particle Gaussianization does not determine the **simultaneous population-size/switching-rate** law. Standard Gaussian maxima and the logistic difference of independent Gumbels are used as established facts. The contribution assessed here is the joint sharp crossover with a shared Gaussian front mode, its independent logistic antisymmetric mode, and the explicit critical scale and amplitudes in the common switching-diffusivity gas.

## Limitations

The environment is global and temporally Markovian, not the spatially heterogeneous drift field of the motivating papers. The result does not extend without proof to asymmetrically switching clocks, heavy-tailed holding times, correlated Brownian driving noises, interacting particles, or pathwise first arrival. The variance law is asymptotic in \(N\) with \(\lambda_N\to\infty\); it does not give non-asymptotic confidence intervals. Pre-existing general extreme-value or random-environment theorems may subsume the special model implicitly. An inaccessible full text on broad stochastic diffusivities leaves a publication-priority risk; originality is judged relative to the actual inspected material, not guaranteed by keyword search. No independent verification or publication-priority certification is claimed.

## References

- J. B. Hass, A. N. Carroll-Godfrey, I. Corwin and E. I. Corwin, *Anomalous Fluctuations of Extremes in Many-Particle Diffusion*, first posted 2022-05-04, arXiv:2205.02265, https://arxiv.org/abs/2205.02265 (especially the discussion of a prospective shared continuum diffusivity on p. 5).
- J. Hass, H. Drillick, I. Corwin and E. I. Corwin, *Extreme Diffusion Measures Statistical Fluctuations of the Environment*, first posted 2024-06-25, arXiv:2406.17733, https://arxiv.org/abs/2406.17733.
- G. Uchida, H. Washizu and H. Miyoshi, *Diffusion with a Broad Class of Stochastic Diffusion Coefficients*, first posted 2023-08-17, arXiv:2308.08820, https://arxiv.org/abs/2308.08820.
- A. J. McNeil, *Extreme Value Theory* (classical independent-normal maximum asymptotics used in the proof); equivalently the Gaussian-maxima theorem as reviewed in https://doi.org/10.1088/1751-8121/ac4394.
