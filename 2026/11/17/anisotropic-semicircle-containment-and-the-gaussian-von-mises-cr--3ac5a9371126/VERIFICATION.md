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
# Verification record

The enclosed `check_anisotropic_mec.py` uses NumPy and SciPy. Install the dependencies listed in `requirements.txt` and run `python check_anisotropic_mec.py` in the directory containing both files. Its successful execution emitted `ANISOTROPIC_MEC_WINDOW_CHECK_OK`.

The tests compared six exact finite polynomial probabilities against direct angular quadrature; three large-sample fixed-anisotropy Laplace ratios; three critical-window probabilities against modified Bessel values; and three conditional marked-sample tests (30,000 independent conditional simulations each). Numerical ratios and empirical moments were close to the specified analytic limits. The checker samples the conditional pivot directly and inverts the exact truncated endpoint-gap distribution; it does not directly simulate exponentially unlikely unconditioned events.

The mathematical evidence is the exact disjoint-anchor density, the exact far-endpoint order-statistic law, the one-dimensional Laplace expansion, uniform weak-modulation expansions, Scheffé's lemma for the joint densities, and the diameter-chord geometry. These arguments establish the asserted infinite limits independently of finite simulation; no external mathematical certification or independent audit is claimed. The full proof and precise quantifiers are in `RESULT.md`.
