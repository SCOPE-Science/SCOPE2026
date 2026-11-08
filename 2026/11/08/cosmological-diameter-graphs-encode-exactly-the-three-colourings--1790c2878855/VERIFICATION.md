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

# Reproducibility and boundaries

The source embedding uses one standard orthonormal axis for every graph node and every graph edge, with the three vectors \(t_f\), \(a_{f,u}\), and \(a_{f,v}\) per edge as defined in `RESULT.md`. The theorem is proved without a computer: inner products take values \(-1,0,1\), diameter-pair count is a direct incidence sum, and two explicit inverse colour maps prove the correspondence. The four-clique argument is an exact Gram identity. The NP-completeness corollary uses the standard graph three-colouring hardness theorem and the explicit polynomial-size point list.

Run `python3 verify.py` with Python 3, no external dependencies. The checker generates all 771 connected labelled simple graphs on two through five nodes, tests every vertex pair's integer squared Euclidean distance, checks that squared-distance-eight adjacency is exactly the sign-incidence characterization, verifies the exact edge-count identity, and checks absence of four-cliques. It additionally compares exhaustive backtracking counts of proper labelled three-colourings of the two graphs for all connected graphs on at most four source nodes. Successful execution prints `PASS: 2627773 assertions for 771 connected labeled graphs, 2 <= n <= 5.`

Exact finite checks do not prove the statement for unbounded graph order; the unrestricted proof appears in `RESULT.md`. There has been no independent mathematical validation. Originality searches do not guarantee global priority, and projective or nonorthogonal-coordinate realizations are outside scope.
