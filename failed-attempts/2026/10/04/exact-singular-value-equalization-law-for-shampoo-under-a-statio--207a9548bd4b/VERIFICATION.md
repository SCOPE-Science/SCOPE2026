---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The stationary-gradient calculation is correct. The defining matrix Shampoo recurrence gives \(L_t=\varepsilon I+tGG^\top\), \(R_t=\varepsilon I+tG^\top G\). A reduced SVD of \(G\) diagonalizes both accumulators and yields \(s_i(P_t)=(t+\varepsilon/\sigma_i^2)^{-1/2}\). The submitted condition-number identity, target threshold, normalized polar limit and exact spectral-norm error follow from these scalars. The cumulative linear-loss statement follows from the standard asymptotic \(\sum_{t=1}^T(t+\tau)^{-1/2}=2\sqrt T+O(1)\). An independent symbolic check also reproduced the condition-number identity.

## originality

FAIL

The final claim is mechanically implied by the published Shampoo recurrence plus ordinary SVD functional calculus. Algorithm 1 already fixes the two additive Gram accumulators and the left/right inverse fourth-root update. Under the submitted assumption \(G_t=G\), summation and diagonalization immediately give every displayed finite-time singular value; the remaining equalization, threshold and polar-limit formulas are scalar algebra. Bernstein--Newhouse independently identify the semi-orthogonal polar direction as the spectral-norm steepest-descent direction associated with Shampoo when averaging is removed. The submitted stationary calculation is therefore a useful worked specialization, but under implication-based originality it is covered without needing the exact formulas to have been printed previously.

## value

FAIL

The stationary-gradient regime is a reasonable diagnostic, but the result is obtained by a textbook substitution into the defining recurrence followed by simultaneous SVD diagonalization. The threshold, delay and polar-error expressions do not require a new structural lemma, boundary phenomenon or classification beyond that scalarization. Under the common value bar, this is an informative worked calculation rather than a separately valuable mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
