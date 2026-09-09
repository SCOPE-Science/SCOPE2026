# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** A replayable Groebner-certified genus-6 canonical Betti cell separating generic and trigonal Clifford strata
- **Round:** 2026-09-07-first-light-01
- **Lane:** 373
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Commutative Algebra
- **Method:** exact Groebner-basis Schreyer syzygy computation with upper-semicontinuity certification and rational-scroll replay

## Problem

Certify, by exact Groebner-basis Schreyer computation over Q plus semicontinuity and rational-scroll replay, a Betti-table fragment of a genus-6 canonical curve that separates the generic (Clifford index 2) stratum from the trigonal (Clifford index 1) stratum: vanishing of the Green-predicted linear syzygy entry on an explicit candidate-generic ideal, and a nonzero extremal syzygy witness on an explicit scroll-contained trigonal ideal.

## Attempted claim

For an explicitly committed candidate-generic genus-6 canonical ideal I_C over Q in P^5, the Green-predicted linear-strand vanishing holds (generic-type Betti entry zero, certified by Schreyer resolution with rank-logged differentials and upper-semicontinuity transfer), while an explicitly committed trigonal genus-6 ideal I_D contained in a named rational normal scroll exhibits a verified nonzero extremal syzygy cycle, jointly certifying the Cliff-1 vs Cliff-2 Betti separation at genus 6.

## Research outcome

Certified fallback (b): a smooth trigonal genus-6 canonical curve over F_101 in the explicit scroll S(2,2) with identical 6-quadric kernel and 8 verified rank-8 Eagon-Northcott linear syzygies; stdlib-only replay prints VERIFY_OK.

## Why this attempt failed

Failed axes: originality, value.

originality: Substantive comparison defeats novelty. The mathematics is classical: 2x4 determinantal scroll S(2,2) with 6 quadrics and 8 Eagon-Northcott linear syzygies is textbook (Eisenbud; von Bothmer scrollar syzygies genus 6-8); quadric/cubic kernel dims 6 and 31 follow for ANY smooth (3,4) curve by Riemann-Roch (21-15=6, 56-25=31) without computation; smooth trigonal (3,4) existence is Bertini-general. Closest computational precedent Bopp-Schreyer arXiv:1803.10481 already constructs random canonically embedded curves genus<=15 over small finite fields via Macaulay2 to study Green, same object family and field setting. Kemeny arXiv:1907.07553 (even-genus geometric syzygies) and Voisin/Kemeny Green theorems plus von Bothmer classification already imply the trigonal extra-syzygy phenomenon. The 8 verified identities involve only scroll quadrics and are independent of the curve coefficients; the only curve-specific computation is smoothness of one random matrix (seed 606 over F101), an arbitrary parameter choice. Absence of this exact JSON matrix in the literature does not establish priority; it is a parameter substitution within a known construction, not a new object, theorem, counterexample, or boundary property. value: Headline is a single random smooth bidegree-(3,4) curve over F101 realizing the expected trigonal Betti fragment. The invariant values were known/mechanically implied: h0 kernels and EN rank-8 follow from general scroll + Riemann-Roch theory for any such curve, not discovered by computation; smoothness of a random (3,4) example is expected and the specific seed-606 coefficients are arbitrary with no mathematical interpretation distinguishing them. No future researcher reasonably needs this precise matrix: Bopp-Schreyer already supplies a package generating such curves, and any smooth (3,4) instance gives the same benchmark. The DRAFT has interpretation (Clifford-1 vs generic) but does not certify the generic side, so no separation is delivered, and the extra syzygies are scroll-general, not a new datum. This is textbook instantiation plus certification of an arbitrary object, explicitly excluded by the value standard ('certification alone does not rescue an arbitrary object'; reject textbook restatements, parameter substitutions, unexplained enumerations). It does not meet the narrow-datum eligibility clause because the value was already known/implied and the precise fact is not reusable.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Fallback (b) only: no generic-side Green vanishing cell, so the full Cliff-2 vs Cliff-1 separation is not certified. Certificate is over F_101, not Q; Q-lift of smoothness is a remark, not certified. Minimality of the syzygy classes uses the graded-minimal linear-coefficient argument, not a separately computed minimal-resolution differential.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
