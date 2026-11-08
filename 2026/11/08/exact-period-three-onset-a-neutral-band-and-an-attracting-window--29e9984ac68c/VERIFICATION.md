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

The exact piecewise formulas and four-branch period-three enumeration are proved in RESULT.md. For executable spot checks, run `python3 check_period_three.py` with standard Python 3. The checker independently searches every 3-step branch itinerary on a finite family of rational parameters and confirms the neutral-family algebra on finite sample values. It is neither exhaustive over real parameters nor an independent audit. At the critical algebraic parameter, the exact identity follows from the equation \(t_0^2(4-t_0)=3\), not the numerical tolerance checks. Stability at the nonsmooth branch collision and global entropy values remain unasserted.
