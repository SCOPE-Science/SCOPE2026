# Sharp distance exponent for capture under collective Brownian rightmost resetting

## Finding

Let \(N\ge2\) independent one-dimensional Brownian particles with diffusion coefficient \(D>0\) start at a common position \(x>0\). A shared rate-\(r\) Poisson clock, \(r>0\), resets every particle to the **current spatial maximum** of the group. The first hit of zero by any particle is terminal. Write \(Q_N(x)\) for the probability of eventual capture, and put \(\lambda=\sqrt{r/D}\), \(y=\lambda x\). For each \(0<s<1\), define
\[
\Delta(s)=\frac{s(\sqrt{2-s^2}-s)}{2+s(\sqrt{2-s^2}-s)}>0.
\]
Then for every such \(s\),
\[
 e^{-y}\le Q_N(x)\le \min\!\left\{1,\frac{N}{\Delta(s)}e^{-sy}\right\}.
\]
In particular there is a bound with the sharp exponential rate and at most a linear prefactor:
\[
  e^{-y}\le Q_N(x)\le \min\{1,6eN(y+2)e^{-y}\}.
\]
Consequently, for every fixed \(N,D,r\) in the stated range,
\[
 \lim_{x\to\infty}\frac{1}{x}\log Q_N(x)=-\sqrt{r/D}.
\]
The adjustable bound also gives the simpler fixed-parameter estimate \(Q_N(x)\le (N/\delta)e^{-y/2}\), where \(\delta=\Delta(1/2)=(4/\sqrt7-1)/3\).

## Assumptions and scope

Between alarms the particles have increments \(\sqrt{2D}W_i(t)\), where the \(W_i\) are independent standard Brownian motions, independent of the shared Poisson clock. The process is unconfined and has no drift. An alarm moves the group to its maximum just before the alarm only if capture has not yet occurred. The asymptotic is for a common start tending to infinity at fixed population size, diffusion and reset rate. It is not an estimate of a stationary spatial tail or of a conditional hitting time.

## Proof

**Single-cycle bounds.** Let \(S\) be the first alarm and \(H\) the first zero hit for freely evolving particles from \(x\). For a single particle the Laplace transform of its first hit at parameter \(r\) is \(e^{-\lambda x}\); it is the bounded solution of \(Df''=rf\) with \(f(0)=1\). The shared independent alarm makes this transform the probability that the hit precedes the alarm. Inclusion of this event for any chosen particle, and a union bound over all particles, therefore give
\[
 e^{-y}\le \Pr_x(H\le S)\le Ne^{-y}.
\]

**The two-particle maximum transform.** For free Brownian increments \(B_i(t)=\sqrt{2D}W_i(t)\) in one cycle, let \(M_N=\max_{i\le N}B_i(S)\). Couple with the first two particles, so \(M_N\ge M_2\). Conditional on \(S=t\), write
\[
 M_2=\frac{B_1(t)+B_2(t)}{2}+\frac{|B_1(t)-B_2(t)|}{2}.
\]
The two terms come from independent centered normals of variance \(Dt\), the second taken in absolute value. Completing the square in the half-normal integral gives
\[
 \mathbb E(e^{-\kappa M_2}\mid S=t)= e^{D\kappa^2 t}\operatorname{erfc}(\kappa\sqrt{Dt/2}).
\]
Set \(\kappa=s\lambda\) and integrate over the dimensionless alarm time \(u=rt\). For \(a=1-s^2>0\) and \(b=s/\sqrt2>0\), the integral of \(e^{-au}\operatorname{erfc}(b\sqrt{u})\) over \(u\ge0\) is \((1-b/\sqrt{a+b^2})/a\). This follows by averaging \(\int_0^{(z/b)^2}e^{-au}du\) against \((2/\sqrt\pi)e^{-z^2}dz\) for \(z\ge0\). Rationalizing the resulting expression gives
\[
 \mathbb E e^{-\kappa M_N}\le \mathbb E e^{-\kappa M_2}
 =\frac{1-s/\sqrt{2-s^2}}{1-s^2}
 =\frac{2}{2+s(\sqrt{2-s^2}-s)}=1-\Delta(s).
\]

**Infinite horizon.** At a surviving alarm the common restart is \(x+M_N>0\), and the future has the original transition law from that point. For the trial function \(U_s(x)=(N/\Delta(s))e^{-s\lambda x}\), the probability of capture in the first cycle plus its continuation term is bounded by
\[
\begin{aligned}
 \Pr_x(H\le S)+\mathbb E[\mathbf1_{\{S<H\}}U_s(x+M_N)]
 &\le Ne^{-y}+U_s(x)(1-\Delta(s))\\
 &\le U_s(x).
\end{aligned}
\]
In the first inequality the survival indicator is bounded by one in the nonnegative transform of the **free** maximum. No independence of survival and the maximum is assumed. Iterating the positive continuation operator from zero shows that capture in any finite number of cycles is bounded by \(U_s\); every finite hit is in one of these cycles because the Poisson clock is nonexplosive. The first-cycle lower bound persists for eventual capture. This proves the adjustable bound.

**Sharp logarithmic rate.** Since \(\sqrt{2-s^2}\ge1\) and \(s\sqrt{2-s^2}\le1\) on \((0,1)\), we have \(\Delta(s)\ge s(1-s)/3\). At \(s=1-1/(y+2)\) this is at least \(1/[6(y+2)]\), and \(e^{-sy}\le e^{1-y}\). Substitution gives the two-sided estimate, and taking logarithms and dividing by \(x\) gives the sharp rate. The value at \(s=1/2\) follows by substitution.

## Relationship to other results

The qualitative zero-drift escape assertion is not the quantitative claim here. The related result *A sharp inward-drift threshold for survival under rightmost-particle resetting* gives the same model with a constant inward drift and proves positive survival at zero drift as a special case. Its positive-drift-margin argument supplies a distance bound with some \(\theta>0\), not a specified full admissible range of exponents or the sharp logarithmic rate at zero drift. Here the exact two-particle contraction over \(0<s<1\), combined with the single-cycle lower bound, is what identifies the exponent. This shows quantitatively how the eventual-capture probability at large initial distance compares to the probability of a hit before the very first alarm.

Lee, Yang and Lizana study the same rightmost relocation and first-hit event in a confining harmonic potential. Their right-censored estimates are not results for the present unconfined capture probability. Lee, Yang, Park and Lizana analyze a general group-resetting framework and a stationary center-of-mass avoidance probability, not the eventual probability that any particle has hit zero. Majumdar, Sabhapandit and Schehr study a single discrete walk reset to its historical maximum, rather than the current maximum of a Brownian group.

## Verification and limitations

Run `python3 checker.py` using the Python standard library. The script checks the transformed integral by bounded quadrature and the rationally certified contraction inequalities at sample points. The exact rate and all-parameter bounds follow from the proof, not from finite diagnostics. No exact leading prefactor, distribution conditional on capture, confinement extension, or pure exponential equivalence is claimed.

## References

1. [*A sharp inward-drift threshold for survival under rightmost-particle resetting*](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-a-sharp-inward-drift-threshold-for-survival-under-rightmost-part--6963419da67c), Finding and proof of the exponential capture estimate.
2. J. Lee, S.-G. Yang and L. Lizana, *Beyond average: heterogeneous first-passage dynamics in many-particle systems with resetting*, [arXiv:2604.24406](https://arxiv.org/abs/2604.24406).
3. J. Lee, S.-G. Yang, H. J. Park and L. Lizana, *General Theory for Group Resetting with Application to Avoidance*, [arXiv:2412.02524](https://arxiv.org/abs/2412.02524).
4. S. N. Majumdar, S. Sabhapandit and G. Schehr, *Random walk with random resetting to the maximum*, [arXiv:1509.04516](https://arxiv.org/abs/1509.04516).
