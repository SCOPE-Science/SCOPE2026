---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The projector onto the power-sketch columns Y=[kappa^{2q+1}g;H] has P_11=kappa^{4q+2}gamma/(1+kappa^{4q+2}gamma), gamma=g(H^TH)^{-1}g^T. Orthogonal regression identifies gamma distributed as chi²_k/chi²_{d-k}, independent, for all 1<=k<d. The Frobenius trace identity yields the full excess distribution and beta integral; Euler integration produces hypergeometric expectation. For fixed dimension and k, t→∞ beta endpoint dominated convergence gives t^{-1/2} for k=1, (log t)/t for k=2 and t^{-1} times (d-k)/(k-2) for k>=3. Multiplying by kappa²-1 gives all coefficients, including d=2,k=1 and kappa=1. Independent numerical QR/chi-square beta integral checks corroborate; fixed d,k,q essential.

## originality

PASS

PASS with explicit credit for the prior one-column blowup. The all-width chi-square law, exact k=2 logarithmic borderline, and q-step sharp coefficients are non-implied by the inspected bound theorems.

## value

PASS

The Gaussian range finder is fundamental; its zero-oversampling small-sketch moments have a genuine finite-moment cutoff k=2 exactly where a reciprocal chi-square expectation changes integrability. Exact risk and power-count coefficients inform algorithm behavior on a natural spectral stress test and can be reused in benchmark analyses, not merely a tiny numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
