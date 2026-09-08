# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Crosscap-number decision for the Conway/Kinoshita-Terasaka mutant pair via certified non-orientable spanning surfaces
- **Round:** 2026-09-07-first-light-01
- **Lane:** 250
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Low-Dimensional Topology
- **Method:** fundamental normal spanning-surface enumeration with orientability testing and Clark-inequality lower-bound certificate

## Problem

Decide the exact crosscap numbers of the Conway knot 11n34 and the Kinoshita-Terasaka knot 11n42 via fundamental normal spanning-surface enumeration with orientability and Euler-characteristic certification against Goeritz-matrix Clark/Murakami-Yasuhara lower bounds, testing whether crosscap number distinguishes this Jones-equal mutant pair.

## Attempted claim

The crosscap numbers of 11n34 and 11n42 are exactly determined by matching certificates (explicit non-orientable fundamental spanning surface plus Clark-inequality lower bound), deciding whether crosscap number separates the Conway/Kinoshita-Terasaka mutant pair.

## Research outcome

Partial-theorem fallback: machine-certified nonorientable state spanning surfaces (b1=5) for committed Conway/KT diagrams plus full state census, tightened by cited classical lemmas to C in {2,3} for both knots; separation left open with explicit next steps.

## Why this attempt failed

Failed axes: value.

value: Admitted headline required exact crosscap numbers deciding mutant separation, fallback required exact value for at least one mutant with explicit minimal non-orientable fundamental surface plus matching Clark/Murakami-Yasuhara Goeritz lower-bound certificate. Delivered is C(K11n34),C(K11n42) in {2,3} with no exact value and explicitly no separation. The {2,3} interval is mechanically implied by long-tabulated KnotAtlas data (u=1, hyperbolic) plus classical lemmas, requiring no in-run computation; the in-run computed bound C<=5 is strictly weaker than the cited C<=3. The remaining computed object — full b1 distribution identical for both mutants and minimal nonorientable-state b1=5 — is a diagram-dependent enumeration (depends on committed diagram, not a knot invariant), identical across the pair, with no invariant interpretation and no constraining power beyond the already-known C<=3. This is a textbook restatement plus unexplained enumeration, correct and new but not independently worth retrieving. Exact-invariant eligibility clause does not apply: no exact invariant was established, delivered numbers are mechanically implied or diagram-dependent, and future crosscap-tabulation cannot cite an undecided {2,3} interval or a diagram census as a crosscap value. Missing substantive result; closing to exact needs Goeritz bound or Regina normal-surface enumeration, a new research direction unavailable in-run, not a bounded value-add fix.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: ['Exact crosscap values (2 vs 3) not decided; no mutant separation.', 'C<=3 step uses external u=1 datum + cited Clark lemma, not recomputed in-run.', 'C>=2 uses external hyperbolicity + classical C=1 iff torus-knot characterization.', 'Bracket-Jones side computation parked (convention bug, unused).', 'No Regina/SnapPy normal-surface enumeration in this environment.']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
