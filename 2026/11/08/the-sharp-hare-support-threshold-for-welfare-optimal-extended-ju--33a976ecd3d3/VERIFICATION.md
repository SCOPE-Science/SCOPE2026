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

For q=ceil(n/k), max candidate degree <=q makes all ell>=2 cohesive groups impossible (ceil(ell n/k)>q); hence EJR reduces to JR. If a welfare-maximizing committee has a JR violation, an unselected candidate c must have exactly q uncovered supporters, and all selected candidates have degree exactly q. The kq>=n selected incidences are concentrated on at most n-q covered voters, forcing overlap of at least two selected candidate supports. Removing one overlapping degree-q candidate and selecting c retains welfare and increases covered voters by >=1. A coverage-max welfare optimum cannot violate JR, and iterating stops within <=n swaps. A degree-q+1 family with n=3q,k=3 and distinct groups of sizes q+1,q,q-1 produces a unique welfare-max {a,b,c} that violates JR, whereas {a,b,d} obtains welfare 3q+2. This covers all integer q>=1, including q=1. Independently enumerated 110874 eligible small approval instances up to n=4,m=4 (all k), confirming no welfare-and-coverage-max witness violates JR; theorem relies on the exchange proof.

## originality

PASS

The Hare quota upper bound on per-candidate support and exact degree-(q+1) counterexamples give a structurally new tractable welfare/EJR compatibility regime. Inspected published general welfare/JR price results and unrestricted hardness do not imply this support degree threshold.

## value

PASS

Identifies a natural election sparsity boundary at one Hare quota of supporters per candidate, constructs welfare- and EJR-optimal committees in polynomial time, and proves uniform tightness one supporter beyond. This resolves a genuine fairness–welfare tradeoff on a motivated domain and is not merely a tautological identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
