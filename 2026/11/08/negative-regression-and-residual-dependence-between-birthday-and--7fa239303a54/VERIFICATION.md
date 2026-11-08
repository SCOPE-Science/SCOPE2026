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

Run `python3 verify.py` with Python's standard library; no third-party packages are needed. The checker's results were obtained by executing the embedded source on the finite test cases: 5,430 assertions passed. The tests compare two separate exact rational covariance expressions at \(2\le n\le119\), completely enumerate draw prefixes of length \(n+1\) at \(2\le n\le6\), verify the resulting covariance using an independently specified first-step Markov expectation for remaining collection time, check decreasing conditional cover-time means at \(2\le n\le100\), and inspect finite asymptotic diagnostics. The closed form for every \(n\), stochastic dominance, and scaling limits rest on the proof in RESULT.md rather than finite tests. No independent audit or external validation is asserted.
