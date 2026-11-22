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

# Reproduction and mathematical checks

Run `python checker.py` with NumPy and SciPy. The code evaluates \(K_{n,t}\) using the exact binomial-tail representation, verifies positivity and symmetry on finite grids, checks the degree-one formula against \(C_1^2=1/48\), and checks the Gaussian-tail integral and several scaled numerical residuals. These checks are finite and approximate where noted; the continuum maximization, equality classification and limiting theorem rest on the analytic proof in RESULT.md. No independent verification has been performed.
