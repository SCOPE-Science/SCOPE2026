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

The frozen claim is mathematically correct. Independent Floyd–Warshall distances gave diameter five and the antipodal distance-complement identity. For each of all 190 pairs the witness locus was exactly two whole antipodal pairs at distances 1–4 and empty at distance 5. Marking each superset of {u,v} union W(u,v) in the omitted set gives exactly the same bad masks as omitting an antipodal pair, over all 2^20 choices. This recovers 59,049 allowed sets with polynomial (2z+z²)^10. In a separate part of the replay, backtracking over distance-preserving injections gave all 120 automorphisms (graph automorphisms are exactly the distance-preserving permutations). Partitioning the 1024 transversals under their images yielded frequencies 2,4,2,10,2 at sizes 12,20,40,60,120. The repaired Finding asserts only that exact profile; its orders 10,6,3,2,1 follow by orbit–stabilizer. The cube and absence of slides are correct background corollaries, since a one-token replacement flips exactly one pair choice and that pair has distance five.

## originality

PASS

Original originality decision: FAIL. The frozen claim presents the antipodal classification as distinct from prior resolving work, but the earlier witness-locus table directly implies it, the polynomial and the reconfiguration deductions. Moreover Palmer and Robinson counted exactly these same 20 orbits in 1984 under their self-dual coloring formulation. This is shown prior coverage, not failed retrieval. The repaired claim credits both and restricts the novel assertion to the distribution of sizes of the already known 20 orbits (equivalently, of stabilizer orders). No matching size profile or covering theorem for it was verified. The cited single-element cycle index gives total orbit counts but does not give simultaneous-fix or stabilizer-size statistics. This PASS is for the actual replacement only.

## value

PASS

The narrower result distinguishes strongly symmetric and asymmetric configurations on the natural full orbit space of minimum equalizers. For example, 240 of 1024 labeled choices have trivial stabilizer while 24 have stabilizer order ten, facts not read off from the known tally of 20 equivalence classes. The size profile is useful when converting counts or sampling weights between labeled configurations and symmetry classes. This is a motivated exact invariant of a canonical finite symmetry action; the already-covered classification, counts and cube observations are not used to justify novelty or value of the repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
