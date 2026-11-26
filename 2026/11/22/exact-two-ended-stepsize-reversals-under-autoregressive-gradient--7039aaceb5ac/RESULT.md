# Exact two-ended stepsize reversals under autoregressive gradient noise

## Finding

Temporal correlation alone can reverse the optimal order of learning rates, even when **the additive oracle errors all have the same marginal variance**. This equality concerns the errors, not the unconditional variances of the stochastic gradients evaluated along the random iterates. For scalar quadratic stochastic gradient descent with a fixed positive finite horizon, the optimal schedule has at most one increase, and its position is determined sharply by the *sign* of the noise correlation.

Fix an integer \(N\ge3\), \(-1<\rho<1\), \(D,\sigma>0\), and let \(t=D^2/\sigma^2\). Define
\[
 S_N=N-(N-2)\rho,\qquad k=\frac{t}{1+\rho+tS_N},\qquad
 (b_0,\ldots,b_{N-1})=(1,1-\rho,\ldots,1-\rho,1).
\]
The unique minimum-expected-final-squared-error schedule among all deterministic \(0\le\eta_j\le1\) is
\[
 \boxed{\eta_j^*=\frac{k b_j}{1-k\sum_{\ell=j+1}^{N-1}b_\ell}\in(0,1),\qquad 0\le j<N.}
\]
Its minimum risk is
\[
 \boxed{\min\mathbb E[(x_N-\theta)^2]=\sigma^2\frac{t(1+\rho)}{1+\rho+tS_N}.}
\]
All strictly interior adjacent comparisons are decreasing: \(\eta_1^*>\eta_2^*>\cdots>\eta_{N-2}^*\). The only possible increases occur at the start or end, never both:

* **Negative correlation, \(-1<\rho<0\):** an initial increase \(\eta_0^*<\eta_1^*\) holds exactly when \(t<-\rho(1+\rho)\); equality gives equal first two steps, and beyond it all steps decrease. The critical signal-to-noise ratio is **independent of horizon**.
* **Positive correlation, \(0<\rho<1\):** a final increase \(\eta_{N-2}^*<\eta_{N-1}^*\) holds exactly when
\[
 \boxed{\rho(1+\rho)>t[1-N\rho+(N-2)\rho^2].}
\]
The initial and all other interior comparisons decrease. Let
\[
 r_N=\frac{N-\sqrt{N^2-4(N-2)}}{2(N-2)}\in(0,1).
\]
For \(\rho\ge r_N\), that final increase is unavoidable for **every** \(t>0\). For \(0<\rho<r_N\), it occurs exactly for
\[
 t<\frac{\rho(1+\rho)}{1-N\rho+(N-2)\rho^2}.
\]
At equality there is a terminal tie, and \(r_N\sim1/N\) as \(N\to\infty\). At \(\rho=0\), every optimal step strictly decreases.

Exact three-step witnesses, with \(\sigma^2=1\), are: \(\rho=-1/2\), \(D^2=1/10\) gives \((\eta_0^*,\eta_1^*,\eta_2^*)=(1/6,1/5,2/17)\) and terminal risk \(1/17\); \(\rho=1/2\), \(D^2=1\) gives \((2/5,1/6,1/4)\) and terminal risk \(3/8\). Both are exact unique global optima over the complete stated step cube.

## Assumptions and scope

Let \(f(x)=(x-\theta)^2/2\) on \(\mathbb R\). The deterministic initial iterate satisfies \(|x_0-\theta|=D>0\). The oracle returns \(g_j=x_j-\theta+\xi_j\), and we apply \(x_{j+1}=x_j-\eta_jg_j\) for \(j=0,\ldots,N-1\), with deterministic rates \(\eta_j\in[0,1]\). The centered gradient-noise vector has finite second moments and stationary AR(1) covariance
\[
 \mathbb E\xi_j=0,\qquad \mathbb E[\xi_i\xi_j]=\sigma^2\rho^{|i-j|},\qquad \sigma>0,\ -1<\rho<1.
\]
No Gaussian assumption or independence across steps is required. The oracle noise need not have zero conditional mean given previous oracle errors; in fact for nonzero \(\rho\) this fails in the Gaussian AR(1) model. The noise vector is exogenous with the prescribed joint moments, and \(x_0\) is deterministic. The objective is **exact expected terminal squared error**; expected terminal objective gap is one-half this quantity. The result is not a minimax theorem over arbitrary smooth convex objectives.

## Proof

**1. Convert a learning-rate schedule to a constrained noise-weight vector.** Set
\[
 w_j=\eta_j\prod_{\ell=j+1}^{N-1}(1-\eta_\ell),\qquad
 R=\prod_{\ell=0}^{N-1}(1-\eta_\ell).
\]
Telescoping gives \(R=1-\sum_j w_j\). As \(0\le\eta_j\le1\), we have \(w_j\ge0\) and \(\sum_jw_j\le1\). Unrolling the iteration gives
\[
 x_N-\theta=R(x_0-\theta)-\sum_jw_j\xi_j.
\]
For \(C_{ij}=\rho^{|i-j|}\), the exact terminal risk is
\[
 \mathcal R(w)=D^2(1-\mathbf1^\top w)^2+\sigma^2 w^\top Cw.
\]
For any \(w\) with positive components and \(\sum_jw_j<1\), the rates \(\eta_j=w_j/[1-\sum_{\ell>j}w_\ell]\) lie in \((0,1)\) and realize these weights exactly. It suffices to find an interior minimizer over the relaxed simplex; uniqueness of its rates then follows.

**2. Compute the strict convex optimum.** For \(|\rho|<1\), the Toeplitz matrix \(C\) is positive definite; its inverse is \((1-\rho^2)^{-1}\) times the tridiagonal matrix with endpoint diagonal entries \(1\), interior diagonals \(1+\rho^2\), and neighboring entries \(-\rho\). Thus
\[
 C^{-1}\mathbf1=\frac1{1+\rho}(1,1-\rho,\ldots,1-\rho,1)^\top,
 \qquad \mathbf1^\top C^{-1}\mathbf1=\frac{S_N}{1+\rho}.
\]
The risk Hessian \(2\sigma^2 C+2D^2\mathbf1\mathbf1^\top\) is strictly positive definite. Its sole stationary point satisfies \(Cw=t(1-\mathbf1^\top w)\mathbf1\), hence
\[
 w^*=\frac{t}{1+\rho+tS_N}(1,1-\rho,\ldots,1-\rho,1)^\top=k b.
\]
Every component is positive; \(\sum w^*=kS_N<1\) because \(1+\rho>0\). Therefore the unconstrained strictly convex minimizer is feasible and has a unique realization by admissible rates. Substitution yields the displayed minimum risk. No finite-sample simulation is used to justify global optimality.

**3. Prove the full order classification.** The explicit reconstruction has positive denominators. For indices \(1\le j<N-2\), consecutive weights are equal and the earlier denominator is strictly smaller, hence \(\eta_j^*>\eta_{j+1}^*\). For the initial comparison, write \(q=1-\rho\), \(P_N=1-N\rho+(N-2)\rho^2=1-\rho S_N\). Direct cross multiplication gives
\[
 \operatorname{sgn}(\eta_0^*-\eta_1^*)=\operatorname{sgn}(\rho+kP_N)
 =\operatorname{sgn}(t+\rho(1+\rho)).
\]
For the final comparison,
\[
 \eta_{N-1}^*=k,\quad \eta_{N-2}^*=\frac{k(1-\rho)}{1-k},\quad
 \operatorname{sgn}(\eta_{N-1}^*-\eta_{N-2}^*)
 =\operatorname{sgn}(\rho-k)
 =\operatorname{sgn}(\rho(1+\rho)-tP_N).
\]
If \(\rho<0\), only the first sign can be negative; if \(\rho>0\), only the last can be positive. For \(\rho=0\), both comparisons decrease. The polynomial \(P_N\) has exactly one root \(r_N\) in \((0,1)\), because \(P_N(0)=1\), \(P_N(1)=-1\), and \(P_N'=-N+2(N-2)\rho<0\) throughout \((0,1)\) for \(N=3,4\) and at its first positive root for all larger \(N\) (equivalently inspect its two explicit roots and the second exceeds one). Solving yields the displayed radical. Its smaller-root equation gives \(Nr_N=1+(N-2)r_N^2\), so \(r_N\sim1/N\). Every boundary and strictness statement follows.

## Verification

Run `python3 verify.py` (Python standard library only) to recompute exact rational covariance moments and rate reconstruction, verify optimality first-order identities and strict risk gaps for sampled coordinate perturbations of the unconstrained weight quadratic (which need not stay in the simplex), check the adjacent-order formulas on the test grid including a start-boundary tie, and confirm both rational witnesses. The verifier prints `VERIFY_OK` with an assertion count. It is a finite diagnostic; the global uniqueness and the infinitely many parameter cases are established by the preceding positive-definite quadratic argument.

## Relationship to prior work

Grimmer and Shen (2026) prove exact worst-case last-iterate SGD guarantees for *conditionally centered* gradient noise and monotone optimal steps in a high-dimensional smooth convex class. The present fixed scalar quadratic with *temporally correlated* oracle errors does not meet that conditional-centering hypothesis, and does not purport to contradict or sharpen their minimax guarantee. A published extension with iteration-dependent conditional variance ceilings also allows step-order reversals, but those arise from **unequal variance bounds**, whereas all one-step marginal variances here are identical and correlation controls the location of the optimal reversal.

Classical generalized least squares already gives the AR(1) inverse-covariance endpoint/interior weight structure; Hermans and collaborators (2018), equation (5), explicitly record the corresponding weights for estimation of a common mean. That structure and linear-quadratic covariance optimization are **not claimed as new**. The contribution assessed here is the complete finite-horizon *sequential gradient-step* optimum including prior initial-error bias and its sharp two-ended, sign-dependent phase diagram, with explicit necessity, uniqueness and examples. Distinct published analyses of AR(1) noise in heavy-ball momentum concern stationary variance at fixed steps rather than finite-horizon optimization of every gradient step. A separate published theorem for descending permutations of fixed steps assumes independence of oracle noise across time; it does not imply the present comparison. These differences do not exclude older equivalent derivations in estimation/control literature.

The [same-date result on three-step order](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-three-exact-noise-correlation-phases-for-the-optimal-order-of-a--3db9e0ceb6be) uses the same scalar quadratic and AR(1) covariance, but optimizes the permutation of a prescribed three-rate multiset rather than the rates themselves. Its correlation boundaries therefore do not give the signal-to-noise thresholds for the full schedule class here. The common date does not establish precedence.

## Limitations

The result concerns a single fixed scalar quadratic, known curvature normalized to one, exogenous stationary AR(1) *second moments*, a fixed finite horizon, and deterministic nonnegative nonovershooting steps. It does not cover data-adaptive steps, unknown noise correlations, vector Hessians, nonlinear objectives, long-run stationary steps, or a minimax worst-case stochastic-gradient class. The absolute noise scale enters only through \(t\). Classical GLS supplies essential ingredients and may make related sequential formulations easier to derive; historical priority is assessed only against the compared sources.

## References

1. B. Grimmer and Q. Shen, *Exact Theory and Optimal Stepsizes for Stochastic Gradient Descent in Smooth Convex Minimization*, arXiv:2610.42048v1, first public 2026-10-30, https://arxiv.org/abs/2610.42048 .
2. L. Hermans, V. Nassiri, G. Molenberghs, M. G. Kenward, W. Van der Elst, M. Aerts and G. Verbeke, *Fast, Closed-form, and Efficient Estimators for Hierarchical Models with AR(1) Covariance and Unequal Cluster Sizes*, Communications in Statistics - Simulation and Computation 47 (2018), 1492–1505, doi:10.1080/03610918.2017.1316395 .
3. *Exact minimax SGD schedules with heterogeneous oracle noise and a sharp step-order reversal criterion*, Resultary, 2026-11-08, record b6e07361803f.
4. *Sign-reversed optimal momentum and the one-ninth antipersistent noise floor*, Resultary, 2026-11-08, record 6f3da69dd7fc.
5. *Descending spectral steps minimize every terminal quadratic noise risk*, Resultary, 2026-10-18, record 2f7a38830384.
