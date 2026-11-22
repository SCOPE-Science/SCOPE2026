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

The self-contained `verify.py` script uses Python 3 standard library only. It exhaustively compares the predicted simple-permutation equality criterion for every permutation of lengths one through eight (40320 diagrams at length eight). It checks the complete external-trace maximum sequence \(2,4,8,15,24,35,48,63\), the exact non-simple maxima at lengths four through eight \(14,23,34,47,62\), and the number of extremal representations \(2,6,46,338,2926\) at those sizes. An independently coded segment-crossing test is applied at all cut pairs through four marked vertices. Explicit simple and non-simple construction series are checked through thirty marks.

The actual checker, extracted from the same package as this document, was run successfully; output ends with `VERIFY_OK`. The computations are finite checks, not a certificate of the infinite theorem. The full proof, including case splits for common intervals and the sharp non-simple construction, is in `RESULT.md`. No independent audit has been performed.
