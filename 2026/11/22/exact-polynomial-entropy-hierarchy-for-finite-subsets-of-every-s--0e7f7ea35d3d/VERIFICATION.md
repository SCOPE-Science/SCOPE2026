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

# Verification and reproducibility

Run `python3 checker.py` from the package directory. The code uses only Python's standard library, and `checker_output.txt` records its exact expected output. It checks that all mechanical coding partitions of lengths 1 through 60 have \(N+1\) distinct cylinders for the coprime rational approximant \(233/377\). At four displayed lengths it also counts distinct words in three fixed separated phase arcs, verifying the labeling construction in finite arithmetic.

The mathematical proof does **not** infer irrational or infinite-time claims from this finite experiment. It relies instead on standard Sturmian interval coding and Weyl equidistribution, compactness and uniform continuity of the intercept phase map, and the explicit Bowen/Hausdorff separation and singleton quotient arguments recorded in RESULT.md. In particular, linear growth in every fixed phase arc is an asymptotic irrational-rotation statement, not a property verified by these rational experiments. The full-hyperspace statement uses only invariant-subsystem monotonicity, and the zero ordinary entropy statement uses the finite-product entropy inequality.

This package records a self-review. Independent audit: not performed.
