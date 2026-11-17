---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For upper-triangular invertible matrices over F_{2^s}, rescaling each coordinate transforms idempotence into Artin-Schreier equations y_j^2+y_j=sum_{i<j}b_ij y_i^2. Frobenius linearity and the nondegenerate absolute trace pairing show each new uniform coefficient row induces a uniform binary linear functional on the existing F_2 solution space of dimension d. It is zero with probability 2^{-d}, so the solution dimension increases to d+1, otherwise stays d. Thus K_n=2^{D_n}-1 and transition probabilities are independent of field extension degree. Conditional moments produce E K_n=n and Var K_n=n(n-1)/2; all-increase and never-increase paths give the two exact extreme atoms. Independent rational Markov calculations verified distributions and moments through n=9; these corroborate rather than prove all n and all s.

## originality

PASS

Field-size-universal random triangular evolution-algebra idempotent distribution: best-of-knowledge comparison of exact mathematical statements and their logical implications found no dominating prior result for the specified original parameter range. Previously published general and overlapping special-case results are explicitly credited. Novelty is not inferred from an unsuccessful search; see named comparisons and residual access risks.

## value

PASS

The full rational-idempotent-count distribution for a natural upper-triangular ensemble, independent of extension field size despite genuinely nonlinear multiplication equations, is a useful exact benchmark for random evolution algebras and finite-field random semilinear maps; exact mean, variance and rare-event atoms supplement the distribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
