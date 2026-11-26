---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and limits

The unchanged companion `verify.py` uses Python 3 and SymPy. It checks the symbolic leading quadratic and vertex comparison and 1,200 fixed-seed rational cases of the uniform resolvent bound. Its additional finite-noise Brownian-bridge calculations are separate from the surviving high-noise theorem. These checks verify algebra and finite instances, not the stochastic hypotheses, the general theorem, or historical priority. Joint Gaussianity of the error vector, independent of the target and latent process, is an explicit hypothesis for identifying the gain with the conditional-variance reduction. The compactness and uniform convergence argument in `RESULT.md` applies with fixed \(-1<\rho<1\). The tie at \(\rho=1/2\) is only a leading-order tie.
