# Independent audit — SCOPE-20260914-043

Audit date (UTC): 2026-10-01 (UTC)

## Final claim

Every separable simple nuclear finite non-elementary C*-algebra with nonzero densely defined traces, strict comparison, and stable rank one has the stated weak tracial cone approximation in every Pedersen hereditary subalgebra.

## Correctness

**FAIL** — The proof requires Z-stability and CPoU for each hereditary subalgebra, but it obtains Z-stability solely from strict comparison plus stable rank one under the stated general hypotheses. The available 2026 theorem of Lin proves this equivalence only with an additional trace-space hypothesis: the extremal boundary is sigma-compact and countable-dimensional. The record does not assume or derive that condition, nor another theorem covering its full generality. Consequently the central implication feeding the CPoU gluing step is unsupported.

## Originality

**PASS** — No source checked proves the record’s broader hypothesis set. The closest 2026 theorem requires additional tracial-boundary structure, and Z-stability-to-finite-nuclear-dimension results run in the opposite direction. The broad WTAC implication is therefore best-of-knowledge original, but originality cannot rescue its missing proof.

### Equivalent formulations

Aliases and equivalent formulations were compared against the closest primary sources; the assessment follows implication rather than title matching.

### Broader coverage

The checked broader theorems do not imply the exact final claim under the same hypotheses.

### Exact database or table

No finite database/table comparison is decisive for this theorem claim.

### Claim versus prior implication

No source checked proves the record’s broader hypothesis set. The closest 2026 theorem requires additional tracial-boundary structure, and Z-stability-to-finite-nuclear-dimension results run in the opposite direction. The broad WTAC implication is therefore best-of-knowledge original, but originality cannot rescue its missing proof.

## Value

**PASS** — If true under the stated unrestricted trace-space hypotheses, the result would strengthen a central regularity implication for stably finite nuclear C*-algebras and yield a useful uniform tracial approximation principle.

## Source inspections

- Tracial approximation and Z-stability — https://doi.org/10.4171/JNCG/654 — PARTIAL_COVERAGE: The equivalence is proved with sigma-compact countable-dimensional extremal trace boundary, an assumption absent from the record.
- Nuclear dimension of simple C*-algebras — https://arxiv.org/abs/1901.05853 — NOT_COVERING: It computes nuclear dimension for Z-stable algebras; it does not establish the missing general strict-comparison-to-Z-stability implication.
- A remark on weak tracial approximation — https://arxiv.org/abs/2209.12246 — NOT_COVERING: It discusses weak tracial approximation definitions/examples, not the claimed general cone approximation theorem.
- Published-results semantic search — https://github.com/Resultary/2026/tree/main/2026/9/14/SCOPE043 — NO_STRONGER_MATCH_FOUND: The exact record was the direct match; no distinct SCOPE result supplied the theorem under these hypotheses.

## Residual risks

- Literature search is best-of-knowledge and cannot exclude an obscure or unindexed source.
- The audit credits only inspected proofs, source material, and fresh computations described above.

## Disposition

FAILED
