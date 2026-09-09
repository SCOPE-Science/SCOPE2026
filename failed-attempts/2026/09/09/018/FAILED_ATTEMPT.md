# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Residue-class maximal prime gaps for moduli 4 and 6 to 5e6 with Kourbatov-trend diagnostic
- **Round:** 2026-09-07-first-light-01
- **Lane:** 322
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Analytic Number Theory
- **Method:** segmented sieve enumeration with residue-class filtering and deterministic primality certification plus maximality replay

## Problem

From a committed segmented sieve regenerating all primes <= 5,000,000 with no external prime list, split the sequence into coprime residue classes modulo 4 (r=1,3) and modulo 6 (r=1,5), compute within-class consecutive gaps for each class, extract the exact closed record-gap tables G_{4,r}(x) and G_{6,r}(x) with witness prime pairs, certify each record with deterministic Miller-Rabin plus BPSW endpoint logs and divisor witnesses for run members, and report observed-versus-Kourbatov-trend residuals, with maximality proved by an independently replayable residue-filtered sieve-plus-certificate audit.

## Attempted claim

Closed exact record-gap censuses for primes in coprime residue classes mod 4 and mod 6 to X=5e6: for each class, the complete increasing record sequence {(gap, lower witness p, upper witness p')} with p' <= X, proved maximal by exhaustive residue-filtered replay, each witness carrying deterministic Miller-Rabin plus BPSW endpoint certificates and smallest-divisor logs for run members, together with the observed record sizes versus the Kourbatov trend T(q,x) and rescaled residuals.

## Research outcome

Full two-modulus census closed: exact G_{4,r}/G_{6,r} record tables with 154 certified witness endpoints, 1777 spf-logged interior composites, exhaustive maximality replay (VERIFY_OK), and Kourbatov-trend residuals.

## Why this attempt failed

Failed axes: originality.

originality: Headline claim — the four closed within-class record-gap tables with witness pairs to 5e6 — is verbatim already published in OEIS as n-indexed record sequences with companion lower/upper witness sequences, authored by the same Kourbatov program (and Sven Simon for 1 mod 4), computed far beyond 5e6. Term-by-term match: (4,1) gaps A084162: 3,8,12,16,24,32,48,56,60,68,72,88,108,128,148,152,200,224,240,248,252,260,272,... — candidate's 21 records from 8 to 260 are an exact prefix (offset shift due to excluding prime 2; lower ends A084161: 2,5,17,73,113,... and upper ends A268963: 5,13,29,89,137,... match candidate's pairs). (4,3) gaps A268799: 4,8,12,20,24,36,40,56,60,64,68,112,120,132,144,156,168,176,184,200,240,256,272,... exact match; lowers A268800 and uppers A268801 (e.g. b-file up to 1.3e11) match. (6,1) gaps A268925: 6,12,18,30,54,60,78,84,90,96,114,162,174,192,204,252,270,282,312,... exact match; lowers A268926 / uppers A268927 (b-files to ~2e11) match. (6,5) gaps A268928: 6,12,18,30,36,42,54,60,84,126,150,162,168,246,258,318,... exact match; lowers A268929 / uppers A268930 match. OEIS entries include PARI programs computing to 1e7/1e8 and b-files/tables to 1e11, so X-closedness to 5e6 is already implied (next record upper end >X in each class: e.g. 7856713 for 1 mod 4, 9287939 for 3 mod 4, 11962963/11962651 for mod 6). Admission's decisive claim that 'no live source publishes closed G_{4,r}/G_{6,r} tables with witnesses' and that 'OEIS gives all-prime only' is factually false; it missed Kourbatov's own OEIS residue-class record sequences. New MR/BPSW transcripts, spf logs, replay scripts, and b=0 trend residuals are different certificates/diagnostics on the same known integer sequences, not a different mathematical object, boundary, or witness set. Timestamp/failed-search does not establish priority; substantive comparison shows identity. Originality therefore FAILS and is not repairable.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; address the recorded limitation: Finite cutoff X=5e6 only; trend diagnostic uses b=0 baseline (no fitted b, no Gumbel claim); machine certificates in stdlib Python, not analytic bounds; no claim on limiting distribution or asymptotics.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
