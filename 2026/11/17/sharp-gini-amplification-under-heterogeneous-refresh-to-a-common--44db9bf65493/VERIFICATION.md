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

Coarea reduces the norm of every constant-preserving linear operator to cut indicators; convexity of each cut output Gini in the independent rate vector sends global maxima to cube vertices. For a k-versus-m binary input and r selected/s unselected refreshed sites, direct three-level counting gives G(P1_S)=km+[ks(m-k-s)+mr(k-m-r)]/n. For k<=m the r-term is nonpositive and optimizing integer s yields floor((m-k)^2/4); parity-aware comparison across k proves k=1 is optimal, giving M_n=1+floor((n-2)^2/4)/[n(n-1)]. Singleton and endpoint rate witnesses attain the bound. Blending a maximizing rate vector with epsilon>0 uniform refresh gives an all-positive transition matrix and still has amplification if (1-epsilon)M_n>1. Correct n=2,3 equality, n>=4 amplification, and unattained n->infinity 5/4.

## originality

PASS

The global Gini amplification over all independently chosen common-mean refresh probabilities, including a strictly positive Markov counterexample, is not implied by Dobrushin oscillation contraction or spectral mixing of doubly-stochastic gossip. Similar published Gini records concern different kernels.

## value

PASS

A natural distributed averaging family that is positive and unital can increase complete-pair dispersion despite strict Doeblin positivity. The sharp all-n 5/4 envelope and first amplifying size distinguish two inequivalent stability notions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
