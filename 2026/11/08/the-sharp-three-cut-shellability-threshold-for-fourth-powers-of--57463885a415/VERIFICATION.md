---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

Definition uses complements of disconnected 3-sets (not independent triples). An independent implementation checked all four complete ordered facet-complement files at n=17,18,19,20 against all disconnected triples (408,528,665,820 facets), verified every preceding-facet ridge-containment shelling intersection, and counted spanning facets 1,10,20,31. All four orders passed with no missing/duplicate facets. Independently enumerated each Alexander dual at n=11..16 and computed exact F2 reduced homology (K nonzero q/r = (5,1),(3,6),(3,40),(3,15),(3,1),(2,3)); duality places these strictly below top dimension n-4 and obstructs pure shellability. n<=10 is void because each vertex has at most one nonneighbor. For n>=21, Theorem 1.4 of Chauhan--Shukla arXiv:2603.23155 yields shellability and wedge counts; no false infinite extrapolation from the four certificates.

## originality

PASS

Best-of-knowledge originality: the exact final claim and its critical new proof or torsion representation are not logically implied by checked stronger/related sources; known numerical/theorem components are explicitly attributed. Inaccessible plausible primary full text is recorded as residual risk and never represented as read.

## value

PASS

Closes all four exact missing boundary orders of the published sharp n=4p+1 shellability conjecture for fixed p=4. Each certificate is a constructive exhaustive shelling order; together with established large-n theorem and low-n obstructions it settles a genuinely motivated infinite threshold and exact wedge formula. The tabulated small-n Betti ranks are acknowledged prior, not presented as novel.

The dated certificate retains the supplied scientific assessment, sources and limitations.
