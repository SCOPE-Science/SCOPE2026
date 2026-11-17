---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For the explicit equal-moment EMA scalar rule s+=beta s+(1-beta)kappa x, v+=beta v+(1-beta)kappa² x², x+=x-eta |s+|s+/v+, a sign-symmetric orbit must have moments ±kappa c a and constant v=kappa²a², c=(1-beta)/(1+beta), forcing a=eta c²/2. The normalized branch derivative at (1,-c,1) is J+=[[1-8beta,-4beta/c,2beta],[1-beta,beta,0],[2(1-beta),0,beta]], with J-=TJ+T, T=diag(-1,-1,1). Two-step determinant calculation yields the stated cubic and Schur reduction A=1-beta^8, B=a2+beta^4 a1, C=a1+beta^4 a2. The factorizations for A-C, A+C, A±B+C yield strict Schur stability exactly beta²-8beta+1>0, i.e. 0<beta<4-sqrt(15); above it a multiplier leaves the unit disk; at equality the cubic is (z+1)^2(z-beta^4). The local objective gap kappa eta² c^4/8 is positive. No claim about nonlinear stability at boundary, global basins or other cycles.

## originality

PASS

The FlexGrad source introduces EMA signal and square buffers, but its documented convex convergence theorem covers cumulative updates rather than this equal-buffer noncumulative mirror specialization. Prior Adam/SAM/Padam two-cycle results concern different normalization and state recurrences; their stability polynomials do not logically yield the exact beta-only 4-sqrt(15) cutoff here. Semantic searches yielded no earlier identical three-state polynomial or cycle frontier. PASS best-of-knowledge with primary-section access limitation.

## value

PASS

A sharp analytic momentum threshold separating a locally attracting nonoptimal two-cycle from linear instability in a named practical optimization variant is a motivated model-specific dynamical classification. It is neither the trivial existence of cycles nor an unsupported global claim; it distinguishes EMA from cumulative convex guarantees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
