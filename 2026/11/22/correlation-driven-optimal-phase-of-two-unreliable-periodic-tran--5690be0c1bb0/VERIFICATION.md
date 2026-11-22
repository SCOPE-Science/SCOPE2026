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

# Verification and limits

The elementary proof in `RESULT.md` derives the recurrence and integrates the next-success waiting time for every feasible real joint Bernoulli distribution, followed by a strict convexity calculation. The convergence of the recurrence uses \(h=1-p-q+r<1\).

Execute `python3 verify.py` using the standard Python 3 library. The replay output is `PASS: 15510 diagnostics (exact rational checks plus supplementary simulations).` The checker compares independently coded rational formulas, tests a grid of feasible correlations and offsets, verifies the exact boundary example, and includes seeded squared-gap simulations as a supplementary independent representation of mean residual waiting.

The diagnostics are finite and do not establish the universal theorem by enumeration. No field data, real-time service reliability estimates, or independent audit is claimed. The result's range is limited to labeled, independent cycles with a fixed within-pair joint operating law, even if the two scheduled times coincide across a cycle boundary.
