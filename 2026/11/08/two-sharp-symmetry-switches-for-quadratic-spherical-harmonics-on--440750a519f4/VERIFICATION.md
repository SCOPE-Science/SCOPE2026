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

Run `python check_lune_spectrum.py` with NumPy version at least 1.24. The checker uses no downloaded data, and the only runtime dependency is named in `requirements.txt`. Its successful output is `LUNE_QUADRATIC_CUBATURE_CHECKS_PASS 656`.

The check constructs full global and lune Gram matrices in an unnormalized Cartesian quadratic basis, with a fourth-moment-exact transverse cubature and an exact degree-two radial rule. It uses angular Gauss-Legendre quadrature and then solves the generalized eigenvalue problem numerically; the closed eigenvalues are compared only after computing the Gram spectrum. Dimensions \(3,4,5,6,8\), apertures \(0.3,0.75,1.3,1.8,2.5,3.0\), trace, bounds, top/bottom branches and both transition multiplicities are tested. The tolerance is \(2\times10^{-11}\) on eigenvalues.

The general proof does not rest on that finite experiment. It invokes exactly the beta radial moments through degree four, angular Fourier moments at orders zero, two and four, and orthogonality of transverse harmonic sectors; the two crossing equations are elementary strict comparisons. The checker does not establish priority, a complete census of past literature, arbitrary noise stability, or any result for higher harmonic degrees. Independent audit and external mathematical validation are not performed.
