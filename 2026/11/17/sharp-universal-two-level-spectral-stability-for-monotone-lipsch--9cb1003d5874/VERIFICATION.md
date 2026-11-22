---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

At simple two-point spectra, Df is the Hermitian Schur multiplier with coefficients u,v,w∈[0,1], including complex off-diagonal phase. Convexity reduces the induced spectral norm to eight binary masks; all but (1,0,1)/(0,1,1) have gain ≤1. Extreme Hermitian unitaries yield max_{0≤s≤1}(s+√(4−3s²))/2=2/√3. Integrate derivative along Hermitian segment, mollify nonsmooth monotone f and use positive-part perturbations near diag(1,−ε) for sharpness. L=0 and repeated eigenvalues covered.

## originality

PASS

The exact spectral operator-norm universal coefficient 2/√3 for every monotone real scalar Lipschitz function on complex Hermitian 2×2 matrices is not implied by earlier full-text Resultary results using entrywise maximum and independent-coordinate norms, or by the sharp Frobenius estimate in Carlsson. Divided-difference Schur multipliers are known ingredients, but the induced two-level spectral norm, all-functions bound and fixed positive-part sharpness remain distinct in inspected statements.

## value

PASS

A sharp, natural dimension-two spectral stability coefficient for the whole monotone Lipschitz functional calculus quantifies real amplification missed by scalar and Frobenius contraction, with a fixed positive-part sharpness family. It is a reusable norm-geometry boundary rather than a coordinate norm recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
