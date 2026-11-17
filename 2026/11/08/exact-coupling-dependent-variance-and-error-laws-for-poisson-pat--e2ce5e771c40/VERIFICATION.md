---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

For a jump in cell phase v and offset u the exact error mark is w(v,u)=v−1_{u<v}. Its phase mean is u−1/2 and phase square mean u²−u+1/3; conditional Poisson variance decomposition and each U_i uniform yield λ/6+λ² Var(sum U_i)/n² for any coupling. For even n, (V,1−V) pairs force constant sum. Independent offsets assign each isolated jump an independently uniform mark; double-jump cell collision probability ≤λ²/(2n), and two-cell-block collision probability ≤λ²/n for paired design, yielding triangular compound-Poisson TV bounds. Shared U yields a conditionally uniform jump on [U−1,U], exactly resolution invariant. Direct independent rational uniform moments and 9 variance-order cases corroborate without proving the all-n theorem.

## originality

PASS

Best-of-knowledge PASS: elementary Poisson random-measure calculus and independent jittering are standard, but the exact arbitrary-dependence variance functional, attained pairwise coupling floor and three mutually distinct scaled error laws are not consequences of the inspected cited results as written. No broad precedence certification; specialized Monte Carlo sampling literature could imply portions.

## value

PASS

A natural numerical integration problem for a discontinuous random path: the dependence structure changes leading-order mean-square error even with unchanged uniform marginals, and an explicit attainable lower bound guides stratified sampling design. The distributional distinction prevents using variance alone as a full error description; this is a motivated exact coupling optimization rather than arbitrary finite slicing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
