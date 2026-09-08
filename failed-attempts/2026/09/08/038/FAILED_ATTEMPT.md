# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** A certified window-best systole upper bound around the Bolza surface via Fricke trace identities and collar-lemma packing
- **Round:** 2026-09-07-first-light-01
- **Lane:** 132
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Hyperbolic Geometry
- **Method:** Fricke trace-identity computation with collar-lemma packing and geodesic-length replay

## Problem

Fix genus g=2 closed hyperbolic surfaces parametrized by an explicit Fricke box B centered at the Bolza point (3 generators with a polynomial trace relation + box bounds |t_i - t_i(Bolza)| <= r in committed rational endpoints). Over B: (a) exhibit one explicit point p* in B with a certified systole value L* = 2*arccosh(|tr*|/2) from a committed trace triple, and (b) prove a rigorous upper bound U(B) on sup_{p in B} sys(p) via trace-identity length formulas plus a collar-lemma packing inequality, with an explicit gap U(B) - L_low >= delta > 0 against a low-systole baseline L_low attained at a box corner. Deliver replayable logs: integer-word matrix entries, trace values, length conversions, collar-width computations.

## Attempted claim

There exists an explicit Fricke box B around the Bolza point (radius r ~ 0.05-0.1 in trace coordinates, fixed by committed endpoints) and an explicit surface p* in B such that (i) sys(p*) = L* certified to +/-0.01 by trace identity 2*arccosh(|tr|/2) with interval arithmetic, and (ii) sup_{p in B} sys(p) <= U(B) with U(B) - L* <= epsilon (epsilon ~ 0.05) proved by collar-lemma disjointness plus trace-polynomial interval bounds, separating the extremal from a baseline corner with systole <= L* - delta (delta >= 0.15).

## Research outcome

Complete certified 132-row finite-word (<=8, 13120 words) trace-minimum census over Bolza-value Fricke window B=[13/3,16/3]^3 with exact-arithmetic traces, rigorous length/collar intervals (width ~2e-6), certified extremal gap >=0.457 (>0.15 bar), window sup bound U<=3.273614036, and a passing independent stdlib re-verifier.

## Why this attempt failed

Failed axes: value.

value: FAIL: result is correct and new but not independently worth finding later; it is a textbook function evaluation plus unexplained enumeration over an arbitrary slice, severed from its motivating question. Reasons: (1) Geometric disconnect conceded by DRAFT itself: coordinates are X(F2) free-group character variety, 'no claim is made that every point is a closed genus-2 surface holonomy (that would require genus-2 trace relations)'. Hence grid-max/min, gap, U and collar widths are statements about formal trace-length data 2*arccosh(m/2) and arcsinh(1/sinh(l/2)), not systoles or collars of closed genus-2 surfaces; representations are not shown discrete/Fuchsian/simple-closed, so collar-lemma quantity has no geometric collar meaning. Proximity of box centre 29/6 to Bolza value 2+2*sqrt2 is numerological, not a maximizer-centered neighborhood in the genus-2 moduli/character variety. (2) Enumeration is trivial in content: independent check shows for all 132 rows reported trace == min(x,y,z) (0 mismatches; wlen in {1,2} only, 101x length-1, 31x length-2 as ab). The 13120-word search never beats the three generators; the table is exactly 2*arccosh(min(x,y,z)/2) at 132 arbitrary rationals. Gap 0.4571... is just corner difference 2*acosh((16/3)/2)-2*acosh((13/3)/2) by monotonicity, requiring no census. Sup bound U=3.273614036 is the same corner evaluation. (3) Scope is arbitrary: why [13/3,16/3]^3 radius 0.5, why 5x5x5 step 1/4, why 3x3x3 half-step refinement around corner maximum yielding 7 points? No mathematical justification; refinement around the box corner maximum is ad hoc. (4) No downstream use: as length-spectrum benchmark it benchmarks only evaluation of arccosh/min; as trace-audit template it is plain 2x2 multiplication in Q(sqrt(D)) — textbook; it does not calibrate any sharp systolic constant since no genus-2 systole is bounded. Falls squarely under 'textbook restatement + mere parameter substitution (new arbitrary rationals in known formula) + unexplained enumeration' which must be rejected even if correct and new. Fallback is therefore not a citable census over a natural window but a bare grid log.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Fallback-level claim only: certifies the finite-word proxy (words length <=8), not the full infinite-word systole; coordinates are X(F2) Fricke trace coordinates of a Bolza-value window, not restricted to closed genus-2 holonomies (genus-2 trace relations not imposed). Target window-best bound U(B) with U-L*<=0.05 is NOT claimed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
