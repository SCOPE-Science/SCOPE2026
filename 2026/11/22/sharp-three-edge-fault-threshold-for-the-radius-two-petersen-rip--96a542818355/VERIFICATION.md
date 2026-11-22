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

# Finite verification

Run `python3 check_petersen_faults.py` in Python 3 with the standard library; it needs no external files. The included `verification_output.txt` is the verbatim output of the package version of that script.

The verifier regenerates the 10 vertices and 15 graph edges, 120 concrete ground-set permutations, each triple-deletion orbit, breadth-first-search graph distances and all nonempty Vietoris–Rips faces. It verifies cone vertices in 121 smaller-fault cases; all nine disjoint orbit cardinalities totaling 455; exactly ten disconnecting triples; and every matched cover pair, directed Hasse edge and acyclic topological ordering for the eight connected orbit representatives. It independently checks mod-two boundary ranks.

The actual homotopy classification uses the integer-valid acyclic discrete-Morse theorem to pass from critical cells to a CW model with one zero-cell and zero, one or four two-cells and no other cells. The code makes no claims about infinite graph families, other radii or homology maps across deletions. There has been no independent audit or external validation.
