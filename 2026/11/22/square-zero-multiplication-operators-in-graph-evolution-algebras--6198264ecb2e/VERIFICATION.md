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

Run `python3 check_square_zero.py` (Python standard library, no third-party dependencies). It enumerates actual coordinate multipliers \(L_x\), checks \(L_x^2=0\) by matrix multiplication, computes ranks by elimination, and independently compares the resulting cycles' rank frequencies with the theorem. It also tests the support criterion on every labeled C4-free graph of the specified small sizes and verifies the C4 counterexample.

The recorded run checks 13 complete cycle/field cases, 613 labeled C4-free graphs, and 22,147 graph/coefficient-vector pairs. These finite tests cannot prove the unbounded assertions: those are established by the coefficient formula, unique two-walk argument, cyclic kernel recurrence and gap enumeration in RESULT.md. The computations cover prime fields only. Earlier equivalent statements could exist outside the inspected literature. No independent external validation was performed.
