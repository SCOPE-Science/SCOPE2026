# A universal Gamma–inverse-Gaussian boundary layer for rare successful stochastic returns in a stiff harmonic trap

## Finding

In a target-visible two-stage stochastic-return search, a very stiff harmonic return almost never captures a target before reaching home. However, the rare captures have a universal **joint** spatial and temporal law, distinct from the unconditioned return-time distribution.

Let a particle search from the origin for a target at \(L>0\), and let an independent Poisson alarm of rate \(r>0\) switch it into a return phase whenever the alarm precedes target capture. The return follows \(dX_t=-\kappa X_t\,dt+\sqrt{2D}\,dW_t\), with \(D>0\), until it first reaches either \(0\) (home) or \(L\) (target). After reaching home a fresh search starts. Write \(T\) for the target-hitting time during an uninterrupted search, \(R\) for its independent exponential alarm, and \(q=\Pr(T<R)\in(0,1)\).

Set \(K=\kappa L^2/D\). For one search–return cycle, let \(E_K\) be the event that the alarm occurs first and the ensuing harmonic return reaches \(L\) before \(0\). On \(E_K\), denote by \(Y\in(0,L)\) the position at the alarm and by \(\tau\) the subsequent time to reach the target. Define the dimensionless variables
\[
Z_K=K(1-Y/L),\qquad V_K=(DK^2/L^2)\tau.
\]
Then, as \(K\to\infty\) with \(D,L,r\) and the search law fixed,
\[
\Pr(E_K)\sim\frac{rL^2q}{DK^2}=\frac{rqD}{\kappa^2L^2},
\]
and for all \(u,s\ge0\),
\[
\boxed{\lim_{K\to\infty}\mathbb E\bigl[e^{-uZ_K-sV_K}\mid E_K\bigr]
=\left[u+\frac{1+\sqrt{1+4s}}2\right]^{-2}.}
\]
Equivalently, \(Z_K\) converges to a \(\operatorname{Gamma}(2,1)\) random variable \(Z\); conditional on \(Z=z\), \(V_K\) converges jointly to the first time a diffusion with generator \(\partial_{zz}-\partial_z\), started at \(z\), reaches zero. This is an inverse-Gaussian passage-time mixture. The limiting conditional mean of the dimensionless duration is \(2\), and its variance is \(6\). The ultimate completion probability attributable to a successful **return** is asymptotic to \(rL^2/(DK^2)\).

## Assumptions and scope

The search dynamics is a time-homogeneous nonexplosive regular one-dimensional diffusion, started at \(0\), with diffusion coefficient \(D>0\) near \(L\) and continuous drift there, killed at \(L\). Its alarm-position subprobability measure is absolutely continuous on \(( -\infty,L)\):
\[
h(x)\,dx=\Pr(R<T, X_R\in dx)=r\int_0^\infty e^{-rt}p_t^{(L)}(0,x)\,dt\,dx.
\]
Assume \(h\ge0\), \(h(L)=0\), \(h\) is continuously differentiable from the left at \(L\), \(h\) is integrable, \(0<q<1\), and its boundary flux satisfies \(-Dh'(L)=rq\). These conditions follow from the killed Fokker–Planck equation and probability-current identity for standard Brownian or Ornstein–Uhlenbeck searches with fixed coefficients. For the stated asymptotic theorem, no finite higher moment of the alarm-position distribution is required.

The return coefficient \(\kappa\) alone tends to infinity. The alarm never runs during a return. The target remains absorbing during both phases; return motion is stopped at the first hit of \(0\) or \(L\). No claim is made about protocols that disregard target detection during returns, change the return drift with the search law, or send the alarm rate to infinity simultaneously.

## Proof

**1. Alarm-position flux.** Integrating the killed search propagator with exponential discount gives \(\int_{-\infty}^L h(x)\,dx=1-q\). Its stationary resolvent equation, integrated over the domain, shows that the flux through the absorbing endpoint equals \(rq\), so \(-Dh'(L)=rq\) under the stated regularity. Hence
\[
h(L-\varepsilon)=\frac{rq}{D}\varepsilon+o(\varepsilon)
\qquad(\varepsilon\downarrow0).
\]
Only this boundary slope will survive in the rare-return limit.

**2. Exact return boundary-value problem.** For \(0<x<L\), introduce
\[
f_K(x;s)=\mathbb E_x\left[\exp\left(-\frac{sDK^2}{L^2}\tau\right);\tau_L<\tau_0\right]
\]
with \(\tau=\tau_0\wedge\tau_L\). The backward generator \(D\partial_{xx}-\kappa x\partial_x\) gives \(Df''-\kappa xf'=(sDK^2/L^2)f\), with \(f(0;s)=0\) and \(f(L;s)=1\). Under the rescaling \(F_K(z;s)=f_K(L(1-z/K);s)\),
\[
F_K''+(1-z/K)F_K'=sF_K,\quad F_K(0;s)=1,\quad F_K(K;s)=0.
\]
In particular, at \(s=0\),
\[
F_K(z;0)=\frac{\int_0^{1-z/K}e^{Ky^2/2}\,dy}{\int_0^1e^{Ky^2/2}\,dy}.
\]
By endpoint Laplace estimates, \(F_K(z;0)\to e^{-z}\) at each fixed \(z\ge0\). The same integral formula provides an integrable exponentially decreasing envelope on \(0\le z\le K/2\), with an exponentially negligible contribution on \(K/2\le z\le K\).

For \(s\ge0\), the maximum principle gives \(0\le F_K(z;s)\le F_K(z;0)\). On compact sets, ODE regularity and the last bound yield subsequential convergence. Any limit solves \(F''+F'=sF\), has \(F(0)=1\), is bounded, and decays as \(z\to\infty\). The unique such solution is
\[
F(z;s)=e^{-a_s z},\qquad a_s=\frac{1+\sqrt{1+4s}}2.
\]
Consequently the whole sequence converges locally uniformly.

**3. Rare successful returns and the conditional joint law.** A successful return must start in \((0,L)\). Change variables \(z=K(1-x/L)\), and use the Markov property to obtain exactly
\[
\mathbb E[e^{-uZ_K-sV_K};E_K]
=\frac{L}{K}\int_0^K h\bigl(L(1-z/K)\bigr)e^{-uz}F_K(z;s)\,dz.
\]
The boundary expansion yields \(h(L(1-z/K))\sim(rqL/D)z/K\) at every fixed \(z\). Together with the bounds for \(F_K\), an endpoint-layer dominated-convergence argument applies, since the region away from \(L\) contributes exponentially little. It gives
\[
\mathbb E[e^{-uZ_K-sV_K};E_K]
\sim\frac{rL^2q}{DK^2}\int_0^\infty z e^{-(u+a_s)z}\,dz
=\frac{rL^2q}{DK^2}(u+a_s)^{-2}.
\]
Taking \(u=s=0\) proves the success-probability asymptotic. Division proves the asserted joint Laplace-transform limit and hence joint weak convergence. The conditional transform at fixed \(z\) is \(\exp[-z(\sqrt{1+4s}-1)/2]\), exactly the first-passage transform for a drift-\(-1\), variance-rate-\(2\) diffusion. Integrating this transform over the \(z e^{-z}\) Gamma density produces the theorem's joint transform.

**4. Proportion of detections during returns.** The probability that a cycle succeeds in search is \(q\), while success in return has probability \(\Pr(E_K)\). Cycles ending at home renew independently. The final successful cycle is therefore a return success with probability \(\Pr(E_K)/(q+\Pr(E_K))\), and the claimed equivalent follows.

## Verification

The accompanying `conditional_check.py` reconstructs the finite-\(K\) boundary-value problem and checks its Laplace transforms for two sets of physical parameters, at four values of \(K\). The separate `mfpt_check.py` checks the killed Brownian resolvent boundary flux, the exact finite-strength return splitting law, and the renewal mean-time identity. These finite computations provide consistency checks only: the limit and its universality are proved by the endpoint and ODE arguments above.

For Brownian search, an independently reproducible test case is \(q=e^{-L\sqrt{r/D}}\) and
\[
h(x)=\frac{r}{2\sqrt{Dr}}\left(e^{-\sqrt{r/D}|x|}-e^{-\sqrt{r/D}(2L-x)}\right),\quad x<L.
\]
Its boundary derivative satisfies \(-Dh'(L)=rq\), supplying a direct normalization check.

## Relationship to prior work

Dubey and Pal (2026) analyze finite-time stochastic harmonic returns with targets visible during both stages, deriving mean first-passage times and efficiency comparisons. Frydel (2025) studies feedback-terminated harmonic returns and gives exact return-time and splitting formulas; in particular its stiff-return mean-delay logarithm is prior knowledge. General two-stage renewal identities and linear-force return protocols were studied by Biswas and collaborators (2024). These established ingredients are fully credited. The present statement concerns the previously unextracted **joint conditional law** of near-target alarm-position gaps and rapid successful return durations in the singular stiff-return regime, with a universal Gamma–inverse-Gaussian limit. It is not a claim that the underlying renewal identity, return splitting probability, or inverse-Gaussian first-passage transform is new.

## Limitations

The asymptotic result holds at fixed search law, fixed positive \(D,L,r\), with an absorbing target active during returns and a harmonic return field. The boundary-density regularity and flux identity must be verified when transferring it to other search diffusions. The limiting conditional duration distribution concerns extremely rare successful returns; it says nothing about a typical return. No uniform estimate is claimed for varying \(r\), \(L\), or nonharmonic return potentials. Standard drifted-Brownian first-passage theory implies some ingredients, so implicit prior derivations of the assembled joint law cannot be ruled out by literature searching alone. Independent scientific verification has not been conducted.

## References

- A. Dubey and A. Pal, *Towards synergy between theory and experiments: First-passage processes under resetting with stochastic return protocols*, arXiv:2610.18814 (first public version 13 October 2026), https://arxiv.org/abs/2610.18814.
- D. Frydel, *Search by Return: Stochastic Resetting in Fluctuating Harmonic Potentials*, arXiv:2511.14646 (first public version 18 November 2025), https://arxiv.org/abs/2511.14646.
- Biswas and collaborators, work on general two-stage first-passage renewal with finite-time returns, arXiv:2406.08975, https://arxiv.org/abs/2406.08975.
