---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The read-once full binary tree counts an independently chosen allowed output at every internal node of the symmetric {0,1,k} nondeterministic disjunction. The derived bilinear convolution u⋆v exactly counts weighted traces. Independent symbolic expansion confirms associator ((u⋆v)⋆w−u⋆(v⋆w))=(0,−v_1 Δ,v_k Δ) with Δ=u_1 w_k−u_k w_1. The symmetric subspace u_1=u_k has multiplicative coordinates r, r+3s, yielding root vector (a^n,((a+3t)^n−a^n)/3,same) for b=c=t. If bc=0 the positive-weight domain is deterministic and total is (a+b+c)^n. Left comb vs balanced gives bc(b−c)^2>0 exactly at four leaves when b,c>0 unequal; n<=3 shapes coincide by commutativity. All nonnegative and zero-weight boundaries accounted for. Independently checked symbolic associator and all tree shapes through seven leaves, corroborating all-size induction.

## originality

PASS

Aldini–Graziani–Mezzina–Vergottini (arXiv:2607.20178) introduce the underlying symmetric three-valued Nmatrix and dynamic/static semantics, and study logical rules and a deterministic five-valued associative refinement. Their full accessible source sections on truth tables and calculus do not provide weighted counts of independent resolution histories or the bracketing-invariance classification. Resultary search found no theorem giving the same weighted associator and four-leaf sharp obstruction beyond the target. Historical overlap with general weighted multihyperalgebra semantics remains a residual risk.

## value

PASS

The exact all-size invariant separates reachability-set associativity from multiplicity-of-dynamic-traces associativity for a natural newly introduced nondeterministic choice semantics. Its iff nonnegative-weight criterion, exact root counts, and smallest four-leaf witness identify a meaningful structural boundary, not a tiny unexplained numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
