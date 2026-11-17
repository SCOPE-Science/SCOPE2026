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

# Reproduction and boundaries

Run `python3 check.py` with Python 3; it uses standard-library arithmetic and checks the finite balancing identity on small compositions as well as the explicit squared-logarithmic example. The script is diagnostic only and cannot establish the statement for arbitrary positive integers or infinite sequences. The mathematical proof in RESULT.md uses majorization, Tonelli's layer-cake identity, and discrete convexity; its finite-attainment argument uses \(\Phi_k(m)/m\sim(\log m)^k\). The specific value \(k=2,n=2\) and block size five is a lower bound, *not* a claim that it is globally optimal. No independent mathematical audit has been performed.
