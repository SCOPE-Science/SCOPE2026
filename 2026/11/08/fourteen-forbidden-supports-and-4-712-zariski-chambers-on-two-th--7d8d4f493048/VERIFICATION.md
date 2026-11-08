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
# Reproducibility

The package contains `verification/verify.py` and `verification/output.txt`. Execute `python3 verification/verify.py`. Only Python's standard library is required.

The program constructs all \(13\) curves with self-intersections \(-2\) (fiber components) and \(-1\) (sections), and all \(15\) nonzero pairwise intersections. Every one of the \(2^{13}=8192\) principal submatrices is tested for negative definiteness by two independent exact-arithmetic methods (rational Schur/\(LDL^T\) and integer Bareiss determinants). For all cases the result coincides with avoidance of the \(14\) stated forbidden supports. The program also computes the inclusion-minimal failing sets directly, checks their singular determinants and every one-point deletion, and recomputes coefficients using inclusion--exclusion over \(2^{14}\) selections. Its final line is `ALL_CHECKS_PASSED`.

**Scope of evidence:** The program proves the finite intersection-matrix assertion by exhaustive enumeration, assuming the geometric identification of that matrix. The geometric input is established independently by adjunction, Kodaira fiber incidence, torsion specialization and the published Miranda--Persson classification. This is not an experimental extrapolation to unspecified surfaces. An independent scientific audit has not been performed.
