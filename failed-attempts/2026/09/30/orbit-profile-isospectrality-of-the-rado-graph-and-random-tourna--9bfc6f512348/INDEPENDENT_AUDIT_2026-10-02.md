# Independent mathematical audit — SCOPE-20260930-9bfc6f512348

Final disposition: **FAILED**.

## Correctness
**PASS** — The orbit formulas are correct. On injective \(k\)-tuples, both the Rado graph and random tournament are encoded by \(\binom{k}{2}\) independent pair bits. Complement/reversal translates by the all-one vector, while graph/tournament switching translates by the cut space of dimension \(k-1\). The quotient sizes and small-\(k\) exceptions follow immediately, and equality-pattern partitions give the Stirling transform for arbitrary tuples. The binary orbital-pairing argument correctly distinguishes the base graph and tournament groups up to permutation conjugacy.

## Originality
**FAIL** — A published September 30 result already gives the complete five-group Rado-graph tuple-orbit profiles, including the identical closed formulas and Stirling transforms. The reduct-classification literature already supplies the corresponding random-tournament reversal and switching operations. On a labeled tournament those operations act on the same pair-bit space by the same all-one and cut translations, so the tournament formulas and hence the cross-family profile equality are a mechanical reuse of the existing Rado calculation. The base non-conjugacy witness is immediate from undirected binary orbitals being self-paired and tournament orientation orbitals being transposed. The final cross-family statement is therefore covered by prior formulas plus standard classified operations.

### Equivalent formulations
The assigned cross-family result is the same finite affine action applied to the classified tournament reducts.

### Broader coverage
Together these sources dominate the scientific content needed for the equality.

### Exact database or table
The absence of the phrase profile-isospectrality is irrelevant because the tournament side is an immediate equivalent calculation.

### Claim versus prior implication
The final theorem is mechanically implied by prior results and elementary coding.

## Value
**FAIL** — Numerical isospectrality is a neat observation, but after the exact Rado profile theorem and the tournament reduct generators are available, the cross-family calculation adds no nontrivial new structure: it repeats the same affine quotient on the same-dimensional bit space and appends an elementary orbital-pairing distinction.

## Source inspections
- **Exact tuple-orbit profiles of the five reduct groups of the Rado graph** (https://github.com/Resultary/2026/tree/main/2026/9/30/SCOPE-exact-tuple-orbit-profiles-of-the-five-reduct-groups-of-the-rado--292fd3720b95): complete RESULT.md Method: published-result full-text inspection. Assessment: EXACT_PRIOR_COVERAGE_OF_RADO_SIDE. Evidence: It proves exactly the five injective formulas and Stirling transforms used in the assigned record.
- **The 42 reducts of the random ordered graph** (https://arxiv.org/abs/1309.2165): primary article context and classification descriptions of the relevant reduct operations Method: primary-source inspection. Assessment: CLASSIFIED_TOURNAMENT_OPERATIONS. Evidence: The reduct catalog contains the random graph and random tournament subfamilies with the corresponding reversal/complement and switching generators.

## Checked sources
- https://github.com/Resultary/2026/tree/main/2026/9/30/SCOPE-exact-tuple-orbit-profiles-of-the-five-reduct-groups-of-the-rado--292fd3720b95
- https://arxiv.org/abs/1309.2165

## Residual risks
- No correctness defect is asserted; rejection is prior coverage plus a mechanical cross-family transport.
