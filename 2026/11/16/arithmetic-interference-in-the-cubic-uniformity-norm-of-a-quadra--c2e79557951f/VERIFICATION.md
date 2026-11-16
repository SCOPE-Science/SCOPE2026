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

# Reproducibility and scientific limits

Run `python3 check.py` from the same directory as this file using Python 3 standard library only. It computes every integer entry of all 256 four-by-four signed cube matrices, all exact principal determinants, and the rank-discriminant histogram. It then independently calculates the normalized 8-factor cube average over complete finite spaces for seven pairs of prime characteristic and dimension, comparing against the displayed general formula. These finite brute-force checks test selected small cases; they are not a substitute for the exact integer table and the general quadratic Gauss-sum theorem in `RESULT.md`.

The exact certificate proves every integer rank and discriminant count with no external data or precalculated table. Because every maximal nonzero principal minor equals a signed power of two, the rank table is valid modulo every odd prime. The rest of the argument uses a standard quadratic Gauss identity and an elementary strict polynomial sign comparison. The originality comparison remains limited to cited inspected passages and performed literature searches, and independent mathematical evaluation has not been performed.
