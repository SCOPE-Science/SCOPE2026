# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Quantified CKN threshold step for circulation-capped axisymmetric-with-swirl flows
- **Round:** 2026-09-07-first-light-01
- **Lane:** 610
- **Disposition:** NO_RESULT
- **Domain:** Mathematical Fluid Dynamics
- **Method:** Caffarelli-Kohn-Nirenberg epsilon-regularity with Carleman backward-uniqueness and self-similar profile comparison

## Problem

Fix the named class A(1): axisymmetric suitable weak solutions (CKN sense) in Q1 = B1(0) x (-1,0) with swirl u^theta possibly nonzero and scale-invariant circulation bound sup|Gamma| <= 1 where Gamma = r u^theta. With CKN functionals D(r), C(r), P(r) and E(r) = D+C+P at an axis point taken as (0,0), either (a) prove an improved epsilon-regularity threshold E(1) <= eps_1 implies regularity in Q_{1/2} with explicit eps_1 >= 1.5 eps_ref (eps_ref = Guevara-Phuc reference constant), thereby excluding one discretely self-similar swirl blow-up profile class, or (b) exhibit an explicit logged axisymmetric (discretely) self-similar barrier witness with swirl and scaled energy e_star sharply constraining the optimal threshold from below. Preserve high-risk mode: do not domesticate to routine enumeration. Valuable partial: certified one-cylinder decay, single-profile exclusion, or one-step backward-uniqueness lemma.

## Attempted claim

Let A(1) be axisymmetric suitable weak solutions in Q1 with sup|Gamma| <= 1, Gamma = r u^theta, and let E(r) be as above at axis point (0,0) with reference constant eps_ref from Guevara-Phuc Theorem 1.2. Prove that E(1) <= eps_1 with explicit eps_1 >= 1.5 eps_ref implies (0,0) is a regular point (u bounded in Q_{1/2}), and consequently no axisymmetric discretely self-similar swirl blow-up with factor lambda in [1,2] and profile circulation sup|r U^theta| <= 1 can arise as a blow-up limit in A(1). In the dual direction, if the improvement fails, exhibit an explicit logged barrier witness field with scaled energy e_star pinning the optimal threshold from below. Binary test: proof with logged eps_1 (or e_star) and cylinder energies.

## Research outcome

Target blocked on three legs (existential-only eps_ref; Gamma-cap non-smallness; open DSS-barrier existence). Validated target exit taken; exact preset fallback E(1)<=1e-4 => E(1/2)<=3/4 E(1) pursued via four reproduced quantitative budget routes (R1-R4, script + log in artifacts), all blocked by factors x5-x93. Statement not disproved. No emergent finding. CLEAN_EXIT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['No numeric eps_ref exists in Guevara-Phuc (existential-only); target 1.5x margin unauditable without a full quantitative CKN re-proof.', 'Gamma cap sup|Gamma|<=1 gives no energy smallness (1/r-annulus counterexample); swirl coupling O(r^-3) with sharp Hardy constant.', 'DSS barrier leg is an open singular-existence problem.', 'Fallback budgets are PDE-free/ideal-constant feasibility blocks (x5-x93), not a disproof of the true decay statement; proof remains open.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['No numeric eps_ref exists in Guevara-Phuc (existential-only); target 1.5x margin unauditable without a full quantitative CKN re-proof.', 'Gamma cap sup|Gamma|<=1 gives no energy smallness (1/r-annulus counterexample); swirl coupling O(r^-3) with sharp Hardy constant.', 'DSS barrier leg is an open singular-existence problem.', 'Fallback budgets are PDE-free/ideal-constant feasibility blocks (x5-x93), not a disproof of the true decay statement; proof remains open.']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
