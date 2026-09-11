# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Self-orthogonal-member exclusion decision for 3-MOLS(10)
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1029
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Combinatorial Design Theory
- **Method:** SAT-encoded OA(5,10) search with transpose-orthogonality clauses and isotopism canonicalization

## Problem

Decide whether any triple of mutually orthogonal Latin squares of order 10 contains a member that is orthogonal to its own transpose with constant diagonal symbols. Either exhibit such a triple with the self-orthogonal member in isotopism-canonical form plus replay verification, or produce a proof-logged SAT unsatisfiability certificate excluding the subtype with a checkable counting replay.

## Attempted claim

No triple of mutually orthogonal Latin squares of order 10, equivalently no OA(5,10), contains a member Latin square that is orthogonal to its own transpose when normalized to constant diagonal symbols.

## Research outcome

Closed-form TARGET exclusion: constant-diagonal self-orthogonal squares are impossible at every order n>=2 by diagonal-pair repetition, so no 3-MOLS(10) contains one; replay-verified (VERIFY_OK). This also corrects the admission nonvacuity premise.

## Why this attempt failed

Failed axes: originality, value.

originality: FAIL because the headline is a one-step mechanical consequence of the standard textbook definition of orthogonality/self-orthogonality, i.e. a textbook exercise, not a new theorem, boundary or classification. Fused retrieval confirms the standard definition everywhere (Cao-Li 2011, Cook, Budshaw, Bright reports): SOLS means n^2 pairs (L[i][j],L[j][i]) pairwise distinct. Constant diagonal immediately repeats (c,c) n times. No prior paper states this verbatim precisely because it is too trivial to publish, but under the shared STANDARD a prior source need not state the headline verbatim: if its result substantively implies it, originality FAILS. A failed verbatim-title search therefore does not establish priority. Triple/OA(5,10) context adds nothing; the claim collapses to single-square definitional vacuity. value: FAIL as vacuity / type-normalization error with ADMISSION_DEFECT. Topic audit_preflight cheap-falsification checks explicitly claimed as PASS that constant-diagonal transpose-orthogonality is realizable at single-square level for order 10 and that diagonal pinning is a non-degenerate isotopism normalization, so the constrained model is nonempty before triple orthogonality. That premise is false at every n>=2 by the one-line theorem itself, as DRAFT Sec. Correction admits. Per TARGET route policy, when the negative/exclusion resolution is only vacuity, normalization error, cheap small-instance mismatch or arbitrary parameter fact, value fails even if literally true. The DRAFT also concedes it decides nothing about the scientifically interesting neighbours (transversal-diagonal self-orthogonal member, general 3-MOLS(10) existence, symbol-permuted transpose variants). No future researcher needs to retrieve the fact that (c,c) repeated n times violates distinctness; there is no downstream construction use beyond pruning a subtype that never existed definitionally. ADMISSION_DEFECT: admission triviality_preflight and target_integrity PASS verdicts were materially false.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The proof decides exactly the posed constant-diagonal subtype and nothing beyond it: it does not decide 3-MOLS(10) containing a self-orthogonal member with transversal (all-distinct) diagonal, general 3-MOLS(10) existence, or isotopic variants such as orthogonality to a symbol-permuted transpose. Exhaustive computational enumeration covers orders 2-4 only; the order-10 conclusion rests on the general counting theorem, and cited background (e.g. SOLS existence for n != 2,3,6) is referenced, not…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
