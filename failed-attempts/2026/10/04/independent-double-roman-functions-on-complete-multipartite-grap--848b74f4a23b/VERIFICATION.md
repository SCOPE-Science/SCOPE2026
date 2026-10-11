---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Independence forces all positive labels into a single part. A zero or one inside that part has no positive neighbor because vertices in one part are pairwise nonadjacent, so every supported-part vertex must be labelled 2 or 3 and every other vertex is zero. Any outside zero sees the entire supporting part; for part size at least two every 2/3 assignment works, whereas on a singleton only label 3 works. Summing \((z^2+z^3)^{n_i}\) over supporting parts and removing the invalid singleton \(z^2\) terms gives the displayed enumerator, total count, and minimum-function counts. The package verifier exhausts all labels for every multipartite type through order nine and agrees exactly.

## originality

PASS

The primary independent-double-Roman literature inspected develops the minimum parameter and general bounds, including examples where complete bipartite graphs witness sharpness, but does not classify every function on arbitrary complete multipartite graphs or give this weight enumerator. Targeted Resultary search returned several related Roman-type enumerators on complete multipartite graphs but no independent-double-Roman enumerator. Best-of-knowledge originality therefore survives, with the caveat that the argument itself is very short.

## value

FAIL

Although the complete weight distribution is a natural refinement of the minimum parameter, on a complete multipartite graph it follows immediately from two elementary observations: independent support lies in one part, and labels 0 or 1 cannot occur inside that part. The remaining polynomial is a binomial expansion with one singleton correction. Under the shared value bar, this is a routine definition-level specialization rather than a motivated structural gap requiring substantive mathematics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
