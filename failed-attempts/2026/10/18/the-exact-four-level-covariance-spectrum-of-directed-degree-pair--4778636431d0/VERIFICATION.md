---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For distinct i,j the only arcs shared by their bidegrees are i→j and j→i. Conditional on these independent Bernoulli variables the four remaining degree counts use disjoint arcs. The centered conditional mean has linear coefficients −d_r b_s, −b_r d_s and mixed coefficient d_r d_s; the two linear coefficients interchange at j. Their orthogonal Bernoulli products give the stated covariance. After weighting, the constant, normalized centered out-/in-degree, and product score form an orthonormal tensor basis of the affected directions. The two linear scores have block n[[1,1],[1,1]], the constant gives zero, the product gives n+n/(n−1), and the orthogonal complement has eigenvalue n. This also gives precisely two null modes, the n=2 multiplicity coincidence, and the sharp variance bound by centering the score; the score r+s attains it. As a separate finite check, fresh exact rational enumeration at n=3, p=2/5 (all 64 digraphs) matched the 9 means and all 81 covariance entries.

## originality

FAIL

The exact spectrum is not explicitly listed in the earlier marginal-histogram theorem, but it is an immediate tensor-and-swap consequence of the exact two-vertex mixed degree law actually proved there, in the same independent-arc model. This is demonstrable coverage by implication, not an inference from similar histograms or indexing dates.

## value

FAIL

The nonlinear product mode and a uniform sharp variance bound are useful summaries for joint scores. However, the only claimed advance is the mechanically tensorized exact second-moment consequence of an existing kernel in the same model. No independent unresolved obstruction, additional result, or nonmechanical narrow invariant is established by this frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
