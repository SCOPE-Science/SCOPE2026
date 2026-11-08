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

Run `python3 verify.py` in the package directory. The program uses only the standard library and checks every derivation of the four-dimensional algebra over the fields of orders two and four. It prints orbit-stratum counts, confirms the rank of every nonzero idempotent derivation, and evaluates the linearized idempotence equations at canonical representatives.

Expected results: for \(q=2\), the strata have sizes \((1,12,4,12)\), total \(29\); for \(q=4\), sizes \((1,80,16,240)\), total \(337\). The zero representative has tangent dimension zero and each nonzero representative has tangent dimension four. The program terminates with `ALL_TORAL_DERIVATION_CHECKS_PASS`.

The general proof is algebraic; these examples are not infinite certificates. Scheme smoothness follows from the explicit orbit and tangent calculations in `RESULT.md`, not from small-field enumeration. Historical novelty and independent expert assessment remain open.
