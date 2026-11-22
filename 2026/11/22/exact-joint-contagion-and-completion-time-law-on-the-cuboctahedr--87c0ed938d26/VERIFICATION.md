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

# Exact reproducibility checks

`python3 verify_dynamics.py` enumerates every initial state of a twelve-vertex graph and applies the synchronous three-neighbor rule until stabilization; each successful state contributes its exact first full-activation time.

`python3 verify_paths.py` independently reconstructs the ordinary cube's twelve edges, checks every subset for maximum degree at most two and absence of cycles via a union-find method, enumerates all Hamiltonian paths by recursive vertex paths, and groups the 72 optimum edge sets under 48 cube symmetries.

Both programs passed with the reported tables. The analytic leaf-pruning/line-graph reductions are stated in `RESULT.md`; the programs certify only finite enumeration, not historical novelty, results on arbitrary graphs, or independent audit.
