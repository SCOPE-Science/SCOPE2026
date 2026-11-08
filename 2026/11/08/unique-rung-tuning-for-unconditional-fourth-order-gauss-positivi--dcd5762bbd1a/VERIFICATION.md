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

# Exact reproducibility

Run `python3 verify.py` in the directory containing the code, with Python 3 and SymPy installed. This verifier reconstructs the two Jacobi Laplacian blocks, the tuned Green inverse, all six spectral projectors, and the full completed fourth-order Gauss heat matrix. It checks exact symbolic identities for all 15 off-diagonal entries, their six polynomial positivity certificates, direct rational evaluations at four positive timesteps, and the untuned negative witness \(-1471112/79673503\) at \(h=8\).

The infinite-parameter statement is supported by the documented polynomial coefficient signs and exact asymptotic pseudoinverse argument, not by those four sample timesteps. The checks do not establish all-step positivity for a different network, a different integrator, or independently variable rail weights. External independent verification has not been performed.
