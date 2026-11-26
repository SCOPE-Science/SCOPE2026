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

FAIL

The proof establishes lexicographic sharpness (voters, then seats, then candidates), not the Finding's unqualified claim that the five-candidate count is sharp within nonwasteful outcomes. Four candidates suffice even with both strict-core stability and Pareto efficiency: take winners a,b,c, sole challenger x, and ballots ax, ax, ab, ac. Both x-supporters have utility 1 and their largest coalition has 3|T|/4=3/2<2, so ordinary EJR+ holds. All four full-coalition payments are 1/4+1/2=3/4, so the strict payment test fails. The final two voters are fully satisfied, and subsets of the first two cannot afford two seats; maintaining the last two utilities forces all winners. Thus global candidate minimality is false; if the finding is meant only at the minimum electorate, the mathematical boundary survives. The three-voter witness separately checks: its profile has utility (2,2,3); challenger e has two supporters with 3>8/3; the full-coalition payments are all 4/3. The fully satisfied voter and the two-seat budget of the remaining pair certify the strict core; Pareto dominance would need all five candidates. For n=2, the one-supporter full-coalition case contributes total k+1 by nonwastefulness, and the two-supporter case is protected by ordinary EJR+ after dividing by two. For n=3 and k≤3, the guaranteed score floor(ka/3)/3+1/a exceeds k/3 for each a=1,2,3, even permitting waste. At n=3 the first possible k is thus four and then m≥k+1. Replicating each of the three voters (two distinct ballots) scales the full-coalition payments and entitlements by 1/r, while the x-supporting share and maximum budgets are unchanged. The independent exact replay `python3 /workspace/review-evidence/independent_finite_checks.py 1` confirms both witnesses and replications r=1,2,3; the general conclusions use the analytical arguments, not that finite run.

## originality

FAIL

A distinct Resultary record gives the identical three-voter witness up to relabeling and a broader sharp eight-entity theorem with a boundary census. Its proof includes the same nonwasteful n≤2 theorem and excludes n=3,k≤3 by bounds that do not actually use nonwastefulness. It also gives the four-candidate witness that disproves the unqualified candidate claim. The original's strict-core and replication observations are straightforward consequences of the explicit known profile and the inequalities, not a new boundary yielding a separately valuable finding. This establishes exact coverage of the substantive corrected claim, not chronological priority. The original qualifying premises and the already published general separation are distinguished below.

## value

FAIL

The motivated exact small boundary and role of the nonsupporting voter are scientifically useful, but the distinct boundary census and identical profile already supply them. On the supported lexicographic reading, the only additions are an immediate strict-core check of that profile and uniform rescaling of its ballots. They do not leave a separately valuable unresolved claim; the unsupported global five-candidate claim cannot be salvaged as stated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
