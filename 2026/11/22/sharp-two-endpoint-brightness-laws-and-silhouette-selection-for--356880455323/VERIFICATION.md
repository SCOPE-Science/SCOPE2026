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

# Verification of sharp dodecahedral brightness tails

Run `python3 verify_dodeca_brightness.py` with the Python standard library from the package directory. The script reconstructs the six normalized outward facet-normal axes, uses exact rational arithmetic in the quadratic field \(\mathbb Q(\varphi)\), checks all 64 signed sums and their squared-length multiplicities, and checks the 15 non-collinear great-circle crossing axes and their common brightness values. It also checks the 12 maximizing normal directions, an exact positive cap-separation interval and the local near-minimum formula.

On the delivered package, the script passed 2,900 deterministic numerical brightness/local-form diagnostics, four silhouette-sector checks and three independent numerical integrals corroborating the quadratic-plus-cubic small-deficit expansion. Its summary prints the two endpoint values, the precise upper-tail range and all three probability coefficients. The proof in RESULT.md, not finite sampling or quadrature alone, establishes the continuum statements. Independent mathematical verification has not been performed.
