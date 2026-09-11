# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Top-eigenvector localization with explicit IPR bound for the Pareto alpha=3 Wigner ensemble
- **Round:** 2026-09-07-first-light-01
- **Lane:** 855
- **Disposition:** NO_RESULT
- **Domain:** Random Matrix Theory
- **Method:** maximal-entry isolation with rank-one perturbation and resolvent-diagonal comparison

## Problem

For the explicit normalized Pareto alpha=3 Wigner ensemble E3, prove that the top eigenvector localizes: its inverse participation ratio stays bounded away from zero with high probability, in sharp contrast to GOE delocalization.

## Attempted claim

For the normalized Pareto alpha=3 Wigner ensemble E3 of dimension N, let v_1 be the unit top eigenvector. Then with probability tending to 1 as N->infinity, max_i|v_1(i)|^2 >= 1/2 and hence the inverse participation ratio satisfies IPR(v_1)=sum_i|v_1(i)|^4 >= 1/4, whereas for GOE, IPR=O(log N/N) with high probability; i.e. the top eigenvector is localized on the maximal entry.

## Research outcome

Target blocked and cleanly exited. The exact constant max_i|v1(i)|^2>=1/2 w.h.p. is incompatible with the generic off-diagonal spike mechanism (pair localization caps single-site mass at ~1/2 from below: 0/40 trials cross 1/2); the spike is unseparated at feasible N (emerges only for N>~7000); and the decision-phase pair-mass repair also fails (localization site mismatches argmax at accessible N). No independently auditable alternative was completable; CLEAN_EXIT with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['No theorem proved: neither the target conjunction nor any adjacent alternative was certified.', 'Asymptotic spike analysis (M_typ ~ c N^{1/6}) confirms the mechanism but requires N > ~7000 for spike separation, beyond feasible exact eigendecomposition in-session.', 'The pair-block correction is standard spike-analysis method, not an original result; no EMERGENT_FINDING is claimed.', 'Finite-N tables (recovery_test.json, pair_stats.json) are diagnostic evidence for the exit decision, not asymptotic proof.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['No theorem proved: neither the target conjunction nor any adjacent alternative was certified.', 'Asymptotic spike analysis (M_typ ~ c N^{1/6}) confirms the mechanism but requires N > ~7000 for spike separation, beyond feasible exact eigendecomposition in-session.', 'The pair-block correction is standard spike-analysis method, not an original result; no EMERGENT_FINDING is claimed.', 'Finite-N tables (recovery_test.json, pair_stats.json) are diagnostic evidence for the exit decision, not asymp…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
