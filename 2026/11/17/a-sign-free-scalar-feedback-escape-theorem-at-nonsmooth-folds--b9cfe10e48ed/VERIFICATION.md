---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Exact two-branch identity x′+y′−x−y=μ+α|x|−g(y) follows since the branch linear x coefficient cancels δ. For ε=min(1/8,α/(8(1+D))) and η≤r/(2(1+D)), both |g(y)|≤ε|y| and |g(y′)|≤ε(D|x|+|g(y)|) hold at all pre-exit points. With Φ=x+y−g(y)−|g(y)|, ΔΦ≥μ+(α−2εD)|x|+(1−2ε)|g(y)|≥μ. Φ is bounded by 9η/4 in Bη, so its range <5η; at N=floor(5η/μ)+1 consecutive internal steps the monotone gain would exceed that range. Handles x=0 continuity, arbitrary δ signs, arbitrary μ, and g not differentiable; only local first departure is proved.

## originality

PASS

The full Simpson primary theorem is affine and its scalar quadratic extension is restricted to opposite determinant signs. The present explicitly proved triangular scalar o(|y|) class is not a restatement of the full unresolved two-coordinate conjecture.

## value

PASS

A constructive strict nonaffine and sign-free class resolves a natural part of a published open higher-order fold question. Its parameter-independent trapping-region exclusion and explicit exit bound are substantive dynamical information, not a normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
