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
# Verification of the Fourier endpoint norm

The standalone standard-library `checker.py` calculates exact rational values in two independent ways: direct enumeration of all permutations on \(4\) through \(8\) letters, and the positive-part formula using exact inclusion-exclusion counts of permutations with no cycles of length one or two. They agree for each rank, with respective norms \(9/4\), \(3\), \(20/3\), \(10\), and \(4249/320\).

An independently constructed coefficient expansion of \(H(z)=e^{-z-z^2/2}F(z)\) agrees with the cumulative exact norm identity through \(n=15\). Weighted character statistics at each rank \(4\le n\le15\) satisfy exact total probability \(1\), first moment \(0\), and second moment \(1\). The terminal marker is `HOOK_SPECHT_EXACT_FOURIER_PROJECTION_CHECKS_PASS`.

The universal proof is the character trace identity, finite-group convolution norm identity, short-cycle enumeration, and the entire-function bound detailed in `RESULT.md`. The checker verifies examples rather than all infinitely many ranks. No independent validation is asserted.
