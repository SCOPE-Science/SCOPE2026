---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The result follows from a proved finite-state classification of three concurrent membership scans, a verified four-orbit quotient, the polynomial identity \((I-tQ)v(t)=D(t)\mathbf1\), and a reset-word renewal decomposition. This suffices for all integers \(n\ge1\).

Run `python3 verify_catalan_triples.py` using Python 3 with no third-party dependencies. The checker's success marker is `CATALAN_TRIPLE_COMMUTANTS_OK`. It performs an exhaustive direct-map composition enumeration of ordered commuting idempotent triples through \(n=8\), independent weighted rank-table comparisons through \(n=6\), and a separate recurrence check of all common-product ranks through \(n=8\). The exact polynomial certificate is checked with integer coefficient arithmetic.

Finite checks do not establish the infinite theorem by themselves, and the checked literature cannot establish absolute historical originality. Independent mathematical audit has not been performed.
