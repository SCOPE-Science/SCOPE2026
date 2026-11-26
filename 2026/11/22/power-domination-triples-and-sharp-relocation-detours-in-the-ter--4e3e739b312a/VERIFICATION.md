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

Independently reproduced the entire finite claim with python3 /workspace/branches/replay_4.py, without executing the frozen programs. Coordinate lines give the six neighbors of each word (81 edges). Synchronous white-set reduction gives the same closure as legal successive forces: a force enabled at a smaller observed set remains enabled at a larger one unless its target is already observed. All sets of size at most two fail; exhausting the 2925 triples finds three successful signatures with counts 324, 648, 324. Orbits were independently keyed by the coordinate equality partitions on the three rows, sorted over coordinate permutations and minimized over a common row permutation. Such a key is complete since any matching coordinate partitions can be sent to each other by independent symbol permutations. All ten orbit sizes and complete forcing-round histories agree with orbit_table.json. Joining the buckets of triples containing a common retained pair gives exactly the jump edges; keeping only exchanges along a coordinate line gives the slide edges. Bitset layer searches from all 1296 states reach every state and reproduce all six orbit-wise sphere lists. Jump eccentricities are 3,4,3 by signature, slide eccentricity is 6 throughout, and only type (2,2,3) has a unique distance-four partner. Symmetry of distance makes that partner relation an involution. Intersecting the two move-rule spheres for the same endpoints over all 839160 unordered distinct pairs reproduces both distance distributions and gap counts 103356, 370008, 324648, 41148. As a witness, {000,001,112} and {000,120,222} have jump distance 2 and slide distance 5. The conclusion concerns this labeled finite graph only.

## originality

PASS

The distinct supported finding is the exact minimum power-dominating triple census on the ternary Hamming three-cube and its joint move-rule metric. The strongest checked Hamming realization theorem studies a different base graph, and the exact same-base near-match uses a different domination condition. Bounded searches found no covering classification; no historical priority or inference from same-day dates is asserted.

## value

PASS

This natural nonbinary Cartesian monitoring graph gives a complete benchmark comparing the same feasible placements under local and unrestricted relocation. Neither the two diameters nor the marginal distance histograms determine the sharp three-move cost on matched endpoints; the exact attaining count and antipodal structure are independently useful. The value is the exhaustive, interpretable comparison at this specified cube, not an extrapolation to other Hamming graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
