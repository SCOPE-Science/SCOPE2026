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

For each of the four orders I reconstructed the outer, inner and spoke edges from congruences on unordered pairs and computed shortest paths by Floyd–Warshall. Each landmark yields a bit mask of unordered edge pairs it distinguishes, using the minimum distance to the two endpoints. A landmark subset resolves if its mask union covers every edge pair. Exhaustive enumeration at cardinalities 1–4 recovers, at 2, 3, and 4 landmarks respectively, (0,0,469), (0,0,368), (0,18,1359), and (0,160,3200), and there are no resolving singletons. Upward closure and the positive counts establish all four minima and optimum counts. The original scalar formula is true, not falsified; §6 and Theorem 1.1 of the primary paper support its finite and infinite parts separately. The corrected files at /workspace/repairs/4/ retain the verified census, with no extrapolation.

## originality

PASS

This is a PASS for the repaired multiplicity census only. The frozen presentation's claimed new small-order dimension boundary has an originality FAIL: Wang–Wang–Zhang §6 explicitly gives all four dimensions and attributes order seven via P(7,3) ≅ P(7,2) to Filipović–Kartelj–Kratica. The main theorem's n≥11 hypothesis cannot be read as absence of the small values from the paper. The replacement removes the dimension classification and two-order exception as contributions and attributes them explicitly. The exact multiplicities of all minimum edge-resolving subsets were not in the inspected dimension statements, representative table or strongest distinct indexed comparison.

## value

PASS

The repaired claim counts optimal choices on all four simple cubic fixed-step boundary orders immediately before the stable theorem, including both known lower-dimension orders. These are distinct data even at identical dimension (e.g. 18 versus 160 minimum triples), useful as exact edge-localization benchmarks. The published size theorem does not mechanically give orbits or multiplicities. No scientific value is assigned to presenting the known scalars as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
