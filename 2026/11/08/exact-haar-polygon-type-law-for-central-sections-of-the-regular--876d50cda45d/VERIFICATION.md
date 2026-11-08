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

# Checks and limitations

Run `python3 trunc_icosa_exact_certificate.py` using the standard Python library. Expected lead marker: `EXACT_CERTIFICATE_OK`. The certificate constructs 12 original icosahedron vertices, 30 edges, 20 triangular faces, 60 truncated vertices and 90 truncated edges. The icosahedral spherical symmetry chamber has 7 active great circles; 128 sign patterns are examined by exact ring arithmetic, yielding exactly 12 positive-area cells with polygon side counts and cell multiplicities reported in `RESULT.md`. Its exact sign arithmetic avoids floating-point misclassification. The normalized cell areas are evaluated with ordinary floating-point `atan2` functions and checked numerically to total the exact chamber area \(\pi/30\).

Run `python3 trunc_icosa_independent_check.py` with NumPy and SciPy available. Expected marker: `INDEPENDENT_CHECK_OK`. This verifies 250000 uniformly distributed direction samples against the computed law using a five-standard-error threshold for each type and separately compares 100 direct planar convex hulls with the combinatorial crossing count. Fixed pseudorandom seed 72936 makes the output reproducible.

The two verifiers are not external certification; simulations alone do not prove the law. Mathematical exactness is supplied by the exhaustive sign-cone construction together with an explicit finite spherical-triangle formula. The probabilities printed to 14 decimal places are numerical evaluations and not interval-certified last digits. No independent audit is claimed.
