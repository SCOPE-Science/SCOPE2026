---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Independent continuous endpoint pairs give a uniform rank matching with exchangeable edge labels. The Dirichlet gap moments give each conditional crossing/nesting probability mean 1/3 and second moment 2/15, and their mixed moment is 1/9. For distinct overlapping edge-label pairs this is exactly the joint success probability, hence gives Bernoulli independence; disjoint pairs have independent endpoints. Only the same-pair covariance −1/9 remains in the sum. For a single statistic, its pair variance is 2/9 and the n(n−1)(n−2) ordered overlapping distinct pairs each contribute 1/45, giving the stated variance and correlation (undefined at n=1). The first Hoeffding projections have joint covariance I/45; the canonical two-edge remainders are orthogonal off the diagonal and O(n²) in second moment. The bivariate iid CLT and Slutsky therefore give the stated independent Gaussian coordinates. A separate exact enumeration of n=2 through 6 agrees (replay: /workspace/branches/f2a0bb80-6f85-48ed-958d-580163425b90/independent_enum.py; output independent_enum.txt). The frozen script was inspected, not run; neither run proves the limit.

## originality

FAIL

Multiple distinct catalogue records give the same moments, exact mixed covariance and independent Gaussian limit for the same total two-edge counts, on the same uniform law. The explicit distinct-label Bernoulli statement is also implied by the earlier mixed-projection calculation. This is demonstrable equivalence, not an inference of priority from a date.

## value

FAIL

Exact dependence and the joint limit are useful facts, but this record supplies the existing formulas and essentially the existing proof. The explicit local Bernoulli statement follows mechanically from the earlier projection calculation and does not motivate a separate repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
