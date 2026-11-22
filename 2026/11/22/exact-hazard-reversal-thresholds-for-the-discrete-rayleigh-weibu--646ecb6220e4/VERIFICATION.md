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

# Reproduction and limits

The self-contained analytical proof is in `RESULT.md`. The accompanying `check_hazard.py` uses Python 3 with the `sympy` and `mpmath` packages. Run it with `python check_hazard.py` from the directory containing these files. During verification the script completed without an assertion failure and printed the following checks as PASS: symbolic second-derivative factorization; positive/negative finite-age threshold checks; strict ordering in sampled root sequences; increasing-hazard diagnostics for sampled shapes at or above one-half; and the explicitly exhibited two-step decline example at shape one-quarter.

For \(\beta=1/4\), the high-precision diagnostic values were \(t_0\approx1.459025832009218012\), \(t_1\approx1.066834456788999705\), \(t_2\approx0.9551989254559809822\), and \(z_{1/4}\approx1.24885811252099272479\). These computed values are approximate; uniqueness, exact ordering, all-age signs and asymptotics are proved analytically in the manuscript. The code does not certify infinitely many indices, all real parameters, or priority against all historical publications. No independent audit has been performed.
