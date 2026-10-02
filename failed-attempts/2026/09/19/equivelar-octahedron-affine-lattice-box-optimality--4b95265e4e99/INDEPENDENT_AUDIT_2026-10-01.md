# Independent audit — SCOPE-20260919-4b95265e4e99

Audit date (UTC): 2026-10-01 (UTC)

## Final claim

The displayed source realization can be divided uniformly by three to an integral primitive configuration whose integral-affine bounding-box profile is exactly \( (156,200,200) \).

## Correctness

**FAIL** — The proof starts from a false normalization premise. The primary source table contains coordinates such as \(112\) and \(-112\), so the published vertex set is not coordinatewise divisible by three. The record instead uses \(111\)/\(-114\) in the corresponding positions after scaling, which is not the source configuration. Hence the claimed homothety, saturation statement for that normalized set, and resulting \( (156,200,200) \) source-affine optimum do not establish the stated claim. Independent source-specific SCOPE analyses also exhibit affine integral copies with cube span \(168\), incompatible with the claimed lower bound \(200\) on the longest span for the same source orbit.

## Originality

**FAIL** — FAIL because the current claim is both scientifically broken and dominated by earlier published SCOPE analyses of the same source realization. The 2026-09-17 and 2026-09-18 records already determine a strictly stronger affine-integer cube optimum (radius 84, span 168) from the actual source coordinates. Thus the claimed source-specific affine optimum is not a new surviving statement.

The audit separately checked equivalent formulations, broader coverage, exact database/table overlap, and claim-versus-prior implication. Full source-inspection details and residual risks are recorded in the companion JSON.

## Scientific value

**PASS** — PASS as a target question: exact affine-integer coordinate invariants of a new polyhedral realization are reusable and mathematically motivated. This does not rescue the record because its source normalization is false and the actual affine orbit was already analyzed.

## Disposition

**FAILED.** A validated finding requires correctness, originality, and value all to pass. The original scientific files and reproducibility artifacts are retained with the failed-attempt package.
