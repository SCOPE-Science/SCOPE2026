---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1,
  "record_status": "passed"
}
---
# Verification and scope

The parity and star argument in `RESULT.md` proves the splitting including the empty attaching complex. As a separate arithmetic check for the double \(K_6\) example, weight a face of cardinality \(k\) by \(x^k\), including weight 1 for the empty face. The face polynomial is
\[
(1+15x+45x^2+15x^3)^2+(2x+x^2)(1+6x+3x^2)^2.
\]
The second term counts the faces with at least one crossing edge and a punctured-side face. The positive-degree coefficients are \((32,340,1476,2589,1404,234)\), giving Euler characteristic \(-251\), in agreement with the wedge. This is an enumeration check, not a proof of the integral homotopy type in place of the collapses and splitting.
