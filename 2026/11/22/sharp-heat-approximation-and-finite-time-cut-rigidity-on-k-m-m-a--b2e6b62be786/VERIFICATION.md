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

For the counting norm and unnormalized unit-edge generator, strict positivity and stochasticity give exactly twice the heat mass across a cut. The finite layer decomposition is exact in edge TV; at an intermediate level of any input with at least three levels, some nested cut contributions have opposing nonzero signs at the same vertex, so the L1 triangle inequality is strict. The four Laplacian spaces have eigenvalues 0, b, a, a+b; projecting gives the across-shore entry X and within-shore off-diagonals A,B. For cut counts p,q let D be the edge boundary and U=p(a-p), V=q(b-q). For equal shores D-U-V=(p-q)^2 and A=B>0. For b=a+1, direct subtraction gives 1<A/B<b/a (differentiate the exponential difference for the first inequality and use increasing sinh(x)/x for the second). At relative weight 1, D-U-V=d(d-1), d=q-p. At weight b/a, multiplying the proposed slack by a(2a-1) gives -aU+(a-1)V+(2a^2-1)d(d-1), which expands to the stated polynomial. At d=0,1 this is respectively p(p-1) and (a-p)(a-p-1); outside those integers the quadratic term strictly dominates the linear change from the nearer endpoint for 0<=p<=a. The positive interpolation of the endpoint slacks leaves exactly (1,1) and its complement after empty/full cuts are excluded. This includes m=2. For a common maximizing cut at all finite times, the spectral weights are nonnegative and not all zero, giving strict increase/concavity, and the derivative at zero is 2 since the cut Dirichlet energy is D. Substitution at infinite time gives the two claimed limits, not an infinite-time claim of the same rigidity. The supplied checker was inspected, not executed; its finite rational cut, Euler heat and signal tests are supplementary, not the all-time proof.

## originality

PASS

Credit existing stationary cut constants and the general coarea method; the positive-finite-time optimizer split, sharp heat-defect coefficient and two-level equality result in this normalization are not covered by the strongest inspected statements.

## value

PASS

This is a sharp finite-time smoothing-error bound for a natural edge-variation norm. The complete optimizer characterization answers a nontrivial stability question: changing one shore by one vertex selects a persistent optimal orbit from a larger set that would tie in the stationary limit. The exact finite-time weights and integer cut inequalities, not merely the known limits or a general coarea principle, provide that information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
