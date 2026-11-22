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

# Reproduction and limits

The primary mathematical proof is in `RESULT.md`. The package also contains `checker.py`, a Python 3 standard-library script. Run it in the same directory with `python3 checker.py`; the observed output for this package was `STADIUM_TRIANGLE_COVERING_CHECKS_OK cases=10 random_triangles=60000 hex_samples=9000`.

The checker evaluates the unique quadratic root, determinant of the explicit maximizing triangle and lattice, the exact circle limit, monotone derivative, 60,000 independent randomly generated contained triangles, and 9,000 random points in the lattice's translated hexagon covering. These are reproducibility diagnostics, not an exhaustive proof. The continuum argument uses the sharp disk-chord bound and classical planar Bambah–Rogers covering theorem, which is stated in Kallus's full text. Neither the global proof nor originality has been independently audited.
