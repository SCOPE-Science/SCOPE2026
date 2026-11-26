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

On exactly the listed 18 edges, simultaneous majority with unchanged ties defines a deterministic successor for each of the 2048 labelled states. The suffix starting at the first occurrence of the first repeated state is the entire least-period orbit; its start index is the least entry time. The independent fresh trajectory census reproduced 20 fixed states and 61 unordered two-cycles, the full orbit-level basin spectrum and all time-by-period counts. In particular the 48 depth-six starts all fix, and exhaustive checks gave F^8=F^6 but not F^7=F^5. The graph action commutes with the update because adjacency and current-bit ties are invariant under relabelling; filtering all degree-preserving vertex permutations by edge preservation exhausts automorphisms. The 12 surviving permutations give the reported period/class-size/basin-size signatures, with six spatial fixed classes and eleven two-cycle classes. Replay: python /workspace/branches/cef202a4-d94b-485b-a7fd-71a970bad7f4/fresh_majority_check.py; recorded fresh output fresh_majority_check.json in the same directory. This is exact finite enumeration, not a formal proof checker or a theorem on other graphs.

## originality

PASS

The new claim is the joint clock, orbit-level basin and symmetry census on the explicit Herschel graph, not the general eventual period bound. The closest distinct published records match either the graph or the majority rule and several output statistics, but not both. The Resultary exact hit is this record itself.

## value

PASS

The Herschel graph is a canonical small non-Hamiltonian polyhedral graph with both odd- and even-degree update sites. A reproducible complete benchmark identifies which periods attract which starts, distinguishes maximum delay from orbit lengths, and detects that sharp delays occur only in fixed-point basins. Neither the universal period bound nor another graph's isolated counts supply this information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
