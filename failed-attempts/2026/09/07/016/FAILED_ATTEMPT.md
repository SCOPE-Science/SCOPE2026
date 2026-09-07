# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Certified census and first-occurrence closure for diameter-16 prime sextuplets in [10^12, 10^12+10^9]
- **Round:** 2026-09-07-first-light-01
- **Lane:** 21
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Analytic Number Theory
- **Method:** segmented sieve enumeration with deterministic Miller-Rabin and Pratt primality certificates

## Problem

Let pattern S(p) = (p, p+4, p+6, p+10, p+12, p+16). Enumerate by segmented sieve ALL p in closed interval I = [1000000000000, 1001000000000] (10^12 to 10^12+10^9) such that all six entries of S(p) are prime. For each survivor, certify primality by (a) deterministic Miller-Rabin for 64-bit integers using known basis set {2, 325, 9375, 28178, 450775, 9780504, 1795265022} and (b) a full Pratt certificate (primitive root + prime factorization of q-1 for each prime q in S(p), recursively certified, verifiable by modular exponentiation). Cross-check the count N(I) by two independent sieve implementations (chunked bytearray segmented sieve + independent wheel/modular recount) with archived logs and hashes. Diff the enumerated list against public first-occurrence tables to isolate any tuple whose first-occurrence status above 10^12 is missing or uncertified.

## Attempted claim

Exhibit the least p* in I absent from public tables (or the least p* in I overall if I is entirely untabled), with full decimal expansions of all six primes p*, p*+4, p*+6, p*+10, p*+12, p*+16, deterministic Miller-Rabin transcripts, machine-checkable Pratt certificate files, and proof of minimality/completeness below p* within I via archived sieve logs plus independent recount agreement. Example artifact: p* = [explicit 13-digit integer to be filled by enumeration] with 6 certificates each verifiable in <5 seconds.

## Research outcome

Complete Pratt-certified census of diameter-16 prime sextuplets (p,p+4,p+6,p+10,p+12,p+16) in closed I=[1e12,1e12+1e9]: N(I)=42 with explicit ordered list, least p*=1000033407547 (full 13-digit expansions), deterministic 7-base Miller-Rabin transcripts + sympy second opinion on all 252 values, 252/252 standalone Pratt certificates verified, byte-identical double-sieve agreement (odd-only 0.74s + wheel-30 1.84s), miss histogram + H-L prediction 38.87 vs 42 observed (ratio 1.08, Poisson p=0.33). Table novelty conditional on offline truncation claim (live OEIS/Wikipedia fetch unavailable).

## Why this attempt failed

Failed axes: value.

value: Even though correct and narrowly new, the result as stated is not independently worth finding later. It is a textbook pattern at an arbitrary round-number interval with only routine computation: (i) Pattern S(p) minimal-diameter claim and p=7(30) filter are 2-line CRT exercises; (ii) Interval [1e12,1e12+1e9] is decimal-round, not mathematically distinguished (not a maximal gap, not a new limit, not a community-requested benchmark gap, not a counterexample); any 1e9 window has a trivial least-in-I if non-empty, conflated here with first-occurrence record while explicitly disclaiming maximal-digit record; (iii) Computation is trivially recomputable: 0.74s + 1.84s sieves, <10s total on laptop with standard C/Python, so archival value is nil; (iv) No surprise or consequence: observed 42 vs HL 38.87 ratio 1.08 Poisson p=0.33 (<0.6 sigma) is exactly null result, no anomaly, no new conjecture, no refutation, no method advance; (v) Certificates are credential inflation: deterministic MR already proves 13-digit primality in <1ms; 252 Pratt certs add files but no insight; (vi) Miss histogram (5-of-6 uniform within noise, as expected) and HL product are perfunctory byproducts, explicitly without finding. This is precisely mere parameter substitution (same classical 6-tuple at larger bound) plus unexplained enumeration (list of 42 positions with no structure revealed) with generic add-ons that could be attached to any interval. Per scope rule, such enumerations are rejected even if correct and new.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Live OEIS A022008 b-file / Wikipedia / constellation-table diff NOT performed: both HTTPS fetches failed with transport errors on 2026-09-07 (logged). First-occurrence novelty therefore rests on range argument (42/42 >=1e12, 0 overlap with brute-verified head [7,97,16057,19417]) plus triage offline knowledge that dense b-file coverage stops far below 1e12 and largest-known records are 100s-of-digits size records; exact line diff upgrade via diff_tables.py --bfile with local b-file. No originali…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
