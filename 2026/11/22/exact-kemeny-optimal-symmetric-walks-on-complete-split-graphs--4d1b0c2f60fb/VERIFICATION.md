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

Run `python3 verify_split.py` using Python 3 and its standard library. In the recorded package the checker completed **168,156 exact-rational assertions**. The checker constructs independently a symmetric stochastic transition matrix for small class sizes and inverts the modified Laplacian with rational Gaussian elimination to calculate the pseudoinverse trace, then compares the theorem's closed forms, support loss, feasibility, and endpoint derivative inequalities. It also checks finite rational candidate grids and size grids.

The analytic proof—not this finite sample—establishes the theorem for **all integers** \(p,q\ge2\), every irreducible symmetric admissible Markov kernel, and every allowed boundary value. The nonstandard steps to verify directly are the strict trace-inverse convexity, four-subspace Laplacian decomposition, clique-row saturation, and the two elementary endpoint-derivative inequalities. No independent mathematical audit has been performed, and literature priority is subject to uninspected specialist sources.
