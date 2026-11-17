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

# Reproducibility and verification

Execute `python CHECK.py` with Python 3 and SymPy installed in the directory containing `CHECK.py`. The script verifies symbolic third-order return expansions at both first-order zeros, the exact completed-square minimum, the resulting leading rotation-number coefficient at a representative parameter, and 80,000 sampled drift-sign comparisons across parameter regimes. In a completed run, all assertions passed.

Scientific proof does not rely on these finite tests. The all-parameter sign conclusions follow from definiteness of the local quadratic form and compactness away from its zeros. The sharp rotation-number law additionally requires a dominated-convergence argument and a discrete versus continuous passage-time estimate, both included in `RESULT.md`.

No test covers the excluded \(|c|=4a\) boundary. Historical priority and independent mathematical verification have not been established.
