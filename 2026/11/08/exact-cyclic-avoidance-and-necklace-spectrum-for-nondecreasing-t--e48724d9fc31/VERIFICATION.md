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

# Reproduction

From the directory containing the supplied files, run `python3 verify.py`. The script requires only the Python standard library and uses exact integer arithmetic.

The script computes the six-periodic binomial polynomial, derives length counts from the formal logarithmic-derivative recurrence, and independently forms the two-layer transfer matrix. It compares counts through length twelve for alphabet sizes one through eight, and directly checks every candidate cyclic word for cases in which the total search space is no larger than 450,000. On success it prints `PASS`.

These checks are finite consistency tests. The proof for unbounded alphabet size and length is the nilpotent-matrix determinant computation in `RESULT.md`, combined with the exact trace identity. The paper comparison is a self-review, not an independently established priority certificate.
