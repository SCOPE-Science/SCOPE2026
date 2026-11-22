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

The stated result is a complete finite-domain classification, not an extrapolation from a selected sample. Both reproducibility programs explicitly cover every one of the \(3^{11}=177147\) starting colorings on the independently specified Herschel graph.

Run `python3 verification/exhaustive_graph.py`. This uses a complete successor array and directed indegree peeling, then reverse-order transient depths. Its final marker is `HERSCHEL_EXHAUSTIVE_OK`; its output includes all 27 GHM and 21 CCA transient-time/period cells, period-basin totals, and recurrent populations.

Independently run `g++ -O2 -std=c++17 verification/independent_trajectories.cpp -o verify && ./verify`. This uses separately implemented local update rules and Floyd cycle detection from each initial state. Its final marker is `HERSCHEL_FLOYD_OK`. Its full histogram matches the first program's numbers cell for cell. Both programs check the pointwise equality of eventual periods, recurrent-state inclusion, matching transitions on the GHM recurrent set, and sharp maxima.

The two completed output files are included under `verification/`. The whole finite state space is exhausted, but no wider graph-family statement or external independent validation is asserted. The graph's eleven-vertex, eighteen-edge adjacency is independently readable in the cited University of Washington diagram.
