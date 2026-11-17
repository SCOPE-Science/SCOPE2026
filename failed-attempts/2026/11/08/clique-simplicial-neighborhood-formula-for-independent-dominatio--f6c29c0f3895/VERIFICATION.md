---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The exact bijection is mathematically sound: in the central graph each independent dominating set intersects original vertices in a clique A. A subdivider of edge uv must be selected exactly when neither u nor v is in A. An unselected original vertex v is undominated precisely when N_G(v)=A, so admissible A are all cliques except distinct open neighborhoods of simplicial vertices. The set cardinality is |A|+e_G(V\A), which equals |A|+m−sum_{v in A}deg(v)+binom(|A|,2) for a clique. The triangle-free min-degree>=2 and multipartite cases follow by elementary clique restriction. Independent checks read actual source verifier and reconstructed the bijection on representative isolated, complete and triangle-free graph cases; no finite test is an all-graph proof.

## originality

FAIL

FAIL decisively: the 2026-10-18 published full RESULT.md "Clique-indexed independent-domination polynomial of every central graph" proves precisely the SAME all-graph admissible-clique bijection and polynomial with exponent written using degree sum. The current simplicial-neighborhood correction is exactly the complement of its condition N_G(v) != A, not a different classification. A separate 2026-11-02 result proves the complete same triangle-free polynomial and 1+n+m count. There is no surviving independent theorem after comparison of implications.

## value

FAIL

FAIL because the main complete polynomial and all-set bijection are already fully known; the distinct-neighborhood exclusion is a direct restatement of the earlier inadmissibility predicate and the multipartite and triangle-free formulas are substitutions/counts from the prior exact all-graph polynomial. Reproducible code, alternative notation, and correct calculations do not create distinct scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
