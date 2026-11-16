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

# Verification and limitations

The analytic proof in RESULT.md establishes the all-dimensional statement by correlation counting, exact signed-shell enumeration, Vandermonde's identity, a beta integral and Stirling's formula.

To perform supplementary arithmetic checks with the embedded standalone script, use:

```shell
python3 simplex_fourier_checker.py
```

This script uses Python's standard library only. In this run it produced `PASS 164 exact comparisons; triangle e.g. n=2 energy 102 d=3 normalized limit 5/21`. The direct enumerations include all \(n\le18\) in dimension one, all \(n\le12\) in dimension two, all \(n\le6\) in dimension three, and all \(n\le3\) in dimension four, along with further exact checks of the triangular polynomial and normalized constants. These are finite examples and cannot by themselves verify the infinite theorem. The proof handles the infinite range independently of these tests.

No check was made for arbitrary nonconstant Fourier coefficients, other convex polyhedra, or joint two-index limits. Prior-literature comparisons are scoped to the sources named in the review; priority is not an independent certificate.
