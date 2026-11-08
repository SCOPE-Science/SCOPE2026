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

# Reproduction and limits

Run `python3 verify.py` with Python 3 (standard library only). The implementation enumerates the complete modular recurrence state cycle at each exponent from 1 to 14 and compares its value-image against the predicted three residue balls. It separately checks the two odd-index residue bijections at exponents 3 through 10 and the polynomial isometry on finite rings up to exponent 11. It never assumes that a partial index sample is exhaustive, because the independent state cycle test explicitly stops on the first repeated state and checks it is the original state.

The algebraic proof in RESULT.md, rather than this finite computation, proves the complete theorem at all exponents. No independent mathematical review or external certification has been performed.
