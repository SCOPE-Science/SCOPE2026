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

# Reproduction and verification

Run `python3 verify.py` with the Python standard library. The program enumerates all nonidentity symplectic transvections from projective vector representatives with all nonzero root parameters, forms every ordered two-factor product, and checks each actually attained product against the rank/Wall-line formula. Its direct matrix arithmetic is independent of the closed-form target-type population proof. It also compares each complete product support with the two closed-form support expressions and verifies that the sum of all fiber sizes equals the number of ordered pairs.

The captured output is `verify_output.txt`, showing ten full checks over fields of orders 2, 3, 4, 5, 7 and 9, in dimensions two, four and six. No sampling is substituted for enumeration in those cases. Extension-field arithmetic is represented using fixed irreducible quadratic polynomials.

These finite checks cannot prove the universal theorem. The proof's nontrivial ingredients are the rank-two Wall-line bijection (valid in every characteristic), the \(\operatorname{SL}_2\) rational-eigenline census, the symmetric-binary-form census, and the two-plane incidence counts. The full argument is provided in `RESULT.md`. Independent audit has not been performed.
