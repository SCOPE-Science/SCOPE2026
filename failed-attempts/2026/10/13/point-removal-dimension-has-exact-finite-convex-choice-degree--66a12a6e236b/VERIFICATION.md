---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Reconstructed Marcone–Volpi Theorem 5.3 forward uniform transformation: r input orders require exactly r-1 independent linear separators while the final order is replaced computably by two extensions. Converse: m separator instances are normalized onto common domain, one extra computable order added, and preserving first m output orders retrieves each separator via its cut below the inserted point. Appendix Proposition A.1 supplies uniform LS≡_W XC1. The fixed-arity and disjoint-union degrees follow by ordinary product composition. No finite experiment substitutes for uniformity; representational assumptions explicitly fixed.

## originality

FAIL

The complete new degree claim is an immediate formal consequence of **the same primary paper**: Theorem 5.3 proves precisely both computable instance-to-solution transformations with the exact r-1/m+1 arity counts; Proposition A.1 explicitly proves LS≡_W XC1. Juxtaposing these existing uniform reductions and taking finite Cartesian products/parallelization yields the displayed Weihrauch degrees without new reduction or nonstandard lemma. The absence of a printed equation in the paper does not make its direct corollary original.

## value

FAIL

No new computational separation, equivalence reduction, exact complexity boundary, or algorithm beyond those already exhibited in the primary source is established. Counting separator calls and substituting the source appendix equality is a routine deduction/packaging of a directly implied existing theorem. It has clear conceptual interest but not a separately valuable mathematical advance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
