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

# Verification

Run `python3 checker.py` from a directory containing the extracted standalone checker. No third-party Python modules are required. Its exact recorded output is included as `checker_output.txt`.

The checker enumerates every matrix in the coefficient ring \(\mathbb F_p[T]\) for six finite examples, obtains the coefficients reachable by binary terms by iterative closure under \(a\diamond b=Ta+(I-T)b\), and compares the attained rank sets with the expected values. For every reached coefficient, it directly counts the solutions of its two-variable equation against \(p^{2d-\operatorname{rank}(r)}\). In total it evaluates 27,318 pairs of variable assignments, across the six cases. The recorded final line is `VERIFY_OK cases=6 evaluated=27318`.

This is finite corroboration only; the general all-dimension result is justified in `RESULT.md` by the coefficient-closure lemma, linear-image theorem and elementary-divisor decomposition. The checker does not enumerate every possible equation of arbitrary arity and does not purport to certify novelty or to provide an independent mathematical audit.
