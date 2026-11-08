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

# Reproducibility and boundaries

Run `python3 verify.py` with standard Python 3. The checker reconstructs finite independent Bernoulli discovery subset laws, exact harmonic means, finite variances, deterministic mean roots, the finite-end cutoff bias, and selected asymptotic-kernel constants. It requires no external packages or remote services.

All checks are finite numerical or finite subset-enumeration tests. They cannot certify a central limit theorem or determine historical originality. The infinite result is proved in `RESULT.md` by an Euler--Maclaurin error estimate, a Lyapunov triangular-array argument, and inversion of the monotone discovery threshold.

The variance normalization is for the scaled time \(A_n=\lambda\tau_{n,\theta}/H_n\). The theorem does not claim total-variation convergence to a continuous law (which is not established by weak convergence), moment convergence, or a universal limit for changing \(\theta\).
