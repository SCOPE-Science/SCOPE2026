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

# Reproduction and scope

Run the included `verify_inversion.py` with Python 3; it requires only the standard library. The exact part enumerates all \(2^n\) binary words for each \(2\le n\le10\), at \(p\in\{0,1/3,2/3,9/10\}\). It independently checks the spin identity, probability normalization, mean and zero-inversion mass with exact rationals. Recorded result: **8,284 exact assertions passed**.

Seeded simulations were also executed: \(n=1000\), \(p=1/2\), 1,200 samples gave standardized empirical mean \(-0.004\) and variance \(1.038\); with \(n=1400\), switch intensity \(2.4\), 3,000 samples gave zero-inversion fraction \(0.4787\), against limiting prediction \(0.4819\); in a rare-switch experiment with \(n=500\), switch probability \(0.00005\), 15,000 samples gave positive-inversion frequency \(0.0127\), versus first-order prediction \(0.0125\). These finite tests do not certify any limiting law. The infinite statements follow from the direct martingale, point-process and rare-event arguments given in RESULT.md.
