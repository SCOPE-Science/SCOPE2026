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

For n>=3, each time-two pair of 3-bit columns encodes 64 symbols. Period-two constraints for both phases depend only on triples, so all n-step closed walks in the 4096-vertex two-time de Bruijn graph biject with F_n^2 fixed configurations. Independently assembled all 262144 possible triples, 6140 valid edges and Kosaraju SCCs (4038 total); only cyclic components are (30 vertices,75 internal edges), (27,81) and (4,4). First two are time-diagonal, last has exactly the four directed edges on nodes 455,504,3640,3591. Therefore only four nonfixed returns when 4|n, giving two temporal 2-orbits. Direct original-rule full configurations n=3..6 corroborate. Finite exhaustive graph establishes all ring lengths, unlike mere bounded brute force.

## originality

PASS

McIntosh original Life still-life work explicitly gives the 30- and 27-state fixed-only components for width three; §conclusion states his approach does not calculate period-two patterns. Earlier period-three rigidity and two-row torus results handle different periods/heights, not this complete three-row temporal two-classification.

## value

PASS

Proves a sharp universal spatial rigidity for all circumferences of a natural finite-width full Conway Life system, ruling out localized and partial-column oscillators. The exact unique nontrivial two-time transfer component is a meaningful classification, not a toy observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
