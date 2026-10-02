# Independent audit — SCOPE-20260917-dfc5a7d88a20

Audit date (UTC): 2026-10-01 (UTC)

## Final claim

Tensoring the known two-dimensional strong-maximal A2 logarithmic obstruction over disjoint coordinate pairs yields weights in dimension d with norm growth at least a constant times A times a logarithmic factor of exponent floor(d/2)/2, and therefore any near-linear logarithmic upper bound must use at least that exponent.

## Correctness

**PASS** — The product-weight calculation is exact: rectangular A2 characteristics multiply over independent coordinate blocks, tensor-product test functions make the strong maximal averages factor, and weighted L2 norm ratios multiply. Repeating the known two-dimensional lower family over floor(d/2) pairs gives characteristic comparable to the reciprocal parameter raised to that number of pairs and the stated logarithmic factor. An unused coordinate in odd dimension cannot reduce the test-function norm ratio. The asymptotic conversion from the parameter to A is correct.

## Originality

**FAIL** — Although the exact all-dimensional formula may not have been printed before this record, it is mechanically implied by Lerner's two-dimensional theorem together with the standard exact product identities for rectangular weights and tensor-product strong maximal functions. The audit standard treats such direct implications as covered even when the precise statement is absent.

### Equivalent formulations

The higher-dimensional formula is the tensor-product reformulation of the two-dimensional lower bound. Evidence: The exact record was the closest published-results match. Lerner already supplies the complete two-dimensional lower-bound ingredient.

### Broader coverage

The decisive originality issue is implication from the prior two-dimensional theorem, not later domination. Evidence: A later 2026-09-19 published result gives a stronger all-dimensional logarithmic exponent, although it postdates this record. The prior two-dimensional theorem plus standard block products already supplies the audited formula.

### Exact database or table

Inapplicable as a finite-table question; theorem implication is decisive. Evidence: No finite database/table is relevant to this uniform analytic inequality.

### Claim versus prior implication

Applying those two facts repeatedly is sufficient to derive the claimed exponent with no new nonstandard lemma, so the claim is covered by prior theorem plus standard machinery. Evidence: Lerner gives a two-dimensional lower family of order A times the square root of log A. For independent coordinate blocks both the A2 characteristic and tensor test-function norm ratios multiply exactly.

## Value

**FAIL** — The dimension-dependent statement is obtained by the standard tensor-product construction with no additional structural difficulty once Lerner's two-dimensional example is available. Under the audit bar, this is a routine amplification of a known obstruction rather than an independently motivated boundary, classification, invariant, or structural lemma. Later work also obtains a stronger dimension-dependent logarithmic obstruction, further reducing the standalone value of this elementary tensor corollary.

## Sources inspected

- Failure of the linear A2 bound for the strong maximal operator — https://arxiv.org/abs/2609.14008. COVERING INPUT whose standard tensor product implies the audited claim: The source establishes exactly the lower family used in each coordinate pair.
- Improved weighted bounds for the strong maximal function — https://arxiv.org/abs/2609.17246. NOT needed for correctness and not the originality basis: It concerns all-dimensional upper bounds, while the audited lower bound is a tensor consequence of Lerner.

## Residual risks and limitations

- The precise historical first appearance of the tensorized formula was not established, but that does not rescue originality because prior theorem plus standard factorization already implies it.
- The mathematical lower bound is correct, but the scientific rejection is for originality and value, not correctness.
- The failed package should be preserved intact as evidence of a valid but routine corollary.

## Disposition

**FAILED**
