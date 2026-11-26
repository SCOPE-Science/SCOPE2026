---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The final /workspace/repairs/3/RESULT.md uses full directed bigram multiplicities for one genuine replacement in a linear word. Row and column marginals recover the ordered interior replacement; their nonzero pattern separates both ends. For a fixed b→d, comparing support in the equation R_a−R_a′=C_c′−C_c forces both changed neighbor pairs to lie in {b,d}; direct evaluation gives exactly one double fiber and q²−1 interior outcomes. When q≥3 each literal triple has a private difference for some replacement, forcing n−2≥q³ at equality; covering all triples suffices and is preserved under padding. For the count, A²=J and equal row/column degrees give q²−1 nonzero Laplacian eigenvalues q counted with multiplicity. The equal Matrix-Tree cofactors are q^(q²−3). Fixing a first triple arc selects one representative per cyclic Euler tour, and BEST followed by q³ distinct starts gives (q!)^(q²) linear words. The original limitation incorrectly attributed binary behavior to extra collisions; the repaired statement correctly identifies the loss of the third-letter private-context argument. Fresh full-profile enumeration at length 8 found 00010111 attaining 8 distinct results, consistent with the frozen outputs. The analytic proof and correction were rechecked; supplied scripts/outputs were inspected, not executed.

## originality

PASS

The distinct result is exact maximum cardinality of the fixed-source one-substitution bigram image and the sharp necessity/sufficiency of complete triple coverage. The equality-case count uses the known de Bruijn count and is not a novel independent enumeration of de Bruijn cycles. No inspected competing claim covers the collision census and structural cutoff.

## value

PASS

An exact mutation-observation capacity for overlapping bigrams quantifies a genuine compression collision effect not answered by the Hamming ball size. The first saturation length and rigidity link observation diversity to complete triple coverage, giving a meaningful source-design cutoff and characterization. The binary clarification does not change these q≥3 results, and no generic code-size claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
