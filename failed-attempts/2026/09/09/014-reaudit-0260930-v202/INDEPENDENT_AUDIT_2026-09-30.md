---
audit_date: 2026-09-30
status: failed
---

# Independent mathematical audit

## Final claim

For two-qubit Werner states, under rank-1 qubit projective measurements in the stated Collins-Gisin normalization, the I3322 critical visibility is exactly 4/5, with maximal value -1+5v/4, so this restricted I3322 test is weaker than CHSH on the Werner line.

## Correctness — PASS

The optimization in RESULT.md was reconstructed. Eliminating Bob's Bloch vectors reduces the pure singlet part to a one-variable bound whose maximum is 5 at the stated planar configuration; an independent dense numerical check peaks at t approximately sqrt(3), and the exact identity in the package proves the bound. The affine Werner-state expression then gives threshold 4/5. The scope restriction to rank-1 qubit projectors is essential.

## Originality — FAIL

The core optimizer is already covered by Vidick and Wehner: their Theorem 1 proves that the maximally entangled state in every finite dimension has I3322 value at most 1/4, and notes that a single EPR pair attains 1/4. A rank-1 qubit projective strategy is a special case. For the Werner mixture in this normalization, the maximally mixed contribution is fixed, so the stated affine formula and visibility 4/5 are an immediate corollary rather than a new theorem.

### Equivalent formulations

Searches: I3322 maximally entangled state 1/4; Werner I3322 projective qubit threshold

Evidence: Vidick-Wehner, arXiv:1011.5206, Theorem 1: maximally entangled state value at most 1/4, attained by one EPR pair.; Collins-Gisin literature already gives the same qubit maximizer/settings numerically.

Reasoning: The package's qubit-projective pure-state optimum is contained in the prior all-dimension maximally-entangled bound.

### Broader coverage

Searches: I3322 maximally entangled all dimensions

Evidence: arXiv:1011.5206

Reasoning: Prior coverage is strictly broader in dimension and observables for the maximally entangled state.

### Exact database or table

Searches: Resultary Werner I3322 threshold 4/5

Evidence: Only the present published record appeared as a direct internal match.

Reasoning: Database absence cannot restore novelty against the primary theorem.

### Claim versus prior implication

Searches: Vidick Wehner I3322 EPR 1/4

Evidence: Theorem 1 plus affine mixing on the Werner line.

Reasoning: The prior 1/4 optimum mechanically implies the package's 4/5 visibility after the stated normalization is inserted.

## Value — FAIL

Although the exact proof is correct and compact, the final claim is a direct restricted corollary of a stronger published optimizer theorem. Re-proving that special case does not meet the value bar for a new mathematical finding.

## Sources inspected

- package RESULT.md
- artifacts/verify.py blob 20e9f1977a49f36f580a413373eeec9e7094b003
- https://arxiv.org/abs/1011.5206
- https://arxiv.org/abs/quant-ph/0306129

## Residual risk

The failure is scientific coverage, not a transport or access failure.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and value.
