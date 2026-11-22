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

# Reproducibility and limits

Run `python3 verify.py` with standard Python 3. It uses three exact-integer routes: direct matching recursion followed by a full Walsh transform through \(n=12\), a weighted-binomial expansion of the signed matching sum through \(n=50\), and centered-chi-square moments from the explicit cumulants. The checks assert 11,014 equalities, including the exact sign and spectral inertia for every dimension through \(50\), and Parseval's identity for each enumerated transform. Their successful completion confirms finite examples but cannot certify the infinite theorem; the proof in RESULT.md supplies the infinite justification. No independent audit has been performed.
