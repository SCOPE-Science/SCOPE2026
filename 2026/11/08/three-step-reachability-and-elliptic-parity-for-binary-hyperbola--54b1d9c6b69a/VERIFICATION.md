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

The finite-field verification was run as `python3 check_binary_hyperbola_3step.py` and returned `BINARY_HYPERBOLA_THREE_STEP_EXACT_CHECKS_PASS`. It exhaustively enumerates ordered triples in binary fields with \(q=2,4,8,16,32\), checks the stated support cardinalities \(1,4,42,256,1023\), and independently counts the Artin–Schreier fibers. The finite computation proves only these field instances. The general proof uses the two-pole genus formula and Hasse bound; all infinite-family deductions are checked algebraically in RESULT.md. Independent audit has not been performed.

