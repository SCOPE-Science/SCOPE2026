# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Skein completion destroys full dualizability for 2Rep(Z-2)
- **Round:** 2026-09-07-first-light-01
- **Lane:** 956
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Higher Category Theory
- **Method:** dualizability obstruction via adjunction and cusp diagrams

## Problem

Let C=2Rep(Z/2) and let SkFr(C) be its framed skein completion. Decide whether SkFr(C), equivalently its distinguished generating object in the Morita 4-category, is fully dualizable, with failure witnessed by a named 1-morphism lacking a right adjoint.

## Attempted claim

The framed skein completion SkFr(2Rep(Z/2)) is not fully dualizable: a named generating 1-morphism induced by the regular module strand has no right adjoint in the completion, so the cusp zigzag identity fails and the object cannot define a framed 4d local TFT via the cobordism hypothesis.

## Research outcome

Proved SkFr(2Rep(Z/2)) is not fully dualizable via an explicit infinite regular-strand witness S with no right adjoint, certified by a no-dual theorem plus VERIFY_OK finite check.

## Why this attempt failed

Failed axes: originality, value.

originality: FAIL. The headline is substantively implied by textbook stronger facts, so ADMISSION_DEFECT in admission broader_coverage and equivalent_formulations preflights which only surveyed fusion-2-category theorems. nLab dualizable object and Wikipedia Dual object state Vect dualizable iff finite-dimensional; Brochier-Jordan-Snyder 1804.07538 explicitly states in the infinite setting infinite-dimensional vector spaces are not dualizable and studies locally presentable tensor categories; Gunningham-Jordan-Safronov notes arbitrary ribbon category is not 4-dualizable. Forgetful symmetric monoidal functor Rep(Z/2)->Vect preserves duals, sending S=oplus_N R to infinite-dimensional vector space, so non-dualizability of S follows in one line. DRAFT reproves this special case via the same unit-compactness argument used for the textbook criterion. No prior source need state SkFr(2Rep(Z/2)) verbatim: the stronger Vect criterion exhaustively covers it as corollary/repackaging. Timestamp and failed admission search do not establish priority. value: FAIL. ADMISSION_DEFECT in triviality_preflight/value: the result is a textbook restatement in higher-categorical language plus routine colimit artifact, not an independently retrievable invariant. Dualizable=finite is standard intuition (nLab: size vs additivity); infinite direct sums never preserve duals by unit-compactness. Witness S=countable sum of R is arbitrary (any infinite sum, any group, countable vs other infinite would do; Z/2 and R not motivated as natural skein invariant like torus skein algebra), and TFT no-go follows mechanically from cobordism hypothesis once non-dual is known. Admission risk that missing adjoint is routine colimit artifact was not mitigated by level-sharpness (compact R self-dual vs infinite S non-dual is exactly finite vs infinite Vect phenomenon, not new 3-level obstruction). Certification VERIFY_OK strengthens evidence but per STANDARD does not create value. No future researcher needs this precise countable-sum fact beyond the general theorem.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Definition-dependent: framed skein completion is taken as free filtered (skein/factorization-homology cocompletion) so End = Ind(Rep(Z/2)); under a Karoubi-only reading the infinite witness would be absent. Result is specific to 2Rep(Z/2) in characteristic zero; no classification of other completed 1-morphisms is claimed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
