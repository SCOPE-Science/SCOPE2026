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

Projecting onto constants, zero-sum partwise constants and the within-part differences gives eigenvalues 0, N and N−s, respectively. The diagonal and cross-part signs are immediate; a pair within a part of fraction p has sign given by F_p(x)−kappa with x=N(1+N eta)t. The integrand g_p increases strictly from 0 to 1/p, so its running average crosses each kappa in (0,1) exactly once; it decreases strictly with p, making the largest part decisive. At t=0 the matrix is the identity. In x coordinates the optimized quantity NT has derivative 1−g_p(x); its one zero, x*=log((2−p)/(1−p)), lies in range since the running average is less than g_p(x*)=1. Substituting p+(1−p)e^(−x*)=1/(2−p) gives the stated value. Strict ordering persists after maximization by evaluating at the attained optimizer for the smaller p. The one-deleted-edge graph is one minimizer, not the only one: all noncomplete graphs with largest part two tie. The star is the unique maximizing shape up to isomorphism. The expansion g_p(x)=x+O(x²) and continuity at the inverse level 1 give the coupling limits; taking p→0 and p→1 verifies the shape ratio. Complete graphs stay nonnegative. The nested checker was inspected, not executed; the recorded numerical checks are corroboration only.

## originality

PASS

The supported distinct content is the sharp finite-coupling recovery and unique optimizer on general, possibly unequal multipartitions, with strict largest-part ordering and its optimized shape comparison. Pure-generator, star and balanced multipartite overlaps are real but do not imply that content. The spectral decomposition and generic scalar-filter formulas are not counted as new.

## value

PASS

The exact global sign boundary and unique worst strength answer a natural question not settled by eventual positivity. The reduction shows that the largest part alone governs the delay even among highly unequal shapes, resolves all extremal ties, and gives a quantitative limiting comparison of optimized delays.

The dated certificate retains the supplied scientific assessment, sources and limitations.
