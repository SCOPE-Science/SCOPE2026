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

# Verification scope
The analytical argument in `RESULT.md` covers all admissible disks and all \(p>-1\). The only new positive range requiring proof is \(0<p<1\); the known \(p\ge1\) range is cited as established. The negative obstruction is analytic and uses \(p\in(-1,0)\).

`verify.py` (Python 3 standard library only) evaluates boundary integrals and the derivative bounds independently with periodic midpoint quadrature. The reference run passed 593 assertions, including 420 nested-disk samples and near-tangency negative diagnostics. Run `python verify.py` for the same deterministic tests. Finite quadrature and numerical differences do not certify infinitely many parameters, and the earlier mathematical notes are not independently re-audited.
