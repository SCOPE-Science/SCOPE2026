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

# Reproducibility and scope

Run `python verify_square_norm.py` using standard Python. The terminal marker is `DYADIC_SQUARE_WIENER_NORM_PASS`.

The checker constructs complete square-residue sets directly, implements an independent radix-two complex FFT, and verifies the cardinality recurrence, eight-frequency transform recurrence at every frequency, Parseval identity and sharp absolute Fourier norm for depths \(1\le k\le12\). It compares the depth-asymptotic coefficient and parity offsets against closed radicals, and tests the explicit bound on the two-step increments at additional depths. The stated all-depth results follow from the written proof rather than from finite enumeration. No independent assessment has been performed.
