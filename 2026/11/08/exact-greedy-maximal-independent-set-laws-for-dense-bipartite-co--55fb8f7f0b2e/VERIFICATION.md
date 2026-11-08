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

The complete theorem is proved analytically in RESULT.md. The accompanying Python 3 checker performs independent exact-rational recursive greedy-state calculations, complete maximal-independent-set enumeration, and checks of the algebraic inclusion-exclusion expression. Run `python3 check.py` with no additional packages.

Finite graph examples include the deleted-edge cycles \(C_6,C_8,C_{10},C_{12},C_{14},C_{16}\), a disconnected pair of six-cycles, and the Fano-plane incidence graph. Exact full terminal-set probabilities, exact total variation, and the two-point size distribution are all checked against the stated formulas. The graph cases cover degree two and degree three, while separate rational identity checks cover degrees one through nine. The degree-one algebraic checks are only formula checks, not claims of the theorem's graph domain.

The checker additionally enumerates all uniform vertex permutations for the six-vertex and eight-vertex examples and compares the outcomes with the independently calculated recurrence. This verifies representative finite cases only; it does not establish the infinite family theorem or historical priority. The comparison with existing published work is a bounded self-review, not independent validation.
