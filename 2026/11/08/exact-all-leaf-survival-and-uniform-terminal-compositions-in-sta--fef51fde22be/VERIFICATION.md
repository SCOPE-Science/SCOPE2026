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
The claimed general formula follows from the exact productive-step transition kernel, pathwise equality of positive-state masses, and a bounded product martingale; all three arguments are given in `RESULT.md`. The finite absorbing chain is built independently in `proof_checker.py` and solved using exact SymPy rational arithmetic. Eight small \((r,n)\) cases were checked successfully, including four cases with \(r\ge3\). To reproduce: run `python proof_checker.py` in a Python environment with `sympy`.

The computations are finite cross-checks only. They do not certify infinite parameter ranges; that burden rests on the written proof. The result makes no claim about arbitrary opinion graphs, asymmetry, absorption time, or unrestricted extinction patterns. No independent external audit has been performed.
