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

# Verification of the finite-jet theorem

Run `python3 CHECK.py` with Python 3 standard-library modules only. The checker computes \(c_2\) and \(c_4\) by independently integrating \((x-y)^2\) and \((x-y)^4\) over the product of two intervals using exact rational arithmetic. It compares these with the closed Taylor identities and verifies the exact radical inverse, the attainable-jet inequality and the equal-length equality case on 216 rational configurations. It separately checks direct finite-frequency Fourier intensities and displays a two-parameter order-two ambiguity fiber. The recorded execution returned `FINITE_JET_INTENSITY_CHECKS_PASSED 1315`.

The proof is the displayed analytic factorization, coefficient calculation, unique positive quadratic root and strict derivative sign, not the finite test sample. All interval lengths and gaps are real and strictly positive. There is no claim about noise amplification of derivative estimates, global three-interval phase retrieval, external certification, or independent mathematical review.
