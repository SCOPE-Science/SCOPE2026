# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** LERF status of <a,b,c|u^4> with free <b,c>
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1726
- **Disposition:** AUDIT_1_REJECT
- **Domain:** geometric group theory
- **Method:** Magnus HNN hierarchy, cocompact cubulation, profinite separability

## Problem

Let u = a b^2 a^{-1} b^{-3} c in F(a,b,c), which is cyclically reduced, involves each of a,b,c, and is not a proper power, and let G4 = <a,b,c | u^4 = 1>, a three-generator one-relator group with torsion of order 4 whose Magnus subgroup <b,c> is free of rank 2. Is G4 subgroup separable (LERF), i.e. is every finitely generated subgroup H <= G4 closed in the profinite topology on G4? A complete answer proves either that every finitely generated H <= G4 is an intersection of finite-index subgroups of G4, or exhibits one explicit finitely generated H <= G4 and one explicit g in G4 in its profinite closure but not in H, with full proof of both facts.

## Attempted claim

Let u = a b^2 a^{-1} b^{-3} c in F(a,b,c), which is cyclically reduced, involves each of a,b,c, and is not a proper power, and let G4 = <a,b,c | u^4 = 1>, a three-generator one-relator group with torsion of order 4 whose Magnus subgroup <b,c> is free of rank 2. Is G4 subgroup separable (LERF), i.e. is every finitely generated subgroup H <= G4 closed in the profinite topology on G4? A complete answer proves either that every finitely generated H <= G4 is an intersection of finite-index subgroups of G4, or exhibits one explicit finitely generated H <= G4 and one explicit g in G4 in its profinite closure but not in H, with full proof of both facts.

## Research outcome

Proved G4 is LERF: u contains c once so G4 collapses by Tietze to F(a,b)*C4, a virtually free group, and finite extensions of LERF free groups are LERF.

## Why this attempt failed

Failed axes: value.

value: ADMISSION_DEFECT: admitted as high-risk counterexample_boundary needing Magnus HNN/cubulation, but u contains c once so G4 is a disguised F2*C4 by one visible Tietze move. LERF then follows mechanically from textbook Hall plus finite-extension lemma, as DRAFT itself states. The specific exponents 2,-3 are unexplained and arbitrary; no motivation shows why a future researcher would need this datum rather than the general virtually-free=>LERF principle. This is a textbook corollary for an arbitrary parameter fact, intrinsically low value and arbitrary scope, not a repairable motivation gap.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: The proof applies classical textbook theorems (Hall 1949 LERF for free groups, Kurosh subgroup theorem, Schreier finite-index finite generation) as cited facts rather than re-proving them; the Python artifact verifies only the combinatorial word identities, relator data, and commutator normal forms, while the LERF deduction itself is the human-readable mathematical proof in DRAFT.md.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
