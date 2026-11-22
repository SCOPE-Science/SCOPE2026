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

# Verification and limits

The accompanying pure-Python program `check_return.py` independently enumerates axis-selection probabilities by dynamic programming and combines them with one-dimensional central-binomial return weights. The actual command `python check_return.py` passed 16 checks, including an exact binomial identity in the independent-heading specialization, direct comparisons at several fixed nonzero nematic parameters and a numerical check of the critical second-order coefficient.

The analytic proof does not depend on these finite experiments. It uses the exact two-by-two tilted transition matrix, the two Fourier saddle points required by lattice parity, sixth-order Taylor expansion of the leading eigenvalue and fourth-order expansion of its amplitude, and Gaussian moment integration to order two beyond the leading local limit. The statement assumes a fixed nematic parameter strictly between minus one and one; no estimate uniform at the endpoints or numerical inference under noise is claimed. Independent audit has not been performed.
