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

# Verification and mathematical limits

The proof uses intrinsic Euclidean facet-normal lengths, a nonnegative-array linear-programming dual certificate using the explicit integer tents \(u_j\) and \(v_j\), a complementary-slackness equality reconstruction, and two scalar quantile minimizations. In particular, no finite computation is used as a proof for unbounded column number.

Execute `python verify_monge3.py` with Python 3, NumPy, SciPy. The verifier ran successfully, reporting 17,138 assertions: exact rational primal witnesses and integer dual coefficients through \(q=36\), all parallelogram corners and midpoint samples where \(3\mid q\), Frobenius ball constraints, and independent HiGHS linear programs through \(q=16\). The boundary \(q=3\) is tested for consistency but is not claimed as new.

The structural facet statement is Theorem 5.3 of Erickson and Kretschmann (2023). The 2026 Erickson–Jones manuscript was available at abstract level only; its uninspected full text remains a priority uncertainty. No independent scientific audit has been performed.
