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

The theorem is proved symbolically for every algebraically closed field of characteristic \(3\); the executable provides a finite-field cross-check, not a substitute for that proof.

Run `python3 verify_as_genus6_cartier.py` in the same directory. The script needs only Python's standard library. It independently constructs the semilinear Cartier matrix by reducing the differential monomials through the Artin–Schreier relation and separately constructs the predicted matrix from the formula. Exact inverses and arithmetic are implemented in \(\mathbb F_9\), with \(t^2+1\) irreducible over \(\mathbb F_3\). It checks every one of \(729\) triples and the Frobenius-twisted Cartier iterates. The observed counts are \(81\) exceptional profiles \((6,2,1,0)\) and \(648\) generic profiles \((6,3,1,0)\), with successful marker `AS_GENUS6_CH3_CARTIER_REPLAY_PASS`.

The argument for all parameters uses the complete valuation-derived differential basis, the Cartier power-selection identity, and a direct image-rank computation. These independently justify the universal claim, while finite replay checks the displayed matrix and exact counts only over \(\mathbb F_9\). No independent audit has been performed.
