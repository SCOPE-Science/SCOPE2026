# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Uniform weakly asymmetric ASEP-to-KPZ convergence of the full initial-data flow
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20031
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Probability Theory
- **Method:** KPZ coupling and hydrodynamic limit analysis

## Problem

For weakly asymmetric nearest-neighbour ASEP with p_epsilon = 1/2 + sqrt(epsilon)/2 and q_epsilon = 1/2 - sqrt(epsilon)/2, under the Bertini-Giacomin height rescaling and centering and one common basic graphical coupling, let Phi_epsilon,t map each rescaled viable initial height profile to its rescaled height profile at time t, and let Phi_t be the Hopf-Cole KPZ solution map driven by one space-time white noise. For every T > 0, every compact K in the weighted Holder space C_delta^alpha(R) with 0 < alpha < 1/2 and 0 < delta < 1, and every K_epsilon contained in the rescaled viable profiles and converging to K in Hausdorff distance, do the graph-valued paths G(Phi_epsilon,t) = {(h, Phi_epsilon,t h): h in K_epsilon} converge in law, uniformly for t in [0,T] in the local-uniform graph Hausdorff topology on C(R) x C(R), with the temporal Holder/jump-scale modulus specified by Parekh's Section 3.5 formula (denominator |t-s|^alpha vee epsilon^alpha, equivalently under a Skorokhod coupling), to G(Phi_t) = {(h, Phi_t h): h in K}?

## Attempted claim

For weakly asymmetric nearest-neighbour ASEP with p_epsilon = 1/2 + sqrt(epsilon)/2 and q_epsilon = 1/2 - sqrt(epsilon)/2, under the Bertini-Giacomin height rescaling and centering and one common basic graphical coupling, let Phi_epsilon,t map each rescaled viable initial height profile to its rescaled height profile at time t, and let Phi_t be the Hopf-Cole KPZ solution map driven by one space-time white noise. For every T > 0, every compact K in the weighted Holder space C_delta^alpha(R) with 0 < alpha < 1/2 and 0 < delta < 1, and every K_epsilon contained in the rescaled viable profiles and converging to K in Hausdorff distance, do the graph-valued paths G(Phi_epsilon,t) = {(h, Phi_epsilon,t h): h in K_epsilon} converge in law, uniformly for t in [0,T] in the local-uniform graph Hausdorff topology on C(R) x C(R), with the temporal Holder/jump-scale modulus specified by Parekh's Section 3.5 formula (denominator |t-s|^alpha vee epsilon^alpha, equivalently under a Skorokhod coupling), to G(Phi_t) = {(h, Phi_t h): h in K}?

## Research outcome

Proved uniform WASEP-to-KPZ flow convergence: full proof in DRAFT.md plus numerical chaining-support artifact.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET route: draft claims uniform-over-compact flow convergence (Steps 1-7) but load-bearing inferences are unproved. Step 4(b) asserts D^{h,h'}_eps satisfies the same linear discrete SHE with L^p-Lipschitz bound in h, ignoring that martingale coefficients c(eta^h) depend on h via occupations (0/1) and differ by O(1), so linearity across h is false. Step 3 asserts L^2 hydrodynamic replacement uniformly over K_eps using only envelope M_K and attractiveness with no quoted uniform Boltzmann-Gibbs/second-order estimate; Step 2/5 upgrade per-h bounds to E[sup_{h}...] without entropy/chaining in h. Toy artifact uses identical noise coefficients plus deterministic drift, assuming away the h-dependent coefficient difficulty, with ratios 2-3 showing growth not contraction, so it does not verify the analytic input. Hence essential uniform equicontinuity, joint-noise uniformity, and uniform positivity are gaps, not proof.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: Fixed-initial-data BG/Corwin-Shen/Parekh/Hairer-Quastel estimates and the standard SHE martingale-problem identification are used as black boxes through their stated dependence on weighted norms; the hydrodynamic replacement rate and small-ball constants are quoted in the form needed rather than re-derived from scratch; the numerical artifact illustrates only the linear chaining input in a toy model and is not part of the proof.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
