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

# Reproducible checks

From a directory containing the two standalone Python source files, run:

```sh
python3 singer_homotopy_certificate.py
python3 singer_matroid_verifier.py
```

The first script uses only the standard library and exhaustively checks the cyclic \((21,5,1)\) line design, its 1120 noncollinear triangles, 54 triangle orbits, and the unique stabilizer-three orbit. It constructs oriented quotient attaching words with the stabilizer correction, performs nine valid one-occurrence relator/generator cancellations and checks that the 45 residual relators consist of 31 empty words and 14 seventh powers. Success marker: `SINGER_Q4_HOMOTOPY_CERTIFICATE_OK`.

The second script requires SymPy. It independently rebuilds integral quotient boundary matrices for orders two, three and four and computes Smith forms. For order four it confirms ten edges, 54 triangles, invariant factor seven and 44 free second-homology generators. Success marker: `SINGER_PROJECTIVE_MATROID_QUOTIENT_CHECKS_OK`.

These finite checks are exhaustive for the **explicit twenty-one-point construction**, not a search over arbitrary projective planes or field orders. The noncomputational inference from a one-occurrence cellular cancellation to a homotopy equivalence and from null attaching loops to wedge-sphere summands is supplied in the proof, not inferred from computational success alone. No independent audit has been performed.
