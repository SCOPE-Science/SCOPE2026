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
The proof calculates the frame operator directly from Gabor atoms, uses exact finite root-of-unity orthogonality, and diagonalizes the resulting full/one-missing residue blocks. The determinant and positivity checks use \(m,q\ge2\), \(z\ne0\), and the frame-eligible erasure condition. Separate off-diagonal equations classify tightness, including the unique minimally sampled four-dimensional exception.

The standalone `CHECK.py` uses NumPy to form the original complex Gabor atoms and the dense Hermitian frame matrix, independently diagonalizing with `numpy.linalg.eigvalsh`. It tests admissible and inadmissible erasure masks, compares every eigenvalue to the theorem, checks exact admissible-mask combinatorial counts, and tests the tightness endpoints. Executing `python CHECK.py` returned `ONE_DEFECT_SUBGROUP_ERASURE_CHECKS_PASSED 2830`.

These checks are finite spot/exhaustion tests in small dimensions; they do not prove the unrestricted theorem and cannot establish originality. No external independent mathematical audit or formal proof certification has been performed.
