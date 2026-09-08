# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Certified per-block maximal-gap census to 2,000,000 with merit and an admissible prime-constellation witness
- **Round:** 2026-09-07-first-light-01
- **Lane:** 71
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Analytic Number Theory
- **Method:** segmented-sieve enumeration with deterministic Miller-Rabin certification and independent primality replay

## Problem

Enumerate all primes <=2000000 by segmented Eratosthenes (base primes to sqrt(2M)=1415, segment 32768) and certify a per-block maximal-gap census: partition into 20 blocks B_k=((k-1)*100000,k*100000] (B_1 includes 2); for gaps g_i=p_{i+1}-p_i with p_{i+1}<=2000000, for each B_k report block prime count, maximal gap g_max(k) among gaps with left endpoint in B_k, least first-occurrence pair (p,p+g) achieving it, and merit m=g/log(p) (natural log). Also list global first occurrences. Additionally produce one admissible constellation witness <=2M: a prime quadruplet (p,p+2,p+6,p+8) or sextuplet with explicit tuple, sieve window dump, and deterministic Miller-Rabin certificates (bases 2,7,61) for each member.

## Attempted claim

A complete, byte-reproducible table for all 20 blocks to 2000000 (block counts, g_max(k), least first-occurrence pair, merit g/log p) from a logged segmented sieve, with deterministic Miller-Rabin (bases 2,7,61) certificates for every gap endpoint, plus at least one certified admissible quadruplet (p,p+2,p+6,p+8) or prime sextuplet with explicit tuple, sieve log and certificates; an independent replay script with different bases re-verifies all primality claims and reproduces the CSV exactly (matching SHA256).

## Research outcome

Full 2M target achieved with replay: segmented-sieve census (148933 primes, 148932 gaps), 20-block maxima with merit, 61 first occurrences, dual Miller-Rabin certification, quadruplet+sextuplet witnesses, byte-identical independent replay with SHA-256 hashes, in ~3 s single-core stdlib-only computation.

## Why this attempt failed

Failed axes: originality, value.

originality: Mathematical content is definitionally anticipated. Prime Pages 'Gaps Between Primes' (Caldwell, t5k.org/notes/gaps.html) tabulates first occurrences through gap 381 including every claimed entry below 2M (e.g. difference-34 at 1327 listed as gap-33 composites, difference-118 at 1349533, difference-132 at 1357201), differing only by g_composites=g_difference-1 convention; exhaustive searches (Nicely to 1e15, Kourbatov to 4e18, Visser beyond 2^64) cover [2,2M]. Candidate's own draft concedes max gap 132 is 'long known' and witnesses are 'classical (5-13 and 7-23)'. The least quadruplet (5,7,11,13) and sextuplet (7,11,13,17,19,23) are textbook least prime k-tuples. Per-100k-block maxima and merit g/ln p are deterministic slices/ratios of the same known prime list using standard definitions discussed on the same Prime Pages page (average gap log n, Cramer merit). SHA256/CSV/MR-certificate/replay packaging is provenance engineering, not a new theorem, extremum, or method. No cited source provides a distinct claim; packaging does not establish priority. value: Even taking correctness for granted, result is not independently worth finding later. It is a textbook segmented-sieve enumeration to an arbitrary bound (2M), arbitrary 100k blocking, standard merit ratio, and trivial least constellation witnesses, with explicitly disclaimed record novelty, no anomaly, no conjecture decision, and no theoretical consequence. Crude Cramer comparison ('merits peak at 9.35 below 211') is descriptive scatter, not a test. This is exactly the excluded class: textbook restatement + mere parameter choice (2M/100k blocks) + unexplained enumeration. A replayable CSV of known gaps to 2M with hashes does not become a citable extremal dataset when authoritative tables to 1e15+ already exist.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: No new maximal-gap record (132 is classical); witnesses (5,7,11,13) and (7,11,13,17,19,23) are the known least tuples — contribution is certification, not discovery; merit column is descriptive, no theorem about Cramer model above 2M; correctness rests on two agreeing Python implementations plus deterministic MR theory (bases 2,7,61 valid below 2032801^2 >> 2M); gaps.csv (2.7 MB) is the bulk artifact.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
