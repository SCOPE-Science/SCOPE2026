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

For a vertex outside \(S\), having an outside neighbor is equivalent to the complement meeting another part, so restraint is exactly \(c(S)\ge2\). Domination is automatic if \(S\) meets at least two parts, while one-part support dominates exactly when it is the whole part. Inclusion-exclusion over sets meeting at most one part and complements meeting at most one part gives the stated formulas, and the minimum/count cases follow immediately. I independently replayed the definition against the criterion on representative multipartite profiles, including \((1,1)\), \((1,2)\), \((2,2)\), \((1,1,1)\), \((1,2,3)\), and \((2,2,2)\); the inspected verifier exhausts all isomorphism types through order ten.

## originality

PASS

Henning--Kazemi already treat complete multipartite graphs for the minimum \(k\)-tuple restrained-domination number, so the scalar minimum side is not treated as wholly new. Their framework does not enumerate every ordinary restrained dominating set or give the displayed polynomial. Resultary searches likewise found related domination polynomials but no prior all-set restrained-domination formula for arbitrary complete multipartite part sizes.

## value

FAIL

Although the full polynomial is apparently unpublished, the classification on a complete multipartite graph follows immediately from two definition-level observations: an outside vertex sees exactly the other parts, and a selected one-part set dominates only when it is the full part. The formulas are then routine inclusion-exclusion. Under the same value bar used for other complete-multipartite domination variants, this is a clean expository specialization rather than a substantive new structural gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
