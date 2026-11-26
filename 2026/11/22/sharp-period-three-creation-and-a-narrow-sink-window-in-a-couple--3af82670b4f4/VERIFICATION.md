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

Put v=3y/2, c=3b/2, t=x(1−x), and z=c²t. The two third-iterate residuals f=X−x and g=V−v satisfy g−f=ct[c(1−2x)−z−1]−2(1+z)v. If z=−1 their common zero would force x=1/2, impossible. Substitution of the unique v annihilating g−f gives f=−ct H_s(z)/(4(1+z)²) with H_s(z)=z³−(s+3)(z+2), so reconstruction is exact and t=0 gives only the two fixed points. The discriminant is 4(s+3)²(s−24); H_s(0)<0 and H_s(s/4)=(s−24)(s+4)²/64. Below threshold the sole real root is above s/4. At threshold the roots 6 and −3 (the latter double) give exactly three distinct nonfixed points. Above threshold the two negative roots are admissible and the positive root lies below s/4, so there are six nonfixed points. Their primitive period divides three and is not one. Direct multiplication of the step Jacobians gives τ=1−c Σ(2x_j−1) and Δ=c³∏(2x_j−1); independent exact polynomial reductions verify (τ−1)²=s−24 and Δ=(s+4)(τ−1). The six x-values pair under x→1−x and sum to 3, so the two return traces sum to 2; this proves both signs occur without assuming that reflection conjugates the dynamics. The negative branch has its characteristic polynomial negative at 1 and hence a real multiplier >1. The positive branch meets the first two strict Schur inequalities, and the third is equivalent to (s+4)√(s−24)<1. That quantity increases strictly; at equality Δ=1 and 0<τ<2 give a unit complex pair, and afterward Δ>1 gives instability. At s=24 the multipliers are 1 and 0.

## originality

PASS

The same two-parameter map is published, but the inspected original statements cover fixed-point and period-two behavior, not this census or its Floquet window. The nearest distinct indexed creation-and-sink formulas are for genuinely different three-dimensional maps whose three-cycles reduce to a scalar quadratic iteration.

## value

PASS

Unit self-coupling is the no-decay drift in the published family: increments telescope around a cycle and the cyclic sum of the quadratic feedback vanishes. On this structurally distinguished section, the count is exhaustive and it resolves the difference between mere creation of a real cycle and its very short interval of Schur stability. The exact multipliers and boundaries are usable benchmarks in this family, not numerical examples or a generic bifurcation claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
