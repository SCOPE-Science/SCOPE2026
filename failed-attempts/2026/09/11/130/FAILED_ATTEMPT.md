# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Quasirandom single-step book density increment with logarithmic gain
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1024
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Ramsey Theory
- **Method:** book-algorithm induction with quasirandom counting

## Problem

Can one certified book-algorithm step be made quantitative on a restricted quasirandom host class? Fix n at least 2^20, base density d equals 1/2, and discrepancy epsilon equals 10^{-4}. Decide whether every epsilon-quasirandom n-vertex graph of density d either contains a book B_2(m) with at least n over 200 ln n pages or contains an 8th-fraction subset whose induced density rises by at least 1 over 50 ln n.

## Attempted claim

Let n be at least 2^20, d equals 1/2, epsilon equals 10^{-4}. Let G be an n-vertex epsilon-quasirandom graph of density d plus or minus epsilon with codegree discrepancy at most epsilon n for all but at most epsilon n squared pairs. Then either G contains a book B_2(m) with m at least n over 200 ln n pages on some spine edge, or there exists S subset of V(G) with |S| at least n over 8 and e(G[S]) at least (d plus 1 over 50 ln n) times C(|S|,2). A proof and an explicit verified violator both count as complete resolution.

## Research outcome

Proved the quasirandom single-step book dichotomy: under the stated density and codegree-discrepancy hypothesis a good spine edge always exists with ~0.2499n pages, far above n/(200 ln n), verified by replayable stdlib ledger plus Paley nonvacuity witness.

## Why this attempt failed

Failed axes: value.

value: FAIL: correct and literally new but intrinsically low value as a textbook weakening with arbitrary scope. The proof shows the first disjunct always holds with ~693x slack (0.2499n vs n/(200 ln n)~378), using only pigeonhole edge-minus-bad-pairs plus threshold comparison; no second-moment count, no neighbourhood-averaging density extraction, and the second (density-gain) arm is never used. Constants 200/50, eps=1e-4, n>=2^20 are unmotivated slices far from sharp (DRAFT Sec.5 admits 700x looseness and disclaims any R(4,t) statement, weaker-hypothesis result, or constant improvement). The headline is thus a mere parameter-weakened corollary of the definitional codegree bound, i.e. a textbook exercise, not a reusable induction lemma. ADMISSION_DEFECT: Admission preflight/qualification anticipated a fresh second-moment plus averaging ledger yielding an explicit log-power R(4,t) saving and cited random graphs as hypothesis witnesses; the submitted proof needs neither arm, yields no saving, and random G(n,1/2) violates H2 at n=2^20. No bounded addition can supply sharpness, a live second arm, or downstream use without changing the problem, so not repairable.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Constants 200 and 50 are far from sharp: the proof yields book 0.2499n, about 700x the page threshold at n=2^20, and never uses the density-gain arm. The result assumes the full stated discrepancy hypothesis (codegree bound for all but eps*n^2 pairs); it gives no statement under weaker quasirandomness, no improvement toward R(4,t) itself, and raw G(n,1/2) at n=2^20 does not satisfy the hypothesis since fluctuations ~sqrt(n) exceed eps*n.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
