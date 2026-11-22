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

The analytic proof is in `RESULT.md`. In the same extracted directory, execute `python verifier.py`; `verifier_output.txt` records one successful run. SymPy expands the two-step rational Cayley product, its numerator and denominator square moduli, the strictly convex reduction, and the equal-step boundary identity. Numerical checks compare direct complex amplification values to the analytic optimizer for 97,200 sampled choices, test boundary cases and the stiff asymptotics, and include a pure-decay exact extinction example.

Only analytic identities and strict convexity establish global minimization. The finite checks neither establish global coverage nor independent mathematical validation. No calculations involving nonnormal matrices or physical-time error are included.
