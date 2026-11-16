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

# Verification and reproducibility

Run `python verify_two_equators.py` and `python verify_resonant_splitting.py` with ordinary scientific-Python dependencies as imported within each script. Both files are complete and self-contained, with no other project dependencies. The first checks 200 finite Laplacian/harmonic-restriction and exact-nullity comparisons. The second independently integrates a degree-three four-dimensional harmonic Gram matrix and compares its two rational resonances with quadratic eigenvalue splitting. Both completed with PASS outputs. No finite test is represented as a proof of the infinite-dimensional statement; the analytical argument is in RESULT.md.

There is no independent external mathematical validation. The priority assessment uses full readable primary texts for the 2022 harmonic reconstruction and 2023 Fourier uniqueness-pair references, and published summaries only for narrower specialist two-equator and meridian results. Such summaries cannot exclude equivalent results in uninspected full articles.
