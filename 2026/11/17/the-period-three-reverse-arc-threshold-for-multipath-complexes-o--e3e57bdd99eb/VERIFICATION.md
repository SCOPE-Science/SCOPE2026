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

Run `python verify.py` using Python 3 with only the standard library. The script reconstructs directed edge sets, rejects all directed cycles (including length-two cycles) and all indegree/outdegree collisions, verifies the factorized join with one maximal forward facet removed, checks the explicit relative matching and acyclicity by topological sorting of the gradient graph, and computes reduced Euler characteristics and modular boundary ranks. Exact recorded results are in `verification_output.txt`.

For \(k=2,3,4\) the face counts are \(80,728,6560\), including the empty face; the predicted counts are \(9^k-1\). Reduced homology over characteristic two is rank one in each of degrees \(k-1\) and \(3k-2\); characteristic three was also tested for \(k=2,3\). These finite calculations are checks, not an infinite proof or an integral torsion test. The main proof supplies the integral and homotopy information using relative discrete Morse theory, an explicit simplicial retraction, and the pair long exact sequence. The full classification is subject to independent mathematical audit.
