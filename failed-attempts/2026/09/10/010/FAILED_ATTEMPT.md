# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Burden two for the ordered-group sparse expansion (Q,<,+,powers-of-2) via successive differences
- **Round:** 2026-09-07-first-light-01
- **Lane:** 514
- **Disposition:** NO_RESULT
- **Domain:** Model Theory
- **Method:** successive-difference burden analysis with published dp-rank subadditivity and L-legal indiscernible-sequence pattern combinatorics

## Problem

Let L={<,+,P} and T=Th(Q,<,+,P) with P={2^n:n in N}. Prove burden/dp-rank(T)=2: exhibit an explicit L-legal depth-2 ICT pattern, and exclude depth 3 via one Dolich-Goodrick successive-difference (D-to-D') computation plus published dp-rank subadditivity, separating T from the Simon-Walsberg dp-minimal dense-pair classification of (Q,+,<) expansions.

## Attempted claim

T=Th(Q,<,+,P) with P={2^n:n in N} in L={<,+,P} is strong NIP of burden and dp-rank exactly 2: (i) phi1(x;y1):=(y1<x) and phi2(x;y2):=P(x-y2) witness an explicit L-legal ICT-pattern of depth 2, and (ii) one Dolich-Goodrick D-to-D' iterate on P plus published dp-rank subadditivity excludes ICT-patterns of depth 3, placing T strictly above the Simon-Walsberg dp-minimal dense-pair classification.

## Research outcome

No auditable claim completed. Target burden/dp-rank=2 fails on both clauses: (i) the literal pair (phi1:=(y1<x), phi2:=P(x-y2)) cannot form a depth-2 ICT pattern — proved UNSAT over all order types (Gamma_{k,l} branches jointly force a_k<a_{k'} and a_{k'}<a_k); hence the exact qualified preset fallback with the same phi1/phi2 is likewise provably unsatisfiable, not merely unbuilt. (ii) The Dolich-Goodrick D-to-D' route is doubly blocked: Q lacks definable completeness and the computed iterate D'=P (gamma(2^n)=2^n) points the wrong way (conditional infinite burden). Incidental lemmas are textbook/trivial and not claimed. All 9 artifact scripts replay green.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['Literal target clause (i) with phi1:=(y1<x) is false as written: proved unsatisfiable over all weak order types (pairwise and triple exhaustions), in any linear order, hence in any model of T.', 'Exact qualified preset fallback is proved unsatisfiable for the same reason (27/27 types infeasible on 3-branch core; pairwise argument covers length 6); monster-model escape impossible as proof uses only order axioms.', 'Target clause (ii) doubly blocked: (Q,<,+) is not definably complete so Dolich-Goodrick hypotheses do not apply verbatim, and conditional on DG applying, D^{(k)}=P infinite for all k forces infinite burden, opposite of burden<=2.', 'No alternative formulas attempted: scope forbids inventing an easier substitute; dp-rank/NIP of (Q,<,+,{2^n}) via other formulas remains open.', "Emergent observations (cut-row impossibility, D'=P fixed point) are correct but do not meet SCOPE originality/value bar for standalone claims (textbook VC-dimension corollary and elementary arithmetic) and are logged as obstructions only."]

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['Literal target clause (i) with phi1:=(y1<x) is false as written: proved unsatisfiable over all weak order types (pairwise and triple exhaustions), in any linear order, hence in any model of T.', 'Exact qualified preset fallback is proved unsatisfiable for the same reason (27/27 types infeasible on 3-branch core; pairwise argument covers length 6); monster-model escape impossible as proof uses only order axioms.', 'Target clause (ii) doubly blocked: (Q,<,+) is not definably complete so Dolich-…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
