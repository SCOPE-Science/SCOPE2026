# Exact drift-dependent diffusivity and weak-reset enhancement in an asymmetric Brownian ratchet

## Finding

For a Brownian particle freely diffusing between Poissonian instantaneous projections to the minima of an asymmetric periodic ratchet, the **centered** effective diffusivity has an explicit formula that accounts for the dependence between cycle displacement and cycle duration. This extends the previously published exact current calculation to the unwrapped displacement variance. For every fixed threshold asymmetry, the diffusivity is **strictly enhanced at sufficiently small positive resetting rate**, whereas it tends to zero as the rate becomes large. More precisely, for the definitions below,

\[
\boxed{\frac{D_{\mathrm{eff}}}{D}=\frac{\ell^2}{2}S(\ell,\delta)+\frac{\ell^3}{2}M(\ell,\delta)\,\partial_{\ell}M(\ell,\delta)}.
\]

The second term is strictly negative for every asymmetric threshold \(\delta\ne 1/2\) and zero at the symmetric threshold. The weak-rate law is

\[
\boxed{\frac{D_{\mathrm{eff}}}{D}=1+\left[\frac1{24}+\frac12\left(\delta-\frac12\right)^2\right]\frac{rL^2}{D}+O_{\delta}\!\left(\frac{r^2L^4}{D^2}\right)}.
\]

In particular, the asymmetry increases the leading positive coefficient by exactly half the squared threshold displacement; for each fixed \(0<\delta<1\), at least one finite resetting rate maximizes the diffusivity above the unreset value \(D\). Uniqueness of that maximizer is **not** asserted.

## Assumptions and scope

Fix \(L,D,r>0\) and \(0<\delta<1\), and put \(a=\delta L\). Start at \(X_0=0\). Between the points of an independent rate-\(r\) Poisson process, \(X\) evolves by \(dX_t=\sqrt{2D}\,dB_t\). At each such point, the particle is projected instantaneously onto the nearest *ratchet-attracting minimum*, not necessarily onto the geometrically nearest lattice point:

\[
X_t=L\left\lceil\frac{X_{t-}-a}{L}\right\rceil.
\]

Endpoints of projection cells have probability zero and can be assigned arbitrarily. Thus the attraction basin of the minimum \(nL\) is \(((n-1)L+a,nL+a]\). Observe \(X_t\) on the **unwrapped real line**, not modulo \(L\). The infinite-potential-strength projection is the instantaneous limit of the sawtooth ratchet discussed in Roberts–Sezik–Lardet (2024); finite-strength potential or finite return time are excluded.

Define the velocity and centered effective diffusivity by

\[
v=\lim_{t\to\infty}\frac{\mathbb E[X_t]}t,\qquad
D_{\mathrm{eff}}=\lim_{t\to\infty}\frac{\operatorname{Var}(X_t)}{2t}.
\]

Write \(\ell=L\sqrt{r/D}\), \(u=e^{-\delta\ell}\), \(w=e^{-(1-\delta)\ell}\), \(q=e^{-\ell}\), and define

\[
M(\ell,\delta)=\frac{u-w}{2(1-q)},\qquad
S(\ell,\delta)=\frac{(u+w)(1+q)}{2(1-q)^2}.
\]

Both limits exist and are finite, and \(v=rLM(\ell,\delta)\). The formula is invariant under replacing \(\delta\) with \(1-\delta\), which reverses drift but does not change dispersion.

## Proof

**1. Cycle statistics.** Let \(T\) denote an exponential waiting time of rate \(r\) and let \(Y=\sqrt{2D}B_T\). The Brownian resolvent gives the bilateral Laplace density

\[
p_Y(y)=\frac{\lambda}{2}e^{-\lambda|y|},\qquad \lambda=\sqrt{r/D}.
\]

The completed-cycle displacement is \(J=L\lceil(Y-a)/L\rceil\). For every integer \(k\ge1\), the tails are

\[
\Pr(J\ge kL)=\tfrac12e^{-\lambda(a+(k-1)L)},\qquad
\Pr(J\le-kL)=\tfrac12e^{-\lambda(L-a+(k-1)L)}.
\]

Summing these geometric tails, using \(\mathbb E[Z]=\sum_{k\ge1}(\Pr(Z\ge k)-\Pr(Z\le-k))\) and \(\mathbb E[Z^2]=\sum_{k\ge1}(2k-1)(\Pr(Z\ge k)+\Pr(Z\le-k))\) for integer \(Z\), yields

\[
\mathbb E[J]=LM(\ell,\delta),\qquad \mathbb E[J^2]=L^2S(\ell,\delta).
\]

The successive pairs \((J_i,T_i)\) are independent and identically distributed; crucially, \(J_i\) and \(T_i\) **within a pair are not independent**.

**2. Centered regenerative dispersion.** The renewal-reward law gives \(v=\mathbb E[J]/\mathbb E[T]=r\mu\), where \(\mu=\mathbb E[J]\). As all cycle moments are finite (exponential waiting times and exponentially decaying jump tails), the regenerative variance law yields

\[
2D_{\mathrm{eff}}=\frac{\mathbb E[(J-vT)^2]}{\mathbb E[T]}=r\mathbb E[(J-r\mu T)^2].
\]

To justify this for the actual continuous trajectory, rather than merely the lattice position at the latest reset: the unfinished cycle contributes a Brownian displacement whose second moment is uniformly bounded by \(2D/r\). The completed-cycle variance grows linearly; Cauchy–Schwarz then shows the residual and its cross term are \(o(t)\) after division by \(t\). The regenerative renewal law also gives a bounded error in \(\mathbb E[X_t]-vt\), so the centered and variance formulations agree.

Differentiate the exact integral \(\mu(r)=\int_0^\infty re^{-rs}\mathbb E[J\mid T=s]ds\) at fixed \(D,L,\delta\). Exponential moment bounds justify differentiation and yield

\[
\mathbb E[JT]=\frac{\mu(r)}r-\mu'(r).
\]

Using \(\mathbb E[T^2]=2/r^2\), one obtains

\[
D_{\mathrm{eff}}=\frac r2\mathbb E[J^2]+r^2\mu(r)\mu'(r).
\]

Since \(d\ell/dr=\ell/(2r)\), substitution gives precisely the displayed explicit formula. Omitting the second term would incorrectly treat a biased resetting walk as a compound Poisson process with independent marks.

**3. Strict sign of the clock–jump correction.** Put \(c=|1-2\delta|\in(0,1)\) when \(\delta\ne1/2\), and \(y=\ell/2\). Then

\[
|M|=\frac{\sinh(cy)}{2\sinh y},\qquad
\partial_y\log|M|=c\coth(cy)-\coth y<0.
\]

The inequality follows since \(z\mapsto z\coth z\) is strictly increasing on \((0,\infty)\): its derivative has numerator \(\sinh z\cosh z-z>0\). Therefore \(M\partial_\ell M<0\) for \(\delta\ne1/2\), and the correction vanishes when \(\delta=1/2\).

**4. Strict weak-resetting enhancement and large-rate suppression.** Direct Taylor expansion at \(\ell=0\), with fixed \(\delta\), gives

\[
M=\frac12-\delta+O_\delta(\ell^2),\qquad
S=\frac2{\ell^2}+\delta^2-\delta+\frac13+O_\delta(\ell^2).
\]

Thus \(\ell^3M\partial_\ell M=O_\delta(\ell^4)\), proving the asserted small-rate expansion with the strictly positive coefficient \(1/24+(\delta-1/2)^2/2\).

At fixed \(0<\delta<1\), put \(d=\min(\delta,1-\delta)>0\). For \(\delta\ne1/2\), direct inspection of the exponentials yields

\[
\frac{D_{\mathrm{eff}}}{D}\sim\frac{\ell^2}{4}e^{-d\ell}
\quad (\ell\to\infty),
\]

while at \(\delta=1/2\) the exact specialization is

\[
\frac{D_{\mathrm{eff}}}{D}=\frac{\ell^2}{4}\operatorname{csch}(\ell/2)\coth(\ell/2)
\sim\frac{\ell^2}{2}e^{-\ell/2}.
\]

Both tend to zero. By continuity, strict enhancement for all sufficiently small positive \(r\), and decay to zero for large \(r\), a global maximizer with value above \(D\) exists at some finite positive resetting rate. No uniqueness or closed form for that rate is inferred.

## Verification

The independent standard-library script `verify.py` evaluates \(M,S,D_{\mathrm{eff}}\) in two ways: closed formulas and separately summed bilateral-Laplace threshold tails. The latter also computes the mixed clock–jump moment from tail identities \(\mathbb E[rT\mathbf1_{Y>z}]=\tfrac12e^{-\lambda z}(1+\lambda z/2)\), rather than differentiating the closed-form \(M\). It then checks weak-rate coefficients, parity under \(\delta\mapsto1-\delta\), positivity, high-rate suppression and the symmetric published formula. The observed run passed 262 deterministic assertions. These finite numerical checks supplement, but do not substitute for, the exact proof above.

For the asymmetric witness \(\delta=1/4\), \(\ell=8\), the exact expression evaluates to \(D_{\mathrm{eff}}/D\approx1.934807543062\), compared with approximately \(1.169\) as the optimum in the *different nearest-site symmetric model* of Alston–Bertrand. This is not a contradiction: for \(\delta\ne1/2\), the present asymmetric attraction basins do not implement geometric nearest-site resetting.

## Relationship to prior work

Roberts, Sezik and Lardet (2024), arXiv:2405.10698, established the sawtooth ratchet and its exact instantaneous-limit **current**. The present formula uses and agrees with that current, but additionally determines the centered long-time position variance and the temporal clock–jump covariance correction; their current/efficiency calculations do not supply those assertions.

Alston and Bertrand (2024), arXiv:2401.12772, proved exact diffusivity and enhancement for *geometrically nearest-site* local resetting. At the symmetric basin \(\delta=1/2\), the formula here specializes to their exact lattice expression. Their nearest-site global enhancement bound does not cover the asymmetric attraction projector. This symmetric identity is a check, **not** a new finding.

Ghosh et al. (2023), arXiv:2307.06202, numerically studied velocity and diffusivity for a Brownian ratchet with the substrate potential active during diffusion, unlike the free-diffusion stage here. Liu et al. (2024), DOI:10.1002/cphc.202400313, treated fat-tailed resetting and described diffusivity mainly through numerical observations, not this all-parameter exponential-clock formula.

The renewal-reward variance identity is classical. The specific exact asymmetric two-parameter evaluation, its strictly negative clock–jump correction, and the all-asymmetry weak-rate enhancement with explicit coefficient constitute the contribution assessed here. No claim of absolute publication priority or independent certification is made.

## Limitations

The theorem concerns the singular instantaneous-return ratchet, Poisson clocks, Brownian free stages, fixed \(0<\delta<1\), infinite periodic lift, and centered asymptotic diffusivity. It does **not** cover finite relaxation times, spatial forces during diffusion, non-Poisson switching, microscopic energetic costs, parameter estimation or uniqueness of the maximizing rate. The high-rate asymptotics are not uniform in \(\delta\) as \(\delta\to0,1\). Published unindexed work could affect the priority assessment. No independent audit has been performed.

## References

- C. Roberts, E. Sezik, E. Lardet, *Ratchet-mediated resetting: Current, efficiency, and exact solution*, arXiv:2405.10698 (first posted 17 May 2024), https://arxiv.org/abs/2405.10698.
- H. Alston, T. Bertrand, *Boosting macroscopic diffusion with local resetting*, arXiv:2401.12772 (first posted 23 January 2024), https://arxiv.org/abs/2401.12772.
- P. K. Ghosh, S. Nayak, J. Liu, Y. Li, F. Marchesoni, *Autonomous Ratcheting by Stochastic Resetting*, arXiv:2307.06202 (first posted 12 July 2023), https://arxiv.org/abs/2307.06202.
- J. Liu, Y. Li, P. K. Ghosh, S. Nayak, F. Marchesoni, *Ratcheting by Stochastic Resetting With Fat-Tailed Time Distributions*, ChemPhysChem (first published 12 August 2024), https://doi.org/10.1002/cphc.202400313.
