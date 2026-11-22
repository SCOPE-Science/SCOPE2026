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

# Mathematical reproducibility

Run `python3 verify.py` from the directory containing `verify.py`. It uses only the Python standard library and creates rational weighted cycle Laplacians and exact Kalman matrices, with no external datasets or network calls.

The executed checker prints `VERIFY_OK 550 exact_ranks 13 totient_checks`. It compares full exact Kalman ranks for all sensor locations on sizes \(n=5,\ldots,15\) at five rational weights \(1/2,1/3,3/4,2,1\). For odd sizes and weight \(1/2\), it checks exact gcd rank deficiency at each site. It also compares the totient counting formula over 13 odd ring sizes, from \(5\) through \(29\).

An exploratory floating-point PBH sweep covered 3,210 combinations through size \(27\) including detected resonances and reported no mismatches at its specified numerical tolerance. Finite exact and floating-point computations do not certify all real weights or all sizes; the analytic reflection-and-recurrence proof in RESULT.md establishes the infinite-family theorem. No independent review or independent validation is claimed.
