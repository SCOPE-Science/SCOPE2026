# Independent audit — SCOPE-20260912-081

Audit date (UTC): 2026-10-01 (UTC)

## Final claim

At t=q=1/2, the specified boundary blocks contain an infinite orthogonal family with eigenvalues tending to -2/3 and multiplicity n+1, so the ordinary resolvent is noncompact and |D|^{-s} is not ordinary trace class for any real s.

## Correctness

**PASS** — The package records the Kaad-Kyed vertical/horizontal formulas. On V^n_{i0}, the horizontal term vanishes by the matrix-coefficient pairing, while the vertical eigenvalue is e_n=(t^(n+1)-1)/(t^(-1)-t); at t=1/2 it tends to -2/3 and stays bounded away from zero. The n+1 orthogonal i-indices give an infinite bounded spectral family, proving ordinary noncompactness and divergence of the positive ordinary trace sums for every real s.

## Originality

**FAIL** — The substantive obstruction is already covered by Kaad-Senior's statement that this resolvent is compact only in the semifinite sense.

### Equivalent formulations

The present boundary eigenvalue family is an explicit witness for that already-known ordinary noncompactness.

### Broader coverage

The predecessor is broader than this single t=q=1/2 witness on the key novelty point.

### Exact database or table

This check is specifically inapplicable.

### Claim versus prior implication

The record is a direct explicitization/corollary rather than a new theorem.

## Value

**FAIL** — As a scientific finding, the record is a routine explicit witness for an already-known obstruction. It is a useful cautionary calculation, but it does not supply a motivated new boundary, invariant, classification, or structural lemma beyond the prior noncompactness result.

## Sources inspected

- A twisted spectral triple for quantum SU(2) — https://arxiv.org/abs/1109.2326 — COVERING: The abstract explicitly states that the resolvent becomes compact only relative to a semifinite trace, not in the ordinary operator sense.
- The quantum metric structure of quantum SU(2) — https://arxiv.org/abs/2205.06043 — CONTEXT: The paper supplies the two-parameter operator family; the package specialization t=q=1/2 uses those formulas.
- Published Resultary SCOPE081 — https://github.com/Resultary/2026/tree/main/2026/9/12/SCOPE081 — SELF_MATCH: The exact published record was the direct match; no distinct stronger SCOPE record appeared.

## Limitations

- The conclusion is about ordinary operator trace/compactness at t=q=1/2.
- For non-real z, the correct statement is absence of a trace-class convergence half-plane, not an extended-real trace value.

## Disposition

FAILED
