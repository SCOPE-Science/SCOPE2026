---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Every paired-dominating set is total dominating and even, so the published equality gamma_t=q gives the lower bound. The published q-vertex total-dominating set supported in one coordinate is a clique because every pair has zero sum in another coordinate. It therefore has a perfect matching for even q; for odd q, adjoining a vertex with a nonzero second coordinate adjacent to zero gives a perfect matching on q+1 vertices. Fresh direct enumeration on F2xF2, F3xF3 and F3xF5 agrees.

## originality

FAIL

Shariatinia–Maimani–Yassemi already prove that the total-domination number of a finite reduced nonfield product is the smallest field size q and, in the proof, explicitly use S={(a,0,...,0):a in F1} as a q-vertex total-dominating set. Because there is a second factor, S is a clique: any two of its vertices have zero sum in that second coordinate. The audited paired-domination formula is therefore the immediate parity consequence of a published optimum clique witness: S itself has a perfect matching when q is even, and when q is odd one extra vertex adjacent to one member yields size q+1. Under the audit rule that direct corollaries are covered even without identical wording, originality fails.

## value

FAIL

Paired domination is a natural invariant, but in this family the claimed value is mechanically forced by a previously published optimum total-dominating clique plus parity. The extra argument is too routine to constitute a substantive new structural result under the common value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
