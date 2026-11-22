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

Run `python3 verify_direct.py` with Python 3 and its standard library to enumerate the exact labelled transitions for every \(2\le m\le7\) and \(0\le k\le m\). This checks 167472 initial states and compares local updates, two-step return, activity profiles, and least periods against the theorem. Output is `direct_output.txt`.

Run `python3 verify_weighted.py` with Python 3 to independently enumerate all pair-type occupancy counts and verify the exact activity polynomial, its full balanced population and the first two moments, for 1888 parameter choices \(2\le m\le60\) and \(0\le k\le m\). Output is `weighted_output.txt`.

Both checks were completed successfully. The supplied proof of the all-size theorem is an analytic case analysis and hypergeometric moment derivation; finite enumeration provides regression verification only. No independent external audit is claimed.
