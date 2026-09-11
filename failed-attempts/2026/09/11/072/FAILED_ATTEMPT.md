# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Decidable conjugacy with uniform radius for rank-two S-adic minimal subshifts
- **Round:** 2026-09-07-first-light-01
- **Lane:** 862
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Descriptive Set Theory
- **Method:** Hjorth turbulence with Baire-category generic coding and clopen-partition invariants

## Problem

Is topological conjugacy decidable for primitive recognizable S-adic minimal subshifts of alphabet rank 2, with a computable uniform bound on the block-code radius?

## Attempted claim

For primitive recognizable S-adic minimal subshifts of alphabet rank 2 with bounded recognizability index, there is a computable R (explicit function of alphabet size and recognizability index) such that any topological conjugacy between two such subshifts is, up to a shift power, a sliding block code of radius <R; hence conjugacy (and factor existence) is decidable on this class by finite enumeration over a computable window.

## Research outcome

Uniform conjugacy radius R(I0) and finite-window decision procedure for primitive recognizable binary-alphabet rank-2 S-adic minimal subshifts, with replayable census: self-maps of Fibonacci are exactly shifts; Fibonacci vs alternating-directive system certified non-conjugate.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET route, judged against admitted target claim. Headline (uniform R(I0)=2*I0+C0 + decidability by finite enumeration + exact window test) is not established; DRAFT Lemmas 1-3 are research sketches with essential gaps. Lemma 1 contraction (r+I0)/m+I0: +I0 cannot absorb block-boundary error without uniform max-length or length-ratio bound; only min-length m>=2 assumed, max length unbounded, telescoping to raise m also raises max length; absolute C0<=4 unproved. Lemma 2 pigeonhole over binary codes 2^(2^(2R+1)) fails across levels: renormalized maps live between varying pairs (Xn,Yn) with arbitrary intervening products, so coincidence does not force a shift as in Durand-Leroy Sec 5.3 for one substitution. Lemma 3 window W=4I0+2/O(I0+L): stabilization data L, O(I0) return bound, and exact desubstitution membership from c.e. directives asserted without proof; semi-decidable vs decidable gap unaddressed. Class C(2,I0) conflates primitivity positivity with length growth and assumes properness telescoping preserves binarity and uniform index. Evidence: census exhausts only radius<=1 (260 codes) while demo R=12; X=Fibonacci is constant-directive rank-1, not rank-2 unbounded witness; X-vs-Y non-conjugacy already follows from length-3 languages; window_test uses finite prefixes (~10k, W=26) never proved equal to true languages. Hence mechanics demo only, not proof.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: Proof is a research-level lift of the Durand-Leroy architecture (sketch level per lemma, not a formalized article); uniformity is over bounded index I0 and binary alphabets only; directives must be computably presented; demo census is exhaustive only at radius<=1, full radius-<R enumeration is doubly exponential and not run.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
