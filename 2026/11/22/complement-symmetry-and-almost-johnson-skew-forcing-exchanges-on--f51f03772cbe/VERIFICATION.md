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

An independent reproduction (branches/reproduce-exchanges.py clebsch; output in branches/reproduce-exchanges.out) used dynamic programming on all 65,536 white sets: the empty set succeeds, and a nonempty white set succeeds iff an open neighborhood hits it in a singleton whose deletion gives a previously successful set. The deleted bit decreases the index, so this evaluates the first-force recurrence exactly with no restriction on the forcing vertex's color. It reproduces every polynomial coefficient, the 6,490 optima, complement closure, and the stated stalled exchanges for the matroid counterexample. For automorphisms an image of 0 and a bijection of its five neighbors prescribe the other ten images via their pairs of shared neighbors; the reconstruction verifies all 1,920 adjacency-preserving permutations and the nine orbits. Pairwise XOR population two constructs precisely the legal jumps. Full unweighted shortest-path searches from all 6,490 sources, without relying on the orbit reduction, return 116,320 edges, the four asserted degree multiplicities, all eccentricities eight, and exactly 9,120 unordered pairs at Johnson distance plus one and none farther. The representative counts and the distance-three example also agree.

## originality

PASS

The result is the census and metric for skew forcing on the five-regular Clebsch graph, not for ordinary forcing, matching flips or the ten-regular graph sometimes called Clebsch. No checked prior result supplies these data or implies the exchange-distance bound and detour count.

## value

PASS

On a canonical strongly regular graph the minimum family is invariant under complementation but not a matroid basis family. Its exchanges are nevertheless connected and uniformly within one step of the ambient Johnson lower bound, with a complete count of genuine detours. This tests specific structural expectations about mobility in skew forcing and supplies a reusable exact benchmark beyond the forcing number alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
