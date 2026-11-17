---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For each r>=1 and the precise graph K1 joined to r disjoint K3 blades, the hub-zero local triangle occupation counts 0,1,2,3 update to 0,0,1,3 and hub-one counts update to 0,2,3,3 under strict open-neighbor majority. Counting (z,o,p,q) and hub flips via K=3o+p+2q,L=3o+q,U=3o+2q yields the complete ordered decision table for first entry times and period, with first periodic entry at most four. The proof tracks the orientation of a two-occupied blade under alternating hub flips, ensuring an actual spatial two-cycle, not merely an occupation-cycle. It derives sharp maximum times 1 at r=1, 3 at r=2, 4 at r>=3, all multinomial fixed/two-cycle/basin counts and c_r/5^r -> 1 via a Hoeffding bound. Independent full-state enumeration r=1..4 confirms all first-entry/period categories and total populations; it is not the all-r proof.

## originality

PASS

PASS on the complete deterministic windmill first-entry/period and basin census. Goles–Olivos gives only the general period-at-most-two theorem; later majority dynamics on triangular books, wheels, pineapple, barbells and trees use different graph architectures and do not imply the sharp windmill four-step cutoff or its multinomial basin weights. A direct specialized predecessor for K4 bouquets remains possible in older unindexed dynamics literature.

## value

PASS

Exact transient thresholds and full oscillator basin sizes on a family with arbitrarily many triangle blades are natural discrete dynamical invariants. The distinction between immediate periodic orbits and their full basins, plus a sharp universal entry-time bound, goes substantially beyond the textbook period-two fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
