# Strict finite-budget underdispersion of pooled absorbing-outcome counts

## Finding

Consider independently renewed trajectories whose binary absorbing outcomes are associated with different exponential lifetimes. For each positive finite deadline, the asymptotic (many-worker) variance of the pooled observed outcome fraction is **strictly smaller** than the variance predicted by independent Bernoulli samples of the same observed mean with the same expected completed count, unless the two lifetimes have identical rates. The difference has an explicit, sign-definite formula.

Let \(0<b<1\), \(\lambda_0,\lambda_1>0\), and \(t>0\). Introduce
\[
 c=b\lambda_0+(1-b)\lambda_1,\quad
 L=\lambda_0\lambda_1/c,\quad
 h=b(1-b)(\lambda_1-\lambda_0),\quad
 z=ct,\quad u=1-e^{-z}.
\]
Set
\[
 m(t)=Lt+\frac{b(1-b)(\lambda_1-\lambda_0)^2}{c^2}u,
 \qquad q(t)=b+\frac{hu}{c\,m(t)}.
\]
For \(M\) independent workers each renewed immediately after each absorption, the pooled fraction \(\widehat q_M(t)\) satisfies
\[
 \sqrt M\bigl(\widehat q_M(t)-q(t)\bigr)
 \ \Longrightarrow\ \mathcal N(0,V(t)),
\]
with exact coefficient
\[
 \boxed{V(t)=\frac{q(t)(1-q(t))}{m(t)}
 -\frac{2h^2L^2}{c^4m(t)^4}H(ct)},
 \qquad H(z)=ze^{-z}\{z\sinh z+z^2-4(\cosh z-1)\}.
\]
For every \(z>0\), \(H(z)>0\). Thus, if \(\lambda_1\ne\lambda_0\), then
\[
 0<V(t)<\frac{q(t)(1-q(t))}{m(t)}\quad (t>0),
\]
and for \(\lambda_1=\lambda_0\) equality holds. The corresponding one-worker residual variance has the nonzero exact long-time gap
\[
 \lim_{t\to\infty}\Bigl[\operatorname{Var}\{R(t)-q(t)K(t)\}
       -q(t)(1-q(t))m(t)\Bigr]
 =-\left(\frac{h}{c}\right)^2.
\]
The comparison uses the mean-matched parameter \(q(t)\), **not** the underlying unbiased target \(b\); it does not claim that binomial intervals centered at the biased estimate cover \(b\).

## Assumptions and scope

For every renewal \(i\), sample a binary outcome \(X_i\) independently with \(\Pr(X_i=1)=b\). Conditional on \(X_i=x\), draw a duration \(T_i\) having rate \(\lambda_x\) exponential distribution. The pairs \((X_i,T_i)\) are iid, with immediate restart and no overhead. Define
\[
 K(t)=\max\Bigl\{k\ge0:\sum_{i=1}^kT_i\le t\Bigr\},
 \quad R(t)=\sum_{i=1}^{K(t)}X_i.
\]
Let \((R_j,K_j)\), \(1\le j\le M\), be independent copies, and \(\widehat q_M=(\sum_jR_j)/(\sum_jK_j)\) when the denominator is positive. Its arbitrary value on zero completions does not affect the stated large-\(M\) result. For fixed \(t>0\) all moments are finite by domination of the renewal count by a Poisson process at rate \(\max(\lambda_0,\lambda_1)\). The population of workers \(M\to\infty\) with \(t\) held fixed; no simultaneous large-time central limit is asserted.

## Proof

**1. Exact mean and large-worker limit.** Define the duration transforms, for \(s>0\),
\[
 f(s)=\frac{b\lambda_1}{s+\lambda_1}
       +\frac{(1-b)\lambda_0}{s+\lambda_0},\qquad
 f_1(s)=\frac{b\lambda_1}{s+\lambda_1}.
\]
The renewal transforms are
\[
 \mathcal L\{\mathbb EK\}(s)=\frac{f(s)}{s(1-f(s))},\qquad
 \mathcal L\{\mathbb ER\}(s)=\frac{f_1(s)}{s(1-f(s))}.
\]
Because \(1-f(s)=s(s+c)/[(s+\lambda_1)(s+\lambda_0)]\), partial fractions give the displayed \(m(t)\) and \(\mathbb ER(t)=b\,m(t)+(h/c)(1-e^{-ct})\). Thus \(q(t)=\mathbb ER/m\), and the iid bivariate central limit theorem followed by the delta method gives \(V(t)=\operatorname{Var}(R-qK)/m^2\).

**2. An exact second-moment renewal identity.** Mark the number of completed renewals with \(u_0\) and the sum of their outcomes with \(v_0\). The full joint generating transform is
\[
 \int_0^\infty e^{-st}\,\mathbb E[u_0^{K(t)}v_0^{R(t)}]dt
 =\frac{1-f(s)}{s\{1-u_0[f(s)-f_1(s)+v_0f_1(s)]\}}.
\]
For the centered per-renewal mark \(X_i-q\), replace the inner expression by
\(e^{-q\theta}\{f(s)-f_1(s)+e^{\theta}f_1(s)\}\) and differentiate twice at \(\theta=0\). For \(q=q(t)\), the exact uncentered second moment is its variance since \(\mathbb E[R-qK]=0\), and inversion yields
\[
 \operatorname{Var}(R-qK)
 =q(1-q)m+2\mathcal L^{-1}\left\{
 \frac{[f_1(s)-qf(s)]^2}{s[1-f(s)]^2}\right\}(t).
\]
In this inverse transform \(q=q(t)\) is a fixed real number for the chosen horizon and must **not** be varied during inversion.

**3. Evaluate the correction.** Direct algebra gives
\[
 \frac{f_1(s)-qf(s)}{1-f(s)}
 =\frac{As+B}{s(s+c)},\quad
 A=b\lambda_1-q[b\lambda_1+(1-b)\lambda_0],
 \quad B=(b-q)\lambda_1\lambda_0.
\]
Writing \(u=1-e^{-z}\), one finds \(A=hL(z-u)/(cm)\), \(B=-hLu/m\). The inverse transform is therefore the elementary convolution of \((As+B)^2/s^2\) with \(1/[s(s+c)^2]\). With
\[
 F_0=1-(1+z)e^{-z},\quad
 F_1=z-2+(z+2)e^{-z},\quad
 F_2=z^2/2-2z+3-(z+3)e^{-z},
\]
its value is
\[
 \frac{h^2L^2}{c^4m^2}
 \bigl[(z-u)^2F_0-2u(z-u)F_1+u^2F_2\bigr]
 =-\frac{h^2L^2}{c^4m^2}H(z).
\]
Substitute into step 2 and divide by \(m^2\), proving the stated exact variance.

**4. Strictness and limits.** The hyperbolic-function bracket has a manifestly positive series
\[
 z\sinh z+z^2-4(\cosh z-1)
 =\sum_{n=3}^\infty\frac{2n-4}{(2n)!}z^{2n}>0
 \qquad(z>0).
\]
The variance is strictly positive because \(R-qK\) has nonzero probability of different values at every positive time and \(0<q<1\). As \(z\to\infty\), \(H(z)=z^2/2-2z+o(z)\) and \(m(t)\sim Lz/c\), giving the claimed limiting correction. This completes the proof.

## Verification

The included standalone `check_variance.py` evaluates the closed form at 10 heterogeneous rate/weight/budget sets and reconstructs the same centered second moment independently through a tilted two-state Markov-additive generator. Additional tests check homogeneous-rate equality, the long-time constant, and positivity coefficients. Execute `python check_variance.py` with `mpmath` installed. It reports `PASS 61 analytical/independent-generator tests`. For \(b=1/2\), \(\lambda_1=6\), \(\lambda_0=1.2\), \(t=2\), the mean completed count is approximately \(4.44411263\), the observed limiting fraction is approximately \(0.57494960\), and the true variance coefficient is about \(0.96220453\) times the naive mean-matched binomial coefficient. These numerical checks supplement, not replace, the all-parameter proof.

## Relationship to prior work

Reia and Fontanari establish the binary exponentially marked renewal model and its exact first moments, finite-deadline selection bias and alternative filtered protocol. Their discussion explicitly warns that fluctuations of the pooled outcome fraction are not generally described by the Bernoulli variance but does not give the all-budget strict sign comparison or its exact coefficient. A separate earlier analysis of the same two-outcome exponential renewal model obtained endpoint sign reversals for the covariance between the **two completed-outcome counts**, using the same marked-renewal generating function. That count-covariance theorem and its underlying transform are not new here; its endpoint signs do not determine the strict finite-time binomial-gap sign for the pooled outcome fraction. Patch, Nazarathy and Taimre establish general asymptotic covariance corrections for multivariate renewal-reward processes; general renewal-transform and large-time moment technology therefore predates this finding. The present claim is the sign-definite, exact **finite-time** comparison in the specified exponential binary model, not a claim to invent renewal-reward covariance methods or the already known bias formula. A prior abstract on stopped renewal sampling (Kremers and Robson, 1987) was considered, but the full treatment was unavailable; priority cannot be guaranteed from the inspected materials.

## Limitations

The strict comparison requires a binary outcome with conditional **exponential** durations and immediate iid regeneration. It compares fluctuations around the finite-budget large-worker mean \(q(t)\), which is generally biased relative to \(b\); reduced variance need not mean smaller mean-squared error or correct confidence-interval coverage for \(b\). The asymptotic distribution is for many workers at fixed positive deadline, not a full finite-\(M\) variance formula. General duration laws may have different signs. Explicit novelty is subject to independent literature-priority verification, especially older renewal-sampling work.

## References

- S. M. Reia and J. F. Fontanari, *Renewal Bias in Parallel Simulations of Absorbing Processes*, arXiv:2611.12692v1 (first publicly submitted 2026-11-09), https://arxiv.org/html/2611.12692v1 .
- B. Patch, Y. Nazarathy and T. Taimre, *A Correction Term for the Covariance of Renewal-Reward Processes with Multivariate Rewards*, arXiv:1408.1530 (2014), https://arxiv.org/html/1408.1530v1 .
- W. Kremers and D. Robson, *Unbiased estimation when sampling from renewal processes: The single sample and k-sample random means cases*, Biometrika 74 (1987), 329–337, https://doi.org/10.1093/biomet/74.2.329 .
