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

# Computation record
Run the accompanying standalone Python 3 file with `python3 verify.py`. It uses only the standard library. For every square-zero rank and isolated-vertex count with between one and six total vertices, it generates all partial injections, checks commutation by actual composition, checks nilpotence by directed-cycle detection, and compares the full rank arrays with the two formulas. Fifteen cases passed in the recorded run (`verification_output.txt`), with marker `ALL_ROOK_CENTRALIZER_NILPOTENT_RANK_CHECKS_PASS`. In particular, the \((r,s)=(2,2)\) case tests all ranks on six vertices. These exhaustive finite examples do not constitute an infinite-family proof; the structural decomposition and signed cycle sieve in the main result do.
