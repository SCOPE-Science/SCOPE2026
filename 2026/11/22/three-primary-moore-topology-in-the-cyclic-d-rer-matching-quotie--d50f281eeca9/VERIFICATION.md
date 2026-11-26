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

Flags in the barycentric subdivision have distinct vertex ranks. Rotation preserves ranks, so each simplex embeds in the quotient on its closure; two different face deletions cannot be identified because they omit different ranks. This yields a regular CW model with oriented boundaries by alternating deletion, retaining distinct flag orbits even when their vertex orbits agree. I independently reconstructed it without using the supplied verifier or its certificate. Fixed-flag counts for the six rotations are (166087,1,7,115,7,1), and both enumeration and Burnside counting give 27,703 cells with the frozen dimension counts. An independently chosen sequence of free pairs left (115,992,2029,1155) cells through dimension three. A spanning-tree presentation with 878 generators was reduced to the empty presentation by one-occurrence substitutions on the ordered triangle words. Separately, exact integral unit pivots left C0=Z, C2=Z, C3=Z⁵ and a one-row top differential with nonzero entries −3 and 3, hence Smith factor 3 and kernel Z⁴. The result has a 3-dimensional CW model, not a claim that the original orbit-space cellulation is 3-dimensional. By Hurewicz a π2 generator extends over the degree-three Moore space; the Whitehead exact sequence makes π3→H3 surjective, so four sphere maps realize an integral basis. The resulting wedge map is an integral homology equivalence of simply connected CW complexes and hence a homotopy equivalence.

## originality

PASS

The closest claims cover the unquotiented Dürer matching complex and the ordinary full-dihedral quotient. The rational rank four follows from the known rotation character; the integral 3-torsion and cyclic orbit-space homotopy type do not. No exact published result for this cyclic quotient was identified in the inspected sources.

## value

PASS

The Dürer graph has a natural nonfree cyclic action and an already-studied matching complex. Determining the integral homotopy of the ordinary quotient gives a concrete benchmark: the covering complex is a sphere wedge, the rational character predicts the cyclic rank, yet the cyclic quotient carries integral 3-torsion absent from the further dihedral quotient. This is a meaningful exact invariant not obtained by character averaging, and gives a case where the orbit-space topology matters independently of the covering homology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
