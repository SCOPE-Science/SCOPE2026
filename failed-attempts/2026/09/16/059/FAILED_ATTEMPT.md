# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Hyperfinite A-infinity subfactor at the ~5.04892 quantum-group index?
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20514
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Operator Algebras
- **Method:** Jones-tower and bimodule-fusion analysis

## Problem

Does there exist an irreducible hyperfinite subfactor N \subset M of the hyperfinite II_1 factor with Jones index \lambda_0 \approx 5.04892, the largest root of x^3-6x^2+5x-1, whose standard invariant is Temperley-Lieb-Jones (both principal graphs A_\infty, i.e. infinite depth with trivial standard invariant)?

## Attempted claim

Does there exist an irreducible hyperfinite subfactor N \subset M of the hyperfinite II_1 factor with Jones index \lambda_0 \approx 5.04892, the largest root of x^3-6x^2+5x-1, whose standard invariant is Temperley-Lieb-Jones (both principal graphs A_\infty, i.e. infinite depth with trivial standard invariant)?

## Research outcome

TARGET resolved negatively: proved no irreducible hyperfinite subfactor has index ~5.04892 with A_infinity standard invariant, via exact root enclosure plus Popa amenability forcing index 4.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET disproof fails at load-bearing Lemma 3. Lemma 1 (lambda0 in (5,6)) and Lemma 2 (||A_inf||=2) check out and the script ran clean, but Lemma 3(i) 'M hyperfinite => amenable subfactor' is false. Amenable extremal => index=||Gamma||^2 is conditional on amenability; hyperfiniteness of the ambient does not imply amenability. Positive counterexamples: Bisch 1994 irreducible R-subfactor at index 9/2 with A_infinity graphs that is Popa-non-amenable, and Bisch-Caceres 2025 full text constructing hyperfinite TLJ (hence A_inf) subfactors at index 5 and other indices !=4. Hence hyperfinite A_inf does not force index 4, and the contradiction collapses. Headline truth is undecided by this proof.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: The proof applies Popa's amenability theorem and the classical A_n norm formula of Goodman-de la Harpe-Jones as cited standard black boxes rather than re-deriving them; it rules out only the hyperfinite realization and says nothing against abstract TLJ(delta_0) existence or non-hyperfinite realizations at this index.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
