# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** A certified duality-plus-enumeration crossing-probability window for bond percolation on 6x6 to 10x10 tori
- **Round:** 2026-09-07-first-light-01
- **Lane:** 127
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Statistical Mechanics
- **Method:** planar-duality crossing analysis with transfer-matrix exact enumeration and dual-path obstruction logging

## Problem

Certify an explicit finite-size critical window for i.i.d. bond percolation on n x n tori (n=6..10) and associated r x n rectangles: find explicit p_low < 1/2 < p_high and explicit 0 < a < b < 1 such that the horizontal crossing probability satisfies P_{p_low}(cross) <= a and P_{p_high}(cross) >= b, proved via planar duality plus exact transfer-matrix enumeration logs and witnessed by a documented dual-blocking open/closed path family.

## Attempted claim

For bond percolation on the 8x8 torus (and 8xR rectangle family within 6x6-10x10 scope), with p_low=0.44 and p_high=0.56: P_{0.44}(horizontal open crossing) <= 0.35 and P_{0.56}(horizontal open crossing) >= 0.65, established by exact transfer-matrix crossing counts plus a logged dual-blocking witness configuration family and duality complementarity, replayable from committed edge lists.

## Research outcome

Proved four exact finite-size critical windows straddling p=1/2 (4x6, 5x6, 6x6, 6x7 rectangles at p_low=0.44/p_high=0.56) via exact transfer-matrix crossing-count polynomials with exact-rational probability evaluation, exhaustive duality-complementarity check, 8 logged dual-blocking witnesses, plus a 44-file exact crossing census (R=2..6 x C=6..10, H+V) — all replayed by an independent verifier.

## Why this attempt failed

Failed axes: value.

value: Correct and new but an unexplained enumeration with post-hoc windows, explicitly rejectable even if correct and new. p_c=1/2 for Z^2 bond is already exactly known (Kesten); finite-size inequalities P0.44<=a<P0.56>=b for monotone crossing events are guaranteed to exist for some a<b and the quoted a,b (1/4,11/20,1/3,2/3,2/5,3/4,3/10,7/10) are just nice roundings of computed values at arbitrarily chosen p=0.44/0.56, with no theoretical consequence (no threshold localization, no RSW-constant improvement, no Cardy-formula comparison performed despite 'benchmarking' claim). Census R=2..6 x C=6..10 at p in {0.40,0.45,0.50,0.55,0.60,0.44,0.56} is an arbitrary computational frontier (6x8..6x10 missing) with no interpretation; dual-blocking 'family' is 8 trivial configs (empty + single vertical cut missing one column of horizontals), and duality XOR is shown only on 3x4, contributing no insight to the windows. Reusable tm.py pipeline is plumbing; certification alone does not create value. Notably the data contain a potentially genuine pattern (R x (R+1)-H has P1/2=1/2 exactly: verified 2x3,3x4,4x5,5x6,6x7) that could have been a theorem, but DRAFT notes two instances en passant as '(exact symmetry)' with no statement, conjecture, or proof — leaving only raw numbers. No downstream user would independently need to find these specific rectangle/p/threshold triples later.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Certified object is free-boundary rectangles, not the nominal 8x8 torus (2^128 exhaustive enumeration and torus transfer matrix infeasible in budget); 6x8-6x10 rectangles not enumerated (width-6 state explosion; 6x7-V took ~44s, 6x6-H ~128s, so wider cases exceeded remaining budget). No asymptotic RSW/Cardy claim; finite-size certificates only. Originality rests on the admission arXiv scan (no covering finite-size exact crossing table found), not on a fresh literature search in this pass.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
