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

# Verification

The proof in RESULT.md reconstructs the original affine map, computes the base-departure probability, derives the renewal generating function and exact maximum distribution, and establishes the two distinct parameter windows analytically.

Run `python3 verify_excursions.py` using the Python standard library. This separately implements exact rational Markov propagation and exact rational finite-height absorbing-state equations. Expected terminal marker: `SPACE_TIME_EXCURSION_VERIFICATION_OK`. Tests include \(\lambda\in\{1/3,1/2,3/5,3/4\}\), return steps \(1\) through \(9\), barriers through \(7\), and checks of the two windows at \(N=L=20000\). Finite checks cannot independently certify the infinite assertions or literature novelty. No independent mathematical audit has been performed.
