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

The stationary mean is normalized by \(x_s=\sqrt{a/b}\) and the field by \(a x_s\). The analytic proof is in `RESULT.md`, including all parameter domains and the domination/squeeze estimates for the limiting regimes. Run `python checker.py` for 31 independent numerical consistency checks using SciPy; the output is `PASS: 31 numerical/asymptotic consistency checks`. The checker is not a proof of limiting statements. The beta-integral constant and the critical crossover were also derived directly from the hitting-time integral. No independent scientific audit has been performed.
