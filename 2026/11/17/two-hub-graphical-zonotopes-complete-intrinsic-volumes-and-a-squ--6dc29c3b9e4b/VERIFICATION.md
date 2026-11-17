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

# Checks and limits

`check_k2q_intrinsic.py` is standalone Python 3 code using only the standard library. Execute `python3 check_k2q_intrinsic.py` from the extracted package directory. It enumerates all \(2^{2q}\) edge subsets for \(q=1,\ldots,7\), checks the exact connectivity classes, and verifies their sums against the closed expressions. It also independently evaluates the integer Gram determinant of every forest for \(q\le6\) using Bareiss elimination; it does not merely replay the component-size formula. The test prints `K2Q_INTRINSIC_PASS q=1..7` on success.

The unrestricted proof is in `RESULT.md`. The tests are finite and do not establish asymptotics or all-dimension validity on their own. The asymptotic proof uses binomial/multinomial concentration and Taylor bounds. Independent external audit has not been performed.
