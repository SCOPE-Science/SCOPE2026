---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For mixed stable/unstable Riesz splitting choose unit stable and unstable vectors. Stable orbit shrinks below 1/2, unstable orbit grows above 2 uniformly at large n. Their normalized linear interpolation is a continuous path in unit sphere; by intermediate value a unit vector maps at time n to orbit norm exactly 1, violating uniform small-or-large alternative for ε=1/2,M=2 at arbitrary cutoff. Single-side hyperbolic spectrum gives operator-norm decay or inverse-norm decay and hence expansion. In finite dimension unit-circle eigenvalues defeat the condition. Explicit diagonal formulas a_N²+b_N²=1 and 4^-N a_N²+4^N b_N²=1 hold algebraically for every N≥1 (not just numerical samples). This respects both quantifier interpretations at the offending time.

## originality

FAIL

A published full Banach-space intrinsic criterion in Exact scalar annulus for super-asymptotic expansivity on Banach spaces (public Resultary RESULT.md, 2026/10/11/SCOPE-...1db36a867fe9) establishes super asymptotic expansivity iff some power is a global strict contraction or strict lower expansion. It explicitly treats diag(1/2,2), and strictly entails the mixed spectral obstruction and finite-dimensional spectrum classification. Thus the source-defined theorem and counterexample are already covered even without same wording.

## value

FAIL

The published exact scalar-annulus/global-branch theorem for arbitrary Banach operators already proves this mixed obstruction, the finite-dimensional dichotomy and the same explicit diagonal example. Exposing a flaw in another paper would be valuable if new, but this duplicate reformulation contributes no new motivated mathematical fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
