# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Falsifiable interface revealment ledger for Voronoi square crossing window
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1046
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Statistical Mechanics
- **Method:** randomized-algorithm revealment with OSSS inequality and Russo-Margulis differential inequality

## Problem

Fix Poisson-Voronoi percolation of intensity 1 on the square [0,n]^2 with cells colored red independently with probability p, and let H_n be red left-right crossing. Does the vertically-started interface exploration algorithm achieve max-cell revealment at most 0.20 n^{-1/4} uniformly for p in [0.25,0.75] and all n>=16, yielding a 1/4-to-3/4 threshold window of width at most 0.70 n^{-1/4} via OSSS plus Russo-Margulis?

## Attempted claim

For intensity-1 Poisson-Voronoi red coloring on [0,n]^2 with n>=16, the named vertical-interface exploration determining red left-right crossing H_n satisfies sup_{p in [0.25,0.75]} max_{cells i} P[algorithm queries i] <= 0.20 n^{-1/4}, and consequently the p-interval on which P_p[H_n] rises from 1/4 to 3/4 has width at most 0.70 n^{-1/4}. At n=16 the bounds evaluate to 0.10 against cap 1 and 0.35 against maximum width 0.5, hence both constrain query probabilities at every scale n>=16.

## Research outcome

Exact finite-scale stall lemma for the canonical left-edge interface exploration at n=16: P[query (8,0)] >= 765/4096 ~= 0.1868 > 1/10 proved, plus a coded stall ledger; target revealment half blocked.

## Why this attempt failed

Failed axes: value.

value: EMERGENT_FINDING genuinely arose from target work (Monte-Carlo stall then exact certificate) but fails the ordinary STANDARD value test. Object is arbitrary, not pre-motivated: a researcher-invented full-component flood-fill on a 16x16 i.i.d.-bit proxy, admittedly not the continuum Voronoi model and not every conceivable billed exploration. Invariant 765/4096 is an elementary monochrome-segment geometric sum, i.e. a textbook exercise / arbitrary finite-slice computation. It lower-bounds only this deliberately wasteful algorithm and says nothing about optimal revealment or the threshold window; a smarter interface-following exploration evades it by construction. No future Voronoi researcher needs this precise constant, and exact Fraction certification alone does not create value. Falls under textbook exercise, arbitrary slice, unexplained number.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Proved only for the canonical component-revealing formalization on the 16x16 independent-bit proxy at p=1/2, not for the continuum Voronoi model directly nor for every conceivable exploration code; Monte-Carlo off-critical numbers (~0.75) are computed evidence, not proved bounds; no claim on the true Voronoi one-arm exponent or any preset fallback.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
