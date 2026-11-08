---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility

Run `python3 verify.py` in a directory containing the supplied verifier file. The code uses only Python's standard library and carries out exhaustive exact-rational enumeration of the oriented rooted forests on \(K_{1,k}\) for \(1\le k\le8\) and the six parameter values listed in code. It verifies the normalization, the first and second moments, the control covariance, and the variance-optimal step. The recorded output contains `VERIFIED exact rational assertions: 429`.

The finite enumeration is **not** an exhaustive verification of the theorem's unbounded parameters. The paper's explicit two-case combinatorial decomposition, symbolic binomial-moment algebra and rational asymptotic limit provide the all-parameter proof. The computed witness at \(q=100\), \(k=10000\) has heuristic-to-raw variance ratio about \(0.95137244\) and optimal-to-raw ratio about \(0.48753967\), consistent with the proved limits, not their justification.

No independent audit has been performed. No floating-point sampling simulation or external mathematics certificate is claimed.
