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

Execute `python3 verify.py` in a directory containing the embedded standalone verifier; it requires only Python 3's standard library. `verification_output.txt` records a successful execution. The verifier enumerates the exact labelled Petersen graph and its line graph, all 180 nonempty neighborhood simplices, the 74-pair acyclic discrete Morse matching, the thirty-vertex/sixty-edge bipartite double-cover graph, an integral 31-generator fundamental-cycle basis, two integral 31-by-31 action matrices, and the 31-by-62 relation matrix. Its integer Euclidean Smith routine returns twenty-nine unit factors and two factors of two; no floating-point methods are used. It checks the full directed Hasse-graph acyclicity and repeats the homological character calculation in a separate signed-simplicial Lefschetz computation for all 120 group elements.

The equivariant nerve equivalence is a mathematical lemma justified by the explicit invariant cover by left stars: each nonempty multiple intersection is a single right vertex, the nerve is exactly the neighborhood complex, and the group permutes stars. The code checks the combinatorial hypothesis rather than supplying a machine proof of the general nerve theorem. The Smith computation is reproducible from exact graph data. Human mathematical review of the argument and separate external originality verification have not been performed.
