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

Run `python3 verify.py`. The standard-library-only program prints `VERIFICATION_OK` after enumerating every prime power of order at most \(169\) whose characteristic is at least five, checking the field-basis construction, square-set sizes, Euler's quadratic-character criterion on all nonzero elements, four-position patterns, and the complete list of failing orders and masks. A recorded example output appears in `finite_census.txt`. The result covers precisely \(42\) fields; it is a finite exhaustive certificate, not a Monte Carlo test.

The source proof separately derives \(16N_q(\varepsilon)\ge q-10\sqrt q-39\) for all finite fields of characteristic at least five. Since this is positive for \(q>169\), it proves the infinite remainder. To check the argument independently, verify the six pair correlations equal \(-1\), apply Hasse to the smooth cubic models and the smooth monic quartic model with two rational points at infinity, and bound the excluded four starts by \(32\). In characteristic three, shifts zero and three coincide; in characteristic two no nonsquare exists. These are mathematical proof steps rather than consequences of the finite script.

This is a self-review. No independent audit or independent validation has been performed.
