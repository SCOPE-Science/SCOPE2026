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

# Reproducibility
Run `python3 artifacts/verify.py` with a standard Python 3 interpreter from the extracted package root. Expected output is `CUBIC_STABILITY_EXACT_AND_CURVATURE_PASS cases=175 primes=5 bands=6 extension_fields=1`.

The checker independently constructs cubic-convolution fibers and computes their integer Gaussian arithmetic energy for 175 deterministic pseudo-random coefficient arrays in prime fields of orders \(5,7,11,13,17\). It additionally checks 15 exact cubic-collision arrays over the quadratic extension field of order \(25\), then compares these values to the stated rational coefficient and decomposed deficit, tests nonnegativity and the sharp one-site imbalance example, and probes the six radial, phase-symmetry, and positive quadratic sectors numerically. No finite enumeration is represented as an infinite-field proof. The proof in RESULT.md establishes the claims in every allowed characteristic, including extension fields.

The self-review passed; independent audit was not performed. The source-comparison record is in AUDIT.json, with remaining historical-priority risks documented there.
