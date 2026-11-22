# Universal ballistic wall-pressure onset and a nonanalytic residence-time signature

## Finding

A symmetric finite-speed run-and-tumble particle between two sticky walls has a universal *first* opposite-wall pressure-correlation slope at the earliest possible travel time, even when the two independent wall-residence distributions are arbitrary and non-Markovian. The *next* right-hand term exposes their small-time release exponents.

Fix speed \(v>0\), separation \(L>0\), and bulk reversal rate \(\gamma>0\). At wall \(i\in\{0,L\}\), each arrival produces a new independent, strictly positive holding time \(S_i\) with distribution function \(F_i\) and finite positive mean \(m_i\). The particle leaves that wall pointing inward. Define

\[
\tau=\frac Lv,\qquad c=\frac1{2L+v(m_0+m_L)},\qquad q_i=vc m_i.
\]

Let \(B_i(t)\) indicate occupation of wall \(i\) in the unique stationary process and set \(C_{0L}(t)=\mathbb E[B_0(0)B_L(t)]-q_0q_L\). Then for \(0\le t\le\tau\),

\[
C_{0L}(t)=-q_0q_L,
\]

whereas, for \(\varepsilon\downarrow0\),

\[
\boxed{\quad C_{0L}(\tau+\varepsilon)+q_0q_L
=vc e^{-\gamma\tau}\varepsilon+o(\varepsilon).\quad}
\]

Suppose additionally that, for both walls, \(F_i(s)=a_i s^{\beta_i}+o(s^{\beta_i})\) as \(s\downarrow0\), with \(a_i>0\) and \(0<\beta_i<1\). Define \(\beta=\min\{\beta_0,\beta_L\}\) and \(a_* =\sum_{i:\,\beta_i=\beta}a_i\). Then the sharper law is

\[
\boxed{\quad C_{0L}(\tau+\varepsilon)+q_0q_L
=vc e^{-\gamma\tau}\left[\varepsilon-\frac{a_*}{1+\beta}\varepsilon^{1+\beta}
+o(\varepsilon^{1+\beta})\right].\quad}
\]

The same statements hold with left and right interchanged. In particular, the leading arrival slope depends on each holding law only through its mean; the first genuinely nonanalytic correction determines the smaller short-hold exponent (and the sum of the associated coefficients). For \(N\) independent stationary particles with individual outward force magnitude \(f_0>0\), the covariance of the total forces has the displayed formula multiplied by \(Nf_0^2\).

## Assumptions and scope

The state consists of a position \(X_t\in[0,L]\), an interior orientation \(+1\) or \(-1\), and an attached state at each wall. Interior motion is deterministic at velocity \(v\) times orientation. An independent rate-\(\gamma\) Poisson process reverses orientation in the interior. When an outward-moving particle meets a boundary, it stays at that boundary for an independently sampled time with the specified wall-dependent law, with no interior reversals during adhesion. It is released with the only inward orientation. Each new wall visit draws a fresh independent holding time, independent of interior reversals and all other holds. No absorption, translational Brownian diffusion, interparticle interactions, or resetting occurs.

The initial law is the equilibrium renewal law, not a fresh wall-arrival law. Positive finite means give positive recurrence. Holding times may have atoms away from zero and need no second moment. The fractional refinement assumes each of the two stated small-time asymptotics and strictly subunit exponents; no assertion about the second coefficient is made for exponents greater than or equal to one, where bulk reversals contribute at the same order.

## Proof

**Stationary normalization.** The invariant interior plus/minus orientation occupation measures have equal constant spatial densities \(c\), since their kinetic forward equations admit zero net flux and constant density. At a wall, visits arrive at rate \(vc\); renewal-reward balance yields attached mass \(q_i=vc m_i\). Their total probability is \(2Lc+q_0+q_L=1\), establishing the stated \(c\). Regeneration at successive visits, the positive probability of eventual cross-wall travel, and finite wall means give the unique stationary law. A standard finite-speed telegraph first-wall hitting time has finite mean on a finite interval; a uniform geometric-block bound in fact gives finite exponential moments for its bulk excursion time.

**Stationary residual life.** Conditioned on \(B_0(0)=1\), the remaining left-wall holding time \(R_0\) has a continuous residual-life distribution, even if \(S_0\) has atoms. Its density at almost every \(s\ge0\) is

\[
r_0(s)=\frac{1-F_0(s)}{m_0}.
\]

Thus \(q_0 r_0(s)=vc[1-F_0(s)]\). This equilibrium-renewal factor is essential: replacing \(R_0\) by a fresh copy of \(S_0\) changes the onset.

**Earliest opposite-wall path.** A trajectory initially attached to wall zero cannot be at wall \(L\) before time \(\tau=L/v\), because its net spatial displacement is \(L\) while its interior speed magnitude is at most \(v\). At time \(\tau+\varepsilon\), the contribution to \(\Pr(B_0(0)=1,B_L(\tau+\varepsilon)=1)\) from trajectories that (i) release initially at time \(s\le\varepsilon\), (ii) cross without a single bulk reversal, and (iii) remain on their first opposite-wall hold is exactly

\[
K(\varepsilon)=vc e^{-\gamma\tau}
\int_0^\varepsilon [1-F_0(s)] [1-F_L(\varepsilon-s)]\,\mathrm ds.
\tag{1}
\]

The no-reversal factor is \(e^{-\gamma\tau}\); the first factor inside the integral comes from the equilibrium residual, the second from survival of the fresh right-wall hold.

**Control of all other trajectories.** Every path counted in the joint probability but not in (1) must have an initial residual \(s\le\varepsilon\), and one of the following events after release. Either it reaches the opposite wall after a nonstraight excursion, or it reaches that wall directly, leaves it and returns before observation. A nonstraight crossing within \(\tau+\varepsilon-s\) has total backwards-going interior time at most \(\varepsilon/2\). If the particle reverses before first hitting either boundary, it therefore must make two Poisson reversals with separation at most \(\varepsilon/2\); or its first reversal is within \(\varepsilon/2\) after departure, permitting a brief return to the initial boundary. The probability of the first event in a bounded time interval is \(O(\varepsilon)\) by the Poisson two-point union bound, and of the second is \(O(\varepsilon)\) by the exponential first-flip bound. If it first reaches the opposite wall by a straight flight but then returns to that same wall, its inward departure requires at least one further bulk reversal in the remaining at most \(\varepsilon\) time, again with probability \(O(\varepsilon)\). The same estimates apply if additional boundary visits occur. Since \(\Pr(R_0\le\varepsilon)\le\varepsilon/m_0\), the total uncounted joint mass is \(O(\varepsilon^2)\). Constants can depend on fixed \(L,v,\gamma,m_0\), but not on the shape of either waiting-time distribution. Consequently,

\[
\Pr(B_0(0)=1,B_L(\tau+\varepsilon)=1)
=K(\varepsilon)+O(\varepsilon^2).
\tag{2}
\]

**Sharp fractional expansion.** For any strictly positive wall holds, \(F_i(s)\to0\) at zero, so the integral in (1) is \(\varepsilon+o(\varepsilon)\), proving the universal onset. For the stated power laws, integrate the product expansion:

\[
\begin{aligned}
\int_0^\varepsilon[1-F_0(s)][1-F_L(\varepsilon-s)]\,\mathrm ds
&=\varepsilon-\frac{a_0}{1+\beta_0}\varepsilon^{1+\beta_0}
-\frac{a_L}{1+\beta_L}\varepsilon^{1+\beta_L}\\
&\quad+o(\varepsilon^{1+\beta}).
\end{aligned}
\]

Here the positive product term is \(O(\varepsilon^{1+\beta_0+\beta_L})=o(\varepsilon^{1+\beta})\). Because \(\beta<1\), the error in (2) is \(O(\varepsilon^2)=o(\varepsilon^{1+\beta})\). Keep precisely the terms with minimal exponent and subtract the stationary product \(q_0q_L\). Interchanging the two walls gives the same result by the identical argument.

## Verification

Run `python verification/check_front.py` using Python's standard library. The script checks equilibrium normalization, the exact straight-path convolution for independent non-Markov Beta holding laws \(F_0(s)=s^{1/2}\) and \(F_L(s)=s^{3/4}\) on \([0,1]\), its beta-function evaluation and short-time coefficient, and a closed-form exponential-holding reduction. Independent direct event-driven simulations include bulk reversals, boundary holds and repeated arrivals; their observed cross-wall probability agrees with the straight-path lower contribution plus the predicted small correction. Simulation is diagnostic only. The finite-speed decomposition, equilibrium residual identity and Poisson event bounds above establish the theorem for every admissible law.

## Relationship to prior work

Li, Eichhorn and Dabelow (2026) derive the one-dimensional mean active-gas pressure in a box for standard run-and-tumble motion; the model's stationary pressure and hard-wall accumulation are prior art, not a claimed contribution. Angelani's confined run-and-tumble treatment likewise establishes the sticky-wall stationary law for exponential turning. Bressloff's 2023 occupation-time propagator and 2026 Bressloff–Linn renewal method provide antecedents for sticky-boundary and non-Markovian waiting-time analysis. The claim here is restricted to the exact *first possible opposite-wall two-time pressure event* and its universal slope and wall-residence fractional correction. Previously published explicit two-wall *integrated long-time* pressure covariance formulas do not give this short-lag law; likewise published non-Poisson wall-dwell dispersion formulas concern a distinct sliding-wall transport observable. The relevant comparison full texts and access limitations are described in the accompanying review. Novelty beyond inspected sources is not a proof of priority.

## Limitations

This is a sharp onset theorem, not an all-time joint wall-force distribution or spectral relaxation law. The model assumes finite-speed one-dimensional motion, independent renewal holds, independent Poisson interior flips, and a stationary initial ensemble. Wall forces are assumed constant while attached; a force-dependent residence law is not addressed. For equal subunit short-hold exponents, the coefficient identifies only the sum of amplitudes, not each wall separately. No inference-stability theorem from noisy data, higher-dimensional extension, interacting-gas result, or claim for second asymptotic order at exponent one or above is supplied. Publication priority has residual uncertainty because some contemporaneous primary full texts were inaccessible; independent scientific audit is not performed.

## References

1. S. Li, R. Eichhorn and L. Dabelow, *Ideal gas of active particles in a box*, arXiv:2610.01287v1 (first public 1 October 2026), https://arxiv.org/abs/2610.01287 .
2. L. Angelani, *Confined run-and-tumble swimmers in one dimension*, Journal of Physics A **50** (2017), author manuscript https://arxiv.org/abs/2206.03123 .
3. P. C. Bressloff, *Encounter-based model of a run-and-tumble particle II: absorption at sticky boundaries*, arXiv:2302.01158v1 (2023), https://arxiv.org/abs/2302.01158 .
4. P. C. Bressloff and S. Linn, *Renewal theory for a run-and-tumble particle with stochastic resetting and a sticky boundary*, Physical Review E **113**, 054122 (2026), https://arxiv.org/abs/2602.02446 .
5. T. Pietrangeli, C. Ybert, C. Cottin-Bizonne and F. Detcheverry, *Optimal run-and-tumble in slit-like confinement*, Phys. Rev. Research **6**, 023028 (2024), https://arxiv.org/abs/2404.07680 .
