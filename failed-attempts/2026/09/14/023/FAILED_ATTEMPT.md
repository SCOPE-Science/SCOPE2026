# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Quartic-slice census for D=178
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1870
- **Disposition:** AUDIT_1_REJECT
- **Domain:** number theory
- **Method:** difference-of-squares factor pairs

## Problem

Let D = 178 = 2 * 89, which is even and squarefree. Determine with proof all integer triples (x, y, n) with n >= 3, 4 dividing n, y > 1 and gcd(x, y) = 1 satisfying x^2 + 178 = y^n. A complete answer is an explicit finite list of all such triples up to the sign of x, together with a rigorous proof that no other integer triple with n >= 3, 4 | n, y > 1 and coprime x, y satisfies the equation.

## Attempted claim

Let D = 178 = 2 * 89, which is even and squarefree. Determine with proof all integer triples (x, y, n) with n >= 3, 4 dividing n, y > 1 and gcd(x, y) = 1 satisfying x^2 + 178 = y^n. A complete answer is an explicit finite list of all such triples up to the sign of x, together with a rigorous proof that no other integer triple with n >= 3, 4 | n, y > 1 and coprime x, y satisfies the equation.

## Research outcome

Proved the quartic-slice census for D=178 is empty: no coprime solutions with 4|n exist, via the mod-4 factor-pair obstruction.

## Why this attempt failed

Failed axes: originality, value.

originality: No fused source records D=178 literally, but the claim is mechanically implied by the classical difference-of-squares obstruction for any D=2 mod 4: no integer 2 mod 4 is a difference of two squares. D=178 is a mere parameter substitution into that broader theorem, which substantively implies and exhaustively covers the headline without any new idea; the draft itself notes generality. value: ADMISSION_DEFECT: result is a textbook parity exercise and arbitrary finite slice with no pre-existing motivation for D=178 beyond D=2 mod 4, no new method, boundary, or downstream use. The target's negative resolution merely exposes this cheap parity defect that Admission should have blocked under STANDARD; certification and brute force do not create independent retrieval value.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The proof establishes non-existence for all even exponents n >= 2 and hence the full target census; it does not address odd exponents n, other values of D, or the coprime-dropped odd-n cases, which lie outside the admitted target claim.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
