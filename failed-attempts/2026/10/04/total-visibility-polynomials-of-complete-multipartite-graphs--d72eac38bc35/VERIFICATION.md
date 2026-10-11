---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

The structural condition is correct. The only distance-two pairs are pairs in the same non-singleton part \(V_i\), and their common neighborhood is exactly \(V(G)\setminus V_i\). Hence a set \(X\) is total mutual-visible exactly when its complement \(Y\) meets \(V(G)\setminus V_i\) for every non-singleton part, equivalently \(Y\not\subseteq V_i\) for every such part. Weighted inclusion-exclusion over the disjoint partite classes gives the polynomial. Inclusion-minimal admissible complements are exactly a singleton from a singleton part or, when at least two non-singleton parts exist, a two-set meeting two distinct such parts. The resulting maximal-set counts and lower number follow. A fresh independent check for profile \((2,2,1)\) gave coefficient vector \((1,5,10,8,1,0)\), agreeing with the formula; the frozen verifier checks every multipartite isomorphism type through order nine.

## originality

FAIL

Bujtás--Klavžar--Tian prove the stronger all-graph characterization: \(X\) is total mutual-visible iff for every distance-two pair \(u,v\), the common neighborhood \(N(u)\cap N(v)\) is not contained in \(X\). Specializing this theorem to a complete multipartite graph immediately gives the submitted complement condition because same-part pairs are the only distance-two pairs and have common neighborhood \(V\setminus V_i\). Their Proposition 3.2 already computes the total visibility polynomial for balanced complete bipartite graphs and explicitly notes that general \(K_{m,n}\) is obtained similarly. After the general criterion, the arbitrary-multipartite formula is one inclusion-exclusion step and the maximal-set theorem is the elementary classification of inclusion-minimal complements satisfying that condition.

## value

FAIL

The graph family and invariant are natural, but once the published all-graph distance-two criterion is specialized, the polynomial is elementary inclusion-exclusion and the maximal-set/lower-number statements are the minimal transversals of a disjoint family of partite powersets. This does not add a nonstandard structural lemma or a sufficiently independent exact invariant beyond the stronger prior theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
