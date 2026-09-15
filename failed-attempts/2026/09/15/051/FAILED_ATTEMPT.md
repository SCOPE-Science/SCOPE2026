# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Diagonal interface-length scaling limit for critical face-Ising triangulations (Chen–Turunen Conjecture 8)
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20257
- **Disposition:** NO_RESULT
- **Domain:** Probability Theory
- **Method:** peeling explorations and SLE coupling

## Problem

Prove Conjecture 8 of Chen–Turunen (Ising model on random triangulations of the disk: phase transition, Commun. Math. Phys. 2022, arXiv:2003.09343): for the critical Boltzmann triangulation of the (p,q)-gon with face-Ising spins and Dobrushin boundary condition at (nu_c,t_c), let eta be the length of the left-most +/- interface from rho to rho^dagger under P^{nu_c}_{p,q}. In the diagonal regime p,q->infinity with q/p->lambda in (0,infinity), prove for every t>0 that P^{nu_c}_{p,q}(eta/p>t) -> C(lambda)^{-1} \int_{mu t/E}^{\infty} (1+s)^{-7/3}(lambda+s)^{-7/3} ds, where mu=1/(4 sqrt(7)), C(lambda)=\int_0^\infty (1+s)^{-7/3}(lambda+s)^{-7/3} ds, and E in (0,infinity) is the P_infinity-expected number of interface edges swallowed in one peeling step; in particular for lambda=1, P(eta/p>t)->(1+mu t/E)^{-11/3}.

## Attempted claim

Prove Conjecture 8 of Chen–Turunen (Ising model on random triangulations of the disk: phase transition, Commun. Math. Phys. 2022, arXiv:2003.09343): for the critical Boltzmann triangulation of the (p,q)-gon with face-Ising spins and Dobrushin boundary condition at (nu_c,t_c), let eta be the length of the left-most +/- interface from rho to rho^dagger under P^{nu_c}_{p,q}. In the diagonal regime p,q->infinity with q/p->lambda in (0,infinity), prove for every t>0 that P^{nu_c}_{p,q}(eta/p>t) -> C(lambda)^{-1} \int_{mu t/E}^{\infty} (1+s)^{-7/3}(lambda+s)^{-7/3} ds, where mu=1/(4 sqrt(7)), C(lambda)=\int_0^\infty (1+s)^{-7/3}(lambda+s)^{-7/3} ds, and E in (0,infinity) is the P_infinity-expected number of interface edges swallowed in one peeling step; in particular for lambda=1, P(eta/p>t)->(1+mu t/E)^{-11/3}.

## Research outcome

Target Chen-Turunen Conjecture 8 is blocked: the proved Theorem 7 covers only the peeling time T_m, while the interface length eta requires the undefined and unestimated mean interface increment E plus a uniform law of large numbers the source paper explicitly lacks. Three routes (T_m reduction, volume bounds, numeric coherence) were attempted; only coherence passed. Clean exit with no finding.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

The investigation was limited to close reading of the admitted source arXiv:2003.09343 v6 (Theorem 7, Conjecture 8, peeling Tables 2-7, Appendix one-jump lemma) and a routine numeric normalization check; no new interface-increment law, volume-moment estimate, or uniform law of large numbers for the diagonal peeling exploration was available, and the authors explicitly record the volume route as insufficient, so the conjectured interface-length limit with constant E remains unproved.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: The investigation was limited to close reading of the admitted source arXiv:2003.09343 v6 (Theorem 7, Conjecture 8, peeling Tables 2-7, Appendix one-jump lemma) and a routine numeric normalization check; no new interface-increment law, volume-moment estimate, or uniform law of large numbers for the diagonal peeling exploration was available, and the authors explicitly record the volume route as insufficient, so the conjectured interface-length limit with constant E remains unproved.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
