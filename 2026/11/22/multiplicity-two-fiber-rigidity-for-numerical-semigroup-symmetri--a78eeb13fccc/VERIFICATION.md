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

# Verification record

The proof is the unrestricted argument in RESULT.md, Steps 1–5. The standalone checker is `verify.py`; `VERIFY_OUTPUT.txt` contains the exact output of its execution from this package. Run `python3 verify.py` under Python 3. It exhausts sources of Frobenius number at most 20 and checks the original-pseudo-Frobenius deletion, target symmetry, all three inverse-fiber cases, and direct gap-coordinate indexing.

The exhaustive finite experiment does not prove the infinite statement. No independent review, expert review, formal proof certification, or external validation was performed.
