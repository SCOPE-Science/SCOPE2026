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

# Reproducibility and boundaries

`CHECK.py` needs Python 3 and its standard library only. From the directory containing it, run `python CHECK.py`.

The exact arithmetic checks reconstruct all fiber-sum incidence matrices for nonempty offset sets of sizes at most four over the fields of orders 3, 5, 7 and 9, verify their ranks using rational Gaussian elimination, and separately construct the corresponding Fourier matrices and check their numerical ranks. Over the extension field of order 9, every five-column submatrix for a two-view configuration has full rank, while two disjoint three-point cosets yield the same measurements.

Expected result: `CHECK_OK exact_incidence_rank_cases=[(3, 7), (5, 30), (7, 98), (9, 255)]`.

This finite check does not certify the infinite family. The universal proof is the exact Fourier-inversion, reflection-composition and quotient-orbit argument in `RESULT.md`. Floating-point Fourier ranks are only an separate numerical corroboration of the exact rational incidence computations. Independent validation has not been performed.
