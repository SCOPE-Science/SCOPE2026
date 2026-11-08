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

Run `python3 verify.py` with Python 3 and no external packages. The checker independently constructs five-run binary words, enumerates all distinct substrings including the empty substring, and checks closedness by testing whether a proper border has exactly two occurrences. The program checks 3125 parameter tuples with every run length at most five, 160 deterministic pseudorandom tuples with lengths at most thirteen, and 24 members of the extremal construction. For lengths 5 through 17, it also enumerates all positive five-part compositions and compares their exact formula values with the documented finite maxima. Expected successful output begins `VERIFY_OK`.

The computations do not certify infinitely many parameters. The proof in `RESULT.md` separately classifies all possible border forms and proves the asymptotic inequality for all positive run lengths. This review has not been independently audited.
