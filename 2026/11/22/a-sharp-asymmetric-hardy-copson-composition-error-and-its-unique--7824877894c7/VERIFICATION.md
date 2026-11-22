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

# Verification notes

The analytic proof in `RESULT.md` supplies the all-real-BV sharp inequality, the unique stationary-point and jump-support argument, and the exact reflection reduction.

The bundled `check_hardy_copson.py` was executed from its actual supplied file. It passed a 65-step bisection diagnostic for the unique root, 59 numerical comparisons of jump-response and direct nested averaging, and 65 separately generated signed multi-jump BV inequality tests. It verified the strict single-operator comparison and computed \(s_*=0.589195414987420\ldots\), \(C_*=0.410507498717943\ldots\). These finite numerical tests cannot establish the general BV inequality or historical novelty; the analytic proof supplies correctness.

Only the two unweighted normalized Hardy/Copson compositions on real BV(0,1) are claimed. Independent mathematical audit has not been performed.
