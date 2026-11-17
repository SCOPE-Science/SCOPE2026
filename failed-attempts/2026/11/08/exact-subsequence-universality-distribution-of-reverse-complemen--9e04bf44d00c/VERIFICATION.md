---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The greedy-arch factorization of a q=2m fixed-point-free reverse-complement half-word v yields iota(v theta(v^R))=2k+1 when the residual alphabet plus its complement covers Sigma, otherwise 2k. Exact-support surjection generating series B_s(z)=s!z^s/∏(1-hz) imply F_q(z,u)=(T_q(z)+(u-1)R_q(z))/(1-u²A_q(z)), where A=qz B_(q-1), T=Σ_{s<q} binom(q,s) B_s and R=Σ_{s=m}^{q-1}binom(m,s-m)2^(q-s)B_s. The minimum full symmetric length is qj and count q!^(j/2) for j even, or q!^((j-1)/2)2^m m! for j odd. Independently enumerated all half-words q=2 through n=8 and q=4 through n=6, checking the exact arch index and GF histograms, supporting the all-index proof. C PASS.

## originality

FAIL

An earlier 2026-11-02 published theorem for mixed alphabet involutions (f>=1 fixed letters and d>=1 swapped pairs) already gives the same general symmetry-midpoint lemma, full arch/surjection rational enumerator, and exact support-correction formula. Its even-length term, after the formally immediate specialization f=0,d=m and a half-length variable y=z², is IDENTICALLY (T+(u-1)R)/(1-u²A) in the submitted finding; the qj shortest count likewise follows from the same minimal arch and pair-transversal argument. The prior theorem explicitly excludes f=0 from its stated scope, so this is a boundary extension of its proof rather than a formal instance of its hypotheses. But no new mathematical idea, nonstandard lemma, classification mechanism or distinct invariant survives: the entire reported result is the mechanically extendable f=0 endpoint, which was acknowledged as a related known pure type. O FAIL under the explicit anti-renaming/substitution bar, not merely a failed literature search.

## value

FAIL

Watson–Crick fixed-point-free symmetry and exact universality index are natural and the formula is correct. However, as submitted the complete distribution and shortest-count theorem are direct one-boundary specialization of the earlier full midpoint and support-count argument with odd central letters removed. The extra algebra has no separate motivated structural advance beyond that older mechanism. V FAIL as a standalone new result; this does not imply that the endpoint object itself is uninteresting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
