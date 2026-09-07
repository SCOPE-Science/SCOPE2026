# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Complete GF(5)-representability census for rank-4 8-element matroids by single-element extension with explicit coordinatizations and excluded-minor witnesses
- **Round:** 2026-09-07-first-light-01
- **Lane:** 17
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Matroid Theory
- **Method:** single-element extension generation with Grassmann-Plucker exact coordinatization checks

## Problem

Let M(4,8) be the set of isomorphism types of matroids of rank 4 on 8 elements. Starting from the certified catalogue of rank-4 7-element matroids (Mayhew-Royle), generate all single-element extensions to 8 elements, deduplicate to canonical representatives by isomorphism hashing, and for each M in M(4,8) decide GF(5)-representability: either produce an explicit 4x8 matrix over GF(5) in normalized [I4|A] form whose bases equal the bases of M (verified by exact rank/determinant checks and Grassmann-Plucker relations), or produce an excluded-minor certificate consisting of deletion/contraction sets D,C such that M\D/C is isomorphic to a documented GF(5) excluded minor on <=9 elements, with explicit isomorphism. Output canonical hashes, counts, matrices, witnesses, and replayable logs.

## Attempted claim

Complete classification of M(4,8): every isomorphism type appears exactly once (by canonical hash), partitioned into R GF(5)-representable with explicit [I4|A] matrices over GF(5) realizing exactly the claimed bases, and N non-representable each with explicit (D,C,reference-minor,isomorphism) where the minor is one of the published <=9-element GF(5) excluded minors; plus for 3-connected representable cases the number of inequivalent GF(5)-representations up to row operations/column scaling/permutation. Independent checker replays hashes, matrix basis-equality, minor isomorphism, and duality counts in <15 minutes.

## Research outcome

Certified partial GF(5) census: 18 rank-4 8-element types (12 with explicit [I4|A] + Plucker, 6 with Fano/dual/Vamos minor witnesses), hash-distinct, with duality and fixed-basis representation counts, all replayed 95/95 PASS in ~0.5s stdlib-only. Global M(4,8) completeness explicitly disclaimed.

## Why this attempt failed

Failed axes: originality, value.

originality: No substantive new mathematical delta vs nearest priors. (1) Mayhew-Royle (math/0702316) already gives abstract catalogue to 9 elements; the 18 abstract types are contained therein. (2) F7 non-GF(5) (needs char 2), F7* by duality, V8 via Ingleton (1971) are decades-old textbook facts (Oxley); DRAFT itself claims no novelty for them (§2, §4). (3) Brettell et al. 2307.14614 (564 excluded minors <=9 elements, 2128 on 10) and 2206.15188 (Hydra-5 / six inequivalent GF(5) representations) already cover obstruction counts and representation-multiplicity theory; DRAFT explicitly disclaims testing the six-prediction (fixed-basis column-scaling counts 64-576 are strictly finer, §5 footnote, §6) and uses only F7/F7*/V8, not the 564-list. (4) The 12 [I|A] matrices plus fixed-basis counts/hashes are new strings but routine instances obtainable by standard exact linear algebra; no evidence they close a sought gap, instantiate a named non-trivial class (P8-like/whirl/spike identified in topic rejection_risks but absent here as anonymous Rxx), or were previously unknown/sought. Methods (extension, canonical-hash, determinant enumeration, brute-force iso) are standard. Hence constructive-partial artifact adds no conceptual novelty; timestamp/absence of prior publication of those exact matrices does not establish priority. value: Not independently worth finding later. Target in topic.json was complete M(4,8) census (thousands of types per DRAFT §1) with extension closure from 7-element catalogue, canonical-hash dedup, per-matroid GF(5) matrix or (D,C,reference<=9,iso) to published 564-list, inequivalent-representation tallies, and <15min checker; fallback was complete 3-connected (simple+cosimple) rank-4 8-element sub-stratum plus full pending list for remainder. Delivered is 18 arbitrary types (~<5% of stratum) with no completeness, no extension closure, no 564-list use (offline, §1), no 3-connected-core closure, no Hydra-5 tally, U(4,8) deliberately omitted (MDS q+1), Vamon-relaxation not closed — all disclaimed in §1 and §6. Selection of the 12 Rxx is unmotivated (no natural class, no theoretical consequence, no application beyond generic reusable pipeline). Mitigations claimed in topic (Plucker/duality/counts/minor witnesses) are defused by DRAFT itself: Plucker is sanity consequence, counts are non-projective, duality is routine. This is exactly textbook restatement (Fano/Ingleton/duality) plus unexplained enumeration of routine instances, which must be rejected even if correct and new.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Partial only: NOT the complete M(4,8) census (thousands of types); no Mayhew-Royle extension closure and no 564-member excluded-minor list used (offline). Hash is sound-but-incomplete invariant; representation counts are fixed-basis column-scaling orbits, not Hydra-5 projective classes; U(4,8) omitted (MDS q+1, non-GF(5), no UNSAT attempted); Vamos relaxation status not closed; Ingleton cited as known theorem.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
