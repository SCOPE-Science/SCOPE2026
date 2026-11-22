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

The attached `verify.py` was executed against its included source. It uses Python 3 with SymPy for exact symbolic elimination and rational matrix reconstruction. The exact-rational test constructs 1,728 RK4 end-step matrices independently from the claimed reduced formula and checks all entries, conservation and two-inequality equivalence. The remaining 30 rational checks cover representative symmetric-rate cases. SymPy confirms the resultant sextic, the two Bernstein sign certificates and the crossover root bracket. The observed program output is in `verify_output.txt`.

These computations do not prove all real rates or all steps, which are handled by the analytic identities and sign inequalities in `RESULT.md`. No independent audit was performed.
