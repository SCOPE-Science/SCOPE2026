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

The proof of the unrestricted result is in `RESULT.md`; it uses finite Fourier invertibility, translation-cycle arithmetic and a constructive bijection. `CHECK.py` is a dependency-free, executable consistency checker. Run `python3 CHECK.py` from a directory containing this file. The expected result is `CHECK_OK exact_phase_arrays=39640 exhaustive_parameter_cases=32 constructive_parameter_cases=1734`.

The checker computes exact root-of-unity phase-exponent differences for cross-Gram cancellation, independently compares them with the half-cycle ratio criterion, exhaustively counts all windows in enumerated small cases, and checks explicit witness constructions through even lengths at most 34. It is not an exhaustive all-length certificate. The claim requires the written proof for arbitrary lengths and does not include unrelated time-frequency lattices or perturbation stability. No independent audit or external formal verification has been performed.
