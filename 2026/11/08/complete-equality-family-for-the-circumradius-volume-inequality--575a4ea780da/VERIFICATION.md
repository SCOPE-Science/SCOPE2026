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

# Verification of the equality-family classification

The proof in `RESULT.md` establishes the universal assertions. The attached `verify.py` program is an independently executable, standard-library-only calculation of finite algebraic examples; it does not provide a machine certificate for arbitrary real generators.

Run `python3 verify.py` from the directory containing both files. The code checks the exact fractions underlying the witness with circumradius \(R=2\), volume \(16\), and unequal squared generator lengths \(321/100\) and \(281/100\). It enumerates all sixteen sign patterns, checks orthogonality of the three balanced sums and the determinant identity, and verifies orientation via signed maximal minors. It also checks the universal squared inequality against 4,000 seeded rational four-generator instances. This replay completed successfully with the terminal line:

`FOUR_GENERATOR_ZONOTOPE_EQUALITY_CHECKS_PASSED`

The script cannot establish absence of a previously published equivalent characterization, cannot replace the exact proof of the inequality or all equality cases, and does not evaluate degenerate 4-generator configurations exhaustively. Its symbolic and numerical results are adjunct consistency checks only.
