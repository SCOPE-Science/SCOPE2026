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

The theorem was verified algebraically by direct outer-product calculations and by a disjoint classification of the two scalar cross-evaluations \(\varphi(s)\) and \(\psi(u)\). Every case has an explicit inverse construction; the nonzero/nonzero fiber has a bijection with \(\mathbb F_q^\times\), and all target populations admit independent incidence counts.

Run `python3 verify_joint_products.py` in the directory containing this document and the included script. The script uses only the Python standard library and literal matrix multiplication. The included `checks.txt` records successful tests for seven small prime-field configurations. It verifies exhaustive factor-pair enumeration, all attained target fibers, all forbidden support types among attained outputs, the target population formulas, and the weighted-mass identity. It does not enumerate every unattained matrix-pair target in the entire ambient square, and it does not execute extension-field cases; those cases follow from the symbolic proof, not from the tests.

Historical priority beyond the specifically compared sources is not certified. No independent external mathematical audit or validation has been performed.
