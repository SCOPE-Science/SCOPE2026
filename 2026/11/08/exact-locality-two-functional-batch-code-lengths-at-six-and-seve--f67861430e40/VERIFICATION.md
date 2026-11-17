---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For each nonzero request a, three distinct disjoint XOR-pair types and singleton copies give the exact equal-request capacity M_a=x_a+sum_{b<c,b XOR c=a}min(x_b,x_c). Summing all a gives 4n-(1/2)sum_{b<c}|x_b-x_c|; balanced integer multiplicities minimize discrepancy r(7-r), giving total capacity at n=11 of 38<42 and at n=12 of 43<49. Padding excludes all shorter lengths. The pinned full 66,621-byte recovery_witnesses.json was read and an independently written 2640-case mixed-request enumerator checked all masks, disjointness, max-two size, and exact XOR (924 for t=6,1716 for t=7; zero invalid). The 12/13-column generators contain a binary basis. This is an exhaustive finite certificate for exactly these two parameters, not an infinite-parameter extrapolation.

## originality

PASS

The exact locality-two six/seven request optima are not determined by known unrestricted or locality-three constructions; the restricted certificate is a genuine new finite computation and proof at natural neighboring request counts. Extensive comparison with the same-object 2026 locality-two primary work and earlier published length-eleven six-request theorem found no same statement or theorem implying both length values.

## value

PASS

The minimum storage length under a strict two-symbol recovery budget is a natural and operationally meaningful parameter, and six and seven are consecutive nontrivial batch-load cutoffs. Exact tight lower bounds plus all mixed-request recoveries resolve a finite problem that unrestricted or locality-three results do not settle. Generalization or paper-sized theory is not required for the precise finite optimal values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
