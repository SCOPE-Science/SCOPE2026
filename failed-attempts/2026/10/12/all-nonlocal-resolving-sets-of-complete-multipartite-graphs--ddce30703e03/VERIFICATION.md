---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For u!=v in one part, every w outside {u,v} has d(w,u)=d(w,v): it is 2 for a third vertex in that part and 1 for w in another part; u and v alone distinguish this nonedge. Hence all nonedges are distinguished iff at most one vertex is omitted from every part of size >=2, with singleton classes unconstrained. Every such omitted set is a clique. The minimum is N-r because one omitted vertex per class is possible, including singleton classes; when G=K_N this correctly yields dimension 0. Each size-n_i class contributes n_i z^(n_i-1)+z^n_i (n_i>=2), while a singleton contributes 1+z; multiplication yields the given polynomial and the coefficient of z^(N-r) gives the basis count. A wholly separate checker examined 128 complete multipartite isomorphism types, 64,916 subsets, 1,371 minimum bases across orders 2..10; all distance-definition evaluations matched the exact product. The infinite family is proved by the endpoint-only lemma, not the finite check.

## originality

FAIL

The all-set criterion is exactly the statement that the complement of S is a clique of a complete multipartite graph. Klavzar–Kuziak (2022), Proposition 5.1, already proves that the complement of any clique is nonlocal resolving for arbitrary graphs; their Proposition 5.2 proof already gives the endpoint-only obstruction inside an independent twin class. Combining these requires no new hypothesis, structural lemma, or computation. The entire alleged enumerator is z^N times the standard clique polynomial evaluated at 1/z, namely z^N product_i(1+n_i/z), so its coefficients, minimum, and basis count are mechanically preexisting clique counts. This is substantive exact prior mathematical implication, not an unsuccessful-search failure.

## value

FAIL

Complete multipartite graphs and the nonlocal invariant are natural, but the purported classification is just the elementary description of complements of cliques. The factorized size enumerator is literally the reciprocal of the classical clique polynomial, and the basis count is its leading coefficient. Once the endpoint-only false-twin observation and general clique-complement construction are known, every asserted fact follows by independent binomial factors. No new obstruction, computation of an unknown invariant, qualitative boundary, extremal phenomenon, or nontrivial natural classification remains. The rejection is for this specific known-polynomial reexpression and textbook deduction, not for finite or elementary mathematics as such.

The dated certificate retains the supplied scientific assessment, sources and limitations.
