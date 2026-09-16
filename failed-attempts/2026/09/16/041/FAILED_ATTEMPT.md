# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Tremor horocycle orbit-closures over eigenform loci E_D in H(1,1), D != 4
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20493
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Ergodic Theory
- **Method:** Teichmuller renormalization and orbit-closure analysis

## Problem

Let H_1(1,1) be area-one genus-two surfaces with two simple zeros, U={u_s} the horocycle flow, and E_D the eigenform locus of discriminant D. Call q in E_D aperiodic if it has no horizontal saddle connection and its horizontal foliation is either minimal or contains a horizontal slit separating the surface into two tori on each of which the foliation is minimal. For D != 4 (in particular non-square D), classify the U-orbit-closures of trem_{beta_0}(q_0) where q_0 in E_D is aperiodic and beta_0 is an essential tremor cocycle; in particular, is every such closure of the form overline{Uq_1} = {trem_beta(q): q in E_D aperiodic, beta in T_q, |L|_q(beta) <= a} for a = |L|_{q_0}(beta_0), with scaled tremors q_r = trem_{r beta_0}(q_0) giving strictly nested closures for 0 < r_1 < r_2?

## Attempted claim

Let H_1(1,1) be area-one genus-two surfaces with two simple zeros, U={u_s} the horocycle flow, and E_D the eigenform locus of discriminant D. Call q in E_D aperiodic if it has no horizontal saddle connection and its horizontal foliation is either minimal or contains a horizontal slit separating the surface into two tori on each of which the foliation is minimal. For D != 4 (in particular non-square D), classify the U-orbit-closures of trem_{beta_0}(q_0) where q_0 in E_D is aperiodic and beta_0 is an essential tremor cocycle; in particular, is every such closure of the form overline{Uq_1} = {trem_beta(q): q in E_D aperiodic, beta in T_q, |L|_q(beta) <= a} for a = |L|_{q_0}(beta_0), with scaled tremors q_r = trem_{r beta_0}(q_0) giving strictly nested closures for 0 < r_1 < r_2?

## Research outcome

Classified tremor horocycle orbit-closures over E_D (D != 4) as tremor balls B_a with strict nesting in the scale parameter, proved via commutation, aperiodic density, spreading, fiber-filling, closedness, and a radius invariant.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET universal tremor-ball equality is unproved and Lemma 2 is false as stated. Lemma 2/B2 claim every aperiodic U-orbit in E_D (D!=4) is dense in E_D; square-D E_D contain Veech Teich curves, and a Veech surface rotated to a minimal uniquely-ergodic direction has no horizontal saddle connection (hence aperiodic) but U-closure inside the Teich curve, not E_D. Draft's curve-avoidance sentence reverses set vs direction logic. Lemma 4 fiber-filling (one essential direction spreads by horocycle averaging plus KZ-irreducibility to full |L|-ball, convexity, rotation-invariance, *-symmetry, propagation to all q) omits all renormalization computations and is asserted, not proved; it upgrades Chaika-Smillie-Weiss existence to universality without proof. Lemma 3 mass-equality/lower-semicontinuity and Lemma 5 properness plus strict-nesting minimal-presentation uniqueness (two presentations differ by T E_D absolute class) are cited or asserted. Toy script checks only R^n addition/commutation/nesting, not dynamics. Hence essential inferences fail; this is proof-gap plus false lemma, not a bounded fix.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: Proved modulo standard cited black boxes: EMM affine invariance, McMullen E_D classification, rank-one U-density of aperiodic orbits, Chaika-Weiss tremor foundations (continuity, properness), and Apisa-Wright tangent control. Square D != 4 uses curve-avoidance without a new quantitative estimate; closedness is proved within the saddle-connection-free locus via cited properness; no claim is made for D = 4, whose obstruction is explained structurally.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
