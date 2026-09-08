# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Least quadruplet-quintuplet diamond 30 apart below 10^9: certified 9-tuple witness at 685124351 with a Hardy-Littlewood density gap
- **Round:** 2026-09-07-first-light-01
- **Lane:** 110
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Analytic Number Theory
- **Method:** sieve weight optimization with deterministic primality verification (segmented sieve census, Hardy-Littlewood/Selberg density bracket, deterministic Miller-Rabin plus ECPP-style logs)

## Problem

Let H=(0,2,6,8,30,32,36,38,42): a prime quadruplet (0,2,6,8) plus, 30 higher, a prime quintuplet of the canonical (0,2,6,8,12) shape. Prove H admissible; prove by complete segmented-sieve census that the least n<10^9 with all nine of n+H prime is n=685124351 and that it is the unique such n below 10^9; certify all nine values by deterministic Miller-Rabin (bases 2,7,61, valid below 2^32) with replayable logs; compute the Hardy-Littlewood singular series S(H)~868.2 and show the HL prediction (~1.2 hits) versus the naive independence model (~0.0013) explains the ~700x local-factor enhancement at this explicit witness; and produce a Selberg Lambda^2 sieve upper-bound certificate for the H-count below 10^9.

## Attempted claim

(T1) H=(0,2,6,8,30,32,36,38,42) is admissible. (T2) n=685124351 is the least integer below 10^9 with all nine of n+H prime, and the unique such integer below 10^9; the nine primes are 685124351, 685124353, 685124357, 685124359, 685124381, 685124383, 685124387, 685124389, 685124393 (offsets +0,+2,+6,+8,+30,+32,+36,+38,+42). (T3) Each of the nine values carries a deterministic Miller-Rabin certificate (bases 2,7,61) with replayable logs. (T4) S(H)~868.2, the Hardy-Littlewood prediction below 10^9 is ~1.2 versus ~0.0013 for the naive independence model, and a Selberg Lambda^2 upper-bound certificate (level D=10^5, value U recorded by the audit script, U>=1) brackets the certified count of 1.

## Research outcome

Certified least+unique quadruplet-quintuplet diamond witness n=685124351 below 1e9 with nine deterministic primality logs, admissibility proof, singular series 866.36+/-0.31 giving HL~1.23 vs naive~0.0014, and Selberg upper-bound bracket U=1794237.

## Why this attempt failed

Failed axes: value.

value: Correct and new but not independently worth finding later. The package is: (a) a one-point cap extension of the known 8-point twin-quad core to H=(0,2,6,8,30,32,36,38,42); (b) a brute-force segmented-sieve first-occurrence/ uniqueness census below 1e9 (observed count 1 vs HL heuristic 1.23, i.e. exactly as expected, no anomaly); (c) textbook evaluations of classical formulas at this single tuple: singular-series product S(H)~866 (the ~866x HL-vs-naive ratio is just S(H) itself, expected to be large for any dense k=9 cluster) and a Selberg Lambda^2 upper bound U~1.79M sifting only to 11, which is ~10^6x above the truth 1 and brackets the count only in the vacuous sense U>=1. No general theorem, no new sieve weights or method (pipeline is standard segmented sieve plus deterministic 32-bit MR), no sharp bound, no anomaly or calibration that constrains or advances the Hardy-Littlewood/Maynard-Tao program; a single-witness leading-term evaluation does not test or refine sieve constants. The citable content reduces to a first-occurrence database record for an ad hoc 9-tuple plus routine formula plug-ins: a mere parameter substitution (one-point cap) with textbook restatements and an unexplained single-tuple enumeration. Fails the independent worth-finding-later bar even though correct and new.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Least/unique below 1e9 only, not infinitude; HL-vs-naive gap is model calibration at one witness, not HL proof (observed 1 vs HL 1.23 is agreement); Selberg U~1.79M is weak but rigorous and nontrivial; integral diagnostics exploratory, not claimed; base term known in A059925, machinery classical — novelty is the 9-point cap, certification, and density bracket.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
