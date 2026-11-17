---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

Petersen KG(5,2) has ten 2-subset vertices and 15 disjointness edges. All proper named palette assignments were directly enumerated: 120 at k=3 and 12960 at k=4. Every legal single-coordinate recolouring was constructed, yielding 60 edges at k=3 (every state degree one) and 53280 at k=4. Independent full-source BFS across all 12960 four-colour states found connected graph with radius 13 and diameter 14, eccentricity multiplicities 3360/9600, exactly 44400 unordered diametral pairs, and every one of the stated 14 distance-shell counts. Git source includes a separate 11-orbit construction via S5 and colour-label canonicalization; 11 table orbits sum to 12960. This is an exhaustive finite proof with defined complete adjacency generation, not partial enumeration.

## originality

PASS

The metric of Petersen named four-colour single-vertex recolouring is distinct from known three-colour Petersen Kempe-swap graphs, four-edge-colouring reconfiguration and bounds for arbitrary subcubic graphs. Existing literature supplies chromatic counts and connectivity/mixing bounds but not these sharp metric/orbit and distance-pair spectra.

## value

PASS

A complete exact reconfiguration metric for a canonical 10-vertex graph at its sharp palette transition is a motivated finite classification: the radius–diameter gap and 11 symmetry orbit shell census distinguish structure not recoverable from connectivity or chromatic-polynomial counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
