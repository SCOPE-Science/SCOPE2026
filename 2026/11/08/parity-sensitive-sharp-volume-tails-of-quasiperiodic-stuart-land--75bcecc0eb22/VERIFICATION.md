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

The proof directly reduces the oscillator to its orthogonal normal modes, computes the induced volume metric, derives the Dirichlet moment identity, and obtains the lower and upper endpoints through Mellin inversion and a local Gaussian-ellipsoid argument.

Reproduction: run `python3 verify_torus_volume.py` using Python 3 with only its standard library. It tests the exact gamma formula and its independent-beta factorization for multiple dimensions and moments, exact \(N=2\) consistency constants, and Monte Carlo diagnostics in ambient dimensions \(6,7,8,9\). The observed final marker was `TORUS_VOLUME_CHECK_OK`.

The stochastic checks are finite-sample spot-checks, not proof of the limiting laws. The theorem does not assert that a single quasiperiodic orbit is periodic; its volume is that of its complete omega-limit torus. Resonant frequencies, non-isotropic directions, and degenerate invariant tori of zero sampling probability are excluded from the general claim. No independent mathematical audit has been performed.
