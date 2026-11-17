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
# Reproducibility checks and boundaries

Execute `python3 verify.py` in the directory containing this document and the verifier. The checks evaluate \(I_j\) and \(J_j\) exactly as rational polynomials for rational taper parameters; separately integrate the slice and complete-boundary surface densities by Simpson quadrature; and test the sign trichotomy on both sides of the crossing for dimensions \(2\) through \(12\). They also confirm the exact planar formula, pyramid endpoints and the near-prism limit over that finite range. The scientific proof of the infinite-dimensional statements is provided separately in `RESULT.md`; finite tests are not substituted for it.

The package does not claim a complete historical priority census, uniqueness of an intermediate minimizer, or independent mathematical certification.
