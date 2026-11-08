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

The complete source for the finite checker is `scripts/verify.py`; its actual successful replay output is `verification/output.txt`. Run with Python 3 standard library using `python scripts/verify.py`. It exhaustively computes all rational points and lines of the reduced quadric over the binary field and counts the quadric over the quartic field. The infinite field-extension assertion follows from the linear-algebra and quadratic-form proof in `RESULT.md`, not from this enumeration. The primitive coefficient identity and saturated line-family definition are proved symbolically in `RESULT.md`. Independent audit has not been performed.
