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

# Reproduction notes

Use Python 3 standard library only: `python CHECK.py`. The script tests 847 exact rational pairs using integer iteration, compares against the derived parity-window criterion, checks the uniform phase bound, and verifies a rational tail-sum/expectation identity. Expected final output: `QUASI_AFFINE_NEAR_FLIP_LAW_OK: 847 exact integer-orbit cases`.

No enumeration is used to infer the general formula. The proof in RESULT.md uses Hoseana's exact period-two classification, interval nesting, real-parameter counting bounds and measure calculations; it covers every admissible real parameter and all integer thresholds. An independent mathematical audit has not been performed.
