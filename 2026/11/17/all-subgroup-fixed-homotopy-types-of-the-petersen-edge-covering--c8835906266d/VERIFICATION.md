---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Petersen P=KG(5,2) has 10 vertices, 15 graph edges, and edge-covering M2(P) is the complex of subsets of those edges avoiding all ten degree-three stars. For a subgroup H≤S5, barycentric coordinates of a geometric H-fixed point are constant on each H-orbit of the 15 edge-vertices. The simplicial orbit-union complex of allowable orbits is therefore PL-homeomorphic to the fixed locus; this is NOT a quotient nor only individually fixed vertices. The frozen standard-library verify.py builds all 120 permutations and multiplication/inverses, closes generated subgroups to 156, conjugacy classes to 19, enumerates exact allowed orbit-union faces and performs ordered matching on augmented face posets. For every representative, it verifies matched cover incidences and topologically sorts the full Hasse graph with matched edges reversed, establishing acyclic matchings. The critical counts by class yield one 4×S7 for the identity, 10 subgroups of 2×S3, 20 S1, 48 S0, 75 contractible points and two empty fixed loci (A5, S5); sums 156. For positive-dimensional CWs all critical cells appear in a single positive degree with one base cell, giving wedge spheres, while the augmented empty-face convention distinguishes S0 and void. The finite classification was independently recomputed from the frozen proof algorithm by fresh subgroup closure, orbit-face enumeration and full directed Hasse acyclicity checking: 156 subgroups/19 classes, with exact six-category census (1,10,20,48,75,2). All loops and cases are finite; no infinite extrapolation is made. Ordinary K≃4S7 is prior and not a new finding.

## originality

PASS

Best-of-knowledge PASS: geometric H-fixed topological classification for all 156 S5 subgroups of edge-covering M2(P) is not furnished by prior nonequivariant wedge homotopy or H7 standard representation; a very close Petersen induced-forest fixed-point theorem applies to a different simplicial vertex set (10 graph vertices rather than 15 graph edges).

## value

PASS

All-subgroup geometric fixed-point homotopy types form a natural equivariant topological fingerprint of the canonical Petersen 2-matching/edge-covering complex. The exact 156-subgroup table distinguishes spheres, discrete sets, contractible and empty fixed loci, information invisible in ordinary rational S5 homology. A complete classification on this well-studied symmetric complex is a motivated exact result despite being finite.

The dated certificate retains the supplied scientific assessment, sources and limitations.
