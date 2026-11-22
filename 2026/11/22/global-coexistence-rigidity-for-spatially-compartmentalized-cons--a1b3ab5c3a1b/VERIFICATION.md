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

# Verification and boundaries

An independent exact-rational implementation of the multi-nutrient vector field and entropy derivative is provided in `verify_global.py`. It builds a positive equilibrium by fixing rational biomasses, nutrients, uptake and isolation and solving the positive local balance, mortality and input relations. The equilibrium balance was checked exactly. Seven hundred nontrivial, independently generated positive rational states were evaluated, and in all cases the direct derivative equals the claimed negative-sum rational expression exactly and is negative. The source proof also underwent a separate symbolic single-species, single-nutrient identity check with an expanded residual of zero. The human-readable algebraic proof supplies the universal argument: the checks cannot establish it by themselves.

The theorem requires a positive equilibrium and fixed positive species isolation. A boundary equilibrium, time-varying environment, or local isolation of zero is outside its hypotheses. The polynomial sum-of-squares identity, positivity of its factors and LaSalle's invariant-set check are essential. Independent audit is not performed; literature priority is limited to the inspected works and retrieved records.
