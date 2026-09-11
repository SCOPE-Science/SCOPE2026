# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Uniform Herman-Avalanche Lyapunov bound with N=80 Green decay on a centre window at coupling 3
- **Round:** 2026-09-07-first-light-01
- **Lane:** 886
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Spectral Theory
- **Method:** Herman subharmonicity with Avalanche Principle and large-deviation Green-function decay

## Problem

For the almost Mathieu operator (Hu)_n = u_{n+1}+u_{n-1}+3*cos(2*pi*(n*alpha+theta))*u_n with alpha=(sqrt(5)-1)/2, prove that for every E in the explicit centre window W=[0,0.5] the Lyapunov exponent satisfies L(E) >= log(3/2)-0.05, and that the finite-volume Green function on [1,80] satisfies exponential decay with rate >=0.30 off an explicitly logged resonant phase set of small measure.

## Attempted claim

Uniform bound L(E) >= log(3/2)-0.05 for all E in [0,0.5] at lambda=3 golden mean, plus finite-volume Green decay on scale N=80 with rate >=0.30 outside an explicitly listed resonant set.

## Research outcome

TARGET complete: rigorous Herman bound L>=log(3/2) on [0,0.5] plus replayable N=80 Green-decay ledger (rate 0.30, C*=8.0, 0.85% explicitly logged resonant set, VERIFY_OK). New content is the explicit conjunction/ledger; Herman conjunct alone is classical.

## Why this attempt failed

Failed axes: value.

value: Value FAILS as textbook restatement plus unexplained enumeration. Conjunct (a) is admitted classical Herman bound, reproved, not new. Conjunct (b) is a 10-second double-precision enumeration on an arbitrary grid (41 E x 400 theta, N=80 not Fibonacci, rate 0.30, C*=8.0 large, 1.5% gate) with no interval arithmetic and explicitly no grid-to-continuum enclosure. It therefore does not constitute the claimed multiscale-analysis input for localization, which requires uniform continuum bounds off a small-measure set; between grid points resonances are unenclosed. The thresholds and grid are post-hoc tuned to pass VERIFY_OK, not motivated before computation, and the resulting statistic (140/16400 resonant) is grid-dependent, not a reusable exact invariant of the natural operator that a future researcher could need. Recomputation is trivial. Certification alone in double precision does not rescue an arbitrary scope. This is precisely mere parameter substitution and unexplained enumeration, even though correct and new.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: ['Green part is a finite-grid (41x400) computed witness, not a continuum proof over all (E,theta); no interval arithmetic; grid-to-continuum gaps open.', 'C*=8.0 is a large constant; only the long-range slope 0.30 is controlled.', 'Double precision only; inversion residuals <=1e-12 negligible vs threshold gaps.', 'Herman proof is classical (Herman 1983), reproved; novelty is the conjunction with the explicit N=80 ledger.']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
