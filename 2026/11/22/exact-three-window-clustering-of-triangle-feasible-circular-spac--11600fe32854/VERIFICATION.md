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

# Reproducible mathematical checks

Run `python check_triangle.py` using Python 3 and only its standard library. The exact arithmetic verifies the independent-exponential one-window probability, the joint two-window probabilities for overlap one and overlap two, all six ordering-cone contributions to the third-order event, the exact conditional success \(232/525\), and all three variance regimes and the large-sample variance inflation.

The numerical diagnostics use a deterministic seed to simulate cyclic exponential gap windows at \(n=3,4,5,7,20\) (50,000 replications apiece) and a separate 200,000-replication test of the five-exponential three-success event. Their tolerance checks are not used to establish exact rational probabilities or any infinite limit.

The six-cone integral identity and bounded independent-block argument in `RESULT.md` are the analytic proof of the nonstandard third probability and of the Gaussian limit respectively. No machine proof of the infinite result, independent replication by another party, or general central limit theorem beyond this model is claimed.
