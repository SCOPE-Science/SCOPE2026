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

For classical s∈{-1,0,1} on GP(10,2) with J>0, H/J=∑edges s_us_v+d∑s_v², an exact min-plus variable-elimination over a bounded 7-variable separator computes all 21 occupancy minima and degeneracies, preserving ties through integer counts. Independent implementation reproduced the entire e(q) vector (0,0,-1,-2,-3,-4,-5,-6,-7,-8,-10,-11,-12,-13,-15,-15,-16,-16,-17,-17,-18); its lower convex hull has vertices (0,0),(14,-15),(20,-18), with q=16,18 on final face. Thus E0/J=min{0,-15+14d,-18+20d} for EVERY d∈R. Equality at d=1/2 includes Q=14,16,18,20 with counts 40,390,600,250 (total 1280); d=15/14 includes Q=0,14 (counts1,40). Active plateau Q=14 (six vacancies), exactly 40 states. Exact DP proof covers all 3^20 states implicitly, not just Monte Carlo.

## originality

PASS

The published Ising dodecahedron full text describes spin-1/2 binary classical configurations and transverse-field quantum fluctuations (250 fully occupied minima), not the three-state classical Blume–Capel model with D sum s² and occupancy-sector convex hull. Other known spin-one field phase diagrams use different graphs, and the related icosahedral/truncated tetrahedral records do not imply the 20-site dodecahedral counts. No inspected source covered 14-active plateau and (14,16,18,20) boundary count.

## value

PASS

The natural twenty-vertex dodecahedral frustrated-spin model acquires a nontrivial exactly six-vacancy optimal plateau, with sharp crystal-field thresholds and striking four-sector degeneracy at D/J=1/2. Complete integer ground-state sector minima and counts supply reproducible physical finite-cluster reference data, not arbitrary small random graph recomputation; a future researcher comparing frustrated spin-one clusters can use this exact benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
