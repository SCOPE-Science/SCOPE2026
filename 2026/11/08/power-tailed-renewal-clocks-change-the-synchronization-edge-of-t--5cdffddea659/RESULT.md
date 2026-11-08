# Power-tailed renewal clocks change the synchronization edge of the Kuramoto model

## Finding

In the Lorentzian-frequency Kuramoto population, with all oscillator phases globally returned to the same Ott–Antonsen (OA) state at independent renewal times, a power-tailed reset clock produces a **three-regime classification of the stationary synchronization-amplitude density**. The central claim concerns the full stationary density and its sharp attractor-edge asymptotics, including a critical tail-exponent threshold, reciprocal-moment thresholds, and a universal two-sided near-critical crossover profile.

Let \(K>0\), \(\sigma>0\), \(0<r_0\leq1\), and \(b=K/2\), \(a=K/2-\sigma\). Between common resets, the OA synchronization amplitude solves
\[
\dot r=ar-br^3,\qquad r(0)=r_0.
\]
Suppose the independent inter-reset duration \(T\) has a continuous distribution, positive survival \(S(t)=\Pr(T>t)\) for finite \(t\), finite mean \(\mu\), and
\[
S(t)\sim c t^{-q}\quad(t\to\infty),\qquad c>0,\quad q>1.
\]
Write \(R\) for the stationary synchronization amplitude and assume that \(r_0\) is not already a deterministic equilibrium. Then \(R\) has a density, on the open interval between \(r_0\) and the attracting equilibrium, given exactly by
\[
\boxed{p_R(r)=\frac{S(t(r))}{\mu\,|ar-br^3|}},
\]
where \(t(r)\) is the unique positive time at which the unreset trajectory reaches \(r\). This formula is normalized and has no equilibrium atom.

Its sharp boundary laws are as follows.

**Subcritical coupling** \(0<K<2\sigma\): put \(\delta=\sigma-K/2>0\) and
\[
C_-=\frac{r_0}{\sqrt{1+(b/\delta)r_0^2}}.
\]
As \(r\downarrow0\),
\[
p_R(r)\sim\frac{c\delta^{q-1}}{\mu\,r[\log(C_-/r)]^q},\qquad
\Pr(R<\varepsilon)\sim\frac{c\delta^{q-1}}{\mu(q-1)}[\log(C_-/\varepsilon)]^{1-q}.
\]
In particular the density diverges at zero for **every** power-law exponent \(q>1\).

**Critical coupling** \(K=2\sigma\): here \(b=\sigma\), and as \(r\downarrow0\),
\[
\boxed{p_R(r)\sim\frac{2c(2b)^{q-1}}{\mu}\,r^{2q-3}},\qquad
\Pr(R<\varepsilon)\sim\frac{c(2b)^{q-1}}{\mu(q-1)}\,\varepsilon^{2(q-1)}.
\]
The endpoint density diverges for \(1<q<3/2\), tends to the positive constant \(2c\sqrt{2b}/\mu\) for \(q=3/2\), and vanishes for \(q>3/2\). This is a sharp critical exponent boundary.

**Supercritical coupling** \(K>2\sigma\): let \(r_*=\sqrt{a/b}\), require \(r_0\ne r_*\), and put
\[
C_+=\frac{r_*}{2}\left|\frac{r_*^2}{r_0^2}-1\right|.
\]
As \(d=|r-r_*|\downarrow0\) along the trajectory,
\[
p_R(r)\sim\frac{c(2a)^{q-1}}{\mu\,d[\log(C_+/d)]^q},\qquad
\Pr(|R-r_*|<\varepsilon)\sim\frac{c(2a)^{q-1}}{\mu(q-1)}[\log(C_+/\varepsilon)]^{1-q}.
\]
The stationary density therefore diverges integrably at the nonzero synchronization attractor for every such clock.

The transition admits a **universal two-sided boundary-layer scaling**. Fix \(\sigma>0\), \(r_0>0\), and the renewal clock, and set \(K_\pm=2(\sigma\pm\eta)\), \(b_\pm=\sigma\pm\eta\), for \(\eta>0\) sufficiently small. For each fixed \(z>0\), define
\[
\rho_- (\eta,z)=\sqrt{\frac{\eta z}{b_-}},\qquad
\rho_+(\eta,z)=\sqrt{\frac{\eta(1+z)}{b_+}}.
\]
Then the stationary amplitude distributions on both sides of the coupling threshold have the **same sharp crossover**:
\[
\boxed{\lim_{\eta\downarrow0}\eta^{1-q}\Pr_{K_\pm}(R\le\rho_\pm(\eta,z))
=\frac{c\,2^{q-1}}{\mu(q-1)}[\log(1+1/z)]^{1-q}.}
\]
The limit is locally uniform for \(z\in(0,\infty)\). It describes the low-amplitude probability mass at a shrinking scale as the interaction strength passes through the synchronization threshold, without requiring a special one-parameter family of waiting-time distributions.

The same three cases yield **sharp reciprocal synchronization-moment thresholds** for every \(s>0\):
\[
\mathbb E[R^{-s}]\begin{cases}
=\infty,&0<K<2\sigma,\\
<\infty\ \text{exactly when }s<2(q-1),&K=2\sigma,\\
<\infty,&K>2\sigma.
\end{cases}
\]
At the critical equality \(s=2(q-1)\) the moment diverges. These are stationary-ensemble statements, not finite-population claims.

## Assumptions and scope

The model consists of the infinite-population Lorentzian-frequency Kuramoto system restricted to the OA manifold. A single common renewal clock instantaneously resets **all phases** to the same initial OA state with amplitude \(r_0\). The bare evolution between resets is deterministic. The renewal intervals are independent and identically distributed and independent of that evolution. The nonarithmetic assumption follows from the continuous duration distribution; the survival is asymptotic to the stated pure power, not merely bounded by one. The origin is not included as an initial reset amplitude.

For arbitrary finite-mean reset intervals the exact density formula still holds, but the three displayed asymptotic equivalents require the stated tail. If \(K>2\sigma\) and \(r_0=r_*\), the amplitude is constant and its stationary law is instead a point mass; that excluded case does not have the displayed continuous density.

The attractive equilibrium equals \(0\) when \(K\le2\sigma\), and \(r_*=\sqrt{1-2\sigma/K}\) when \(K>2\sigma\). The results use physical continuous time and the long-time equilibrium-renewal ensemble. The stationary law is that of the order-parameter amplitude across realizations of the **common** resetting clock; it is not a deterministic mean-field order parameter resulting from independent reset clocks for each oscillator.

## Proof

**1. Bare OA orbit and inverse clock.** The OA equation is \(\dot r=ar-br^3\). Writing \(y=r^2\) gives \(\dot y=2ay-2by^2\). Thus if \(a\ne0\),
\[
\frac1{r(t)^2}=\frac ba+\left(\frac1{r_0^2}-\frac ba\right)e^{-2at},\qquad
t(r)=\frac1{2a}\log\left(\frac{r_0^{-2}-b/a}{r^{-2}-b/a}\right).
\]
The logarithm is of a strictly positive ratio on the moving orbit. If \(a=0\), integration instead gives
\[
r(t)=\frac{r_0}{\sqrt{1+2br_0^2t}},\qquad
t(r)=\frac{r^{-2}-r_0^{-2}}{2b}.
\]
Except at a fixed starting equilibrium, the orbit is strictly monotone in time and has a nonzero velocity at every interior amplitude.

**2. Stationary age and exact push-forward.** The renewal reward theorem, or equivalently the limiting backward recurrence law for a nonarithmetic finite-mean renewal process, gives the age since the latest reset the density
\[
f_A(t)=\frac{S(t)}\mu,\qquad t\ge0.
\]
Indeed \(\int_0^\infty S(t)\,dt=\mu\), so it is normalized. The amplitude is exactly \(R=r(A)\); the monotone change of variables \(dt/dr=1/(ar-br^3)\) yields the claimed density. It has total mass one and no atom at the limiting equilibrium, since that equilibrium is approached only at infinite age.

Moreover, for the event of being within \(\varepsilon\) of the attracting equilibrium, the orbit reaches the corresponding amplitude at \(t_\varepsilon\) and monotonicity yields
\[
\Pr(\text{distance from attractor}<\varepsilon)
=\Pr(A>t_\varepsilon)=\frac1\mu\int_{t_\varepsilon}^\infty S(u)\,du.
\]
The clock-tail assumption and direct integration of power bounds imply
\[
\Pr(A>t)\sim\frac{c}{\mu(q-1)}t^{1-q}.
\]

**3. Subcritical endpoint.** With \(a=-\delta<0\), the exact orbit simplifies to
\[
r(t)=\frac{r_0e^{-\delta t}}{\sqrt{1+(b/\delta)r_0^2(1-e^{-2\delta t})}}
\sim C_-e^{-\delta t}.
\]
Consequently \(t(r)\sim\delta^{-1}\log(C_-/r)\), while \(|ar-br^3|\sim\delta r\). Substitution into the exact density and integrated-age tail proves both subcritical equivalents.

**4. Critical endpoint.** At \(a=0\), the exact inverse satisfies \(t(r)\sim(2br^2)^{-1}\), and \(|\dot r|=br^3\). Thus \(S(t(r))\sim c(2b)^q r^{2q}\), proving the density coefficient and exponent. The integrated-age tail proves the probability equivalent. Its exponent \(2q-3\) changes sign precisely at \(q=3/2\).

**5. Supercritical endpoint.** For \(a>0\), set \(B=r_*^2/r_0^2-1\ne0\). Then
\[
r(t)=r_*(1+Be^{-2at})^{-1/2},\qquad
|r(t)-r_*|\sim C_+e^{-2at}.
\]
Hence \(t\sim(2a)^{-1}\log(C_+/d)\) and \(|ar-br^3|\sim2ad\), giving the two supercritical equivalents by the same substitutions.

**6. Universal two-sided near-critical crossover.** Fix \(z>0\) and sufficiently small \(\eta\), so that both \(\rho_-(\eta,z)\) and \(\rho_+(\eta,z)\) lie below the fixed starting amplitude \(r_0\). For subcritical \(a=-\eta\), the reciprocal-square flow formula at \(r=\rho_-\) gives the exact crossing time
\[
t_-(\eta,z)=\frac{\log(1+1/z)-\log(1+\eta/(b_-r_0^2))}{2\eta}.
\]
For supercritical \(a=+\eta\), the fixed point \(r_*^2=\eta/b_+\) lies below \(\rho_+^2\), and the same inverse flow gives
\[
t_+(\eta,z)=\frac{\log(1+1/z)+\log(1-\eta/(b_+r_0^2))}{2\eta}.
\]
Both expressions equal \(\log(1+1/z)/(2\eta)+O(1)\) as \(\eta\downarrow0\), locally uniformly on compact positive \(z\)-intervals. Since both orbits decrease through their stated cutoffs, their lower-tail probabilities equal the equilibrium-age tail at these crossing times, namely \(\mu^{-1}\int_{t_\pm}^\infty S(u)\,du\). Inserting the integrated survival equivalent from Step 2 proves the stated common limit and its local uniformity. This also shows why the scaling is the same on either side of criticality despite their different fixed points.

**7. Reciprocal moments.** In the subcritical case the near-zero density times \(r^{-s}\) has a divergent integral for every \(s>0\), since an algebraic reciprocal overwhelms any logarithmic damping. At criticality its integrability is equivalent to \(\int_0^1 r^{2q-3-s}\,dr<\infty\), i.e. \(s<2(q-1)\); equality diverges logarithmically. In the supercritical case \(R\) remains in the compact interval with strictly positive endpoints \(r_0\) and \(r_*\), hence all reciprocal moments are finite.

## Verification

The standalone Python 3 script `check.py` uses only the standard library. Run `python3 check.py`. It independently evaluates the time flow and inverse, compares the analytical velocity with centered finite differences, checks density normalization by numerical quadrature in age, tests attractor probability equivalents, checks both sides of the critical \(q=3/2\) boundary, and checks an additional non-Lomax power-tailed clock. The recorded run passed 753 deterministic diagnostic assertions, including the two-sided near-critical crossover.

For illustration with \(\sigma=b=\tau=1\) and \(r_0=0.8\), the critical density at \(r=0.001\) equals approximately \(18.80300518\) for \(q=1.25\), \(1.41421263\) for \(q=1.5\), and \(0.003999997\) for \(q=2\). These numbers verify the three qualitatively different endpoint trends. Numerical diagnostics are finite, while Steps 1–7 establish the full continuum theorem.

## Relationship to prior work

Sarkar and Gupta [1] derive the OA amplitude equation and the stationary order-parameter densities for **exponentially distributed reset times** (notably their equations (18), (22), (29), (34), and (54)). Their critical Poisson density decays to zero at the incoherent boundary, whereas the present algebraically tailed renewal clock has the sharp \(q=3/2\) boundary separating divergence from vanishing. This result does not claim originality for the OA differential equation or its Poisson specialization.

Masó-Puigdellosas, Campos and Méndez [2] develop the general renewal/backward-age formalism for diffusive motion with non-Poissonian resetting, including the basic age/renewal composition. The generic equilibrium-age law used here is classical; the Kuramoto-specific critical exponent, all-coupling endpoint classification, reciprocal-moment cutoffs, and two-sided crossover are the proposed additional results.

Bressloff [3] studies stochastic density equations for locally or globally reset interacting systems and the Kuramoto OA dynamics, explicitly with Poisson shot resetting. The global-reset example corroborates the OA reduction but does not establish power-tail stationary edge laws. Work on subsystem resetting [4] examines only part of the oscillator system, a different dynamical model.

## Limitations

This result is an analytical consequence of the stated OA dynamics in the infinite-population limit; it is not a proof of the OA reduction for every microscopic initial density or a finite-population fluctuation theorem. It does not classify synchronized-phase behavior under independent per-oscillator resetting, and it excludes infinite-mean reset clocks, adaptive clocks, and reset states at fixed points. The stationary density equivalent requires a pure regularly varying tail with finite positive coefficient; oscillating slowly varying corrections can modify threshold-limit constants. The first-public-priority comparison cannot exclude unindexed literature containing a broader implicit composition theorem. No independent scientific audit has been performed.

## References

[1] M. Sarkar and S. Gupta, *Synchronization in the Kuramoto model in presence of stochastic resetting*, arXiv:2203.00339 (first publicly posted 2022-03-01), https://arxiv.org/abs/2203.00339.

[2] A. Masó-Puigdellosas, D. Campos, and V. Méndez, *Conditioned backward and forward times of diffusion with stochastic resetting: a renewal theory approach*, arXiv:2205.01613 (2022), https://arxiv.org/abs/2205.01613.

[3] P. C. Bressloff, *Global density equations for interacting particle systems with stochastic resetting: from overdamped Brownian motion to phase synchronization*, arXiv:2401.03501 (2024), https://arxiv.org/abs/2401.03501.

[4] R. Majumder, R. Chattopadhyay, and S. Gupta, *Kuramoto model subject to subsystem resetting: How resetting a part of the system may synchronize the whole of it*, arXiv:2402.14921 (2024), https://arxiv.org/abs/2402.14921.
