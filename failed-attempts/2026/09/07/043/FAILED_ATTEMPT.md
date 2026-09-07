# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Explicit certified star-discrepancy constant for the cubic Kronecker sequence with frequency ({cbrt(2)}, {cbrt(4)})
- **Round:** 2026-09-07-first-light-01
- **Lane:** 78
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Dynamical Systems
- **Method:** Diophantine approximation and discrepancy theory (Erdos-Turan-Koksma + cubic-norm badly-approximable constant + exact DEM verification)

## Problem

Let alpha1={cbrt(2)}, alpha2={cbrt(4)}, alpha=(alpha1,alpha2) in T^2, and P_N={( {n*alpha1}, {n*alpha2} ): 1<=n<=N}. Let D_N^*(P_N)=sup_{0<x1,x2<=1} |A_N(x1,x2)/N - x1*x2| be the L_inf star discrepancy. Prove an explicit constant C (target C<=12) and N0<=100 such that D_N^*(P_N) <= C*(log N)^2/N for all N>=N0, where C is derived in closed form from (i) an explicit simultaneous-approximation constant of alpha via the cubic norm on Q(cbrt(2)) and (ii) stated Erdos-Turan-Koksma truncation parameters, and confirm the bound at N in {128,256,512,1024,2048} by exact DEM critical-box enumeration plus bracket checks to N=20000.

## Attempted claim

For alpha=({cbrt(2)},{cbrt(4)}), D_N^*(P_N) <= 12*(log N)^2/N for all N>=100, with C=12 derived from a closed-form cubic-norm approximation constant plus stated ETK truncation H(N), and exact DEM values at N in {128,256,512,1024,2048} all lying below the curve (effective fitted constant C_hat <= 8).

## Research outcome

Delivered a CLAIMED partial-theorem package: proved cubic-norm constant c0=0.0260595..., proved explicit ETK bound (82+29 log N)/N^{1/3} (N>=8000), and an exact DEM benchmark table at nine checkpoints to N=20000 all lying below 12(log N)^2/N with effective C_hat=0.344. Honestly separates the unproved uniform (log N)^2/N rate as conjecture.

## Why this attempt failed

Failed axes: correctness, value.

correctness: Theorem 1 (cubic-norm c0=1/(1/2+2S)^2=0.02605957...) is correct and was recomputed to 80 digits; finite check min_{max<=200} d*k^2=0.0759 (2.91x margin) confirmed. Theorem 2 as stated (D<=(82+29 log N)/N^{1/3}) is NOT proved: the derivation drops terms and underestimates the shell sum by ~2x. Recomputing the proof's own majorant S_k*k^2/(2NC0) with C0=0.026 gives 32.91 vs claimed closed form 17.13 at N=8000 (ratio 0.52), 1.839 vs 0.968 at N=3e8, and violations on the full [8000,1e12] grid. A correct completion of the same H=floor(N^{1/3}) route needs roughly (372+58 log N)/N^{1/3} (still N^{-1/3} rate, vacuous far beyond 3e8). The outer ETK 9/4 form and N>=8000 min-branch condition check out; the sum-k-log-k lemma and S_k identity check out. Theorem 3 DEM values reproduce exactly at N=128,256 via independent mask+searchsorted code (0.0315385760, 0.0193580172); critical-box 4-variant logic is sound. Values are exact for the float64 point set, 1e-12-close to the true alpha set (disclosed gap argument), not interval-certified for the true reals. The target D<=12(log N)^2/N (N>=100) is honestly downgraded to Conjecture 4, so not overclaimed, but the only proved uniform bound (Thm 2) has a broken constant derivation and is vacuous (RHS>1) for N<3e8 by the draft's own calculation. value: Judged on what is proved, not the conjectured target. (i) The only proved uniform bound (Thm 2, even if repaired to ~372+58 log N) is an N^{-1/3} rate that is both asymptotically weaker than the long-known optimal (log N)^2/N for badly approximable vectors and numerically vacuous (RHS>1, hence implied by D<=1) for all N<3e8 by the draft's own crossover, so it supplies no usable QMC/Koksma-Hlawka error bar at practical N. (ii) The nine DEM numbers (N=128..20000, fitted Chat=0.344) are correct finite-point computations but, absent the uniform proof, constitute an unexplained enumeration at isolated N: at N<=2048 the C=12 comparison curve itself exceeds 0.34-2.2 (vacuous, >1 at N=128), margins are 35-70x, larger-N spikes are explicitly not ruled out, and the promised fallback two-sided bracket (all dyadic 2^k k=7..14 plus infinitary c_low/N lower bound) is replaced by nine upper points plus the trivial projection sanity N*D>=N/(2(N+1))~0.5. This is a routine effectivization/parameter substitution (canonical cubic vector into standard norm+ETK machinery) plus a small table, not independently worth finding later as a research record.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: The target uniform analytic bound D_N^* <= 12(log N)^2/N is NOT proved: the honest ETK+H=N^{1/3} route yields only an N^{-1/3} rate (Theorem 2), vacuous (RHS>1) below N=3e8; the (log N)^2/N rate is Conjecture 4 supported by finite-N data to N=20000. Exact enumeration covers N<=20000 only (O(N^2)); hidden spikes at larger N not ruled out. Point generation uses float64 certified by a 3000x gap argument, not interval arithmetic. Only the fallback's upper-bracket half is delivered (nine checkpoints…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
