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

# Reproducibility and boundaries

Run `python3 verify.py` with `verification_output.txt` in the same extracted directory for comparison. No external packages, random seeds, network data or previous results are required.

The exact finite cutoff check enumerates all \(2^{\binom n2}\) ordered adjacency masks on \(n=1,\ldots,5\), retaining respectively \(1,2,7,41,388\) triangle-free masks. The resulting type polynomials occupy respectively \(1,2,7,36,337\) fibers. For every fiber, a minimum over all vertex permutations checks that the underlying graph-isomorphism class is unique. This is exhaustive over that stated finite range.

The explicit six-point graphs have independent-set polynomial \(1+6z+9z^2+3z^3\) and identical full bivariate type polynomial. The only nonzero differences between gap-specific enumerators occur in gaps two and four, where opposite copies of \(u^2v-uv^2\) cancel. An independent check counts four-cycles by common-neighbor pairs. Direct extensions with \(t=0,\ldots,6\) pass as recorded in `verification_output.txt`.

The unbounded \(t\)-extension is proved symbolically via the old-independent-set partition into sets meeting or avoiding \(\{3,4\}\). Finite testing is not used as an infinite certificate. This verification is same-model only; independent mathematical audit has not been performed.
