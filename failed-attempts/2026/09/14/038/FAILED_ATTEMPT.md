# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** YZZ Heegner height on disc-6 Shimura curve over Q(sqrt(-19))
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1914
- **Disposition:** AUDIT_1_REJECT
- **Domain:** arithmetic geometry
- **Method:** Yuan-Zhang-Zhang Shimura-curve Gross-Zagier formula

## Problem

Let B be the indefinite quaternion algebra over Q of discriminant 6, let X be the Shimura curve attached to an Eichler order of squarefree level 7 coprime to 6, and let A/Q be the GL2-type abelian variety that is the Jacquet-Langlands transfer to X of a weight-2 newform f of level 42 with trivial character whose Atkin-Lehner eigenvalues at 2, 3, 7 are compatible with ramification at 2 and 3. Let K = Q(sqrt(-19)), in which 2 and 3 are inert and 7 splits, satisfying the Shimura-curve Heegner hypothesis for (B, level 7). Let D_K be the Heegner CM divisor on X defined over K and P_A its image in A(K) via the Jacquet-Langlands parametrization with an Atkin-Lehner-selected Schwartz test function in the Yuan-Zhang-Zhang incoherent Weil representation. Via the Yuan-Zhang-Zhang Gross-Zagier height formula, decide whether the Neron-Tate height of P_A is nonzero, equivalently whether L'(1/2, pi_A, K) != 0 with analytic rank one for A/K, where this derivative is not tabulated. A complete answer is a self-contained proof either of nonzero height with explicit YZZ constant and rank-one conclusion, or of zero height with vanishing derivative, via a bounded attack combining Dokchitser L-derivative evaluation with explicit CM-divisor and local-height computation, with order, level, embedding, and test vector fully specified.

## Attempted claim

Let B be the indefinite quaternion algebra over Q of discriminant 6, let X be the Shimura curve attached to an Eichler order of squarefree level 7 coprime to 6, and let A/Q be the GL2-type abelian variety that is the Jacquet-Langlands transfer to X of a weight-2 newform f of level 42 with trivial character whose Atkin-Lehner eigenvalues at 2, 3, 7 are compatible with ramification at 2 and 3. Let K = Q(sqrt(-19)), in which 2 and 3 are inert and 7 splits, satisfying the Shimura-curve Heegner hypothesis for (B, level 7). Let D_K be the Heegner CM divisor on X defined over K and P_A its image in A(K) via the Jacquet-Langlands parametrization with an Atkin-Lehner-selected Schwartz test function in the Yuan-Zhang-Zhang incoherent Weil representation. Via the Yuan-Zhang-Zhang Gross-Zagier height formula, decide whether the Neron-Tate height of P_A is nonzero, equivalently whether L'(1/2, pi_A, K) != 0 with analytic rank one for A/K, where this derivative is not tabulated. A complete answer is a self-contained proof either of nonzero height with explicit YZZ constant and rank-one conclusion, or of zero height with vanishing derivative, via a bounded attack combining Dokchitser L-derivative evaluation with explicit CM-divisor and local-height computation, with order, level, embedding, and test vector fully specified.

## Research outcome

TARGET resolved on the nonzero side: unique level-42 newform identified as E=[1,1,1,-4,5]; over Q(sqrt(-19)) analytic rank one with L'(E/K,1)≈2.6579!=0 and Heegner point (457,9699) of Neron-Tate height ≈4.2277, via reproducible PARI/GP evidence plus YZZ/JL theorems.

## Why this attempt failed

Failed axes: originality, value.

originality: The exact numerical payload is already tabulated in the official LMFDB database: 15162.j5 records the -19 twist of 42a1 with conductor 15162, analytic and Mordell-Weil rank 1, generator (449,9255) (same point as (457,9699) on the draft's model), regulator 4.22771015427673, L'=3.05904911868116, and minimal twist 42a1; 42.2.a.a records dimension 1, the identical q-expansion, and Atkin-Lehner signs -1,+1,+1; 42.a records the isogeny class, torsion, and modular degree. Given these tabulations plus the general Gross-Zagier/Kolyvagin theorems cited by the draft itself, nonzero height and analytic rank one follow mechanically. No new local YZZ computation was performed: the 'explicit constant' is the arithmetic ratio of two tabulated numbers. value: FAIL with ADMISSION_DEFECT: topic.json premises value on this derivative being 'not tabulated', but full-page LMFDB inspection shows L'(E^D,1)=3.05904911868116, the regulator, generator, and ranks are tabulated for exactly this curve and twist, so the admission qualification was materially false. What remains is a known-database recomputation: re-deriving tabulated invariants with PARI and relabeling their ratio as a YZZ constant, with no new theorem, boundary, or downstream fact a future researcher could not already retrieve from LMFDB. Certification and replayability strengthen evidence but do not create value under the shared STANDARD.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The Shimura-curve CM divisor is identified with the classical Heegner point via Jacquet-Langlands/Picard functoriality rather than exhibited in coordinates on a model of X; the YZZ constant is given numerically and structurally, not re-derived local integral by local integral; PARI height/L-value/rank values are trusted multiprecision numerics stable across 64/128/256-bit precision rather than interval-certified proofs; the Manin constant is taken as 1 for the optimal squarefree-level quotient,…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
