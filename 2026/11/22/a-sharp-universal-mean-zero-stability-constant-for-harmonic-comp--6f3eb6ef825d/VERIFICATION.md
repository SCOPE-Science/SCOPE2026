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

# Verification evidence

The analytic proof in `RESULT.md` is the basis for every infinite-dimensional assertion. The separate `check_face_spectrum.py` uses a direct full-cube grounded Dirichlet-matrix solve, not the resolvent basis derived in the proof, and compares its Walsh-conjugated Gram operator with the exact binomial formula.

Run `python3 check_face_spectrum.py` (requires NumPy). In this execution the checker printed: `PASS: 14 full Dirichlet matrix/Walsh spectral comparisons; max entry error 4.26e-14` and `PASS: rational universal maximum 3548/2883 and finite monotonicity checks`. The exact rational values for codimensions one through seven and the algebraic tail bound for all larger codimensions are independently stated in the mathematical proof; finite tests alone are not exhaustive verification.

The provenance of the July 15, 2026 motivating preprint is verified from its first-public arXiv metadata. Original full text was not accessible, and thus comparison beyond the abstract and a detailed technical synopsis is limited. Independent mathematical audit is not performed.
