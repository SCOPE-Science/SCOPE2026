# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Insertion-automaton growth separation of Av(4231,3124) versus Av(4231,3214)
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1074
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Permutation Pattern Theory
- **Method:** insertion-encoding regular-language automata with transfer-matrix growth analysis

## Problem

Decide the Stanley-Wilf growth-rate ordering of the 4231-anchored siblings Av(4231,3124) and Av(4231,3214) via insertion-encoding DFAs and rigorous disjoint transfer-matrix spectral-radius enclosures.

## Attempted claim

The Stanley-Wilf growth rate of Av(4231,3124) is strictly smaller than that of Av(4231,3214), established by regular insertion-encoding DFAs whose transfer-matrix spectral radii admit disjoint rigorous interval enclosures proving gr(Av(4231,3124)) < gr(Av(4231,3214)).

## Research outcome

First exact census of Av(4231,3124) vs Av(4231,3214) to n=12 dual-verified (to n=15 single-engine) plus a certified insertion-encoding obstruction: coarse profiles provably inexact with witness pair, >=112 states forced for B at depth 8.

## Why this attempt failed

Failed axes: originality, value.

originality: FAIL: the headline census core is exact-database recomputation, not a first enumeration. OEIS A165535 (Av(4231,3124)) and A165532 (Av(4231,3214)) list the exact claimed sequences since 2009, cite Kremer-Shiu Discrete Math. 268 (2003) Table 1, give explicit algebraic generating functions, and provide b-files to n=1000 (Blomberg added a(13)-a(15) in 2018). The claimed new terms n=9..15 (e.g. A12 1782733 vs 1451780, A15 120707058 vs 88566290) appear verbatim in those tables and follow mechanically from the published g.f. series expansion. Admission's preflight claim that no OEIS/Wilf table lists this pair is objectively false: ADMISSION_DEFECT. Route is EMERGENT_FINDING genuinely arising from the blocked DFA target, so no evasion, but it receives no value presumption and the database coverage is fatal. The coarse-profile witness concerns an author-invented quotient with no prior standing and does not rescue headline originality. value: FAIL: judged on the strongest self-contained headline, there is no independently retrievable contribution. Recomputing two OEIS sequences to n=12-15 when 1000 terms plus closed-form algebraic generating functions and the Kremer-Shiu finite-transition-matrix source are already public adds no benchmark, constant, classification, or growth-rate decision; the draft itself disclaims any Stanley-Wilf inequality or regularity theorem. The length<=3-profile impossibility rules out only the authors' own ad-hoc quotient, not a recognized conjecture or published automaton candidate, and the >=112 signature lower bound neither decides (non-)regularity nor supplies matrices, radii, or enclosures the target required. Certification and triple-engine replayability are evidence properties that do not create value under the shared STANDARD for database-recomputed numbers and an unexplained ad-hoc obstruction.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: No Stanley-Wilf limit or growth-rate inequality in either direction is proved; the census direction (A ahead of B through n=15) is finite evidence only. Dual-engine verification covers n<=12; rows n=13..15 are single-engine (same binary, same frontier method, but without the independent full-ranking cross-check). The obstruction rules out only the length<=3-profile quotient route and lower-bounds exact insertion-encoding state counts; it does not decide (non-)regularity of either insertion lang…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
