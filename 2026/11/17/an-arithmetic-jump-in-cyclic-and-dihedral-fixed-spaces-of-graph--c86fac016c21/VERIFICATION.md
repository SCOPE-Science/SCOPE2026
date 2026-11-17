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

The included `verify.py` is a standalone Python 3 standard-library checker. Running `python3 verify.py` reproduces `verification_output.txt` exactly.

## Checks actually executed
All cyclic distance-orbit subsets for \(4\le n\le22\) were tested against the graph's direct 3-vertex-connectivity predicate, which independently checks connectivity after deleting zero, one, or two vertices. All ordinary simplicial homology Betti numbers with \(\mathbb F_2\) coefficients for \(4\le n\le20\) were computed by boundary-matrix ranks. Every cyclic edge-orbit was checked to be preserved by reflection for \(4\le n\le30\). The prime-cover nerve supports were exhaustively checked at \(n=6,10,12,15,30,42,60,105,210\).

## Boundaries
The computer checks do not prove the infinitely many cases; that proof is the connectivity theorem and prime-cover argument in `RESULT.md`. The computations test ordinary mod-two homology, not arbitrary integral torsion. The geometric fixed-space model is established in the proof, not assumed from finite fixed-simplex enumeration. No external or independent mathematical audit has been performed.
