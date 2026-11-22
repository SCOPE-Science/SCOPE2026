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

# Reproducibility and verification

The mathematical argument is in RESULT.md. `check_central_trinomial.py` uses only Python's standard library and exact integers; run `python3 check_central_trinomial.py`. It tests the recurrence and constant-term sum, the modulo-five digit law, unit image through modulus 125, finite samples of the Pan--Sun dilation theorem, valid separated-support products, and primitive-root finite orders. The published theorem itself and the infinite support-separation construction are not certified by finite tests.
