---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Direct composition yields d=2^m. Fixed points solve p=R_q(x)=x/[1−q(1−x)²]^d. Sign R_q′=sign(1−q(1−x)[1+(2d−1)x]), with a unique quadratic maximum d²/(2d−1) yielding q_d, the two fold roots and global at-most-three census. Strictly increasing return gives monotone convergence and excludes other periodic orbits. SymPy independently verified cusp fixed-point identities and G′=1, G″=0, G‴=−(2d−1)^3/[d²(d−1)] at d=4,8,32. Cubic coefficient implies n^{-1/2} constant; d log(1−c(1−x)²/d) gives Gaussian limit. Finite calculations corroborate, not prove all m.

## originality

PASS

The published exponent-two alternating cusp is equivalent to d=2 (one extinction season), which the final claim expressly excludes. Jamilov et al. study regular F-stochastic classes and associated Markov measures; their statements do not derive the opposed-vertex multiseason return or d-dependent thresholds. The d=2 classification alone is not an all-d theorem.

## value

PASS

Alternation of individually globally regular but opposing vertex-extinction maps produces explicit bistability: a motivated counterexample to naive regularity under switching. Full depth parameter boundary, cusp slowdown constant and nontrivial Gaussian limit are useful structurally.

The dated certificate retains the supplied scientific assessment, sources and limitations.
