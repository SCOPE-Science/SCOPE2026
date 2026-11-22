---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducible checks

Place `verify_power_domination.py`, `verify_structural.py`, and `dyck_isomorphism.json` in the same directory. Python 3.9 or later is sufficient; neither checker imports third-party packages.

Run `python verify_power_domination.py` and `python verify_structural.py`. Both completed successfully with the supplied certificate. The first reconstructs Shrikhande and rook adjacency, confirms the strongly regular pair parameters, exhausts all Shrikhande subsets of size one or two and all rook subsets of sizes one to three, checks the complete optimum relocation graphs and their 1,128 unordered shortest-path pairs, and verifies that all 48 cubic intermediary edges map bijectively to the LCF Dyck edge list. The second checks the three displacement orbits with different coordinate-set logic, re-derives all local triangles, verifies the line-graph slide condition for every pair of distinct optimal configurations, checks every source distance and independently repeats the LCF edge-certificate comparison.

Expected optimum counts: Shrikhande, size two with 48 configurations; rook, size three with 416 configurations. Expected exchange edges 240 and slide edges 96, both with one component. Expected distance histograms: jumps `(1: 240, 2: 696, 3: 192)` and slides `(1: 96, 2: 192, 3: 336, 4: 384, 5: 120)`. All 32 cubic intermediary vertices, all 48 cubic edges, and the complete 32-entry Dyck mapping are checked, not merely displayed.

All verification is finite and graph-specific. The scripts are reproducibility tools, not a separate human or external mathematical audit, and no unseen graph sizes are certified by the finite computations.
