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

# Reproducibility and limits

Run `python3 CHECKER.py` from the directory containing these files. The checker uses only the Python standard library and reports the root, optimal shape, universal maximal-correlation constant and endpoint dependence parameter. The submitted checker was executed successfully against its actual source file.

The analytic proof's critical, non-numerical steps are: (i) the density is exactly a symmetric rank-one perturbation of independence; (ii) the score has full range between opposite equal-magnitude extrema; (iii) the stationary Markov transition operator has precisely one nonzero centered eigenvalue; (iv) the admissible endpoints maximize the eigenvalue's magnitude for each fixed shape; and (v) the global shape ratio has a derivative controlled by a strictly decreasing function above the unique turning scale. These establish all-parameter and all-lag statements, including endpoint equality, without finite extrapolation.

The computational checks include direct Simpson quadrature at selected real shapes, the exact transformed integral, nonnegative-density test grids at the parameter boundary, numerical Chapman--Kolmogorov convolution at lag two, and checks of the displayed numerical precision. This is not an exhaustive proof over a continuous parameter space; the proof in `RESULT.md` supplies that. No independent mathematical audit or external certification is claimed.
