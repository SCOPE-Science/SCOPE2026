---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For the explicit 20-edge 11-vertex Mycielski graph, independently enumerated all 12480 proper labelled 4-colour states via pentagon/apex/shadow constraints; built all 45240 legal one-vertex recolour edges. Components have 6240 vertices each, and symmetry action S4 x D5 has 56 orbits (48 size 240, 8 size 120). One exact BFS per orbit determines all source eccentricities and pair distances, giving radius15, diameter17, global eccentricities 15:2160,16:10200,17:120 and 60 diametral unordered pairs. Exactly one 120-element orbit is peripheral, and each member has one antipode. This is exhaustive finite proof, not extrapolation to other graphs or palettes.

## originality

PASS

The Oct26 published paper covers the state count, 2x6240 components, 45240 edges, diameter17, degree histogram and palette/dihedral exchange; these are PRIOR premises. The new, narrower mathematical information is the complete radius/eccentricity distribution (radius15), 60 diametral pairs, uniqueness of antipode for all peripheral colourings, and single peripheral symmetry orbit. These are not consequences of component counts/diameter/degree alone and were not stated/proved in the inspected Oct26 result. The true final RESULT includes the new precise peripheral theorem, so it survives without changing the mathematical claim; the audit explicitly corrects novelty attribution. Residual unindexed metric-census risk remains.

## value

PASS

For the 4-chromatic triangle-free Grötzsch graph at its exact critical palette, the otherwise-known disconnected reconfiguration graph has a nontrivial peripheral geometry. The exact radius, eccentricity census, 60 diametral pairs and unique antipode orbit form a natural complete extremal-metric classification not read off from the previously known diameter and degree histogram; no general-family claim is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
