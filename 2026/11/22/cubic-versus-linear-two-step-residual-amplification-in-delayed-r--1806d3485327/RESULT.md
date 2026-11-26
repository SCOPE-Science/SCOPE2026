# Cubic-versus-linear two-step residual amplification in delayed-residual linear solvers

## Finding

Let \(K>1\), \(A=\operatorname{diag}(\sqrt K,1)\), and let \(r_j=b-Ax_j\) for the consistent real system \(Ax=b\) started at \(x_0=0\). Use two updates \(x_{j+1}=x_j+\alpha_j A^{\mathsf T}r_j\). Use the residual Rayleigh step \(\alpha_0=\|r_0\|_2^2/\|A^{\mathsf T}r_0\|_2^2\) first and the residual-difference step of Xu [1] second:
\[
\alpha_1^{\mathrm{RD}}=\frac{\|r_1-r_0\|_2^2}{\|A^{\mathsf T}(r_1-r_0)\|_2^2}.
\]
Let \(M_{\mathrm{RD}}(K)\) be the supremum of \(\|r_2\|_2/\|r_0\|_2\) over starting residuals with both components nonzero. This supremum is attained for every \(K>1\). If \(t=|(r_0)_1|^2/|(r_0)_2|^2\), then
\[
\lim_{K\to\infty}\frac{M_{\mathrm{RD}}(K)}{\sqrt K}=\frac12,
\qquad K^3t\longrightarrow 1\quad\text{for every sequence of maximizing starts}.
\]

**Comparison with the known repeated-Cauchy case.** The delayed-residual (DR) step \(\alpha_1=\alpha_0\) is exactly the two-step Cauchy cycle of [2] on a dual quadratic whose gradient is \(-r\). The exact squared gain in [2] implies a worst-start factor \((3\sqrt3/16+o(1))K^{3/2}\) with maximizing scale \(Kt\to1/3\). Thus the RD startup replaces cubic by linear growth in \(\kappa_2(A)=\sqrt K\), and the most amplifying initial residuals put asymptotically less energy in the high mode. The DR result is a benchmark from [2], not an independent novelty claim here.

## Assumptions and scope

All arithmetic is exact. The spectral condition number of \(A^{\mathsf T}A\) is \(K\), not \(\sqrt K\). The result concerns the Euclidean physical residual after exactly two updates, with the same first step for both rules. It does not bound the objective function after any step, the eventual convergence rate, typical starts, or finite-precision errors.

## Proof of the residual-difference law

Write \(B=AA^{\mathsf T}=\operatorname{diag}(K,1)\). The two residual updates multiply by \(I-\alpha_jB\). The first step has size \((1+t)/(1+Kt)\) and its high- and low-mode multipliers are \(-(K-1)/(1+Kt)\) and \((K-1)t/(1+Kt)\). The identity \(r_1-r_0=-\alpha_0Br_0\) gives \(\alpha_1^{\mathrm{RD}}=(1+K^2t)/(1+K^3t)\), with high- and low-mode multipliers \(-(K-1)/(1+K^3t)\) and \((K-1)K^2t/(1+K^3t)\). Multiplying the two mode factors and averaging with the initial squared weights \(t/(1+t),1/(1+t)\) gives
\[
R_K(t)=\frac{\|r_2\|_2^2}{\|r_0\|_2^2}
 =\frac{(K-1)^4(t+K^4t^4)}{(1+t)(1+Kt)^2(1+K^3t)^2}.
\]
This is continuous and positive on \(t>0\) and tends to zero at both endpoints. A positive maximum is therefore attained at an interior point.

Set \(z=K^3t\). The high-mode contribution to \(R_K(t)/K\) is
\[
\left(1-\frac1K\right)^4\frac{z}{(1+z/K^3)(1+z/K^2)^2(1+z)^2}\le \frac{z}{(1+z)^2}.
\]
The low-mode contribution to \(R_K(t)\) is at most 1: both step sizes lie between \(1/K\) and 1, so both low-mode multipliers have modulus at most 1, and the initial low-mode weight is at most 1. Consequently \(R_K(t)/K\le z/(1+z)^2+1/K\), uniformly for \(z>0\). At \(z=1\), the high-mode term tends to \(1/4\). The function \(z/(1+z)^2\) tends to zero at both endpoints and has its unique maximum \(1/4\) at \(z=1\). The uniform upper bound and the test value at 1 show convergence of the maximum to \(1/4\); for any maximizing choice, the profile must tend to \(1/4\), forcing \(z\to1\). Taking the square root gives the stated constant for the residual norm.

## Derivation of the comparison from the existing benchmark

Put \(x=A^{\mathsf T}u\) in the dual quadratic \(q(u)=\tfrac12u^{\mathsf T}Bu-b^{\mathsf T}u\). Its gradient is \(Bu-b=-r\); the Rayleigh step is the Cauchy line-search step on this quadratic, and repeating it gives precisely DR. The \(m=2\) specialization of the exact squared gain \(F_m(K,t)\) in [2, Proof §2] is
\[
D_K(t)=\frac{(K-1)^4(t+t^4)}{(1+t)(1+Kt)^4}.
\]
For \(y=Kt\), division by \(K^3\) gives \((1-1/K)^4 y(1-y/K+y^2/K^2)/(1+y)^4\). This converges on compact \(y\)-intervals to \(y/(1+y)^4\), and is bounded by \(y/(1+y)^2\) for \(K\ge1\), so no maximum escapes to either tail. The unique limiting maximizer is \(y=1/3\), with value \(27/256\). This gives the comparison constant and the stated maximizing scale by specialization and elementary maximization of the known formula.

## Verification

The proof is analytic. The accompanying Python script `verification/check_two_step.py` supplies finite exact-rational diagnostics of the two squared gains and a finite sample of the rescaled bounds. These diagnostics are not a certificate for the infinite-parameter limits.

## Relationship to prior work

Xu [1, equations (8), (14), (16), (17)] specifies both step rules and the common initialization, supplies the residual recurrence, and reports residual spikes. His window-contraction analysis does not optimize the physical residual after exactly two updates as \(K\to\infty\). The new quantitative point here is the RD maximum and its maximizing initialization scale. Results [3,4] use the same two-mode RD recurrence but concern long-run decay for a fixed matrix, not the worst second residual in an increasingly ill-conditioned family. For the least-squares quadratic in primal variables \(x\), the RD step is BB2. For the dual quadratic in \(u\) above, DR is BB1; these are not the two endpoints of a single primal BB interval with a shared Cauchy start. An objective-ratio bound for a BB interval, or an asymptotic gradient-root factor, is a different observable. The scope comparison does not assert exhaustive historical priority.

## References

1. X. Xu, *Two-point residual step size gradient methods for linear systems*, [arXiv:2611.02743v1](https://arxiv.org/abs/2611.02743).
2. [*A sharp all-spectrum gradient-safety frontier for cyclic steepest descent*](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-a-sharp-all-spectrum-gradient-safety-frontier-for-cyclic-steepes--93b3b7067606/RESULT.md), Finding and Proof §§2, 5 (exact cycle gain).
3. [*Sharp all-start double-log rate for residual-difference spectral steps on two-mode systems*](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-sharp-all-start-double-log-rate-for-residual-difference-spectral--e4d106d38983/RESULT.md), Finding and Proof §§1–2.
4. [*Sharp all-start doubly-exponential decay for residual-difference gradient iteration on two spectral levels*](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-sharp-all-start-doubly-exponential-decay-for-residual-difference--df4e091a200b/RESULT.md), Finding and Proof §§1–3.
