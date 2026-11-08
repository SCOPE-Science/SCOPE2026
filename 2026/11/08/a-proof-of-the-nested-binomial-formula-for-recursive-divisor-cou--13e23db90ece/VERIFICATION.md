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

# Verification summary

The proof is symbolic and uses only the divisor recurrence and the formal binomial theorem in \(\mathbb Q[[x_1,\ldots,x_w]]\). The generating-function denominator has constant coefficient \(1\), ensuring that every inverse and coefficient operation is defined formally. The last summation gives the published finite formula, and the proof separately handles an empty prime signature and the one-prime case.

## Reproducible exact checks

`check_fink_conjecture.py` has no nonstandard dependencies. It independently implements a proper-divisor recursion on exponent tuples, the nested-binomial sum, and the coefficient recurrence of the rational generating function. Run `python3 check_fink_conjecture.py`. Its 764 positive-exponent cases and six empty/zero-exponent controls all agree, as recorded in `check_output.txt`.

## Limits

These finite checks do not certify the infinite identity; the proof in `RESULT.md` does. The related literature comparison is based on inspected accessible sources and cannot exclude all unindexed equivalents. No independent audit has been carried out.
