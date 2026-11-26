---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Take the Schur complement of the unit middle entry of the Hermitian Toeplitz matrix. The remaining 2×2 matrix has both diagonal entries 1−|z|² and off-diagonal w−z² up to conjugation, so its positive semidefiniteness is exactly the disk-fiber criterion. Put t=|z|² in the proposed inner ellipsoid. On 0≤t≤1/3 the squared deficit (1−2t)²−(8/9)(1−3t)=(2t−1/3)² certifies containment because 1−2t is positive there. Equality requires t=1/6, saturation of the transverse radius, and exactly the phase opposite to z²; these conditions also suffice for both boundaries. After affine normalization, the five contact vectors (e^{2πij/5},−e^{4πij/5})/sqrt(2) have zero sum and Gram entries −1/4 off the diagonal, or equivalently second moment I_4/4. This positive John certificate is valid against unrestricted centers and orientations. The outer ball contains the hull by strict convexity and shares only its generators; their normalized covariance is again I_4/4 and mean zero, proving unrestricted Löwner optimality. Integration of π(1−|z|²)² over the disk gives π²/3; multiplying the four-ball volume π²/2 by the semiaxis products gives 4π²/27 and 2π², respectively, and the stated ratios. The exact square identity and finite moment certificate are analytic proofs, not the random checks in the uploaded script.

## originality

PASS

The verified distinct contribution is the complete four-dimensional inner ellipsoid and its contact circle and fraction. The Toeplitz/co-orbitope representation and the Löwner ball are already covered; the cited polar result does not give the inner ellipsoid of the original body. The strongest distinct catalogue summary treats a proper projection, not the same optimum.

## value

PASS

This is the smallest universal trigonometric orbitope with distinct first and second harmonic planes, and its metric normalization matters independently of the known membership and face descriptions. The complete harmonic equality locus and affine-invariant fraction 4/9 quantify a specific anisotropy not indicated by the round enclosing ellipsoid. The contact certificate gives a reusable exact model for this natural noncentrally symmetric body; the contribution does not rest on recalculating the known outer ball.

The dated certificate retains the supplied scientific assessment, sources and limitations.
