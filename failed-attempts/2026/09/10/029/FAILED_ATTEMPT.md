# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Quantitative Tracy-Widom edge rate for Pareto-4.5 real Wigner matrices at the fourth-moment threshold
- **Round:** 2026-09-07-first-light-01
- **Lane:** 562
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Random Matrix Theory
- **Method:** Dyson Brownian motion local relaxation with Stieltjes-transform local-law comparison and moment-matching replacement

## Problem

Localize the fourth-moment threshold for Tracy-Widom edge universality in real Wigner matrices at finite (4+eps) moment: prove an explicit quantitative edge-comparison rate for a named Pareto-4.5 entry law via one-step Dyson Brownian motion relaxation plus Stieltjes local-law comparison, or isolate the heavy-tail obstruction.

## Attempted claim

For N x N real Wigner H with H_ij=N^{-1/2} x_ij where x_ij are i.i.d. standardized symmetric Pareto exponent 4.5 (mean 0, variance 1, finite (4+eps) moment with eps=1/2), let lambda_N be the largest eigenvalue and F1 the GOE Tracy-Widom distribution. Then sup_s |P(N^{2/3}(lambda_N-2) <= s) - F1(s)| <= C N^{-1/18} for all N >= N0 with absolute C, N0.

## Research outcome

Proved a critical-truncation sparse-large-entry control trilogy for the standardized symmetric Pareto-4.5 Wigner edge problem: at T*=N^{34/81} (unique minimal exponent where the bad-row interlacing count binds), bad count, bad quadratic mass, and bad first-order mass all sit below the N^{-5/9} window with probability >=1-N^{-1} at explicit N0 (2, 22, 4), with third moments necessary and sufficient. Full TW rate and literal fallback rigidity explicitly not claimed (good-matrix local law remains open).

## Why this attempt failed

Failed axes: correctness, value.

correctness: Headline is a pure-probability trilogy about M=N^2 i.i.d. standardized symmetric Pareto-4.5 variables at T*=N^{34/81}, w=N^{-5/9}. Checked each leg independently. (T1) PASS: B~Binomial(M,p), p=c0*T^{-4.5}, mu=c0*N^{1/9}, threshold 3N^{1/9} gives 1+d=3/c0=11.2586, K1=c0*((1+d)ln(1+d)-d)=4.52986; g(y)=K1*y-9ln y has minimum 2.82>0 at y=9/K1=1.987, re-ran verify_trilogy.py grid including N=2: T1_OK. (T3) PASS on stated route: Z=|x|1_{bad}; E[Z]=(9/7)c0 T^{-7/2} (k=1<4.5 finite), E[Z^2] has k=2<4.5 finite, E[Z^3] has k=3<4.5 finite (C=3c0 T^{-1.5}=0.799T^{-1.5}); third-moment expansion E[(sumZ)^3]=M E[Z^3]+3M(M-1)E[Z^2]E[Z]+M(M-1)(M-2)E[Z]^3<=1.33256 N^{129/81} uses only convergent moments; Markov against (N^{3/2}w)^3=N^{229.5/81} gives 1.33256 N^{-100.5/81}<=N^{-1} iff N^{19.5/81}>=1.33256, N0=4 sharp for majorant (3^{19.5/81}=1.3028<1.33256<=4^{19.5/81}=1.3962). (T2) FAIL fatally: proof sets Y=x^2 1_{bad} and claims E[Y^3]=3c0 T^{+3/2}=0.799 T^{1.5}. But Y^3=|x|^6 1_{|x|>T} corresponds to k=6>alpha=4.5, whose Pareto integral diverges: int_T^R 4.5 c0 t^{0.5} dt=3c0(R^{1.5}-T^{1.5})->infinity (R=10:19.7, 100:793.8, 1000:25273, 10000:799383). The formula C_k=4.5c0/|k-4.5| is valid only for k<4.5 (convergent upper tail); applying it at k=6 has no mathematical basis. Hence A2=4.36045 N^{231/81} and the N0=22 Markov chain are unproved; verify_trilogy.py only asserts the finite constants, it does not detect divergence. Consequences: the 'm=2 majorant 2.628 N^{-80/81} misses by N^{1/81}, third moments necessary and sufficient' comparison is invalid (m=3 object is infinite, not a tighter finite bound); 'N0 sharpness' for T2 refers to an invalid majorant. Correct finite-moment tools do not close the stated N0 on inspection: with only convergent EY=1.8c0 T^{-2.5}, EY2=9c0 T^{-0.5}, one-sided Chebyshev Var/ (thr-mean)^2 at N=22 gives 0.1001 > 1/22=0.04545; at N=100 gives 0.0168>0.01; at N=1000 gives 0.00125>0.001 (only N>=10000 passes). So T2 as stated is unproved and not repaired by the obvious finite-moment fallback. Monte Carlo (200k trials, exact Pareto sampler |X|=x_m U^{-1/4.5}) gives empirical P(sumY>Mw)=0.0078 at N=22 (below 0.045) and 0.00096 at N=100, so the inequality may be true, but that is experimental evidence, not proof — distinguished per audit standard. Calibration (xm^2=5/9, EX^2=1, EX^4=25/9, c0=0.2664629696, tau=37/81 identities) re-ran CALIBRATE_OK and is correct; criticality algebra tau_count=34/81 > tau_first=19/63 > tau_quad=2/9 is correct as algebra but inherits T2's unproved premise as a 'binding' claim. DRAFT Sec.5 is truncated ledger, not a proof of target/fallback. Report honestly disclaims target N^{-1/18} rate and fallback rigidity (good-matrix local law open). One of three headline legs is mathematically invalid; headline correctness FAILS. value: EMERGENT_FINDING: no Admission conditional-value presumption; applied ordinary full value standard. Even if T2 were repaired, the trilogy is elementary i.i.d. Pareto tai…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: Does not prove the full N^{-1/18} Tracy-Widom Kolmogorov rate (target), nor the literal fallback rigidity inequality: both additionally require edge control (local law/delocalization) of the truncated good matrix at support N^{34/81}-N^{37/81}, which is stated as the explicit open step and is not claimed. Numerical support is small-N only. Constants/N0 sharpness claims refer to the stated majorants, not to optimality of the exponents.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
