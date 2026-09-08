# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** A minimal no-show paradox witness with Banzhaf-Shapley gap in 6-8 voter weighted games at Penrose quotas
- **Round:** 2026-09-07-first-light-01
- **Lane:** 116
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Social Choice Theory
- **Method:** exact power-index enumeration with paradox-profile transfer analysis

## Problem

Survey canonical weighted voting games [w;q] on n in {6,7,8} voters with quotas in the Penrose square-root window q in [0.50,0.65] of total weight for an explicit participation-failure witness: a concrete weight vector, quota, and ballot profile where a voter strictly benefits by abstaining (no-show paradox) or a transfer of support strictly harms, with exact Banzhaf and Shapley-Shubik vectors before and after.

## Attempted claim

There exists a weighted voting game on n in {6,7,8} with normalized quota q in [0.50,0.65] and an explicit ballot profile such that (i) a specified voter obtains a strictly preferred outcome by abstaining (or a specified transfer strictly harms its recipient), and (ii) the exact normalized Banzhaf and Shapley-Shubik vectors before and after are computed in rationals and exhibit a certified gap of at least a stated rational threshold versus the Penrose square-root estimate.

## Research outcome

Minimal 6-voter Penrose-window witness coupling a tie-break-free no-show paradox and upward-monotonicity failure on one profile with a certified dual Banzhaf/Shapley gap >=1/25, all exactly reproducible.

## Why this attempt failed

Failed axes: originality, value.

originality: Substantively not new. IRV failure of participation/no-show and upward monotonicity are textbook theorems (Moulin 1988 participation; Fishburn-Brams/Doron-Kronick monotonicity), not open problems. Any weighted profile with total weight 21 splits into 21 unit voters, so the 6-voter weighted example is a 21-voter unweighted IRV paradox instance of a known phenomenon — a parameter substitution, not a new object. Exact Banzhaf/Shapley enumeration for one 6-voter game is a routine 2^6 exercise; deviation ~0.08 from the asymptotic Penrose sqrt-share at n=6 is expected and carries no threshold motivation (1/25 arbitrary). The 'coupling' is artificial: indices play no role in the paradox proof (different rules: paradox in weighted IRV, indices on [w;Q] Yes/No game, openly admitted). Nearest priors subsume it: Bonifacio-Fioravanti general participation incompatibilities, Kurz minimum-sum enumeration infrastructure, Aziz-Paterson/Rushdi computation methods, plus textbook IRV counterexamples. Verbatim triple not recorded, but phenomenon is mechanically implied by textbook results; failed-search/timestamp does not establish priority. value: Not independently worth finding later. Falls into explicit reject classes: (1) textbook restatement — IRV violates no-show and monotonicity, proved decades ago with simpler unweighted 3-candidate examples; this adds a heavier weighted instance with no minimality claim. (2) mere parameter substitution — weights (6,5,4,3,2,1) and quota 4/7 add no conceptual leverage; any majority quota in [0.5,0.65] qualifies, so 'Penrose window' is a weak relabel, not a design connection (Jagiellonian/optimal-quota theory concerns Yes/No power, not IRV transfers). (3) tiny unmotivated gain — dual-gap >=1/25 at voter 0 is an arbitrary cutoff on an expected small-n deviation with no downstream theorem, calibration use, or approximation consequence; post-abstention footprint (lightest voter to 1/30) likewise has no stated use. No benchmark need is shown beyond existing paradox examples and power-index tables. Fallback census over n=6-8 window would be database repackaging.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The no-show/monotonicity failure is in weighted IRV with the stated weights and majority quota, not in a bare Yes/No quota referendum (which is provably no-show-free; lemma included). Single explicit witness, not a full n=6-8 census; minimality of weights not claimed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
