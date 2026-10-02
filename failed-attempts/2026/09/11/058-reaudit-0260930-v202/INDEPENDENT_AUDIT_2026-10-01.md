# Scientific audit — SCOPE-20260911-058

Date (UTC): 2026-10-01

## Final claim

For the supersingular curve with j-invariant 1728 over the field of 1031 elements, every based 2-isogeny loop of length at most eight yields an endomorphism in the commutative quadratic subfield, so two such loops cannot be noncommuting generators of the full endomorphism order.

## Correctness

**PASS** — The standard maximal-order basis for the j=1728 curve gives an exact reduced-norm form. Any element outside the quadratic subfield has reduced norm at least 258, while a length-at-most-eight 2-isogeny loop has degree and norm at most 256. The package verifier was inspected and independently checked the point count, order discriminant, norm bound, and short self-loop context.

## Originality

**FAIL** — The claimed obstruction is a direct specialization of the already published exact j=1728 endomorphism-ring basis. Once that basis is known, its reduced norm immediately yields the general norm gap; substituting p=1031 and the degree bound 256 gives the record's conclusion. The absence of the literal number 1031 in prior prose does not make this corollary original.

### Equivalent formulations
Short-loop commutativity is equivalent here to saying every endomorphism of norm below the first off-quadratic norm lies in the quadratic subfield.

### Broader coverage
The broader structural description directly gives the norm gap and dominates the p=1031 numerical specialization.

### Exact database or table
Absence of an exact table is immaterial because a stronger published structural theorem already implies the claim.

### Claim versus prior implication
Prior work mechanically implies the claimed obstruction after the elementary comparison 256 < 258.

## Value

**FAIL** — Short-isogeny generation is a motivated topic, but this particular p=1031 and length-eight disproof is a routine numerical corollary of an established maximal-order description rather than a new structural boundary or independently motivated exact invariant.

## Sources inspected

- Package result and verifier: https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/11/058/RESULT.md — Supports correctness of the finite norm-gap deduction.
- Frobenius and the endomorphism ring of j=1728: https://math.colorado.edu/~kstange/papers/1728.pdf — Covers the structural basis from which the record's norm-gap corollary follows.
- Resultary published-results search: https://github.com/Resultary/2026/tree/main/2026/9/11/SCOPE058 — No separate exact p=1031 table was located, but this does not overcome stronger prior structural coverage.

## Residual risks and limitations

- The conclusion concerns only the stated curve and length bound.
- The correctness argument uses the standard identification of isogeny degree with reduced norm.
- The originality failure is based on prior stronger structural coverage, not merely on an exact-title match.

## Disposition

FAILED
