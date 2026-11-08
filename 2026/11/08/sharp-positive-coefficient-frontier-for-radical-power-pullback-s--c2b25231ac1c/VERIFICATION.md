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

# Verification details

The analytical proof covers every integer \(m\ge2\) and every real \(p>0\). Its critical steps are the upper-tail log-concavity inequality, preservation of log-concavity by convolution, strictness of the first inequality, and the exact derivative calculation for \(d_1\).

Run `python3 verify_coefficients.py` with Python 3 standard library. Completed output: `VERIFY_OK exact_rational_checks=8479 m_range=2..18 positive_p_samples=11`. The checker computes all polynomial coefficients from the exact factorization using rational numbers and checks 11 rational parameters for each of the 17 orders, including both sides of the theoretical positivity boundary. It does not test the irrational equality boundary numerically; equality is proved symbolically. Finite testing does not imply universal truth.

No independent audit has been performed.
