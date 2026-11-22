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

The proof in RESULT.md is symbolic and covers every complete bipartite graph \(K_{a,b}\) with \(a,b\ge2\). The executable `verify_partial_biclique.py` directly enumerates small partial induced-automorphisms and checks them against a distinct closed formula; in particular it checks \(K_{4,4}\) versus \(K_{2,6}\), the finite sharpness family up to \(h=19\), and absence of low-rank signature collisions within \(4\le n<100\). It also certifies the two polynomial identities by exact rational evaluation on interpolation grids large enough for their stated bivariate degree bounds. Its expected terminal result is `BICLIQUE_PARTIAL_AUTOMORPHISM_CHECKS_PASSED`.

Finite tests do not establish the infinite theorem; the reconstruction uses exact factorization of the rank-four polynomial and the universal inequality \(8t^2<n(n-1)\) under both-product feasibility. Only a self-review was conducted; independent validation and external audit have not been performed. Some relevant indexed repository sources were accessible as published summaries but not as complete texts, leaving a documented literature-priority risk.
