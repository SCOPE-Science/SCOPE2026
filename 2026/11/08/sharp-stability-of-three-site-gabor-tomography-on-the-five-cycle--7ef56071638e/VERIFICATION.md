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

The deterministic checker `CHECK.py` computes the full 25-by-25 Gabor lifting singular spectrum independently of the ambiguity formula, verifies all ten representative equality cases, and tests 180 nonsymmetric random coefficient patterns and off-grid phases. It returned `THREE_SITE_GABOR_CHECKS_PASSED 5259` using Python and NumPy.

The global inequality and equality classification are symbolic arguments, not consequences of finite trials. The five-cycle affine-support census in the checker is exhaustive (all ten three-element supports); the floating-point checks of continuous weights and phases are not exhaustive. The 2026 motivating preprint was available in abstract form, not as complete inspected full text. Independent mathematical auditing has not been performed.
