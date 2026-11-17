---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Strict-source distance separation and radius-interval covering for length-k schedules imply exactly two repeated incidences because k²-(k²-2)=2. Anchoring unique radius-zero center and clockwise ordering radii yields deficits t_j>=0 summing two, endpoints t0,t_(k-1)<=1 and interior <=2; all such configurations obey center distance constraints via path gap estimates. Adjacent source slide transfers a deficit unit between neighboring gaps, preserving circular radius order. On fixed order the two-particle graph connects, and one full circulation shifts anchor one step, so each order is a component. Counting gap vectors gives (k²+k-4)/2, degrees 2/3/4 and edges formula. Fresh C++ brute-force direct graph enumeration k=3,4,5 reproduced totals 56/672/7176, 2/6/24 components and degree histograms and edges, without using gap encoding.

## originality

PASS

Earlier 2026/11/08 source-slide theorem covers k² (isolated) and k²-1 (single mobile defect, each component a cycle), not k²-2. An older arbitrary-source-replacement reconfiguration theorem covers k²/k²-1 and a different move. The independent two-particle defect collisions, capacity-two interior sites, mixed degrees and new state census are not supplied by either prior; graph-burning number is credited to Bonato et al.

## value

PASS

Two units of coverage slack are the first case with interacting mobility defects and mixed vertex degrees. Exact components and degree census form a natural complete extremal reconfiguration classification of schedules near maximal burnable cycle size; it is not an unmotivated arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
