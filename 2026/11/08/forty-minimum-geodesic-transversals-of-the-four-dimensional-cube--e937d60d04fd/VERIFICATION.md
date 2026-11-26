---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Every shortest path flips distinct coordinates; if any coordinate is unused the path can be extended, so the maximal paths are exactly the antipodal ones. Each ordering traces a maximal Boolean-lattice chain, which can be translated to any starting vertex. Their 192 vertex sets were generated independently; all 4,368 five-subsets fail and exactly 40 of the 8,008 six-subsets hit them. Upward closure excludes smaller sizes. The distance-intermediate-value argument applies to the middle spheres and to the Q3 projections, establishing the two constructions. The successful masks are exactly the eight spheres and 32 lifted neighborhoods. Independent replay checked all 50 certificate orbits, disjoint complete coverage, and each of the 48 disjoint-path witnesses. Translations and coordinate permutations are transitive on each family, and the induced independence vs matching distinguishes them. Replay: python3 /workspace/review_evidence/cube.py.

## originality

PASS

The claim credited as distinct is the exhaustive labelled census and the two-orbit classification, not the minimum six or the known middle spheres. The strongest plausible compatible earlier statements inspected establish the minimum and give an extremizer but do not classify the minimizers. A later Resultary record explicitly treats the forty minima as known starting states. The conflicting earlier preprint claim of eight is not compatible coverage.

## value

PASS

At a natural first small case of the hypercube transversal problem with a known sharp minimum, identifying all equality cases resolves whether the standard layer construction is forced. It is not: all the other optima form a single structurally different matching orbit. The resulting explicit extremizer set supports further questions about the geometry and reconfiguration of optimal transversals, distinct from computing the scalar minimum again.

The dated certificate retains the supplied scientific assessment, sources and limitations.
