# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Closing open C4-extremal intervals at n=41-48: exact decision at a width-one order and variance-refined upper bounds below recorded minima
- **Round:** 2026-09-07-first-light-01
- **Lane:** 170
- **Disposition:** NO_RESULT
- **Domain:** Extremal Graph Theory
- **Method:** stability-constrained degree-sequence elimination with polarity-subgraph local search and variance-corrected pair-counting bounds

## Problem

For n in 41..48, where ex(n,C4) is currently known only as a strict interval (e.g., OEIS A006855 comments: 132<=a(41)<=133, 137<=a(42)<=139, 142<=a(43)<=145, 148<=a(44)<=151, 154<=a(45)<=158, 157<=a(46)<=165, 163<=a(47)<=171, 168<=a(48)<=176), decide at least one width-one order exactly (primary target: ex(41,C4) in {132,133}) by (a) exhibiting an explicit C4-free witness at the lower end and (b) a degree-sequence stability-elimination proof log ruling out the top value; and tighten upper bounds across the rest of the window strictly below the current recorded minima via a variance-corrected pair-counting argument.

## Attempted claim

Exact value ex(41,C4) decided (either a verified 133-edge C4-free graph on 41 vertices closing upward, or a stability-elimination proof log that no 133-edge C4-free graph exists, certifying ex(41,C4)=132), plus refined upper bounds U'(n) < U_rec(n) for at least two further n in 42..48, each with a replayable variance-corrected degree-pair proof log and explicit lower-bound witnesses L(n) at or above recorded minima.

## Research outcome

Attempted to beat recorded ex(n,C4) bounds for n=41..48 (baselines live-confirmed: OEIS lower 132..168, upper 133..176). Lower-bound search (ER7 polarity deletion/swap-SA, GRASP, eject chains, AG(2,7) incidence) peaked 1-3 edges below McKay minima (130..167). Upper-bound attack proved sound Lemma N and enumerated top-count degree-sequence spaces with 58-99.9% elimination, but survivors remain so no top count falls. No strict improvement: NO_RESULT with a verified partial theorem, full survivor logs, calibration witnesses, and an independent stdlib verifier.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['No recorded OEIS/McKay bound beaten: no width-one closure and no strict upper- or lower-bound improvement; fallback claim not met.', 'Lemma N leaves survivors (434/66/62/5/21); top counts not ruled out.', 'Enumeration covers only the single recorded top count per n for n=44..48.', 'ex(D,C4) table applied strictly inside exact range (observed max degree <=10, verifier guard <=20).', 'Lower-bound search was bounded (~30 min across engines); ER7 route empirically exhausted 1-3 edges short.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['No recorded OEIS/McKay bound beaten: no width-one closure and no strict upper- or lower-bound improvement; fallback claim not met.', 'Lemma N leaves survivors (434/66/62/5/21); top counts not ruled out.', 'Enumeration covers only the single recorded top count per n for n=44..48.', 'ex(D,C4) table applied strictly inside exact range (observed max degree <=10, verifier guard <=20).', 'Lower-bound search was bounded (~30 min across engines); ER7 route empirically exhausted 1-3 edges short.']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
