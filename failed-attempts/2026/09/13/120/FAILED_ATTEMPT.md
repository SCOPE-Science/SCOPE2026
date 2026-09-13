# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Unitary conjugacy versus =+
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1757
- **Disposition:** AUDIT_1_REJECT
- **Domain:** descriptive set theory and operator algebras
- **Method:** spectral-multiplicity versus countable-set coding, pinnedness and generic ergodicity

## Problem

Let H be a separable infinite-dimensional complex Hilbert space, U(H) with the strong operator topology, C_unit unitary conjugacy defined by U C_unit V iff V = WUW* for some W in U(H), and let =^+ be equality of countable sets of reals on R^N defined by (x_n) =^+ (y_n) iff {x_n: n in N} = {y_n: n in N} as sets. Both C_unit and =^+ are known not to be Borel reducible to any CLI Polish group orbit. Determine whether C_unit is Borel reducible to =^+. A complete answer is either an explicit Borel map f: U(H) -> R^N with U C_unit V iff f(U) =^+ f(V), or a rigorous proof that no such Borel reduction exists, e.g. via spectral-multiplicity invariants, pinnedness, turbulence, or Baire-category generic ergodicity.

## Attempted claim

Let H be a separable infinite-dimensional complex Hilbert space, U(H) with the strong operator topology, C_unit unitary conjugacy defined by U C_unit V iff V = WUW* for some W in U(H), and let =^+ be equality of countable sets of reals on R^N defined by (x_n) =^+ (y_n) iff {x_n: n in N} = {y_n: n in N} as sets. Both C_unit and =^+ are known not to be Borel reducible to any CLI Polish group orbit. Determine whether C_unit is Borel reducible to =^+. A complete answer is either an explicit Borel map f: U(H) -> R^N with U C_unit V iff f(U) =^+ f(V), or a rigorous proof that no such Borel reduction exists, e.g. via spectral-multiplicity invariants, pinnedness, turbulence, or Baire-category generic ergodicity.

## Research outcome

Proved unitary conjugacy on U(H) is not Borel reducible to =+ by reducing turbulent E2 into it and applying Hjorth generic ergodicity.

## Why this attempt failed

Failed axes: originality.

originality: Full-text inspection shows Kechris-Sofronidis 2001 proves a strictly stronger theorem for the same object: generic S_infty-ergodicity/generic turbulence of unitary conjugacy on U(H), explicitly including countable-subset (=+-type) invariants. Since =+ is classifiable by countable structures, C_unit-not<= =+ follows mechanically. The submission is therefore a weaker corollary/reproof of a known stronger fact, so originality FAILS under the substantive-implication rule.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; address the recorded limitation: The proof relies as black boxes on three classical theorems: Kakutani's product-measure equivalence criterion, the Kuratowski Borel isomorphism theorem, and Hjorth's theorem that turbulent Polish group actions are generically =+-ergodic. The turbulence verification and all coding/invariance steps are proved self-contained in DRAFT.md, but the Hjorth generic-ergodicity implication itself is cited rather than re-proved.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
