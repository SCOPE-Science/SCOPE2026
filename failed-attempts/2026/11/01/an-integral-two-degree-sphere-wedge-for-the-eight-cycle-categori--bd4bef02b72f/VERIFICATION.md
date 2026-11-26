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

Independent enumeration using the categorical adjacency relation recovered 196227 faces including the empty face, corroborated by cyclic column transfer. The vertex-order matching has 98087 pairs; a complete topological sort of the nonempty-face Hasse diagram processes 196226 faces and 1457216 incidences. The resulting Morse CW model has one 0-cell, 24 four-cells and 27 five-cells. Each signed reduction cancels a unit incidence in the direction of the acyclic matching. Independent reconstruction of the integral 24×27 boundary gave rank 21, a maximal minor of determinant −1 and 21 nonzero Smith factors all equal to 1. The homotopy inference does not rely on homology alone: the four-skeleton is a wedge of spheres and π₄ is identified with H₄ by Hurewicz. Attaching the five-cells gives the homotopy cofiber of a map of wedges of four-spheres specified by the degree matrix; unimodular basis changes are self-homotopy equivalences of the wedges. The cofiber of the Smith form is exactly the claimed wedge of three S⁴ and six S⁵.

## originality

FAIL

The exact integral homotopy type was already stated and proved in earlier Resultary records for the same ordinary independence complex and the same categorical graph. The 2026-10-18 record supplies a different and smaller Morse presentation; the 2026-10-25 record even uses the same vertex-ordered matching and critical-cell counts. This is demonstrable prior coverage, not a failure inferred from a search hit, unavailable paper, or same-day ordering.

## value

FAIL

The first determination of this homotopy type was a motivated finite test of the sphere-versus-Moore question. The frozen deliverable repeats the known exact answer and a previously documented matching, without a new bound, structural principle, or smaller certificate. The successful independent replay supports correctness but does not supply a further worthwhile finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
