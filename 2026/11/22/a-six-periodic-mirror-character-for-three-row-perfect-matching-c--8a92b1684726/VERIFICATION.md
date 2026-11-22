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

# Reproducible verification

Run `python3 CHECK.py` in the same directory; it requires only the Python standard library (Python 3.9+).

The checker reconstructs the allowable three-row domino column transitions from three-bit boundary masks, determinizes compulsory horizontal-edge choices, reconstructs exactly seven reachable states, and confirms the displayed transition matrix and terminal mask. It verifies the exact integer whole-matrix identity \(M^8=M^2\); together with the four initial values this verifies the all-order periodic fixed-face formula. It also independently enumerates all full perfect matchings, constructs full edge involutions and counts all invariant face selections for half-widths 1 through 6, obtaining the signed values \(0,-1,1,0,-1,1\).

The independent enumeration is a finite consistency test, not the proof of periodicity. The matrix identity and finite-state transfer definition are the proof of the infinite statement. The cited all-order nonequivariant homotopy classification and the standard simplicial Lefschetz/finite-quotient arguments are mathematical inputs, not independently certified here. No external audit or independent validation has been performed.
