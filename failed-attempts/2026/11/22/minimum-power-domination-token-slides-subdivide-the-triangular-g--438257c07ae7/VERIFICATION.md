---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The residual graph records exactly the initially unobserved subdivision vertices; a residual cycle prevents the first force onto any of its edges. With an original selected, observed incident subdivision vertices enable observation of all originals and then leaf-edge forcing observes a residual forest. With only subdivision vertices selected, every residual leaf or isolate is initially observed, because it has at least n-2 incident selected subdivisions; when an observed leaf forces its residual subdivision, that subdivision can in turn observe the other original endpoint, preserving the observed-leaf invariant under peeling. The forest criterion thus holds even without a selected original. Inclusion-minimality excludes redundant subdivisions incident to selected originals and requires the residual forest on r>=2 missing originals to be connected (otherwise an inter-component selected edge can be unselected). Conversely, adding an edge to that residual tree creates a cycle, and unselecting an original adds a universal vertex to the tree, creating a triangle. This proves the tree form and size n-2+binomial(r-2,2), minimized only at r=2,3. The triple-edge state can slide its unique subdivision token to either endpoint, and no other optimization-preserving move exists because each slide changes the number of selected originals by one. The missing pair and triple-edge maps therefore identify precisely the vertex–edge incidences of J(n,2). Its degree 2(n-2) yields the stated counts and the n=3 cycle. In the subdivision, distances are doubled endpoint distances plus one per midpoint, minimized over the midpoint's endpoints. A disjoint pair and support triple are possible from n=5, and disjoint support triples from n=6; these give distances five and six, respectively. For n=4 every support triple meets every pair and every other support triple, bounding distances by four, attained by midpoints of (12,13) and (24,34); n=3 gives diameter three. Thus the diameter and degree claims hold for all n>=3.

## originality

FAIL

The other frozen slide record, 4, gives the identical labelled all-order graph isomorphism and diameter under precisely the same move restriction; its radius and eccentricity results even go further in describing that same graph. Here the explicit degree counts are immediate from subdivision of the regular Johnson graph. The additional all-set forest characterization has independent same-family coverage and follows from earlier fort theory combined with closed-neighborhood zero forcing. The inclusion-minimal tree form is a short consequence of that criterion; it does not sustain a distinct slide theorem. No priority order is inferred between same-day records.

## value

PASS

The shared labelled slide-graph classification, considered as one theorem, is structurally useful: it gives a model for local minimum-sensor moves whose alternation and distances are invisible in the optimizer count or unrestricted-jump graph. The explicit degree and small-order statements are useful consequences but do not justify a separate contribution, and the supporting tree form alone does not provide a distinct motion classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
