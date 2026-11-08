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
# Verification notes

The analytical proof in `RESULT.md` establishes the limit. The standalone `thin_shell_check.py` generates the shell exactly from the product of cone measure on the boundary and the radial density proportional to the scale factor. It detects failure of convex position by an oriented-cross-product test for inclusion of a point in another three-point triangle.

The checker uses exact rational arithmetic for the angular polynomial integral, confirming the coefficients \(1,3,963/8,20\) in the mean of \((1+\varepsilon\cos3\theta)^4(1-8\varepsilon\cos3\theta)^2\). With 900,000 independent four-point samples per tested configuration, the observed ratios \((1-Q)/(\delta\log(1/\delta))\) were:

| Shape | \(\delta=0.02\) | \(\delta=0.005\) | \(\delta=0.001\) | Exact asymptotic coefficient |
| --- | ---: | ---: | ---: | ---: |
| Disk | 0.254742 | 0.240538 | 0.233232 | 0.202642 |
| Threefold support, \(\varepsilon=0.10\) | 0.278131 | 0.264948 | 0.256555 | 0.238676 |

These are diagnostics, **not** a numerical proof of convergence: the logarithmic approach is slow and binomial sampling error is nonzero. The sign of the coefficient and its shape dependence are also established analytically. Independent review remains unperformed.
