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

# Reproducibility checks

Run `python3 verify.py` using Python 3.8 or newer (standard library only). Recorded output: `verification_output.txt`.

For \(p=5,7,11\), the code exhaustively verifies the cross-polytope-face equivalence, the graph-distance criterion, the cyclic action, primitive equatorial weights, and the compatible mapping-cone chain identities. It computes reduced homology ranks of the algebraic cone model over four prime fields. The outputs agree with the universal formula: over \(\mathbb F_2\) ranks one in every degree \(1,\ldots,p-1\), and over odd prime fields zero in all positive degrees.

The infinite-family homeomorphism, integral torsion calculation, \(\pi_1\) and \(\pi_2\) are proved in `RESULT.md` via covering space theory and the lens-space transfer, not inferred from finite code. The cellular model code is corroboration, not a separately certified equivariant triangulation. Independent validation has not been performed.
