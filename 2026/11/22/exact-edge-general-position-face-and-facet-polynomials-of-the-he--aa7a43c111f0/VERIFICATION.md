---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

In the Fano incidence graph the unique-line and unique-intersection axioms give distance 2 within each part, and distances 1 and 3 across parts. A nonincident point/line pair has three length-three geodesics; their edge triples are distinct because the endpoints and middle edges can be recovered from the path. Thus it is necessary and sufficient to avoid the 84 forbidden triples. The printed highest-index recurrence tests all subsets, and one-edge addability exactly tests maximality by heredity. I independently used nonzero vectors and covectors in F_2^3 with dot-product incidence (not cyclic line labels); all length-three simple paths are geodesics because an endpoint shortcut would form a four-cycle. The replay python3 /workspace/branches/audit_exact_124.py 4 marks all supersets of the 84 forbidden triples, then scans all 2^21 subsets with an explicit one-edge extension test. It gives face coefficients 1,21,210,1246,4725,11592,17962,16446,7875,1617,84, then zeros, and only facet coefficients 66,546,861,84 at sizes 7–10. Totals 61779 and 1557 agree, and labelled maximum sets have cardinality 10 and count 84.

## originality

PASS

The supported distinct finding is the complete labelled face and inclusion-maximal facet census for the Heawood edge-general-position complex. Primary definitions and exact extremal numbers for other graph families are prior, and a table of maxima alone would not subsume the two enumerators. The strongest located exact match was the identical published record, not a distinct prior. Bounded searches and full-text access limitations preclude a claim of global priority.

## value

PASS

The Heawood graph is the canonical smallest projective-plane incidence graph, and the face/facet distributions of its geodesic-triple obstruction complex are meaningful beyond its extremal number. The labelled census is an exact test case for enumeration algorithms and shows quantitatively that saturation can occur at three smaller cardinalities than the maximum. The 84 maximum sets alone would not provide this information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
