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

# Mathematical verification

The included `verify.py` uses exact integer and polynomial arithmetic. Install the pinned dependency in `requirements.txt`, then run `python3 verify.py`.

It reconstructs the sixteen exceptional-curve vertices and forty intersections, the incidence matrix and an integral 25-cycle basis. The seven signed Frobenius matrices are checked by exact chain identities and finite-order identities. For each of the seven permutations, it computes a full symbolic diagonal by **only unimodular elementary operations over \(\mathbb Z[u]\)** and verifies the chain of diagonal factors. As an independent numerical cross-check, it computes integer Smith forms after \(u=2,3,5,8,11\) and compares every invariant factor with the symbolic prediction. The expected final line is `QUARTIC_DEL_PEZZO_ALL_SEVEN_PICARD_POINT_GROUPS_OK`.

The symbolic polynomial operations together with the normalization and torus-character-lattice theorem justify the infinite family; the finite specializations do not alone prove an infinite-field statement. The verifier does not independently establish historical originality, realize every Frobenius type over every small field, or classify nonpermutation signed-Weyl actions.

Self-review: passed. Independent audit: not yet performed.
