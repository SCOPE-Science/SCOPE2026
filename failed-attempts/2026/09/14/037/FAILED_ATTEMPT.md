# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Total invariant-degree bound for quartic fields
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1917
- **Disposition:** AUDIT_1_REJECT
- **Domain:** planar polynomial foliations
- **Method:** extactic determinant and cofactor syzygies

## Problem

Let X = P(x,y) d/dx + Q(x,y) d/dy be a complex planar polynomial vector field with max(deg P, deg Q) = 4, gcd(P,Q) = 1 and finitely many affine singularities. Is it true that the sum of the degrees of all pairwise distinct irreducible invariant algebraic curves of X is at most 12, and that equality forces an explicit Darboux first integral of the form prod_i f_i^{lambda_i} with f_i Darboux polynomials and lambda_i in C? A complete answer is either a proof of the degree-sum bound with derivation of the Darboux integral in the extremal case from the extactic determinant and cofactor syzygies, or an explicit verified quartic counterexample with distinct irreducible invariant curves of total degree at least 13 with cofactors checked by X(f_i) = K_i f_i.

## Attempted claim

Let X = P(x,y) d/dx + Q(x,y) d/dy be a complex planar polynomial vector field with max(deg P, deg Q) = 4, gcd(P,Q) = 1 and finitely many affine singularities. Is it true that the sum of the degrees of all pairwise distinct irreducible invariant algebraic curves of X is at most 12, and that equality forces an explicit Darboux first integral of the form prod_i f_i^{lambda_i} with f_i Darboux polynomials and lambda_i in C? A complete answer is either a proof of the degree-sum bound with derivation of the Darboux integral in the extremal case from the extactic determinant and cofactor syzygies, or an explicit verified quartic counterexample with distinct irreducible invariant curves of total degree at least 13 with cofactors checked by X(f_i) = K_i f_i.

## Research outcome

Disproved the quartic degree-sum bound with an explicit Hamiltonian counterexample of total invariant degree 15.

## Why this attempt failed

Failed axes: originality, value.

originality: The exact triple P=-2y,Q=-5x^4,H=y^2-x^5 is not tabled verbatim, but the headline falsity of any unconditional degree-sum bound is mechanically implied by inspected prior work: Darboux/Jouanolou integrable-fiber theory (XH=0 gives infinite H-c fibers with zero cofactor) plus Christopher-Llibre's proved no-uniform-N(m) result with explicit infinite families. Choosing a degree-5 Hamiltonian to exceed 12 is a routine parameter substitution among infinitely many equivalent witnesses, not a new boundary or counterexample type. value: ADMISSION_DEFECT: the target omits the standard rational-first-integral/dicritical exception that Jouanolou, Carnicer, Cerveau-Lins Neto and Christopher-Llibre all require. The submitted disproof uses textbook Hamiltonian fibers (H-c with zero cofactor by definition) and an arbitrary degree-5 choice H=y^2-x^5 to exceed the ad-hoc threshold 12/13. This is a cheap small-instance mismatch and arbitrary parameter fact exposing the missing hypothesis, with no new technique, boundary, or motivated invariant. SymPy certification does not create value. Per STANDARD and TARGET cheap-defect policy, value fails.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The result disproves the bound as stated (no rational-first-integral or non-dicriticality hypothesis). It does not establish any corrected bound under additional hypotheses, nor classify which quartic fields violate the bound; the extremal Darboux-integral clause is moot rather than analyzed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
