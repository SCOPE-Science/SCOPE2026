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

# Verification notes

The standalone `check.py` requires Python, NumPy and SciPy (see `requirements.txt`). Run `python check.py` from the extracted package directory. The checker calculates the product-sphere tangent Gram determinant from derivatives of the four normalized sphere points (expecting \(2048/243\)), verifies the face-distance linear terms \(8L_i/27\) and the diagonal quadratic loss \(2Q/9\), and checks the exact angular-to-cosine normalization of \(16\sqrt3/\pi\).

It then samples shape coordinates in a bounded five-dimensional box using a fixed-seed scrambled Sobol sequence and **computes the true tetrahedron facet planes** from four perturbed unit vectors, without imposing the asymptotic linearized inequalities as the event. The measured actual-to-predicted leading local-volume ratios for angular excesses \(0.04\), \(0.02\), \(0.01\), \(0.005\) were approximately \(1.098875\), \(1.045508\), \(1.020037\), \(1.008212\), respectively. The executable returned `FOUR_RANDOM_CAPS_TETRAHEDRAL_QUARTIC_ONSET_OK`.

The checker tests finite configurations and is not a proof of the infinite limit. The full proof is the regular-tetrahedron localization, explicit Taylor expansion, five-dimensional integral, orientation-orbit count, and Haar-normalized Jacobian in `RESULT.md`. An independent audit has not been performed.
