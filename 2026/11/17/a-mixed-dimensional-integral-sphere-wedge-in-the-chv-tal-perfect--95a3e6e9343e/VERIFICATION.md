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

Chvatal graph was fixed by the 24 explicit edges in RESULT.md; an independent vertex-recursive perfect-matching enumerator found exactly 52 six-edge perfect matchings, hence 1,880 faces including empty, cardinality-vector (1,24,204,612,675,312,52). Independent full face-poset toggle matching pairs 930 pairs, leaving one 0-cell, 17 2-cells and one 3-cell. Every one of 6,816 nonempty Hasse arrows was checked acyclic by topological ordering; independently signed Morse projection of the sole critical 3-cell onto the 17 2-cells vanishes over Z. The two-skeleton is wedge 17 S2; pi2 equals Z^17 by simple connectivity/Hurewicz, so the 3-cell attaches trivially. Result: integral wedge of 17 S2 and S3. A pure 5-dimensional shellable complex could not support nonzero lower-degree reduced homology, hence nonshellability. The graph is not the ordinary matching complex.

## originality

PASS

Bayer-Jelic Milutinovic-Vega introduce perfect-matching extendability complexes but classify honeycomb families; Chvatal is not in those families. The previously published Chvatal ordinary matching-complex theorem is a different simplicial complex admitting partial matchings not contained in any perfect matching; its Z/3 Moore summand cannot logically settle the perfect-extendibility complex. Other exact graph cases are adjacent examples only. The identical November 17 Resultary mirror is the current package, not independent prior support.

## value

PASS

A pure extendability complex with homology in dimensions 2 and 3 and an explicit integral sphere-wedge splitting is a nontrivial structural example for perfect-matching complexes. The certified nonshellability at dimension five is a sharp qualitative distinction from tabulated matching counts and can inform future graph-family classification; the result is finite and self-contained.

The dated certificate retains the supplied scientific assessment, sources and limitations.
