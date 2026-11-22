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

# Verification

The proof is analytic, based on strict conditional negative type of the Euclidean distance matrix, an exact one-dimensional quadratic reduction, and the strict convexity of a positive three-focus sum of distances.

Run `python3 verify.py` with Python 3 standard library. The checker directly solves both the three-site and four-site mass-one gauging equations, independently evaluates the three-focus potential, checks the exact quotient for the fourth weight, and compares signs. It checks the exhibited convex quadrilateral and verifies the critical strict inequality using elementary radicals. Its fixed seed generates 381 nondegenerate, distinct configurations that meet the separation criteria; it checks 9 interior-of-edge points for the last randomly selected triangle. The observed output was:

```
PASS: explicit exposed negative site; 381 independent random four-site checks; open-edge checks
```

The randomized tests are finite floating-point consistency tests, not exhaustive proof or independent mathematical audit. The universal and minimality claims are supplied by the symbolic argument in `RESULT.md`. The four-point system is defined only for distinct points; although the sign curve runs through the original three foci, the microscopic weight is not assigned a four-distinct-site meaning at those three collisions.
