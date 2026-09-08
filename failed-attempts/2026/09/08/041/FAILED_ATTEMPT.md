# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Ingleton-violation propagation from a tic-tac-toe 9-point relaxation: an infinite minor-minimal linear-vs-algebraic separation family
- **Round:** 2026-09-07-first-light-01
- **Lane:** 134
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Matroid Theory
- **Method:** Ingleton rank-inequality evaluation plus algebraic function-field representation and free-extension induction

## Problem

Starting from the rank-4 9-point tic-tac-toe sparse-paving matroid, isolate a named relaxation T* and prove a linear-vs-algebraic separation that propagates: T* violates Ingleton's inequality (hence is not linearly representable over any field) yet is algebraic over an explicit characteristic, and every free single-point extension on a committed line preserves the violation, yielding an infinite family of pairwise non-isomorphic minor-minimal non-linear matroids.

## Attempted claim

Exhibit an explicit rank-4 9-element relaxation T* of the tic-tac-toe sparse-paving matroid, given by its committed nonbases/hyperplanes, such that: (a) T* violates Ingleton's inequality on a committed ordered 4-tuple of subsets with explicit subset ranks giving deficit d >= 1, hence T* is not linearly representable over any field; (b) T* is algebraic over an explicitly named characteristic (with explicit transcendental/polynomial assignment whose independent sets match T*), or explicitly folded-linear if algebraic fails at the stated level, so T* separates linear from the named stronger notion; (c) PROPAGATION LEMMA: for the committed line L of T*, the free single-point extension T*(+e on L) preserves an Ingleton violation with deficit >= d, so iterating gives an infinite pairwise non-isomorphic family {T*_k} of non-linearly representable matroids, each carrying the inherited minor-minimal violation.

## Research outcome

Exact machine-checked Ingleton-deficit atlas correcting the admission expectation (TTT 9-pt family has deficit 0, so no violation to propagate) plus an exact maximum-deficit-1 bound over the 16-member Vamos-specimen relaxation poset with explicit witness; infinite lift and algebraic separation left as conjectures with obstruction identified.

## Why this attempt failed

Failed axes: originality, value.

originality: No substantive delta. V deficit 1 is textbook (original Ingleton-violating example; Bamiloshin Sec1/4 presupposes it, same nonbasis list). TTT zeros were recorded/implied: Sec5 states T3 satisfies Ingleton (fails GE, not Ingleton); dual fails Ingleton-Main extension, not the inequality. P8 zeros implied by Sec1/4 census: exactly 39 eight-element violators, all AG(3,2) relaxations with V configuration. The V-poset max-1 phrasing is new verbatim but is a mechanical corollary (known violator + 15 small zero scans), no lemma, representation, or propagation. Admitted TTT D*>=1 fallback is refuted by the draft itself; substituted V poset is a different object. Timestamp/replay log confers no priority. value: Not independently worth finding. Residual after honest retraction: 6 TTT zeros (expected), 5 P8 zeros (implied by 39-violator census), 1 textbook V=1 plus 15 relaxation zeros. Target payoff (propagation lemma to infinite minor-minimal family + algebraic-yet-nonlinear separation) is absent per DRAFT Sec5: no seed, no assignment, no family. No new boundary, method, or artifact: no Kinser/Mayhew/Zhang-Yeung tests, no isomorphism classification, no solver hard-instance use. Corrects only the admission's own mistaken expectation, already contradicted by literature. Textbook restatement plus routine verification packaged as atlas.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Target infinite-propagation lemma and algebraic representation NOT achieved; TTT 9-pt objects satisfy Ingleton so the literal D*>=1 TTT-poset fallback is false and the claim is an honest corrected pivot. No other inequalities (Kinser/Mayhew/Zhang-Yeung) tested; no isomorphism classification; code validated via known Vamos deficit-1 reproduction only.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
