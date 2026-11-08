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

# Reproducibility and limits

Run `python3 CHECK.py` with Python 3.9 or later. The self-contained checker uses only the standard library, computes the exact polynomial remainder with rational coefficients, and verifies 48,012 numerical instances of the fixed-gap leverage inequality and sharpness construction. The mathematical proof handles all positive gaps and all exterior real points, including the endpoint and coalescing-frequency boundary. A finite numerical scan is neither an infinite verification nor an exhaustive novelty search. The saved calculation does not establish originality or constitute independent review.
