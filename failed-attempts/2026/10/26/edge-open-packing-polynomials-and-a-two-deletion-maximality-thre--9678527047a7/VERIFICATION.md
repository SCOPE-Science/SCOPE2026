---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Incident edges are always compatible in the bipartite graph. Disjoint edges are compatible precisely when their two cross edges are missing, which makes them a unique reciprocal pair. A third compatible edge would have to intersect both, hence be one of the missing cross edges. All other packings of size at least two are subsets of a star with unique center, and minimum degree two rules out empty or singleton maximal packings. This proves both polynomials and the exact extrema on substituting p=q. Inclusion-maximal sizes first differ at one deletion; it takes two deletions for the minimum to drop to two when n>=4. An independent definition-level compatibility search matched both polynomials in all 78 triples with 3<=p,q<=6 (15,961 sets). For (4,4,2) the coefficient lists from degree zero are [1,14,37,20,4] and [0,0,1,4,4].

## originality

FAIL

The entire frozen claim is covered by a distinct indexed Resultary record, not merely by the scalar maximum literature. Its exact enumerators and proof include the reciprocal-pair classification on the same domain, and the displayed maximal polynomial immediately gives the balanced threshold even in sizes not highlighted by its prose. This is a finding of equivalent coverage and no surviving distinct contribution here, not an inference of chronological priority from catalog dates.

## value

FAIL

The maximal-size distribution is naturally motivated by the large gap between maximum and smallest maximal packings after just two deletions. However, as an additional result the threshold and the enumerators add no exact invariant or structural witness beyond the already covered identical indexed theorem; the balanced gap is a direct reading of its maximal polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
