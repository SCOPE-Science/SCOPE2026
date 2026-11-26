---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

All q labels occur, with extra zeros in an even number, so the multiplicity of every label is odd. The parity/syndrome matrix contains (1,0) and all (1,e_j); hence it has rank m+1, including d=2. The even zero-syndrome class has exactly 2^(d−m−1) vertices. Removing it from the even class preserves independence. Odd y has exactly c_(σ(y)) neighbors in the deleted class and d−c_(σ(y)) in the retained class, an odd number; even outside vertices have zero retained neighbors. A coordinate matching bounds the optimum by 2^(d−1). The verified Corollary 27 supplies the stronger upper bound on the optimum and gives deficit at least 1/(4d−2); q≤d<2q gives the strict upper estimate and the all-even limit. These claims do not require determining the optimum in any general finite dimension.

## originality

FAIL

An earlier publicly accessible proof uses the same odd-multiplicity syndrome construction for every even d≥2^k and proves the exact same limit. Its quantitative lower bound gives the frozen lower bound by choosing k=floor(log₂d). The dated public source includes a readable proof, not merely a statement of the question, preregistration, or a claim of unpublished evidence. Its draft/merge status does not alter that mathematical coverage. The exact kernel cardinality in the frozen proof is a rank-nullity refinement of the same construction, not a new bound on the optimum.

## value

FAIL

The asymptotic question itself is worthwhile, but the frozen package does not add a new result about it: the public proof already gives the same family and lower bound, and the deficit order follows on adding the credited upper bound. Rank-nullity makes the existing cardinality argument more explicit without improving an extremal estimate or establishing a new structural classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
