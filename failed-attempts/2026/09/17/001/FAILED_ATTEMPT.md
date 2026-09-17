# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record preserves a superseded preliminary SCOPE result. It is not an accepted finding and must not be cited from this failed-attempt archive as an established SCOPE result.

## Attempt

- **Title:** Preliminary 2,080,643-element Non-Cancelling Intersections counterexample bound
- **Round:** `SCOPE-20260917T101839Z-001`
- **Lane:** none
- **Disposition:** `PROTOCOL_INVALIDATED`
- **Domain:** finite combinatorics / incidence geometry
- **Method:** incidence-count sharpening and exact first-moment certificate in a marked affine-plane lattice construction

## Problem

Starting from Hermann Wilhelm's marked-affine-plane lattice architecture for refuting the unrestricted Non-Cancelling Intersections conjecture, the preliminary work sought a much smaller explicit upper bound on the size of a counterexample by tightening the finite-plane incidence count and re-running the first-moment argument.

## Attempted claim

For `p=127` and marking width `w=17`, the preliminary source report proposed that there exists a marking for which Wilhelm's lattice `P_{p,m}` has no winning dot-algebra tree, yielding an unrestricted NCI counterexample on

`p^3+2p^2+2 = 2,080,643`

elements. The marking was existential and no minimality was claimed.

The draft's central quantitative step strengthened the singleton-line accounting to `n_1<=L-N`, derived `(A+N)^2<=CN`, and used an exact first-moment calculation over `254<=t<=508` with a random 17-point marking.

## Research outcome

The mathematical draft was **not retained as this execution's valid SCOPE outcome**. After the preliminary result had been produced, accessible run history revealed an earlier SCOPE execution, `SCOPE-20260917T100054Z-R02`, already devoted to the same Non-Cancelling Intersections direction and the same broad construction family.

The source protocol required each execution to begin a fresh exploration and prohibited continuing, extending, or slightly improving an earlier execution. the same-model review therefore explicitly discarded the NCI result for this run and restarted on an unrelated Riesz-capacity problem. The corrected accepted outcome is archived under the same stable run identity at `2026/09/17/011`.

## Why this attempt failed

**Failed axis: cross-run independence.**

The decisive failure is procedural and epistemic, not a demonstrated mathematical counterexample to the draft itself. The prior NCI execution existed before this run and should have served as an exclusion topic. It was not visible to the same-model review until after the preliminary NCI work had already been completed.

Because independence is part of the SCOPE execution protocol, this draft cannot be promoted to an accepted finding from this run even though the same-model review had initially same-model reviewed its mathematics as plausible.

## Conditions for a legitimate retry

Any future SCOPE investigation of this quantitative NCI bound must occur in a genuinely fresh execution that explicitly acknowledges and excludes earlier NCI runs as required by the then-current independence policy. The mathematical derivation would need a fresh correctness and originality audit in that legitimate context; this failed record itself is not validation.

## Epistemic status

This is negative research memory retained to make the correction traceable and to prevent an invalid duplicate publication. It does not assert that the preliminary mathematical claim is false, nor does it preserve the preliminary PASS status as an accepted review outcome.
