# Sharp rate-cap transition for finite-horizon dispersion in a telegraph swimmer

## Finding

A one-dimensional free run-and-tumble particle, initially at the origin with an equally likely velocity sign, has a unique optimal deterministic finite-time tumbling protocol when the total expected number of reversals and the maximum instantaneous reversal rate are fixed. The optimum is a **single centered constant-rate pulse**, with zero reversal rate before and after. Its pulse height equals the hardware cap only below one sharp threshold; above the threshold it stops increasing, even if the admissible cap is raised further.

Fix speed \(v>0\), horizon \(T>0\), reversal budget \(B>0\), and cap \(R\ge B/T\). Write
\[
g=\min\{R,(1+B)/T\},\qquad L=B/g.
\]
The unique minimizing reversal rate, up to Lebesgue-null sets, is
\[
\gamma_*(t)=g\,\mathbf 1_{((T-L)/2,(T+L)/2)}(t).
\]
With
\[
K(B)=\frac{B^2-1+(B+1)^2e^{-2B}}2>0,
\]
the exact minimum terminal variance is
\[
\boxed{\inf_\gamma\operatorname{Var}(X_T)=v^2T^2\left[\frac1{1+B}+K(B)\left(\max\left\{\frac1{RT}-\frac1{1+B},0\right\}\right)^2\right].}
\]
In particular, \(R_c=(1+B)/T\) is the **sharp saturation threshold**. For \(B/T\le R<R_c\) the rate cap is active on a centered interval; for \(R\ge R_c\) the same uncapped optimal pulse is used. The cap-induced excess variance is exactly quadratic in the positive inverse-cap deficit, not merely an asymptotic upper or lower estimate.

## Assumptions and scope

Let \(S_0\) equal \(+1\) or \(-1\) with probability \(1/2\) each, and let \(N_t\) be an independent inhomogeneous Poisson process with deterministic measurable intensity \(\gamma:[0,T]\to[0,R]\). Assume \(\int_0^T\gamma(t)\,dt=B\). Set \(S_t=S_0(-1)^{N_t}\) and \(X_t=v\int_0^t S_s\,ds\), with \(X_0=0\). Events reverse velocity rather than redraw it. There is no spatial confinement, Brownian thermal noise, event-triggered feedback, or control cost beyond the integral budget and instantaneous cap. The theorem concerns the ensemble variance at the single endpoint \(T\), not long-time diffusivity.

## Proof

**1. Exact two-time covariance.** For \(s\le t\), Poisson parity gives
\[
\mathbb E(S_sS_t)=e^{-2(\Lambda(t)-\Lambda(s))},\qquad \Lambda(t)=\int_0^t\gamma(u)\,du.
\]
The unbiased initial sign makes \(\mathbb E X_T=0\), hence
\[
\frac{\operatorname{Var}(X_T)}{v^2T^2}=\frac1{T^2}\int_0^T\!\int_0^T e^{-2|\Lambda(t)-\Lambda(s)|}\,ds\,dt.
\]
Let \(\mu\) denote the probability pushforward of normalized Lebesgue measure on \([0,T]\) by the nondecreasing map \(\Lambda\). Thus the variance divided by \(v^2T^2\) equals the energy \(\mathcal E(\mu)=\iint_{[0,B]^2}e^{-2|x-y|}\mu(dx)\mu(dy)\).

**2. The rate cap becomes a measure-density floor.** Lipschitz continuity of \(\Lambda\) with constant \(R\), together with \(\Lambda(0)=0\) and \(\Lambda(T)=B\), implies that the preimage of every interval \((x,y)\subset(0,B)\) has length at least \((y-x)/R\). Consequently
\[
\mu\ge c\,dx\quad\text{on }[0,B],\qquad c=\frac1{RT}.
\]
This inequality means domination of measures, so it permits additional point or singular mass. The original control also has a monotone cumulative map; only the necessary density-floor condition is used to prove the lower bound, and the final candidate will be realized explicitly by an admissible control.

**3. Unconstrained equilibrium measure.** Put \(c_0=(1+B)^{-1}\), and define
\[
\mu_0=c_0\,dx+\frac{c_0}{2}(\delta_0+\delta_B).
\]
A direct integral shows that its potential \(U_0(x)=\int e^{-2|x-y|}\mu_0(dy)\) equals the constant \(c_0\) for every \(x\in[0,B]\). Thus for any probability \(\mu\), writing \(\eta=\mu-\mu_0\) yields \(\mathcal E(\mu)=c_0+\mathcal E(\eta)\). Strict positive definiteness of the kernel (its Fourier transform equals \(4/(4+\xi^2)>0\)) gives \(\mathcal E(\eta)>0\) for every nonzero finite signed measure \(\eta\). This is the classical exponential-kernel capacitary-measure calculation [2]; it is used here as **prior theory**, not claimed as new. If \(c\le c_0\), the rate cap permits \(\mu_0\) and the universal lower bound \(c_0\) is attained uniquely.

**4. Active cap.** Suppose \(c>c_0\), and define
\[
\mu_c=c\,dx+h(\delta_0+\delta_B),\qquad h=\frac{1-cB}{2}\ge0.
\]
Its potential is
\[
U_c(x)=c+\frac{1-c(1+B)}{2}\big(e^{-2x}+e^{-2(B-x)}\big).
\]
Because \(1-c(1+B)<0\) and the sum of exponentials attains its maximum only at the two endpoints, \(U_c\) has its minimum exactly at the endpoints. Any feasible \(\mu\) is \(c\,dx+\nu\) with \(\nu\ge0\), \(\nu([0,B])=1-cB\). Hence
\[
\begin{aligned}
\mathcal E(\mu)-\mathcal E(\mu_c)
&=2\int U_c\,d(\mu-\mu_c)+\mathcal E(\mu-\mu_c)\\
&=2\left[\int U_c\,d\nu-(1-cB)U_c(0)\right]+\mathcal E(\mu-\mu_c)\ge0.
\end{aligned}
\]
The first bracket is nonnegative by minimum support, and the second term vanishes only if \(\mu=\mu_c\). Thus \(\mu_c\) is the unique minimizer even over the larger class of *all* probability measures satisfying the density floor.

**5. Realization and sharp value.** Define \(g=\min\{R,(1+B)/T\}\), so \(c_g=1/(gT)\ge c_0\) and \(L=B/g\le T\). The centered pulse in the finding has \(\Lambda=0\) for the first \((T-L)/2\) units of time, rises linearly at rate \(g\) for the next \(L\) units, and equals \(B\) thereafter. Its pushforward is exactly
\[
\mu_{c_g}=c_g\,dx+\frac{1-c_gB}{2}(\delta_0+\delta_B),
\]
which is the appropriate unique energy minimizer in both cap regimes. Since Lebesgue measure has full support and \(\Lambda\) is continuous nondecreasing, the pushforward uniquely determines \(\Lambda\) almost everywhere (equivalently, its quantiles), and hence the optimizing rate \(\gamma\) almost everywhere.

Expanding the energy around \(\mu_0\), whose potential is constant, gives
\[
\mathcal E(\mu_{c_g})=\frac1{1+B}+(c_g-c_0)^2\,\mathcal E\!\left(dx-\frac B2(\delta_0+\delta_B)\right).
\]
Direct integration yields the last energy as \(K(B)\). Strict positivity follows also from strict positive definiteness, since the signed measure is nonzero for \(B>0\). Substituting \(c_g-c_0=\max\{1/(RT)-1/(1+B),0\}\) gives the claimed exact formula and the unique optimizer.

## Verification

The standalone `check.py` independently propagates the closed telegraph moment equations \(m'(t)=v-2\gamma(t)m(t)\) and \(V'(t)=2v m(t)\) from zero initial moments through every constant-rate interval by matrix exponentiation. It compares the resulting terminal variance against the closed formula over a grid of reversal budgets, horizons, rate caps, and speeds, and checks further randomly generated admissible piecewise-constant protocols. The program reports 90 independent pulse-propagation comparisons and 250 randomized feasible controls. These finite checks support reproducibility; the universal and uniqueness statements follow from the measure-theoretic argument above, not from numerical enumeration.

## Relationship to prior work

Baldovin and Manacorda [1], first publicly submitted on 4 February 2026, study active-particle control through a time-dependent tumbling rate and trapping strength, primarily for prescribed endpoint stationary states and minimum mechanical work. The present result asks the different *finite-time, free-trajectory, fixed expected reversals, capped instantaneous rate, and terminal dispersion* question. The exponential-kernel equilibrium measure and endpoint atoms are already known from Alfonsi and Schied [2], including the unconstrained capacitary law, and are expressly credited. The added mathematical statement is the **exact density-floor-constrained minimizer, strict cap-regime boundary, and quadratic cap penalty**, obtained by mapping the telegraph control constraints to a measure obstacle and proving a new constrained variational inequality. A published periodic-reversal-budget result [3] minimizes *long-time diffusivity* with a homogeneous rate; its periodic objective and unbounded pointwise rates differ from this endpoint problem and do not imply the centered finite-time pulse. Prior art in constrained exponential-kernel energy and optimal execution may offer additional equivalences not located in the examined sources.

## Limitations

The noise is symmetric binary telegraph propulsion, with deterministic open-loop reversal intensity and no mechanical restoring force. The result does not optimize first-passage observables, thermodynamic work, long-time diffusivity, or paths with time-dependent speed, and does not apply directly to non-Poisson turning or a nonconstant harmonic response weight. The result depends on the fixed *expected* reversal count rather than a fixed realized count. The older unconstrained equilibrium measure is not original; publication priority for the specific lower-density obstacle and physical rate-cap theorem should receive independent review.

## References

[1] M. Baldovin and A. Manacorda, “Control protocols for harmonically confined run-and-tumble particles,” arXiv:2602.04560, first submitted 4 February 2026. https://arxiv.org/abs/2602.04560

[2] A. Alfonsi and A. Schied, “Capacitary measures for completely monotone kernels via singular control,” arXiv:1201.2756, first submitted 13 January 2012. https://arxiv.org/abs/1201.2756

[3] “Sharp periodic reversal-budget bounds for active-particle diffusivity,” 2026, publicly indexed finding and complete proof: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-periodic-reversal-budget-bounds-for-active-particle-diffus--6ae3dffd67fb
