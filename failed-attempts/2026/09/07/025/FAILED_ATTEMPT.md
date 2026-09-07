# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Certified genus-26, multiplicity 6-9 census of numerical semigroups: exact counts, Frobenius distributions with gaps, and Wilf-ratio minima
- **Round:** 2026-09-07-first-light-01
- **Lane:** 35
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Semigroup Theory
- **Method:** Apery-set tree recursion with Kunz-coordinate pruning and exact Frobenius-type verification

## Problem

Enumerate up to isomorphism all numerical semigroups S (cofinite submonoids of N) with genus g(S)=26 and multiplicity m(S) in {6,7,8,9}. For each m certify the exact count N(26,m), publish the complete list of Kunz vectors k in N^{m-1} (Apéry sets Ap(S,m)={0} U {m*k_i+i}) with sum k_i=26 satisfying Kunz inequalities, compute for each S its Frobenius number F(S)=max Ap(S,m)-m, conductor c=F+1, embedding dimension e(S), and Wilf ratio W(S)=e*(c-g)/c, tabulate the Frobenius-number distribution per m including proven absent values, verify Wilf inequality W>=1 for the whole slice, and exhibit per m a maximal-Frobenius witness (F=51) and a minimal-Wilf-ratio witness with explicit generators.

## Attempted claim

Complete certified census for g=26, m=6-9: exact counts N(26,6), N(26,7), N(26,8), N(26,9) (pilot via Kunz recursion: 793, 1528, 4035, 6783; total 13139) with replayable enumeration logs; per-m Frobenius-number frequency tables on 29<=F<=51 with certified gaps (pilot: 36 missing for m=6; 35 missing for m=7; 32 and 40 missing for m=8) and maximal witness F=51 explicit in each m (e.g. Kunz (3,6,9,3,5) for m=6 with gens [6,19,22,35]; (4,8,3,2,5,4) for m=7; (3,4,7,1,2,4,5) for m=8; (1,2,3,4,5,6,2,3) for m=9); Wilf verification for all 13k semigroups with per-m minima (pilot: 1.125 for m=6 at Kunz (6,5,5,5,5) F=31; 1.129 for m=7; 1.0667 for m=8 at Kunz (4,4,4,4,4,3,3) F=29; 1.111 for m=9) and explicit minimal witnesses; exact genus/Frobenius verification by membership test.

## Research outcome

Certified genus-26 multiplicity 6-9 census: 793+1528+4035+6783=13139 semigroups with full Kunz/Frobenius/Wilf tables, proven in-range F-gaps (exactly multiples of m), F=51 witnesses in every m, and Wilf minima (global min 16/15 at m=8), all replayable in seconds via stdlib scripts with SHA hashes and independent cold verification.

## Why this attempt failed

Failed axes: value.

value: Even if correct and narrowly new, not independently worth finding later. (a) Textbook restatement: method is direct application of cited Kunz bijection plus membership x>=w_{x mod m}, F=max w-m, split-test for e; no new algorithm (exhaustive composition filter, 1.93s total, <1s per m, stdlib). (b) Mere parameter substitution: single genus-26 slice across m=6-9; totals known to g~60+ so no enumeration frontier is advanced; anyone can regenerate in seconds via GAP/stdlib. Per-m breakdown is intermediate data to known n_26. (c) Tiny unmotivated gains: Wilf verification on 13k genus-26 semigroups is subsumed by literature verifications to far larger genus; minima 9/8, 35/31, 16/15, 10/9 are slice-local minima with no global extremality, no counterexample, no bound improvement, and m=8-closest observation is post-hoc on 4 points. F-gap phenomenon is half trivial lemma (F%m!=0) plus finite contiguity observation in narrow intervals [29,51]/[30,51]/[31,51] with no general theorem, conjecture, or explanation. Maximal-F=51 (2g-1 symmetric) witnesses such as <9,10,25> are elementary symmetric constructions. (d) Unexplained enumeration: 13139-row CSV with no infinite-family theorem, no downstream lemma, no motivated benchmark need; static table adds no capability beyond on-demand GAP enumeration. Draft itself states it proves no infinite-family theorem and gap characterization is finite computed fact. Benchmark/baseline citability claim is insufficient: regenerable in seconds, not a theoretical advance. Matches REJECT precedent for correct-but-narrowly-new enumerations with no independent downstream use.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Rests on textbook Kunz bijection (cited, not re-proved). GAP numericalsgps cross-check unavailable (no GAP binary in environment); substituted by two-method agreement + OEIS g<=9 reproduction + cold verifier. No infinite-family theorem claimed; F-gap statement is finite-range computed fact plus elementary lemma F% m!=0. Totals n_26 known and GAP can enumerate on demand; novelty is the closed joint (Kunz,F,Wilf,witness,replay) certificate for the (26,6-9) slice, not a structural breakthrough.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
