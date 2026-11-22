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

The complete theorem and proof are given in `RESULT.md`. The standalone checker `check_neel_reset.py` uses Python 3 with NumPy and SciPy. Run `python check_neel_reset.py` from a directory containing the extracted script.

The script constructs from first principles a finite-state spin-flip-plus-global-reset generator for even rings of sizes 4, 6 and 8; it solves the stationary probability vector and compares every distinct-distance spin pair at each of five reset rates. It further checks roots and sign changes for multiple even ring sizes, exact infinite-chain first roots, the Lambert asymptotic regime, and the finite ring structure factor through independent discrete Fourier sums. The script completed 400 numerical assertion groups successfully in the reviewed execution.

Numerical agreement is supporting evidence, not a proof beyond tested finite sizes. Uniform validity for all positive rates and separations, the unique sign thresholds, strict finite-size order, and the infinite-volume Lambert scaling follow from the explicit recurrence, monotonicity and asymptotic arguments in `RESULT.md`. The result assumes strict zero temperature, synchronous Poisson resets, even rings or an infinite line, and fair independent phase selection at each reset for the zero-mean structure-factor interpretation.
