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

# Exact reproducibility checks

Run `python prism_walsh_verifier.py` with the Python standard library. The checker independently generates the prism edge sets and all perfect matchings for \(3\le n\le7\), computes full Walsh–Hadamard transforms over \(2^{3n}\) edge characters, and compares exact minimal positive amplitudes and zero existence to the theorem.

Observed matching counts for lengths \(3,4,5,6,7\): `4, 9, 11, 20, 29`. Observed zero-frequency counts: `192, 0, 0, 124928, 0`. Observed least positive magnitudes: `2, 1, 1, 4, 1`. All four six-site identity words, the six sharpness seed words, both zero seed words, signed transfer formula and six-site extension passed direct integer tests. All \(2^{2n}\) prescribed sign assignments at the zero seeds for \(n=3,6\) were individually checked. Witness propagation was checked through length \(201\).

Successful run ends with the exact output marker `PRISM_WALSH_EXACT_TESTS_PASS`. The universal statement depends on the written transfer/number-theoretic argument, not on the finite tests. Neither the current package nor its checks constitutes an independent mathematical audit.
