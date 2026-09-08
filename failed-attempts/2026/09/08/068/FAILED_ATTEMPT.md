# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** First length-7 y-arithmetic-progression witness on a Mordell curve
- **Round:** 2026-09-07-first-light-01
- **Lane:** 206
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Arithmetic Geometry
- **Method:** AP-constrained polynomial-system solving seeded from length-6 families with height-bounded rational-point search and exact verification

## Problem

Produce the first explicit Mordell curve E_k: y^2 = x^3 + k with k nonzero sixth-power-free carrying seven distinct rational points P_i=(x_i,y_i) whose y-coordinates y_1,...,y_7 form a non-trivial arithmetic progression (common difference d != 0): publish the integers (k; x_i, y_i, d), verify each point satisfies the equation by exact arithmetic, and certify minimality (least naive height) among length-7 examples inside the stated search envelope with a replayable search log.

## Attempted claim

First explicit sixth-power-free k and seven distinct rational points on E_k: y^2 = x^3 + k whose y-coordinates form a 7-term arithmetic progression with d != 0, each point verified by exact integer arithmetic, with a replayable log certifying minimal naive height among length-7 examples in the stated envelope.

## Research outcome

Fallback partial theorem secured: certified minimal integer-point length-6 y-AP record k=197225 with machine-checked rank>=2 and exhaustive no-integer-length-7 certificate in |x|<=2000,|k|<=2e6. Length-7 rational existence remains open.

## Why this attempt failed

Failed axes: value.

value: Strongest headline is the fallback: minimal integer-coordinate length-6 y-AP record k*=197225 with rank>=2 plus no-integer-7 cutoff in box B={|x|<=2000,|k|<=2e6}. It is correct and (as a certificate) new, but not independently worth retrieving. (i) Arbitrary scope: bounds 2000/2e6 have no pre-computation motivation in DRAFT and no mathematical interpretation; envelope-relative 'minimality' follows tautologically from uniqueness in that box and implies no global minimality (a smaller-max|y| integer AP outside the box is not ruled out). (ii) Wrong coordinate restriction for the motivated question: the recognized open boundary is rational length-7 (July 2026 paper), and DRAFT honestly concedes rational status is unchanged and non-integral rational points are outside the certificate; an integer-only no-7 bound does not advance AP-vs-rank or uniform-boundedness uses, which need rational facts. (iii) Mere parameter substitution: k* is the least-q integer member of the known P0 family of Thm 2.4 (verified q=64/3 is the smallest positive rational giving integer d,r), so the tuple is mechanically implied by published parametrization; certification (rank>=2 lower bound only, no exact rank/regulator; box enumeration) does not rescue the arbitrary object per standard. No future researcher reasonably needs the precise fact 'no integer 7-term y-AP with |x|<=2000,|k|<=2e6' or the box-minimal P0 instance for a downstream theorem, textbook, or census. This is intrinsic low value / arbitrary scope / unexplained enumeration, not a narrow-but-natural exact invariant.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: No length-7 witness; rational non-integral y-APs outside the integer envelope certificate; minimality/uniqueness is envelope-relative, not over Q; rank is a lower bound (>=2), not exact rank; length-6 infinite families are prior art, novelty is the minimal integer record + rank witness + envelope cutoff.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
