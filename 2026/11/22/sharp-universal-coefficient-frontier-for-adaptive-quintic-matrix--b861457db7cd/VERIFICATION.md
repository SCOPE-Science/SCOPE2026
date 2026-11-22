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

Run `python verify.py` using Python 3 and SymPy. The bundled exact-symbolic checks test the residual recurrence factors, derivative, endpoint root polynomial and invariant-interval positive identity. A rational scalar counterexample with coefficient \(3/2\) checks the strict crossing of its negative fixed-point barrier. A finite rational grid and a varying-coefficient three-mode experiment offer independent diagnostics but cannot establish the theorem's infinite-time or all-parameter statements; the accompanying analytic proof carries those claims.

The package's standalone checker was extracted into the working test directory and executed with output `VERIFY_OK assertions=1651 critical_cap=1.47222926097203`. Independent mathematical review was not performed. The numerical simulations are carried out in ordinary finite precision and are not claimed to certify floating-point stability.
