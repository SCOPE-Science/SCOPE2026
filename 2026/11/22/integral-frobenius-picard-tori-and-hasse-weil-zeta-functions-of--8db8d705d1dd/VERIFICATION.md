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

# Reproducibility and limits

Run `python3 verify.py` with Python 3 and no third-party packages. This recomputes 220 determinants over the Eisenstein integers, the 21-point incidence lattice and 60 flags, Frobenius-fixed counts, the integral involution on a 28-cycle basis, and exhaustive small-prime point counts. Expected final certificate: `HESSE_ARITHMETIC_PICARD_TORUS_OK`.

The detector establishes stable incidence away from characteristic three because every nonzero determinant norm is a power of three. The code proves exact fixed-model finite incidence and integral-module inputs; the attached proof derives the infinite finite-field and scheme-theoretic conclusions. The checker does not compute Picard schemes directly, does not verify unrelated forms of the pencil, and does not provide external or independent certification.
