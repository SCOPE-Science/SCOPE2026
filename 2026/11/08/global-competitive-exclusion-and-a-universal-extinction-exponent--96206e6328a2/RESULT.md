# Global competitive exclusion and a universal extinction exponent in symmetric Ricker competition

## Finding

For \(R>0\) and \(\alpha>1\), consider the positive-quadrant map
\[
 F_{R,\alpha}(x,y)=\bigl(xe^{R-x-\alpha y},\;ye^{R-y-\alpha x}\bigr).
\]
For **every** initial condition \((x_0,y_0)\in(0,\infty)^2\) with \(x_0>y_0\), the first species persists, the second becomes extinct, and the extinction rate is exact:
\[
\liminf_{n\to\infty}x_n>0,\qquad
\lim_{n\to\infty}y_n=0,\qquad
\boxed{\lim_{n\to\infty}\frac{1}{n}\log y_n=-(\alpha-1)R}.
\]
Moreover, the persisting species has the universal Cesàro mean
\[
 \lim_{n\to\infty}\frac{1}{n}\sum_{j=0}^{n-1}x_j=R.
\]
The species-exchanged conclusion holds whenever \(y_0>x_0\). In particular, the selection is determined **solely by the initial ordering**, independently of the periodic or irregular dynamics of the surviving population. No convergence of the survivor to an equilibrium is assumed or asserted.

The boundary is sharp among positive coupling values: at \(\alpha=1\), the ratio \(x_n/y_n\) is conserved and both species persist for every positive initial condition; for each \(0<\alpha<1\) and sufficiently small \(R>0\), an open set of unequal initial populations converges to the positive coexistence equilibrium.

## Assumptions and scope

Here \(R\) is the logarithm of the multiplicative reproductive factor \(r=e^R>1\). The two species have exactly equal intrinsic growth factors and equal self-regulation coefficients, with common cross-competition coefficient \(\alpha>0\). Initial states are strictly positive. The phrase **persists** means \(\liminf_{n\to\infty}x_n>0\) for the winning species; the claimed extinction exponent concerns the original discrete time \(n\) and is not a continuous-time Lyapunov exponent. The theorem does not assume that the surviving scalar Ricker dynamics has a fixed or periodic attractor.

## Proof

**1. Forward positivity, boundedness, and ratio drift.** Positivity is immediate. Since \(ue^{-u}\le e^{-1}\) for every \(u>0\),
\[
 0<x_n,y_n\le M:=\max\{x_0,y_0,e^{R-1}\}\quad(n\ge0).
\]
Define \(q_n=\log(x_n/y_n)\). Subtraction of the two exact logarithmic recurrences gives
\[
 q_{n+1}-q_n=(\alpha-1)(x_n-y_n).
\]
Assume \(\alpha>1\) and \(x_0>y_0\). Then \(q_0>0\), and induction gives \(q_n\ge q_0>0\), \(x_n>y_n\), and strict increase of \(q_n\).

If \(q_n\) were bounded, the drift identity would imply \(\sum_{n\ge0}(x_n-y_n)<\infty\), so \(x_n-y_n\to0\). But \(x_n-y_n=y_n(e^{q_n}-1)\ge y_n(e^{q_0}-1)\), hence \(y_n\to0\), and then \(x_n\to0\). This is impossible: when both coordinates are sufficiently small, \(R-x_n-\alpha y_n\ge R/2>0\), implying \(x_{n+1}\ge e^{R/2}x_n\). Therefore \(q_n\to\infty\). The uniform upper bound on \(x_n\) now yields \(y_n=x_ne^{-q_n}\to0\).

**2. Uniform eventual persistence of the winner.** Put \(\delta=R/4\). Choose \(N\) so large that \(\alpha y_n\le R/4\) for all \(n\ge N\). Whenever \(n\ge N\) and \(x_n<\delta\),
\[
 x_{n+1}\ge e^{R/2}x_n.
\]
As \(x_n\le M\), there must be some \(k\ge N\) with \(x_k\ge\delta\). For each subsequent \(n\) with \(x_n\ge\delta\),
\[
 x_{n+1}\ge \delta\exp(3R/4-M).
\]
Consequently, setting \(m=\min\{\delta,\delta e^{3R/4-M}\}>0\), induction over the two cases \(x_n\ge\delta\) and \(m\le x_n<\delta\) proves \(x_n\ge m\) for every \(n\ge k\). Thus \(\log x_n\) remains bounded.

**3. Universal mean and extinction exponent.** The exact first-component identity telescopes to
\[
 \log\frac{x_n}{x_0}=nR-\sum_{j=0}^{n-1}x_j-\alpha\sum_{j=0}^{n-1}y_j.
\]
Divide by \(n\). Since \(\log x_n\) is bounded and \(y_j\to0\), Cesàro summation gives \(n^{-1}\sum_{j<n}x_j\to R\). The corresponding second-component identity is
\[
 \frac{1}{n}\log\frac{y_n}{y_0}
 =R-\frac{1}{n}\sum_{j<n}y_j-\alpha\frac{1}{n}\sum_{j<n}x_j,
\]
whose right-hand side tends to \(R-\alpha R=-(\alpha-1)R\). Exchanging the coordinates completes the main assertion. Since the limiting logarithmic rate is strictly negative, the loser in fact becomes exponentially small; no uniform prefactor is asserted.

**4. Sharpness of the coupling threshold.** For \(\alpha=1\), the same ratio identity gives \(x_n/y_n=x_0/y_0\) for all \(n\). The sum \(s_n=x_n+y_n\) obeys the scalar Ricker recurrence \(s_{n+1}=s_ne^{R-s_n}\). For \(R>0\), its positive orbit eventually enters a bounded interval away from zero: below \(R/4\) the sum grows by at least \(e^{3R/4}\), while a crossing above \(R/4\), together with the universal upper bound, provides a positive post-crossing floor. Thus both species persist. For \(0<\alpha<1\), the positive fixed point \(x=y=R/(1+\alpha)\) has eigenvalues \(1-R\) and \(1-R(1-\alpha)/(1+\alpha)\). Both have modulus below one for \(0<R<1\), so its open local basin contains unequal initial pairs and excludes global competitive elimination. This establishes sharpness.

## Verification

The accompanying standard-library program `verify.py` checks the exact ratio and telescoping identities algebraically by their evaluated one-step residuals, and numerically checks the extinction exponent for low, intermediate, and oscillatory/high-growth regimes, including both winner orientations. It also checks the near-equilibrium stability multipliers below the sharp coupling threshold. Numerical runs corroborate but do not replace the preceding universal proof.

## Relationship to prior work

The symmetric case is a specialization of the two-species Ricker competition model studied by Goldar et al. (2026). That work analyses local equilibria, bifurcations and periodic trajectories but does not provide an all-initial-data extinction-rate theorem for the symmetric high-competition regime. Kulakov, Neverova and Frisman (2022) investigate competitive exclusion and rich periodic dynamics through bifurcation diagrams; those descriptions do not evaluate a uniform extinction exponent across all positive initial conditions. Ackleh and Salceanu (2015) give substantial prior general competitive-exclusion theory, but their sufficient winner criteria demand a competition-coefficient ordering not met by \(\alpha>1\) in the symmetric two-species specialization. The familiar scalar Ricker time-average identity and elementary log-ratio cancellation are used as established tools; the contribution claimed here is their global, all-growth-regime combination with sharp initial-order selection and the exact losing-species exponent.

## Limitations

The result requires equal intrinsic growth factors, exact exchange symmetry, strictly positive initial populations and \(R>0\). It does not cover unequal competition coefficients, stochastic immigration or perturbations, or quantify transient times before the asymptotic extinction regime. The winning population need not approach a fixed point or cycle. Historical priority is provisional: some general exclusion literature may contain a stronger formulation even where the inspected theorem's sufficient coefficient conditions do not apply. Independent validation has not been performed.

## References

- Goldar, S., Hassan, S. S., Pati, R., Mohsen, A. A., and Izadi, M. (2026), *Dynamics and Bifurcations in a Two-Species Ricker Competition Model With Nonmonotonic Growth*, first published 2026-09-16, https://doi.org/10.1155/ddns/7255117.
- Kulakov, M., Neverova, G., and Frisman, E. (2022), *The Ricker Competition Model of Two Species: Dynamic Modes and Phase Multistability*, https://doi.org/10.3390/math10071076.
- Ackleh, A. S. and Salceanu, P. L. (2015), *Competitive exclusion and coexistence in an n-species Ricker model*, https://doi.org/10.1080/17513758.2015.1020576.
