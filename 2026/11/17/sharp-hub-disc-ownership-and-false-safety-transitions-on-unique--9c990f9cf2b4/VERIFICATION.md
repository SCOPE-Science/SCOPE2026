---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The identity D^q(-I+D^{-q}AD^q)D^{-q}=A-I proves spectrum independent of exponent q. A connected unique-hub graph has Perron root sqrt(Delta)<=rho(A)<Delta: Rayleigh vector with hub entry sqrt(Delta) and 1 on every neighbor gives the lower bound even with extra adjacent neighbors, and irreducible strict row-sum bound gives upper bound. Radius R_h(q)=sum_(j~h)(d_j/Delta)^q falls continuously and strictly from Delta at q=0 to 0 for q->infty because all neighbors have smaller degree. It crosses rho(A) and 1 uniquely in the stated order. Disc containment of rho-1 and stable-halfplane threshold follow directly. For star K_(1,n), R=n^(1-q), thresholds (1/2,1), and rho=sqrt(n). Exact analytic reasoning covers all admissible finite graphs; verifier star examples only corroborate.

## originality

PASS

The true spectrum invariance and Gershgorin discs are classical, but the exact one-row ownership and one-row false-safe transition theorem for every unique-hub graph and its arbitrarily severe star discrepancy supplies a sharp scope test of the concrete hub shortcut advocated by Patil--Meena. Their accessible manuscript discusses empirical misclassifications and special diagonal forms, not this exact full graph-class phase diagram. No claim of failure of all-row Gershgorin.

## value

PASS

Directly clarifies a recently proposed hub-only stability shortcut by proving two necessary/sufficient exact thresholds and constructing unbounded false-safe margins on natural star networks; not merely rediscovering diagonal similarity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
