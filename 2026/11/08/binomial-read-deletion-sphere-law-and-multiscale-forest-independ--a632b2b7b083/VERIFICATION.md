---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Two positional deletions of a finite sequence agree iff the intervening entries form a constant run; the deletion count is 1 plus adjacent changes. Adjacent ell-window Parikh vectors agree iff exiting and entering symbols agree. Thus B_ell=1+sum_(i<=n-ell)1{X_i != X_(i+ell)}. Each fixed-lag graph is a union of paths, so equalities form independent Bernoulli variables by exposing forest roots and fresh child labels. Any cycle violates independence because all edge equalities have probability q^(1-r) rather than q^(-r). Edges from two distinct lags are different and form a two-edge forest, proving zero covariance, while n=3 binary dependence rules out full independence. Independently exhausted q=2,n=5 and q=3,n=4 read sequences, descendant sets, binomial masses, cross-scale covariance. This does not prove the infinite theorem by enumeration.

## originality

PASS

Banerjee et al. 2024 analyze the related binary padded read vector of length n+ell-1 and code redundancy, not the interior unpadded q-ary composition-read output or its complete random deletion-sphere law. The prefix/suffix composition multiset predecessor counts different observations and their deletion multiplicity rather than consecutive sliding reads. Ye–Ge 2026 use ordered ell-mers. Neither these statements nor the reviewed published mathematical findings cover the joint all-lag covariance and exact read-sphere distribution. The graph forest coloring fact is standard and not claimed as independently invented.

## value

PASS

Exact finite-length random deletion-ball statistics for a natural nanopore-style unpadded composition-read channel are useful for average-case ambiguity; the forest criterion identifies why all fixed-lag binomial laws coexist with pairwise covariance zero but non-independence. Scope is all q,n,ell rather than a cherry-picked case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
