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

The all-length support and sharp minimum use the orbit-congruence argument and an explicit two-frequency character evaluation in RESULT.md. They do not rely on numerical extrapolation.

For the finite first-divergence result, two independent exact-integer approaches were run: `check_fourier.py` enumerates rim colourings and applies tensor character transforms using integer real and imaginary arrays; `check_transfer.cpp` computes the character sums via three-state Gaussian-integer transfer traces. Both return equal histograms for three, four, and five rim vertices, and the same unequal histogram at six. Both also verify nonvanishing and minimum reduced magnitude two within their finite test ranges. At six rim vertices every one of the \(4096\) reduced Fourier frequencies is examined for each group. No independent audit was undertaken.
