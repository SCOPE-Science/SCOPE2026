---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The unique maximum split has an ascent into the maximum and a descent out of it when the relevant block is nonempty. Reconstructing the signed series by left-block size gives the displayed recurrences; in the {1,3} series, the length-two left block contributes zero (its signed singleton counts cancel), and the length-three block contributes -z^4 C. With 1-zC=1/C, the series differ only by the z^3 correction, and the Catalan ratios give the factor (n-2)(n-9) on the claimed n>=4 domain. An independent integer descent-mask recursion and direct signed character sum through order nine reproduced no two-coordinate zero at orders 2–8, the four listed two-coordinate zeros at nine, and no singleton zero at nine. This is exhaustive for the stated band and orders, not a classification beyond nine. The frozen checker compares transforms but prints rather than asserts the expected zero lists, contrary to the stronger wording of VERIFICATION.md; the independent reproduction checks the lists directly. The uploaded script was inspected, not executed.

## originality

PASS

The bijection and inversion-coordinate embedding give genuine overlap at the representation and small-order data levels. Neither inspected source states or gives the all-length identity and first complete quadratic-band cancellation census. The originality judgment is limited to that combined contribution.

## value

PASS

The quadratic character band directly tests which pair-parity observables can be recovered by descent-profile convolution. Its exact first lost modes, with the linear band still intact at that order, are a natural low-band cutoff rather than an arbitrary table. The all-length equality for adjacent versus nonadjacent position pairs explains two zeros exactly and distinguishes an isolated cancellation from a generic rank statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
