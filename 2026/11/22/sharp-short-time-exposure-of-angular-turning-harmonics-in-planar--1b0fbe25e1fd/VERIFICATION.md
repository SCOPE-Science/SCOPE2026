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

# Reproducibility and verification scope

Run `python3 checker.py` using Python 3 with only the standard library. The actual run printed `PASS: 128 deterministic exact and finite-rate checks`.

The checker independently expands conditional radial moments for \(k=0,1,2,3,4,5\) Poisson turns, integrating uniform ordered turning times by exact Dirichlet multinomial factors. It compares the uniform angular law with an \(n\)-point root law for integers through \(n=7\), including exact cancellation in lower moments and the coefficient \(2(n!)^2/(2n+1)!\) of the first unmatched harmonic. It verifies selected finite-rate Poisson partial sums against the rigorous \(3(\alpha t)^2\) remainder envelope, explicitly accounting for the uncomputed Poisson tail.

For the general claim, the proof in `RESULT.md` is essential: finite calculations neither enumerate all turning laws nor certify an infinite-harmonic limit. Exact cancellation of independent Gaussian diffusion is derived from a finite Gaussian contraction identity; Brownian trajectories are not simulated in the checker. The theorem does not prove sample-noise robustness, efficiency of statistical estimation, or an independent scientific certification.
