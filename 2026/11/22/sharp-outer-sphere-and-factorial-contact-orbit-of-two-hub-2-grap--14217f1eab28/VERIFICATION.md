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

# Exact verification

Run `python verify_graph2.py` using the Python standard library; no external mathematical packages are required. The checker formally constructs the polynomial ring in three independent indeterminates, recomputes the complete squared-distance gap from the two direct coordinate formulas, expands the five nonnegative coefficient polynomials, and checks their exact identity and that all 41 nonzero monomial coefficients are strictly positive with the claimed zero locus. This is a finite exact-algebra certificate for the general inequality, not experimental evidence in finitely many dimensions.

It also independently reconstructs vertices by maximizing every connected-subset simplex under all strict coordinate orders for \(q=2,3,4,5,6\); it checks exact rational centers and squared radii, counts all vertices and all contacts, and compares with the claimed formulas. The reproducible reference output is:

```text
POSITIVE_POLYNOMIAL_CERTIFICATE_PASS monomials=41
EXHAUSTIVE_PASS q=2 vertices=20 contacts=4 R2=18
EXHAUSTIVE_PASS q=3 vertices=92 contacts=8 R2=19928/375
EXHAUSTIVE_PASS q=4 vertices=498 contacts=26 R2=1465/12
EXHAUSTIVE_PASS q=5 vertices=3142 contacts=122 R2=82610/343
EXHAUSTIVE_PASS q=6 vertices=22766 contacts=722 R2=164521/384
TWO_HUB_2_GRAPH_SPHERE_PASS
```

The finite enumeration is not a proof by exhaustion over all dimensions. The theorem's generality instead follows from its symbolic positive-coefficient identity, vertex parametrization and contact-barycenter argument. The verification is self-review only; independent audit has not been performed.
