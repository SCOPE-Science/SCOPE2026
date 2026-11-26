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

The frozen numerical results are correct. The repaired RESULT and SLOGAN restrict the new census to T(6) and use the Kneser numbers as prior comparison data. In an independent reproduction (branches/reproduce-majority-basins.py; matching .out), the votes for site ij were calculated from the root degrees d_i,d_j, the incumbent x_ij and the total number m of selected edges: closed-neighborhood vote totals d_i+d_j−x_ij for T(6) and m−d_i−d_j+2x_ij for KG(6,2), with thresholds 5 and 4. Indegree peeling in the full functional digraph removes precisely the transient states; remaining cycles of length one or two are labeled individually and the reversed peeling order gives the exact entrance depths and basin totals. All 32,768 states for each graph were included. The first-entry tables, orbit-basin spectra, both consensus basin sizes per graph, and the two sharpness trajectories reproduce exactly. In the repaired text, the root-degree formula and the iterate-equality and orbit-key enumeration are valid, and the comparison uses 9120/1800=76/15 with the same initial-state measure.

## originality

PASS

PASS applies only to the repaired triangular-graph transient and full basin census with a credited comparison. The frozen two-census originality assessment fails: the complete KG(6,2) slice, including its transient histogram, basin sizes and sharp depth, is directly established in an earlier same-rule record omitted from the original comparison. The repair removes it from the new finding, names that source as the baseline and does not claim the recurrent-state counts as a standalone advance. After checking the nearer line-graph and Johnson-graph result statements and the published Kneser comparison, no checked source supplies the individual transient basin sizes or full entry census for T(6).

## value

PASS

The surviving claim is not a re-count of the published Kneser case or of known recurrent states. It determines the fate of every initial state on the canonical line graph of K6 and distinguishes the two complementary dynamics at the level of transient depth, consensus and oscillatory attraction, rather than only recurrent membership. This is an exact finite benchmark for a natural comparison: equal sharp depth does not predict even the fraction of configurations that end up oscillating.

The dated certificate retains the supplied scientific assessment, sources and limitations.
