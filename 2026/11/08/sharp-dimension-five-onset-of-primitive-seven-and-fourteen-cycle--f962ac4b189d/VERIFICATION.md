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

The quotient transition certificates are the two trace files under `data/`; each contains the full ordered orbit in the stated eighteen-vertex labelling. `tools/check_witnesses.py` checked all 21 directed transitions and their direct lifts to the five- and six-dimensional Boolean cubes. The same script exhaustively classified the configurations of cubes of dimensions one, two and three.

The two dimension-four programs use different state transition algorithms and different functional-graph enumeration procedures. `tools/q4_dfs.c` uses precomputed half-cube transition tables and a forward depth-first walk; `tools/q4_peel.c` explicitly decodes every trit and uses indegree peeling. Their complete outputs match and include the count of every occupied first-entry/period class. Each independent execution reached all 43,046,721 states. All checks completed. Neither finite computation establishes an untested assertion about all higher dimensions; that conclusion follows from the proven quotient-lift identity.

The exact file contents can be verified by rerunning the commands in `RESULT.md`. No external certification or independent audit is asserted.
