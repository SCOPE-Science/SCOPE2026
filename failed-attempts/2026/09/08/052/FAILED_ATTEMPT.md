# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Maximal complete caps in AG(3,4) in the 9-14 point window: witness, gap, and replayable census
- **Round:** 2026-09-07-first-light-01
- **Lane:** 159
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Finite Geometry
- **Method:** backtracking cap search with collineation-group canonical pruning and incidence-matrix replay

## Problem

Exhaustively survey complete caps (no three collinear; every exterior point on a secant) in AG(3,4) for sizes 9-14 by collineation-pruned backtracking, certify the maximal complete cap in that window, and tabulate per-size completeness with independently replayable incidence logs.

## Attempted claim

There exists an explicitly listed point set C* in AG(3,4) with |C*|=M (M in 9-14) that is a complete cap, and every other complete cap C in AG(3,4) with |C| in 9-14 satisfies |C| <= M - g for a committed integer gap g >= 1, both certified by collineation-canonical pruning logs and incidence-matrix replay.

## Research outcome

Verified fragment for complete caps in AG(3,4): explicit machine-checked complete caps at sizes 8,10,12,13,14,16 with per-point cube secant cover, exact C12 puncture-incompleteness counts, and a logged 1M+ partial 9-cap search with zero complete examples; maximal-gap census left open.

## Why this attempt failed

Failed axes: value.

value: The admitted headline (explicit C* with |C*|=M in 9-14 and gap |C|<=M-g for all other complete caps, with canonical-pruning logs) is explicitly NOT claimed; DRAFT Sec.4-5 and research_report limitations disclaim maximality, gap, and absence at 9/11/15. The admitted fallback (verified per-size table for every size 9-14 with a witness or replayable absence certificate) is incomplete: witnesses cover 10,12,13,14 inside the window but 9 and 11 are missing (partial 1,057,473 nine-cap pilot with 0 complete, explicitly non-exhaustive) and 15 is open; 8 and 16 lie outside the window. What remains is scattered existence: four in-window examples plus one standard cube and one out-of-window 16, with no maximal size, no gap, no spectrum, no counts/classification, no canonical invariants (stabilizer, orbit, weight distribution) and no demonstrated MDS/quantum-code parameters or other mathematical interpretation — just coordinate lists (arbitrary representatives among large AGL orbits) plus the local fact that subcaps of this one 12-cap are incomplete (expected; subset-of-cap makes the cap counts 12/66/220 trivial). This is an honestly-described incomplete census fragment and unexplained enumeration, not an independently retrievable extremal invariant a future researcher needing maximal size or per-size completeness could use. Certification alone does not rescue arbitrary representatives per the standard. The narrow-datum exception does not apply: the motivated exact invariants were M, g and the full 9-14 spectrum, none of which is established; opportunistic examples at a subset of sizes with gaps are arbitrary scope and missing substantive result. No bounded motivation/interpretation addition without new exhaustive search could create the missing extremal/census result, so this is intrinsic low value, not repairable.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: No maximality, no integer gap g, and no absence proof at sizes 9/11/15: the 9-search is a 2M-node partial pilot, not exhaustive; annealing failures at 9/11/15 are heuristic only. Fallback per-size table for 9-14 is incomplete (missing 9 and 11). 8-cube is a standard F2^3 embedding with no novelty claimed; novelty claimed only for the explicit checked package plus replay pipeline. A missed prior AG(3,4) census source remains possible despite triage finding none.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
