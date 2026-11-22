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

# Reproduction and proof boundary

Run `python check_ipco.py` and `python check_endpoint.py` with Python 3.10 or later. They use only Python's standard library. The exact saved stdout from these runs is `verification_output.txt`.

`check_ipco.py` enumerates all distinct endpoint pairs and all orders of coordinate changes for the listed small Cartesian products of cliques, computes maximum antichains directly, compares the results to the asserted global formula, and solves an independent rooted-geodesic set cover for the extremal examples of dimensions at most three. `check_endpoint.py` computes the exact maximum over all geodesic orders for every endpoint pair in five selected instances and checks the terminal-conditioned identity.

The proof is independent of finite exhaustive tests. Its nonstandard critical steps are: the exact rooted-reachability condition, equivalence of chains and rooted paths, the two-type characterization of incomparability on a geodesic, and the constructive saturation of the segment-charging upper bound. An arbitrary-dimensional assertion cannot be certified by checking finitely many graphs. No randomized or unverified numeric certificates are used.

Scientific limitations: the theorem is restricted to genuinely mixed products of complete graphs and maximization over paths with fixed endpoints. It neither computes the minimum covering number for each *individual* ordering in closed form nor settles the problem for noncomplete factors.
