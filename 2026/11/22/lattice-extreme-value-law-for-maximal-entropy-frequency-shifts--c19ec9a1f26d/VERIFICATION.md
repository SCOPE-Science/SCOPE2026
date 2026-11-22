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

Run `python3 verify.py` from this directory with Python standard library. The script checks exactly, using rational arithmetic, the complete codeword potential for multiple \(k,m\), the finite iid geometric-maximum probabilities, the size-biased block identities, and finite codeword composition injectivity.

The unbounded-time claims are proved in RESULT.md by stationary renewal construction, induced entropy, independent-return extrema, strong law, Borel–Cantelli, and potential bounds. Exact finite enumerations cannot prove infinite weak or almost-sure convergence. Independent auditing remains not performed.
