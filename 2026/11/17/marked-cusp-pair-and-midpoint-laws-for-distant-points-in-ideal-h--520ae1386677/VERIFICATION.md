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

Exact symbolic steps checked: cusp chart width identities, normalized \(e^{-u}\) area density, distance expansion from \(\cosh D\), positive change-of-variables Jacobian, bounded same-cusp/core contributions, conditional \(L^1\) convergence and midpoint hyperboloid formula. The quadrilateral unordered cusp-pair weights add to one, opposite pairs total one half, all midpoint row-sums equal one quarter, and the labelled cross-ratio is recovered algebraically.

Run `python -m pip install -r requirements.txt` and `python verify_marked_cusps.py`. The checker uses independent area sampling in an ideal triangle decomposition and two separate quadrilateral parameter values. Successful output ends with `CUSP_MARKED_CONDITIONAL_GEOMETRY_OK`. Its conditional importance-proposal simulation is an asymptotic consistency test, not an exact sampler of the true rare-event conditional law. Finite-threshold ratios differ systematically by lower-order effects. No computer sampling replaces the analytical proof, and no independent external validation is implied.
