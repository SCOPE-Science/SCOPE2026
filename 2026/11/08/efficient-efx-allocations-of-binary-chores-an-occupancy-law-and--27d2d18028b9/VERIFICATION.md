---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For all n>=2, u>=0 and h_i>=0, any misassigned private-zero chore admits a Pareto improvement by moving it to its unique zero-cost owner; all correctly placed private chores attain minimum aggregate cost u even fractionally. Strong chore EFX quantifies over EVERY owned item, including private-zero ones; the exact residual comparison is c_i-1_{h_i=0}<=c_j+h_j for each i!=j. Multinomial occupancy count follows. For two agents the allowable common chore counts are adjacent central occupancies, giving the proved odd-u halving/even-u increase. For symmetric h>=1, the condition reduces to max c-min c<=h, and multinomial CLT of centered counts plus continuity of the Gaussian range and fixed-width Stirling yield the stated scaling and asymptotics. Empty bundles, u=0, and h_i=0 are handled; no arbitrary binary cost matrix is claimed.

## originality

PASS

Prior binary-chore papers prove existence, fairness variants and some weighted existence; they do not establish the occupancy census, parity reversal, or symmetric Gaussian prevalence. A separate contemporaneous bivalued-chore binomial staircase addresses other symmetric two-type positive costs, so neither theorem appears to imply the other. The new contribution is this exact efficient-allocation count for a structured, natural disutility matrix, not general EFX existence.

## value

PASS

Counting fair-efficient allocations and identifying when zero-cost-to-owner items can reverse labeled-outcome counts are natural allocation-theory invariants. A fixed-n sqrt(u) prevalence threshold answers how many efficient outcomes remain strongly fair. The exact quantitative result is not just a restatement of existence; the parity anomaly makes the zero-owned-item quantifier mathematically consequential.

The dated certificate retains the supplied scientific assessment, sources and limitations.
