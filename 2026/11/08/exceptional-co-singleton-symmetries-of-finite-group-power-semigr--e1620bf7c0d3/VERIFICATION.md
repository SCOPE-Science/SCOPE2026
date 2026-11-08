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

Run `python3 CHECK.py` with Python 3.8 or later and no third-party dependencies. The program uses exact setwise products (bit masks) for the groups specified in RESULT.md, and prints the expected counts and `VERIFY_OK` on success. `CHECK_OUTPUT.txt` contains the observed stdout. The proof for arbitrary finite groups is symbolic; the finite checks cannot certify its universal quantifier. The external independent audit has not been performed.
