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

The source `verify_transfer.py` reconstructs all six- and seven-step column-pair graphs, their recurrent strongly connected components, finite closed-walk reachability tests, and the common-root return certificate. It checks the six sample trace values with ordinary integer path counting. The reported counts are for labelled rings.

The independently implemented `verify_direct.cpp` iterates the Rule 110 map directly for all initial binary words of lengths 3 through 20. It checks that all sixth-return configurations are already fixed by the second or third iterate and checks all seventh-return populations against the transfer results. The outputs are in `transfer_output.txt` and `direct_output.txt`.

The exact proof of the infinite-size statement is the finite transfer-graph equivalence plus its exhaustive strongly connected component/closed-walk certificate and common-vertex 9-step concatenation argument. The bounded direct enumeration is a supplementary test only. Neither output establishes historical novelty or independent mathematical certification.
