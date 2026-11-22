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

Run `python3 verify_circular.py` and `python3 verify_statistics.py` with Python 3 standard library. Their expected captured outputs appear in `verification_outputs/circular.txt` and `verification_outputs/statistics.txt`.

The first script independently enumerates all literal length-bounded square factors from a doubled source and compares each literal square set with the constructive list, before comparing its size to the closed piecewise formula. Its exhaustive region consists of all 3,375 ordered triples with entries from 1 to 15, plus 240 reproducible larger triples. The second script computes exact rational fixed-composition means, using a separate integer-offset set implementation, at thirteen lengths through 500; it confirms the rational arithmetic \(11/36+2/9+1/36=5/9\).

The infinite claim is established by the proof of the structural classification and the Dirichlet scaling argument, not by finite enumeration. Tests cannot rule out unseen published equivalents. No independent audit has been performed.
