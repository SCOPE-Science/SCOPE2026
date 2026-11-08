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

Run `python verify.py` with Python 3 and the standard library only. The program computes all gcd edges and run lengths directly over complete residue periods, compares independent modular edge predictions and published histograms, rejects every proper-divisor subperiod, and checks further indices to 20,000. The verification is a finite cross-check of exact integer identities; the resultant and CRT argument in RESULT.md is the general proof. No independent audit has been performed.
