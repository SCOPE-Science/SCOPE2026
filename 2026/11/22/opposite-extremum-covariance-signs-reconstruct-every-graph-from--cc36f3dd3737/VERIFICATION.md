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

# Reproducibility

`checker.py` requires Python 3 and only its standard library. Run `python3 checker.py`. It deterministically examines all simple labelled graphs of orders two through five, every priority ordering, and every distinct ordered vertex pair. It checks marginal probabilities, the integral's exact rational value, the three-way covariance sign law and the edge lower bound. The recorded output is `PASS: 1098 labeled graphs, 74708 exact assertions; all rank orders n<=5`.

The mathematical proof handles arbitrary finite graph order independently of the exhaustive finite verification. It uses no numerical approximation, stochastic simulation or hidden supporting data. Finite enumeration cannot establish all-order correctness, and no independent audit has occurred.
