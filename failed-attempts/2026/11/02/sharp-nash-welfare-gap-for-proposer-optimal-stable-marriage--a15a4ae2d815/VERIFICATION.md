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

For any stable alternative changing m pairs, proposer optimality makes each switched man strictly worse, so his utility ratio is at most (n-1)/n, with equality only from first to second. Each switched woman's ratio is at most n, with equality only from last to first. The resulting (n-1)^m bound, positivity and m<=n give the claimed bound and the universal n=2 factor one. For n>=3 equality forces m=n and all stipulated ranks. Disjoint perfect matchings can realize those ranks, one stable by all men's top choices and the other by all women's top choices. Each man has a unique second choice, so the Nash maximizer is unique at equality. The matchings and residual list orders give the stated labeled count without duplication and division by (n!)^(2n) gives the probability. Mutual first choices in a bijection force the only stable matching and attain the lower bound. An independent exhaustive replay obtained factors 1 and 8, with 16 and 12 extremal profiles for n=2 and n=3, respectively, and checked the n=3 extremizer ranks and uniqueness.

## originality

FAIL

The distinct earlier Resultary finding 2026/10/25/SCOPE-sharp-nash-welfare-loss-under-proposer-optimal-stable-marriage--1c548a8406a6 establishes all central assertions for exactly the same stability, baseline and positive rank utilities. It also attains its stronger bound for each feasible number of changed pairs. The frozen relationship section does not account for this coverage. No distinct surviving result was established.

## value

FAIL

The exact stable-baseline loss and equality census are meaningful questions, but this submission does not add a distinct comparison, census, characterization, or method beyond the earlier finding. The independently reproduced three-pair number is also already explicitly reported, and the all-size argument is already subsumed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
