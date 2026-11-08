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

Run `python3 check_commutator.py` with a standard Python 3 installation; it uses only the standard library. Its checks include exhaustive centralizer-rank enumeration on \(M_3(\mathbb F_2)\) and \(M_3(\mathbb F_3)\), direct character-sum comparisons for several explicit frequencies in dimensions two and three, and exact rational-coefficient expansion of the all-dimensional centralizer generating function for three matrix sizes at field orders two, three, and four. The expected completion markers are `ALL_COMMUTATOR_GRAPH_CHECKS_OK` and `ALL_EULER_PRODUCT_CHECKS_OK`.

The raw character sums are compared with a numerical tolerance because complex roots of unity are evaluated in floating point. The centralizer and formal-series tests use exact arithmetic, including integer divisibility checks. The symbolic Fourier support theorem and general Euler product are proved in RESULT.md and are not certified by finite experiments. Independent mathematical audit has not been performed.
