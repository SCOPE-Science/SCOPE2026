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
# Verification

The accepted theorem is the rank-at-least-three variable-block local-singularity and Gorenstein classification in `RESULT.md`.

The exact-arithmetic file `CHECK.py` was executed with Python 3. It checked the parameterized Pluecker ratio exponents against expressions in chart generators for five block-size profiles at each of ranks \(r=3,4,5\); it verified rank-one minor monomial identities and the Segre-degree formula by finite differences. It ended with the exact terminal line `ALL_EXACT_CHART_CHECKS_OK`.

The checker is not an exhaustive proof over all parameter tuples and does not prove the determinantal toric ideal theorem or the class-group computation. Those are the non-computational steps in the written proof. Independent mathematical audit has not been performed. The literature search is not a proof of novelty.
