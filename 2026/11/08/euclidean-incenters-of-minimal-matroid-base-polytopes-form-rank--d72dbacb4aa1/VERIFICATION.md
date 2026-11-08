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

# Reproducibility and proof verification

The proof in `RESULT.md` is elementary and universal. It can be independently checked by constructing the convex hull of the origin and all red–black one-exchange basis vectors, projecting the given facet normals onto the equal-sum hyperplane, then maximizing the common inscribed-ball radius. No infinite conclusion rests solely on a finite experiment.

The included `check_minimal_matroid_inball.py` uses NumPy and SciPy, without external downloads. Execute `python check_minimal_matroid_inball.py` in the directory containing it. The run successfully returned `MINIMAL_MATROID_INBALL_FINITE_CHECKS_PASSED shapes=121`; it independently optimized all pairs \(2\le k,r\le12\), checked the sharp facet offsets at every extreme predicted incenter, and checked additional symmetric centers. Tolerances are \(10^{-8}\) for radius comparisons and \(10^{-9}\) for shifted-facet feasibility. These numerical checks provide reproducible evidence, not exhaustive parameter-space certification.

The published inputs used analytically are Ferroni's explicit basis and halfspace description of minimal-matroid polytopes, arXiv:2003.02679, Propositions 2.2 and 2.6. The exact convex-hull transformation and the projected-normal calculations are proved within the accompanying result, not assumed from software.

An independent external mathematical audit has not been performed.
