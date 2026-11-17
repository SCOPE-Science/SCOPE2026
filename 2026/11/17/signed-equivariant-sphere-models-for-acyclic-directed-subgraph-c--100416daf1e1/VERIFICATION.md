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
# Verification

Run the standalone Python scripts `python verify_signed_dag.py` and `python verify_signed_dag_general.py` in the same directory with Python 3 and no third-party packages. `verification_output.txt` records both actual outputs, including `SIGNED_DAG_FINITE_FIXED_HOMOLOGY_CHECKS_PASS` and `SIGNED_DAG_GENERAL_DIRECTED_CHECKS_PASS`.

The first script checks 93 complete-bidirected-graph/signed-subgroup examples for \(2\le n\le6\). It explicitly forms geometric fixed-face orbit complexes, enumerates valid acyclic unions, and computes reduced mod-two simplicial homology. The second independently constructs strongly connected components and signed stabilizer actions for 491 directed-graph/group pairs, calculating the predicted fixed real-vector-space dimension by rational row reduction, including 181 cases with inter-component arcs and 310 without. No test asserts exhaustiveness of all graphs or all subgroups beyond the ranges actually enumerated.

The general correctness and integral homotopy conclusions require the separate convex-cover/nerve proof; mod-two ranks cannot substitute for an integral or equivariant homotopy argument. No independent mathematical audit has been performed.
