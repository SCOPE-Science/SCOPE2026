# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Uniform-envelope dimension persistence and polynomial barrier-cost obstruction for the 2D GFF at gamma=1
- **Round:** 2026-09-07-first-light-01
- **Lane:** 599
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Statistical Field Theory
- **Method:** Gaussian multiplicative chaos moment method with circle-average Bessel-barrier and rooted-measure Frostman estimates

## Problem

Decide whether the one-sided uniform (perfect) gamma0=1 envelope of the 2D continuum GFF (Dirichlet unit disc, circle averages h_r) retains full thick-point dimension: with Q=[1/4,3/4]^2 and Perfect_1(Q)={z in Q: exists C(z)<infinity with h_{2^{-k}}(z)>=k ln2-C(z) for all k>=1}, prove dim_H Perfect_1(Q)=3/2 a.s. via conditioned rooted-measure Frostman estimates, and certify the universal thick-plus-barrier first-moment rate 3/2 showing the barrier cost is polynomial, not exponential.

## Attempted claim

Almost surely, dim_H(Perfect_1(Q))=3/2, where Q=[1/4,3/4]^2 and Perfect_1(Q)={z in Q: exists C(z)<infinity with h_{2^{-k}}(z)>=k*ln2-C(z) for all k>=1} for the continuum GFF circle-average field in the Dirichlet unit disc; i.e. the one-sided uniform gamma0=1 envelope retains the full classical HMP dimension with no exponential increment, the barrier cost being at most polynomial.

## Research outcome

Proved a.s. dim_H Perfect_1(Q)=3/2 at gamma=1: HMP-superset upper bound plus tilted-measure Frostman lower bound with machine-certified first-moment rate 3/2, certified naive-route obstruction, and corrected tilted energy bounds for all s<3/2.

## Why this attempt failed

Failed axes: correctness.

correctness: Upper bound is sound: Perfect_1 subset limsup a-thick set at a=1/2 and HMP Lemma 3.1 gives dim<=3/2. Lower-bound headline 'a.s. dim=3/2 for continuum GFF' is NOT proved. What is machine-certified is BRW-model DP (reproduced: P1 table, tilted energies 3.14/6.70/8.62/12.37 at K=10 etc. match json). Essential GFF transfer is asserted, not proved: (i) Kahane comparison claimed to preserve exponential rate and O(1) tilted ratio up to constants uniform on Q0 from variance/increment numeric checks on k=2..5 only — no covariance-majorization matrices, no treatment of barrier indicators (non-convex) vs Kahane's convex-exponential scope; (ii) Paley-Zygmund/weak-compactness Frostman limit for two-sided tube stated without tightness/energy-lower-semicontinuity/support argument, using dyadic 2^-K scales not HMP factorial scales; (iii) Domain-Markov 0-to-1 boost ('harmonic shift absorbed by taking C larger') stated without bound: sup of harmonic extension on subdisc is unbounded Gaussian, no conditioning/quantitative absorption shown. Model-side asymptotics also overstated: F1 claims P1=c0 2^-K/2 K^-1/2(1+o(1)) but reproduced P1*2^K/2*sqrt(K)=12.92,16.24,17.72,19.22,20.41,21.31 at K=10,15,20,25,30,40 (strictly growing, effective poly exponent q~0.13-0.35, pre-asymptotic); compute_rates.py assumes K^-3/2 (corr -1.5 log2K/K) contradicting draft's K^-1/2 correction -(log2K)/2K and circular for rates.json. F2 claims raw R_j~2^j K/(K-j) (naive cap at s=1) but logged dp_verify.json gives R/2^j=1.0,0.51,0.21,0.07,0.022,0.006,0.0015,... decaying, i.e. R_j~2^{j/2} not 2^j; both raw S_1.4 (26.8->63.7) and tilted S_1.4 (9.2->13.7) still grow in K to 30-40, and s=1.49 tilted 8.6->36.8 growing, so uniform boundedness for all s<3/2 is summand-heuristic extrapolation, not uniform-cap certificate. Q-boundary fix (Q0=[1/4,1/2]^2) is honest and sound. Overall: valuable BRW ballot/tilt calculations reproduced, but continuum a.s. equality does not follow from logged certificates.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: GFF transfer comparison inequalities and Frostman weak-limit/0-1 boost given as complete auditable route with model-side machine certificates and field-side numeric covariance inputs, not line-by-line formalization; lower bound lives on fixed boundary-avoiding Q0 since Q exits the disc; s=1.49 energy summable in j but value still growing at K=40 (summand-level, not uniform-cap, convergence).

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
