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

The complete finite computation is in `checker.py`; `class_table.csv` records the 24 class-representative rows. Run `python3 checker.py class_table.csv` using Python 3. The code tests complete subset enumeration, conjugacy class coverage for both linear groups, torsion-induced permutations, reducible/smooth counts, full cycle decompositions, and injectivity of the key \((q\bmod3,\#S(\mathbb F_q),\#K(\mathbb F_q))\). Both point counts and every extension count refer to geometric configuration schemes, not just coordinate-defined sextactic points. The source computation is independent of any elliptic-curve database.

The geometric input (a conic divisor is linearly equivalent to \(6O\), and a line divisor to \(3O\)) is an algebraic proof premise, not a consequence of the finite program. The method does not certify that all possible class pairs are realized by elliptic curves over each finite field; no such realization is required for the universal implication. Only a self-review has been performed; no independent audit or external certification is claimed.
