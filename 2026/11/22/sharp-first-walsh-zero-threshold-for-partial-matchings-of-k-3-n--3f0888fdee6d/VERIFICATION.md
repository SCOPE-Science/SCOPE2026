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

Exact reproducibility with Python 3 standard library: run `python3 verify_walsh.py` and `python3 verify_structural.py` alongside this file. The first independently constructs the incidence indicator of **all** partial matchings of \(K_{3,n}\), transforms it with a Walsh–Hadamard butterfly, checks complete Fourier spaces at widths three through seven, and verifies every constructed first-degree witness. The second sums signed assignments of distinct columns to occupied rows without any Fourier transform for every width three through twenty-three; it checks the positive boundary values and the cancelling two-row witness. Both scripts completed with their stated final success markers.

The proof in `RESULT.md`, not the limited computations, establishes the parity and exact zero-degree results for arbitrary width. No external or independent audit has occurred.
