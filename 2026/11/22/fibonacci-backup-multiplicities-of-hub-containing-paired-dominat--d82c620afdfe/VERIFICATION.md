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

The hub supplies domination but must use exactly one matching edge. For a proper rim selection, its endpoint lies in the sole odd path, and it must be at an odd position so the residual pieces have even orders. The even pieces each have one matching, giving a+1 choices on a run of length 2a+1. Full rim yields n choices if n is odd, zero otherwise; a hub singleton has no matching. The labelled starting point of the distinguished odd run is unique, so no rotation quotient occurs; the odd run with a positive following gap gives A and each subsequent even run with positive gap gives E. The geometric series yields the whole bivariate census, with y raised to the per-set count. At z=y=1 the proper factor simplifies to x²/(1−x−x²); for y-degree one its factor is x²(1−x²)/(1−x−x²). Counting witnesses by the spoke followed by arbitrary matchings of the remaining path gives nF_n; this is not a third count of vertex sets. Ratios and multiplicity support follow, including n=3,4. Independently enumerated global matchings projected to their endpoint sets and compared every joint coefficient through rim size 17: python3 /workspace/evidence/3-matchings.py. Reviewed VERIFICATION.md, the two supplied checkers and their recorded output without executing them; the recorded Python totals include hub-free sets, whereas the independent check groups only hub-containing sets. The proof is all-order, not an extrapolation.

## originality

PASS

The supported distinct result is the complete joint distribution by size and per-set perfect-matching multiplicity in labelled hub-containing wheel sets. Existing paired-domination minimums and matching counts by witnesses are partial information only. The elementary nF_n witness bijection is not a separate priority claim about the wheel matching polynomial.

## value

PASS

For a fixed selected set, alternative perfect pairings are a physically interpretable redundancy count distinct from either selected-set size or total witness count. The exact joint distribution separates uniquely paired deployments from those with alternatives over a natural infinite family, with explicit exception, support and limiting proportions. It does not establish resilience to an arbitrary specified edge or vertex failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
