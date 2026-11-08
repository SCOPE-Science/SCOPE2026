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

# Executable verification and its limits

The accompanying `verify_net_rips.py` has no dependencies beyond the Python standard library. Execute it with `python verify_net_rips.py` from the directory containing the file. Its expected exact stdout is in `verification_output.txt` and ends with `AFFINE_NET_SCALE3_CHECKS_OK`.

The verifier constructs affine nets over prime fields of orders \(2,3,5,7\), independently computes shortest-path distances for all pairs using breadth-first search, verifies that the 4-distance pairs are exactly the within-part pairs of the claimed complete multipartite graph, and checks graph vertex/edge counts and diameter. At orders 2 and 3 it also constructs **all** simplices of the join and independently computes full mod-two simplicial chain ranks with binary elimination. At order 3 the nonempty face vector is \((18,135,540,1215,1458,729)\), with only one nonzero reduced mod-two Betti number: \(64\) in dimension five.

The code does not enumerate all affine planes or all simplices for larger q; none of those finite checks is offered as proof of the infinite family. The universal proof in RESULT.md uses only affine-plane incidence and exact join topology, including integral homotopy and torsion-free consequences. The possible presence of equivalent work in unindexed literature is not resolved by computational verification. Independent mathematical validation has not been performed.
