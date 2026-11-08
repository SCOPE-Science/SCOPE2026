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

The finite checker `checker.py` runs from the package directory, using standard Python and, if installed, NumPy and SciPy for an independently formulated linear-programming cross-check. It enumerates every atom of each finite test law, verifies nonnegativity, marginal and proper-subset product moments, matches exact risk differences, verifies the sign of mixed log-sum-exp differences and tests the explicit common-bin-width formula. The recorded run returned `PASS 4283 checks`, including `scipy LP cross-checks: 100` and the finite illustrative gain `0.25014236686591174` nats at three fair Bernoulli bits and width four.

The analytic derivation in `RESULT.md`, not finite enumeration, proves the statement for all integers \(n\ge3\) and all permitted inputs. No independent mathematical audit or external validation has been performed.
