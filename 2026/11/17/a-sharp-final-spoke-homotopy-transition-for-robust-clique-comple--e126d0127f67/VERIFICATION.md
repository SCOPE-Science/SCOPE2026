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
# Verification summary

The standalone `verify.py` independently constructs the graph edge set for each parameter configuration, enumerates each subset of vertices and every candidate independent \(k\)-subset, and constructs the complete chain complex. It reduces signed boundary matrices over two distinct finite fields, comparing all reduced Betti numbers to the theorem's formulas. The recorded output is `verification.json` and reports `PASS` for 41 parameter configurations in both characteristics \(2\) and \(3\).

These checks are exact for the listed finite instances but are not exhaustive over all integers and do not certify integral Smith invariants. The integral and infinite-family conclusions require the fully stated proof via the matroid independence-complex shelling and the nullhomotopic link attachment. The partial rank checks do not imply that arbitrary higher edge-deletion patterns behave similarly.
