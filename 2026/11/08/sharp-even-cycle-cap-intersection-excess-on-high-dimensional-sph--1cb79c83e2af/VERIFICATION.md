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

# Mathematical verification

The exact proof depends on five reproducible steps: independence of proper cycle-edge subsets by leaf integration, the self-adjoint trace identity, Funk–Hecke/normalized Gegenbauer eigenvalues, the complex-moment higher-harmonic bound, and the gamma-ratio/one-coordinate normal asymptotics. These are explicitly reconstructed in `RESULT.md`. No computational search is substituted for proof.

`check_even_spherical_cycles.py` is a standalone numerical checker using `numpy` and `scipy`. It independently integrates the zonal kernel for multiple harmonic degrees and dimension/threshold parameters; checks the trace decomposition and valid finite-dimensional upper bounds; runs \(600000\) independent four-vertex Monte Carlo configurations each for three dimensions; and checks the limiting coefficient using truncated absolutely convergent harmonic series. The actual execution returned `EVEN_SPHERICAL_CYCLE_EXCESS_TESTS_OK`.

The numerical comparisons are subject to floating-point and Monte Carlo sampling error. They cannot establish universal inequalities or historical originality. No independent mathematical audit has been performed.
