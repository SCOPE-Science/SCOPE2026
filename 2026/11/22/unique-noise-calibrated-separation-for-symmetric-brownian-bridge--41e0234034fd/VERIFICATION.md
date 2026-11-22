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

The analytic proof uses the exact Green kernel of the pinned bridge, a two-by-two Gaussian Schur complement, Descartes' sign rule on an explicitly transformed sextic, and a repeated-observation comparison. The included `verify.py` checks the kernel-product integral, symbolic gain, derivative identity, collocation identity, and 70 exact rational instances; `VERIFIER_OUTPUT.txt` records a successful local execution. The test requires SymPy, and its finite checks are not a proof of uniqueness or publication priority.

**Scope:** Two observations with identical positive noise variances, reflection-symmetric locations, integrated posterior path variance. No assertion about optimality among all asymmetric pairs. **Limitations:** Historical source text not fully available for the Mukherjee dissertation; no independent audit.
