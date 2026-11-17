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

The finite verification script `verify.py` independently constructs the four-edge subdivision, the induced permutation on every added vertex, and the orbit-conflict graphs for invariant independent sets. It computes the signed invariant-independent-set sums by a recursive independence-polynomial evaluation and compares them with the predicted edge-cycle parity, without substituting the local proof's factorization as a computational axiom.

Actual run: all graph automorphisms of labeled simple graphs on at most four vertices and with at most four edges, plus six cases on five or six vertices (including complete graphs, a five-cycle, a path reflection, and exchanged triangles). 251 cases passed, with 70 cases directly reversing an existing edge. The exact command is `python verify.py`; the output appears in `verifier_output.txt`.

Proof checks: the edge-orbit local partition sums are \(-1\) or \(0\) in both inversion and non-inversion cases; the augmented Lefschetz sign is the negative of the signed invariant-independent-set sum; the previously published nonequivariant suspension theorem provides the homological degree shift; equality of rational characters is then sufficient to identify representations.

Limitations: finite testing does not certify the universal proof and does not test all graphs; rational representation isomorphisms do not assert integral lattice isomorphisms or equivariant homotopy equivalence. No independent audit has been performed.
