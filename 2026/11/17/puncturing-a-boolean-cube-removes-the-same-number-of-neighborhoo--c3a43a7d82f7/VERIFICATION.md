---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Deleting even vertex 0 from Q_n removes the open-neighborhood simplex F0 in the odd-shore complex but all its edges remain through centers ei+ej. For each other center y, three or more neighbors determine y uniquely, so facetwise elementary apex collapses remove all dimension >=3 cells while retaining a 2-complex. The intact parity complex is simply connected via halved-cube generators gi=e1+ei and filled coordinate squares; every deleted triangle {ei,ej,ek} has the explicit 3-triangle disk using w=ei+ej+ek and surviving centers ei+ej,ej+ek,ek+ei, so π1 stays zero. Removing exactly C(n,r) faces for r>=3 changes χ by C(n−1,2), giving ν_n=2^{n−3}(n²−5n+8)−1−C(n−1,2). Hurewicz/Whitehead yields wedge of ν_n copies of S²; the other parity shore is its Dowker nerve and homotopy equivalent. Independent direct enumeration of all source-neighborhood faces for n=3..7, both shores, gives Euler-derived ν=(0,4,25,101,336). This is a bounded check; all n follow from the facet and disk proof.

## originality

PASS

PASS best-of-knowledge for the one-deleted-vertex sphere-wedge classification, exact C(n−1,2) rank loss and equivalence of asymmetric parity components. The 2026-10-11 intact-cube result covers μ_n and the 2-complex collapse mechanism, but not removed triangles or the punctured parity rank. A same-day stronger two-vertex deletion paper includes and explicitly acknowledges the one-puncture intermediate lemma; it is not by itself evidence that the one-puncture finding was previously known independently, though publication priority order needs external confirmation.

## value

PASS

The open-neighborhood homotopy type of a punctured hypercube is a natural stability problem for Lovász complexes. The exact loss of one combinatorially controlled cycle-lattice rank on each different parity component and their shared integral wedge type provide a useful one-defect base case for the already appearing two-defect theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
