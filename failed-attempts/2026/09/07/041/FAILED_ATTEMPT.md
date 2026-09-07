# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Explicit sparsity-aware smallest-singular-value tail for 160x80 sparse Rademacher matrices at p=0.2 beating textbook net constants
- **Round:** 2026-09-07-first-light-01
- **Lane:** 77
- **Disposition:** NO_RESULT
- **Domain:** Probability
- **Method:** non-asymptotic concentration and net arguments

## Problem

Let N=160, n=80, p=0.2. Let B_ij i.i.d. Bernoulli(p) and R_ij i.i.d. Rademacher (+/-1), independent, and define Y_ij = B_ij*R_ij/sqrt(p), so E[Y_ij]=0, Var=1, sparsity 80%. Let s_min(Y)=sigma_n(Y). Prove a fully closed-form, numerically evaluable tail bound P(s_min(Y) <= 2.0) <= 0.01 via a sparsity-aware epsilon-net argument (compressible/incompressible split with support-restricted covering counts + exact binomial small-ball tensorization + explicit operator-norm/degree conditioning), and validate it by an independent Monte Carlo SVD experiment with fixed protocol (arXiv-recorded seed, >=2000 trials, Clopper-Pearson interval). All constants must be numbers, not O()/C/c; the RHS must evaluate in <1s in plain Python/numpy.

## Attempted claim

For Y as above with (N,n,p)=(160,80,0.2): P(s_min(Y) <= 2.0) <= 0.01 proved by an explicit inequality of the form P <= P_zero-row/col + P_opnorm(K0) + |N_comp(eps0,delta,s)| * q_sb(t)^{N-k} + C_inc*(C_sb*t)^{N-n+1} + exp(-cN) where every term is instantiated numerically (e.g. eps0, delta-compressibility, support size s, net cardinalities via exact sum_{k<=s} C(n,k)*(3/eps0)^k, one-dimensional small-ball L(t) from exact Bernoulli-Rademacher Paley-Zygmund/Esseen bound, matrix-Bernstein operator-norm tail with K0 ~= 26-30), RHS evaluates to <=0.01, strictly beating the naive dense RV instantiation which is >=1 at eps=2.0/(sqrt(N)-sqrt(n-1))~=0.53 for any published generic C>=2. Companion simulation: >=2000 i.i.d. trials show empirical frequency of {s_min<=2.0} equal to 0 (95% Clopper-Pearson upper <=0.002) and median/mean ~=3.8-3.9, consistent with the bound.

## Research outcome

Target (N,n,p)=(160,80,0.2) sparse-Rademacher s_min tail P(<=2.0)<=0.01 was NOT proved. Empirical evidence strongly suggests the bound is true: 2000 fixed-seed (20260907) SVD trials give mean s_min 3.870 (sd 0.207), q05 3.515, median 3.876, min 3.207, max 4.519, with 0 trials <=2.0 or <=1.5 (95% Clopper-Pearson upper 0.00150). Closed-form ledger computed: gap sqrt(160)-sqrt(79)=3.7609 so eps=0.5318 (t=2) / 0.3989 (t=1.5); zero-column term n(1-p)^N=2.5e-14 and degree term N(1-p)^n=2.8e-06; matrix-Bernstein P(||Y||>=u)<=240*exp(-u^2/(320+1.49u)) non-vacuous only at u>=55 (0.129 at 55, 0.036 at 60, 0.0023 at 70); compressible nets C(80,s)(1+2/rho)^s tabulated (e.g. s=4,rho=0.1 gives 3.1e11); pointwise Paley-Zygmund single-vector values 0.0726 (t=2) and 0.0516 (t=1.5) are far too weak for union bounds. The uniform compressible/incompressible union bound with all-explicit constants remains vacuous, so neither the headline nor the fallback analytic claim is established. Partial evidence (Monte Carlo table, vacuity ledger) is preserved in output/artifacts and WORKLOG.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No completed closed-form uniform bound P(s_min(Y)<=2.0)<=0.01 or fallback P(<=1.5)<=0.05: (1) matrix-Bernstein gives non-vacuous operator-norm control only at K0>=60 (P(||Y||>=60)<=0.036, P(>=70)<=0.0023), so any rho-net approximation penalty rho*K0 forces tiny rho and huge nets; (2) uniform single-vector MGF small-ball sup over the sphere was not reduced to explicit numbers (worst case y=e1 gives P(||Ye1||<=3.2)=P(Bin(160,0.2)<=2)=2.6e-13, but the full-sphere net (1+2/rho)^80 overwhelms it); (3) the incompressible distance/LCD branch was not instantiated with explicit constants, so the final union-bound RHS is vacuous (>1) and Step 1 of the audit plan is not met. Textbook baseline check is also qualified: (C*eps)^81 with eps=0.5318 is vacuous (147) for C=2 but equals 1.1e-8 for C=1.5, so 'vacuous for any published C>=1.5' as worded is false; the correct statement is that no published numeric (C,c) covers this sparse ensemble, i.e. constants are unspecified. All simulations used numpy.linalg.svd without interval certification; empirical quantiles are estimates with sampling error only.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No completed closed-form uniform bound P(s_min(Y)<=2.0)<=0.01 or fallback P(<=1.5)<=0.05: (1) matrix-Bernstein gives non-vacuous operator-norm control only at K0>=60 (P(||Y||>=60)<=0.036, P(>=70)<=0.0023), so any rho-net approximation penalty rho*K0 forces tiny rho and huge nets; (2) uniform single-vector MGF small-ball sup over the sphere was not reduced to explicit numbers (worst case y=e1 gives P(||Ye1||<=3.2)=P(Bin(160,0.2)<=2)=2.6e-13, but the full-sphere net (1+2/rho)^80 overwhelms it); (…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
