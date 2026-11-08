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

# Reproducible checks and scope
The accompanying Python standard-library program is `verify_hexagon.py`. Run `python verify_hexagon.py`; its expected standard output is embedded as `verify_hexagon_output.txt`. The program enumerates the 127 nonempty subsets of the seven-point Newton support, computes hulls, normalizes by translation, and tests possible residual exponent translations with integer arithmetic. It confirms 1 unit type, 6 primitive segments, 8 unimodular triangles, and 3 unit parallelograms with multiple residual translation choices. Its residual mixed-area inequalities are all exact.

The sharp two-section construction is evaluated in the prime fields of sizes 5, 7, 11 and 13. For field size 5, the program additionally exhausts all 12,870 subsets of eight evaluation points, verifying matrix rank at least six for each; this gives a complete independent finite-field obstruction to two independent sections sharing eight points. Outputs end with `ALL_CHECKS_PASSED`.

General prime powers are covered by the symbolic proof in `RESULT.md`, including the Newton-shape reduction and toric intersection bound, not by finite experiments. The code is ordinary independent verification, not an external audit or formal proof of the general theorem.
