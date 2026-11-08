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

# Reproduction

The full self-contained Python and C++ source programs and their corresponding reference outputs are included as sibling files. Run `python3 verify_even5.py > even5_output.json`; compile the C++ program using `g++ -std=c++17 -O2 -Wall -Wextra verify_folded4.cpp -o verify_folded4`, then execute `./verify_folded4 > folded4_output.txt`. Both programs were executed from these final file paths, and their outputs matched the embedded output files byte-for-byte.

Both exhaust all feasible five-sets and their exact one-for-one moves. The Python program also enumerates every smaller cardinality; the C++ program independently enumerates all 65,536 masks. All 416 shortest-path BFS searches complete in each move graph. All results are exact finite facts for the defined host graph; independent scholarly audit is not performed.
