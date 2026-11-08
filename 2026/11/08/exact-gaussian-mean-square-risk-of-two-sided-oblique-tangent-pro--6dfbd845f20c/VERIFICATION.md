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

# Verification of the Gaussian oblique tangent risk law

The exact proof is in `RESULT.md`, with a deterministic decomposition, three mutually orthogonal error components, a Gaussian regression/chi-square calculation and a critical-moment argument. The following checks were performed against the actual accompanying program `VERIFY.py` using NumPy and SymPy:

- Exact symbolic projector identities and Frobenius orthogonality for ranks \(1,2\) and multiple integer sketches.
- Three seeded Gaussian Monte Carlo comparisons with \(14,000\) trials each for \((r,\ell)=(1,5),(2,8),(3,11)\), producing empirical normalized means \(0.796953\), \(0.947570\), \(1.041534\) versus exact predictions \(0.777778\), \(0.960000\), \(1.040816\).
- Successful terminal signature `VERIFY_OK`.

The random checks corroborate—not replace—the exact Gaussian moment proof. The divergence at \(\ell\le r+1\) is established analytically via the inverse chi-square integral, not by a simulation timeout or sample maximum. Independent scientific validation has not been performed.
