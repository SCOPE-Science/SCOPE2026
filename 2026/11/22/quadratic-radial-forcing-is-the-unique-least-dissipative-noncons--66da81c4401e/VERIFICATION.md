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

The standalone Python 3 script `checker.py` performs two exact-rational calculations of stationary entropy production for polynomial examples of the stated smooth radial SDE. The first evaluates the proposed Laguerre spectral formula. The second independently applies stationary raw moment equations for \(Z S^k\) and computes the entropy rate from the stationary force–axial covariance. Both routes agree for rational \(\eta\) values \(1/3,1,2,7/2,11\), pure Laguerre forces through degree six, and several mixed-degree cases. Sharp gap equality and strict upper bound are separately checked. The test completed with 189 exact rational assertions.

These finite checks confirm algebra and normalization on tested finite-dimensional examples. The theorem for arbitrary finite polynomial degree follows from the exact reversible radial Ornstein–Uhlenbeck spectral decomposition, bounded spectral multiplier, and monotonicity of Laguerre weights; neither simulations nor finite samples are used as proof of the infinite statement. The physical beam-force interpretation is idealized; no experimental verification or independent scientific audit has been performed.
