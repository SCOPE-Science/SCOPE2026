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

# Verification, evidence and limits

Execute `python check.py` using Python 3 and NumPy. The recorded completed execution returned `PASS 92 network, orbit, spectrum, optimum and edge checks`. Checks cover stars, complete bipartite graphs, even cycles and hypercubes, including direct two-step state updates, direct Laplacian eigenvalues, exact Jacobian eigenvalue formulas, sharp normal-attractor/repeller boundaries, unique spectral optimization and endpoint expansions. The script is included in this result as executable text; no output logs or certificates from previous findings are used.

The all-graph proof uses (i) the invariant class-constant subsystem, (ii) Perron–Frobenius for the graph's top Laplacian eigenvalue, (iii) the common return Jacobian and its spectrum, (iv) convex minimax optimization, and (v) Taylor expansions. The finite checks are not a substitute for those arguments.

The proof does not establish global attraction, characterize arbitrary periodic orbits, classify non-biregular graphs or determine transverse nonlinear stability at the all-unit endpoint. Scientific review was conducted in the same review channel; independent audit has not been performed.
