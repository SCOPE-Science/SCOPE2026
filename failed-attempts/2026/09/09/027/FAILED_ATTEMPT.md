# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Hull-dimension spectra and LCD-vs-one-dimensional-hull gaps for short binary linear codes (lengths 16-24) with Gram-rank certificates
- **Round:** 2026-09-07-first-light-01
- **Lane:** 342
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Coding Theory
- **Method:** Gram-rank hull certification (rank GG^T over F2) with building-up construction, syndrome distance proof, and MacWilliams-identity replay

## Problem

Determine the hull-dimension spectrum at committed short parameters: for 4-5 flagship [n,k] cells with n in 16..24 and k in {5,6} plus one k=7 anchor, exhibit explicit binary generators realizing hull 0 (LCD) and hull 1 (one-dimensional hull) at best-known distance where possible, certify each hull by exact F2-rank of G*G^T, certify each distance by syndrome replay with live weight enumerator and MacWilliams cross-check, pin d_LCD(n,k) and d_one(n,k) with witnesses, and test Bouyuklieva n-to-n+1 monotonicity along the chain.

## Attempted claim

Hull-dimension spectrum with LCD-vs-one-dim gap at short lengths: at 4-5 committed [n,k] cells (n in 16..24, k=5,6 plus one k=7 anchor), both hull 0 and hull 1 occur among codes attaining best-known distance, with explicit generators, exact F2 Gram-rank certificates (rank k and k-1), syndrome distance proofs, MacWilliams-checked enumerators, exact d_LCD and d_one values at 3+ cells including one building-up-linked LCD/one-dim pair, and a verified Bouyuklieva monotonicity step along the chain.

## Research outcome

Paired LCD/one-dim-hull witness table at 5 short cells with machine-checked Gram-rank hull certs, tally+MacWilliams distance certs, width<=2 intervals and gap row; fallback-level claim (no building-up link, exact pins only at Griesmer-optimal [20,5],[20,6]).

## Why this attempt failed

Failed axes: originality, value.

originality: Strongest headline existential facts are substantively anticipated by conjunction of prior exact tables. Bouyuklieva 2010.13399 Table 1 gives exact d_LCD at committed cells (16,5)=6, (20,5)=9, (20,6)=8, (24,6)=10, (24,7)=9 with no intervals; Li-Shi-Kim 2211.02480 Table 1 gives exact d_one at same cells (16,5)=6, (20,5)=9, (20,6)=8, (24,6)=10, (24,7)=10 with no intervals (intervals only appear n>=25); abstract confirms d_one(n,k) determined for 14<=n<=24. Jointly these imply both hulls {0,1} occur at optimum distance with gap 0 at four cells and gap -1 at [24,7] — mechanically, without new computation. Sogang CICAGO site publishes explicit one-dim generators achieving optima including [20,5,9], [20,6,8], [24,6,10], [24,7,10]. Candidate's new content is alternative stochastic-search matrices plus textbook Gram-rank (Lemma 2.3), standard tally, and MacWilliams/syndrome logs as one bundle, plus a width-<=2 gap row that is weaker than known exact gaps. No building-up linkage (admitted success criterion unmet), no equivalence/inequivalence analysis, no new enumerator or structural property. Candidate's [24,7] one-dim witness (d=8) is 2 below the published optimum (10), so it does not even reproduce the known fact. A failed API triage or new certificate format does not establish priority. value: Even if certificates are correct, result is not independently worth retrieving. Bare distances reproduce known hull-constrained optima at 4 cells and are suboptimal at [24,7] one-dim (8 vs known 10). The paired gap bound |gap|<=2 is strictly weaker than exact gaps implied by prior tables (0,0,0,0,-1) and follows trivially from [ach,UB] widths; general LCD/one-dim inequalities already in Li-Shi-Kim Lemmas 3.1-3.2 and Bouyuklieva. Witness matrices are arbitrary hull-constrained stochastic-search outputs with no canonical property (no building-up link, no extremal enumerator, no completed census — 5 cells, admitted incomplete). Per standard, certification alone does not rescue an arbitrary object: future researcher needing [20,5,9]/[20,6,8]/[24,6,10] LCD/one-dim codes can use Bouyuklieva classified values plus Sogang explicit generators; candidate alternatives add no distinguishing invariant. This is unexplained enumeration / repackaging of known optima with replay logs, plus one suboptimal witness, not a narrow exact invariant whose value was unknown and motivated.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Exact d_LCD/d_one pins only at [20,5] (d=9) and [20,6] (d=8) via Griesmer equality; elsewhere width-1/2 intervals only. No building-up-linked LCD/one-dim pair (audit success criterion unmet). n=24 distance rests on tally+MacWilliams (no syndrome BFS). Bare distances may overlap published d_LCD tables; novelty is the paired certified bundle. Prior-art gap per API-level triage only.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
