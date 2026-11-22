# Critical half-grid staircase for a stochastically rounded flip contraction

## Finding
Let \(\mathcal R(y;U)=\lfloor y+U\rfloor\), with fresh independent uniform \(U\in[0,1]\) at every iteration. Fix any real detuning \(c\). For sufficiently small \(\varepsilon>0\), put \(r_\varepsilon=1-\varepsilon\) and \(\theta_\varepsilon=\tfrac12+c\varepsilon\) and consider the integer-valued random recurrence
\[
 X_{j+1}=\mathcal R\bigl(\theta_\varepsilon-r_\varepsilon(X_j-\theta_\varepsilon);U_{j+1}\bigr),\qquad X_j\in\mathbb Z.
\]
It has a unique invariant probability \(\pi_{\varepsilon,c}\). Set
\[
 K_c=\left\lceil2|c|+\tfrac12\right\rceil,\qquad I_c=\{1-K_c,2-K_c,\ldots,K_c\},
\]
and define positive-part rates on the integers by
\[
 u_c(n)=(\tfrac12-n-2c)_++(\tfrac12-n+2c)_+,\qquad
 d_c(n)=(n-\tfrac12+2c)_++(n-\tfrac12-2c)_+.
\]
Then the invariant laws **converge in total variation** as \(\varepsilon\downarrow0\) to a probability \(\pi_c\) supported **exactly** on \(I_c\). Its weights are explicit: take \(w_{1-K_c}=1\), define successively
\[
 w_n=w_{n-1}\frac{u_c(n-1)}{d_c(n)}\quad(2-K_c\le n\le K_c),
 \qquad \pi_c(n)=\frac{w_n}{\sum_{j=1-K_c}^{K_c}w_j},
\]
and set \(\pi_c(n)=0\) outside \(I_c\).

The law obeys the reflection symmetry \(\pi_c(n)=\pi_c(1-n)\) and depends only on \(|c|\). Its support has size \(2K_c\), increasing precisely when \(|c|\) crosses the levels \(1/4,3/4,5/4,\ldots\). At the level itself the newly born extreme states have zero limiting mass; strictly beyond it their masses are positive. On \(|c|\le1/4\), \(\pi_c=(\delta_0+\delta_1)/2\); at \(c=1/2\),
\[
 \pi_{1/2}=\tfrac1{14}\delta_{-1}+\tfrac37\delta_0+\tfrac37\delta_1+\tfrac1{14}\delta_2,
 \quad\operatorname{Var}_{\pi_{1/2}}X=\tfrac{15}{28}.
\]
For \(|c|\le1/4\) and all sufficiently small \(\varepsilon\), the **exact**, not only limiting, invariant law is \((1-\theta_\varepsilon)\delta_0+\theta_\varepsilon\delta_1\).

## Assumptions and scope
The lattice is the unbounded integer grid. Arithmetic evaluating the affine expression is exact, followed by **one** unbiased rounding with a new independent uniform. The detuning \(c\) is fixed while \(\varepsilon\to0^+\). In particular \(\theta_\varepsilon\in(0,1)\) for sufficiently small \(\varepsilon\). The claim concerns the stationary distribution, not a simultaneous long-time and small-parameter trajectory limit. A discrete-time probability kernel is always used; the continuous-time birth-death generator below is its first-order **two-step** limit, not a claim that the original one-step chain converges to a continuous-time process without grouping.

## Proof
**1. Unique invariant probability and a fixed finite core.** The shared-uniform rounding coupling is monotone in its real input and satisfies
\[
 \mathbb E_U|\mathcal R(a;U)-\mathcal R(b;U)|=|a-b|.
\]
The one-step kernel therefore contracts Wasserstein distance \(W_1\) by \(r_\varepsilon<1\) on probabilities on \(\mathbb Z\) with finite first moment. Completeness gives a unique fixed point there. It is also the unique invariant probability without a moment assumption: from any integer start, transition laws converge to that fixed point, and bounded convergence over an arbitrary invariant initial law proves equality.

Choose any integer \(M>2|c|+3\). For all sufficiently small \(\varepsilon\), the finite lattice interval \(J=\{-M,\ldots,M+1\}\) is invariant under the rounded update: the unrounded affine function is decreasing, maps the endpoint \(-M\) strictly below \(M+1\), maps \(M+1\) strictly above \(-M\), and its entire image is contained in \((-M,M+1)\). Its two neighboring rounded integers therefore lie in \(J\). Consequently the invariant probability is carried by this same finite set for **every sufficiently small** \(\varepsilon\). This fixed core is the key tightness input and does not presume the desired limit.

**2. Exact first-order two-step transition law.** Write \(R(n)=1-n\) and \(t_c(n)=n-\tfrac12+2c\). For each fixed integer \(n\), the unrounded next value has the exact expansion
\[
 \theta_\varepsilon-r_\varepsilon(n-\theta_\varepsilon)
 =R(n)+\varepsilon t_c(n)-c\varepsilon^2.
\]
In \(J\), uniformly in \(n\), one step goes from \(n\) to \(R(n)\) with probability \(1-\varepsilon|t_c(n)|+O(\varepsilon^2)\), to \(R(n)+1\) with probability \(\varepsilon(t_c(n))_++O(\varepsilon^2)\), and to \(R(n)-1\) with probability \(\varepsilon(-t_c(n))_++O(\varepsilon^2)\). These statements remain valid when \(t_c(n)=0\): the exceptional jump then has probability \(O(\varepsilon^2)\). Applying the same expansion at \(R(n)\) in the second step, and observing that \(R(R(n)+1)=n-1\), \(R(R(n)-1)=n+1\), yields
\[
 P_{\varepsilon,c}^{\,2}=I+\varepsilon Q_c+O_J(\varepsilon^2),\qquad
 (Q_cf)(n)=u_c(n)[f(n+1)-f(n)]+d_c(n)[f(n-1)-f(n)].
\]
The matrix error is entrywise and uniform over finite \(J\). Its rows stay within \(J\) at the endpoints.

**3. Complete communicating-class analysis.** The upward rate \(u_c(n)\) is strictly positive exactly for \(n<\tfrac12+2|c|\), and the downward rate \(d_c(n)\) is strictly positive exactly for \(n>\tfrac12-2|c|\). The unique closed communicating class is therefore the consecutive integer interval \(I_c\): within it adjacent states communicate in both directions, the lower endpoint has no downward rate and the upper endpoint no upward rate; outside it all jumps are directed inward until the class is reached. This remains true when either endpoint rate vanishes at a half-integer threshold. Thus the finite generator \(Q_c\) on \(J\) has exactly one invariant probability, supported and strictly positive on \(I_c\). Birth-death detailed balance gives the displayed product weights, since all denominators \(d_c(n)\) used in the product are strictly positive.

**4. Identification and total-variation convergence.** Any sequence \(\varepsilon_k\downarrow0\) has a subsequence whose invariant probabilities on fixed \(J\) converge. The stationarity equation \(\pi_{\varepsilon_k,c}P_{\varepsilon_k,c}^{\,2}=\pi_{\varepsilon_k,c}\), divided by \(\varepsilon_k\), implies \(\pi Q_c=0\). Uniqueness in Step 3 makes every subsequential limit equal to \(\pi_c\). On the fixed finite set \(J\), coordinatewise convergence is equivalent to total-variation convergence.

**5. Symmetry and sharp phase boundaries.** Since \(u_c(n)=d_c(1-n)\), the reflected probability is also invariant for \(Q_c\); uniqueness gives \(\pi_c(n)=\pi_c(1-n)\). Both rate formulas are even in \(c\), proving detuning-sign symmetry. The ceiling formula gives \(K_c=k\) when \(k-\tfrac32<2|c|\le k-\tfrac12\), and jumps to \(k+1\) only when \(2|c|>k-\tfrac12\). This proves the exact thresholds and endpoint convention. At \(c=1/2\) the rate ratios generate weights \(1:6:6:1\), yielding the stated law and variance. Finally, if \(|c|\le1/4\), for all small \(\varepsilon\) both unrounded images of states \(0,1\) lie strictly between \(0\) and \(1\); thus \(\{0,1\}\) is closed. Its stationary mean equals \(\theta_\varepsilon\) by the conditional-mean equation, forcing Bernoulli weights \(1-\theta_\varepsilon,\theta_\varepsilon\) by uniqueness.

## Verification
Run `python3 check.py` with standard Python 3. The checker constructs exact rational transition kernels and finite stationary vectors for ten detunings at three positive values of \(\varepsilon\). It verifies exact normalization, conditional-mean stationarity, reflection, detailed-balance identities for the limiting rates, the exact Bernoulli zone, the four-site weights at \(c=1/2\), and finite-parameter total-variation comparisons. The output was `PASS`. These finite checks support arithmetic and special cases; the limit for all fixed real \(c\) is established by the fixed-core and generator argument above, not by finite experiments.

## Relationship to prior work
Weiß and Zhu (2024 preprint, Sections 2–3 and Appendix A) define mean-preserving rounding, give its transition probabilities and establish general stationary and moment results for integer-valued ARMA-type recurrences. Those general facts are not claimed as new. Related work on the same idealized overshooting rounded affine contraction proves fixed-phase stationary Gaussian asymptotics when \(2\theta\notin\mathbb Z\) and an exact fair Bernoulli law when \(\theta=1/2\); it keeps \(\theta\) fixed as the contraction approaches one. In contrast, the present statement takes the singular *simultaneous* detuning \(\theta_\varepsilon=1/2+c\varepsilon\), derives the two-step birth-death limit, and identifies a discrete family of stationary laws and every support-onset boundary. Neither fixed-phase limit determines this double-scaling law. Mean-preserving integer-time-series identities alone do not state the parameter-dependent communicating-class classification. A published equivalent critical-window law could supersede the novelty assessment; comparison has been made against the accessible sources specified below.

## Limitations
The theorem concerns a stochastic difference equation on an exact integer grid, not standard floating-point hardware. The parameter \(c\) must remain fixed in the limit; no bound uniform over unbounded \(c\), no rate of total-variation convergence, and no corresponding double-scaling mixing-time theorem are asserted. The model has deliberately no added innovations beyond rounding. The exact stationary weights of the limiting birth-death chain are not a general formula for the finite-\(\varepsilon\) chain. Priority beyond inspected source material is not independently established.

## References
1. C. H. Weiß and F. Zhu, *Mean-preserving rounding integer-valued ARMA models*, arXiv:2402.15772, first submitted 2024-02-24, https://arxiv.org/abs/2402.15772. Inspect Sections 2–3 and Appendix A for kernel, stationarity and the alternative model.
2. L. Xia, S. Massei, M. E. Hochstenbach, B. Koren, *On the influence of stochastic roundoff errors and their bias on the convergence of the gradient descent method with low-precision floating-point computation*, arXiv:2202.12276, first submitted 2022-02-24, https://arxiv.org/abs/2202.12276 (background on optimization motivations, not the originating stationary-law claim).
3. *Lattice-phase Gaussian law at the flip boundary of stochastic-rounding descent*, public mathematical finding, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-lattice-phase-gaussian-law-at-the-flip-boundary-of-stochastic-ro--4edb1a74d619 (fixed-phase and exact resonant endpoint).
4. *A sign-reversal Gaussian limit for unbiased lattice rounding*, public mathematical finding, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sign-reversal-gaussian-limit-for-unbiased-lattice-rounding--3bd484d77163 (fixed-phase limit for the same map).
