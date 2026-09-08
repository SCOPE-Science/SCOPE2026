# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Certified real hyperbolic-center census for x^2+c in periods 4-7 via Gleason resultants, Sturm isolation, and orbit replay
- **Round:** 2026-09-07-first-light-01
- **Lane:** 61
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Dynamical Systems
- **Method:** dynatomic-resultant elimination with Sturm interval root isolation and orbit-iteration replay

## Problem

Let f_c(x)=x^2+c with c real. For each n in {4,5,6,7} determine the finite set C_n={c in R : 0 has exact period n under f_c}. Formulate the center polynomial P_n(c) by dynatomic-resultant elimination: F_n(c)=f_c^n(0) in Z[c], then exact removal of all P_d for d|n, d<n by polynomial division so P_n vanishes exactly on exact-period-n centers. Isolate every real root of each P_n in pairwise-disjoint rational intervals of width <=1e-10 with exact Sturm-count certificate (Sturm real-root count equals number of intervals), factor each P_n over Q, assign each root to its irreducible minimal-polynomial factor, and compute its length-n kneading word by certified sign evaluation of the critical orbit.

## Attempted claim

Closed certified census: for n=4,5,6,7, the exact count |C_n|, a list of disjoint rational isolating intervals (width <=1e-10) covering all real roots of P_n with Sturm certificate, full factorization of P_n over Q with discriminants and root-to-factor map, kneading word per center, and one lowest-|discriminant| period-7 center c* with explicit interval, minimal polynomial, and full critical-orbit replay proving f_{c*}^7(0)=0 with minimal period 7 (multiplier 0), all rechecked by an independent exact-rational orbit-iteration verifier.

## Research outcome

Closed Sturm-certified census: 2+3+5+9 real hyperbolic centers for periods 4-7 with irreducible minimal polynomials, discriminants, 19 disjoint 1e-10 rational isolating intervals, stable kneading words, rightmost period-7 orbit witness, all replayed by independent exact-rational verifier.

## Why this attempt failed

Failed axes: value.

value: Even though correct and formally new as a package, the result is not independently worth finding later. (1) Objects are classical: Gleason/center polynomials F_n,P_n for x^2+c have been known since the 1980s; coefficients for n<=7 recompute in milliseconds and factor in 0.001-0.03s; discriminants are bare integers with no stated application, and with single irreducible factor per n there is no discriminant ordering — draft Sec.6/8 admits 'minimal |disc|' is degenerate and retreats to rightmost center (maximal c) as canonical choice, whose 'smallest residual' is a bisection artifact, not an intrinsic extremum. No genuine extremal discovery. (2) Scope is a tiny subset of an existing certified census: Vigneron-Mihalache (2024) already certifies ALL hyperbolic centers to period 41 (tera-polynomial) with public database; a period 4-7 real slice (<2s total, well under a minute) is a small-range restriction with no new method — exact division + sympy Sturm + dyadic bisection + naive interval arithmetic are textbook computational algebra. (3) No surprise or consequence: kneading words are distinct within each n as expected for distinct real centers; no admissibility classification, no Galois/external-angle result, no conjecture resolved, no constant improved, explicitly no claim for n>=8, complex centers, or Galois groups. Counts 2,3,5,9 follow the expected ~2^{n-1}/n growth and are implied by the larger database. (4) This is therefore a small unexplained enumeration with standard-tool certification and a degenerate witness: textbook computation + tiny unmotivated gain over a much larger certified table. It does not meet the 'independently worth finding later' bar; value FAILS.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Real line periods 4-7 only; no claim for n>=8, complex centers, Galois groups, or external angles. Kneading means orbit signs vs 0 with stability only, not combinatorial admissibility. P_7 irreducibility makes 'lowest-|disc|' degenerate (single value); rightmost interval chosen as canonical representative. Midpoint c0 is rational approximation (residual 4.3e-10), not exact center; exact-period proof is via Sturm+gcd, multiplier 0 follows abstractly. sympy sturm/factor/discriminant/gcd trusted a…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
